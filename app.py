from flask_blog import init_app, db

app = init_app()
db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
