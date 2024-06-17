docker run \
  --rm \
  -it \
  -p 2222:22 \
  --detach \
  -v ./data:/data \
  local-ubuntu-image:latest