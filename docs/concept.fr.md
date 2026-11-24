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
| *Swap Arcade* de Les Cookson & Ken Higginson, Kickstarter 2026 ([campagne](https://www.kickstarter.com/projects/amat/swap-arcade-full-arcade-that-turns-into-a-furniture-cabinet/description)) | Meuble de rangement à double porte, module d'arcade transformable, aspect « meuble », façade en aplats de couleur, 2 joysticks + 6 boutons par joueur |
| *« This Arcade Machine is hidden in plain sight! And This is how I Built It! »* d'Alexandre Chappel — <https://youtu.be/OB8VauGEvqg> | Méthode de construction maison, principe de la borne cachée, outillage d'atelier. Sa [page de vente](https://www.alch.shop/projects/p/arcade-cabinet) propose des plans payants (dessins métriques, fichiers d'impression 3D, liste de pièces avec liens, vidéos de ressources) pour une borne réalisée dans **une seule plaque de contreplaqué de 16 mm**, sur Raspberry Pi avec RetroPie. |

### Ce que nous gardons, changeons et ajoutons par rapport à ces plans

| | Garder | Changer / ajouter |
|---|---|---|
| Matériau | Construction en panneaux, **dessins métriques**, petites pièces imprimées en 3D | Vérifier si toute la borne tient encore dans peu de plaques (optimisation de débit, voir R8) |
| Documentation | Liste de pièces avec liens, vidéos de ressources, note claire « ce qui est inclus » | **Libre et gratuite**, avec **schéma de câblage complet** et guide de sécurité (la référence exclut explicitement l'électronique), nomenclature avec quantités, prix et alternatives, bilingue |
| Périmètre | 2 joueurs, logiciel de type RetroPie | Meuble refermable avec rangement (première référence) |
| Licence | — | Licences ouvertes avec mention obligatoire (voir ADR 0001) |

!!! info "Ce que nous savons de Swap Arcade"
    D'après la page publique de la campagne : jeux rétro intégrés **et** connexion
    à Switch, PlayStation, PC et plus ; se transforme en meuble ; construite en
    MDF, bois dur et contreplaqué ; pièces réparables et remplaçables (joysticks,
    boutons, câbles, électronique). Ses spécifications détaillées, dimensions et
    mécanisme ne nous étaient pas accessibles, donc rien n'est supposé ici.

    Le mécanisme étudié en détail vient de la seconde référence : voir
    [ADR 0003](design-decisions/0003-fold-mechanism.md).

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
| R8 | Débit optimisé (objectif : nombre minimal de plaques standard, ex. contreplaqué 16 mm), tous les dessins en métrique |
| R9 | Schéma de câblage complet, câblage du bouton marche/arrêt, et note « inclus / non inclus » dans le guide de montage |

## Questions ouvertes

- Mécanisme de repli : charnière + vérin à gaz, tringlerie ou coulissant ?
- Écran : 24" 16:9 paysage, ou 4:3 / compatible vertical ?
- Ordinateur : Raspberry Pi 5, mini-PC, ou laissé au choix ?
- Matériau : contreplaqué bouleau ou MDF (finition, poids, coût).
