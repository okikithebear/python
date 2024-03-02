import requests
from bs4 import BeautifulSoup

def scan_web_app(url):
    
    response = requests.get(url)

  
    if response.status_code == 200:
        print(f"Target {url} is accessible.")

      
        analyze_html(response.text)
    else:
        print(f"Failed to access the target {url}. Status Code: {response.status_code}")

def analyze_html(html_content):
   
    soup = BeautifulSoup(html_content, 'html.parser')

 
    forms = soup.find_all('form')
    if forms:
        print(f"Forms found on the page:")
        for form in forms:
            print(form)

   


target_url = "https://woodpentry.org/"
scan_web_app(target_url)
