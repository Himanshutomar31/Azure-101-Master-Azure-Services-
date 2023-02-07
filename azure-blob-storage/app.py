"""
Module for Azure Blob Storage CRUD
"""

import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


def create_container(blob_service_client):
    try:
        container_name = "az_204_blob_storage"
        container_client = blob_service_client.create_container()
    except Exception as exp:
        raise exp



try:
    account_url = "https://blobaz204.blob.core.windows.net"
    default_credential = DefaultAzureCredential()

    blob_service_client = BlobServiceClient(account_url, credential=default_credential)

    create_container(blob_service_client)
except Exception as exp:
    print(exp)
    