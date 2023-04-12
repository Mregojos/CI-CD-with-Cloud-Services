# CI/CD with AWS Cloud Services

* Tech Stack: AWS, CodePipeline

## Objective
* Build a CI/CD Pipeline and Deploy an app using AWS Cloud Services

## Architecture
![Architecture](https://github.com/Mregojos/CI-CD-with-Cloud-Services/blob/main/images/Architecture.png)

## Tasks
1. Create and Containerize the App



2. Create a Database on EC2

a. Create a Database using Docker
```sh
# PostgreSQL
docker pull postgres
docker run --name my-postgres -p 5000:5432 -e POSTGRES_USER=matt -e POSTGRES_PASSWORD=password -d postgres

# pgAdmin
docker pull dpage/pgadmin4
docker run --name pgadmin -d -p 8080:80 -e "PGADMIN_DEFAULT_EMAIL=matt@example.com" -e "PGADMIN_DEFAULT_PASSWORD=password" dpage/pgadmin4
```

b. Open pgAdmin
![Database](https://github.com/Mregojos/CI-CD-with-Cloud-Services/blob/main/images/2-a.png)

* Make sure the EC2 Security group has correctly modified.
![](https://github.com/Mregojos/CI-CD-with-Cloud-Services/blob/main/images/2-b.png)

3. Test the app locally
```sh
docker build -t streamlit .
docker run --name streamlit -d -p 8501:80 -v $(pwd):/app streamlit
```

4. Push the image to AWS ECR Repository
```sh
# Create a CodeCommit Repository
aws ecr create-repository --repository-name app

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <AWS ID>.dkr.ecr.us-east-1.amazonaws.com
docker build -t app .
docker tag app:latest <ECR Repo>/app:latest
docker push <ECR Repo>/app:latest

```

5. Create a CodeCommit Repository
![CodeCommit Repository](https://github.com/Mregojos/CI-CD-with-Cloud-Services/blob/main/images/5.png)

6. Create a task definition and AppSec source files

[taksdef.json](https://github.com/Mregojos/CI-CD-with-Cloud-Services/blob/main/code/taskdef.json)

Register this task definition
```sh
aws ecs register-task-definition --cli-input-json file://taskdef.json
```

[appspec.yaml](https://github.com/Mregojos/CI-CD-with-Cloud-Services/blob/main/code/appspec.yaml)

Push taskdef.json and appspec.yaml to CodeCommit Repository
```sh
git clone <CodeCommit https>
cd <repo>
git add -a
git commit -m "task definitions"
git push
```

7. Create Application Load Balancer and Target Groups

![](https://github.com/Mregojos/CI-CD-with-Cloud-Services/blob/main/images/7-a.png)

![](https://github.com/Mregojos/CI-CD-with-Cloud-Services/blob/main/images/7-b.png)

8. Create Amazon ECS Cluster and Service

a. Create Amazon ECS Cluster
![Amazon ECS Cluster](https://github.com/Mregojos/CI-CD-with-Cloud-Services/blob/main/images/8-a.png)

b. Create Amazon ECS Service

[Create Service](https://github.com/Mregojos/CI-CD-with-Cloud-Services/blob/main/code/create-service.json)

```sh
aws ecs create-service --service-name app-service --cli-input-json file://create-service.json
```

9. Create Code Deployment

a. Create a CodeDeploy application
![](https://github.com/Mregojos/CI-CD-with-Cloud-Services/blob/main/images/9-a.png)

b. Create a deployment group
  i. Create IAM for CodeDeploy
  ![](https://github.com/Mregojos/CI-CD-with-Cloud-Services/blob/main/images/9-bi.png)
  
  ii. Create a deployment group
  ![](https://github.com/Mregojos/CI-CD-with-Cloud-Services/blob/main/images/9-bii.png)
  
10. Create the Pipeline and check if the pipeline is working
a. Check the Pipeline
![](https://github.com/Mregojos/CI-CD-with-Cloud-Services/blob/main/images/10-ai.png)
![](https://github.com/Mregojos/CI-CD-with-Cloud-Services/blob/main/images/10-aii.png)















### Reference

* [Task Definition](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-ecs-ecr-codedeploy.html#tutorials-ecs-ecr-codedeploy-taskdefinition)
