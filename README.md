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

6. 
