# textadventure-engine

Un motore minimale, estensibile e testato per creare giochi di avventura testuale in Python.  
Progettato per essere semplice da usare, facile da estendere e adatto sia a piccoli progetti personali che a librerie più complesse.

---

## ✨ Caratteristiche principali

- Struttura flat semplice da comprendere
- Classi base per:
  - GameEngine — ciclo principale del gioco
  - Scene — singola scena del gioco
  - Parser — interpretazione dei comandi
  - State — stato condiviso del gioco
- Test automatici tramite pytest
- Compatibile con Python 3.10+
- Installabile direttamente da GitHub

---

## 📦 Installazione

### Installazione da GitHub
```
pip install git+https://github.com/Giovanni6741/TextAdventureEngine.git
```
### Installazione locale (sviluppo)
```
pip install .[dev]
```
---

## 🧱 Struttura del progetto
```
textadventure-engine/
│   pyproject.toml
│   README.md
│
├── src/
│   └── textadventure/
│       ├── engine.py
│       ├── parser.py
│       ├── scene.py
│       ├── state.py
│       └── __init__.py
│
└── tests/
    ├── test_engine.py
    └── test_scene.py
```
---

## 🚀 Come iniziare

### 1. Crea una scena
```
from textadventure import Scene

class Intro(Scene):
    def enter(self, state, parser):
        print("Benvenuto nel gioco!")
        command = input("> ")
        return parser.parse(command, state)
```
### 2. Avvia il motore
```
from textadventure import GameEngine, Parser, State
from intro import Intro

engine = GameEngine(Intro(), State(), Parser())
engine.run()
```
---

## 🧪 Test

Per eseguire i test:
```
pytest
```
I test verificano:
- comportamento della classe Scene
- ciclo del motore GameEngine

---

## ⚙️ Workflow GitHub Actions

Il repository include un workflow che esegue automaticamente i test ad ogni push:
```
name: Run Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.10"
      - run: pip install .[dev]
      - run: pytest -q
```
---

## 📜 Licenza

Questo progetto è distribuito sotto licenza Apache 2.0.

---

## 🤝 Contribuire

Le pull request sono benvenute.  
Per modifiche importanti, apri prima una issue per discutere cosa vorresti cambiare.

---

## 📬 Contatti

Autore: Giovanni  
Progetto: textadventure-engine
