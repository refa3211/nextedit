import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def fetch_hosts_from_github(repo_url):
    response = requests.get(repo_url)
    if response.status_code == 200:
        return response.text.split('\n')
    else:
        print(f"Failed to fetch hosts list from {repo_url}")
        return []


def input_hostname_to_nextdns(hostnames):
    driver = webdriver.Chrome()  # Assuming you have Chrome WebDriver installed
    driver.get("https://my.nextdns.io/login")

    # Replace 'YOUR_EMAIL' and 'YOUR_PASSWORD' with your NextDNS credentials
    email_input = driver.find_element_by_xpath("//input[@name='email']")
    email_input.send_keys("refa3211@telegmail.com")

    password_input = driver.find_element_by_xpath("//input[@name='password']")
    password_input.send_keys("R3fa3@#ldns")
    password_input.send_keys(Keys.RETURN)

    time.sleep(5)  # Wait for login

    for hostname in hostnames:
        if hostname.strip():
            driver.get("https://https://my.nextdns.io/159376/denylist")
            time.sleep(5)  # Wait for page to load
            add_domain_input = driver.find_element_by_xpath("//input[@name='Add a domain...']")
            add_domain_input.send_keys(hostname)
            add_domain_input.send_keys(Keys.RETURN)
            time.sleep(2)  # Wait for domain to be added

    driver.quit()


if __name__ == "__main__":
    # Replace 'GITHUB_REPO_URL' with the URL of your GitHub repository containing the hosts list
    github_repo_url = "GITHUB_REPO_URL"
    hosts = fetch_hosts_from_github(github_repo_url)
    input_hostname_to_nextdns(hosts)
