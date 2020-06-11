import flask
import datetime
from flask import Flask


from utils.db import mysql


from blueprints.korisnik import korisnik_blueprint


app = Flask(__name__, static_url_path="")


app.config["MYSQL_DATABASE_USER"] = "root" 
app.config["MYSQL_DATABASE_PASSWORD"] = "rootroot" 
app.config["MYSQL_DATABASE_DB"] = "bioskop" 

mysql.init_app(app) 


app.register_blueprint(korisnik_blueprint, url_prefix="/api")


@app.route("/")
@app.route("/index")
def index_page():
    
    return app.send_static_file("index.html")

if __name__ == "__main__":

    app.run("0.0.0.0", 5000, threaded=True)
