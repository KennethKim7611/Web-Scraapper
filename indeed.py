import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = "https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')

    pages = []

    for link in links[0:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page

def extract_indeed_jobs(last_page):
    jobs = []
    titles = []
    companyNames = []
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("a", {"class": "fs-unmask"})
        for result in results:
            jobTitle = result.find("h2",{"class":"jobTitle"})
            title = jobTitle.find("span").text
            if title == "new":
                title = jobTitle.find_all("span")[1].string
            titles.append(title)
            company = result.find("span", {"class": "companyName"})
            if company is not None:
                company = company.text
            else:
                company = None
            location = result.select_one("pre > div").text
            jobs.append([title, company, location])
        
    return jobs
    