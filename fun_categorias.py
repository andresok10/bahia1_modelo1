from werkzeug.utils import secure_filename
from flask import Flask,request,redirect,render_template,url_for,session, Blueprint
from modelo1 import db, subcat_mujer, subcat_hombre, cat
app_blueprint = Blueprint('fun_categorias', __name__)
########################################################### crud categorias ###################################
@app_blueprint.route('/cat', methods=["get"])   #value="{{catid.nombre}}"
@app_blueprint.route('/cat/<id>', methods=["get", "post"])
def catx(id=None):
    msg=""
    catxx = cat.query.all()
    subcatx = subcat.query.all()
    # para actualizar
    catid = cat.query.get(id)
    if request.method == 'POST':
        #catid.nombre = request.form.get('nombre')
        catid.nombre = request.form['nombre']
        db.session.commit()
        msg="actualizado conexito"
    return render_template("categorias/cat.html", catx=catxx, catid=catid, msg=msg, subcatx=subcatx)  #, subcatid=subcatid

@app_blueprint.route('/add_cat', methods=["get", "post"])  # action="{{ url_for('agregar_categoria') }}"
def add_catx():
    nombrex = request.form['nombre']
    cate = cat(nombre=nombrex)
    db.session.add(cate)
    db.session.commit()
    return redirect(url_for('fun_categorias.catx'))
################################################################

@app_blueprint.route('/subcat', methods=["get"])
@app_blueprint.route('/subcat/<id>', methods=["get", "post"])
def subcatxx(id=None):
    msg=""
    subcatx = subcat.query.all()
    # para actualizar
    subcatid = subcat.query.get(id)
    if request.method == 'POST':
        subcatid.nombre = request.form['nombre']
        subcatid.catid = request.form['catidx']
        db.session.commit()
        msg="actualizado conexito"
        return redirect("/cat")
    return render_template("categorias/cat.html", subcatx=subcatx, subcatid=subcatid, msg=msg)

@app_blueprint.route('/add_subcat', methods=['POST'])
def add_subcatx():
    nombre = request.form['nombre']
    catidx = request.form['catidx']
    sub = subcat(nombre=nombre, catid=catidx)
    db.session.add(sub)
    db.session.commit()
    return redirect(url_for('fun_categorias.catx'))
########################################################################
@app_blueprint.route('/delete_cat/<id>', methods=["get","post"])
def delete_catx(id):
    catxx = cat.query.filter_by(id=id).one()
    #catxx = cat.query.filter_by(id=id).join(sub_cat).filter_by(catid=id).one()#.first()
    #print(catxx)
    #catx = session.query(Cat).filter_by(id=id).delete()
    if request.method == 'POST':
        if id>="1" and request.form['si']:  # no se puede eliminar categoria 1, elimina la categoria q sea 2 o superior
            db.session.delete(catxx)
            db.session.commit()
            return redirect(url_for('fun_categorias.catx'))
    return render_template("categorias/cat_delete.html",catx=catxx)

@app_blueprint.route('/delete_subcat/<id>', methods=["get", "post"])
def delete_subcatx(id):
    subcatid = subcat.query.filter_by(id=id).first()
    if request.method == 'POST':
        if id==id and request.form['si']:  # no se puede eliminar categoria 1, elimina la categoria q sea 2 o superior
            db.session.delete(subcatid), db.session.commit()
            #return redirect("/categorias")
            return redirect(url_for('fun_categorias.catx'))
    return render_template("categorias/subcat_delete.html", subcat=subcatid)
