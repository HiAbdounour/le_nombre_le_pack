# Le Nombre (Le Pack)
## Présentation du jeu
Le Nombre est un jeu de devinette simpliste.

Le but du jeu est de trouver un nombre choisi aléatoirement. Le joueur a le choix entre des nombres de 1, 2, 3 ou 4 chiffres. Le joueur dispose d'un nombre illimité* d'essais pour trouver le nombre caché.\
À chaque essai, le nombre renseigné par le joueur s'affiche dans une liste d'essais avec une certaine couleur :
- rouge si le nombre renseigné est strictement plus petit que le nombre caché
- bleu si le nombre renseigné est strictement plus grand que le nombre caché
- vert si le nombre a été trouvé

La partie se termine lorsque le joueur a trouvé le nombre caché. Ensuite, elle ramène au menu du jeu.

*\*En théorie, les essais sont illimités. En pratique, la liste des nombres essayés devient si grande qu'elle dépasse la taille de la fenêtre graphique. À partir de ce moment, il devient difficile de trouver le nombre caché.*

## Comment jouer ? 
Ce jeu est (pour le moment) disponible uniquement sous forme Python : il est nécessaire de télécharger le code source pour pouvoir y jouer. \
Version PC uniquement.\
Deux moyens existent pour télécharger le code source.

### Depuis la Release GitHub

Rendez-vous dans la section  [Releases](https://github.com/HiAbdounour/le_nombre_le_pack/releases)  et sélectionnez la version qui vous intéresse (la première est la plus récente).\ 
Après un message descriptif de la Release, vous trouverez un dossier .zip et un dossier .rar contenant tous les fichiers du repo. Il vous suffit de télécharger l'un des dossiers, de le dézipper puis de lancer le fichier main.py (depuis un IDE ou depuis le terminal en tapant ``python main.py``).

### Depuis le terminal

Ouvrez le terminal et déplacez-vous dans le dossier où vous souhaitez télécharger le code source.\
Ensuite, tapez :
```
    git clone https://github.com/HiAbdounour/le_nombre_le_pack
```
Cette instruction va directement télécharger le code source sur votre machine.\
Pour lancer le jeu, il suffit de taper
```
	python main.py
```

### Prérequis

Python version 3.12 ou ultérieure \
pygame version 2.6.1 ou ultérieure

## Sources

Le Nombre est une version revisitée du Jeu du Juste Prix.\
La génération aléatoire du nombre est gérée par le module ``random``  de Python.
