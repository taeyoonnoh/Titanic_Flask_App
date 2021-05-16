from flask import Blueprint, render_template, request,redirect,url_for
from titanic_app.models.titanic_passesngers import Titanic
from titanic_app.models.edit_passengers import Edit_Titanic
from titanic_app import db
import pandas as pd

bp = Blueprint('edit', __name__)

@bp.route("/",methods=['GET','POST'])
def edit_index() :
    
    if request.method=="POST" :
        try :
            # 데이터 추가
            name = request.form['name']
            age = request.form['age']
            gender = request.form['gender']
            fare = request.form['fare']
            embarked = request.form['embarked']
            pclass = request.form['pclass']
            survived = request.form['survived']
            edit_titanic = Edit_Titanic(name, gender, age, fare, embarked, pclass, survived)
            db.session.add(edit_titanic)
            db.session.commit()
        
        except :
            try :
                # 데이터 삭제
                passenger_id_name = request.form['passengerid_name'].split(" ")
                passenger_id = passenger_id_name[0]
                name = passenger_id_name[1]
                return redirect(url_for("edit.delete",passenger_id=passenger_id,name=name))
            except :
                try :
                    # 데이터 수정
                    passenger_id = request.form['passengerid']
                    return redirect(url_for("edit.check",passenger_id=passenger_id))
                except :
                    # 그 외에는 그냥 refresh
                    return redirect(url_for("edit.edit_index"))

    edit_titanic = db.session.query(Edit_Titanic).all()

    return render_template("second.html",info=edit_titanic)

# 데이터 수정
@bp.route("/<passenger_id>",methods=['GET','POST'])
def check(passenger_id) :
    check_titanic = db.session.query(Edit_Titanic).filter(Edit_Titanic.passenger_id==passenger_id).one()

    if request.method=="POST" :
        check_titanic.name = request.form['name']
        check_titanic.gender = request.form['gender']
        check_titanic.age = request.form['age']
        check_titanic.fare = request.form['fare']
        check_titanic.embarked = request.form['embarked']
        check_titanic.pclass = request.form['pclass']
        check_titanic.survived = request.form['survived']
        db.session.commit()

    # gender info
    gender_info = {'male','female'}
    diff_gender = gender_info.difference({check_titanic.gender})

    # embarked info
    embarked_info = {'S','Q','C'}
    diff_embarked = embarked_info.difference({check_titanic.embarked})

    # class info
    class_info = {'1','2','3'}
    diff_class = class_info.difference({check_titanic.pclass})

    # survived info
    survived_info = {'0','1'}
    diff_survived = survived_info.difference({check_titanic.survived})

    return render_template("check.html",
        check_titanic=check_titanic,
        diff_gender=list(diff_gender),
        diff_embarked=list(diff_embarked),
        diff_class = list(diff_class),
        diff_survived = list(diff_survived)
    )

# 데이터 삭제
@bp.route("/<passenger_id>/<name>")
def delete(passenger_id,name) :
    delete_passenger = db.session.query(Edit_Titanic).filter(Edit_Titanic.passenger_id==passenger_id).one()
    db.session.delete(delete_passenger)
    db.session.commit()
    return redirect(url_for("edit.edit_index"))