# 0002 — Cadrage du besoin

| | |
|---|---|
| **Date** | 2026-11-24 |
| **Jalon** | v0.0 Étude de conception |
| **Auteurs** | Porteur du projet · assistant IA (Claude) |
| **Statut** | Terminé |

## Objectif
Fixer les grandes orientations du projet à partir de l'analyse [0001](0001-reference-analysis.md),
avant de lancer l'étude de conception.

## Décisions du porteur du projet

| ID | Décision | Raison |
|---|---|---|
| D1 | **Meuble posé au sol et déplaçable.** Pas de fixation murale. | Pas de trous dans le mur ; la borne peut changer de pièce ; plus de volume pour l'électronique. |
| D2 | **Vrai mini-PC ou PC compact puissant**, pas de Raspberry Pi. | Émuler les consoles récentes. |
| D3 | **Émulation visée** : toutes les consoles rétro, PS3, Xbox 360, Switch, et PS4 si le matériel le permet. | Une borne polyvalente, pas seulement un multicade. |
| D4 | **Commandes de mouvement** : vraies Wiimotes et un capteur de mouvement intégré ; gestion du mouvement pour l'émulation Switch. | Un vrai plus par rapport aux références. |
| D5 | **Outils de base uniquement**, pas de CNC. **L'impression 3D est obligatoirement dans la boucle** pour les pièces qui le justifient. | Rester constructible par le plus grand nombre. |
| D6 | **Budget non contraint** pendant la phase concept. | On cherche d'abord la meilleure solution ; les coûts seront relevés au fil de l'eau. |
| D7 | **Plans entièrement libres.** | Permettre à d'autres de rejoindre le projet et de travailler ensemble. |
| D8 | **Journal de bord** de chaque étape ; toutes les itérations restent visibles. | Traçabilité et accueil des contributeurs (voir [règles](index.md)). |

Conséquence directe de D1 : l'option A de l'[ADR 0003](../design-decisions/0003-fold-mechanism.md)
(meuble mural) est écartée **telle quelle**. Son principe de porte-caisson qui
devient pupitre reste une brique candidate pour un meuble posé au sol.

## Conséquences techniques à étudier
Ce ne sont pas des décisions : ce sont les points que l'étude de conception devra traiter.

1. **Puissance et chaleur.** PS3, Xbox 360 et PS4 demandent un processeur récent
   multicœur et une carte graphique performante. Selon la machine retenue, la
   dissipation va d'environ 65 W (mini-PC) à plus de 300 W (PC compact avec carte
   graphique). Il faut une ventilation active filtrée (entrée basse, sortie haute),
   un compartiment technique accessible et une attention au bruit. Le choix du
   matériel et du système (Linux type Batocera, ou Windows avec un frontend type
   RetroBat ou LaunchBox, certains émulateurs étant surtout développés pour Windows)
   fera l'objet d'un ADR dédié.
2. **Manettes.** Les jeux 3D de ces consoles se jouent avec deux sticks et des
   gâchettes : le panneau arcade ne suffit pas. Il faut des manettes sans fil, leur
   rangement et leur recharge dans le meuble. L'encodeur du panneau doit être
   compatible XInput au minimum ; piste libre à évaluer : une carte RP2040 avec le
   firmware open source GP2040-CE.
3. **Mouvement.**
    - Les Wiimotes servent aux jeux Wii (Dolphin) et Wii U (Cemu). Elles ont besoin
      d'une **barre capteur infrarouge** (de simples LED IR) et d'une liaison
      Bluetooth. Piste : une barre capteur USB avec Bluetooth intégré (type Mayflash
      DolphinBar), logée dans le fronton ou sous l'écran.
    - Le mouvement de la Switch passe par le **gyroscope** des Joy-Con ou de manettes
      compatibles (Pro Controller, DualShock 4, DualSense), pas par la caméra IR de la
      Wiimote. Il faut donc aussi prévoir ces manettes et leur recharge.
    - Un cadre de LED IR autour de l'écran pourrait également servir à des pistolets
      IR (type GUN4IR) : synergie à étudier.
    - Le récepteur Bluetooth doit être placé loin de toute masse métallique.
4. **Mobilité et stabilité.** Roulettes à frein, si possible cachées dans le socle ;
   centre de gravité bas (PC et alimentation en bas) ; stabilité vérifiée ouverte et
   fermée ; prises en main pour pousser ; parties mobiles verrouillées pendant le
   déplacement ; passage des seuils.
5. **Outillage et impression 3D.** Sans CNC, l'impression 3D sert aussi à la
   précision : **gabarits de perçage et de montage**, pièces du mécanisme, grilles,
   platines, supports. Pas de fraise spéciale de type Lamello ; défonceuse optionnelle.
   Les grandes pièces sont découpées pour tenir sur un plateau standard ; matériau
   résistant à la chaleur (PETG ou ASA plutôt que PLA) près du PC.
6. **Juridique.** L'émulation de consoles récentes, notamment la Switch, est un sujet
   sensible : le projet ne fournit ni ne référence aucune clé, firmware, BIOS ou jeu.
   Chacun utilise des copies issues de son propre matériel, selon la loi de son pays.
7. **Ergonomie double usage.** L'arcade se joue debout au pupitre ; les jeux console à
   la manette peuvent se jouer assis, plus loin. La hauteur et la taille de l'écran
   doivent servir les deux.
8. **Propriété intellectuelle.** Swap Arcade a un brevet en instance : on s'appuie sur
   des principes génériques (charnières, pivots, contrepoids, glissières) sans
   reproduire sa cinématique, et on vérifie avant de publier un mécanisme proche.

## Hypothèses à confirmer

| ID | Hypothèse |
|---|---|
| H1 | « Outils de base » = perceuse-visseuse, scie sauteuse, scie circulaire avec guide, ponceuse, serre-joints ; débit des panneaux possible en magasin. |
| H2 | Imprimante 3D grand public : volume d'environ 220 × 220 × 250 mm, PLA et PETG. |
| H3 | Un seul adulte doit pouvoir déplacer la borne et la transformer. |
| H4 | Point de départ : écran 16:9 d'environ 27". |

## Fichiers produits ou modifiés
- Création du journal : `docs/journal/` (index, entrées 0001 et 0002).
- `docs/concept` : spécifications publiques de Swap Arcade, décisions D1 à D8, exigences R1 à R14.
- `docs/design-decisions/0003-fold-mechanism` : vérification par la transcription, impact de D1.
- `docs/study-hybrid-concept` : nouvelles contraintes et critères.
- `docs/safety` : mobilité et chaleur.
- `docs/legal` : clés et firmwares.
- `docs/index`, `docs/roadmap`, `README`, `software/README.md`, `CHANGELOG.md`, `mkdocs.yml`.

## Questions ouvertes
- Nombre de boutons par joueur : 6 ou 8 ?
- Posture principale : debout, assis, ou les deux ?
- Taille d'écran définitive et hauteur des yeux.
- Roulettes visibles ou escamotables ?

## Étape suivante
Lancer l'étude de conception (v0.0) : scénarios d'usage, décomposition fonctionnelle,
tableau morphologique, puis 3 à 5 concepts croqués.
