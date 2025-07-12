from fastapi import FastAPI, UploadFile, File
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os
import logging

load_dotenv(override=True)
app = FastAPI()

# Setup logger
logger = logging.getLogger("azure-upload-app")
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Load config
AZURE_CONNECTION_STRING = os.getenv("AZURE_CONNECTION_STRING")
CONTAINER_NAME = os.getenv("CONTAINER_NAME")

print(AZURE_CONNECTION_STRING)
print(CONTAINER_NAME)

# Validate config
if not AZURE_CONNECTION_STRING or not CONTAINER_NAME:
    raise ValueError("Missing Azure connection string or container name in .env")

# Setup Azure clients
blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)
print()
@app.post("/uploads")
async def upload_file(file: UploadFile = File(...)):
    try:
        blob_client = container_client.get_blob_client(file.filename)
        content = await file.read()
        blob_client.upload_blob(content, overwrite=True)
        logger.info(f"File '{file.filename}' uploaded to {blob_client.url}")
        return {"message": "Upload successful", "url": blob_client.url}
    except Exception as e:
        logger.exception("Upload failed")
        return {"error": str(e)}


#  10 sec me aa jata h jitni bhi badi file ho
