# Concept

## Vision

Une borne d'arcade 2 joueurs **posée au sol, déplaçable et cachée à la vue de
tous**. Fermée, elle ressemble à un buffet ; ouverte, c'est une vraie borne
d'arcade. Elle est animée par un PC assez puissant pour émuler les consoles
récentes, accepte des commandes de mouvement (Wiimotes, gyroscope) et range ses
manettes à l'intérieur.

## Inspirations

FoldCade mélange deux références. Nous reprenons des **idées, pas des plans** ;
tous les dessins sont refaits de zéro.

| Référence | Ce que nous retenons |
|---|---|
| *Swap Arcade* de Les Cookson & Ken Higginson, Kickstarter 2026 ([campagne](https://www.kickstarter.com/projects/amat/swap-arcade-full-arcade-that-turns-into-a-furniture-cabinet/description)) | Borne pleine taille qui devient un buffet, aspect « meuble », décor en aplats de couleur, polyvalence rétro + consoles, rangement intégré, sécurité du mouvement (contrepoids, double verrouillage) |
| *« This Arcade Machine is hidden in plain sight! And This is how I Built It! »* d'Alexandre Chappel — <https://youtu.be/OB8VauGEvqg> | Méthode de construction maison, porte qui devient pupitre, quincaillerie invisible, pièces imprimées en 3D. Sa [page de vente](https://www.alch.shop/projects/p/arcade-cabinet) propose des plans payants (dessins métriques, fichiers d'impression 3D, liste de pièces avec liens, vidéos de ressources) pour une borne réalisée dans **une seule plaque de contreplaqué de 16 mm**, sur Raspberry Pi avec RetroPie. |

### Ce que nous gardons, changeons et ajoutons par rapport à ces plans

| | Garder | Changer / ajouter |
|---|---|---|
| Matériau | Construction en panneaux, **dessins métriques**, petites pièces imprimées en 3D | Outils de base sans CNC ; **gabarits de perçage imprimés en 3D** pour la précision ; vérifier le nombre de plaques (optimisation de débit, voir R8) |
| Documentation | Liste de pièces avec liens, vidéos de ressources, note claire « ce qui est inclus » | **Libre et gratuite**, avec **schéma de câblage complet** et guide de sécurité (la référence exclut explicitement l'électronique), nomenclature avec quantités, prix et alternatives, bilingue, **journal de bord** public |
| Périmètre | 2 joueurs | Meuble **posé au sol et déplaçable** ; **PC puissant** (émulation jusqu'à PS3, Xbox 360, Switch, voire PS4) ; **commandes de mouvement** ; rangement et recharge des manettes |
| Licence | — | Licences ouvertes avec mention obligatoire (voir ADR 0001) |

!!! info "Ce que nous savons de Swap Arcade"
    D'après la page publique de la campagne (consultée le 2026-11-24, détails dans
    le [journal 0001](journal/0001-reference-analysis.md)) : environ
    178 × 71 × 36 cm en mode borne et 91 × 74 × 34 cm en mode meuble ; écran 27"
    avec haut-parleurs ; joysticks Sanwa et 8 boutons par joueur ; Raspberry Pi 4
    sous Batocera ou mini-PC N100 ; encodeur compatible Switch, PlayStation et PC ;
    partie haute en MDF sur un cadre métallique articulé, contrebalancée et
    verrouillée par goupilles à l'avant et à l'arrière ; rangement accessible
    seulement en mode borne.

!!! warning "Brevet en instance"
    Swap Arcade est annoncée « patent pending ». Nous nous appuyons sur des
    principes génériques (charnières, pivots, contrepoids, glissières) sans
    reproduire sa cinématique, et nous vérifions avant de publier un mécanisme proche.

Le mécanisme de la seconde référence est détaillé dans l'[ADR 0003](design-decisions/0003-fold-mechanism.md).

## Orientations décidées

Décidées le 2026-11-24 par le porteur du projet ; raisons et conséquences dans le
[journal 0002](journal/0002-scoping.md).

- **D1** Meuble posé au sol et déplaçable, sans fixation murale.
- **D2** Vrai mini-PC ou PC compact puissant, pas de Raspberry Pi.
- **D3** Émulation : toutes les consoles rétro, PS3, Xbox 360, Switch, et PS4 si le matériel le permet.
- **D4** Commandes de mouvement : vraies Wiimotes et capteur intégré ; mouvement pour l'émulation Switch.
- **D5** Outils de base, pas de CNC ; impression 3D obligatoirement dans la boucle.
- **D6** Budget non contraint pendant la phase concept.
- **D7** Plans entièrement libres et collaboratifs.
- **D8** Journal de bord de chaque étape ; toutes les itérations restent visibles.

## Exigences fonctionnelles (brouillon)

| ID | Exigence |
|---|---|
| R1 | 2 joueurs : 1 joystick et 6 à 8 boutons d'action chacun (nombre fixé par l'étude), start/crédit, boutons de fonction (menu, raccourcis) |
| R2 | Écran 16:9, taille à décider (point de départ : environ 27") |
| R3 | Replié, l'écran et les commandes sont masqués ; aucune pièce libre ; aspect de meuble crédible |
| R4 | Mécanisme sûr : pas de point de pincement, mouvement amorti ou contrebalancé, verrouillage redondant, stable ouvert |
| R5 | Compartiment technique pour un PC puissant : ventilation active filtrée, passage de câbles, accès maintenance sans démontage risqué |
| R6 | Réalisable avec des outils de base, sans CNC ; impression 3D pour les pièces spécifiques et les gabarits, sur une imprimante grand public |
| R7 | Budget non contraint en phase concept ; les coûts sont relevés dans la nomenclature dès qu'ils sont connus |
| R8 | Débit optimisé (objectif : nombre minimal de plaques standard), tous les dessins en métrique |
| R9 | Schéma de câblage complet, câblage du bouton marche/arrêt, et note « inclus / non inclus » dans le guide de montage |
| R10 | Posée au sol sans fixation murale ; déplaçable par une personne (roulettes à frein ou équivalent) ; stable ouverte comme fermée |
| R11 | Émulation cible : consoles rétro, PS3, Xbox 360, Switch ; PS4 si le matériel le permet |
| R12 | Commandes de mouvement : vraies Wiimotes avec barre capteur IR intégrée ; gyroscope (Joy-Con ou manettes compatibles) pour l'émulation Switch |
| R13 | Manettes sans fil, Wiimotes et Joy-Con rangées et rechargées dans le meuble |
| R14 | Plans libres et collaboratifs ; chaque itération tracée dans le [journal de bord](journal/index.md) |

## Questions ouvertes

- Mécanisme de transformation : charnière + vérin à gaz, contrepoids, tringlerie ou coulissant ?
- Écran : taille définitive, hauteur des yeux, posture debout et assise ?
- PC : mini-PC à graphique intégré ou PC compact avec carte graphique ? Linux (type Batocera) ou Windows (frontend type RetroBat ou LaunchBox) ?
- Encodeur du panneau : compatible XInput au minimum (piste libre : RP2040 + GP2040-CE) ?
- Capteur de mouvement : barre IR seule, ou cadre IR qui sert aussi aux pistolets ?
- Roulettes : visibles ou escamotables ?
- Matériau : contreplaqué bouleau ou MDF (finition, poids, coût).
