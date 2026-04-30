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
    

    #
    ## Exercise 3 — Count and Size Summary

    # Modify `list_contents.py` so that after printing the `.csv.gz` filenames, it also prints a summary line with
    # the **total file count** and **combined size in bytes**.

    # Expected output (values will differ):
    # ```
    # AzurePublicDatasetV2/trace1.csv.gz
    # AzurePublicDatasetV2/trace2.csv.gz
    # ...
    # ---
    # Total: 42 file(s), 8,301,204,512 bytes
    # ```

    print(f"Listing files in container: {container_name}")

    total_size = 0 
    total_file_count = 0
    for blob in container_client.list_blobs():
        #blob is a BlobProperties element 
        #the name of the blob is a string so can just python str function, endswith()

        #do i need to actually modify the list or can i just filter it out?
        #Filtering algorithm implementation: check if the string name endswith "csv.gz"
        if blob.name.endswith(".csv.gz"):
          print(blob.name)
          total_size+=blob.size
          total_file_count+=1
    
    print(f"Total file count is {total_file_count} and total combined size in bytes is {total_size}")

if __name__ == "__main__":
    main()
