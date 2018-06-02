from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length,Email,NumberRange
class Details(FlaskForm):
    fname=StringField('first name',validators=[DataRequired(),Length(min=2,max=50)])
    lname=StringField('last name',validators=[DataRequired(),Length(min=2,max=50)])
    email=StringField('email',validators=[DataRequired(),Email])
    mobile=StringField('mobile',validators=[DataRequired(),NumberRange(min=0,max=9)])
    company=StringField('company',validators=[DataRequired(),Length(min=2,max=50)])
    position=StringField('position',validators=[DataRequired(),Length(min=2,max=50)])
    submit=SubmitField('proceed')
