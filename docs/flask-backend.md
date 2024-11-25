## virtial environment set-up
```
python -m venv backend-env
```
## env installation
```
pip install python-dotenv
```
## 1st-phase-requirements
```
pip install flask flask_cors flask_jwt_extended flask_sqlalchemy flask_migrate
```
## 2nd-phase-requirements
```
pip install gunicorn psycopg2 psycopg2-binary
```
## install flask-bcrypt
```
pip install flask-bcrypt
```


## create api setp-by-set
1) create service
2) blue print on route
3) regiseter blue-print on main server

## sql-archemy database initialize
1) flask db init
2) flask db migrate
3) flask db upgrade

## deploy
1) pip install -r requirements.txt
2) gunicorn --bind 0.0.0.0:5000 wsgi:app
