import os
import oci
import io
import filecmp
# from oci.object_storage.models import CreateBucketDetails


config = oci.config.from_file('/home/app/.oci/config')
compartment_id = config["tenancy"]
object_storage = oci.object_storage.ObjectStorageClient(config)
namespace = object_storage.get_namespace().data
bucket_name = "list-instances-bucket"

object_name = "instances.csv"
destination_dir = '/home/app'.format(object_name) 
get_obj = object_storage.get_object(namespace, bucket_name, object_name)
with open(os.path.join(destination_dir,object_name), 'wb') as f:
    for chunk in get_obj.data.raw.stream(1024 * 1024, decode_content=False):
        f.write(chunk)

