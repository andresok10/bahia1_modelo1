from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey,Column,String,Integer,CHAR,Numeric,Float,Boolean,DECIMAL,DateTime,Text
db = SQLAlchemy()
############################################################
class cat(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(20), nullable=False)

class subcat_mujer(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(20), nullable=False)
    img1 = Column(String(50))
    sub_mujer = Column(Integer)

class subcat_hombre(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(20), nullable=False)
    img1 = Column(String(50))
    sub_hombre = Column(Integer)

##########################################################
class articulos(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(30), nullable=False)  #, unique=True
    precio = Column(Float, default=0)
    info = Column(String(20))                           
    img1 = Column(String(20))
    stock = Column(Integer, default=1)
    sub_mujer = Column(Integer)
    sub_hombre = Column(Integer)
    #sub_mujer = Column(String(10))
    #sub_hombre = Column(String(10))

    #re_fact = db.relationship("car_factura", back_populates="re_articulo")
    #def __repr__(self):
    #    return self.nombre
    #con back_populates 
    #relacion2 = db.relationship("sub_cat", back_populates="relacion1")

###########################################################
class usuarios(db.Model):
    id = Column(Integer,autoincrement=True, primary_key=True)
    nombre = Column(String(30), nullable=False)
    usuario = Column(String(30), nullable=False, unique=True) #,unique=True
    password = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    admin = Column(Boolean, default=False)
    #fecha = Column(DateTime, default=datetime.now)
    #fecha = Column(DateTime, default=datetime.today)

class Pedido(db.Model):
    id = Column(Integer, primary_key=True)
    #usuario_id = Column(Integer)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))  # Cambiar el nombre de la columna y la referencia a la tabla de usuarios
    #fecha = db.Column(db.DateTime, default=datetime.now)
    total = Column(Float)
    detalles = db.relationship('DetallePedido', backref='pedido', lazy=True)

class DetallePedido(db.Model):
    id = Column(Integer, primary_key=True)
    producto_id = Column(Integer)
    cantidad = Column(Integer)
    precio = Column(Float)
    pedido_id = Column(Integer, ForeignKey('pedido.id'))

    # hombre  camisas
    #articulos(img1="1.jpg",nombre="ok48",precio=10.22, info="xxx",stock=1, sub_mujer=0, sub_hombre=1),
    #articulos(img1="2.webp",nombre="ok49",precio=20.22, info="xxx",stock=2, sub_mujer=0, sub_hombre=1),
    #articulos(img1="3.webp",nombre="ok50",precio=10.22, info="xxx",stock=1, sub_mujer=0, sub_hombre=1),
    #articulos(img1="4.webp",nombre="ok51",precio=20.22, info="xxx",stock=2, sub_mujer=0, sub_hombre=1),
    # pantalon
    #articulos(img1="1.webp",nombre="ok48",precio=10.22, info="xxx",stock=1, sub_mujer=0, sub_hombre=2),
    #articulos(img1="2.jpeg",nombre="ok49",precio=20.22, info="xxx",stock=2, sub_mujer=0, sub_hombre=2),
    #articulos(img1="3.jpg",nombre="ok50",precio=10.22, info="xxx",stock=1, sub_mujer=0, sub_hombre=2),
    #articulos(img1="4.webp",nombre="ok51",precio=20.22, info="xxx",stock=2, sub_mujer=0, sub_hombre=2),
    # abrigos
    #articulos(img1="1.webp",nombre="ok48",precio=10.22, info="xxx",stock=1, sub_mujer=0, sub_hombre=3),
    #articulos(img1="2.jpg",nombre="ok49",precio=20.22, info="xxx",stock=2, sub_mujer=0, sub_hombre=3),
    #articulos(img1="3.jpg",nombre="ok50",precio=10.22, info="xxx",stock=1, sub_mujer=0, sub_hombre=3),
    #articulos(img1="4.jpg",nombre="ok51",precio=20.22, info="xxx",stock=2, sub_mujer=0, sub_hombre=3),
    # chaquetas
    #articulos(img1="1.jpg",nombre="ok48",precio=10.22, info="xxx",stock=1, sub_mujer=0, sub_hombre=4),
    #articulos(img1="2.jpg",nombre="ok49",precio=20.22, info="xxx",stock=2, sub_mujer=0, sub_hombre=4),
    #articulos(img1="3.jpg",nombre="ok50",precio=10.22, info="xxx",stock=1, sub_mujer=0, sub_hombre=4),
    #articulos(img1="4.webp",nombre="ok51",precio=20.22, info="xxx",stock=2, sub_mujer=0, sub_hombre=4)

#]

try:
    consultas=[
    usuarios(nombre="dave1x",usuario="dave1",password="qqww",email="ok1@gmail.com",admin=True),
    usuarios(nombre="dave2x",usuario="dave2",password="aass",email="ok2@gmail.com",admin=False),

    cat(nombre="Mujer"),
    cat(nombre="Hombre"),
    cat(nombre="Niño"),
    cat(nombre="Niña"),

    subcat_mujer(nombre="Blusas y Camisetas", img1="1.png", sub_mujer=1),
    subcat_mujer(nombre="Faldas",             img1="2.webp", sub_mujer=2),
    subcat_mujer(nombre="Pantalon",           img1="3.webp", sub_mujer=3),
    subcat_mujer(nombre="Trajes de Baño",     img1="4.webp", sub_mujer=4),
    subcat_mujer(nombre="Shorts",             img1="5.jpg", sub_mujer=5),
    subcat_mujer(nombre="Vestidos Elegantes", img1="6.jpg", sub_mujer=6),
    subcat_mujer(nombre="Conjuntos/Enterizos", img1="7.jpg", sub_mujer=7),
    subcat_mujer(nombre="Para Trabajo",         img1="8.webp", sub_mujer=8),
    subcat_mujer(nombre="Chaquetas/Abrigos", img1="9.jpg", sub_mujer=9),
    subcat_mujer(nombre="Zapatos",            img1="10.jpg", sub_mujer=10),
    subcat_mujer(nombre="Joyeria y Accesorios", img1="11.jpg", sub_mujer=11),
    subcat_mujer(nombre="Perfumes y Maquillajes",img1="12.jpg", sub_mujer=12),

    subcat_hombre(nombre="camisas y camisetas", img1="1.jpg", sub_hombre=1),
    subcat_hombre(nombre="Pantalon",        img1="2.png", sub_hombre=2),
    subcat_hombre(nombre="Sudaderas y Abrigos", img1="3.jpg", sub_hombre=3),
    subcat_hombre(nombre="Chaquetas",          img1="5.webp", sub_hombre=4),
    subcat_hombre(nombre="Trajes Elegantes",   img1="5.webp", sub_hombre=5),
    subcat_hombre(nombre="Ropa de Baño",       img1="6.jpg", sub_hombre=6),
    subcat_hombre(nombre="Gorras y Bolsos",    img1="7.jpg", sub_hombre=7),
    subcat_hombre(nombre="Zapatos",            img1="8.png",     sub_hombre=8),
    subcat_hombre(nombre="Joyeria y Accesorios", img1="9.jpg", sub_hombre=9),

    # mujer  blusas
    articulos(img1="blusa1.webp", nombre="ok1",precio=10.22, info="xxx",stock=2, sub_mujer=1, sub_hombre=0),
    articulos(img1="blusa2.webp", nombre="ok2",precio=20.22, info="xxx",stock=3, sub_mujer=1, sub_hombre=0),
    articulos(img1="blusa3.jpg", nombre="ok3",precio=10.22, info="xxx",stock=2, sub_mujer=1, sub_hombre=0),
    articulos(img1="blusa4.jpg", nombre="ok4",precio=20.22, info="xxx",stock=3, sub_mujer=1, sub_hombre=0),
    # faldas
    articulos(img1="falda1.jpg",nombre="ok5",precio=10.22, info="xxx",stock=5, sub_mujer=2, sub_hombre=0),
    articulos(img1="falda2.jpg",nombre="ok6",precio=20.22, info="xxx",stock=5, sub_mujer=2, sub_hombre=0),
    articulos(img1="falda3.jpg",nombre="ok7",precio=10.22, info="xxx",stock=5, sub_mujer=2, sub_hombre=0),
    articulos(img1="falda4.jpg",nombre="ok8",precio=20.22, info="xxx",stock=5, sub_mujer=2, sub_hombre=0),
    #pantalon
    articulos(img1="1.jpg",nombre="ok9",precio=10.22, info="xxx",stock=5, sub_mujer=3, sub_hombre=0),
    articulos(img1="2.webp",nombre="ok10",precio=20.22, info="xxx",stock=5, sub_mujer=3, sub_hombre=0),
    articulos(img1="3.jpg",nombre="ok11",precio=10.22, info="xxx",stock=5, sub_mujer=3, sub_hombre=0),
    articulos(img1="4.webp",nombre="ok12",precio=20.22, info="xxx",stock=5, sub_mujer=3, sub_hombre=0),
    # Trajes de baño
    articulos(img1="1.webp",nombre="ok13",precio=10.22, info="xxx",stock=5, sub_mujer=4, sub_hombre=0),
    articulos(img1="2.jpg",nombre="ok14",precio=20.22, info="xxx",stock=5, sub_mujer=4, sub_hombre=0),
    articulos(img1="3.webp",nombre="ok15",precio=10.22, info="xxx",stock=5, sub_mujer=4, sub_hombre=0),
    articulos(img1="4.webp",nombre="ok16",precio=20.22, info="xxx",stock=5, sub_mujer=4, sub_hombre=0),
    # short
    articulos(img1="1.webp",nombre="ok16",precio=10.22, info="xxx",stock=5, sub_mujer=5, sub_hombre=0),
    articulos(img1="2.webp",nombre="ok17",precio=20.22, info="xxx",stock=5, sub_mujer=5, sub_hombre=0),
    articulos(img1="3.webp",nombre="ok18",precio=10.22, info="xxx",stock=5, sub_mujer=5, sub_hombre=0),
    articulos(img1="4.jpg",nombre="ok19",precio=20.22, info="xxx",stock=5, sub_mujer=5, sub_hombre=0),
    # vestidos
    articulos(img1="1.webp",nombre="ok20",precio=10.22, info="xxx",stock=5, sub_mujer=6, sub_hombre=0),
    articulos(img1="3.webp",nombre="ok21",precio=20.22, info="xxx",stock=5, sub_mujer=6, sub_hombre=0),
    articulos(img1="9.jpg",nombre="ok122",precio=10.22, info="xxx",stock=5, sub_mujer=6, sub_hombre=0),
    articulos(img1="11.jpg",nombre="ok23",precio=20.22, info="xxx",stock=5, sub_mujer=6, sub_hombre=0),
    # conjuntos
    articulos(img1="1.jpg",nombre="ok24",precio=10.22, info="xxx",stock=5, sub_mujer=7, sub_hombre=0),
    articulos(img1="2.jpg",nombre="ok25",precio=20.22, info="xxx",stock=5, sub_mujer=7, sub_hombre=0),
    articulos(img1="1.jpg",nombre="ok26",precio=10.22, info="xxx",stock=5, sub_mujer=7, sub_hombre=0),
    articulos(img1="2.jpg",nombre="ok27",precio=20.22, info="xxx",stock=5, sub_mujer=7, sub_hombre=0),
    # Para Trabajo
    articulos(img1="1.jpg",nombre="ok28",precio=10.22, info="xxx",stock=5, sub_mujer=8, sub_hombre=0),
    articulos(img1="2.webp",nombre="ok29",precio=20.22, info="xxx",stock=5, sub_mujer=8, sub_hombre=0),
    articulos(img1="3.webp",nombre="ok30",precio=10.22, info="xxx",stock=5, sub_mujer=8, sub_hombre=0),
    articulos(img1="4.webp",nombre="ok31",precio=20.22, info="xxx",stock=5, sub_mujer=8, sub_hombre=0),
    # chaquteas y abrigos
    articulos(img1="1.webp",nombre="ok32",precio=10.22, info="xxx",stock=5, sub_mujer=9, sub_hombre=0),
    articulos(img1="4.png",nombre="ok33",precio=20.22, info="xxx",stock=5, sub_mujer=9, sub_hombre=0),
    articulos(img1="chaqueta1.jpg",nombre="ok34",precio=10.22, info="xxx",stock=5, sub_mujer=9, sub_hombre=0),
    articulos(img1="chaqueta1.jpg",nombre="ok35",precio=20.22, info="xxx",stock=5, sub_mujer=9, sub_hombre=0),
    # zapatos
    articulos(img1="1.webp",nombre="ok36",precio=10.22, info="xxx",stock=5, sub_mujer=10, sub_hombre=0),
    articulos(img1="2.webp",nombre="ok37",precio=20.22, info="xxx",stock=5, sub_mujer=10, sub_hombre=0),
    articulos(img1="3.webp",nombre="ok38",precio=10.22, info="xxx",stock=5, sub_mujer=10, sub_hombre=0),
    articulos(img1="4.jpg",nombre="ok39",precio=20.22, info="xxx",stock=5, sub_mujer=10, sub_hombre=0),
    # accesorios
    articulos(img1="1.png",nombre="ok40",precio=10.22, info="xxx",stock=5, sub_mujer=11, sub_hombre=0),
    articulos(img1="2.jpg",nombre="ok41",precio=20.22, info="xxx",stock=5, sub_mujer=11, sub_hombre=0),
    articulos(img1="3.webp",nombre="ok42",precio=10.22, info="xxx",stock=5, sub_mujer=11, sub_hombre=0),
    articulos(img1="4.jpg",nombre="ok43",precio=20.22, info="xxx",stock=5, sub_mujer=11, sub_hombre=0),
    # maquillaje
    articulos(img1="m1.jpg",nombre="ok44",precio=10.22, info="xxx",stock=5, sub_mujer=12, sub_hombre=0),
    articulos(img1="m2.jpg",nombre="ok45",precio=20.22, info="xxx",stock=5, sub_mujer=12, sub_hombre=0),
    articulos(img1="m3.jpg",nombre="ok46",precio=10.22, info="xxx",stock=5, sub_mujer=12, sub_hombre=0),
    articulos(img1="m4.jpg",nombre="ok47",precio=20.22, info="xxx",stock=5, sub_mujer=12, sub_hombre=0),
]
    db.session.add_all(consultas)
    db.session.commit()
    db.session.close()
except:
    #break
    pass
