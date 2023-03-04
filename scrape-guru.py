from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.guru.com/d/freelancers/skill/web-scraping/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")

# Name of web-site to be scraped
website = soup.title.text.strip()

#Open csv file to save data to
csv_file = open(website+'.csv', 'w', newline='', encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['owner','city','state','country','earnings amount','service name','service description'])

# Freelancer details
# Take top 20 freelancers
count = 1; 
for freelancer in soup.findAll('div', class_='record__details'):
    if(count > 20):
        break

    try:
        #1. HEADER
        header = freelancer.find('div', class_='record__header')

        #1.1 name
        name = header.h3.a.text.strip()
        
        #1.2 location
        location = header.find('span', class_='freelancerAvatar__location')
        city = location.find('span', class_='freelancerAvatar__location--city').text.strip().replace(',','')
        state = location.find('span', class_='freelancerAvatar__location--state').text.strip().replace(',','')
        country = location.find('span', class_='freelancerAvatar__location--country').text.strip().replace(',','')
        
        #1.3 earnings
        earnings = header.find('span', class_='earnings')
        earningsamount = earnings.find('span', class_='earnings__amount').text.strip()

        #2. Content
        header = freelancer.find('div', class_='record__content')

        #2.1 serviceListing
        servicename = header.h2.a.text.strip()
        servicedescription = header.find('p', class_='serviceListing__desc').text
    except:
        pass

    #Save data to file
    csv_writer.writerow([name,city,state,country,earningsamount,servicename,servicedescription])

    count += 1

csv_file.close()