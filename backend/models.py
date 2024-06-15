import datetime
from flask_sqlalchemy import SQLAlchemy


db= SQLAlchemy()

class User(db.Model):
    __tablename__='user'
    id= db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(255),nullable=False)
    id_TH=db.Column(db.Integer, db.ForeignKey('town_hall.id_th'),default=1)
    id_ArcherTowe=db.Column(db.Integer, db.ForeignKey('archer_tower.id_AT'),default=1)
    id_Canon=db.Column(db.Integer, db.ForeignKey('canon.id_Canon'),default=1)
    id_Wizard=db.Column(db.Integer, db.ForeignKey('wizard_tower.id_WT'),default=1)
    fecha_creacion=db.Column(db.DateTime, default=datetime.datetime.now())


#Town Hall =TH = ayuntamiento
class TownHall(db.Model):
    __tablename__='town_hall'
    id_th= db.Column(db.Integer, primary_key=True)
    TH_hp=db.Column(db.Integer,nullable=False)
    img=db.Column(db.String(255),nullable=False)
    Time_Upgrade=db.Column(db.DateTime, nullable=False)
    fecha_mejora=db.Column(db.DateTime, default=datetime.datetime.now())


#AT = Archer Tower    
class ArcherTower(db.Model):
    __tablename__='archer_tower'
    id_AT= db.Column(db.Integer, primary_key=True)
    AT_hp=db.Column(db.Integer,nullable=False)
    AT_damage=db.Column(db.Integer,nullable=False)

    Unlock_THLvl=db.Column(db.Integer, nullable=False)
    Time_Upgrade=db.Column(db.DateTime, nullable=False)
    fecha_mejora=db.Column(db.DateTime, default=datetime.datetime.now())

    
class Canon(db.Model):
    __tablename__='canon'
    id_Canon= db.Column(db.Integer, primary_key=True)
    Canon_hp=db.Column(db.Integer,nullable=False)
    Canon_damage=db.Column(db.Integer,nullable=False)

    Unlock_THLvl=db.Column(db.Integer, nullable=False)
    Time_Upgrade=db.Column(db.DateTime, nullable=False)
    fecha_mejora=db.Column(db.DateTime, default=datetime.datetime.now())

#WT=Wizard Tower
class WizardTower(db.Model):
    __tablename__='wizard_tower'
    id_WT= db.Column(db.Integer, primary_key=True)
    WT_hp=db.Column(db.Integer,nullable=False)
    WT_damage=db.Column(db.Integer,nullable=False)

    Unlock_THLvl=db.Column(db.Integer, nullable=False)
    Time_Upgrade=db.Column(db.DateTime, nullable=False)
    fecha_mejora=db.Column(db.DateTime, default=datetime.datetime.now())
