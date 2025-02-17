import os
import requests

# Updated API configuration
API_URL = "https://support-lab-be.glean.com/api/index/v1/indexdocument"
INDEX_API_TOKEN = "<INDEX_API_TOKEN>"  # Replace with your Glean Indexing API token

def index_document(file_path):
    """
    Reads the content of the provided file and sends it to the Glean Indexing API.
    
    The payload includes:
      - version: Version number for optimistic concurrency control.
      - document: The document definition containing required fields:
          * id: The unique document identifier.
          * datasource: The datasource name.
          * viewURL: A permalink for viewing the document.
          * title: The document title.
          * filename: The source filename.
          * body: The text content with a specified mimeType.
          * permissions: Document access control details.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return

    # Define the document ID and generate the viewURL dynamically.
    doc_id = "GleanPartnerWorkshop_Example_Document"
    view_url = f"https://docs.google.com/document/d/1GEBM5eM0_Au8PZXZweQEq14K2zVaycYwVVJQjXLb4fc/"

    # Prepare the JSON payload with the required fields.
    payload = {
        "version": 1,
        "document": {
            "id": doc_id,
            "           ": "gleanpartnerworkshop",
            "viewURL": view_url,
            "title": "Glean Partner Workshop Example Document",
            "filename": "GleanPartnerWorkshop_Example_Document",
            "body": {
                "mimeType": "text/markdown",
                "textContent": content
            },
            "permissions": {
                "allowAnonymousAccess": True
            }
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {INDEX_API_TOKEN}"
    }

    # Send the POST request to the Glean Indexing API.
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            print("Document indexed successfully!")
        else:
            print(f"Failed to index document. Status code: {response.status_code}")
            print("Response:", response.text)
    except Exception as e:
        print(f"An error occurred during the API request: {e}")

def main():
    # Path to the document generated in Step 0.
    file_path = os.path.expanduser("./GleanPartnerWorkshop_Example_Document")
    index_document(file_path)

if __name__ == "__main__":
    main()
