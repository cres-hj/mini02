from flask import Blueprint, render_template, redirect, request
import datetime as dt

todo_app = Blueprint('todo_app', __name__)

todos = []
tno = 1

# 읽기
@todo_app.route('/todo/list')
def todo_list():
    return render_template('/todo/list.html', todos = todos)


# 추가
@todo_app.route('/todo/write', methods = ['GET', 'POST'])
def todo_write():
    global tno
    if request.method == 'GET':
        return render_template('/todo/write.html', todos = todos)
    elif request.method == 'POST':
        w_date = dt.datetime.now().strftime('%Y-%m-%d')
        f_date = request.form.get('f_date')
        title = request.form.get('title')
        content = request.form.get('content')
        new_todo = {'tno':tno, 'f_date':f_date, 'w_date':w_date, 'title':title, 'content':content, 'finish':False}
        todos.append(new_todo)
        tno += 1
        return redirect('/todo/list')
        
@todo_app.route('/todo/read')
def read():
    tno = int(request.args.get('tno'))
    for todo in todos:
        if todo['tno'] == tno:
            return render_template('/todo/read.html', todo = todo)
    return render_template('/todo/list.html')


# 수정
@todo_app.route('/todo/finish', methods = ['POST'])
def todo_finish():
    tno = int(request.form.get('tno'))
    for todo in todos:
        if todo['tno'] == tno:
            todo['finish'] = True
            return redirect(f'/todo/read?tno={tno}')
    return redirect('/todo/read')



# 삭제
@todo_app.route('/todo/delete', methods = ['POST'])
def todo_delete():
    tno = int(request.form.get('tno'))
    for todo in todos:
        if todo['tno'] == tno:
            todos.remove(todo)
            return redirect('/todo/list')
    return redirect('/todo/list')
