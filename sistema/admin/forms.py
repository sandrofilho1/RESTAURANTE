from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    username = StringField('Usuario: ', [validators.Length(min=4, max=20)])
    email = StringField('Email: ', [validators.Length(min=6, max=25)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='As senhas não conferem')
    ])
    confirm = PasswordField('Repita a senha')

class LoginFormulario(Form):
    email = StringField('Email: ', [validators.Length(min=6, max=25)])
    password = PasswordField('New Password', [validators.DataRequired()])