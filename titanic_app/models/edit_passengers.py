from titanic_app import db

# 추가 / 수정 / 삭제를 하기 위한 모델
class Edit_Titanic(db.Model) :
    __tablename__ = "edit_titanic"

    passenger_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(64))
    gender = db.Column(db.VARCHAR(32))
    age = db.Column(db.Integer)
    fare = db.Column(db.Float)
    embarked = db.Column(db.VARCHAR(32))
    pclass = db.Column(db.VARCHAR(32))
    survived = db.Column(db.VARCHAR(32))

    def __init__(self,name,gender,age,fare,embarked,pclass,survived) :
        self.name = name
        self.gender = gender
        self.age = age
        self.fare = fare
        self.embarked = embarked
        self.pclass = pclass
        self.survived = survived