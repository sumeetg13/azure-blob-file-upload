# 📁 Azure Blob File Upload API (FastAPI)

A lightweight FastAPI application to upload files (e.g., CSVs) to an Azure Blob Storage container.

---

## 🚀 Features

- Upload files via HTTP POST
- Store uploaded files directly in Azure Blob Storage
- Supports `.env`-based configuration
- Lightweight and fast using FastAPI

---

## 🔧 Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/azure-blob-upload-api.git
cd azure-blob-file-upload
```

### 2. Create and activate virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate
```

## ⚙️ Environment Variables
Create a .env file in the project root with the following:

```
AZURE_STORAGE_CONNECTION_STRING=DefaultEndpointsProtocol=https;AccountName=your_account;AccountKey=your_key;EndpointSuffix=core.windows.net
```

## To upload file

```curl
curl -X POST http://localhost:8000/uploads -F "file=@yourfile.csv"
```

Response:

```
{
    "message": "Upload successful",
    "url": "https://sl2storage.blob.core.windows.net/csv-files/submission_cn.csv"
}
```

## 🧪 Testing Uploads
Check your Azure Portal → Storage Account → Containers → your-container-name to confirm file upload.

## 📦 Tech Stack

- Python

- FastAPI

- Azure Blob Storage SDK

- Uvicorn