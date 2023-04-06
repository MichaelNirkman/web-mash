import requests
import xml.etree.ElementTree as ET

positive_responses = ["y", "Y", "yes", "Yes"]
negative_responses = ["n", "N", "no", "No"]

def gather_links_from_url(url, interactive=True, has_sitemap=True):

    links = []

    if interactive:
        has_sitemap = boolean_prompt("Is there a sitemap.xml available for this site?")
    
    if has_sitemap:
        sitemap_url = f"{url}/sitemap.xml"
        print(f"Attempting to fetch sitemap from {sitemap_url}")

        response = requests.get(sitemap_url)

        if response.status_code != 200:
            print(f"Could not fetch a sitemap, HTTP error code {response.status_code}")
            exit()
        
        links = parse_sitemap(response.content)

    else:
        print("Well, I haven't implemented another way to get links yet so...")

    return links


        

def parse_sitemap(sitemap):
    sitemap_root = ET.fromstring(sitemap)

    urls = []

    for item in sitemap_root:
        urls.append(item[0].text)

    return urls

def boolean_prompt(query):
    try:
        while True:
            response = input(f"{query} (y/n): ")
            if response == "" or response in positive_responses:
                return True
            elif response in negative_responses:
                return False
            else:
                print("Did not recognize the answer, please supply another one")
    except KeyboardInterrupt:
        print("\n\nBye! \n")