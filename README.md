<div align="center">

# 🇪🇺 Catalogue Monitor — data.europa.eu

**Explorateur open source du méta-catalogue européen — 213 catalogues, 1,7 M datasets, 40 pays.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub last commit](https://img.shields.io/github/last-commit/gunout/catalogue-monitor-ue)](https://github.com/gunout/catalogue-monitor-ue/commits)
[![GitHub issues](https://img.shields.io/github/issues/gunout/catalogue-monitor-ue)](https://github.com/gunout/catalogue-monitor-ue/issues)
[![GitHub stars](https://img.shields.io/github/stars/gunout/catalogue-monitor-ue?style=social)](https://github.com/gunout/catalogue-monitor-ue/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/gunout/catalogue-monitor-ue?style=social)](https://github.com/gunout/catalogue-monitor-ue/network/members)

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/fr/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)](https://developer.mozilla.org/fr/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/fr/docs/Web/JavaScript)
[![API](https://img.shields.io/badge/API-data.europa.eu-003399)](https://data.europa.eu/api/hub/search)
[![Proxy](https://img.shields.io/badge/proxy-localhost:8002-blueviolet)](#architecture)
[![DSFR](https://img.shields.io/badge/design-DSFR-000091)](https://www.systeme-de-design.gouv.fr/)
[![Status](https://img.shields.io/badge/status-ready-brightgreen)](#)

[🚀 Démarrage](#démarrage-rapide) · [✨ Fonctionnalités](#fonctionnalités) · [🏗️ Architecture](#architecture) · [🛠️ Stack](#stack-technique) · [📄 Licence](#licence)

</div>

---

## 📖 À propos

**Catalogue Monitor** est un tableau de bord **mono-fichier** qui interroge l'API publique de [data.europa.eu](https://data.europa.eu) et affiche en temps réel les catalogues de données ouvertes de toute l'Europe.

- **213 catalogues** référencés
- **1 752 791 datasets** agrégés
- **40 pays** représentés
- **8 types de sources** (DCAT-AP, CKAN, geospatial, udata, etc.)

Le monitor offre des **filtres de facettes interactifs** (pays, thèmes, types, HVD, catalogues, formats, licences) et charge les résultats **page par page** via un proxy local pour contourner les restrictions CORS de l'API.

> Conçu pour les journalistes, chercheurs, data scientists et citoyens qui veulent **explorer et comprendre** le paysage européen des données ouvertes.

---

## ✨ Fonctionnalités

- 🎛️ **Filtres de facettes interactifs** : 7 facettes (pays, thèmes, types, HVD, catalogues, formats, licences)
- 🔍 **Recherche texte** dans les catalogues chargés
- 🔀 **Tri avancé** : datasets, date, titre, pays
- 📄 **4 vues** : Catalogues · Par pays · Par types · Analyses
- 📊 **Panneau Intelligence** : totaux, filtres actifs, top 5, progression
- 📥 **Exports** CSV / JSON côté client
- 🌙 **Dark mode** persistant
- 📱 **Responsive** : mobile, tablette, desktop
- 🎨 **Design DSFR** (Système de Design de l'État)
- 🔌 **Proxy CORS local** en Python (inclus)
- ⚡ **Chargement incrémental** avec barre de progression
- ✋ **Bouton STOP** pour interrompre le chargement

---

## 🚀 Démarrage rapide

### 1. Cloner le dépôt

    git clone https://github.com/gunout/catalogue-monitor-ue.git
    cd catalogue-monitor-ue

### 2. Lancer le proxy CORS

    python3 proxy.py

Le proxy écoute sur http://localhost:8002.

### 3. Lancer le serveur HTML

Dans un autre terminal :

    python3 -m http.server 8080

### 4. Ouvrir le monitor

Dans ton navigateur :

    http://localhost:8080/index.html

### 5. C'est parti

1. Attends le chargement des facettes (2-3 secondes)
2. Coche **🌍 France** dans la sidebar
3. Clique sur **🌐 CHARGER FILTRÉ**
4. Les ~30 catalogues français s'affichent

---

## 🧭 Utilisation

| Action | Résultat |
|---|---|
| Cocher une **facette** (pays, thème…) | Ajoute un chip en haut + met à jour le compteur |
| Cliquer sur **🌐 CHARGER FILTRÉ** | Lance la requête API avec les filtres |
| Cliquer sur **✖ STOP** | Interrompt le chargement en cours |
| **🔍 Recherche texte** | Filtre localement les catalogues chargés |
| **Tri** | Datasets ↓ / ↑ · Date ↓ · Titre A→Z · Pays A→Z |
| **📋 Catalogues** | Vue liste détaillée |
| **🌍 Par pays** | Barres horizontales par pays |
| **🔌 Types** | Répartition par type de source |
| **📊 Analyses** | Top éditeurs + types |
| **📥 CSV / JSON** | Télécharge les catalogues filtrés |
| **🗑️ Effacer** | Réinitialise tout |

### Exemples de filtres

- 🌍 France → ~30 catalogues
- 🌍 France + 📂 Environnement → ~10 catalogues
- 📂 Agriculture + ⭐ HVD → ~15 catalogues
- 🔌 ckan + 🌍 Allemagne → ~50 catalogues

---

## 🏗️ Architecture

    ┌─────────────────┐      ┌──────────────────┐      ┌─────────────────┐
    │  Ton navigateur │─────▶│  Proxy Python    │─────▶│  data.europa.eu │
    │  (localhost:8080│ HTTP │  (localhost:8002)│ HTTP │  (API officielle│
    │                 │      │  CORS: *         │      │   pas de CORS)  │
    └─────────────────┘      └──────────────────┘      └─────────────────┘

**Pourquoi un proxy ?** L'API data.europa.eu n'envoie pas les en-têtes `Access-Control-Allow-Origin` pour les appels navigateur, ce qui bloque toutes les requêtes `fetch` cross-origin. Le proxy Python fait le relais côté serveur, où le CORS ne s'applique pas.

---

## 🛠️ Stack technique

| Composant | Technologie |
|---|---|
| **Frontend** | HTML5 + CSS3 (variables, grid, flexbox) |
| **Logique** | JavaScript vanilla (ES2020) |
| **API** | data.europa.eu/api/hub/search |
| **Proxy** | Python 3 + http.server (bibliothèque standard) |
| **Design** | DSFR 1.11.2 (variables CSS) |
| **Exports** | Blob API native |
| **Zéro dépendance** | Aucun npm, webpack, ou framework |

---

## 📁 Structure du projet

    catalogue-monitor-ue/
    ├── index.html      ← l'application complète (HTML + CSS + JS)
    ├── proxy.py        ← proxy CORS local (Python)
    ├── catalogue.json  ← exemple de réponse API (fallback local)
    ├── README.md       ← ce fichier
    └── LICENSE         ← MIT

---

## 🔧 Personnalisation

### Changer les facettes affichées

Dans `index.html`, cherche la constante `FACET_KEYS` et modifie le tableau :

    const FACET_KEYS = [
      { key: 'country', label: '🌍 Pays', max: 50 },
      { key: 'categories', label: '📂 Thèmes', max: 30 },
      // Ajoute ou retire des facettes ici
    ];

### Changer le port du proxy

Dans `index.html`, modifie la constante :

    const CORS_PROXY = 'http://localhost:8002/proxy?url=';

Et dans `proxy.py` :

    HTTPServer(('localhost', 8002), ProxyHandler).serve_forever()

### Filtrer par défaut sur un pays

Dans `index.html`, après la déclaration de `state`, ajoute :

    state.selectedFilters = { country: new Set(['fr']) };

---

## ⚠️ Limites connues

- **CORS bloqué** sans le proxy : l'API refuse les appels directs depuis un navigateur
- **L'API v2 est en beta** : son schéma peut évoluer sans préavis
- **Pas de cache persistant** : chaque chargement refait les appels réseau
- **Volume limité** : 100 pages maximum (10 000 catalogues) par sécurité
- **Filtre `source_type`** : sélectionner tous les types = aucun résultat (ET logique)

---

## 🗺️ Roadmap

- [x] **v1.0** — Monitor mono-fichier avec facettes
- [x] **v1.1** — Proxy CORS Python
- [ ] **v1.2** — Cache IndexedDB des résultats
- [ ] **v1.3** — Vue carte européenne (choroplèthe)
- [ ] **v1.4** — Export PNG des vues
- [ ] **v2.0** — Version PWA (offline + installable)
- [ ] **v2.1** — Backend FastAPI optionnel (pour remplacer le proxy Python)

---

## 🤝 Contribution

Les contributions sont **les bienvenues** !

1. Fork le projet
2. Crée une branche (`git checkout -b feature/ma-fonctionnalite`)
3. Commit tes changements (`git commit -m 'Ajout de ma fonctionnalité'`)
4. Push (`git push origin feature/ma-fonctionnalite`)
5. Ouvre une Pull Request

### Signaler un bug

Ouvre une [issue](https://github.com/gunout/catalogue-monitor-ue/issues) en précisant :

- Le navigateur et sa version
- Les étapes pour reproduire
- Le comportement attendu vs observé
- Les logs de la console (F12)

---

## 📄 Licence

Distribué sous licence **MIT**. Voir le fichier LICENSE pour plus d'informations.

Les **données** affichées proviennent de [data.europa.eu](https://data.europa.eu) et sont soumises à leur propre licence (majoritairement CC BY 4.0).

---

## 🙏 Remerciements

- [data.europa.eu](https://data.europa.eu) — pour l'API publique
- [Etalab](https://www.etalab.gouv.fr) — pour l'ouverture des données
- [DSFR](https://www.systeme-de-design.gouv.fr) — pour le design system de l'État
- [Shields.io](https://shields.io) — pour les badges
- [Python](https://python.org) — pour le proxy standard

---

<div align="center">

**⭐ Si ce projet t'est utile, mets-lui une étoile ! ⭐**

[Signaler un bug](https://github.com/gunout/catalogue-monitor-ue/issues) · [Proposer une fonctionnalité](https://github.com/gunout/catalogue-monitor-ue/issues) · [Contribuer](https://github.com/gunout/catalogue-monitor-ue/pulls)

Fait avec 🇪🇺 pour les données publiques européennes.

</div>

---

<div align="center">

### 🇫🇷 Gunout · 2026

![Made in France](https://img.shields.io/badge/Made_in-France-002395?style=flat-square&labelColor=FFFFFF&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5MDAgNjAwIj48cmVjdCB3aWR0aD0iOTAwIiBoZWlnaHQ9IjYwMCIgZmlsbD0iIzAwMjM5NSIvPjxyZWN0IHdpZHRoPSI5MDAiIGhlaWdodD0iNDAwIiB5PSIxMDAiIGZpbGw9IiNmZmYiLz48cmVjdCB3aWR0aD0iOTAwIiBoZWlnaHQ9IjIwMCIgeT0iNDAwIiBmaWxsPSIjZWQyOTM5Ii8+PC9zdmc+)
![GitHub](https://img.shields.io/badge/GitHub-gunout-181717?style=flat-square&logo=github&logoColor=white)
![Year](https://img.shields.io/badge/2026-ED2939?style=flat-square&labelColor=FFFFFF)

<sub>© 2026 <strong>Gunout</strong> — Tous droits réservés.</sub>

</div>
