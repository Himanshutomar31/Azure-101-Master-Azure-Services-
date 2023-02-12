import azure.functions as func
import pandas as pd


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.form
        print(req_body)
        type = req_body["business_type"]
        if type.upper() == "B2B":
            print("B2B")
            df = pd.read_csv(req.files.get('file1'))
            print(df)
        
        if type.upper() == "B2C":
            print("B2C")
        
        return func.HttpResponse("executed successfully.")
    except Exception as exp:
        print(exp)
        return func.HttpResponse("unsuccessfully.")
