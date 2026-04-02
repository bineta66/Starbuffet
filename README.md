# Star Buffet - Documentation du Projet Django

## Étape 1 : Architecture et modélisation

### 1.1 Création du projet et de l'application

* Créer le dossier `Restaurants` sur le bureau.
* Déplacement dans le dossier `Restaurants`.
* Création de l'environnement virtuel et activation :


python -m venv venv
source venv/bin/activate


* Installation de Django :


pip install django


* Création du projet `starbuffet` :

django-admin startproject starbuffet


* Création de l'application `Resto` :

python manage.py startapp Resto


### 1.2 Définir le modèle Traiteur

* Dans `Resto/models.py`, créer une classe `Traiteur` avec les champs :
  `nom_complet`, `adresse`, `est_actif`, `téléphone`, etc.

### 1.3 Ajouter l'application dans `settings.py`

INSTALLED_APPS = [
    'Resto',
]


### 1.4 Créer et appliquer les migrations

* Configurer la base de données MySQL dans `settings.py`.
* Installer MySQL client :


pip install mysqlclient


* Création des migrations :

python manage.py makemigrations


* Application des migrations :


python manage.py migrate


### 1.5 Ajouter le modèle dans l’admin

* Dans `Resto/admin.py`, ajouter le modèle `Traiteur`.
* Créer un super utilisateur :


python manage.py createsuperuser


## Étape 2 : Affichage de la liste des traiteurs (/traiteurs/)

### 2.1 Création de la vue liste traiteur

* Dans `Resto/views.py` : récupérer les traiteurs avec `Traiteur.objects.all()`.
* Affichage via le template `traiteur.html` qui hérite de `base.html`.

### 2.2 Configuration de l'URL

* Dans `Resto/urls.py` : ajout du chemin pour afficher la liste.
* Inclusion des URLs de l'application dans `starbuffet/urls.py`.

## Étape 3 : Détail dynamique (/traiteurs/[int:id](int:id)/detail/)

### 3.1 Création de la vue détail

* Récupération d’un traiteur avec `get_object_or_404(Traiteur, id=id)`.
* Affichage des informations dans `detail.html`.

### 3.2 URL du détail


urlpatterns += [
    path('traiteurs/<int:id>/detail/', views.detail_traiteur, name='detail_traiteur'),
]


## Étape 4 : Authentification & sécurité

### 4.1 Configuration Login / Logout

* Pages : `/login/` et `/logout/`.
* Gestion des sessions utilisateur.
* Protection des vues avec le décorateur `@login_required`.
* Protection CSRF sur les formulaires.
* Validation automatique des données.
* Gestion des erreurs avec `get_object_or_404`.

## Étape 5 : Ajout de Traiteur avec ModelForm

* Création d’un formulaire basé sur le modèle (`ModelForm`).
* Affichage dans un template.
* Validation et enregistrement des données.
* Redirection vers la liste des traiteurs.

### Avantages

* Génération automatique des champs.
* Gain de temps.
* Réduction des erreurs.

## Résultat attendu

L’application permet :

* D’afficher la liste des traiteurs.
* De consulter le détail d’un traiteur.
* De gérer l’authentification.
* D’ajouter des traiteurs de manière sécurisée.

## Structure du projet


starbuffet_project/
│
├── Resto/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       ├── liste.html
│       ├── detail.html
│       ├── login.html
│       └── ajouter.html
│
├── starbuffet_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── manage.py


## Dépendances installées


Django==6.0.3
djangorestframework==3.20.4
mysqlclient==2.3.1
Pillow==10.0.0


## Conclusion

Le projet **Star Buffet** permet de comprendre et maîtriser les bases du framework Django :

* Gestion des données
* Vues dynamiques
* Formulaires
* Sécurité

### Améliorations possibles :

* Système de réservation
* Recherche de traiteurs
* Interface plus avancée (CSS/JS)
* Géolocalisation des prestataires
