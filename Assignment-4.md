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

- aws s3 ls: *shows the bucket name 
![day4_1](https://user-images.githubusercontent.com/63596252/81147496-0e8acd80-8f98-11ea-8d3a-e91b79801ccc.png)

- ls -r: *shows all folders inside 

![day4_2](https://user-images.githubusercontent.com/63596252/81147499-0f236400-8f98-11ea-8df9-60d8d894d022.png)

- aws s3 ls --recursive:

![day4_3](https://user-images.githubusercontent.com/63596252/81147500-0fbbfa80-8f98-11ea-827a-2382350094c3.png)

- mv source  destination: sends file from one folder to other and deletes at source.

![day4_4](https://user-images.githubusercontent.com/63596252/81147501-0fbbfa80-8f98-11ea-90e5-89b62632c48e.png)

- ls -a : shows all files including hidden(starting with .)

![day4_5](https://user-images.githubusercontent.com/63596252/81147504-10549100-8f98-11ea-9c3f-3cb33e7e3314.png)

- ls -l : shows detailed information of files.

![day4_6](https://user-images.githubusercontent.com/63596252/81147505-10ed2780-8f98-11ea-927d-3cd3926f206f.png)

- history: shows all the commands used till now.

![day4_7](https://user-images.githubusercontent.com/63596252/81147507-10ed2780-8f98-11ea-829e-350a258637fd.png)

- Ctrl+R : search anycommand by using its initials

![day4_8](https://user-images.githubusercontent.com/63596252/81147509-1185be00-8f98-11ea-9e4f-f43f62d05f9b.png)

![day4_9](https://user-images.githubusercontent.com/63596252/81147511-121e5480-8f98-11ea-852b-489195c406a0.png)

- python is inbuilt in linux so we can directly access it 

![day4_10](https://user-images.githubusercontent.com/63596252/81147513-121e5480-8f98-11ea-95df-060b298731a2.png)


and with description of code we can give it like this.

![day4_11](https://user-images.githubusercontent.com/63596252/81147514-12b6eb00-8f98-11ea-932a-43c2399351d9.png)



                                
                               
