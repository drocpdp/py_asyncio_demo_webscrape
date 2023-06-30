from app import app
from flask import render_template
from app.scrape_sites import ScrapeSites


@app.route("/")
def landing_page():
    return render_template('base.html')


@app.route('/scrape', methods=['POST'])
def scrape():
    print('ok')
    ScrapeSites().main()
    return 'ok'