from flask import Flask, render_template
from contacts_view import contacts_app
from supply_view import supp_app
from todo_view import todo_app
from finance_view import finance_app
app = Flask(__name__)

app.register_blueprint(contacts_app)
app.register_blueprint(supp_app)
app.register_blueprint(todo_app)
app.register_blueprint(finance_app)

@app.route('/')
def index():
    return render_template('index.html')
