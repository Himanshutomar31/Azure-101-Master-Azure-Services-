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



try:
    account_url = "https://blobaz204.blob.core.windows.net"
    default_credential = DefaultAzureCredential()

    blob_service_client = BlobServiceClient(account_url, credential=default_credential)
    container_client = blob_service_client.get_container_client("az-204-blob-storage")
    if container_client.exists():
        print("Container exists")
    else:
        print("Not Found")
        create_container(blob_service_client)
except Exception as exp:
    print(exp)
    