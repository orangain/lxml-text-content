#!/bin/sh

set -ex
IMAGE=$1

cd $IMAGE
docker build -t lxml-text-content:$IMAGE .
docker run -v $(pwd)/..:/work -w /work lxml-text-content:$IMAGE /bin/sh -ex run_test_in_docker.sh
