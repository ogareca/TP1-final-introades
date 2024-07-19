from flask import Flask, request, jsonify
from models import db,User,TownHall,ArcherTower,Canon
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

port=5000                                                  #postgre user                        database
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:postgres@localhost:5432/tp1intro'
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

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    id_TH = data.get('id_TH', 1)
    id_ArcherTower = data.get('id_ArcherTower', 1)  
    id_Canon = data.get('id_Canon', 1)  

    if not name:
        return jsonify({"error": "El nombre es requerido"}), 400

    try:
        new_user = User(name=name, id_TH=id_TH, id_ArcherTower=id_ArcherTower, id_Canon=id_Canon, money=0)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "Usuario creado", "id": new_user.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


#create tables
if __name__ == '__main__':
    print("Starting server..")
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0',debug=True, port=port)
    print("Started....")