from flask import Blueprint, render_template

finance_app = Blueprint('finance_app', __name__)

@finance_app.route('/finance/list')
def index():
    return render_template('/finance/list.html')
