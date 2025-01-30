import boto3
from dotenv import load_dotenv
import os

load_dotenv()

try :
    ec2 = boto3.client('ec2',
                    os.getenv('AWS_REGION'),
                    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                    aws_session_token=os.getenv('AWS_SESSION_TOKEN')
                    )
    print("Ec2: ", ec2.describe_instances())
except Exception as e:
    print(e)