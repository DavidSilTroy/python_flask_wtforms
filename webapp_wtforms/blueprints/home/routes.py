from flask import render_template
from webapp_wtforms.blueprints.home import home_views  

 

@home_views.route('')
@home_views.route('/')
@home_views.route('/index')
@home_views.route('/home') 
def home():  
    return render_template("pages/home/index.html",name = 'David Silva Troya')  