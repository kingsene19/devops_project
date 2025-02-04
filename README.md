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
- Users
- Visits

Each endpoint has been unit tested

We use the command `coverage manage.py test` to check them

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

To deploy we use `docker compose up` at the root of the project. The application is dockerized and the container runs with our Django app and Postgres. We can then access it locally.

### CI/CD Pipeline Setup

We implement a CI/CD pipeline using Github Actions which will be activated when a push or pull_request is done to the main branch.
We have three jobs:
- **verification** : Install dependencies, verify linting and formating, run tests
- **build-push-image** : Build and push image to dockerhub
- **deploy** : Deploy the application using minikube

When we make a push or pull request to the main branch the pipeline activates, the jobs then run in sequence when one succeeds the next start thanks to `needs-on` property specified in the pipeline

- Verification
- Build Push Image
- Deploy

Once the deployment is successful so we will do it locally as well as explain the configurations made in the next part

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

We can then deploy our application and to expose the application on the network interface we use the command

```bash
kubectl port-forward --address 0.0.0.0 services/django-service 8081:80
```

The application is then available locally on port 8081 and it is also possible to access it through a computer on the same LAN by using <host_ip>:8081
