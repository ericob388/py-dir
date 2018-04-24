import boto3
import botocore


def get_file(bucket, key, local_path):
    s3 = boto3.resource('s3')

    try:
        s3.Bucket(bucket).download_file(key, local_path)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
