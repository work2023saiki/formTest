from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField     
from wtforms.validators import DataRequired, Email, Length, EqualTo    #バリデーターを使うためインポート

# ==================================================
# Formクラス
# ==================================================
# 入力クラス  新規登録画面
class InputForm(FlaskForm):   #flask_wtfのFlaskFormクラスを継承する
    name = StringField('名前：', validators=[DataRequired('必須入力です')])    #ユーザー名を入力するところ。第1引数の'名前：'は登録画面に表示するラベル。第2引数のvalidatorsで登録エラーを表示。
    password = PasswordField('パスワード：', validators=[Length(3, 10, 'パスワードの長さは3文字以上10文字以内です'), EqualTo('confirm_password', "パスワードが一致しません")])   
    confirm_password = PasswordField('パスワード確認：')
    
    submit = SubmitField('送信')   #送信ボタン
    
# 入力クラス  ログイン画面    
class InputForm2(FlaskForm):     #class InputForm(FlaskForm):を使ってみたが上手くページが表示されなかったため、ログイン画面専用のクラスとして定義。
    name2 = StringField('名前：', validators=[DataRequired('必須入力です')])
    password2 = PasswordField('パスワード：')
    
    submit2 = SubmitField('ログイン')