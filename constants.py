import io
import json
import logging
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from repo_location import REPO_LOCATION

import boto3
import h5py


@dataclass
class Ssl4eoMulti:

    aws_arn: str = "arn:aws:s3:::ssl4eo-s12-landsat-combined"
    aws_region: str = "us-west-2"
    location_file = REPO_LOCATION / "location_prefix.txt"
    s3_bucket: str =  "ssl4eo-s12-landsat-combined"

    @classmethod
    def get_qualified_path(cls) -> str:
        return f"s3://{cls.s3_bucket}"
    
    @classmethod
    def get_s3_bucket(cls) -> "boto3.resources.factory.s3.Bucket":
        s3 = boto3.resource("s3")
        return s3.Bucket(cls.s3_bucket)

    @classmethod
    def __fetch_object_keys(cls, page):
        # Each page is already a dictionary
        if 'Contents' in page:
            logging.info(f"Processing page with {len(page['Contents'])} objects")
            return [obj['Key'] for obj in page['Contents']]
        else:
            return []

    @classmethod
    def get_all_objects_in_bucket(cls, save_folders: bool = False) -> list:
        """
        Running function with save_folder = True is very time-consuming.
        It will give all the elements in a bucket.
        For ease of access, a list of all possible locations have been saved 
        at "location_prefix.txt". These can be used as prefix with
        cls.get_location_data to get data for a particular location.

        By default, the function returns the top page elements in the bucket.         
        """
        s3 = boto3.client('s3')
        logging.info(f"Starting to fetch objects from bucket: {cls.s3_bucket}")
        
        if save_folders:
            paginator = s3.get_paginator('list_objects_v2')
            pages = paginator.paginate(Bucket=cls.s3_bucket)
            bucket_ob = []
            with ThreadPoolExecutor() as executor:
                results = executor.map(cls.__fetch_object_keys, pages)
                for keys in results:
                    bucket_ob.extend(keys)

            folders = set()
            for item in bucket_ob:
                folders.add(item.split('/')[0]) 

            if cls.location_file.exists():
                with open(cls.location_file.as_posix(), "r") as f:
                    existing_folders = [i.strip() for i in f.readlines()]
                    folders = folders - set(existing_folders)
                    if len(folders):
                        existing_folders.extend(folders)
                        cls.__write_locations(existing_folders)
            else:
                cls.__write_locations(folders)

            return bucket_ob

        else:
            return s3.list_objects_v2(Bucket=cls.s3_bucket)["Contents"]
        
    @classmethod
    def list_all_files_recursively(cls, prefix: str):
        s3 = boto3.client('s3')
        paginator = s3.get_paginator('list_objects_v2')
        operation_parameters = {'Bucket': Ssl4eoMulti.s3_bucket, 'Prefix': prefix}
        page_iterator = paginator.paginate(**operation_parameters)
        files = []

        try:
            for page in page_iterator:
                if "Contents" in page:
                    for obj in page["Contents"]:
                        files.append(obj["Key"])
                    
            return files
        
        except Exception as e:
            print(f"Error fetching objects from S3: {e}")
            return []
        
    @classmethod
    def fetch_and_process_file(cls, s3_key: str):
        s3 = boto3.client('s3')
        
        try:
            response = s3.get_object(Bucket=cls.s3_bucket, Key=s3_key)
            file_content = response['Body'].read()
            
            if s3_key.endswith('.h5'):
                with h5py.File(io.BytesIO(file_content), 'r') as h5file:
                    data = h5file["data"][:]
                
                    return data
            elif s3_key.endswith('.json'):
                json_content = json.loads(file_content.decode('utf-8'))
                return json_content
        
        except Exception as e:
            print(f"Error fetching file from S3: {e}")


    @classmethod
    def __write_locations(cls, folders):
        """Helper method to write folder names to the location file"""
        with open(cls.location_file.as_posix(), "w") as f:
            for folder in folders:
                f.write(f"{folder}\n")

if __name__ == "__main__":

    Ssl4eoMulti.get_all_objects_in_bucket(top_1000=False, save_folders=True)
    