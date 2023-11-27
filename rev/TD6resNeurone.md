# Mémo - Apprentissage Profond avec PyTorch

## Partie 1: Les réseaux de neurones

### Fondamentaux des réseaux de neurones

#### Neurone Artificiel
- Un neurone artificiel reçoit des entrées pondérées, applique une fonction d'activation, et produit une sortie.
- La fonction d'activation introduit une non-linéarité, permettant au réseau de modéliser des relations complexes.

#### Fonctionnement du réseau
- Propagation avant (forward): Les données passent à travers le réseau de la couche d'entrée à la couche de sortie.
- Rétropropagation (backward): Les gradients sont calculés par rapport à l'erreur, et les poids sont ajustés pour minimiser l'erreur.

### Un premier réseau de neurones simple

#### Descente de gradient
- La descente de gradient est utilisée pour minimiser la fonction de perte en ajustant les poids du réseau.
- Taux d'apprentissage: Il contrôle la taille des pas dans la direction opposée au gradient. Trop petit peut ralentir la convergence, trop grand peut provoquer une divergence.

#### Mini-batch
- L'entraînement sur des mini-lots (mini-batch) accélère le processus d'optimisation tout en évitant le surajustement.

## Partie 2: Perceptron Multi-Couches (PMC)

### Architecture des PMC
- Les PMC sont composés de plusieurs couches de neurones (entrée, cachée, sortie).
- Chaque connexion entre les neurones a un poids associé.

### Apprentissage avec PyTorch

#### Tenseurs
- Les tenseurs sont la structure de données fondamentale en PyTorch.
- Ils peuvent être scalaires, vecteurs, matrices, etc.

#### Module `torch.nn`
- Ce module fournit les éléments de base pour construire des modèles en PyTorch.
- `nn.Module`: Classe de base pour tous les modules PyTorch.
- `nn.Linear`: Couche linéaire pour les transformations linéaires (équivalent d'une couche dense).

#### Fonction d'activation
- La fonction d'activation introduit une non-linéarité dans le réseau. Exemples: ReLU, Sigmoid, Tanh.

### Prise en main de PyTorch

#### Création d'un modèle
- Définir une classe héritant de `nn.Module`.
- Définir les couches du modèle dans la méthode `__init__`.
- Implémenter la propagation avant dans la méthode `forward`.

#### Entraînement du modèle
- Initialiser un optimiseur (ex: `torch.optim.SGD`).
- Définir une fonction de perte (ex: MSE pour la régression).
- Boucle d'entraînement: Propagation avant, calcul de la perte, rétropropagation, mise à jour des poids.

#### Validation et évaluation
- Évaluer le modèle sur des données de validation.
- Utiliser des métriques appropriées (ex: MSE pour la régression).

Bonne chance pour votre examen!
