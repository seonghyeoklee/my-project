# my-project (portfolio)

>## Flask 
* ### 플라스크 프로젝트 구조
    + #### 플라스크는 ‘프로젝트의 구조를 어떻게 하라’와 같은 규칙이 없다. 우리 프로젝트에서 사용 할 프로젝트의 구조는 다음과 같다.

```
server
   ├─ app.py
   ├─ models.py
   ├─ config.py
   ├─ views/
   │   └─ main_views.py
   ├─ static/
   │   └─ style.css
   └─ templates/
        └─ index.html
```

+ ### `models.py` : 데이터베이스를 처리하는 파일
    + #### 프로젝트는 ORM(object relational mapping)을 지원하는 파이썬 데이터베이스 도구인 SQLAlchemy를 사용한다. SQLAlchemy는 모델 기반으로 데이터베이스를 처리한다.

+ ### `config.py` : 파이보 프로젝트를 설정하는 파일
    + #### `config.py` 파일은 프로젝트를 설정한다. 프로젝트의 환경변수, 데이터베이스 등의 설정을 이 파일에 저장한다.

+ ### `views` : 화면을 구성하는 디렉터리
    + #### views 디렉터리에는 함수들로 구성된 뷰 파일들을 저장한다. 프로젝트에는 기능에 따라 여러 가지 뷰 파일을 만든다.
    
+ ### `static` : CSS, 자바스크립트, 이미지 파일을 저장하는 디렉터리
    + #### static 디렉터리는 파이보 프로젝트의 스타일시트(.css), 자바스크립트(.js) 그리고 이미지 파일(.jpg, .png) 등을 저장한다.

