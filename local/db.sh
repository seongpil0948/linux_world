docker run \
  --rm \
  -p 8084:5432 \
  --name pgdata_lhs_unsafety \
  -e POSTGRES_PASSWORD=Intellisys123! \
  -d \
  -v pgdata_lhs_unsafety:/var/lib/postgresql/data \
  postgres:12 