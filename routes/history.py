from flask import Blueprint, render_template
from models.client import Database
global db

history_route = Blueprint('history', __name__)

@history_route.route('/history')
def history():
    # 최근 BMI 기록 10개 가져오기
    records = db.get_bmi_records(10)
    return render_template('history.html', records=records)