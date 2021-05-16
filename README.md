# Titanic_Flask_App

## Project Information
* Titanic 데이터를 가지고 CRUD 및 데이터 시각화 기능이 담긴 웹 어플리케이션을 구현했습니다.
* Flask 로 기능 구현을 했고 Heroku를 통해 배포를 했습니다.

<br/>

## 주요 기능
* **CRUD**
  * Create Passengers
  * Add Passengers
  * Edit Passengers
  * Delete Passengers


* **Data Visualization**

<br/>

## Setups
* Python Version : 3.7.10
* `pip install -r requirements.txt`

<br/>

**Development Mode (로컬에서 구동할 때 아래와 같이 입력)**
* `export FLASK_APP=titanic_flask`
* `export FLASK_ENV=development`
* `flask run`

<br/>

**Production Mode (웹에서 구동할 때 아래와 같이 입력)**
* `export FLASK_APP=titanic_flask`
* `export FLASK_ENV=production`
* `git add .`
* `git commit -m "{commit message}"`
* `git push heroku main`

<br/>

## Folder Layout
```
Titanic_Flask_App
├── migrations
├── train.csv
├── Procfile
├── config.py
├── requirements.txt
│ └── models
│        └── titanic_passengers.py
│        └── edit_passengers.py
│ └── routes
│        └── main_route.py
│        └── edit_route.py
│        └── visualization_route.py
│ └── templates
│        └── titanic.html
│        └── first.html
│        └── second.html
│        └── check.html
│        └── visualization.html
│ └── static
│        └── css
│             └── styles.css
│ └── init.py
│ └── titanic.sqlite3
```

<br/>

## Demonstration Video

https://user-images.githubusercontent.com/74780115/118387614-4b34de80-b65a-11eb-9959-f2e443e203c3.mp4


