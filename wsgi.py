from webapp_wtforms import create_app as application


app = application()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

# run this app with:
#flask --app webapp_wtforms run --debug