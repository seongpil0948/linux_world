docker build . \
  --force-rm \
  --tag local-ubuntu-image:latest \
  --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') \
  --file /Users/choeseongpil/Code/Project/linux_world/ubuntu/Dockerfile
  # --pull \
  # --no-cache \
  