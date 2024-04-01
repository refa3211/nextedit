import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
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
    time.sleep(1)

    email_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/form/div[1]/input")
    email_input.send_keys("refa3211@telegmail.com")

    password_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/form/div[2]/input")
    password_input.send_keys("R3fa3@#ldns")

    password_input.send_keys(Keys.RETURN)

    time.sleep(1)  # Wait for login

    for hostname in hostnames:
        if hostname.strip():
            driver.get("https://my.nextdns.io/159376/denylist")
            time.sleep(0.5)  # Wait for page to load
            add_domain_input = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div/input")
            add_domain_input.send_keys(hostname)
            print(hostname)
            add_domain_input.send_keys(Keys.RETURN)
            time.sleep(1)  # Wait for domain to be added

    driver.quit()


if __name__ == "__main__":
    # Replace 'GITHUB_REPO_URL' with the URL of your GitHub repository containing the hosts list
    github_repo_url = "https://raw.githubusercontent.com/refa3211/nextedit/main/host"
    hosts = fetch_hosts_from_github(github_repo_url)
    input_hostname_to_nextdns(hosts)
