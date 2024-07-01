import os 
import pandas as pd 
from urllib.parse import urlparse


# Variables
result_path = './results'

# ------------------------------------------------


print('[+] Checking the directory: ')
if os.path.isdir(result_path):
    print("   [+] Directory '/results' is already exists.")
else:    
    os.mkdir(result_path)
    print('   [+] Directory is created.')


with open('urls.csv', 'r') as file:
    urls = file.readlines()


data = []
for url in urls:
    parsed_url = urlparse(url)
    
    username = parsed_url.username
    password = parsed_url.password
    domain = parsed_url.hostname.split('.')[0]

    credential = {"username": username, "password": password, "domain_name": domain}
    data.append(credential)

df = pd.DataFrame(data)
distinct_domains = {entry['domain_name'] for entry in data}
distinct_domains_list = list(distinct_domains)

for domain in distinct_domains_list:
    df_new = df[df['domain_name'] == domain][['username', 'password']]

    file_path = f'./results/{domain}.json'


    if os.path.exists(file_path):
        df_existing = pd.read_json(file_path, orient='records')
        df_concatenated = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_concatenated = df_new
    df_concatenated.to_json(file_path, orient='records', indent=4)

    print(f"[+] Data successfully appended to {file_path}.")

    
    






