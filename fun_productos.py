from werkzeug.utils import secure_filename
from flask import Flask,request,redirect,render_template,url_for,session, Blueprint
from modelo1 import db, subcat_mujer, subcat_hombre, articulos
#app = Flask(__name__)
app_blueprint = Blueprint('fun_productos', __name__)
########################################################### crud articulos #####################################################
################################################################################################################################
@app_blueprint.route('/articulos', methods=["get"])
@app_blueprint.route('/articulos/<id>', methods=["get","post"])
def articulosx(id=None):
    msg=""
    #catx = cat.query.all()
    subcatx = subcat.query.all()
    artx = articulos.query.all()

    # para actualizar
    idx = articulos.query.get(id)
    if request.method == 'POST':
        idx.img1 = request.form["img1"]
        #filex = request.files["img1"]
        idx.nombre = request.form['nombre']
        idx.precio = request.form['precio']
        idx.info = request.form['info']
        idx.stock = request.form['stock']
        idx.catid = request.form['catid']
        #nombre_archivo = secure_filename(filex.filename) 
        #filex.save(app.root_path + "/static/upload/" + nombre_archivo)
        #artz.img1 = nombre_archivo
        db.session.commit()
        msg="actualizado conexito"
    #return render_template("articulos/lista-articulos-y-update.html", cat=catx, subcat=subcatx, art=artx, artxz=artxz, artzx=True, msg=msg)
    return render_template("articulos/lista-articulos-y-update.html", subcat=subcatx, art=artx, artid=idx, msg=msg) #artzx=True,


'''<div>
            <select type="text" name="catid">
                <option value="">Selecciona categoria</option>
                {% for tip in categorias %}
                <option value="{{tip.id}}">{{ tip.nombre }}</option>
                {% endfor %}
        </select>
        </div>
        <input class="boton" type="submit" value="Registrar">'''

@app_blueprint.route('/articulo_new', methods=["post"])
def articulo_newx():
    msg=""
    filex1 = request.form["img1"]
    #filex1 = request.files["img1"]
    #filex2 = request.files["imagen2"]
    #filex3 = request.files["imagen3"]
    nombre = request.form['nombre']
    precio = request.form['precio']
    infox = request.form['info']
    stock = request.form['stock']
    catid = request.form['catid']
        #nombre_archivo = secure_filename(filex.filename)
        #nombre_archivo = secure_filename(filex1.filename) 
        
        #nombre_archivo = secure_filename(filex2.filename)  
        #nombre_archivo = secure_filename(filex3.filename)  
        #filex1.save(os.path.join("C:/Practicas-Deybi/python/apps/app-gacela/app-gacela-normal/static/",nombre_archivo))
        #filex1.save(os.chdir("C:/Practicas-Deybi/python/apps/app-gacela/static/upload/"))
        #filex1=open(os.chdir("C:/Practicas-Deybi/python/apps/app-gacela/app-gacela-normal/static",nombre_archivo))
        #filex1.save(app.root_path + "././static/upload/" + nombre_archivo)
    art = articulos(img1=filex1, nombre=nombre, precio=precio, info=infox, stock=stock, catid=catid)
        #art.img1 = nombre_archivo
        #art.imagen2 = nombre_archivo
        #art.imagen3 = nombre_archivo
    db.session.add(art)
    db.session.commit()
    msg="producto agregado con exito"
    return redirect(url_for("articulosx", msg=msg))

@app_blueprint.route('/delete_articulo/<id>', methods=["get", "post"])
def delete_articulox(id):   # /delete_articulo/{{art.id}}
    art = articulos.query.get(id)
    if request.method=="POST":
        if id>"1" and request.form['si']:
            #if art.imagen != "":
            #    os.remove(app.root_path+"/static/upload/"+art.imagen)
            db.session.delete(art), db.session.commit()
            return redirect("/articulos")
    return render_template("articulos/articulo-delete.html",art=art)
