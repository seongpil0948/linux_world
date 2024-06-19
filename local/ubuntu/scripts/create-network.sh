# create network if not exists
if [ ! "$(docker network ls | grep my-network)" ]; then
  docker network create my-network
fi

if [ ! "$(docker network ls | grep jenkins)" ]; then
  docker network create jenkins
fi