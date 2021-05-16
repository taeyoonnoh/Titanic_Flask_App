from flask import Blueprint, render_template, request,redirect,url_for,send_file
from titanic_app.models.titanic_passesngers import Titanic
from titanic_app.models.edit_passengers import Edit_Titanic
from titanic_app import db
import sqlite3 as sq
import pandas as pd
from io import BytesIO
import base64
import seaborn as sns
import matplotlib.pyplot as plt
import psycopg2 as pg2

bp = Blueprint('visualization', __name__)

@bp.route("/",methods=['GET','POST'])
def visualization() :
    # Local에선 이렇게 할 것
    # conn = sq.connect("C:\\Users\\lge\\Desktop\\assignment\\titanic_flask\\titanic_app\\titanic.sqlite3")

    # heroku 에 적용할 땐 아래 코드 사용할 것
    conn = pg2.connect(database="d758eese0nfeeu",user="issrrbbbwqlmbl",password="9198288aea2523075436169ea74e9914b81697891fb3075ce1915a7e7d405013",host="ec2-35-174-118-71.compute-1.amazonaws.com",port="5432")

    cur = conn.cursor()
    df = pd.read_sql_query("select * from titanic", conn)
    df['survived'] = pd.to_numeric(df['survived'])
    df['pclass'] = pd.to_numeric(df['pclass'])

    # df 저장하려면 아래 주석을 푸시오
    # df.to_csv("C:\\Users\\lge\\Desktop\\assignment\\titanic_flask\\check.csv")

    img = BytesIO()
    sns.set_style("dark")

    fig,axes = plt.subplots(2,3, figsize=(15,11))
    # fig.tight_layout()
    
    fig.suptitle("Titanic Info Visualization",weight='bold',fontsize="30")
    
    sns.countplot(x=df['survived'],ax=axes[0][0]).set_title("Survived Frequency",weight='bold',fontsize='20')
    axes[0][0].set_xlabel("Survived",fontsize="15")
    axes[0][0].set_ylabel("Counts",fontsize="15")

    sns.countplot(x=df['gender'],hue=df['survived'],ax=axes[0][1]).set_title("Gender vs Survived",weight='bold',fontsize='20')
    axes[0][1].set_xlabel("Gender",fontsize="15")
    axes[0][1].set_ylabel("Counts",fontsize="15")    

    sns.countplot(x=df['pclass'],hue=df['survived'],ax=axes[0][2]).set_title("Pclass vs Survived",weight='bold',fontsize='20')
    axes[0][2].set_xlabel("Pclass",fontsize="15")
    axes[0][2].set_ylabel("Counts",fontsize="15")  

    sns.histplot(x=df['age'],hue=df['survived'],element='poly',ax=axes[1][0]).set_title("Age vs Survived",weight='bold',fontsize='20')
    axes[1][0].set_xlabel("Age",fontsize="15")
    axes[1][0].set_ylabel("Counts",fontsize="15") 

    sns.histplot(x=df['fare'],hue=df['survived'],element='poly',ax=axes[1][1]).set_title("Fare vs Survived",weight='bold',fontsize='20')
    axes[1][1].set_xlabel("Fare",fontsize="15")
    axes[1][1].set_ylabel("Counts",fontsize="15") 

    sns.countplot(x=df['embarked'],hue=df['survived'],ax=axes[1][2]).set_title("Embarked vs Survived",weight='bold',fontsize='20')
    axes[1][2].set_xlabel("Embarked",fontsize="15")
    axes[1][2].set_ylabel("Counts",fontsize="15")     

    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    return render_template("visualization.html",plot_url=plot_url)