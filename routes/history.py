from flask import Flask, render_template, request, redirect, url_for
from models.client import Database

db = Database()
history_route = Flask("history", __name__)

@history_route.route('/history')
def history():
    # 최근 BMI 기록 10개 가져오기
    records = db.get_bmi_records(10)
    return render_template('history.html', records=records)