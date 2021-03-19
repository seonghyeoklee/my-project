# my-project (portfolio)

* ### 개발환경
```
back-end : Flask
front-end : React
database : mySql
```


>## Flask 
* ### 플라스크 프로젝트 구조
    + #### 플라스크는 ‘프로젝트의 구조를 어떻게 하라’와 같은 규칙이 없다. 우리 프로젝트에서 사용 할 프로젝트의 구조는 다음과 같다.

```
server
   ├─ app.py
   ├─ auth.py
   ├─ awards.py
   ├─ config.py (.gitignore)
   ├─ db.py
   ├─ edu.py
   ├─ license.py
   ├─ network.py
   ├─ profile.py
   └─ project.py

```

#### `app.py` : application 실행 및 관리하는 파일
+ ##### 애플리케이션 팩토리를 사용하여 app 객체를 전역으로 사용할 때 발생하는 문제를 예방하고 jwt token, db Connection을 설정한다.

#### `db.py` : 데이터베이스를 처리하는 파일
+ ##### 프로젝트는 ORM(object relational mapping)을 지원하는 파이썬 데이터베이스 도구인 SQLAlchemy를 사용한다. SQLAlchemy는 모델 기반으로 데이터베이스를 처리한다.

#### `config.py` : 설정하는 파일
+ ##### `config.py` 파일은 프로젝트를 설정한다. 프로젝트의 환경변수, 데이터베이스 등의 설정을 이 파일에 저장한다.
```
DB_CONNECT = {
    'username' : 'sample',
    'password' : 'sample',
    'server' : '127.0.0.1',
    'dbname' : 'sample',
}

SECRET_KEY = 'sample'
```


>### Flask 실행

```
cd server

pip3 install -r requirements.txt

export FLASK_APP=app
export FLASK_ENV=development

flask run
```

>### React 실행

```
cd web

npm install

npm run start
```


Open [http://localhost:3000](http://localhost:3000) to view it in the browser.


