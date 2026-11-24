# 0001 — Analyse des références

| | |
|---|---|
| **Date** | 2026-11-24 |
| **Jalon** | v0.0 Étude de conception |
| **Auteurs** | Porteur du projet · assistant IA (Claude) |
| **Statut** | Terminé |

## Objectif
Comprendre le besoin avant toute conception, en analysant le dépôt, l'image de
référence locale et les sources publiques des deux références.

## Ce qui a été fait
- Relecture complète du dépôt (concept, ADR 0001 à 0003, étude, sécurité, feuille de route).
- Analyse de l'image locale `assets/references/inspiration-concept.webp` (non redistribuée).
- Lecture de la page Kickstarter de Swap Arcade (description, FAQ, récompenses) et
  de ses visuels, consultée le 2026-11-24.
- Lecture de la description et de la transcription automatique de la vidéo
  d'Alexandre Chappel, et de sa page de plans.

## Constats

### Image de référence locale
C'est un visuel marketing de Swap Arcade qui montre les quatre états : borne
complète, ouverture, repli, buffet fermé.

### Swap Arcade (produit commercial)

| Élément | Valeur publiée |
|---|---|
| Campagne | 12 mai – 12 juin 2026 ; 231 392 $ engagés par 177 contributeurs ; livraison annoncée en janvier 2027 |
| Prix | 1 297 $ (1 097 $ en lève-tôt) ; un kit DIY **sans transformation** à 447 $ |
| Mode borne | environ 70" × 28" × 14" (≈ 178 × 71 × 36 cm) |
| Mode meuble | environ 36" × 29" × 13,5" (≈ 91 × 74 × 34 cm) |
| Écran | 27", HDMI, haut-parleurs intégrés |
| Commandes | 2 joueurs, joysticks Sanwa JLF-TP-8YT, **8 boutons par joueur** + boutons de fonction ; options spinner, trackball 2", pistolet Sinden |
| Électronique | Raspberry Pi 4 sous Batocera ; option mini-PC Intel N100 ; encodeur Brook Zero-Pi compatible Switch/Switch 2, PS1 à PS3, PC X-Input |
| Structure | Partie haute en MDF peint, fixée à un **cadre métallique** avec articulation ; meuble en bois dur et contreplaqué ; finitions Naturel, Noyer, Tabac foncé ou brut |
| Sécurité | Mouvement **contrebalancé** ; goupilles de verrouillage rapide aux coins avant, seconde série redondante à l'arrière |
| Rangement | Dans le meuble bas, accessible **uniquement en mode borne** ; les portes avant sont de fausses portes |
| Propriété | **Brevet en instance** (Cookson Innovations Inc.) |

La cinématique exacte n'est pas publiée. Les visuels montrent des panneaux en bois à
charnières noires visibles, qui s'ouvrent pour laisser monter la partie haute.

### Borne cachée de Chappel (réalisation maison, 2021)
La transcription **confirme** le mécanisme décrit dans l'[ADR 0003](../design-decisions/0003-fold-mechanism.md) :

- meuble **mural** en contreplaqué chêne de 16 mm, une seule plaque, chants plaqués, aucune vis visible (lamelles et vis en poche) ;
- la façade bascule à 90° et devient le pupitre ; l'écran est incliné vers l'arrière dans le caisson ;
- pivot : cylindre imprimé en 3D traversé par un tourillon ; arrêt : taquets d'étagère ; loquet : ressort et tige en laiton dans un logement imprimé ;
- fausse rainure en bas, car la traverse inférieure fait partie de la porte ;
- dessus du pupitre clipsé (connecteurs de type Lamello Clamex), retiré à la ventouse ; il est déjà tombé une fois et trois coins ont cassé : **l'accès maintenance est un point faible** ;
- Raspberry Pi sous RetroPie, kit encodeur USB, boutons à microrupteur ; haut-parleurs au-dessus de l'écran ; platine imprimée en 3D (USB, reset, interrupteur général, alimentation) ;
- plans vendus 15 $ : dessins bois métriques et fichiers 3D, **sans schéma électrique**, aucune licence indiquée.

### Synthèse
La « meilleure borne » doit tenir trois promesses à la fois :

1. **Expérience arcade authentique** (écran, posture, commandes, son, présence) ;
2. **Disparition totale** (meuble crédible, aucune pièce libre ni quincaillerie visible) ;
3. **Constructible et ouverte** (outillage accessible, réparable, sûre, documentée jusqu'au câblage).

Swap Arcade tient 1 et 2 au détriment de 3 ; Chappel tient 2 et 3 au détriment de 1.

### Écarts relevés dans le dépôt
- Le concept indiquait que les spécifications de Swap Arcade étaient inaccessibles.
- L'ADR 0003 se disait « non vérifié ».
- R1 prévoyait 6 boutons par joueur ; Swap Arcade en a 8.
- La connexion consoles n'était pas une exigence.
- Le brevet en instance de Swap Arcade n'était pas mentionné.

Ces écarts sont traités dans l'entrée [0002](0002-scoping.md).

## Décisions
Aucune : entrée d'analyse.

## Fichiers produits ou modifiés
Aucun dans le dépôt (analyse seule).

## Étape suivante
Cadrer le besoin avec le porteur du projet : format, plateforme, outillage, licence.
