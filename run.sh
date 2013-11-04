#!/bin/sh

set -ex
VERSION=$1
IMAGE=libxml:$VERSION

cd libxml$VERSION
docker build -t $IMAGE .
docker run -v $(pwd)/..:/work -w /work $IMAGE python test.py
