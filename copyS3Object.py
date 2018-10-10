from __future__ import print_function

import json
import urllib
import boto3

print('Loading function')

s3 = boto3.resource('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    src_bucket = s3.Bucket("bucket_1")
    print("source bucket name: "+src_bucket.name)
    
    dest_bucket = s3.Bucket("bucket_2")
    print("destination bucket name: "+dest_bucket.name)
    
    sourceObj = src_bucket.objects.filter(Prefix = "XXXX")
    
    try:
        for srcObj in src_bucket.objects.all() :
            print("srcObj key :"+srcObj.key)
            copy_source = {
                'Bucket': 'tempsourcebucket',
                'Key': srcObj.key
            }
            dest_obj = dest_bucket.Object(srcObj.key)
            dest_obj.copy(copy_source)
    except Exception as e:
        print(e)