from google.cloud import storage


class BucketConfig:

    # Cloud Storage Bucket Methods
    # Bucket Connection
    @staticmethod
    def getbucketconn():
        try:
            storage_client = storage.Client.from_service_account_json(
                'C:/Users/Shubham Snehi/Downloads/awacs-dev-160bf0e57dc1.json')
            bucket = storage_client.get_bucket('balatestawacs')
            print("Bucket Connection Successful")
            return bucket
        except:
            print("Unable to connect bucket")
        return

    # Get List of files in Bucket
    @staticmethod
    def getbuckectfilelist(bucket):
        try:
            files = [files.name for files in list(bucket.list_blobs(prefix=''))]
        except:
            files = "Failed to get files"
        return files

    # Upload File to Bucket
    @staticmethod
    def uploadtobucket(tempfilepath, myfile, uploadbucket):
        try:
            storage_client = storage.Client.from_service_account_json(
                'C:/Users/Shubham Snehi/Downloads/awacs-dev-160bf0e57dc1.json')
            bucket = storage_client.get_bucket(uploadbucket)
            print("Upload Bucket Connection Successful")
            blob = bucket.blob('portedfiles1/' + myfile.filePath + '/' + myfile.fileName + '.csv')
            blob.upload_from_filename(tempfilepath)
            print("File Uploaded Successfully!")
            print("File Name:", myfile.fileName + '.csv', "File Time:", myfile.fileDate,
                  "File Path:", myfile.filePath, "Upload Bucket:", myfile.uploadBucket)
            return
        except:
            return "File Didn't Uploaded"
