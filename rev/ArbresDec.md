# Mémo sur les Arbres de Décision et la Classification Supervisée

## 1. Arbres de Décision

- **Définition :** Un arbre de décision est un modèle de classification basé sur des critères qui divise l'espace des données en sous-régions homogènes.

- **Construction :** L'arbre est construit en choisissant des critères de manière itérative pour diviser les nœuds jusqu'à l'obtention de feuilles pures.

- **Pureté d'un Nœud :** Mesurée par l'indice de Gini, qui évalue l'homogénéité du nœud en termes de classes.

- **Surapprentissage :** Risque d'ajustement excessif à un ensemble de données d'entraînement, évité en limitant la profondeur de l'arbre.

## 2. Indice de Gini

L'indice de Gini pour un nœud est calculé par la formule :

\[ G(t) = 1 - \sum_{j} p(j|t)^2 \]

où \( p(j|t) \) est la proportion d'observations de la classe \( j \) au nœud \( t \).

## 3. Exemple Pratique

- **Construction :** L'arbre est construit en choisissant des paramètres (X, seuil) pour minimiser l'indice de Gini.

- **Interprétation :** Un nœud avec un indice de Gini proche de 0 est pur, tandis qu'un indice proche de 1 indique une impureté élevée.

## 4. Application avec scikit-learn

- **Utilisation :** La classe `DecisionTreeClassifier` de scikit-learn permet de créer et d'entraîner des arbres de décision.

- **Évaluation :** L'évaluation de la performance se fait en divisant les données en ensembles d'entraînement et de test.

- **Visualisation :** La représentation graphique de l'arbre peut être obtenue avec la librairie graphviz.

## 5. Gestion du Surapprentissage

- **Profondeur de l'Arbre :** Limiter la profondeur de l'arbre aide à prévenir le surapprentissage en évitant une trop grande complexité.

---

**Remarque :** Adapter les paramètres, choisir judicieusement les critères, et gérer le surapprentissage sont des éléments clés pour un arbre de décision efficace.

