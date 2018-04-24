import boto3


# Ensure AWS Credentials are configured
sts = boto3.client('sts')
arn = sts.get_caller_identity()['Arn']
