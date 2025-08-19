import boto3
import os
from botocore.exceptions import NoCredentialsError

s3 = boto3.client('s3', aws_access_key_id='YOUR_ACCESS_KEY',
                        aws_secret_access_key='YOUR_SECRET_KEY')

BUCKET_NAME = 'your-bucket-name'

def upload_file_to_s3(file_bytes, filename):
    s3.put_object(Bucket=BUCKET_NAME, Key=filename, Body=file_bytes)
    return f"File {filename} uploaded to S3."

def generate_presigned_url(filename):
    url = s3.generate_presigned_url('get_object',
                                    Params={'Bucket': BUCKET_NAME, 'Key': filename},
                                    ExpiresIn=3600)
    return url
