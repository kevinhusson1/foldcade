# Journal de bord

Le journal trace **chaque étape** du travail sur FoldCade, dans l'ordre, pour que
toutes les itérations restent visibles : ce qui a été essayé, décidé, abandonné, et
pourquoi. Il sert de mémoire au projet et de point d'entrée pour toute personne
qui veut nous rejoindre.

## Entrées

| N° | Date | Titre | Jalon | Résultat |
|---|---|---|---|---|
| [0001](0001-reference-analysis.md) | 2026-11-24 | Analyse des références | v0.0 | Spécifications de Swap Arcade et mécanisme de Chappel établis |
| [0002](0002-scoping.md) | 2026-11-24 | Cadrage du besoin | v0.0 | Meuble posé au sol et déplaçable, mini-PC puissant, commandes de mouvement, outils de base + impression 3D |

## Règles

1. **Une entrée par étape** terminée (ou séance de travail significative), numérotée
   `NNNN`. Un numéro n'est jamais réattribué.
2. **On ne réécrit pas une entrée publiée.** Une correction de fond se fait dans une
   nouvelle entrée, ou dans une note « Mise à jour (date) » ajoutée en bas. Les
   coquilles peuvent être corrigées.
3. **Chaque entrée** donne l'objectif, ce qui a été fait, les constats, les décisions,
   les fichiers produits ou modifiés et l'étape suivante.
4. **Les itérations de conception ne s'écrasent pas** : croquis, rendus, maquettes et
   fichiers CAO sont rangés par itération (par ex. `assets/renders/iter-0003/`).
   Les variantes rejetées sont conservées avec la raison du rejet.
5. **Les décisions structurantes deviennent des ADR** (`docs/design-decisions/`). Un
   ADR remplacé prend le statut « Remplacé par ADR XXXX » ; il n'est jamais supprimé.
6. **Bilingue** FR/EN, comme le reste de la documentation.
7. **Git** : un commit (ou une pull request) par entrée, par exemple
   `docs(journal): 0003 décomposition fonctionnelle`. L'historique Git reste la
   trace complète ; le journal en est le résumé lisible.

## Modèle d'entrée

```markdown
# NNNN — Titre

| | |
|---|---|
| **Date** | AAAA-MM-JJ |
| **Jalon** | v0.x |
| **Auteurs** | … |
| **Statut** | En cours / Terminé |

## Objectif
## Ce qui a été fait
## Constats
## Décisions
## Fichiers produits ou modifiés
## Questions ouvertes
## Étape suivante
```
