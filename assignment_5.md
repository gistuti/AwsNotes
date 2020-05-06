If we are accessing the s3 from outside i.e. locallaptop then we need to use the secret key and access key.

# Difference between RDS in AWS and RDS inside EC-2 in AWS.

	                                         |RDS in AWS|RDS inside EC-2 in AWS|
	


	|It is managed by AWS and it is a dedicated AWS server|EC-2 is mananged by AWS but any application inside will be managed by developers|

			      |Scalability is maintained by AWS | Developer need to do the maintainance|

	                                          |It is costly | It is Cheap|

- S3 is a **bucket** and everything in thus bucket is an object and these objects are immutable.

- Lambda Function (serverless): - It does not have a server, - It requires no maintainance, - Automatic scalability is present, - Charged according to the compute time.

- Difference between EC-2 Server and Lambda Function i.e. Serverless.


	                          |EC-2 Server|Lambda Function|

	  |Charges applied for storing the code|No charges for storing the code|
	
	  |Hourly charges for instance running|When the code is triggered then they calculate the time ,memory and CPU is used.|

	
# How to launch Lambda Function. 

 * 1. Select Lambda from services and select create function *

![day5_1](https://user-images.githubusercontent.com/63596252/81172279-946c4000-8fbb-11ea-9476-e7ff8654997a.png)

 * 2. Select * Use a blueprint * and search for hello and select hello-world python. *
![day5_2](https://user-images.githubusercontent.com/63596252/81172282-959d6d00-8fbb-11ea-9bfe-c298f5d13bad.png)

 * 3. Use existing role and give function name. *
![day5_3](https://user-images.githubusercontent.com/63596252/81172283-96360380-8fbb-11ea-9000-e3ed1aab497a.png)

 * 4. Click on Create Function. *
![day5_4](https://user-images.githubusercontent.com/63596252/81172284-96360380-8fbb-11ea-9a86-9058c0b6c10c.png)

 * 5.Select the function created. *
![day5_5](https://user-images.githubusercontent.com/63596252/81172286-96ce9a00-8fbb-11ea-9b16-d4a9b36325b9.png)

 * 6. Click on test and give desired values. *
![day5_6](https://user-images.githubusercontent.com/63596252/81172287-96ce9a00-8fbb-11ea-9e62-40fe32747b76.png)

 * 7. Save the code and Test it. *
![day5_7](https://user-images.githubusercontent.com/63596252/81172290-97673080-8fbb-11ea-895d-37d7e7638296.png)
