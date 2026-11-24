<div align="center">

# FoldCade

**Une borne d'arcade open source qui se fond dans votre salon.**
**An open-source arcade cabinet that disappears into your living room.**

[🇬🇧 English](README.md) · 🇫🇷 Français

![statut](https://img.shields.io/badge/statut-concept-orange)
![matériel](https://img.shields.io/badge/mat%C3%A9riel-CERN--OHL--P--2.0-blue)
![logiciel](https://img.shields.io/badge/logiciel-MIT-green)
![docs](https://img.shields.io/badge/docs-CC%20BY%204.0-lightgrey)

<!-- TODO : image principale (rendu ou photo) : assets/renders/hero.webp -->

</div>

## Qu'est-ce que FoldCade ?

FoldCade est une borne d'arcade 2 joueurs, entièrement documentée, constructible
et **modifiable**. Son idée phare : le module d'arcade **se replie** et repose sur
un meuble de rangement en bois. Une fois la partie finie, il ne reste dans la
pièce qu'un joli meuble : une borne *cachée à la vue de tous*.

C'est un **mélange assumé de deux inspirations** :

1. une **borne moderne et refermable** (arcade verticale sur un meuble de rangement
   à double porte, avec de la place pour une console et ses câbles) ;
2. une réalisation **maison de « borne cachée »** qui montre comment fabriquer
   ce type de machine avec des outils courants.

L'objectif est une **proposition propre et originale**, pas une copie : plans
ouverts, nomenclature honnête et guide de montage accessible à tous.

> **Statut : concept / pré-v0.1.** Rien n'est encore validé. Voir la
> [feuille de route](docs/roadmap.fr.md). Ne construisez pas à partir de plans
> non publiés.

## Objectifs

- ✅ 2 joueurs, 2 joysticks, 6 boutons chacun, boutons start / crédit
- ✅ Écran, haut-parleurs et ordinateur masqués ou protégés une fois replié
- ✅ Rangement pour console / accessoires dans le meuble
- ✅ Réalisable avec un atelier standard (ou découpe CNC / laser)
- ✅ Documentation bilingue (FR / EN), nomenclature avec alternatives et prix
- ✅ Sécurité d'abord : secteur, poussières, points de pincement documentés

## Plan du dépôt

| Dossier | Contenu |
|---|---|
| [`docs/`](docs/index.fr.md) | Site de documentation (MkDocs, FR + EN) |
| [`hardware/`](hardware/) | CAO, plans de découpe, impressions 3D, électronique, nomenclature |
| [`software/`](software/) | Notes sur l'image système, configuration, scripts |
| [`assets/`](assets/) | Rendus et photos |
| [`.github/`](.github/) | Modèles d'issues, CI |

## Pour commencer

1. Lisez le [concept](docs/concept.fr.md) et les [règles de sécurité](docs/safety.fr.md).
2. Suivez la [feuille de route](docs/roadmap.fr.md) et choisissez une *good first issue* dans l'onglet Issues.
3. À la sortie : téléchargez le paquet v0.x dans **Releases** (plans de découpe, nomenclature, STL).

## Contribuer

Toutes les compétences sont bienvenues : menuiserie, CAO, électronique,
logiciel, traduction, photo. Voir [CONTRIBUTING.md](CONTRIBUTING.md) et le
[Code de conduite](CODE_OF_CONDUCT.md).

## Licence et attribution

Libre et ouvert, **usage commercial autorisé — à condition de citer la source.**
Détails dans [LICENSE.md](LICENSE.md) et [ATTRIBUTION.md](ATTRIBUTION.md).

| Matériel | Logiciel | Docs et médias |
|---|---|---|
| CERN-OHL-P-2.0 | MIT | CC BY 4.0 |

Ce projet **ne fournit ni jeux ni ROMs**. Voir les [notes juridiques](docs/legal.fr.md).
