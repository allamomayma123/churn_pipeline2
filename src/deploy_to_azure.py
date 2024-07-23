import os

def deploy_to_azure():
    os.system("az webapp up --name <app-name> --resource-group <resource-group> --plan <app-service-plan>")

if __name__ == "__main__":
    deploy_to_azure()
