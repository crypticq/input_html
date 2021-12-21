#/usr/bin/env/python3

import requests
import warnings

print("#" * 62)
print("Check for potential Attack vector in targetd websites")
print("#" * 62)

print(" Enter File Name.  ")
File=input()

warnings.filterwarnings('ignore', message='Unverified HTTPS request')

def input_html(url):

    r = requests.get(url , verify=False)

    if 'input' in r.text and r.status_code == 200:
        print("Found input")
        print(r.url)
    else:
        pass
# check_domin = ['https://www.w3schools.com/html/html_form_input_types.asp' , 'http://ant.design/components/form/' , 'http://testphp.vulnweb.com/']
with open(File, 'r') as outfile:

    for line in outfile:
        # domain = line.strip()
        input_html(line.strip())
        # for domain_in_file in domain:

        #     input_html(domain)
