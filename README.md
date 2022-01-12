Simlple Repository to test S3 functions with AWS

**Usage** :

Build the image : 

```
docker build -t aws_ex . 
```

After it completes, simply run :
```
docker run --rm aws_ex python get_size.py -f file_to_analyse -b bucket_name -id your_key_id -k your_access_key
```