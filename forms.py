from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

# ==================================================
# Formクラス
# ==================================================
# 入力クラス  新規登録画面
class InputForm(FlaskForm):
    name = StringField('名前：', validators=[DataRequired('必須入力です')])
    password = PasswordField('パスワード：', validators=[Length(3, 10, 'パスワードの長さは3文字以上10文字以内です'), EqualTo('confirm_password', "パスワードが一致しません")])
    confirm_password = PasswordField('パスワード確認：')
    
    submit = SubmitField('送信')
    
# 入力クラス  ログイン画面    
class InputForm2(FlaskForm):
    name2 = StringField('名前：', validators=[DataRequired('必須入力です')])
    password2 = PasswordField('パスワード：')
    
    submit2 = SubmitField('ログイン')