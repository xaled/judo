#!/bin/bash

echo "JUDO -- Jailed User Do Uninstall -xaled@maCERT"

if [ "$(id -u)" == "0" ]; then
   echo "Lancer ce script avec un utilisateur normal"
   exit 1
fi


echo "deleting binaries from /usr/bin/.."
sudo rm /usr/bin/judo /usr/bin/juser_removewp.sh /usr/bin/juser_initwp.sh /usr/bin/ju_useradd /usr/bin/ju_usermod /usr/bin/ju_userdel


echo "deleting work dir.."
rm -R ~/.judo

echo "deleting sudo.."
sudo bash -c "cat /etc/sudoers | grep -v  JUDO_ > /etc/sudoers.bkp"
sudo cp -f /etc/sudoers.bkp  /etc/sudoers
sudo rm /etc/sudoers.bkp

echo "chowning Xauthority"
sudo chown $USER:$USER ~/.Xauthority
chmod 600 ~/.Xauthority

echo "deleting groups.."
sudo groupdel judo
sudo groupdel judog


