from flask import Flask, render_template, session, redirect, url_for     #sessionとredirectを新たにインポート

# ==================================================
# インスタンス生成
# ==================================================
app = Flask(__name__)
import os    # 乱数を設定するためインポート
# 乱数を設定
app.config['SECRET_KEY'] = os.urandom(24)   #アプリのセキュリティに関する設定。ランダムな文字列でセッション情報を暗号化するためのキーとして使用する。
# ==================================================
# ルーティング
# ==================================================
from forms import InputForm, InputForm2      #ファイルforms.pyのクラス、InputForm, InputForm2をインポート

#ログイン
@app.route('/', methods=['GET', 'POST'])
def login():
    form2 = InputForm2()      #ファイルforms.pyのInputForm2クラスからオブジェクトを作る
    # POST
    if form2.validate_on_submit():    #「if form2.validate_on_submit() == True:」と同じ。InputForm2クラス、validatorsの内容が表示されないなら、
        
        return redirect(url_for('dammy'))     #redirectとすることで、ユーザー名、パスワードの二重送信を防ぐ。PRGパターンのR。
    # GETリクエストで、ifが通らなかった場合。form2オブジェクトを引数としてformにわたす。
    return render_template('login.html', form=form2)    #ログイン画面へ

# 登録
@app.route('/touroku', methods=['GET', 'POST'])
def touroku():
    form = InputForm()     #ファイルforms.pyのInputFormクラスからオブジェクトを作る
    # POST
    if form.validate_on_submit():    #「if form.validate_on_submit() == True:」と同じ。InputFormクラス、validatorsの内容が表示されないなら、
        session['name'] = form.name.data           #セッションとして保存。他のページに移動してもsession['name']の中身はそのまま。
        session['password'] = form.password.data     #form.password.dataのformは、30行目のformのことで、InputForm()のオブジェクト。form.password.dataのpasswordは、InputForm()のpasswordで、.data部分はたぶん
        session['confirm_password'] = form.confirm_password.data
        
        return redirect(url_for('tourokuOK'))   #redirectとすることで、ユーザー名、パスワードの二重送信を防ぐ。PRGパターンのR。
    
    # GETリクエストで、ifが通らなかった場合。formオブジェクトを引数としてformにわたす。
    return render_template('touroku.html', form=form)

# 登録完了画面
@app.route('/tourokuOK')
def tourokuOK():
    return render_template('tourokuOK.html')


@app.route('/dammy')
def dammy():
    return render_template('tourokuOK.html')    #python_aでは13種類のゲーム選択画面のhtmlファイルを指定する。




# ==================================================
# 実行
# ==================================================
if __name__ == '__main__':
    app.run()