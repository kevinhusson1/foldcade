# Étude de conception : le meilleur des deux références

!!! info "Statut : planifiée"
    Cette étude n'a pas commencé. Cette page en fixe le périmètre pour qu'elle
    soit menée à part et que son résultat soit réintégré au projet.

## Objectif
Concevoir la meilleure solution **entre** deux références :

- **Réf. 1 — Swap Arcade** : une arcade complète qui se transforme en meuble,
  utilisable aussi avec consoles/PC.
- **Réf. 2 — La borne cachée de Chappel** : porte-caisson basculante, maison,
  à l'échelle d'un atelier.

Pas une copie de l'une ou l'autre : un concept original qui combine le rendu
mobilier de la première et la simplicité de réalisation de la seconde.

## Candidats
| | Idée |
|---|---|
| A | Porte-caisson basculante ([ADR 0003](design-decisions/0003-fold-mechanism.md)) |
| B | Module d'arcade qui se replie sur un meuble de rangement (photo de référence) |
| C… | Hybrides à inventer pendant l'étude |

## Critères (pondération à fixer au lancement)
Réalisable avec outils standards · coût · aspect « meuble » fermé · ergonomie
(hauteur, inclinaison de l'écran, posture) · sécurité du mécanisme · stabilité /
fixation murale · refroidissement et câblage · connexion console/PC ·
réparabilité · nombre de plaques / efficacité du débit · poids et déplacement ·
documentation bilingue possible.

## Méthode
1. Figer les exigences R1–R9 ([concept](concept.md)) et ajouter des scénarios d'usage (appartement, famille, petite pièce).
2. Décomposition fonctionnelle → tableau morphologique des solutions par fonction.
3. Générer 3–5 concepts, les croquer (vues de côté ouvert/fermé).
4. Matrice de notation pondérée ; éliminer, puis affiner les 2 meilleurs.
5. Maquettes rapides (carton / 1:5) et calculs de charge pour le(s) gagnant(s).
6. Pré-revue de sécurité ([sécurité](safety.md)).

## Livrables
Rapport d'étude (EN/FR), croquis et rendus dans `assets/renders/`, feuille de
notation, décision actée dans l'**ADR 0004**, exigences et feuille de route mises à jour.

## Entrées ouvertes
- Spécifications détaillées de Swap Arcade (accessibles seulement en partie).
- Budget cible, contraintes de la pièce (mural ou posé au sol), public visé.
