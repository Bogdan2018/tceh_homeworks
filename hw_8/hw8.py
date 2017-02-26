# Задача: реализовать веб-сервер на Flask, который бы реализовывал следующую функциональность.
# Требования:


from flask import Flask, request, jsonify, abort
from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError, PasswordField
import locale
import json

app = Flask(__name__)
app.config.update({
    'SECRET_KEY': 'asdfsggah',
    'DEBUG': True,
    'WTF_CSRF_ENABLED': False
})
PasswordField()


class UserFrom(FlaskForm):
    email = StringField(validators=[
        validators.Email()
    ])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.Length(min=6, max=30)
    ])

    confirm = PasswordField('Repeat Password')
    # accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])


#    По адресу /locales должен возвращаться массив в формате json с тремя локалями: ['ru', 'en', 'it']


@app.route('/locales')
def get_value():
    d = locale.locale_alias
    dict_locale = {}
    keys = ['ru', 'en', 'it']
    for k, v in d.items():
        for i in keys:
            if k == i:
                dict_locale.update({k: v})
                dump_json = json.dumps(dict_locale)
    return dump_json


#    По адресу /sum/<int:first>/<int:second> должен получать в url-адресе два числа, возвращать их сумму


@app.route('/sum/<number_1>/<number_2>')
def number_compare(number_1, number_2):
    sum = int(number_1) + int(number_2)
    str_sum = str(sum)
    return str_sum


#    По адресу /greet/<user_name> должен получать имя пользователя, возвращать текст 'Hello, имя_которое_прислали'


@app.route('/greet/<user_name>')
def greet(user_name):
    return 'Hello,{}'.format(user_name)


#    По адресу /form/user должен принимать POST запрос с параментрами:
#    email, пароль и подтверждение пароля. Необходимо валидировать email, что обязательно присутствует,
#    валидировать пароли, что они минимум 6 символов в длину и совпадают.
#    Возрващать пользователю json вида: "status" - 0 или 1 (если ошибка валидации),
#    "errors" - список ошибок, если они есть, или пустой список.


@app.route('/form/user', methods=['GET', 'POST'])
def register():
    print(request.method)
    if request.method == 'POST':
        user_form = UserFrom(request.form)
        if user_form.validate():
            return jsonify({'status': 0, 'errors': user_form.errors})
        else:
            print(json.dumps({'status': 1}))
            print(user_form.errors)
            return jsonify({'status': 1, 'errors': user_form.errors}), 'Incorrect!'


#    По адресу /serve/<path:filename> должен возвращать содержимое запрашиваемого файла из папки ./files.
#    Файлы можно туда положить любые текстовые. А если такого нет - 404


@app.route('/serve/<path:filename>')
def show_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()

    except FileNotFoundError:
        return abort(404)


if __name__ == '__main__':
    app.run()
