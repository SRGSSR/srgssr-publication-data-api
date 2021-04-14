#!/usr/bin/env bash
set -e

if [ "$1" == "" ]; then
    echo "Must provide tag as first parameter!"
    exit 1
fi

aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 224863817770.dkr.ecr.eu-central-1.amazonaws.com
docker build -t jupyter:$1 --build-arg api_version=$2 .
docker tag jupyter:$1 224863817770.dkr.ecr.eu-central-1.amazonaws.com/jupyter:$1
docker push 224863817770.dkr.ecr.eu-central-1.amazonaws.com/jupyter:$1
