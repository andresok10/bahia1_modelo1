from werkzeug.utils import secure_filename
from flask import Flask,request,redirect,render_template,url_for,session, Blueprint
from modelo1 import db, usuarios
app_blueprint = Blueprint('fun_usuarios', __name__)
########################################################### crud usuarios #####################################################
#@app.route('/', methods=['get', 'post'])
@app_blueprint.route('/login', methods=['get', 'post'])
def loginx():
    msg=""
    if request.method == 'POST':       #if flask.request.method == 'GET':
        usuariox = request.form['usuario']
        passwordx = request.form['password']
        #remember = True if request.form.get('remember') else False
        user = usuarios.query.filter_by(usuario=usuariox, password=passwordx).first()
        if user is not None:
            session['id'] = user.id
            session['nombre'] = user.nombre
            session['admin'] = user.admin
            #return redirect(url_for('iniciox'))
            return redirect('/')
        else:
            msg="credenciales invalidas"
    return render_template('/usuarios/login-form-normal.html',msg=msg)

@app_blueprint.route("/registro", methods=["get", "post"])
def registrox():
    msg=""
    if request.method == 'POST':
        nombrex = request.form['nombre']
        usuariox = request.form['usuario']
        passwordx = request.form['password']
        emailx = request.form['email']
        userx = usuarios.query.filter_by(usuario=usuariox).first()
        if userx is None and session["admin"] is True:       # AttributeError: 'NoneType' object has no attribute 'admin'
            user = usuarios(usuario=usuariox, password=passwordx, nombre=nombrex, email=emailx)  # ,admin=admin
            user.admin = True
            db.session.add(user), db.session.commit()
            msg="se registro con exito un admin"   #return redirect("/login")
            
        elif userx is None and session["admin"] is False:
            user = usuarios(usuario=usuariox, password=passwordx, nombre=nombrex, email=emailx)  # ,admin=admin
            db.session.add(user), db.session.commit()
            msg="se registro con exito"   #return redirect("/login")
        else:
            msg="usuario ya existe"
    return render_template("usuarios/register-normal.html",msg=msg)

@app_blueprint.route('/perfil', methods=["get", "post"])
def perfilx():
    if session["admin"] is True or  session["admin"] is False: 
        cuenta = usuarios.query.filter_by(id=session['id']).first()
        return render_template("usuarios/perfil-normal.html",cuenta=cuenta)
    return redirect('/inicio')

@app_blueprint.route('/changepassword/<username>', methods=["get", "post"])
def changepasswordx(username):
    user = usuarios.query.filter_by(username=username).first()
    if request.method == 'POST':
        user.password = request.form['password']
        db.session.commit()
        return redirect("/inicio")
    return render_template("usuarios/cambio-contraseña.html")

@app_blueprint.route("/cerrar")
def cerrarx():
    session.clear()
    #session.pop('activo', None)
    #session.pop('id', None)
    #session.pop('nombre', None)
    return redirect("/login")
    #return redirect(url_for("loginx"))