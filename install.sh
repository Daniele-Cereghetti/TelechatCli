#installazione dipendenze
sudo apt update
sudo apt install -y libncurses-dev
sudo apt install -y python3 python3-pip

#creazione gruppo app
sudo addgroup telechat

#creazione cartella app con relativi permessi
git clone https://github.com/Daniele-Cereghetti/TelechatCli.git
sudo mv TelechatCli /
sudo chmod -R 770 /TelechatCli
sudo chown -R user:telechat /TelechatCli
