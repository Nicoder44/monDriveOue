## Mémo SVM

1. **Définition :**  
   Une SVM (Machine à Vecteurs de Support) est utilisée pour la classification et la régression dans le domaine de l'apprentissage supervisé.

2. **Objectif :**  
   Trouver un hyperplan qui maximise la marge entre les classes dans l'espace des caractéristiques.

3. **Vecteurs de Support :**  
   Ce sont les points les plus proches de l'hyperplan de séparation. La marge est définie par la distance entre l'hyperplan et ces vecteurs.

4. **Classification à Marge Rigide vs Marge Souple :** 
   - *Marge Rigide :* Aucun chevauchement n'est toléré, adapté aux données linéairement séparables.
   - *Marge Souple :* Tolère des erreurs de classification pour mieux gérer les données non linéairement séparables et les données bruitées.

5. **Noyau (Kernel Trick) :**  
   Une technique permettant de traiter des données non linéairement séparables en évitant explicitement de calculer les nouvelles dimensions.
