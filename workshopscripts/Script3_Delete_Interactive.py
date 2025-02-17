import requests
import json

# Default configuration values (modify these as needed)
DEFAULT_INDEX_API_TOKEN = "<INDEX_API_TOKEN>"
DEFAULT_DELETION_API_URL = "https://support-lab-be.glean.com/api/index/v1/deletedocument"
DEFAULT_DOCUMENT_ID = "GleanPartnerWorkshop_Example_Document"
DEFAULT_DATASOURCE = "gleanpartnerworkshop"

def get_input(prompt, default=""):
    user_input = input(f"{prompt} [{default}]: ").strip()
    return user_input if user_input else default

def delete_document(api_url, token, doc_id, datasource):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "datasource": datasource,
        "id": doc_id
    }
    
    response = requests.post(api_url, headers=headers, json=payload)
    
    print("Status Code:", response.status_code)
    if response.text.strip():
        try:
            parsed = response.json()
            print("Response JSON:")
            print(json.dumps(parsed, indent=2))
        except json.decoder.JSONDecodeError:
            print("Response is not valid JSON:")
            print(response.text)
    else:
        print("No response body returned.")

def main():
    print("Delete a document via the Glean API")
    token = get_input("Enter API Token", DEFAULT_INDEX_API_TOKEN)
    api_url = get_input("Enter deletion API URL", DEFAULT_DELETION_API_URL)
    doc_id = get_input("Enter Document ID to delete", DEFAULT_DOCUMENT_ID)
    datasource = get_input("Enter Datasource name", DEFAULT_DATASOURCE)
    
    print(f"\nDeleting document with ID '{doc_id}' from datasource '{datasource}'...")
    delete_document(api_url, token, doc_id, datasource)

if __name__ == "__main__":
    main()
