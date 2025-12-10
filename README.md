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


