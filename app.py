from flask_blog import init_app, db
import os

app = init_app()
file_path = os.path.abspath(os.getcwd()) + "/flask_blog/site.db"
SQLALCHEMY_DATABASE_URI = "sqlite:///" + file_path
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
