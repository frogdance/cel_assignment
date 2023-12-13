# CEL interview take home assignment

## Introduction

Welcome to my repo. To run this app successfully, please follow the instruction below.

## Prerequisites

Before you begin, make sure you have the following:

- Docker
- Docker-compose
- Python 3.11
- Jupyter environment to run notebook

All port are mapped to localhost:

- database: `localhost:5432`
- api: `localhost:8000`
- dashboard: `localhost:8501`

## Run app
1. **Step 1: Run app**

   To get started, perform the following actions:

   ```bash
   docker-compose up -d
   ```
   To shutdown app, perform the following actions:

   ```bash
   docker-compose down
   ```
1. **Step 2: Import data**
    *You just need run this on the first time to import data to database.*
    - open file `dataring.ipynb`
    - install `pandas` and `psycopg2`
    - run all cell code in notebook.
