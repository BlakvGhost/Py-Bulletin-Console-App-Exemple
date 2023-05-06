# Py-Bulletin-Console-App-Exemple

Py-Bulletin-Console-App-Exemple est une application console qui permet de créer des bulletins. Les bulletins créés sont stockés dans un fichier texte et peuvent être consultés ultérieurement.

## Installation

- Cloner le repository:

    ```bash
    git clone https://github.com/blakvghost/Py-Bulletin-Console-App-Exemple.git
    ```

- Créer un environnement virtuel Python avec `python -m venv env`
- Activer l'environnement virtuel avec `source env/bin/activate` (pour Linux/MacOS) ou
   `.\env\Scripts\activate` (pour Windows)
- Installer les dépendances avec `pip install -r requirements.txt`

## Utilisation

Pour lancer l'application, exécuter la commande suivante :

```py
python main.py
```

L'application affichera un menu permettant de créer un nouveau bulletin ou de consulter les bulletins existants.

## Architecture du projet

Le projet est composé des fichiers suivants :

- main.py : le point d'entrée de l'application
- bulletin.py : le module qui contient la classe Bulletin qui permet de créer et de consulter des bulletins
- bulletins.txt : le fichier texte qui contient les bulletins enregistrés

## Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à proposer une pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.

![Screenshot](Capture.png)
