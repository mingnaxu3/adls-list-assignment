from azure.storage.blob import BlobServiceClient

def main():
    # Define the blob service URL
    service_url = "https://azurepublicdatasettraces.blob.core.windows.net/"

    # Create a BlobServiceClient
    blob_service_client = BlobServiceClient(account_url=service_url)

    # Define the container name
    container_name = "azurepublicdataset"

    # List all blobs in the container
    container_client = blob_service_client.get_container_client(container_name)


    #filter for the files ending in '.csv.gz'
    #the list is container_client.list_blobs()
    

    print(f"Listing files in container: {container_name}")
    for blob in container_client.list_blobs():
        #blob is a BlobProperties element 
        #the name of the blob is a string so can just python str function, endswith()

        #do i need to actually modify the list or can i just filter it out 
        if blob.name.endswith(".csv.gz"):
          print(blob.name)

if __name__ == "__main__":
    main()
