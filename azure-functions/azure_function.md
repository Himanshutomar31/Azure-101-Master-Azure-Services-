Azure Functions:

1. A serverless application platform.
2. A simple way to run small piece of code("functions") in the cloud.
3. A Functions as a Service(faas) platform.
4. serverless means Delegate server management responsibility to the cloud provider. It automatically scale to meet demand, and billed only while ur code is running

Azure Function App
It is a collection of one or more related azure functions that are developed, deployed and hosted as a group.

Hosting Choices
-> Azure Functions usually run in a "Service plan" on Azure App Service.
Consumption Plan[Serverless] -> Serverless automatic scale [It has time limit of 5 mins]
App Service Plan -> Traditional pricing model [you are paying for resources you reserved]
Premium Plan -> speed, security and reserved instances.

Develoment Environment choices:

1.  Azure Portal
2.  Visual Studio
3.  Azure Function Core[Cross-platform CLI]

How to create azure function app from portal:
-> search for Function App, fill all the details and click on create.
-> create function app from cli.
-> step1: we will gonna create a resource group and storage account.
az group create --name "Azure-event-grid" --location "eastus" --tags "create-function-app-consumption"
az storage account create --name "Event-grid-storage" --location "eastus" --resource-group "Azure-event-grid" --sku "Standard_LRS"
az functionapp create --name "Azure_event_grid_architecture" --storage-account "Event-grid-storage" --consumption-plan-location "eastus" --resource-group "Azure-event-grid"
--os-type "Linux" --runtime "python" --runtime-version "3.9"

Function Triggers:
Triggers are what causes to execute azure functions.

1.  HTTP Request Trigger(webhooks)
2.  Time Trigger(scheduled tasks)
3.  blob Storage Trigger(data operation)
4.  Queue Trigger (run in response to a message on a queue)
5.  Cosmos DB Trigger
    and many more
    -> Every Azure Function has exactly one trigger
    -> The trigger is the event that causes the function to run.

        Lets discuss about 3 most common triggers:
        1. HTTP Trigger: Implement APIs or respond to webhooks
        				 Customization
        					-HTTP methods -eg GET or POST
        					-Route

        				  Secured via authorization key
        				    -Anonymous: no key required
        					-Function: key per function
        					-Admin: key per function app
        2. Timer Trigger: Run scheduled tasks
        				  we provide CRON expression

        3. Blob Trigger: data operation

        commands to create a function
        func init HttpDataEventGrid --python  [will create a function project]
        cd HttpDataEventGrid
        func new --name HttpExample --template "HTTP trigger" --authlevel "anonymous"
        func templates list -l python
        func start

Input and output bindings in azure funtions
A binding is a connection to data
Input Binding: Get data into our functions. Input bindings provides read-access to data.
Example: Blob Storage binding, cosmos db binding, microsoft graph (used to access one drive)
Output Bindings: Send messages, add document to a database Output bindings let us write to an external system.
Example: Blob Storage binding, Queue Storage binding
Functions can have multiple input and output bindings.
Azure Durable Functions
An extension to Azure Functions
Create stateful, serverless workflow("orchestration")
Three Types of Functions: 1. Client("Starter") Function: Initiate a new orchestration. 2. Orchestrator Function: Defines the steps in the workflow. Handle errors. 3. Activity Functions: Implements a step in the workflow, use any bindings.
Orchestration Patterns: 1. Function Chaining 2. Fan-out Fan-in 3. Asynchronous HTTP APIs 4. Monitor 5. Human Interaction
Implement Custom Handlers
-> Implement Azure Functions using your language or runtime of choices.
