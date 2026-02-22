# Gestion Prix Goncourt (Evaluation métier Python)

## Sommaire
- [Objectifs](#objectifs)
- [Fonctionnalités](#fonctionnalités-principales)
- [Technologies Utilisées](#technologies-utilisées)
- [Installation](#installation)
- [Mise en place de la base de données](#mise-en-place-de-la-base-de-données)

### Objectifs
- Permettre la gestion des livres candidats au Prix Goncourt
- Suivre les sélections successives (1 ère, 2 ème, finale)
- Gérer les membres du jury et leurs votes (implémentation future)
- Produire une documentation (diagramme de classes, use case, mcd et spécifications fonctionnelles)
- Créer et gérer une base de données en MySQL
- Implémenter une partie DAO pour gérer les données
- Produire des résultats fiables (livre gagnant, affichage des votes)

### Fonctionnalités principales
- choix d'un rôle (Utilisateur, Membre du jury ou Président)
- Affichage des livres dans la sélection actuel 
- Gestion des sélections (par le Président uniquement)
- Votes des jurées (simulé avec des insert dans la BDD pour le moment)
- Affichage des votes (Fonctionnalité du Président)
- Passage à la sélection suivante (Gérer par le Président)
- Suppression automatique des votes entre chaques sélections
- Mise à jour automatique de la liste des livres dans la sélection (en fonction des votes)
- Détermination du gagnant à la fin (livre avec le plus de votes)
- Gestion de base de donnée en MySQL

### Technologies utilisées
- Python
- PyMySQL
- MySQl (phpMyAdmin)
- Architecture DAO
- PlantUML
- Looping
- Jupiter
- GitHub

### Installation

```bash
https://github.com/john7440/Evaluation-Metier-Python.git
cd Evaluation-Metier-Python
```
### Ouvrir dans PyCharm
Fichier -> Ouvrir -> Sélectionner le dossier du Projet

### Mise en place de la Base de données

#### Option 1: En utilisant un client MySQL
1. Ouvrir le client MySQL/MariaDB
2. Copier et coller le contenu de `bdd/goncourt.sql`
3. Exécuter le Script

#### Option 2: En ligne de commande
```bash
mysql -u root -p < bdd/goncourt.sql
```

