docker build . \
  --file Dockerfile.ubuntu \
  --force-rm \
  --tag local-ubuntu-image-1:latest \
  --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ')

docker build . \
  --file Dockerfile.ubuntu \
  --force-rm \
  --tag local-ubuntu-image-2:latest \
  --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ')
docker build . \
  --file Dockerfile.centos \
  --force-rm \
  --tag local-centos-image-1:latest \
  --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ')