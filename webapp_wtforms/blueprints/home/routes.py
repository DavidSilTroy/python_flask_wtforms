from flask import redirect, render_template, url_for
from webapp_wtforms.blueprints.home import home_views
from webapp_wtforms.models.user_form import UserForm  

 
# Home page. TODO: Add base.html
@home_views.route('')
@home_views.route('/')
@home_views.route('/index')
@home_views.route('/home') 
def home():  
    return render_template("pages/home/index.html",name = 'David Silva Troya')  

# Successfully sent data with the form
@home_views.route('/well_done')
def well_done():
    return 'Great! Well Done! (I have your data now 😈 hahaha, actually not.)' # just kidding!

# User form, first form
@home_views.route('/user_form', methods=['GET', 'POST'])
def user_form(): 
    form = UserForm()
    if form.validate_on_submit():
        # taking the data to be processed
        name = form.name.data
        password = form.password.data
        # Send to another route
        return redirect(url_for('home_views.well_done'))
    return render_template('pages/form/user_form.html', form=form) 