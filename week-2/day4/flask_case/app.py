from typing import List
from flask import Flask, app, request, render_template
from flask.helpers import url_for
from database.users import UserDatabase
import random,string
from functions import Bank
from flask import session


db = UserDatabase()

app = Flask(__name__)

users={}
app.secret_key='sandeep@123'

@app.route('/')
def index():
    return render_template('login.html',bg='static/bgcol.jpg')


@app.route('/dash', methods=['POST'])
def dashboard():

    user_name = request.form['username']
    password = request.form['password']

    user = db.user_by_creds(user_name, password)

    if(user.role == 'admin'):
        menus: List[str] = [
            {'ttl': 'Create Account', 'url': url_for('create_account')},
            {'ttl': 'All Accounts', 'url': url_for('all_accounts')},
            {'ttl': 'Withdraw', 'url':url_for('withdraw')},
            {'ttl': 'Balance', 'url':url_for('balance')},
            {'ttl': 'Deposit', 'url':url_for('deposite')},
            {'ttl': 'Activate', 'url':url_for('activate')},
            {'ttl':'Deactivate','url':url_for('deactivate')}
        ]
    else:
        menus: List[str] = [
            {'ttl': 'Withdraw', 'url':url_for('withdraw')},
            {'ttl': 'Balance', 'url':url_for('balance')},
            {'ttl': 'Deposit', 'url':url_for('deposite')}
        ]

    return render_template('dashboard.html', menus=menus,bg='static/bgcol.jpg')


@app.route('/create-acc-form')
def create_account():
    return render_template('create_account.html',bg='static/bgcol.jpg')


@app.route('/submit-create-acc',methods=['POST'])
def submit_create_account():
    global userss
    if request.method == 'POST':
        username=request.form['username']
        session['userss']=username
        userss=Bank(session['userss'])
        if username in users:
            return render_template('already_exit.html')
        else:
            password=request.form['password']
            ac_num=''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
            users[username]=ac_num
            return render_template('submit_create_account.html',username=username,ac_num=ac_num)
@app.route('/balance')
def all_accounts():
    ac=users
    return render_template('balance.html',ac=ac)

@app.route('/deposite')
def deposite():
    return render_template('deposite.html',bg='static/bgcol.jpg')

@app.route('/view_depo',methods=['POST'])
def view_depo():
    if request.method == 'POST':
        username=request.form['username']
        ac_num=request.form['ac_num']
        amount=request.form['amount']
        if username in users:    
            depo=userss.deposite(amount)
            return render_template('view_deposite.html',depo=depo)
        else:
            return render_template('crte_acc.html')
@app.route('/withdraw')
def withdraw():
    return render_template('withdraw.html',bg='static/bgcol.jpg')

@app.route('/view_withdraw',methods=['POST'])
def view_with():
    if request.method == 'POST':
        username=request.form['username']
        ac_num=request.form['ac_num']
        amount=request.form['amount']
        if username in users:    
            depo=userss.withdraw(amount)
            if depo==amount:
                return render_template('insuff.html')
            else:
                return render_template('disp_with.html',dep=depo,amt=amount)
        else:
            return render_template('crte_acc.html')

@app.route('/showbalance')
def balance():
    return render_template('shownal.html',bg='static/bgcol.jpg')

@app.route('/usersbalance',methods=['POST'])
def isbalance():
    username=request.form['username']
    ac_num=request.form['ac_num']
    if username in users:
        depo=userss.view_balance()
        return render_template('view_bal.html',depo=depo)
    else:
        return render_template('crte_acc.html')

# @app.route('/eyh56u5u6')
# def status():
#     menus: List[str] = [
#             {'ttl': 'Account', 'url': url_for('account.status')},
#             {'ttl': 'Accounts', 'url': url_for('asfaccounts.status')},
#     ]
#     return render_template('status.html',menus=menus,bg='static/bgcol.jpg')

@app.route('/isactivate')
def activate():
    return render_template('isact.html',bg='static/bgcol.jpg')

@app.route('/activateds',methods=['POST'])
def activateds():
    username=request.form['username']
    ac_num=request.form['ac_num']
    if username in  users:
        depo=userss.Act_status(username)
        return render_template('activateds.html',ac=ac_num)
    else:
        return render_template('crte_acc.html')

@app.route('/isdeactivate')
def deactivate():
    return render_template('isdact.html',bg='static/bgcol.jpg')

@app.route('/deactivateds',methods=['POST'])
def deactivateds():
    username=request.form['username']
    ac_num=request.form['ac_num']
    if username in  users:
        depo=userss.deact(username)
        return render_template('deactivateds.html',ac=ac_num)
    else:
        return render_template('crte_acc.html')
if __name__=='__main__':
    app.run()