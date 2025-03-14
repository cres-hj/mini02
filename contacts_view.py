from flask import Blueprint, render_template, redirect,request
import datetime as dt

contacts_app = Blueprint('contact_app', __name__,)

contacts = []

cno = 1

@contacts_app.route("/contacts/list")
def indax():
    return render_template("contacts/list.html", contacts = contacts)

@contacts_app.route("/contacts/write", methods=["GET", "POST"])
def write():
    global cno
    if request.method == 'GET':
        return render_template("contacts/write.html")
    elif request.method == 'POST':
        name = request.form.get('name')
        tel = request.form.get('tel')
        address = request.form.get('address')
        new_contact = {'cno':cno, 'name':name, 'tel':tel, 'address':address}
        contacts.append(new_contact)
        cno += 1
        return redirect("/contacts/list")
    
@contacts_app.route("/contacts/read")
def read():
    cno = int(request.args.get('cno'))
    for contact in contacts:
        if contact['cno'] == cno:
            return render_template("contacts/read.html", contact = contact)
    return redirect("/contacts/list")

@contacts_app.route("/contacts/update", methods = ['POST'])
def update():
    cno = int(request.form.get('cno'))
    tel = request.form.get('tel')
    address = request.form.get('address')
    for contact in contacts:
        if contact['cno'] == cno:
            contact['tel'] = tel
            contact['address'] = address
            return redirect(f"/contacts/read?cno={cno}")
    return redirect("/contacts/list")

@contacts_app.route("/contacts/delete", methods = ['POST'])
def delete():
    cno = int(request.form.get('cno'))
    for contact in contacts:
        if contact['cno'] == cno:
            contacts.remove(contact)
    return redirect("/contacts/list")