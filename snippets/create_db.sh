DB_NAME=tiffest
DB_PASSWORD=12345
DB_USER=tiffest_user
DB_HOST=localhost
DB_PORT=5432

mkdir -p db_backups

DB_DUMP="db_backups/${DB_NAME}_$(date +'%Y-%m-%d-%H-%M').sql"

pg_dump --no-privileges --no-owner -f $DB_DUMP --dbname=postgres://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}
