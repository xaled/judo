# judo
Jailed user do (judo), run a command in a anprivilged sandbox


## Usage

> $ judo [-u] profile command

-u to update profile directory after exiting


### Example:

> $ judo perso firefox

The script create a random user, then copy the home directory of the profile "perso" to a temp directory, finally it executes the command under the new uid.


## Install & uninstall

> $ ./install.sh

> $ ./uninstall.sh

 
## Configuration
 ~/.judo/profiles/profilename.json

###example:

{
   "randomuid": true,
   "alwaysupdate": false,
   "graphic": true,  --> accès à l'affichage graphique
   "home_dirs": [
      "Downloads"
   ],
   "name": "public",
   "download_dir": "Downloads", --> dossier des téléchargements
   "default_update": [".mozilla/firefox/9z58ish0.default/places.sqlite"],  --> fichier/dossier à mettre à jour (dans ce cas historique de la navigation)
   "audio": true --> accès à la carte son
}

 

tested in ubuntu.
