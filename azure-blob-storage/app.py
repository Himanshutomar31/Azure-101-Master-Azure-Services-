"""
Module for Azure Blob Storage CRUD
"""

import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


def create_container(blob_service_client):
    try:
        container_name = "az-204-blob-storage"
        container_client = blob_service_client.create_container(container_name)
    except Exception as exp:
        raise exp


def upload_blob(blob_service_client):
    try:
        with open("test.csv","w+") as f1:
            f1.write("a,b,c,d")
        file_path = r"test.csv"
        blob_client = blob_service_client.get_blob_client(container="az-204-blob-storage", blob="test1.csv")
        with open(file=file_path,mode="rb") as data:
            blob_client.upload_blob(data)
    except Exception as exp:
        raise exp

def list_blob(container_client):
    blob_data = container_client.list_blobs()
    for blob in blob_data:
        print("\t"+blob.name)

def download_file_from_storage_account(container_client):
    try:
        with open("temp.csv","wb") as f:
            f.write(container_client.download_blob("test1.csv").readall())
    except Exception as exp:
        raise exp


try:
    account_url = "https://blobaz204.blob.core.windows.net"
    default_credential = DefaultAzureCredential()

    blob_service_client = BlobServiceClient(account_url, credential=default_credential)
    container_client = blob_service_client.get_container_client("az-204-blob-storage")
    if container_client.exists():
        print("Container exists")
        #Logic to upload a blob
        upload_blob(blob_service_client)
        list_blob(container_client)
        download_file_from_storage_account(container_client)
        #lets delete the container
        container_client.delete_container()
    else:
        print("Not Found")
        create_container(blob_service_client)
except Exception as exp:
    print(exp)
    