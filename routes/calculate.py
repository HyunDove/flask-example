from flask import Blueprint, render_template, request
from services.bmi_calculator_service import BMICalculator
from models.client import Database

calculate_route = Blueprint('calculate', __name__)
db = Database()

@calculate_route.route('/calculate', methods=['POST'])
def calculate():
    try:
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        
        # 입력값 유효성 검사
        if weight <= 0 or height <= 0:
            return render_template('index.html', error="체중과 신장은 양수여야 합니다.")
        
        # BMI 계산
        calculator = BMICalculator(weight, height)
        result = calculator.get_result()
        
        # 데이터베이스에 저장
        db.save_bmi_record(weight, height, result["bmi"], result["category"])
        
        return render_template('result.html', 
                              bmi=result["bmi"], 
                              category=result["category"],
                              weight=weight,
                              height=height)
    except ValueError:
        return render_template('index.html', error="유효한 숫자를 입력해주세요.")