import sys
import functions.link_handler as lh

def main():
    if not sys.argv[1]:
        print("Did not get an URL, please give one")
        exit
    
    url = sys.argv[1]
    
    print(f"Starting to gather URLS from {url}")

    links = lh.gather_links_from_url(url)

if __name__ == "__main__":
    main()