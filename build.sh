docker build -t frong-bot .
docker tag frong-bot soulsender/frong-bot:latest
sudo docker push soulsender/frong-bot:latest     