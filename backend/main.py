from flask import Flask, request, jsonify
from models import db,User,TownHall,ArcherTower,Canon,WizardTower
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

port=5000
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:password@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.route('/')
def hell_world():
     return """
    <html>
    <body>
    <h1>Welcome to my heroes API</h1>
    <ul><a href="/usuarios">Go to all users</a></ul>
    <ul><a href="/townhall">Go to all town hall</a></ul>
    </body>
    </html>
    """

@app.route('/usuarios')
def usuarios():
    try:
        usuarios=User.query.all()
        usuarios_data=[]
        for usuario in usuarios:
            usuario_data={
                'id':usuario.id,
                'nombre':usuario.nombre,
                'Town_Hall':usuario.id_TH,
                'Torre_Aquera':usuario.id_ArcherTowe,
                'Canon':usuario.id_Canon,
                'Wizard_Tower':usuario.id_Wizard,
                'fecha':usuario.fecha_creacion
            }
            usuarios_data.append(usuario_data)
        return jsonify(usuarios_data)
    except:
        return jsonify({"mensaje":"No hay usuarios"})



@app.route('/usuarios/<usuario_id>')
def usuario(usuario_id):
    try:
        usuario=User.query.get(usuario_id)
        usuario_data={
            'id':usuario.id,
            'nombre':usuario.nombre,
            'Town_Hall':usuario.id_TH,
            'Torre_Aquera':usuario.id_ArcherTowe,
            'Canon':usuario.id_Canon,
            'Wizard_Tower':usuario.id_Wizard,
            'fecha':usuario.fecha_creacion
            }
        return jsonify(usuario_data)
    except:
        return jsonify({"mensaje":"No hay usuarios"})


@app.route('/townhall')
def ayuntamientos():
    try:
        ayuntamiento=TownHall.query.all()
        ayuntamientos_data=[]
        for th in ayuntamiento:
            ayuntamiento_data={
                'level':th.id_th,
                'healt':th.TH_hp,
                'img':th.img,
                'Tiempo_Mejora':th.Time_Upgrade,
                'Inicio':th.fecha_mejora,
            }
            ayuntamientos_data.append(ayuntamiento_data)
        return jsonify(ayuntamientos_data)
    except:
        return jsonify({"mensaje":"No hay ayuntamientos"})

@app.route('/townhall/<id>')
def ayuntamiento(id):
    try:
        th=TownHall.query.get(id)
        ayuntamiento_data={
            'level':th.id_th,
            'healt':th.TH_hp,
            'img':th.img,
            'Tiempo_Mejora':th.Time_Upgrade,
            'Inicio':th.fecha_mejora,
        }
        return jsonify(ayuntamiento_data)
    except:
        return jsonify({"mensaje":"No hay usuarios"})

@app.route('/date/<sections>')
def data(section):
    return section

if __name__ == '__main__':
    print("Starting server..")
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0',debug=True, port=port)
    print("Started....")