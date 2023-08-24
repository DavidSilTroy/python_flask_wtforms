from flask import Blueprint

home_views = Blueprint("home_views", __name__,template_folder='templates') #it will use the main folder for templates