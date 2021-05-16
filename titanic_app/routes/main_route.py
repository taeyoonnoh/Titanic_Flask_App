from flask import Blueprint, render_template, request,redirect,url_for
from titanic_app.models.titanic_passesngers import Titanic
from titanic_app.models.edit_passengers import Edit_Titanic
from titanic_app import db
import pandas as pd

bp = Blueprint('main', __name__)

@bp.route("/",methods=['GET','POST'])
def index() :

    # 데이터 조회
    if request.method=="POST" :
        min_age = request.form['minage']
        max_age = request.form['maxage']
        min_fare = request.form['minfare']
        max_fare = request.form['maxfare']
        gender = request.form['gender']
        return redirect(url_for("main.read_titanic", 
            min_age=min_age,
            max_age=max_age, 
            min_fare=min_fare, 
            max_fare = max_fare,
            gender=gender
        ))

    # 이것은 로컬일 때만 사용 가능
    # df = pd.read_csv(r'C:\Users\lge\Desktop\assignment\titanic_flask\train.csv')

    # heroku 에서는 깃헙에 업로드 한 것을 사용해야 함
    url = 'https://raw.githubusercontent.com/taeyoonnoh/Titanic_with_Visualization/master/train.csv'
    df = pd.read_csv(url,sep=",")
    df = df.dropna(subset=['Age'])
    df = df.reset_index(drop=True)
    
    check_titanic = db.session.query(Titanic).first()
    
    # 데이터베이스에 아무것도 없다면 데이터 추가하기
    if not check_titanic :    
        for i in range(len(df)) :
            name = df['Name'][i]
            gender = df['Sex'][i]
            age = df['Age'][i]
            fare = df['Fare'][i]
            embarked = df['Embarked'][i]
            pclass = str(df['Pclass'][i])
            survived = str(df['Survived'][i])
            titanic = Titanic(name,gender,age,fare,embarked,pclass,survived)
            db.session.add(titanic)
            db.session.commit()
    
    all_titanic_info = db.session.query(Titanic).all()

    return render_template("first.html",info = all_titanic_info)

# 조건에 맞게 조회
@bp.route("/<gender>/<min_age>/<max_age>/<min_fare>/<max_fare>") 
def read_titanic(gender,min_age,max_age,min_fare,max_fare) :     
    check_age = db.session.query(Titanic).filter(Titanic.age<min_age).all()
    for i in check_age : 
        db.session.delete(i)
    
    check_age = db.session.query(Titanic).filter(Titanic.age>max_age).all()
    for i in check_age :
        db.session.delete(i)
    
    check_fare = db.session.query(Titanic).filter(Titanic.fare<min_fare).all()
    for i in check_fare :
        db.session.delete(i)
    
    check_fare = db.session.query(Titanic).filter(Titanic.fare>max_fare).all()
    for i in check_fare :
        db.session.delete(i)
    
    if gender == 'male' :
        check_gender = db.session.query(Titanic).filter(Titanic.gender=='female').all()
        for i in check_gender:
            db.session.delete(i)
    elif gender =='female' :
        check_gender = db.session.query(Titanic).filter(Titanic.gender=='male').all()
        for i in check_gender:
            db.session.delete(i)

    db.session.commit()   
    return redirect(url_for("main.index"))

# 데이터 원상복구
@bp.route("/refresh",methods=['GET'])
def refresh() :
    if request.method=='GET' :
        delete_titanic = db.session.query(Titanic).all()
        for i in delete_titanic :
            db.session.delete(i)
        db.session.commit()


        # 이것은 로컬일 때만 사용 가능
        # df = pd.read_csv(r'C:\Users\lge\Desktop\assignment\titanic_flask\train.csv')

        # heroku 에서는 깃헙에 업로드 한 것을 사용해야 함
        url = 'https://raw.githubusercontent.com/taeyoonnoh/Titanic_with_Visualization/master/train.csv'
        df = pd.read_csv(url,sep=",")
        df = df.dropna(subset=['Age'])
        df = df.reset_index(drop=True)

        for i in range(len(df)) :
            name = df['Name'][i]
            gender = df['Sex'][i]
            age = df['Age'][i]
            fare = df['Fare'][i]
            embarked = df['Embarked'][i]
            pclass = str(df['Pclass'][i])
            survived = str(df['Survived'][i])
            titanic = Titanic(name,gender,age,fare,embarked,pclass,survived)
            db.session.add(titanic)
        db.session.commit()
    
    return redirect(url_for("main.index"))

# `Edit_Titanic` 모델에 있는 데이터를 `Titanic` 모델에 추가하기
@bp.route("/add",methods=['GET'])
def add_passengers() :
    if request.method=='GET' :
        add_passengers = db.session.query(Edit_Titanic).all()
        for i in add_passengers :
            name = i.name
            gender = i.gender
            age = i.age
            fare = i.fare
            embarked = i.embarked
            pclass = i.pclass
            survived = i.survived
            add_to_db = Titanic(
                name = name,
                gender = gender,
                age = age,
                fare = fare,
                embarked = embarked,
                pclass = pclass,
                survived = survived
            )
            db.session.add(add_to_db)
            db.session.commit()
    
    return redirect(url_for("main.index"))
