If we are accessing the s3 from outside i.e. locallaptop then we need to use the secret key and access key.

Difference between RDS in AWS and RDS inside EC-2 in AWS.

	|RDS in AWS|RDS inside EC-2 in AWS|
	
	|---------------------------------|

	|It is managed by AWS and it is a dedicated AWS server|EC-2 is mananged by AWS but any application inside will be managed by developers|

	|Scalability is maintained by AWS| Developer need to do the maintainance|

	|It is costly| It is Cheap|

# S3 is a **bucket** and everything in thus bucket is an object and these objects are immutable.

# Lambda Function (serverless): - It does not have a server, - It requires no maintainance, - Automatic scalability is present, - Charged according to the compute time.

# Difference between EC-2 Server and Lambda Function i.e. Serverless.


	|EC-2 Server|Lambda Function|

	|Charges applied for storing the code|No charges for storing the code|
	
	|Hourly charges for instance running|When the code is triggered then they calculate the time ,memory and CPU is used.|

	
# How to launch Lambda Function.



	 
