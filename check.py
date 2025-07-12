from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv

load_dotenv(override=True)

AZURE_CONNECTION_STRING = os.getenv("AZURE_CONNECTION_STRING")
CONTAINER_NAME = "csv_files"
def create_container():
    try:
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        container_client = blob_service_client.create_container(CONTAINER_NAME)
        print(f"✅ Container '{CONTAINER_NAME}' created successfully.")
    except Exception as e:
        print(f"❌ Failed to create container: {e}")

def test_blob_connection():
    try:
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        # Try listing containers (or access a specific container if you prefer)
        containers = blob_service_client.list_containers()
        print("✅ Connected successfully. Available containers:")
        for container in containers:
            print(f"- {container['name']}")
    except Exception as e:
        print("❌ Connection failed:", str(e))

if __name__ == "__main__":
    # create_container()
    test_blob_connection()
