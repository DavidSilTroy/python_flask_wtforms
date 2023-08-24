from flask import Flask, redirect, url_for, request
import builtins 
from config import Config  
 
#run the app once the script is run
def create_app(): 
     
    #----> configuring web-app with ist name and folders
    app = Flask(
    "Flask-wtforms" ,
    static_folder='webapp_wtforms/static',
    template_folder='webapp_wtforms/templates'
    ) 

    #----> setting web-app configuration
    app.config.from_object(Config)
    app.jinja_env.globals.update(list=builtins.list)  

    #----> Initialize extensions
    from webapp_wtforms.extensions import qrcode
    qrcode.init_app(app)

    #----> Initialize blueprints
    from .blueprints.home.routes import home_views
    app.register_blueprint(home_views, url_prefix="/") 
    
    return app