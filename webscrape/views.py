from webscrape import app
from flask import render_template, request, Blueprint
from webscrape.scrape_sites import ScrapeSites

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def landing_page():
    return render_template('base.html')

@main_bp.route('/scrape', methods=['POST'])
def scrape():
    urls = []
    for _, val in request.form.items():
        urls.append(val)
    scrape = ScrapeSites(urls)
    scrape.main()
    return 'ok'