import requests
from datetime import datetime

# Default values that can be modified directly in the script.
DEFAULT_DOMAIN = "support-lab-be.glean.com"
DEFAULT_SEARCH_API_TOKEN = "Enter Search API Token" # Replace with your Glean Search API token
DEFAULT_QUERY = "Glean Partner Workshop Example Document"
DEFAULT_NUM_RESULTS = 2

def get_input(prompt, default):
    user_input = input(f"{prompt} [{default}]: ").strip()
    return user_input if user_input else default

def get_number_of_results():
    while True:
        num = input(f"Enter number of results to print (1-50) [{DEFAULT_NUM_RESULTS}]: ").strip()
        if not num:
            return DEFAULT_NUM_RESULTS
        try:
            num_int = int(num)
            if 1 <= num_int <= 50:
                return num_int
            else:
                print("Please enter a number between 1 and 50.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 50.")

def search_documents(api_url, token, query, page_size):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "query": query,
        "pageSize": page_size,
        "includeFields": ["datasource", "metadata", "title", "url", "document"],
        "requestOptions": {}
    }
    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        print(response.text)
        return None
    data = response.json()
    # Detailed document results are expected to be in the "results" key.
    return data.get("results", [])

def print_results(results):
    if not results:
        print("No results found.")
        return
    print("\nSearch Results:")
    for idx, result in enumerate(results):
        # Some responses wrap the document in a "document" key.
        doc = result.get("document", result)
        doc_id = doc.get("id", "N/A")
        title = doc.get("title", "N/A")
        url = doc.get("url") or doc.get("viewURL", "N/A")
        ds = doc.get("datasource", "N/A")
        metadata = doc.get("metadata", {})
        create_time = metadata.get("createTime", "N/A")
        update_time = metadata.get("updateTime", "N/A")
        try:
            if create_time != "N/A":
                create_time = datetime.fromisoformat(create_time).strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            pass
        try:
            if update_time != "N/A":
                update_time = datetime.fromisoformat(update_time).strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            pass
        
        print("-" * 40)
        print(f"Result #{idx+1}")
        print(f"Document ID: {doc_id}")
        print(f"Title      : {title}")
        print(f"URL        : {url}")
        print(f"Datasource : {ds}")
        if create_time != "N/A":
            print(f"Created    : {create_time}")
        if update_time != "N/A":
            print(f"Updated    : {update_time}")

def main():
    print("Enter the Search API details. For the URL, just enter the domain (without 'https://').")
    domain = get_input("Search API domain", DEFAULT_DOMAIN)
    # Construct the full URL.
    api_url = f"https://{domain}/rest/api/v1/search"
    
    token = get_input("Search API Token", DEFAULT_SEARCH_API_TOKEN)
    query = get_input("Search term", DEFAULT_QUERY)
    num_results = get_number_of_results()
    
    print("\nSearching for documents...")
    results = search_documents(api_url, token, query, num_results)
    print_results(results)

if __name__ == "__main__":
    main()
