# Gestion Prix Goncourt (Evaluation métier Python)

#### 1. Objectifs
- Permettre la gestion des livres candidats au Prix Goncourt.
- Suivre les sélections successives (1 ère, 2 ème, finale).
- Gérer les membres du jury et leurs votes (implémentation future).
- Produire une documentation (diagramme de classes, use case, mcd et spécifications fonctionnelles).
- Créer et gérer une base de données en MySQL.
- Implémenter une partie DAO pour gérer les données.
- Produire des résultats fiables (livre gagnant, affichage des votes).

#### 2. Foncionnalités principales
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

#### 3. Technologies utilisées
- Python
- PyMySQL
- MySQl (phpMyAdmin)
- Architecture DAO
- PlantUML
- Looping
- Jupiter
- GitHub

#### 4. Documentation
<img width="1605" height="316" alt="goncourt-use_case" src="https://github.com/user-attachments/assets/71b96e9b-49c0-4358-9e61-fe06587a81ce" />
<img width="436" height="772" alt="goncourt-class" src="https://github.com/user-attachments/assets/66486be9-8f4e-4057-96eb-eb169670aa9d" />
<img width="1587" height="1003" alt="mcd" src="https://github.com/user-attachments/assets/88118a12-3870-4bdd-86ff-441a4df7916c" />


