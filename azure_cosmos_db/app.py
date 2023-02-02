
import pandas as pd 
import json
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import azure.cosmos.documents as documents
import azure.cosmos.http_constants as http_constants

print('Imported packages successfully.')

# Initialize the Cosmos client

config = {
    "endpoint": "YOUR ENDPOINT HERE",
    "primarykey": "YOUR PRIMARY KEY HERE"
}

# Create the cosmos client
client = cosmos_client.CosmosClient(url_connection=config["endpoint"], auth={"masterKey":config["primarykey"]}
)

# Create a database
# https://docs.microsoft.com/en-us/python/api/azure-cosmos/azure.cosmos.cosmos_client.cosmosclient?view=azure-python#createdatabase-database--options-none-

database_name = 'posgres-az204'
try:
    database = client.CreateDatabase({'id': database_name})
except errors.HTTPFailure:
    database = client.ReadDatabase("dbs/" + database_name)

# Create a collection of items in a Container
# Items are the individual rows/records of your dataset
# https://docs.microsoft.com/en-us/python/api/azure-cosmos/azure.cosmos.cosmos_client.cosmosclient?view=azure-python#createcontainer-database-link--collection--options-none-

database_link = 'dbs/' + 'posgres-az204'
container_definition = {'id': 'HDIcontainer',
                        'partitionKey':
                                    {
                                        'paths': ['/country'],
                                        'kind': documents.PartitionKind.Hash
                                    }
                        }
try:
    container = client.CreateContainer(database_link=database_link, 
                                        collection=container_definition, 
                                        options={'offerThroughput': 400})
except errors.HTTPFailure as e:
    if e.status_code == http_constants.StatusCodes.CONFLICT:
        container = client.ReadContainer("dbs/" + database['id'] + "/colls/" + container_definition['id'])
    else:
        raise e


# Download and read csv file
df = pd.read_csv('https://globaldatalab.org/assets/2019/09/SHDI%20Complete%203.0.csv',encoding='ISO-8859–1',dtype='str')
# Reset index - creates a column called 'index'
df = df.reset_index()
# Rename that new column 'id'
# Cosmos DB needs one column named 'id'. 
df = df.rename(columns={'index':'id'})
# Convert the id column to a string - this is a document database.
df['id'] = df['id'].astype(str)


# https://docs.microsoft.com/en-us/python/api/azure-cosmos/azure.cosmos.cosmos_client.cosmosclient?view=azure-python#upsertitem-database-or-container-link--document--options-none-
# Write rows of a pandas DataFrame as items to the Database Container

# Create Connection Link string
collection_link = database_link + '/colls/' + 'HDIcontainer'

# Write rows of a pandas DataFrame as items to the Database Container
for i in range(0,df.shape[0]):
    # create a dictionary for the selected row
    data_dict = dict(df.iloc[i,:])
    # convert the dictionary to a json object.
    data_dict = json.dumps(data_dict)
    insert_data = client.UpsertItem(collection_link,json.loads(data_dict)
    )
print('Records inserted successfully.')