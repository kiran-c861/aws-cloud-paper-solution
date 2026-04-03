import boto3
import os
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

def s3_operations(bucket, file_path):
    try:
        # Create bucket
        s3.create_bucket(
            Bucket=bucket,
            CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}
        )
        print("✅ Bucket created")

        # Enable versioning
        s3.put_bucket_versioning(
            Bucket=bucket,
            VersioningConfiguration={'Status': 'Enabled'}
        )
        print("✅ Versioning enabled")

        # Check file
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"{file_path} not found")

        # Upload with metadata
        s3.upload_file(
            file_path,
            bucket,
            os.path.basename(file_path),
            ExtraArgs={"Metadata": {"owner": "prateek"}}
        )
        print("✅ File uploaded with metadata")

    except FileNotFoundError as e:
        print(f"❌ {e}")
    except ClientError as e:
        print(f"❌ AWS Error: {e}")

# Run
s3_operations("my-bucket-fk-it-12345", "sample.txt")