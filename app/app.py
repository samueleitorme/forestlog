from flask import Flask, redirect, request, url_for, abort, render_template
import datetime, os, sqlite3

# App
app = Flask(__name__)

# Rutas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/')
def login():
    return render_template('auth/login.html')

@app.route('/register/')
def register():
    return render_template('auth/register.html')



# Eror 404
@app.errorhandler(404)
def not_found(error):
    return render_template('error/404.html')


# Run
if __name__ == '__main__':
  app.run(debug=True)