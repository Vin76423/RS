from app import app
from flask import render_template

# фласк в данном случае выдает значение по ключу, где значение - это наша функц.отображения.
# {'/' : 'view.index'} :
@app.route('page/')
def index():
    return render_template('CSS_1.html')

@app.route('page/')
def index():
    return render_template('CSS_1.html')

@app.route('page/')
def index():
    
@app.route('page/')
def index():
    return render_template('CSS_1.html')