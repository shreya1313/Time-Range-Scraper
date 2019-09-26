from bs4 import BeautifulSoup
import urllib.request



    jobs_links = list(filter(lambda x: 'jobs' in x, data))
    if jobs_links:
        #indeed
        data = list(filter(lambda x: 'jobs' not in x, data))
        indeed_jobs = list(filter(lambda x: 'indeed' in x, jobs_links))
        for job in indeed_jobs:
            soup = get_html(job)
            links = soup.find_all('a', {'class': 'jobtitle turnstileLink'})
            for link in links:
                data.append('https://www.indeed.co.in' + link.get('href'))

    jd = {START_DATE.strftime("%b"): data}
