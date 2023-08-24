import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    '''
    Later can be set in the server like:
    setx SECRET_KEY "super secret"    

    '''
    
    ''' This values should be set in the enviorament to can get them and not have them in the code'''
    SECRET_KEY = os.environ.get('SECRET_KEY') 
    
    ''' For now we set this in the code, when the web-app is deploy this should be delete and use the previous code instead'''
    SECRET_KEY = 'just to show you'  


