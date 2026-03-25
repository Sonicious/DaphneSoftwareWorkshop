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
   HelloDaphneTable
   ```
   
3. Add:

   * README
   * MIT License
   * If needed: `.gitignore` file

## Clone Repository

```bash
git clone https://github.com/Sonicious/hello-lifecycle.git
cd hello-lifecycle
```

---

# Step 1 — Create Python App

Here, we will use venv and pip

Another Alternative is to use Anaconda. Even mixed forms are possible

## Use environments

use virtual environments or conda environments


## Dependency management

**`requirements.txt`**

```
flask
pytest
```

Install locally (optional):

```bash
pip install -r requirements.txt
```

## Develop Software

On Mac using Port 5000 might cause a conflict with the Airplay receiver. Choose another Port or disable AirPlay Receiver in Settings

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

---

# Step 3 — Test

## Test environments

Testing environments blabla

## `test_app.py`

```python
from app import app

def test_hello():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

```

Run:

```bash
pytest
```

---

# Step 4 — Metadata and publishing

## Publishing with Github Zenodo Integration

- Combination allows to create automated Zenodo publishing with each release
- Citation file and release creation allows Zotero plugin to properly read metadata

## citation file

Github is able to use several citation file formats. The most common is cff

**`CITATION.cff`**

```yaml
cff-version: 1.2.0
message: "If you use this software, please cite it as below."
authors:
- family-names: "Lisa"
  given-names: "Mona"
  orcid: "https://orcid.org/0000-0000-0000-0000"
- family-names: "Angelo"
  given-names: "Miche"
  orcid: "https://orcid.org/0000-0000-0000-0000"
title: "Awesome DAPHNE Software"
version: 2.0
date-released: 2026-03-18
url: "https://github.com/github-linguist/linguist"
```

---

# Step 5 — bring softwrae to the repo

## git workflow in general

In general you should always work with
- create issue
- create branch
- create pull request
- review code (4 eyes principle)
- merge
- if necessary: tag or create release

Have in mind: "Quick and dirty is the way to endless suffering"

The Github/Gitlab is your central place of software knowledge. Also for software project management, your door to colaboration and interaction with users.

## let's commit and push

```bash
git add .
git commit -m "Add app, test, metadata"
git push
```

## [optional] let's tag and push
```bash
git tag -a 0.5 -m "This is our first release tag"
git push --tags
```

---

# Step 6 - Use git for publishing

- go to your zenodo account, integrate github
- activate automated publishing
- go to github
- create a release
- enjoy your automatic publication and fresh DOI

---

# Step 7 - Docker (Core)

## What is Docker

-  principles of Containerisation

## Create your first Dockerfile

**`Dockerfile`**

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

## Build your Docker Container

```bash
docker build -t hello-daphne .
```

## Run your Docker Container

```bash
docker run -p 5000:5000 daphne-workshop
```

---

# Step 8a — GitHub Actions / GitLab CI

## What is continious integration?

- Continious integration are processes which are started automatically after git action
- Classic examples:
  - Test on each push
  - create DOXYGEN on each push to main
  - create Docker Containers and push to registry
  - submit a slurm job during push to special hpc branch

## Examples in Github

GitLab is equivalent with other wordings and syntax:

* `.gitlab-ci.yml`
* built-in container registry
* pipelines by default

## Automated Testing (CI)

GitHub Actions example:

`.github/workflows/testing.yml`

```yaml
name: Test

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v6
      - run: pip install -r requirements.txt
      - run: pytest
```

---

# Step 9b — NGINX Reverse Proxy

## Reverse Proxy

## NGINX Config file

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

```bash
docker network create daphnenet
```

```bash
docker run -d --name app --network daphnenet daphne-workshop
```

```bash
docker run -d \
  --name nginx \
  --network daphnenet \
  -p 8080:80 \
  -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro \
  nginx
```

## Test

[http://localhost:8080](http://localhost:8080)

# Further topics

* Git signatures and vigilant mode for more trust
* docker-compose, kubernetes
* Working with Github Container Registry
* Github Repo Templates
* Github Docs