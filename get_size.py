import argparse 
import boto3

if __name__=="__main__":

    parser = argparse.ArgumentParser(description='Random script')
    parser.add_argument('-b', '--bucket_name', type=str, help='Bucket name')
    parser.add_argument('-id', '--access_key_id', type=str, help='AWS access key ID',default=None)
    parser.add_argument('-k', '--access_key', type=str, help='AWS access key',default=None)
    parser.add_argument('-f', '--file', type=str, help='Path to the file to parse',default=None)
    args = parser.parse_args()

    session = boto3.Session(aws_access_key_id=args.access_key_id,aws_secret_access_key=args.access_key)
    client = session.client("s3")
    response = client.head_object(Bucket=args.bucket_name,Key=args.file)
    size = response['ContentLength']
    print("File size :",size)