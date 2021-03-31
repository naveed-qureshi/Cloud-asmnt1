import boto3
import os
s3=boto3.client('s3')
images=os.listdir('./images')
for img in images:
	s3.upload_file('./images/'+img,'bucket534',img)
