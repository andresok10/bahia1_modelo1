from flask import Flask
from flask_wtf.csrf import CSRFProtect   #from flask_wtf import FlaskForm,CSRFProtect  # pip install Flask-WTF
#from modelo1 import *
#from fun_inicio_cookie_cart2 import app_blueprint as a
#from fun_inicio_session_get import app_blueprint as a
from fun_inicio1xx import app_blueprint as a
from fun_categorias import app_blueprint as b
from fun_productos import app_blueprint as c
from fun_usuarios import app_blueprint as d
from modelo1 import *
app = Flask(__name__)
app.secret_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
#app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://postgres:123456@localhost:5432/test'
#engine=create_engine('postgresql://ok:7qF6RmXo5vKNJ4QzWOQDD4NyPGigclw9@dpg-cpgajvmct0pc73dag83g-a:5432/db1_dhy6')
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://ok:b5Dko0Kgdnn3L7Oj6Qpl05Lz0rTopmSc@dpg-cphs6eq1hbls73b8isk0-a:5432/db1_oi4n"
# postgresql://ok:rHQrESj4Llaes3LVEL5rWP7yoepeQBVL@dpg-cq0sdm3v2p9s73cfofdg-a/ok1_1kc3
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://okk:wTmHgGld5N1p88fC0UcYg1oZ3DevB3dl@dpg-cq0tr7eehbks73ehlp7g-a/db1_rlpa"
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/bahia1"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://usuario:contraseña@localhost/nombre_base_datos'  # Reemplaza con tu propia configuración de MySQL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#app.config['STRIPE_SECRET_KEY'] = 'sk_test_51LJBxwEpqu9KnJeFKsKsZSeGMNI51RAcOrG7SYa4LrtP7vkvLNXUdjsAXt8flVgb3VITVYqSAJUGMYeDxiaAgRhA002OY7g4L3'
#app.config['SESSION_TYPE'] = 'filesystem'
#app.config['SESSION_TYPE'] = 'sqlalchemy' #RuntimeError: A 'SQLAlchemy' instance has already been registered on this Flask app. Import and use that instance instead.
#app.config['STRIPE_PUBLIC_KEY'] = 'tu_clave_publica_de_stripe'
db.init_app(app)
#from flask_session import Session
#Session(app)
csrf = CSRFProtect(app)

app.register_blueprint(a)
app.register_blueprint(b)
app.register_blueprint(c)
app.register_blueprint(d)

app.app_context().push()
db.create_all()

try:
    db.session.add_all(consultas)
    db.session.commit()
    #db.session.close()
except:
    pass

if __name__ == '__main__':
    #app.app_context().push()
    #db.create_all()
    csrf = CSRFProtect(app)
    app.run(host='0.0.0.0', debug=True)
    #app.run(debug=True)

#ImportError: cannot import name 'app_blueprint1' from partially initialized module 'fun_inicio' (most likely due to a circular import) 
#<a href="/perfil">
#    {{ session['nombre'] }}
#    <!--<img style="width:50px;height:30px;" src="{{url_for('static',filename='images/logos-iconos/perfil1.jpg')}}">-->
#</a>

##@media screen and (min-width:800px) {
#            .titulo{font-size: 18px;justify-content: flex-end}
#            .parrafo_publicidad1 p{font-size:16px;}
#            .cont_nav a{margin: 0px 4px;}
#            .caja_galeria{margin: 0px 4px;}
#            .img_galeriaxxx{width:100%;}
#            h3{display: none;}
#        }