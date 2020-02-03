import oci
import os
import io
import filecmp
from oci.object_storage.models import CreateBucketDetails

config = oci.config.from_file('/home/app/.oci/config')
compartment_id = config["tenancy"]
object_storage = oci.object_storage.ObjectStorageClient(config)


namespace = object_storage.get_namespace().data
bucket_name = "list-instances-bucket"

directory = '/home/app'
files_to_process = [file for file in os.listdir(directory) if file.endswith('csv')]

getbucket = object_storage.list_buckets(namespace, compartment_id)

for bucket in getbucket.data:
    if bucket.name == bucket_name:
        print('Bucket Already exists')
        break
    else:
        print("Creating a new bucket {!r} in compartment {!r}".format(
    bucket_name, compartment_id))
    request = CreateBucketDetails()
    request.compartment_id = compartment_id
    request.name = bucket_name
    bucket = object_storage.create_bucket(namespace, request)

for upload_file in files_to_process:
    print('Uploading file {}'.format(upload_file))
    object_storage.put_object(namespace, bucket_name, upload_file, io.open(os.path.join(directory,upload_file),'r'))