from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional


class SampleForm(FlaskForm):
    email = StringField("Email", validators=[Optional(), Email()])
    name = StringField("Sample Name",  validators=[
                       InputRequired(message="Sample Name can't be blank")])
    price = FloatField("Sample Price in USD")
    quantity = IntegerField("How many?")
    is_true = BooleanField("This is either true or false")
