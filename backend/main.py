from flask import Flask, request, jsonify
from models import db,User,TownHall,ArcherTower,Canon
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

port=5000                                                  #postgre user                        database
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:postgres@localhost:5432/TP1intro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False                 #postgre password


@app.route('/')
def hell_world():
     return """
    <html>
    <body>
    <h1>Welcome to my heroes API</h1>
    <ul><a href="/users">Go to all users</a></ul>
    <ul><a href="/townhall">Go to all town hall</a></ul>
    </body>
    </html>
    """

@app.route('/users')
def users():
    try:
        users=User.query.all()
        users_data=[]
        for user in users:
            user_data={
                'id':user.id,
                'name':user.name,
                'Town_Hall':user.id_TH,
                'Archer_Tower':user.id_ArcherTower,
                'Canon':user.id_Canon,
                'money':user.money
            }
            users_data.append(user_data)
        return jsonify(users_data)
    except:
        return jsonify({"mensaje":"No hay usuarios"})



@app.route('/users/<user_id>')
def usuario(user_id):
    try:
        usuario=User.query.get(user_id)
        usuario_data={
            'id':usuario.id,
            'name':usuario.name,
            'Town_Hall':usuario.id_TH,
            'Archer_Tower':usuario.id_ArcherTower,
            'Canon':usuario.id_Canon,
            'money':usuario.money
            }
        return jsonify(usuario_data)
    except:
        return jsonify({"mensaje":"No hay usuarios"})


@app.route('/townhall')
def townhalls():
    try:
        townhall=TownHall.query.all()
        townhalls_data=[]
        for th in townhall:
            townhall_data={
                'level':th.id_th,
                'img':th.img,
                'upgrade_cost':th.upgrade_TH,
            }
            townhalls_data.append(townhall_data)
        return jsonify(townhalls_data)
    except:
        return jsonify({"mensaje":"No hay ayuntamientos"})

@app.route('/townhall/<id>')
def townhall(id):
    try:
        th=TownHall.query.get(id)
        townhall_data={
            'level':th.id_th,
            'img':th.img,
            'upgrade_cost':th.upgrade_TH,
        }
        return jsonify(townhall_data)
    except:
        return jsonify({"mensaje":"No hay usuarios"})

#create tables
if __name__ == '__main__':
    print("Starting server..")
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0',debug=True, port=port)
    print("Started....")