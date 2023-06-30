from app import app
from flask import render_template, request
from app.scrape_sites import ScrapeSites


@app.route("/")
def landing_page():
    return render_template('base.html')


@app.route('/scrape', methods=['POST'])
def scrape():
    urls = []
    for _, val in request.form.items():
        urls.append(val)
    scrape = ScrapeSites(urls)
    scrape.main()
    return 'ok'