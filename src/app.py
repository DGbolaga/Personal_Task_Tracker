from flask import Flask, abort, render_template, redirect, url_for, flash, request
from cs50 import SQL
import os
from dotenv import load_dotenv
from forms import AddTaskForm, FilterForm, SortForm
from datetime import datetime

load_dotenv()


# Ensure /data directory exists
os.makedirs('data', exist_ok=True)

db_path = 'data/tasks.db'
if not os.path.exists(db_path):
    open(db_path, 'a').close()  # Creates an empty file

# Create and ensure tasks table exists on app start
db = SQL(f"sqlite:///{db_path}")

db.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        status TEXT DEFAULT 'pending',
        added_date TEXT NOT NULL,
        due_date TEXT,
        priority TEXT DEFAULT 'medium'
    );
""")
print("✅ Database ready.")

# Flask app config
app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Render the homepage with a form to add a new task.
    On form submission, saves the task to the database and redirects to the task list page.
    """
    form = AddTaskForm()
    if form.validate_on_submit():
        current_date = datetime.now().strftime('%Y-%m-%d')
        db.execute(
            'INSERT INTO tasks (description, status, added_date, due_date, priority) VALUES (?, ?, ?, ?, ?)',
            form.description.data.strip(), form.status.data, current_date, form.due_date.data, form.priority.data
        )
        flash("Task successfully added!", "success")
        return redirect(url_for('show_all_tasks'))

    return render_template('index.html', form=form)


@app.route('/tasks', methods=['GET', 'POST'])
def show_all_tasks():
    """
    Display all tasks with optional filtering and sorting.
    Allows users to filter by status or priority and sort by priority, due date, or date added.
    """
    filter_type_choices = {
        'status': [('pending', 'Pending'), ('done', 'Done')],
        'priority': [('high', 'High'), ('medium', 'Medium'), ('low', 'Low')]
    }

    filter_form = FilterForm()
    sort_form = SortForm()
    tasks = db.execute('SELECT * FROM tasks ORDER BY id DESC')  # Default: All tasks, newest first

    if request.method == 'POST':
        if filter_form.filter_type.data in filter_type_choices:
            filter_form.filter_value.choices = filter_type_choices[filter_form.filter_type.data]
        else:
            filter_form.filter_value.choices = []

        if filter_form.submit.data and filter_form.validate_on_submit() and filter_form.filter_value.data:
            selected_filter_type = filter_form.filter_type.data
            selected_filter_value = filter_form.filter_value.data
            tasks = db.execute(
                f'SELECT * FROM tasks WHERE {selected_filter_type} = ? ORDER BY id DESC',
                selected_filter_value
            )
            flash(f"Tasks filtered by {selected_filter_type}: {selected_filter_value}", "info")

        elif sort_form.submit.data and sort_form.validate_on_submit():
            sort_by = sort_form.sort_by.data
            if sort_by == 'priority':
                tasks = db.execute("""
                    SELECT * FROM tasks 
                    ORDER BY CASE priority 
                        WHEN 'high' THEN 1 
                        WHEN 'medium' THEN 2 
                        WHEN 'low' THEN 3 
                    END ASC""")
            else:
                tasks = db.execute(f'SELECT * FROM tasks ORDER BY {sort_by} ASC')
            flash(f"Tasks sorted by {sort_by}", "info")

    else:
        filter_form.filter_value.choices = []

    return render_template('tasks.html', tasks=tasks, filter_form=filter_form, sort_form=sort_form)


@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    """
    Delete a specific task by its ID.
    Redirects to the task list with a success or error message.
    """
    task = db.execute('SELECT * FROM tasks WHERE id = ?', task_id)
    if not task:
        flash("Task not found!", "error")
        return redirect(url_for('show_all_tasks'))

    db.execute('DELETE FROM tasks WHERE id = ?', task_id)
    flash("Task deleted successfully!", "success")
    return redirect(url_for('show_all_tasks'))


@app.route('/toggle_status/<int:task_id>', methods=['POST'])
def toggle_status(task_id):
    """
    Toggle the status of a task between 'pending' and 'done'.
    Redirects to the task list with a status update message.
    """
    task = db.execute('SELECT * FROM tasks WHERE id = ?', task_id)
    if not task:
        flash("Task not found!", "error")
        return redirect(url_for('show_all_tasks'))

    current_status = task[0]['status']
    new_status = 'done' if current_status == 'pending' else 'pending'

    db.execute('UPDATE tasks SET status = ? WHERE id = ?', new_status, task_id)
    flash(f"Task status updated to {new_status}!", "success")
    return redirect(url_for('show_all_tasks'))


@app.route('/clear_filters')
def clear_filters():
    """
    Clear all task filters and redirect to the unfiltered task list.
    """
    flash("Filters cleared!", "info")
    return redirect(url_for('show_all_tasks'))


if __name__ == '__main__':
    app.run(debug=True, port=5001)
