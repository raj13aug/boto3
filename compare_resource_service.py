import boto3

aws_mag_con_root=boto3.session.Session()

iam_con_re=aws_mag_con_root.resource(service_name='iam',region_name="ap-southeast-2")
iam_con_cli=aws_mag_con_root.client(service_name='iam', region_name="ap-southeast-2")

#listing iam users with resource object:
for each_user in iam_con_re.users.all():
    print(each_user.name)
print("-----------------------------------------")
#listing iam users with client object:

for each in iam_con_cli.list_users()['Users']:
    print(each['UserName'])