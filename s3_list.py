import boto3

aws_ma_con = boto3.session.Session()
s3_service = aws_ma_con.resource('s3')

for each_s3 in s3_service.buckets.all():
    print(each_s3)
