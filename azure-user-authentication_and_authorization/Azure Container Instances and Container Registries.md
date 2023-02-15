Container fundamentals:
 -> Containerization of ur application allows you to package up your program's binaries libraries and other required components into a single deployable binary package 
    called container image.
 -> container Image is binary application package.
 -> container - runner container image.
 -> Generally very small and very portable.
 -> Container Registries - enables exchanging of container images.
 

Azure container registry:
Azure container registry is a managed Docker Registry Service based on the open source Docker Registry, allowing you to build, store, and managed container images
ACR tasks for container image automation
Service tiers(Basic, Standard, and premium)

ACR rquires authentication and security options
two ways: Azure Active Directory Identities
         ACR admin(by default it is disabled)
		 

acr login server is the public DNS name specifing the network location of our Azure Container Registry




az acr create 
--resource-group psdemo 
--name $ACR_NAME
--sku Standard 

to login in ACR registry
az acr login --name $ACR_NAME


== PUSH an Image into ACR ==
commands:
ACR_NAME = "psdemoacr"
ACR_LOGINSERVER=$(az acr show --name $ACR_NAME --query loginServer --output tsv)
docker tag webappimage:v1 $ACR_LOGINSERVER/webappimage:v1 
docker push $ACR_LOGINSERVER/webappimage:v1 

#build using ACR task 
az acr build --image "webappimage:v1-acr-task" --registry $ACR_NAME .


#creating a service principal for ACI to pull from ACR
 ACR_NAME='psdemoacr'
 ACR_REGISTRY_ID=$(az acr show --name $ACR_NAME --query id --output tsv)
 
 SP_NAME=acr-service-principal
 SP_PASSWORD=$(az ad sp create-for-rbac --name http://$ACR_NAME-pull --scopes $ACR_REGISTRY_ID --role acrpull --query password --output tsv)
 SP_APPID = $(az ad sp show --id http://$ACR_NAME-pull --query appID --output tsv)
 

#Running a container from ACR in ACI
az container create --resource-group psdemo-rg --name psdemo-webapp-cli --dns-name-label psdemo-webapp-cli --ports 80 --image $ACR_LOGINSERVER/webappimage:v1
--registry-login-server $ACR_LOGINSERVER --registry-username $SP_APPID --registry-password $SP_PASSWORD



docker
 
