# Workshop Software Lifecycle in a nutshell

This workshop was held during the DAPHNE4NFDI Annual Meeting 2026

Date: March 25th, 2026

[![DOI](https://zenodo.org/badge/1191456170.svg)](https://zenodo.org/badge/latestdoi/1191456170)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Test](https://github.com/Sonicious/DaphneSoftwareWorkshop/actions/workflows/testing.yml/badge.svg)](https://github.com/Sonicious/DaphneSoftwareWorkshop/actions/workflows/testing.yml)
[![Docker Build test](https://github.com/Sonicious/DaphneSoftwareWorkshop/actions/workflows/dockertest.yml/badge.svg)](https://github.com/Sonicious/DaphneSoftwareWorkshop/actions/workflows/dockertest.yml)
# Step 0 — Start on Github

## Create Repo

1. Go to **GitHub**
2. Create new repository:

   ```
	DaphneWorkshop
   ```
   
3. Add:

   * README
   * MIT License
   * If needed: `.gitignore` file

## Clone Repository

```bash
git clone https://github.com/{YourGithubHandle}/DaphneWorkshop.git
cd DaphneWorkshop
```

---

# Step 1 — Create Python App

The first step is to create our little python app which is the example of Research software. We will have a simple Hello World example to concentrate on the workflows.

We will use the combination **venv + pip** in our example since it's really simple

## Use environments

- Use environments to keep your system python clean
- Recommendations: venv or conda
- venv is very lightweight while conda is bigger
- both have advantages and disadvantages

```bash
python -m venv venv                # create a local virtual environment
venv\Scripts\activate              # Windows
source myfirstproject/bin/activate # Linux/Mac
```

- you should see your venv in the commandline
- use `deactivate` to leave the environment again

## Dependency management

Manage your dependencies in pip or conda.

**`requirements.txt`**

```
flask
pytest
```

Install locally:

```bash
pip install -r requirements.txt
```

## Develop Software

Now we develop research software. In our example we will keep it simple and just use a little web app which gives us a nice answer.

**`app.py`**

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    str = "<h1>Daphne4NFDI</h1><p>Here is a service or software output</p>"
    return str
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

```

You can simply run your web application with `python app.py`

On Mac using Port 5000 might cause a conflict with the Airplay receiver. Choose another Port or disable AirPlay Receiver in Settings

---

# Step 3 — Test

This part is all about testing software.

## Test environments

- Nowadays nowbody writes test functions, but uses test kits or testing frameworks
- classic python testing framework: pytest
- There is even "Test driven development" as a form of software engineering
- A really good core functionality of AI bots is test writing

## test file

We create a file with prefix `test_*.py` or suffix `*_test.py`. There, functions `test_*` and classes with `Test*` are run by **pytest**

**`test_app.py`**

```python
from app import app

def test_hello():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    
```

Errors (typically by assertion commands) are caught and shown in the test environment.

Run:

```bash
pytest
```

All test should run nicely.

---

# Step 4 — Metadata and publishing

## Publishing with Github Zenodo Integration

- Combination allows to create automated Zenodo publishing with each release
- Citation file and release creation allows Zotero plugin to properly read metadata
- Sign in at Zenodo
- go to [Zenodod Github Integration](https://zenodo.org/account/settings/github/)
- resync your github repositories
- enable publishing on your `DaphneWorkshop` repository
- Now Zenodo publishes your new releases of Github automatically on your Zenodo account and puts a DOI on it

## Citation file

Github is able to use several citation file formats. The most common is cff. The message is printed at Zenodo as a Note

**`CITATION.cff`**

```yaml
cff-version: 1.2.0
message: "This message is a note on Zenodo"
authors:
- family-names: "Lisa"
  given-names: "Mona"
  orcid: "https://orcid.org/0000-0000-0000-0000"
- family-names: "Angelo"
  given-names: "Miche"
  orcid: "https://orcid.org/0000-0000-0000-0000"
title: "Awesome DAPHNE Software"
version: 2.0
date-released: 2026-03-25
url: "https://github.com/{YourGithubHandle}/DaphneWorkshop"
```

---

# Step 5 — bring software to the repo

## git workflow in general

In general you should always work with classic git workflows which include:
- issues
- Pull request
- branching
- team reviews

Don't be afraif of project/software management. 
> "Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering." (Quote by Yoda, Star Wars)

The Github/Gitlab is your central place of software knowledge. Also for software project management, your door to collaboration and interaction with users. Make use of it. And stay transparent.

**Warning: Never push secrets to git. Even after changes, it's out there in the internet!**

## Let's commit and push

Do not overly bundle your commits. Each semantic change is a single commit. Add a WIP when you are not finished. Do not work in main.

```bash
git add .
git commit -m "Add app, test, metadata"
git push
```

## [optional] Let's tag and push

You can tag some of your commits, if they are important. But you can also properly tag in Github or Gitlab

```bash
git tag -a 0.5 -m "This is our first release tag"
git push --tags
```

---

# Step 6 - Use git for publishing

- Create a release in Github
- enjoy your automatic publication and fresh DOI of your software

---

# Step 7 - Docker (Core)

## What is Docker

-  Docker is a kind of leightweight virtual machine
-  It bundles software and data into one piece.
-  You can run software inside in sandboxed environments
-  Docker makes software sustainable, even if software outdates or is undergoing key changes in development

## Create your first Dockerfile

Create the following file in your directory

**`Dockerfile`**

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

This is a Dockerfile. It is the blueprint of a Container.

## Build your Docker Container

Now we want to build a container from the blueprint:

```bash
docker build -t hello-daphne .
```

Now you have a Container which you can run.

## Run your Docker Container

Since the container is completely sandboxed, you need to establish information flow through ports to see the results. Port 5000 should be opened to the outside of the local host as port 5000.

```bash
docker run -p 5000:5000 daphne-workshop
```

your container is running now and you can check if everything works if you visit [localhost:5000](localhost:5000)

The Docker Desktop app helps you to manage your containers, images and much more.

---

# Step 8a — GitHub Actions / GitLab CI

## What is continious integration?

- Continious integration are processes which are started automatically
- Classic examples:
  - Test on each push
  - create DOXYGEN on each push to main
  - create Docker Containers and push to registry
  - submit a slurm job during push to special hpc branch

Github actions are based on YAML files which are saved in `.github/workflows/`

GitLab is equivalent with other wordings and syntax:

* `.gitlab-ci.yml`
* built-in container registry
* pipelines by default

## Example: Automated Testing (CI)

GitHub Actions example for testing with **pytest*:

`.github/workflows/testing.yml`

```yaml
name: Test

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v6
      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: '3.x'
          cache: 'pip' # caching pip dependencies
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Test with pytest
        run: pytest
```

Github action which creates and tests your Docker image:

`.github/workflows/dockertest.yml`

```yaml
name: Docker Build test

on:
  push:
    branches: [ "main" ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v6
    - name: Build the Docker image
      run: docker build . --file Dockerfile --tag daphne-workshop
    - name: Run container test
      run: |
        docker run -d -p 5000:5000 --name app daphne-workshop
        sleep 3
        curl -f http://localhost:5000

```

Now you can check your test results after each push into your repo. A fresh Docker build is tested after each push into production

---

# Step 8b — NGINX Reverse Proxy

To test a real Docker situation, let's add a Reverse Proxy in front of the Python application.

## Reverse Proxy

A reverse proxy is a professional webserver which acts as a dealer for incoming requests and also handles security, load balancing, trust, Caching and domain/subdomain situations.

## NGINX Config file

NGINX is a professional webserver used by many companies and also research institutes. It's a good alternative to Apache. Lightweight, fast and super versatile. It just uses a single config file for our approach.

**`nginx.conf`**

```nginx
events {}

http {
    server {
        listen 80;

        location / {
            proxy_pass http://app:5000;
        }
    }
}
```

## Docker Network + Containers

Now we need to create a network, where the docker containers see each other and can communicate to each other without destroying the sandbox idea of docker. Therefore we create a sandbox network.

```bash
docker network create daphnenet
```

Now we run our WebApp container in this container network

```bash
docker run -d --name app --network daphnenet daphne-workshop
```

Last but not least we use the following command to run a NGINX container with the config file. 

```bash
docker run -d \
  --name nginx \
  --network daphnenet \
  -p 8080:80 \
  -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro \
  nginx
```

## Test

Now we can test our setup properly. 

[http://localhost:8080](http://localhost:8080)

# Further topics

* Git signatures and vigilant mode for more trust
* docker-compose, kubernetes
* Working with Container Registries
* Github Repo Templates
* Github Docs