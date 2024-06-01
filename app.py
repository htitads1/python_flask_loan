from flask import Flask,jsonify


from app1 import app2
from app2 import app1
from app3 import app3
from loansapp import loansapp;
main_app = Flask(__name__);
main_app.config['Debug']= True
main_app.config['WTF_CSRF_ENABLED'] = False
main_app.register_blueprint(app1);
main_app.register_blueprint(app2);
main_app.register_blueprint(app3);
main_app.register_blueprint(loansapp);



# Here you can globally configure all the ways you want to allow JWTs to
# be sent to your web application. By default, this will be only headers.


@main_app.route("/hello1")
def helloword():
    return "Welcome To Jenkins"

if __name__ == '__main__':
    print('Main')
    main_app.run(debug=True)