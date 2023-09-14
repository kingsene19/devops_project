## DevOps Project DIC2 GIT 2022/2023

In this project we have developed a simple Django application that is deployed using a Continuous Integration/Continuous Deployment (CI/CD) pipeline using Github Actions, Docker and Minikube.

![Image](https://blog.cellenza.com/wp-content/uploads/2021/06/schemas_Plan-de-travail-1.png)

The structure of files in the repo are as follows:
- At its **root** you can find the Django app with the different apps that we have created for each endpoint as well as the files necessary for Docker deployment
- In the **github** folder you can find the YAML configuration file for the Github Actions pipeline
- In the **kubernetes** folder you can find the configuration files for Kubernetes deployment on your local machine using minikube

The project can be broken down into four stages

### Web Application Development

Using Django we have created an application with two endpoints:

- Homepage

![Image](https://i.ibb.co/DkJw89g/test3.png)

- Users

![Image](https://i.ibb.co/3cgGwq9/test.png)

- Visits

![Image](https://i.ibb.co/NrvDwH7/test1.png)

Each endpoint has been unit tested

We use the command `coverage manage.py test` to check them

![Image](https://i.ibb.co/7QYcxb9/test2.png)

### Dockerization

To Dockerize the application we have followed these steps:

- We write a Dockerfile to create a Docker image containing our Django application

- Write docker-compose.yml file

Since our application uses a Postgres database, we also need a service containing the database that the application will connect to.
To do this, we create a docker-compose file that allows us to connect the application to the service easily by putting them in the same network inside a container.

- Modify settings.py

Instead of passing the credentials allowing access to the database manually, we use the methods of the **os** library to access it

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT", 5432),
    }
}
```

- Deploy

To deploy we use `docker compose up` at the root of the project

![Image](https://i.ibb.co/9gK35Yx/test4.png)
![Image](https://i.ibb.co/gFmMcfc/test5.png)

The application is dockerized and the container runs with our Django app and Postgres. We can then access it locally as shown in the screenshots below

![Image](https://i.ibb.co/2gC138F/test6.png)
![Image](https://i.ibb.co/RjMFLGp/test7.png)
![Image](https://i.ibb.co/h98tXDP/test8.png)
![Image](https://i.ibb.co/tPBhNj9/test9.png)

### CI/CD Pipeline Setup

We implement a CI/CD pipeline using Github Actions which will be activated when a push or pull_request is done to the main branch.
We have three jobs:
- **verification** : Install dependencies, verify linting and formating, run tests
- **build-push-image** : Build and push image to dockerhub
- **deploy** : Deploy the application using minikube

As we can see below when we make a push or pull request to the main branch the pipeline activates

![Image](https://i.ibb.co/DM9p963/test10.png)

The jobs then run in sequence when one succeeds the next start thanks to `needs-on` property specified in the pipeline

![Image](https://i.ibb.co/FztynvB/test12.png)

- Verification

![Image](https://i.ibb.co/TPJdHYv/test13.png)
![Image](https://i.ibb.co/0X66XFJ/test14.png)

As we can see everything passes and we can also get information about the coverage on Sonarcloud

- Build Push Image

![Image](https://i.ibb.co/JdY10Cb/test15.png)
![Image](https://i.ibb.co/SwKd3gy/test16.png)

As we can it passes and we can see the image on dockerhub

- Deploy

![Image](https://i.ibb.co/4gL0jwM/test17.png)

As we can the deployment is successful so we will do it locally as well as explain the configurations made in the next part


### Kubernetes Deployment

For the deployment we need to deploy the postgres database as well as the django app

- Postgres

First we create a **secrets.yml** file which contains the information about the database user and password 
Then we create the **volume.yml** and **volume_claim.yml** for the database
We then create the **deployment.yml** file
Finally we create a **service.yml** file

- Django

Here we create the **deployment.yml** file
Then we create the **service.yml** file

- Deployment

We can then deploy our application as follows

![Image](https://i.ibb.co/xqyhw4C/test18.png)

As we can see from the dashboard we now have two pods running for our django and postgres

![Image](https://i.ibb.co/tQHrqJj/test19.png)

To expose the application we use the command

```bash
kubectl port-forward --address 0.0.0.0 services/django-service 8081:80
```

![Image](https://i.ibb.co/ZGsHN0f/test20.png)

As we can see the application is then available locally on port 8081 and it is also possible to access it through a computer on the same LAN by using <host_ip>:8081

**Accès local**

![Image](https://i.ibb.co/FHTfvC0/test21.png)
![Image](https://i.ibb.co/2PyCVXY/test22.png)
![Image](https://i.ibb.co/NLWtRgW/test23.png)

**Accès sur machine connecté au même réseau**

![Image](https://i.ibb.co/Df3vYcq/test24.png)
![Image](https://i.ibb.co/bLK8cNV/Screenshot-2023-09-13-at-23-55-06.png)
![Image](https://i.ibb.co/RTq94WQ/Screenshot-2023-09-13-at-23-55-26.png)
![Image](https://i.ibb.co/P5Sr7zr/Screenshot-2023-09-13-at-23-55-34.png)

