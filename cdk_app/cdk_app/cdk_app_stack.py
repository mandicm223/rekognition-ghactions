
from aws_cdk import CfnOutput, Duration, RemovalPolicy, Stack
from aws_cdk import aws_ec2 as _ec2
from aws_cdk import aws_iam as _iam
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_logs as _log
from constructs import Construct
from dotenv import dotenv_values

class BussinesLogicStack(Stack):

    def __init__(self, scope: Construct, construct_id: str,**kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        config = dotenv_values(".env")
        # Parameters from .env

        environment = config['ENV']
        first_name_last_name = config['FIRST_LAST_NAME']


        # GET Method Lambda

        lambda_func_get = _lambda.Function(self, 
                                           'lambda_api_get_func',
                                           runtime=_lambda.Runtime.PYTHON_3_9,
                                           function_name=f"{environment}-{first_name_last_name}-recognition",
                                           code=_lambda.AssetCode("./Functions"),
                                           handler='lambda_rekognition.lambda_handler'
                                    )

        # GET Method Lambda LG

        lambda_lg_get = _log.LogGroup(self, 
                                      "lambda_mm_loggroup_get",
                                      log_group_name=f"/aws/lambda/{lambda_func_get.function_name}",
                                      removal_policy=RemovalPolicy.DESTROY,
                                )