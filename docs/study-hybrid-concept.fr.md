# Étude de conception : le meilleur des deux références

!!! info "Statut : planifiée"
    Cette étude n'a pas commencé. Cette page en fixe le périmètre pour qu'elle
    soit menée à part et que son résultat soit réintégré au projet. Chaque étape
    sera consignée dans le [journal de bord](journal/index.md).

## Objectif
Concevoir la meilleure solution **entre** deux références :

- **Réf. 1 — Swap Arcade** : une arcade complète qui se transforme en meuble,
  utilisable aussi avec consoles/PC.
- **Réf. 2 — La borne cachée de Chappel** : porte-caisson basculante, maison,
  à l'échelle d'un atelier.

Pas une copie de l'une ou l'autre : un concept original qui combine le rendu
mobilier de la première et la simplicité de réalisation de la seconde.

## Contraintes fixées
Issues du cadrage ([journal 0002](journal/0002-scoping.md)) :

- meuble **posé au sol et déplaçable**, sans fixation murale (R10) ;
- **PC puissant** dans un compartiment ventilé (R5, R11) ;
- **commandes de mouvement** et rangement/recharge des manettes (R12, R13) ;
- **outils de base, sans CNC**, impression 3D dans la boucle (R6) ;
- budget non contraint pendant le concept (R7) ;
- aucune reprise de la cinématique brevetée de Swap Arcade.

## Candidats
| | Idée |
|---|---|
| A′ | Porte-caisson basculante ([ADR 0003](design-decisions/0003-fold-mechanism.md)) intégrée à un meuble posé au sol |
| B | Module d'arcade qui se replie sur un meuble de rangement (photo de référence) |
| C… | Hybrides à inventer pendant l'étude |

## Critères (pondération à fixer au lancement)
Réalisable avec outils de base et impression 3D · aspect « meuble » fermé ·
ergonomie (hauteur, inclinaison et taille de l'écran, posture debout et assise) ·
sécurité du mécanisme · stabilité ouverte et fermée · mobilité (poids, roulettes,
seuils) · refroidissement d'un PC puissant, bruit et câblage · intégration du
capteur de mouvement et liaison Bluetooth · rangement et recharge des manettes ·
réparabilité et accès maintenance · nombre de plaques / efficacité du débit ·
coût (suivi, non contraignant) · documentation bilingue possible.

## Méthode
1. Figer les exigences R1–R14 ([concept](concept.md)) et ajouter des scénarios d'usage (appartement, famille, petite pièce, déménagement d'une pièce à l'autre).
2. Décomposition fonctionnelle → tableau morphologique des solutions par fonction.
3. Générer 3–5 concepts, les croquer (vues de côté ouvert/fermé).
4. Matrice de notation pondérée ; éliminer, puis affiner les 2 meilleurs.
5. Maquettes rapides (carton / 1:5) et calculs de charge et de stabilité pour le(s) gagnant(s).
6. Pré-revue de sécurité ([sécurité](safety.md)).

## Livrables
Rapport d'étude (EN/FR), croquis et rendus rangés par itération dans
`assets/renders/iter-NNNN/`, feuille de notation, décision actée dans l'**ADR 0004**,
exigences et feuille de route mises à jour, une entrée de journal par étape.

## Entrées ouvertes
- Hypothèses H1 à H4 à confirmer (outillage, imprimante, une seule personne, écran 27") : voir [journal 0002](journal/0002-scoping.md).
- Nombre de boutons par joueur, posture principale, type de roulettes.
- Plateforme PC et système : ADR dédié, à mener en parallèle (il conditionne le volume et la ventilation).
