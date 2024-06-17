docker build . \
  --force-rm \
  --tag local-ubuntu-image:latest \
  --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ')