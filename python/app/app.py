from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    inspect,
)

import uuid

import os

from sqlalchemy.exc import IntegrityError
from utils import get_engine, run_query, create_table
from flask import Flask, request, render_template

from home import home_bp

from flask_cors import CORS

def create_app():
    app = Flask(__name__,template_folder='./templates',static_folder='./static')

    CORS(app)

    blueprints = [home_bp]

    engine = get_engine()

    create_table(engine)

    for bp in blueprints:
        app.register_blueprint(bp)

    @app.route('/home')
    def home():
        return render_template('home.html', active_route="route-home")
    
    @app.route('/schedule')
    def schedule():
        return render_template('schedule.html', active_route="route-schedule")
    
    @app.route('/profile')
    def profile():
        return render_template('profile.html', active_route="route-profile")

    return app


app = create_app()
app.run()
