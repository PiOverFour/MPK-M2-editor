MPK M2-editor
=============
Une alternative à l’éditeur officiel AKAI MPKMini MkII

![Fenêtre de l’éditeur](editor_screenshot.png?raw=true "L’éditeur")

## Résumé
Ce programme remplace l’éditeur officiel AKAI MPKMini MkII. Il est
moins stylé, mais tout aussi utilisable.

## Configuration système
Ce programme est écrit en Python3 et s’appuie sur PyQt5 et
python-rtmidi. Il a été testé sous GNU/Linux, Mac OS X et Windows.

## Installation
Une bonne manière d’installer les dépendances peut être d’utiliser pip.
### Distributions fondées sur Debian
```
  apt-get install build-essential python3-dev python3-pip libasound2-dev libjack-dev
  pip3 install -r requirements.txt
```

### Mac OS X
On peut installer Python et pip avec homebrew. Vous aurez peut-être
besoin d’une version récente de Mac OS X.
```
  brew install python3
  pip3 install -r requirements.txt
```

### Windows
* Télécharger et installer `python3` sur [le site de
  Python](https://www.python.org/downloads/windows/). Dans l’interface
  d’installation, assurez-vous d’installer également `pip`
* Télécharger et install [Visual C++ build tools 2015](http://landinghub.visualstudio.com/visual-cpp-build-tools)
* Dans une invite de commande, taper :
```
  pip3 install -r requirements.txt
```

## Usage
Connectez votre contrôleur, puis démarrez l’aditeur avec
```./mpk-m2-editor.py```.

Si vous connaissez déjà l’éditeur officiel, vous verrez que c’est
similaire, à part que les programmes sont groupés par onglets en haut
de la fenêtre. Vous pouvez envoyer un programme individuel, ou tous à
la fois. Certains champs ont des infobulles, ne pas hésiter à passer
la souris dessus pour plus d’informations.

Vous pouvez utiliser la molette pour changer n’importe quelle valeur.
En maintenant `CTRL`, les valeurs changent par incréments de 10.

Le bouton Envoyer RAM (Send RAM) permet d’envoyer la configuration
actuelle au contrôleur, sans effacer aucun programme.

### Joystick
Les options du joystick fonctionnent de la manière suivante :
* D’abord, sélectionner le comportement de base : **Pitchbend**, **CC1** ou **CC2**.
* **Pitchbend** : c’est tout.
* **CC1** : Le joystick envoie un message CC sur le canal spécifié
  dans le champ **Left** pour l’axe X, **Up** pour l’axe Y.
* **CC2** : Le joystick envoie un message CC sur les canaux spécifiés
  dans les champs **Left** OU **Right** pour l’axe X, **Up** OU
  **Down** pour l’axe Y.

### Remplissage automatique
Cliquer sur le menu Édition -> Remplissage automatique… Ce dialogue
permet de remplir plusieurs champs d’un coup. Cocher d’abord les
options que vous voulez remplir (par ex. PC start). Remplir les champs
correspondans, et cliquer sur le bouton correspondant à la destination
souhaitée (par ex. A pour la banque A). Les options seront seulement
remplies pour l’onglet sélectionné.

![Fenêtre de remplissage automatique](autofill_screenshot.png?raw=true
"La fenêtre de remplissage automatique")

## Retours et _pull requests_ bienvenues !
C’est un bon point de départ, mais n’hésitez pas à contribuer !

## Licence

> Copyright (C) 2017-2020 Damien Picard dam.pic AT free.fr et
> contributeurs
>
> This program is free software: you can redistribute it and/or modify
> it under the terms of the GNU General Public License as published by
> the Free Software Foundation, either version 3 of the License, or
> (at your option) any later version.
>
> This program is distributed in the hope that it will be useful,
> but WITHOUT ANY WARRANTY; without even the implied warranty of
> MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
> GNU General Public License for more details.
>
> You should have received a copy of the GNU General Public License
> along with this program. If not, see <http://www.gnu.org/licenses/>.
