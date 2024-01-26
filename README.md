# 장고 기본 명령어
## 서버 시작하기
`python3 manage.py runserver 8080` : runserver 뒤에있는 포트로 서버를 실행시키겠다는 의미다.
`python3 manage.py runserver 0.0.0.0:8000` : ip를 직접 지정, 같은 네트워크 망안에서 접속이 가능하도록할때 적어준다.
`python3 manage.py runserver 0:8000` : 0 = 0.0.0.0 의 약어. 해당 형태로 동작을 시킬때는 settings.py 에 있는 ALLOWED_HOSTS를 설정해줘야함
## 기본 명령어
`django-admin startproject [project_name]` : 장고 프로젝트를 만드는 명령어. 뒤에 . 를 붙여주면 새로운 파일에서 프로젝트가 생성되는 것이 아니라 현재 파일에서 프로젝트가 생성됨.<br/>
`python3 manage.py startapp [app_name]` : 프로젝트의 기능 단위인 앱을 새로 만들 떄 사용됨.<br/>
`python3 manage.py makemigrations` : 어플리케이션의 변경 사항을 db 에 적용 -> 내용 정리.<br/>
`python3 manage.py migrate` : 실제 변경사항을 db 에 반영<br/>
`python3 mange.py showmigrations` : db 변경사항 목록과 상태를 출력<br/>
`python3 manage.py createsuperuser` : 관리자 계정을 생성<br/>
`python3 manage.py chagepassword` : 게정의 비밀번호 변경 가능<br/>
`python3 manage.py sqlmigrate` : 실행할 sql 명령문을 출력, 어떤 명령문을 실행할지 확인할 때 사용, 튜닝이 안된 쿼리나 슬로우 쿼리 여부를 확인 가능.<br/>
`python3 manage.py dumpdata` : 현재 db의 내용을 백업할 때 사용<br/>
`python3 manage.py loaddata` : 백업 파일에서 db로 내용을 복구할 때 사용<br/>
`python3 manage.py flush` : db 테이블은 그대로 두고 테이블의 내용만 전부 삭제<br/>
`python3 manage.py shell` : shell을 실행. 작성한 모델 등을 불러와 실제로 테스트 해볼 수 있음.<br/>
`python3 manage.py dbshell` : db 에 직접 접근할 수 있는 shell 을 실행.<br/>