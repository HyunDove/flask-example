# 사전 설치 : pip install flask pymysql requests
from flask import Flask, render_template, request, redirect, url_for
from models.client import Database
from routes.main_route import main_route, init_db
import atexit   # 애플리케이션 종료시 실행을 요청 (ex. DB연결 종료)

app = Flask(__name__)   # Flask 앱 초기화
db = Database()   # DB 초기화

# 애플리케이션 종료 시 DB 연결 종료
atexit.register(db.close)

# 라우트 등록
app.register_blueprint(main_route)

# DB 인스턴스를 라우트에 주입
init_db(db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)