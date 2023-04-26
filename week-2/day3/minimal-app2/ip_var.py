from flask import Flask
app=Flask(__name__)

@app.route('/myname/<nm>')
def name(nm:str):
    return f'you name is {nm}'

@app.route('/addition/<int:num1>/<int:num2>')
def addition(num1:int,num2:int):
    return f'<h1>addition of {num1} and {num2} is {num1+num2}</h1>'