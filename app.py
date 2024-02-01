from flask import Flask, render_template, session, redirect, url_for

# ==================================================
# インスタンス生成
# ==================================================
app = Flask(__name__)
import os
# 乱数を設定
app.config['SECRET_KEY'] = os.urandom(24)

# ==================================================
# ルーティング
# ==================================================
from forms import InputForm, InputForm2

#ログイン
@app.route('/', methods=['GET', 'POST'])
def login():
    form2 = InputForm2()
    # POST
    if form2.validate_on_submit():
        
        return redirect(url_for('dammy'))
    # GETリクエストの場合、またはフォームの値がバリデーションを通過しなかった場合
    return render_template('login.html', form=form2)

# 登録
@app.route('/touroku', methods=['GET', 'POST'])
def touroku():
    form = InputForm()
    # POST
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['password'] = form.password.data
        session['confirm_password'] = form.confirm_password.data
        
        return redirect(url_for('tourokuOK'))
    
    # GETリクエストの場合、またはフォームの値がバリデーションを通過しなかった場合
    return render_template('touroku.html', form=form)

# 出力
@app.route('/tourokuOK')
def tourokuOK():
    return render_template('tourokuOK.html')


@app.route('/dammy')
def dammy():
    return render_template('tourokuOK.html')



# ==================================================
# 実行
# ==================================================
if __name__ == '__main__':
    app.run()