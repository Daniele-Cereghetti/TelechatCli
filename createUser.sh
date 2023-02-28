sudo adduser -quiet --disabled-password --ingroup telechat "$1"
sudo echo 'python3 /TelechatCli/TelechatCli.py' >> /home/$1/.bashrc
sudo echo 'exit' >> /home/$1/.bashrc