echo In what volume would you like to pull data to?
read -n 5000 volume
echo Please provide the long DVSYNC token
read -n 5000 token
	
export DVSYNC_TOKEN=$token
export TRANSFER_VOLUME=$volume
docker compose -p assist-hub down --remove-orphans
docker compose -p assist-hub -f ./docker-compose.receiver.yml pull
docker compose -p assist-hub -f ./docker-compose.receiver.yml up
docker compose -p assist-hub up -d
