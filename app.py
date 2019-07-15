from flask import Flask, render_template, request, url_for, Response
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


# url/jobs is your route to the below method
@app.route('/jobs', methods=['GET', 'POST'])
def jobs():
    if request.method == 'POST':
        mycountry = request.form['country']
        base_url = "https://ngojobsinafrica.com/?post_type=noo_job&s=&location[]=" + mycountry + "&category[]=information-technology"
        source = requests.get(base_url).text
        soup = BeautifulSoup(source, 'lxml')

        all_information_technology_jobs = soup.find_all('div', class_="loop-item-wrap")

        for item in all_information_technology_jobs:
            jobs = item.find('div', class_='item-featured')
            job_name = (jobs.a)["title"]

            job_links = item.find('div', class_='item-featured')
            job_link = (job_links.a)["href"]

            companies = item.find('span', class_='job-company')
            company = (companies.a.text)

            job_types = item.find('span', class_='job-type')
            job_type = job_types.a.text

            job_locations = item.find('span', class_='job-location')
            job_location = job_locations.a.text

            job_dates = item.find('time', class_='entry-date')
            job_date = job_dates.find_all('span')[1].text

            dict = {'JobName': job_name, 'Organisation': company, 'JobType': job_type, 'JobLocation': job_location,
                    'JobExpiry': job_date[3:], 'JobLink': job_link}

            return render_template('index.html', result=dict)


@app.route('/', methods=['GET'])
def dropdown():
    countries = ['Zimbabwe', 'Zambia', 'Tanzania', 'Swaziland', 'Rwanda', 'Namibia', 'Mozambique', 'Malawi', 'Lesotho',
                 'Kenya', 'Ethiopia', 'Botswana', 'Africa', 'Eritrea']
    return render_template('home.html', countries=countries)


if __name__ == '__main__':
    app.run(debug=True)
