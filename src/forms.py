from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, ValidationError
from datetime import date

class AddTaskForm(FlaskForm):
    ##id, description, status, added_date, due_date, priority
    description = StringField("Task Description", validators=[DataRequired()])
    status = SelectField("Task Status", validators=[DataRequired()], choices=[('pending', 'pending'), ('done', 'done')])
    due_date = DateField("Due Date", format='%Y-%m-%d', validators=[DataRequired()])
    priority = SelectField("Priority", validators=[DataRequired()], choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high')])
    submit = SubmitField("Add Task")


    def validate_due_date(self, field):
        if field.data < date.today():
            raise ValidationError("Due date cannot be in the past.")
        
class FilterForm(FlaskForm):
    filter_type = SelectField("Filter Type", choices=[('', 'Filter by...'), ('status', 'Status'), ('priority', 'Priority')], validators=[DataRequired()])
    filter_value = SelectField("Filter Value", choices=[('', 'Select Value')], validators=[DataRequired()])
    submit = SubmitField("Filter")

class SortForm(FlaskForm):
    sort_by = SelectField("Sort By", choices=[('', 'Sort by...'), ('due_date', 'Due Date'), ('priority', 'Priority')], validators=[DataRequired()])
    submit = SubmitField("Sort")