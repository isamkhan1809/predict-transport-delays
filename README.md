<div align="center">

```
████████╗██████╗  █████╗ ███╗   ██╗███████╗██████╗  ██████╗ ██████╗ ████████╗
╚══██╔══╝██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
   ██║   ██████╔╝███████║██╔██╗ ██║███████╗██████╔╝██║   ██║██████╔╝   ██║
   ██║   ██╔══██╗██╔══██║██║╚██╗██║╚════██║██╔═══╝ ██║   ██║██╔══██╗   ██║
   ██║   ██║  ██║██║  ██║██║ ╚████║███████║██║     ╚██████╔╝██║  ██║   ██║
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝

            ██████╗ ███████╗██╗      █████╗ ██╗   ██╗███████╗
            ██╔══██╗██╔════╝██║     ██╔══██╗╚██╗ ██╔╝██╔════╝
            ██║  ██║█████╗  ██║     ███████║ ╚████╔╝ ███████╗
            ██║  ██║██╔══╝  ██║     ██╔══██║  ╚██╔╝  ╚════██║
            ██████╔╝███████╗███████╗██║  ██║   ██║   ███████║
            ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝
```

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=4FC3F7&center=true&vCenter=true&width=700&lines=Weather.+Events.+Rush+Hour.+The+Engine+Sees+It+All+%F0%9F%9A%8C;XGBoost+Delay+Predictor+%E2%80%94+R%C2%B2+%3D+0.70;Rain+%2B+Rush+Hour+%3D+Maximum+Delay+Signal;Predict+Delays+Before+They+Happen+%E2%8F%B1%EF%B8%8F" alt="Typing SVG" />

<img src="https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif" width="360" />

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![XGBoost](https://img.shields.io/badge/XGBoost-Champion-F7931E?style=for-the-badge)](https://xgboost.readthedocs.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

> **A machine learning project that predicts public transport delays from weather conditions, city events, and time-of-day patterns — reaching R² = 0.70 with XGBoost.**

</div>

---

## ◈ Why Delays Happen — And How We Predict Them

```
┌─────────────────────────────────────────────────────────────────────┐
│                     DELAY PREDICTION MODEL                          │
│                                                                     │
│   WEATHER SIGNALS         TIME SIGNALS          EVENT SIGNALS       │
│   Precipitation ──┐       Rush hour    ──┐      Concert    ──┐      │
│   Temperature     │       Hour of day   │      Sports      │       │
│   Wind speed      ├──→    Day of week   ├──→   None         ├──→   │
│   Visibility      │       Weekend flag  │                   │       │
│                   └─────────────────────┴───────────────────┘       │
│                                   │                                 │
│            Linear Regression  (baseline, R²~0.41)                   │
│            Random Forest      (strong,   R²~0.63)                   │
│            XGBoost ✦          (best,     R²~0.70)                   │
│                                   │                                 │
│                        Predicted delay_minutes                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## ◈ Model Performance

| Model | RMSE | MAE | R² |
|---|---|---|---|
| Linear Regression | ~6.8 min | ~5.2 min | ~0.41 |
| Random Forest | ~5.1 min | ~3.9 min | ~0.63 |
| **XGBoost** ✦ | **~4.6 min** | **~3.5 min** | **~0.70** |

---

## ◈ Key Findings

> **Precipitation + rush hour** = highest average delays — a compounding effect XGBoost captures.

> **Visibility** is the strongest individual weather predictor.

> **Events** add a consistent delay signal, especially large concerts and sports.

---

## ◈ Feature Schema

| Feature | Description |
|---|---|
| `temperature` | Celsius |
| `precipitation` | mm of rainfall |
| `visibility` | km |
| `is_rush_hour` | 7–9 or 17–19 (0/1) |
| `is_event` | City event nearby (0/1) |
| `delay_minutes` | **Target variable** |

---

## ◈ Quick Start

```bash
git clone https://github.com/isamkhan1809/predict-transport-delays.git
cd predict-transport-delays
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
jupyter notebook transport_delay_prediction.ipynb
# Synthetic data runs automatically — no download needed
```

---

## ◈ Project Structure

```
predict-transport-delays/
├── transport_delay_prediction.ipynb
├── data/
├── requirements.txt
└── README.md
```

---

<div align="center">

**Every minute counts. Predict it before it happens.**

*MIT License*

<br/>

Interested in smart city tech, public transport systems, or ML for urban data?<br/>
Let's connect — built by <a href="https://github.com/isamkhan1809">Isam Khan</a> &nbsp;|&nbsp;
<a href="https://linkedin.com/in/isam-khan-3a1260292"><img src="https://img.shields.io/badge/-LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white&labelColor=000000"/></a>
<a href="https://isamkhan.com"><img src="https://img.shields.io/badge/-isamkhan.com-00D9FF?style=flat-square&logo=googlechrome&logoColor=white&labelColor=000000"/></a>

</div>
