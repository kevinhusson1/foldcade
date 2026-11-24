# ADR 0003 — Mécanisme de repli : porte-caisson basculante (option A)

- **Statut :** Proposé (à valider par un prototype)
- **Date :** 2026-11-24

## Contexte
La borne cachée d'Alexandre Chappel (voir [concept](../concept.md)) repose sur
une **porte-caisson basculante à 90°** : la façade du meuble est un volume creux
qui devient le pupitre de commande une fois abaissé. Le résumé ci-dessous est
une analyse technique fournie par le porteur du projet ; elle décrit cette
réalisation de référence et n'a pas été vérifiée par nous sur l'objet réel.

## Mécanisme de référence (résumé)

| Sous-ensemble | Principe |
|---|---|
| **Pivot** | Deux cylindres creux imprimés en 3D dans les parois latérales du caisson mobile ; des tourillons en bois les traversent jusque dans des perçages borgnes des montants du cadre fixe. Pivot invisible de l'extérieur. |
| **Arrêt à 90°** | Deux taquets d'étagère métalliques dans les parois internes du cadre ; l'arrière du caisson vient en appui une fois abaissé, le pupitre s'arrête à l'horizontale et supporte les mains des deux joueurs. |
| **Interstice masqué** | La traverse inférieure fait partie de la porte mobile. Une rainure décorative fraisée sur la façade imite l'interstice d'une porte standard et masque le jeu nécessaire à la rotation vers l'intérieur. |
| **Loquet** | Tige de laiton à ressort dans un logement imprimé en 3D encastré dans le chant supérieur de la porte ; le ressort la pousse vers le haut dans une gâche sous le plateau fixe. On tire l'ergot vers le bas pour libérer. |
| **Maintenance** | Caisson fermé sur toutes ses faces ; la façade se démonte avec des connecteurs Lamello Clamex/Tenso (alignée en bas par deux lamelles bois, clipsée en haut), retirée avec une ventouse de vitrier. Aucune vis visible. |
| **Fixation murale** | Tasseau français (French cleat) : deux traverses arrière à 45° s'emboîtent sur un tasseau mural au biseau inversé ; la gravité plaque le meuble au mur et répartit la charge. |

## Options pour FoldCade

- **A — Porte-caisson basculante (cet ADR).** Simple, peu de pièces, quincaillerie
  entièrement cachée, adaptée à un meuble mural ou bas. Exige une fixation murale solide.
- **B — Module d'arcade qui se replie sur un meuble de base** (style Swap Arcade,
  d'après la photo de référence). Tringlerie plus complexe ; posé au sol ; à étudier.

## Points à vérifier / adapter (nos remarques, pas issues de la référence)

- **Cas de charge :** appui des deux joueurs sur un pupitre en porte-à-faux ; définir
  une charge d'essai et un coefficient de sécurité avant la v0.1 (voir [sécurité](../safety.md)).
- **Arrêt et pivot :** taquets et tourillons bois à dimensionner au cisaillement ;
  prévoir des fourreaux métalliques ou des charnières certifiées comme variante plus sûre.
- **Loquet :** une défaillance ne doit pas laisser tomber un panneau lourd ; ajouter
  une seconde retenue ou un amortisseur et vérifier les pincements (R4).
- **Lamello Clamex/Tenso** exige une fraise spécialisée : documenter des alternatives
  (serrures à came, aimants, vis masquées sous cache) pour rester abordable.
- **French cleat :** le mur doit porter la charge : préciser types de murs, fixations
  et contrôle des ancrages ; variante posée au sol ou sangle anti-basculement.
- **Chaleur :** un caisson fermé avec un Raspberry Pi demande une ventilation (R5).

## Décision
**Pas encore de choix.** Le but est de concevoir la meilleure solution *entre* les
deux références, pas d'en choisir une. Une [étude de conception](../study-hybrid-concept.md)
dédiée comparera les options A, B et des hybrides ; son résultat sera acté dans l'ADR 0004.
L'option A est citée comme point de départ le mieux documenté, rien de plus.
