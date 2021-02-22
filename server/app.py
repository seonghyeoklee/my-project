from flask import Flask, current_app, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from conf import DB_CONNECT

app = Flask(__name__)
CORS(app)


app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{DB_CONNECT['username']}:{DB_CONNECT['password']}@{DB_CONNECT['server']}:3306/{DB_CONNECT['dbname']}?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy() 
db.init_app(app)


def init_db():
    db.init_app(current_app)
    db.drop_all()
    db.create_all()

    sample_user = User(
            username="lana", email="lana@lana.com", password=generate_password_hash("lanalana", method="sha256")
    )
    db.session.add(sample_user)
    db.session.commit()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80))


@app.route('/login')
def login():
    result = []
    users = User.query.all()

    for user in users:
        print('========================')
        print('id : ',user.id)
        print('username: ',user.username)
        print('email : ',user.email)
        print('========================')
        result.append(
                {
                    'id':user.id,
                    'username':user.username,
                    'email':user.email
                }
            )

    return jsonify(status = 'success', result=result)
