from flask import Flask, request, render_template, url_for

app = Flask(__name__)

from app import views, config, forms, models
from app.scrape_sites import ScrapeSites