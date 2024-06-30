# create network if not exists
if [ ! "$(docker network ls | grep local-linux-network)" ]; then
  docker network create local-linux-network
fi

if [ ! "$(docker network ls | grep jenkins)" ]; then
  docker network create jenkins
fi