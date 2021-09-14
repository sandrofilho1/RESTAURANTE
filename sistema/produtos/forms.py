from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, BooleanField, TextAreaField, validators


class Addprodutos(Form):
    name = StringField('Nome :', [validators.DataRequired()])
    price = IntegerField('Preço :', [validators.DataRequired()])
    stock = IntegerField('Estoque :', [validators.DataRequired()])
    description = TextAreaField('Descrição :', [validators.DataRequired()])

    image = FileField('Imagem :' , validators=[FileRequired(),FileAllowed(['jpg','jpeg','png'])])