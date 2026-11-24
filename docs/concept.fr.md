# Concept

## Vision

Une borne d'arcade verticale 2 joueurs **cachée à la vue de tous** : le module
d'arcade se replie sur un meuble de rangement en bois à double porte. Fermée,
elle ressemble à un buffet ; ouverte, c'est une vraie borne d'arcade, avec de la
place à l'intérieur pour une console, un ordinateur et les câbles.

## Inspirations

FoldCade mélange deux références. Nous reprenons des **idées, pas des plans** ;
tous les dessins sont refaits de zéro.

| Référence | Ce que nous retenons |
|---|---|
| Une borne d'arcade commerciale refermable (financée par crowdfunding ; référence à ajouter — voir TODO) | Meuble de rangement à double porte, module d'arcade transformable, aspect « meuble », façade en aplats de couleur, 2 joysticks + 6 boutons par joueur |
| *« This Arcade Machine is hidden in plain sight! And This is how I Built It! »* d'Alexandre Chappel — <https://youtu.be/OB8VauGEvqg> | Méthode de construction maison, principe de la borne cachée, outillage d'atelier |

!!! note "TODO"
    Ajouter le lien exact de la campagne de financement et la liste de ce que
    nous gardons / changeons (dimensions, mécanisme, matériaux, prix cible).

## Exigences fonctionnelles (brouillon)

| ID | Exigence |
|---|---|
| R1 | 2 joueurs, 2 joysticks, 6 boutons d'action chacun, start/crédit |
| R2 | Taille et format d'écran à décider (voir ADR 0002) |
| R3 | Replié, l'écran et les commandes sont masqués ; aucune pièce libre |
| R4 | Mécanisme sûr : pas de point de pincement, mouvement amorti, stable ouvert |
| R5 | Le meuble accueille console/PC avec ventilation et passage de câbles |
| R6 | Réalisable en panneaux avec outils standards ; CNC/laser optionnel |
| R7 | Budget cible de la nomenclature à définir pour la v0.1 |

## Questions ouvertes

- Mécanisme de repli : charnière + vérin à gaz, tringlerie ou coulissant ?
- Écran : 24" 16:9 paysage, ou 4:3 / compatible vertical ?
- Ordinateur : Raspberry Pi 5, mini-PC, ou laissé au choix ?
- Matériau : contreplaqué bouleau ou MDF (finition, poids, coût).
