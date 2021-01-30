from google.cloud import storage

import os
import sys



number_of_args = len(sys.argv)
print("Arguments: ", str(sys.argv))
if number_of_args != 2:
    raise Exception('Pass one module name. Number of arguments:', number_of_args, 'arguments.', str(sys.argv))

if not os.path.exists('modules'):
    os.makedirs('modules')
f = open("modules/__init__.py", "w")

bucket_name = "modules_for_kubernetes"
source_blob_name = str(sys.argv[1])+".py"
destination_file_name = "modules/model.py"

storage_client = storage.Client()

bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(source_blob_name)
blob.download_to_filename(destination_file_name)

from modules import model

Model = model.Model()
Model.run()


