
import boto3
from warnings import Filter, filters
from botocore.exceptions import ClientError

with open ("users.txt", "r") as fp:
    USERDATA_B64_STR = fp.read()

class Creating_ec2(object):
    def __init__(self,ec2_client):
        self.ec2_client=ec2_client


# creating a secrutiy group
    def creat_VPC(self):
        vpc_id=""
        response=self.ec2_client.describe_vpcs()
        for vpc in response["Vpcs"]:
            if vpc["Tags"][0]["value"].__contain__("Default"):
                vpc_id=vpc["VpcId"]
                break
        response=self.ec2_client.describe_subnets(filters=[{"Name":"vpc-id","Values":[vpc_id]}])
        subnet_id=response["Subnets"][0]["SubnetId"]
        az=response["Subnets"][0]["AvailabilityZone"]
        return vpc_id,subnet_id,az

    def create_security_group(self):
        sg_name="Secruity_group"
        try:
            vpc_id,subnet_id,az=self.creat_VPC()
            response=self.ec2_client.create_security_group(
                GroupName=sg_name,
                Description="This is a SG created using boto3",
                VpcId = vpc_id 
            )
            sg_id=response["GroupId"]
            sg_config=self.ec2_client.authorize_security_group_ingress(
                GroupId=sg_id,
                IpPermissions=[
                    {
                        'IpProtocol':'tcp',
                        'FromPort':22,
                        'ToPort':22,
                        'IpRanges':[{'CidrIp':'0.0.0.0/0'}]
                    }
                ]
            )
            return sg_id,sg_name
        except Exception as e:
            if str(e).__contains__("already exists"):
                response=self.ec2_client.describe_security_groups(GroupName=[sg_name])
                print(response)
                sg_id=response["SecurityGroups"][0]["GroupId"]
                print(sg_id,sg_name)
                return sg_id,sg_name

    def create_ec2_launch_template(self):
        print("creating lauch template")
        template_name='aws_launch_template'
        try:
            sg_id,sg_name=self.create_security_group()
            response=self.ec2_client.create_launch_template(
                LaunchTemplateName=template_name,
                LaunchTemplateData={
                    'ImageId':"ami-0c02fb55956c7d316",
                    'InstanceType':"t2.micro",
                    'KeyName':"ec2_develop",
                    'UserData':USERDATA_B64_STR,
                    'SecurityGroupIds':[sg_id],
                }
            )
            template_id=response['LaunchTemplate']['LaunchTemplateId']
            print('crwating launch template:completed:Template ID:{}, Template Name:{}'.format(template_id,template_name))
        except Exception as e:
            response=self.ec2_client.describe_launch_templates(
                LaunchTemplateNames=[template_name]

            )
            template_id=response['LaunchTemplate'][0]['LaunchTemplateId']
            return template_id,template_name

    def create_ec2_auto_scaling_group(self):
        print("started")
        launch_template_id,launch_template_name=self.create_ec2_launch_template()
        vpc_id,subnet,az=self.creat_VPC()
        client=boto3.client('autoscaling')
        response=client.create_auto_scaling_group(
            AutoScalingGroupName='awspy_autoscaling_group',
            LaunchTemplate={
                'LaunchTemplayeId':launch_template_id,
            },
            MinSize=1,
            MaxSize=3,
            AvailabilityZone=[
                az,
            ],
        )
        if str(response['RespornseMatedata']['HTTPStatusCode'])=="200":
            print('hi')
        else:
            print('bye')
    

try:
    ec2_client=boto3.client('ec2')
    call_obj= Creating_ec2(ec2_client)
    call_obj.create_ec2_auto_scaling_group()
except ClientError as e:
    print(e)