#!/bin/bash

echo "JUDO -- Jailed User Do install -xaled@maCERT"

if [ "$(id -u)" == "0" ]; then
   echo "Lancer ce script avec un utilisateur normal"
   exit 1
fi

#echo "compiling files..."
#gcc -c ju_useradd.c
#gcc -c ju_userdel.c
#gcc -c ju_usermod.c
#gcc ju_useradd.o -o ju_useradd
#gcc ju_usermod.o -o ju_usermod
#gcc ju_userdel.o -o ju_userdel
#rm *.o


echo "copying binaries to /usr/bin/.."
#sudo cp ju_useradd ju_userdel ju_usermod /usr/bin/
sudo chmod +x ju_user*.py
sudo cp ju_useradd.py /usr/bin/ju_useradd
sudo cp ju_usermod.py /usr/bin/ju_usermod
sudo cp ju_userdel.py /usr/bin/ju_userdel
sudo cp juser.py /usr/bin/judo
sudo cp *.sh /usr/bin/


echo "install work dir.."
cp -R judo/ ~/.judo

echo "configuring sudo.."
sudo bash -c "cat sudoers >> /etc/sudoers"

echo "creating groups.."
sudo groupadd judo
sudo groupadd judog

echo "chowning Xauthority"
sudo chown :judog ~/.Xauthority
sudo chmod 640 ~/.Xauthority
