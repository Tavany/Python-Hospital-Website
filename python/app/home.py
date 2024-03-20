from sqlalchemy import (
    MetaData,
    Table,
    insert,
)
from sqlalchemy.exc import IntegrityError
from utils import run_query, get_engine
from flask import Blueprint, request, render_template
import uuid
import jwt
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from datetime import date

home_bp = Blueprint("home", __name__, url_prefix="/home")

@home_bp.route("", methods=["GET","POST"])
def get_reservation():

    if request.method == "GET":

        today = date.today()

        specialist = run_query(f"SELECT DISTINCT specialist FROM doctor;")

        price = run_query(f"SELECT specialist,price FROM doctor")
        
        data = {
            'today': today, 
            'specialists': specialist,
            'price' : price
            }

        message = "Get Data Success"

        return render_template(
                'home.html',
                data = data, 
                message = message,
                active_route="route-home",
            )