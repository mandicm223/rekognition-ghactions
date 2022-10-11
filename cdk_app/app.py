#!/usr/bin/env python3

import aws_cdk as cdk


from cdk_app.cdk_app_stack import BussinesLogicStack


app = cdk.App()
BussinesLogicStack(app, "cdk-app")

app.synth()
