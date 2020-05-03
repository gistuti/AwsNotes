*DAY 4*

Direct communication between the two services **(for example EC-2 and S3)** is not possible in *AWS*.

We can do this in two ways / - Inside AWS,**and** - Outside AWS.

*# Inside AWS *

We can do this by using *IAM Roles* which can be defined as the identity authentication.There are some rules or policies in it through which we can decide the permissions for accessing the services.


## Steps to Attach IAM Roles to EC-2:


1. Select services from the home page.


2. Select Roles.


3. Select the option Create Roles


4. Select EC-2 and click on permissions.


5. Select AmazonS3FullAccess.


6. From the drop down select JSON: Here the value present is in the form i.e. **{key:value}**


7. Select Next Tag.


8. Select Review and give a role name for example *Demo* and then select Create.



## How to attach EC-2 with IAM.

1. Select EC-2 from services.
2. Select the instance.
3. Go to Settings.
4. Select Attach/Rename IAM.
5. From the drop down select the IAM example *Demo*.


## Commands to be used on MobaXterm.

aws s3 ls *(name of bucket)*



                                
                               
