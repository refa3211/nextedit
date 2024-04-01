import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os

user = os.getenv('USER')
password = os.getenv('PASS')

def fetch_hosts_from_github(repo_url):
    response = requests.get(repo_url)
    if response.status_code == 200:
        return response.text.split('\n')
    else:
        print(f"Failed to fetch hosts list from {repo_url}")
        return []

def input_hostname_to_nextdns(hostnames):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://my.nextdns.io/login")
    time.sleep(1)  # Add a short wait for page load
    
    email_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/form/div[1]/input")
    email_input.send_keys(user)

    password_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/form/div[2]/input")
    password_input.send_keys(password)
    
    password_input.send_keys(Keys.RETURN)
    time.sleep(1)  # Wait for login
    
    denylist_url = "https://my.nextdns.io/159376/denylist"
    driver.get(denylist_url)
    for hostname in hostnames:
        hostname = hostname.strip()
        if hostname:
            time.sleep(0.5) 
            add_domain_input = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div/input")
            add_domain_input.send_keys(hostname)
            add_domain_input.send_keys(Keys.RETURN)
            time.sleep(0.5)  # Wait briefly for domain to be added
    
    driver.quit()

if __name__ == "__main__":
    github_repo_url = "https://raw.githubusercontent.com/refa3211/nextedit/main/host"
    hosts = fetch_hosts_from_github(github_repo_url)
    input_hostname_to_nextdns(hosts)
