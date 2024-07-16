from flask_sqlalchemy import SQLAlchemy



db= SQLAlchemy()

#User table
class User(db.Model):
    __tablename__='user'
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(255),nullable=False)
    id_TH=db.Column(db.Integer, db.ForeignKey('town_hall.id_th'),default=1)
    id_ArcherTower=db.Column(db.Integer, db.ForeignKey('archer_tower.id_AT'),default=1)
    id_Canon=db.Column(db.Integer, db.ForeignKey('canon.id_Canon'),default=1)
    id_Wizard=db.Column(db.Integer, db.ForeignKey('wizard_tower.id_WT'),default=1)
    money=db.Column(db.Integer, default=0)


#Town Hall table = TH
class TownHall(db.Model):
    __tablename__='town_hall'
    id_th= db.Column(db.Integer, primary_key=True)
    TH_hp=db.Column(db.Integer,nullable=False)
    img=db.Column(db.String(255),nullable=False)
    upgrade_TH=db.Column(db.Integer, nullable=False)
    moneygiven_TH=db.Column(db.Integer,nullable=False)


#Archer Tower table = AT   
class ArcherTower(db.Model):
    __tablename__='archer_tower'
    id_AT= db.Column(db.Integer, primary_key=True)
    img=db.Column(db.String(255),nullable=False)
    Unlock_THLvl=db.Column(db.Integer, nullable=False)
    upgrade_AT=db.Column(db.Integer, nullable=False)
    moneygiven_AT=db.Column(db.Integer,nullable=False)

#Canon table
class Canon(db.Model):
    __tablename__='canon'
    id_Canon= db.Column(db.Integer, primary_key=True)
    img=db.Column(db.String(255),nullable=False)
    Unlock_THLvl=db.Column(db.Integer, nullable=False)
    upgrade_Canon=db.Column(db.Integer, nullable=False)
    moneygiven_Canon=db.Column(db.Integer,nullable=False)

#Wizard Tower table = WT
class WizardTower(db.Model):
    __tablename__='wizard_tower'
    id_WT= db.Column(db.Integer, primary_key=True)
    img=db.Column(db.String(255),nullable=False)
    Unlock_THLvl=db.Column(db.Integer, nullable=False)
    upgrade_WT=db.Column(db.Integer, nullable=False)
    moneygiven_WT=db.Column(db.Integer,nullable=False)