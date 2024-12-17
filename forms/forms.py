from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Имя', validators=[DataRequired()])
    content = TextAreaField('Дата и место рождения', validators=[DataRequired()])
    content1 = TextAreaField('Место жительства', validators=[DataRequired()])
    content2 = TextAreaField('Род занятий и Хобби', validators=[DataRequired()])
    submit = SubmitField('Отправить анкету')
