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
