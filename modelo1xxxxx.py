from sqlalchemy import URL,ForeignKey,Column,String,Integer,CHAR,Numeric,Float,Boolean,DECIMAL,DateTime,create_engine,func,select
#from sqlalchemy.orm import sessionmaker,scoped_session,relationship,declarative_base
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class sub_cat(db.Model):
    __tablename__ = "sub_cat"
    id = Column(Integer,primary_key=True,autoincrement=True)                            
    nombre=Column(String(30))
    relacion2 = db.relationship("articulos", back_populates="relacion3" ) # backref="categoriasx"'''
############################################################
class articulos(db.Model):
    __tablename__ = "articulos"
    id = Column(Integer,autoincrement=True, primary_key=True)
    nombre = Column(String(50), nullable=False, unique=True)   # unique=True
    precio = Column(Float, default=0)
    info = Column(String(50))                           
    img1 = Column(String(50))
    img2 = Column(String(50))   
    img3 = Column(String(50))
    stock = Column(Integer, default=1)
    catid = Column(Integer, ForeignKey('sub_cat.id'))
    relacion3 = db.relationship("sub_cat", back_populates="relacion2")
###########################################################
#class usuarios(UserMixin, db.Model):     # UserMixin ya implementa x interno flask-login  
class usuarios(db.Model):        
    __tablename__ = "usuarios"
    id = Column(Integer,autoincrement=True, primary_key=True)
    nombre = Column(String(30), nullable=False)
    usuario = Column(String(30), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    admin = Column(Boolean,default=False)
    #fecha = Column(DateTime, default=datetime.now)
    #fecha = Column(DateTime, default=datetime.today)

    #def is_authenticated(self):
    #    return True
    #def is_active(self):
    #    return True
    #def is_anonymous(self):
    #    return False
    #def get_id(self):
    #    return str(self.id)#return unicode(self.id) 
    #def is_admin(self):
    #    return self.admin  # True+False=1  True+True=2   print(true)=True   False+False=0


try:
    consultas=[
    usuarios(nombre="dave1x",usuario="dave1",password="qqww",email="ok1@gmail.com",admin=True),
    usuarios(nombre="dave2x",usuario="dave2",password="aass",email="ok2@gmail.com",admin=False),

    sub_cat(nombre="blusas"),
    sub_cat(nombre="Faldas/vestidos"),
    sub_cat(nombre="calzado-damas"),
    sub_cat(nombre="accesorio"),

    sub_cat(nombre="camisas/camisetas"),
    sub_cat(nombre="Pantalones"),
    sub_cat(nombre="calzado-caballeros"),
    sub_cat(nombre="accesorio"),

    sub_cat(nombre="blusas"),
    sub_cat(nombre="Faldas/vestidos"),
    sub_cat(nombre="calzado-niña"),
    sub_cat(nombre="accesorio-niño"),

    sub_cat(nombre="camisa/camisetas"),
    sub_cat(nombre="Pantalones"),
    sub_cat(nombre="calzado-niño"),
    sub_cat(nombre="accesorio-niña"),

    # mujer
    articulos(img1="blusa1.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok1",precio=10.22, info="xxx",stock=5,catid=1),
    articulos(img1="blusa2.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok2",precio=20.22, info="xxx",stock=5,catid=1),
    articulos(img1="chaqueta1.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok3",precio=30.22, info="xxx",stock=5,catid=1),
    articulos(img1="chaqueta-casual1.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok4",precio=40.22, info="xxx",stock=5,catid=1),

    articulos(img1="falda1.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok5",precio=10.22, info="xxx",stock=5,catid=2),
    articulos(img1="falda2.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok6",precio=20.22, info="xxx",stock=5,catid=2),
    articulos(img1="vestido1.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok7",precio=30.22, info="xxx",stock=5,catid=2),
    articulos(img1="vestido2.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok8",precio=40.22, info="xxx",stock=5,catid=2),

    articulos(img1="zapato1.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok9",precio=10.22, info="xxx",stock=9,catid=3),
    articulos(img1="zapato6.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok10",precio=20.22, info="xxx",stock=10,catid=3),
    articulos(img1="zapato11.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok11",precio=30.22, info="xxx",stock=11,catid=3),
    articulos(img1="zapato2.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok12",precio=40.22, info="xxx",stock=12,catid=3),

    articulos(img1="cartera1.png",img2="blusa1.webp",img3="blusa1.webp", nombre="ok13",precio=10.22, info="xxx",stock=13,catid=4),
    articulos(img1="cartera2.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok14",precio=20.22, info="xxx",stock=14,catid=4),
    articulos(img1="gafa1.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok15",precio=30.22, info="xxx",stock=15,catid=4),
    articulos(img1="gafa2.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok16",precio=40.22, info="xxx",stock=16,catid=4),
    # hombre
    articulos(img1="camisa1.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok17",precio=10.22, info="xxx",stock=1,catid=5),
    articulos(img1="camisa2.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok18",precio=20.22, info="xxx",stock=2,catid=5),
    articulos(img1="camisa3.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok19",precio=30.22, info="xxx",stock=3,catid=5),
    articulos(img1="camisa4.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok20",precio=40.22, info="xxx",stock=4,catid=5),

    articulos(img1="pantalon1.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok21",precio=10.22, info="xxx",stock=5,catid=6), 
    articulos(img1="pantalon2.jpeg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok22",precio=20.22, info="xxx",stock=6,catid=6),
    articulos(img1="pantalon3.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok23",precio=30.22, info="xxx",stock=7,catid=6),
    articulos(img1="pantalon4.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok24",precio=40.22, info="xxx",stock=8,catid=6),

    articulos(img1="zapato1.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok25",precio=10.22, info="xxx",stock=9,catid=7),
    articulos(img1="zapato2.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok26",precio=20.22, info="xxx",stock=10,catid=7),
    articulos(img1="zapato3.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok27",precio=30.22, info="xxx",stock=11,catid=7),
    articulos(img1="zapato4.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok28",precio=40.22, info="xxx",stock=12,catid=7),

    articulos(img1="gafa1.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok29",precio=10.22, info="xxx",stock=13,catid=8),
    articulos(img1="gorra1.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok30",precio=20.22, info="xxx",stock=14,catid=8),
    articulos(img1="gafa2.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok31",precio=30.22, info="xxx",stock=15,catid=8),
    articulos(img1="gorra2.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok32",precio=40.22, info="xxx",stock=16,catid=8),
    # niños
    articulos(img1="camisa1.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok33",precio=10.22, info="xxx",stock=1,catid=9),
    articulos(img1="camisa2.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok34",precio=20.22, info="xxx",stock=2,catid=9),
    articulos(img1="camisa3.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok35",precio=30.22, info="xxx",stock=3,catid=9),
    articulos(img1="camisa4.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok36",precio=40.22, info="xxx",stock=4,catid=9),

    articulos(img1="pantalon1.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok37",precio=10.22, info="xxx",stock=5,catid=10), 
    articulos(img1="pantalon2.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok38",precio=20.22, info="xxx",stock=6,catid=10),
    articulos(img1="pantalon3.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok39",precio=30.22, info="xxx",stock=7,catid=10),
    articulos(img1="pantalon4.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok40",precio=40.22, info="xxx",stock=8,catid=10),

    articulos(img1="zapato1.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok41",precio=10.22, info="xxx",stock=1,catid=11),
    articulos(img1="zapato2.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok42",precio=20.22, info="xxx",stock=1,catid=11),
    articulos(img1="zapato3",img2="blusa1.webp",img3="blusa1.webp", nombre="ok43",precio=30.22, info="xxx",stock=1,catid=11),
    articulos(img1="zapato4",img2="blusa1.webp",img3="blusa1.webp", nombre="ok44",precio=40.22, info="xxx",stock=1,catid=11),

    articulos(img1="gorra1.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok45",precio=10.22, info="xxx",stock=1,catid=12),
    articulos(img1="gorra2.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok46",precio=20.22, info="xxx",stock=1,catid=12),
    articulos(img1="gorra3.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok47",precio=30.22, info="xxx",stock=1,catid=12),
    articulos(img1="gorra4.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok48",precio=40.22, info="xxx",stock=1,catid=12),
    # niñas
    articulos(img1="blusa1.png",img2="blusa1.webp",img3="blusa1.webp", nombre="ok49",precio=10.22, info="xxx",stock=1,catid=13),
    articulos(img1="blusa2.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok50",precio=20.22, info="xxx",stock=1,catid=13),
    articulos(img1="blusa3.png",img2="blusa1.webp",img3="blusa1.webp", nombre="ok51",precio=30.22, info="xxx",stock=1,catid=13),
    articulos(img1="blusa4.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok52",precio=40.22, info="xxx",stock=1,catid=13),

    articulos(img1="pantalon1.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok53",precio=10.22, info="xxx",stock=1,catid=14), 
    articulos(img1="pantalon2.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok54",precio=20.22, info="xxx",stock=1,catid=14),
    articulos(img1="pantalon3.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok55",precio=30.22, info="xxx",stock=1,catid=14),
    articulos(img1="vestido1.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok56",precio=40.22, info="xxx",stock=1,catid=14),

    articulos(img1="zapato-niña1.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok57",precio=10.22, info="xxx",stock=1,catid=15),
    articulos(img1="zapato-niña3.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok58",precio=20.22, info="xxx",stock=1,catid=15),
    articulos(img1="zapato-niña4.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok59",precio=30.22, info="xxx",stock=1,catid=15),
    articulos(img1="zapato-niña5.webp",img2="blusa1.webp",img3="blusa1.webp", nombre="ok60",precio=40.22, info="xxx",stock=1,catid=15),

    articulos(img1="zgafa-niña1.jpeg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok61",precio=10.22, info="xxx",stock=1,catid=16),
    articulos(img1="zgafa-niña2.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok62",precio=20.22, info="xxx",stock=1,catid=16),
    articulos(img1="zgafa-niña3.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok63",precio=30.22, info="xxx",stock=1,catid=16),
    articulos(img1="zgafa-h1.jpg",img2="blusa1.webp",img3="blusa1.webp", nombre="ok64",precio=40.22, info="xxx",stock=1,catid=16)
    ]
    #db.add_all(consultas)
    #db.commit()
    #db.close()
    
except:
    pass
