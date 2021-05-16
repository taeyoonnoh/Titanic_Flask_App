from titanic_app import db

# csv 에 있는 데이터를 담기 위한 모델
# 이후 시각화를 하기 위한 모델
# `Edit_Titanic` 모델을 `Titanic` 모델에 추가할 것 
class Titanic(db.Model) :
    __tablename__ = "titanic"

    passenger_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(128))
    gender = db.Column(db.String)
    age = db.Column(db.Integer,nullable=True)
    fare = db.Column(db.Float)
    embarked = db.Column(db.String)
    pclass = db.Column(db.String)
    survived = db.Column(db.String)

    def __init__(self,name,gender,age,fare,embarked,pclass,survived) :
        self.name = name
        self.gender = gender
        self.age = age
        self.fare = fare
        self.embarked = embarked
        self.pclass = pclass
        self.survived = survived
