import subprocess
from bs4 import BeautifulSoup
import csv

tg_links_input = "./tg_links.csv"
tg_links_output = "./tg_links_with_members.csv"

def getMembersCount(url, csv_file_path):
    curl_command = "curl -L {url}".format(url=url)
    output = subprocess.run(curl_command, shell=True, capture_output=True, text=True)
    html_content = output.stdout
    soup = BeautifulSoup(html_content, "html.parser")

    csv_file = open(csv_file_path, 'a', newline='', encoding='utf-8')
    csv_writer = csv.writer(csv_file)

    members_count_element = soup.find('div', class_='tgme_page_extra')
    if members_count_element:
        members_count = members_count_element.text.strip()
        csv_writer.writerow([url, members_count])
        print("Members Count:", members_count)
    else:
        print("Members count not found.")

def process_links_from_csv(csv_file_path):
    with open(csv_file_path, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            link = row[0]
            print(link)
            getMembersCount(link, tg_links_output)


process_links_from_csv(tg_links_input)