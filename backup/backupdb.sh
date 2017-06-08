while true; do
    if [ -e /backups/dump.db ]; then
        mv /backups/dump.db /backups/dump.db.bak
    fi
    pg_dump > /backups/dump.db
    sleep 24
done