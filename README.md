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

![Image](https://i.ibb.co/f2GYTQY/test.png)

- Users

![Image](https://i.ibb.co/3cgGwq9/test.png)

- Visits

![Image](https://i.ibb.co/NrvDwH7/test1.png)

Each endpoint has been unit tested

We use the command `coverage manage.py test` to check them

![Image](https://i.ibb.co/7QYcxb9/test2.png)