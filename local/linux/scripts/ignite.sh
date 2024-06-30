docker-compose up \
  --remove-orphans \
  --detach \
  --build 
sh scripts/clear-known-hosts.sh
# docker-compose up  --remove-orphans
# docker run \
#   --rm \
#   -it \
#   -p 2222:22 \
#   --detach \
#   -v ./data:/data \
#   local-ubuntu-image:latest
# docker run \
#   --rm \
#   -it \
#   -p 2223:22 \
#   --detach \
#   -v ./data:/data \
#   local-ubuntu-image-2:latest