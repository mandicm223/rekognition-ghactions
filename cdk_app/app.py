#!/usr/bin/env python3
import os
import aws_cdk as cdk
from aws_cdk import (
    Environment,
    App
)
from dotenv import load_dotenv

config = load_dotenv('.env')
environment = config['ENV']


from stacks.cdk_app_stack import BussinesLogicStack


app = cdk.App()
BussinesLogicStack(app,'{0}-stack-rekognition'.format(environment),
            env=Environment(account=os.getenv('AWS_ACCOUNT'),
                            region=os.getenv('AWS_REGION')))

app.synth()
