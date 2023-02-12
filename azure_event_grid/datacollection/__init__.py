import azure.functions as func
import pandas as pd
import os 
from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential
from azure.eventgrid import EventGridPublisherClient, EventGridEvent
import logging


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        type = req_body["business_type"]
 
        event = EventGridEvent(
            data={"data": "azure-sdk", "type": type},
            subject="B2B data",
            event_type="Azure.Sdk.Demo",
            data_version="2.0"
        )

        credential = AzureKeyCredential("VprOibc1YEGuj5kPrlp6bSWQwLOZYhoB3v/ziriPyRs=")
        endpoint = "https://custom-events.centralindia-1.eventgrid.azure.net/api/events"
        client = EventGridPublisherClient(endpoint, credential)

        client.send(event)
        return func.HttpResponse("executed successfully.")
    except Exception as exp:
        print(exp)
        logging.debug(exp)
        logging.warning(exp)
        return func.HttpResponse("unsuccessfully.")
