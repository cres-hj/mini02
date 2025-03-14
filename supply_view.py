from flask import Blueprint, render_template, redirect, request

supp_app = Blueprint('supp_app', __name__)

supplies=[]
sno=1


@supp_app.route("/supply/list")
def index_sup():
  return render_template("supply/list.html", supplies=supplies)

@supp_app.route("/supply/add", methods=['GET','POST'])      # 추가 (get: 작성화면보기 / post: 작성후 비품 목록으로 이동)
def add():
  if request.method=='GET':
    return render_template("supply/add.html")
  elif request.method=='POST':
    global sno
    name = request.form.get('name')
    date = request.form.get('date')
    count = int(request.form.get('count'))
    new_supply = {'sno':sno, 'name':name, 'count':count, 'date':date}
    supplies.append(new_supply)
    sno+=1
    return redirect("/supply/list")
  
@supp_app.route("/supply/read")           # 비품번호를 이용해 항목 출력
def read():
  sno = int(request.args.get('sno'))
  print(sno)
  for s in supplies:
    print(s['sno'])
    if s['sno']==sno:
      return render_template("supply/read.html", supply=s)
  return redirect("/supply/list")

@supp_app.route("/supply/up", methods=['POST'])       # 갯수 증가
def up():
  sno = int(request.form.get('sno'))
  for s in supplies:
    if s['sno']== sno:
      s['count']=s['count']+1
  return redirect("/supply/list")

@supp_app.route("/supply/down", methods=['POST'])     # 갯수 감소
def down():
  sno = int(request.form.get('sno'))
  for s in supplies:
    if s['sno']== sno and s['count']>1:
      s['count']=s['count']-1
  return redirect("/supply/list")


@supp_app.route("/supply/delete", methods=['POST'])   # 삭제
def delete():
  sno = int(request.form.get('sno'))
  for s in supplies:
    if s['sno']==sno:
      supplies.remove(s)
  return redirect("/supply/list")


app.run(debug=True)