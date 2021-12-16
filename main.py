import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

from indeed import extract_indeed_pages,extract_indeed_jobs

import csv

last_indeed_pages = extract_indeed_pages()

indeed_jobs = extract_indeed_jobs(last_indeed_pages)

# field names 
fields = ['Job Title', 'Company Name', 'Location'] 
    
# data rows of csv file 
jobs = indeed_jobs
  
with open('GFG', 'w', encoding='UTF8') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(jobs)