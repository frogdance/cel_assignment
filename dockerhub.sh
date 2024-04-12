#!/bin/sh
docker login
# build and push image dashboard
cd dashboard
docker build -t frogdance/cel-intelligence:lastest .
docker push frogdance/cel-intelligence:lastest
cd ..
# build and push image api
cd api
docker build -t frogdance/cel-api:lastest .
docker push frogdance/cel-api:lastest
cd ..
# build and push image database
cd database
docker build -t frogdance/cel-db:lastest .
docker push frogdance/cel-db:lastest
cd ..