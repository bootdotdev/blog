categories:
- Development
- Python and AWS
date: "2022-09-27"
description: AWS Boto3, Python SDK in AWS
tags:
- AWS
- Python
name: 
- Denis Kinyungu  
title:  Understanding AWS Boto3 the right way.ls
image: ![Cover image]('./static/image/aws_boto.webp')
dofollows:
  - "https://www.dev.to/kinyungu_denis"




## Introduction to AWS Boto3

AWS Boto3 is the AWS Software Development Kit (SDK) for Python. Python interacts with Amazon Web Services such as compute, storage, alerts using Boto.
To use Boto, you need to install it in our system. It only involves a simple command in Linux.
Install the latest Boto3 release via pip:

```
pip install boto3
```

Before using Boto3, you need to set up authentication credentials for your AWS account using either the IAM Console or the AWS CLI. You can either choose an existing user or create a new one.
If you have the AWS CLI installed, then you can use the aws configure command to configure your credentials file in your terminal:

```
aws configure
```


```
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```

Our user identity key is access key  and secret key is users password that are needed to login an aws account.You have now configured credentials for the default profile to use when creating connections.


## SDK features:

* Session - a session manages state about a particular configuration. By default, a session is created for you when needed. It's possible and recommended that in some scenarios you maintain your own session.
* Client - provide a low-level interface to AWS whose methods map close  with service Application Programming Interfaces, supports service operations.
* Paginators -some AWS operations return results that are incomplete and require subsequent requests in order to attain the entire result set. The process of sending subsequent requests to continue where a previous request left off is called pagination. 
* Resource - resources represent an object-oriented interface to Amazon Web Services . They provide a higher-level abstraction than the raw, low-level calls made by service clients.


Amazon web services offer storage, compute, alerts for resources and others. Create an account on [Amazon](https:amazon.com)
In the AWS management console log with username and password that you signed up with. This is the root account and it has the all permission for the AWS services, we need to create a user and attach policies to the user. Search for IAM in the console, click on the users, add users, enter username and give the access type. Attach new policies to the new user such as Amazons3FullAccess, AmazonSNSFullAccess, AmazonRekognitionFullAccess, ComprehendFullAccess and create the user. Grab the access key id, secret access key and store it in a safe place.

We look at the following AWS services:
* AWS s3 -       simple storage in AWS
* SNS -          simple notification service to send emails sms and text based on events.
* AWS Comprehend - helps in sentimental anaysis from text
* AWS Rekognition - enables us to extract text from images


## Amazon s3

It refers to simple storage in Amazon Web Services. The main components are buckets, objects; buckets are like the folders in our local computers and objects are like the files in the folders. So objects are contained in a bucket. An object can be any file, an image or a video. We can create a bucket, list buckets or even delete buckets, knowing to work with buckets is crucial knowledge in s3 storage.

Creating a bucket: 

```
import boto3
s3 = boto3.client('s3', region_name='us-east-1', aws_access_key_id=AWS_KEY_ID, aws_secret_access_key=AWS_SECRET)

bucket = s3.create_bucket(Bucket='kimani_sample_bucket')
```

Bucket names should be unique, as AWS does not allow buckets having the same name.



Listing buckets

```
import boto3
s3 = boto3.client('s3', region_name='us-east-1', aws_access_key_id=AWS_KEY_ID, aws_secret_access_key=AWS_SECRET)

bucket_list = s3.list_bucket()
buckets = bucket_list['Buckets']
print(buckets)
```


Deleting buckets

```
import boto3
s3 = boto3.client('s3', region_name='us-east-1', aws_access_key_id=AWS_KEY_ID, aws_secret_access_key=AWS_SECRET)

response = s3.delete('kimani_sample_bucket')


Buckets contain objects, we can create, list, delete objects and also upload files. An object has a key and can only be one in a bucket as it is unique.


uploading files

```
import boto3
s3 = boto3.client('s3', region_name='us-east-1', aws_access_key_id=AWS_KEY_ID, aws_secret_access_key=AWS_SECRET)

s3.upload_file(Filename='sampled_22.csv', Bucket='sampled', Key='sampled_22.csv')

```

Listing files

```
import boto3
s3 = boto3.client('s3', region_name='us-east-1', aws_access_key_id=AWS_KEY_ID, aws_secret_access_key=AWS_SECRET)

response = list_objects(Bucket='sampled', Maxkeys=2, Prefix='sampled_')
print(response)
```

The response will contain the contents in the bucket and the related information

Getting object metadata and download files

```
response = s3.head_object(Bucket='sampled', Key='sampled_23.csv')
print(reponse)

s3.download_file(filename='sampled_downloaded.csv, Bucket='sampled', Key='sampled_23.csv')
```

Deleting objects

```
s3.delete_object(Bucket='sampled', Key='sampled_23.csv')
```


## Sharing files securely

To keep objects secure using the AWS permissions system. If we upload a file by default aws denies permissions only our key id and secret key have access to it. 
To allow permissions, we have to generate boto3 client for interacting with s3, use the client to download a file

```
s3 = boto3.client('s3', region_name='us-east-1', aws_access_key_id=AWS_kEY_ID, aws_secret_access_key=AWS_SECRET)

s3.download_file(Filename='values.csv', Bucket='sampled', KEY='values.csv')
```

How to control permissions in s3:
* Identity Access Management permissions to control user access to AWS services, objects, buckets by attaching IAM policies to a user and it applies across all AWS services.
* Bucket policy - gives control on the bucket and objects with it.
* Access Control Lists sets permission on specific objects with a bucket. The entities attached in s3, it can either be 'public-read' or 'private'
* Presigned URL - this provides temporary access to an object


Setting ACLs when uploading a file to s3

```
s3.upload_file(Bucket='sampled', Filename='values.csv', Key='values.csv', ExtraArgs={'ACL': 'public-read'})
```

How does on access a public object

`https://{bucket}.{key}`


How to generate a public object url, you begin with generating object URL string

```
url = "https://{}.{}".format("sampled", "values.csv")

# use pandas to read the url
df = pd.read_csv(url)
```

For this request, it checks if we have predesigned URL to call to downloading, if not it will check if IAM bucket policy, ACL policy and decide whether to allow downloading or refuse downloading. Recall AWS default behaviour is to deny permissions.
IAM permissions decides what can the assigned user do in AWS. Bucket policy answers who can access this s3 bucket. ACL decides who can access the objects. Presigned URL's will provide temporary access to the object.


### How to access private objects in s3

We have two options to access private objects in s3, you may download the required file then read it from disk or simply use the `.get_object()`.

```
obj = s3.get_object(Bucket='sampled', Key='22/values.csv')
print('obj')
```

You may want not to read the whole file and view the body, `.get_object` has a streaming body that does not display the whole file, here is how you use it.

```
obj = s3.get_object(Bucket='sampled', Key='22/values.csv')
```

How to use presigned URL, to access objects, they do expire after a certain timeframe and great for temporary access.
Begin with uploading and generate a predesigned URL

```
s3.upload_file(Filename='./values.csv', Key='values.csv', Bucket='sampled')

share_url = s3.generate_predesigned_url(ClientMethod='get_object', ExpiresIn=3600, 
            Params={'Bucket': 'sampled', 'Key': 'values.csv'} )

```

You can use pandas to read the file `pd.read_csv(share_url)`

To load multiple files into one DataFrame, you create a list, request the list of csv's from s3 with prefix, get the response contents, you can iterate over the objects and read it as DataFrame. Then append the DataFrame to list, concatenate all the DataFrames in the list and finally view the DataFrame.

```
df_list =[]

response = s3.list_objects(Bucket='sampled', Prefix='22/')
request_files = response['Contents']

# iterate over each object
for file in request_files:
  obj = s3.get_object(Bucket='sampled', Key=file['Key'])

obj_df = pd.read_csv(obj['Body'])
df_list.append(obj_df)

# concatenate all the DataFrames in the list
df = pd.concat(df_list)
df.head()
```


## How to share files through a website

AWS s3 is able to serve as HTML pages. You can conveert DataFrame to html, render the columns that we need and apply borders.

```
df.to_html('values_tallied.html', render_links=True, columns['service_name', 'request_count', 'info_link'], border=0)
```

How to upload HTML files, image files and access them

```
s3.upload_file(filename='./values_tallied.html', Bucket='richard-website', Key='values.html', 
  ExtraArgs={'ContentType': 'text/html', 'ACL': 'public-read'})


s3.upload_file(Filename='./plot_image.png', Bucket='richard-website', Key='plot_image.png',
  ExtraArgs={'ContentType': 'image/png', 'ACL': 'public-read'})
```

You can also generate an index page, check the objects in your bucket, convert the contents to a DataFrame, write your DataFrame to html and finally upload your index page.


```
listed = s3.list_objects(Bucket='sampled', Prefix='22/')
objects_df = pd.DataFrame(listed['Contents'])
objects_df.to_html('report_listing.html', columns=['Link', 'LastModified', 'size'], render_links=True)

# upload index page
s3.upload_file(Filename='./report_listing.html', Bucket='richard-website', Key='index.html',
  ExtraArgs={'ContentType': 'text/html', 'ACl': 'public-read'})
```


Understanding how we can use AWS Boto3 together AWS s3 storage, lets do a simple project to use what you have learnt.
Let's prepare data, download files for the month from a raw data bucket. Concatenate them into one csv file. Create a DataFrame for our report. Write the DataFrame to csv and HTML. Generate a plot that you will save as HTML file. Then upload your report to a shareable website. Create bucket, upload files for the month to s3 storage. Generate an index.html file that exists in all the files. Finally get the website URL.


```
df_list = []

response = s3.list_objects(Bucket='sampled', Prefix='22_Sept')
request_files = response['Contents']

# iterate over each object
for file in request_files:
  obj = s3.get_object(Bucket='sampled', Key=File['Key'])

obj_df = pd.read_csv(obj['Body'])

# append our DataFrame to list
df_list.append(obj_df)

# concatenate all the DataFrames in the list
df = pd.concat(df_list)

# preview the DataFrame
df.head()

# Write agg_df to a CSV and HTML file with no border
df.to_csv('./sept_final_report.csv')
df.to_html('./sept_final_report.html', border=0)

# uploading the aggregated csv and html

s3.upload_file(Filename='./sept_final_report.csv', Key='22/sept/final_report.csv', Bucket='sampled',
  ExtraArgs={'ContentType': 'text/html', 'ACL': 'public-read'})

s3.upload_file(Filename='./sept_final_report.csv', Key='22/sept/final_report.html', Bucket='sampled', 
  ExtraArgs={'ContentType': 'text/html', 'ACL': 'public-read'})


# upload HTML chart

s3.upload_file(Filename='./sept_final_chart', Key='22/sept/final_chart.html', Bucket='sampled',
  ExtraArgs={'ContentType': 'text/html', 'ACL': 'public-read'})


# create index.html, list bucket objects starting with 22/, convert the response to a DataFrame, then create a column link that contains website url and key

listed = s3.lists_objects(Bucket='sampled', Prefix='22/')
object_df = pd.dataFrame(listed['Contents'])

base_url = "https://sampled"
objects_df['Link'] = base_url + objects_df['Key']
objects_df.to_html('report_listing.html', columns = ['link', 'LastModified', 'Size'], render_links=True)


# upload the index.html file to bucket root

s3.upload_file(Filename='./report_listing.html', Key='index.html', Bucket='sampled',
  Extraargs={'Contenttype': 'text/html', 'ACL': 'public-read'})
```

To obtain the URL of the index and access the files `https://sampled.index.html`



Conclusion

Now you have good understanding about AWS Boto3 and AWS s3 storage. It's good to do it practically on your own so that you understand the concepts clearly.




































































































































