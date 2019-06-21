from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

base_url = "https://ngojobsinafrica.com/?post_type=noo_job&s=&location%5B%5D=zimbabwe&category%5B%5D=information-technology"
source = requests.get(base_url).text
soup = BeautifulSoup(source, 'lxml')

all_information_technology_jobs = soup.find_all('div', class_="loop-item-wrap")


for item in all_information_technology_jobs:
    jobs = item.find('div', class_='item-featured')
    job_name = (jobs.a)["title"]
    print(job_name)

    companies = item.find('span', class_='job-company')
    company = (companies.a.text)
    print(company)

    job_types = item.find('span', class_='job-type')
    job_type=job_types.a.text
    print(job_type)

    job_locations = item.find('span', class_='job-location')
    job_location = job_locations.a.text
    print(job_location)

    job_dates = item.find('time', class_='entry-date')
    job_date = job_dates.find_all('span')[1].text
    print(job_date[3:])

    job_links = item.find('div', class_='item-featured')
    job_link = (job_links.a)["href"]
    print(job_link)




