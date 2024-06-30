#from werkzeug.utils import secure_filename
from flask import Flask, request, redirect, render_template, url_for, session, Blueprint
from modelo1 import db, cat, subcat_mujer, subcat_hombre, articulos, usuarios, Pedido,DetallePedido
import stripe
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import sys, os
app_blueprint = Blueprint('fun_inicio', __name__)
######################################### inicio ############################ onclick="cambiarColor(this)"  id="agregarBtn" 
# /inicio/{{artx.id}}         #{{ url_for('iniciox') }}
# <input type="hidden" name="product" value="{{ artx.id }}">
# {{ url_for('iniciox', id=artx.id) }}

#cat1 = sub_cat.query.filter_by(catid=id).all() if id else sub_cat.query.all()  # Filter subcategories based on category id
#art1 = articulos.query.filter_by(catid=id).all() if id else articulos.query.all()    

cart = []

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

@app_blueprint.route('/', methods=["get"])
@app_blueprint.route('/inicio_uno', methods=["get","post"])
@app_blueprint.route('/inicio_uno/<int:id>', methods=["get","post"])
def inicio1(id=1):
    initialize_cart()
    cat1 = cat.query.all()
    sub1 = subcat_mujer.query.all()
    #subx = subcat_mujer.query.filter_by(sub_mujer=id).all()
    art1 = articulos.query.filter_by(sub_mujer=id).all()
    #art1 = articulos.query.filter_by(id=id).all()
    if request.method == 'POST':
        product_id = int(request.form['product'])
        cantidadx = int(request.form['cantidad'])
        idx = articulos.query.get(product_id)
        actualizar = False
        if idx is not None:
            for x in cart:
                if x["id"] == idx.id:
                    x["stock"] = cantidadx
                    actualizar = True
        if not actualizar:
            cart.append({'id': idx.id, 'img1': idx.img1, 'nombre': idx.nombre, 'precio': idx.precio, "stock": cantidadx})
        session['contador'] = len(cart)
        return redirect(url_for("fun_inicio.inicio1", id=id))
    #return render_template("mujer-final2.html", art1=art1, cat1=cat1, sub1=sub1,)
    #return render_template("mujer_final3.html", art1=art1, cat1=cat1, sub1=sub1,)
    return render_template("f1.html", art1=art1, cat1=cat1, sub1=sub1,)

@app_blueprint.route('/inicio_dos', methods=["get"])
@app_blueprint.route('/inicio_dos/<int:id>', methods=["get","post"])
def inicio2(id=1):
    initialize_cart()
    cat1 = cat.query.all()
    sub1 = subcat_hombre.query.all()
    art1 = articulos.query.filter_by(sub_hombre=id).all()
    if request.method == 'POST':
        product_id = int(request.form['product'])
        cantidadx = int(request.form['cantidad'])
        idx = articulos.query.get(product_id)
        actualizar = False
        if idx is not None:
            for x in cart:
                if x["id"] == idx.id:
                    x["stock"] = cantidadx
                    actualizar = True
        if not actualizar:
            cart.append({'id': idx.id, 'img1': idx.img1, 'nombre': idx.nombre, 'precio': idx.precio, "stock": cantidadx})
        session['contador'] = len(cart)
        return redirect(url_for("fun_inicio.inicio2", id=id))
    return render_template("f2.html", art1=art1, cat1=cat1, sub1=sub1, )
    
#cat1 = sub_cat.query.filter_by(catid=id).all() #if id else sub_cat.query.all()  # Filter subcategories based on category id
#art1 = articulos.query.filter_by(catid=id).all() #if id else articulos.query.all()
#cat2 = cat.query.filter_by(id=not None).all()
#subcat1 = subcat.query.filter_by(catid=id).all() if id else []
#print(f"{subcat1}")
    
############################################## carrito #########################################################
@app_blueprint.route('/carrito', methods=["GET", "POST"])
def carritox():
    msg = ""
    if request.method == 'POST':
        cantidadx = int(request.form['cantidad'])
        product_id = int(request.form['product'])
        idx = articulos.query.filter_by(id=product_id).first()
        if idx and cantidadx <= idx.stock:
            actualizar = False
            for x in cart:
                if x["id"] == idx.id:
                    x["stock"] = cantidadx
                    actualizar = True
                    #break
            if not actualizar:
                cart.append({'id': idx.id, 'img1': idx.img1, 'nombre': idx.nombre, 'precio': idx.precio, 'stock': cantidadx})
            session['cart'] = cart
        #if request.method == 'POST' and int(request.form['cantidad']) > idxx.stock:
        else:
            msg = "No hay suficiente stock"
    #total = sum(item['precio']*item['stock'] + (item['precio']*item['stock']*12/100) for item in cart)  # + subtotal*12/100 
    total = sum(item['precio'] * item['stock'] * 1.12 for item in cart)  # Including 12% tax
    #total = sum(item['precio'] * item['stock'] * 0.12 for item in cart)  # Including 12% tax
    session["total"] = total
    return render_template('cart.html', cart=cart, total=total, msg=msg)

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

#################################################################
@app_blueprint.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    global cart
    cart = [item for item in cart if item['id'] != product_id]
    session['cart'] = cart
    session['contador'] = len(cart)
    return redirect(url_for('fun_inicio.carritox'))

#################################################################
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