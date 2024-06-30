#from werkzeug.utils import secure_filename
from flask import Flask, request, redirect, render_template, url_for, session, Blueprint, make_response, json, jsonify
from modelo1 import db, cat, subcat_mujer, subcat_hombre, articulos, usuarios, Pedido,DetallePedido
import stripe
#from fun_usuarios import *
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
#import json, sys, os
app_blueprint = Blueprint('fun_inicio', __name__)
######################################### inicio ############################ onclick="cambiarColor(this)"  id="agregarBtn" 
# /inicio/{{artx.id}}         #{{ url_for('iniciox') }}
# <input type="hidden" name="product" value="{{ artx.id }}">
# {{ url_for('iniciox', id=artx.id) }}

#cat1 = sub_cat.query.filter_by(catid=id).all() if id else sub_cat.query.all()  # Filter subcategories based on category id
#art1 = articulos.query.filter_by(catid=id).all() if id else articulos.query.all()    

def initialize_cart():
    if "id" not in session:
        session.clear()
    if "admin" not in session:
        session.clear()
    if 'cart' not in session:
        session['cart'] = []
    if 'contador' not in session:
        session['contador'] = 0
    if 'total' not in session:
        session['total'] = 0
    
@app_blueprint.route('/', methods=["get","post"])
@app_blueprint.route('/inicio_uno', methods=["get","post"])
@app_blueprint.route('/inicio_uno/<int:id>', methods=["get","post"])
#@app_blueprint.route('/inicio_uno/<string:id>', methods=["get","post"])
def inicio1(id=1):
    initialize_cart()
    cat1 = cat.query.all()
    sub1 = subcat_mujer.query.all()
    art1 = articulos.query.filter_by(sub_mujer=id).all()
    #request.form.get("id"==id)
    #request.form.get(id==id)
    if request.method == 'POST':
        try: 
            #userx = usuarios.query.filter_by(id=id).all()
            #userx = usuarios.query.get(id)
            #datos = json.loads(request.cookies.get(str(userx.id)))  # session['id']  session.get('id')
            datos = json.loads(request.cookies.get(str(session.get('id')), '[]'))
            print(datos)
        except:
            datos = []
        product_id = int(request.form['product'])
        cantidadx = int(request.form['cantidad'])
        #idx = articulos.query.get(product_id)
        idx = articulos.query.filter_by(id=product_id).first()
        #idx = articulos.query.filter_by(id=id).first()
        actualizar = False
        #if idx is not None:
        for x in datos:
            #print(x)
            if x["id"] == idx.id:
                x["stock"] = cantidadx
                actualizar = True
                #break
                #pass
        if not actualizar:
            #datos.append({"id": id , "stock": cantidadx})
            datos.append({'id': idx.id, 'img1': idx.img1, 'nombre': idx.nombre, 'precio': idx.precio, "stock": cantidadx})
            
        # Save updated cart to cookies
        session['contador'] = len(datos)
        #session['cart'] = datos
        resp = make_response(redirect(url_for('fun_inicio.inicio1',id=id)))
        resp.set_cookie(str(session.get('id')), json.dumps(datos))  # Save cart data
        #resp.set_cookie(str(session['cart']), json.dumps(datos))  # Save cart data
        return resp
        #return redirect(url_for("fun_inicio.inicio1", id=id))
    #return render_template("mujer-final2.html", art1=art1, cat1=cat1, sub1=sub1,)
    #return render_template("mujer_final3.html", art1=art1, cat1=cat1, sub1=sub1,)
    #return render_template("f.html", art1=art1, cat1=cat1, sub1=sub1,)
    return render_template("index_sin_productid.html", art1=art1, cat1=cat1, sub1=sub1,)

@app_blueprint.route('/inicio_dos', methods=["get"])
@app_blueprint.route('/inicio_dos/<int:id>', methods=["get","post"])
def inicio2(id=1):
    initialize_cart()
    cat1 = cat.query.all()
    sub1 = subcat_hombre.query.all()
    art1 = articulos.query.filter_by(sub_hombre=id).all()
    try: 
        datos = json.loads(request.cookies.get(str(session.get('id'))))  # session['id']  session.get('id')
        #print(datos)
    except:
        datos = []
    if request.method == 'POST':
        product_id = int(request.form['product'])
        cantidadx = int(request.form['cantidad'])
        idx = articulos.query.get(product_id)
        actualizar = False
        if idx is not None:
            for x in datos:
                if x["id"] == idx.id:
                    x["stock"] = cantidadx
                    actualizar = True
        if not actualizar:
            datos.append({'id': idx.id, 'img1': idx.img1, 'nombre': idx.nombre, 'precio': idx.precio, "stock": cantidadx})
        session['contador'] = len(datos)
        resp = make_response(redirect(url_for('fun_inicio.inicio2',id=id)))
        resp.set_cookie(str(session.get('id')), json.dumps(datos)) # set_cookie
        return resp
        #return redirect(url_for("fun_inicio.inicio2", id=id))
    return render_template("mhombre2.html", art1=art1, cat1=cat1, sub1=sub1, )
    
#cat1 = sub_cat.query.filter_by(catid=id).all() #if id else sub_cat.query.all()  # Filter subcategories based on category id
#art1 = articulos.query.filter_by(catid=id).all() #if id else articulos.query.all()
#cat2 = cat.query.filter_by(id=not None).all()
#subcat1 = subcat.query.filter_by(catid=id).all() if id else []
#print(f"{subcat1}")
    
############################################## carrito #########################################################
#@app_blueprint.route('/carrito', methods=["GET", "POST"])
#@app_blueprint.route('/carrito/<id>', methods=["get", "post"])
#def carritox(id=1):
@app_blueprint.route('/carrito', methods=["get","post"])
def carritox():
    msg = ""
    try:
        #userx = usuarios.query.filter_by(id=1).all()
        #userx = usuarios.query.get(id)
        #datos = json.loads(request.cookies.get(str(userx.id)))  # session['id']  session.get('id')
        #datos = json.loads(request.cookies.get(str(session.get('id'))))
        datos = json.loads(request.cookies.get(str(session.get('id')), '[]'))
        #print(datos)
    except:
        datos = []
    articulosx = []
    cantidadesx = []
    precios_con_iva = 0
    #precios_sin_iva = 0
    precios_con_iva_articulos = {}  # Usaremos un diccionario para almacenar precios con IVA por artículo
    for x in datos:
        print(x)
        articulo = articulos.query.filter_by(id=int(x["id"])).first()
        if articulo is not None:
            articulosx.append(articulo)
            #cantidadesx.append(x["stock"])
            cantidadesx.append(x["cantidad"])
            #precio_sin_iva = articulo.precio * x["stock"]  # Precio sin IVA
            precio_sin_iva = articulo.precio * x["cantidad"]  # Precio sin IVA
            #precios_sin_iva += precio_sin_iva
                    
            iva = precio_sin_iva * 0.12  # Calcula el IVA
            precio_con_iva = precio_sin_iva + iva  # Precio con IVA
            precios_con_iva += precio_con_iva
                    
            # Guardamos el precio con IVA por artículo en el diccionario
            precios_con_iva_articulos[articulo.nombre] = precio_con_iva
            #precios_con_iva_articulos[articulo.nombre] = round(precio_con_iva,2)
            #precios_con_iva_articulos[articulo.nombre] = float("{:.2f}".format(precio_con_iva))
    
    # Combine los datos de artículos y cantidades en una lista de tuplas
    datos_combinados = list(zip(articulosx, cantidadesx))
    #form.id.data = id
    #request.form.get("id"==id)
    if request.method == 'POST':
        cantidadx = int(request.form['cantidad'])
        product_id = int(request.form['product'])
        idx = articulos.query.filter_by(id=product_id).first()
        #if idx and cantidadx <= idx.stock:
        if idx is not None and cantidadx <= idx.stock:
            #datos = json.loads(request.cookies.get(str(current_user.id)))
            try:
                datos = json.loads(request.cookies.get(str(session.get('id')), '[]'))
                #print(datos)
            except:
                datos = []
            actualizar = False
            for x in datos:
                print(x)
                if x["id"] == idx.id:
                    x["stock"] = cantidadx
                    actualizar = True
                    #break
            if not actualizar:
                datos.append({'id': idx.id, 'img1': idx.img1, 'nombre': idx.nombre, 'precio': idx.precio, 'stock': cantidadx})
            session['contador'] = len(datos)
            session['cart'] = datos
            #resp = make_response(redirect(url_for('fun_inicio3.carritox', id=id)))
            resp = make_response(redirect(url_for('fun_inicio3.carritox')))
            resp.set_cookie(str(session.get('id')), json.dumps(datos)) # set_cookie
            return resp
        #if request.method == 'POST' and int(request.form['cantidad']) > idxx.stock:
        else:
            msg = "No hay suficiente stock"
            #msg='NO HAY LA  CANTIDAD QUE QUIERE2'
    return render_template("carrito3.html", datos_combinados=datos_combinados, precios_con_iva=float("{:.2f}".format(precios_con_iva)), precios_con_iva_articulos=precios_con_iva_articulos, msg=msg)
#########
@app_blueprint.route('/carritozzzz/<id>', methods=["get", "post"])
def carritoxzzzzzz(id):
#@app_blueprint.route('/carrito', methods=["GET", "POST"])
#def carritox():
    msg = ""
    try:
        datos = json.loads(request.cookies.get(str(session.get('id'))))
    except:
        datos = []
    if request.method == 'POST':
        cantidadx = int(request.form['cantidad'])
        product_id = int(request.form['product'])
        idx = articulos.query.filter_by(id=product_id).first()
        if idx is not None and cantidadx <= idx.stock:
            actualizar = False
            for x in datos:
                if x["id"] == idx.id:
                    x["stock"] = cantidadx
                    actualizar = True
                    break
            if not actualizar:
                datos.append({'id': idx.id, 'img1': idx.img1, 'nombre': idx.nombre, 'precio': idx.precio, 'stock': cantidadx})
            #session['cart'] = cart
            session['contador'] = len(datos)
            resp = make_response(redirect(url_for('fun_inicio3.carritox', id=id)))
            resp.set_cookie(str(idx.id), json.dumps(datos)) # set_cookie
            return resp
        #if request.method == 'POST' and int(request.form['cantidad']) > idxx.stock:
        else:
            msg = "No hay suficiente stock"
    #total = sum(item['precio']*item['stock'] + (item['precio']*item['stock']*12/100) for item in cart)  # + subtotal*12/100 
    total = sum(item['precio'] * item['stock'] * 1.12 for item in cart)  # Including 12% tax
    #total = sum(item['precio'] * item['stock'] * 0.12 for item in cart)  # Including 12% tax
    session["total"] = total
    return render_template('cart.html', cart=datos, total=total, msg=msg)
#########
@app_blueprint.route('/carritoxxx', methods=["get", "post"])
#@login_required
def carritoxxxx():
    try: datos = json.loads(request.cookies.get(str(session.get('id'))))
    except:
        datos=[]
    articulosx = []
    #for x in articulosx:
    #    print(x)
    cantidadesx = []
    total = 0
    #iva=0
    #precios_con_iva = 0
    #precios_sin_iva = 0
    for x in datos:    # {{ form.csrf_token }}
        print(x)
        #articulosx.append(db.query(articulos).get(x["id"])) # articulos.append(Articulos.query.get(z[0]))   # obsoleto
        articulosx.append( db.query(articulos).filter_by(id=int(x["id"])).first() )
        cantidadesx.append(x["cantidad"])  # cantidades.append(z[1])

        sub_total = db.query(articulos.precio).filter_by(id=x["id"]).scalar() * x["cantidad"]
        # con este me da 34.10
        #total = float("{:.2f}".format( total + db.query(articulos.precio).filter_by(id=x["id"]).scalar() * x["cantidad"] + sub_total * 0.12 )) # si vale
        # con este me da 34.09
        total = total + db.query(articulos.precio).filter_by(id=x["id"]).scalar() * x["cantidad"] + sub_total * 0.12 # si vale

        #total = float("{:.2f}".format( total + db.query(articulos.precio * x["cantidad"] + sub_total * 12/100).filter_by(id=x["id"]).scalar() )) # si vale
        #sut_total = db.query(articulos).get(x["id"]).precio * x["cantidad"]   # obsoleto
        #total = float("{:.2f}".format( total + db.query(articulos).get(x["id"]).precio * x["cantidad"] + sut_total * 12/100 ))  # absoleto
        #print(total)

    '''for x in datos:    # {{ form.csrf_token }}
        #print(x) # {'id': '4', 'cantidad': 1}
        #z=list(x.values())
        #print(z) # ['4', 1]
        articulosx.append(db.query(Articulos).get(x["id"])) # articulos.append(Articulos.query.get(z[0]))
        cantidadesx.append(x["cantidad"])  # cantidades.append(z[1])
        #sub_total = float(Articulos.query.get(z[0]).precio * z[1]) solo en caso q nomas se obtengas los values()
        sub_total = float(db.query(Articulos).get(x["id"]).precio * x["cantidad"])
        total = float("{:.2f}".format(total + db.query(Articulos).get(x["id"]).precio * x["cantidad"] + sub_total * 12/100))
        #totalx.append(total)    
    articulosz = zip(articulosx, cantidadesx)'''
    articulosz = zip(articulosx, cantidadesx)
    #for x in articulosz:
    #    re=list(x)
    #    print(re)
    return render_template("carrito-normal.html",articulosz=articulosz,  total = float("{:.2f}".format(total)) ) #sub_total=sub_total
######################################################## detalles ########################################
@app_blueprint.route('/detalles/<id>', methods=["get","post"])
def detallesx(id):
    product = articulos.query.filter_by(id=id).first()
    if request.method == 'POST' and product.stock >= int(request.form['cantidad']):
        product_id = request.form['product']
        cantidadx = int(request.form['cantidad'])
        idx = articulos.query.filter_by(id=product_id).first()
        actualizar = False
        for x in cart:
            print(x)
            if x["id"] == idx.id:
                x["cantidad"] = cantidadx  
                actualizar = True
        if not actualizar:
            cart.append({'id': idx.id,'img1': idx.img1, 'nombre': idx.nombre, 'precio': idx.precio, "stock":cantidadx})
        session['cart'] = cart
        session['contador'] = len(cart)   #######
        return redirect(url_for("detallesx",id=id))
    return render_template("detalles.html", product=product)

###################################################################
@app_blueprint.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    global cart
    cart = [item for item in cart if item['id'] != product_id]
    session['cart'] = cart
    session['contador'] = len(cart)
    return redirect(url_for('fun_inicio.carritox'))
###################################################################
@app_blueprint.route('/historial_pedidos')
def historial_pedidos():
    # Obtener el ID del usuario desde la sesión o algún otro método
    id_usuariox = session.get('id')
    if id_usuariox is None:
        # Manejar el caso en el que el usuario no esté autenticado
        return "Debe iniciar sesión para ver su historial de pedidos"
    # Consultar los pedidos asociados al ID del usuario
    pedidos_usuario = Pedido.query.filter_by(usuario_id=id_usuariox).all()
    return render_template('historial_pedidos.html', pedidos=pedidos_usuario)
####################################################################################################################
@app_blueprint.route('/pagar', methods=["get","post"])  #session["total"]
def pagarx(): # 12/25 889    4242424242424242
    stripe.api_key = "sk_test_51LJBxwEpqu9KnJeFKsKsZSeGMNI51RAcOrG7SYa4LrtP7vkvLNXUdjsAXt8flVgb3VITVYqSAJUGMYeDxiaAgRhA002OY7g4L3"
    #stripe.api_key = app.config['STRIPE_SECRET_KEY']
    sessionx = stripe.checkout.Session.create(
        payment_method_types=['card'],
                    #type=['card'],
                    #images= ["static"],
        line_items=[{"price_data":  {
                                                "currency": "usd",
                                                #"images": {"src":"static"},
                                                #"description": "My First Test Customer",
                                                #"city": "San Francisco",
                                                #"label": {"name": "Carrito Purchase",},
                                                #"product_data": {"name": x["id"],},
                                                "product_data": {"name": "pagar a nombre de " + session['nombre'] },
                                                #"product_data": {"name": articulosx[0].nombre,},
                                                #"product_data": {"name": current_user.id,},
                                                #"product_data": {"name": db.query(Articulos).get(x["id"]).nombre,},
                                                #"amount_subtotal": sub_total,
                                                #"amount_total": total,
                                                #"unit_amount": round((float(session['total']) * 100)),},
                                                "unit_amount": round(session.get('total') * 100),},
                                                #"unit_amount": round(total * 100),},
                                                #"amount": round((float(total) * 100)),},
                                                "quantity": 1
                    }],
                    mode="payment",
                    #success_url="http://localhost:5000/gracias",
                    #cancel_url="http://localhost:5000/"
                    #https://app1-ey6x.onrender.com/
                    #success_url="http://localhost:5000/gracias",
                    success_url="https://app1-ey6x.onrender.com/gracias",
                    #cancel_url="http://localhost:5000/"
                    cancel_url="https://app1-ey6x.onrender.com/carrito"
                )
    generar_factura_pdf(session.get('cart', []), session.get('total', 0))
    # Extraer información del carrito de la sesión
    cart = session.get('cart', [])
    total = session.get('total', 0)
    #usuario_id = session.get('usuario_id')  # Asegúrate de tener el ID del usuario en la sesión
    usuario_id = session.get('id')  # Asegúrate de tener el ID del usuario en la sesión
    # Guardar la información del pedido en la base de datos
    nuevo_pedido = Pedido(usuario_id=usuario_id, total=total)
    db.session.add(nuevo_pedido)
    for item in cart:
        detalle_pedido = DetallePedido(pedido=nuevo_pedido, producto_id=item['id'], cantidad=item['stock'], precio=item['precio'])
        db.session.add(detalle_pedido)
    db.session.commit()
    # Limpiar el carrito de la sesión
    session['cart'] = []
    session['total'] = 0
    return redirect(sessionx.url, 303)

#######################################################
def generar_factura_pdf(cart, total):
    # Crea un objeto Canvas
    c = canvas.Canvas("factura.pdf", pagesize=letter)
    # Encabezado
    c.drawString(50, 750, "Factura")
    c.line(50, 740, 550, 740)
    # Contenido de la factura
    y = 720
    for item in cart:
        nombre = item['nombre']
        precio = item['precio']
        cantidad = item['stock']
        subtotal = precio * cantidad
        c.drawString(50, y, f"{nombre}: ${precio} x {cantidad} = ${float('{:.2f}'.format(subtotal*0.12))}")
        y -= 20
    # Total
    c.drawString(50, y, f"Total: ${float('{:.2f}'.format(total))}")
    # Guarda el PDF
    c.save()

############################################################
'''@app_blueprint.route('/carrito_delete/<id>')
def carrito_deletex(id):
    try: datos = json.loads(request.cookies.get(str(current_user.id)))
    except:
        datos = []
    new_datos = []
    for dato in datos:
        if dato["id"] != id:
            new_datos.append(dato)
    resp = make_response(redirect(url_for('carritox')))
    resp.set_cookie(str(current_user.id), json.dumps(new_datos))
    return resp

@app_blueprint.context_processor
def contar_carrito():
    if not current_user.is_authenticated:
        return {'num_articulos': 0}
    if request.cookies.get(str(current_user.id)) is None:
        return {'num_articulos': 0}
    else:
        datos = json.loads(request.cookies.get(str(current_user.id)))
        return {'num_articulos': len(datos)}
    
@app_blueprint.route('/pedido')
def pedidox():
    try: datos = json.loads(request.cookies.get(str(current_user.id)))
    except:
        datos = []
    total = 0
    for articulo in datos:
        total = total + db.query(articulos).get(articulo["id"]).precio * articulo["cantidad"]
        db.query(articulos).get(articulo["id"]).stock -= articulo["cantidad"]
        db.commit()
    resp = make_response(render_template("pedido.html", total=total))
    resp.set_cookie(str(current_user.id), "", expires=0)
    return resp
    
@app_blueprint.route('/gracias')
#@login_required
def graciasx():
    ok=""
    if ok=="hola":
        try: datos = json.loads(request.cookies.get(str(current_user.id)))
        except:
            datos = []
        total = 0
        for articulo in datos:
            total = total + db.query(articulos).get(articulo["id"]).precio * articulo["cantidad"]
            db.query(articulos).get(articulo["id"]).stock -= articulo["cantidad"]
            db.commit()
        resp = make_response(render_template("pedido.html", total=total))
        resp.set_cookie(str(current_user.id), "", expires=0)
        return resp
    return f"gracias por su compra,{ok}"   
'''


'''@app_blueprint.context_processor
def contar_carrito():
    #datos = json.loads(request.cookies.get(str(session.get('id'))))  # session['id']  session.get('id')
    #datos = json.loads(request.cookies.get(str(session.get('id')), '[]'))
    #if not current_user.is_authenticated:
    #    return {'num_articulos': 0}
    if request.cookies.get(str(session.get('id'))) is None:
        return {'num_articulos': 0}
    else:
        datos = json.loads(request.cookies.get(str(session.get('id'))))
        return {'num_articulos': len(str(datos))}'''
    
@app_blueprint.context_processor
def contar_carrito():
    if request.cookies.get(str(session.get('id'))) is None:
        return {'num_articulos': 0}
    else:
        try:
            datos = json.loads(request.cookies.get(str(session.get('id'))))
            return {'num_articulos': len(datos)}
        except:
            return {'num_articulos': 0}