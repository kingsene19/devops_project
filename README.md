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
