# Mémo - Apprentissage par Renforcement

## 1. Introduction

### Définition
L'apprentissage par renforcement vise à enseigner à un agent à prendre des décisions dans un environnement incertain en utilisant des récompenses.

### Applications
- Algorithmes de trading
- Robotique autonome
- Systèmes de recommandation

## 2. Concepts clés

### Agent et Environnement
- **Agent :** Prend des actions.
- **Environnement :** Fournit des états, récompenses, et évolue selon les actions.

### Récompenses
- **Récompense :** Signal numérique indiquant la qualité d'une action dans un état.

### Politique
- **Politique (π) :** Stratégie de l'agent, déterminant quelle action prendre dans chaque état.

## 3. Processus de Décision de Markov (MDP)

### MDP
- **MDP :** Modèle mathématique pour un processus de décision séquentiel.

### Formule de Bellman
\[ Q(s, a) = R(s, a) + \gamma \max_{a'} Q(s', a') \]

- \( Q(s, a) \) : Valeur de l'action \( a \) dans l'état \( s \).
- \( R(s, a) \) : Récompense immédiate pour l'action \( a \) dans l'état \( s \).
- \( \gamma \) : Facteur d'actualisation.
- \( s' \) : Prochain état.

## 4. Q-Learning

### Q-Table
- **Q-Table :** Tableau représentant les valeurs \( Q \) pour chaque paire état-action.

### Algorithme Q-Learning
\[ Q(s, a) \leftarrow (1 - \alpha)Q(s, a) + \alpha [R(s, a) + \gamma \max_{a'} Q(s', a')] \]

- \( \alpha \) : Taux d'apprentissage.

## 5. Exercices

### Exercice 1
1. Exécutez le code "FrozenLake" fourni.
2. Testez le comportement sur une case en essayant d'aller dans une direction spécifique.
3. Codez un scénario gagnant et un scénario perdant.

### Exercice 3
Calculez en Python la récompense cumulative pour différents scénarios.

### Exercice 5
Implémentez le Q-learning dans le script fourni (Ex5Caneva.py) avec la formule de mise à jour.
