
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


@app.route('/canon')
def canons():
    try:
        canons = Canon.query.all()
        canons_data = []
        for canon in canons:
            canon_data = { 
            'level': canon.id_Canon, 
            'img': canon.img, 
            'unlock':canon.Unlock_THLvl,
            'upgrade_cost': canon.upgrade_Canon,
            'money_given':canon.moneygiven_Canon }
            
            canons_data.append(canon_data)
        return jsonify(canons_data)
    except:
        return jsonify({"mensaje": "No hay cañones"})

@app.route('/archertower')
def archertowers():
    try:
        archertowers = ArcherTower.query.all()
        archertowers_data = []
        for tower in archertowers:
            tower_data = { 
            'level': tower.id_AT, 
            'img': tower.img, 
            'unlock':tower.Unlock_THLvl,
            'upgrade_cost': tower.upgrade_AT,
            'money_given':tower.moneygiven_AT }           
                     
            archertowers_data.append(tower_data)
        return jsonify(archertowers_data)
    except:
        return jsonify({"mensaje": "No hay torres de arqueros"})

@app.route('/canon/<id>')
def canon(id):
    try:
        canon = Canon.query.get(id)
        if not canon:
            return jsonify({"mensaje": "No hay cañon con ese ID"}), 404
            canon_data = { 
            'level': canon.id_Canon, 
            'img': canon.img, 
            'unlock':canon.Unlock_THLvl,
            'upgrade_cost': canon.upgrade_Canon,
            'money_given':canon.moneygiven_Canon } 
        return jsonify(canon_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/archertower/<id>')
def archertower(id):
    try:
        tower = ArcherTower.query.get(id)
        if not tower:
            return jsonify({"mensaje": "No hay torre de arquero con ese ID"}), 404
            tower_data = { 
            'level': tower.id_AT, 
            'img': tower.img, 
            'unlock':tower.Unlock_THLvl,
            'upgrade_cost': tower.upgrade_AT,
            'money_given':tower.moneygiven_AT } 
        return jsonify(tower_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#create tables
if __name__ == '__main__':
    print("Starting server..")
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0',debug=True, port=port)
    print("Started....")