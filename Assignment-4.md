*DAY 4*

Direct communication between the two services **(for example EC-2 and S3)** is not possible in *AWS*.

We can do this in two ways
- Inside AWS,**and**
- Outside AWS.

# Inside AWS 


We can do this by using *IAM Roles* which can be defined as the identity authentication.There are some rules or policies in it through which we can decide the permissions for accessing the services.


# Steps to Attach IAM Roles to EC-2:


## 1. Select services from the home page.

![IAM1](https://user-images.githubusercontent.com/63596252/80967905-c1dab180-8e34-11ea-8e7a-f37cf0bce65c.png)


## 2. Select Roles and create Roles.

![IAM2](https://user-images.githubusercontent.com/63596252/80967907-c2734800-8e34-11ea-905a-92e47199c52a.png)


## 3. Select EC-2 and click on permissions.

![IAM3](https://user-images.githubusercontent.com/63596252/80967912-c30bde80-8e34-11ea-86aa-1b69b277097e.png)


## 4. Select AmazonS3FullAccess.

![IAM4](https://user-images.githubusercontent.com/63596252/80967915-c3a47500-8e34-11ea-9300-86e3781133ff.png)

## 5. Give the Role name of your choice.

![IAM5](https://user-images.githubusercontent.com/63596252/80967920-c43d0b80-8e34-11ea-8ef2-28aeb6fc72d5.png)

## 6.Demo is created

![IAM6](https://user-images.githubusercontent.com/63596252/80967923-c4d5a200-8e34-11ea-82a1-90efcde68d7b.png)





## How to attach EC-2 with IAM.

## 1. Select EC-2 from services.
## 2. Select the instance.
## 3. Go to Settings.
## 4. Select Attach/Rename IAM.

![IAM7](https://user-images.githubusercontent.com/63596252/80967924-c56e3880-8e34-11ea-965f-4ea38a21d55d.png)

## 5. From the drop down select the IAM example *Demo*.

![IAM8](https://user-images.githubusercontent.com/63596252/80967927-c606cf00-8e34-11ea-9df3-4e0c339d6d4f.png)



## Commands to be used on MobaXterm.

aws s3 ls *(name of bucket)*



                                
                               
