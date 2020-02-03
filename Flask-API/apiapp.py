import json
from flask import Flask
import os
import oci
import io
import filecmp
from oci.object_storage.models import CreateBucketDetails


config = oci.config.from_file()
compartment_id = config["tenancy"]
object_storage = oci.object_storage.ObjectStorageClient(config)
namespace = object_storage.get_namespace().data
bucket_name = "list-instances-bucket"

object_name = "instances.json"
destination_dir = '/Users/prassark/'.format(object_name) 
get_obj = object_storage.get_object(namespace, bucket_name, object_name)
with open(os.path.join(destination_dir,object_name), 'wb') as f:
    for chunk in get_obj.data.raw.stream(1024 * 1024, decode_content=False):
        f.write(chunk)


app = Flask(__name__)

# We're using the new route that allows us to read a date from the URL
@app.route('/instances')

def readinstance():
    filename = os.path.join(app.static_folder, '/Users/prassark/instances.json')
    with open(filename) as instance_list:
        data = json.load(instance_list)
    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True)