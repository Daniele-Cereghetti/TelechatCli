# TelechatCli

## About that project
That program hat the goal to create a very simple chat in CLI.
This program will be implemented with SSH, this protocol will play the role of authentication and connection encryption.  You have the program run on the remote server (taking advantage of ssh's option to connect and run one command), and after that you are ready to use the chat (the user will have to be created on the server).

## System requirements
The software is meant to run on an Ubuntu environment. The version used was 22.04.2

## Installing
Initially you have to install the dependencies and the program, I created a script that does both of the above actions: run the script with the following command.:
```
./install.sh
```

If it doesn't work give execution permissions first
```
sudo chmod +x install.sh
```
## SSH configuration
If you want to configure ssh server with a key-only login, you can follow [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server).

## Add a user
Create the user on the server
```
sudo adduser --disabled-password --ingroup telechat username
```

Create the key on the client
```
ssh-keygen
```

Copy the public key on the server
```
ssh-copy-id username@remote_host
```

## Connection to the application
For the final user, must to execute that comand for using the chat
```
ssh user@remote_host "python3 /TelegramCli/TelegramCli.py"
```
