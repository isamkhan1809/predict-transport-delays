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

### *Weather. Events. Rush Hour. The Delay Engine Sees It All.*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![XGBoost](https://img.shields.io/badge/XGBoost-Champion-F7931E?style=for-the-badge)](https://xgboost.readthedocs.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

---

> **A machine learning project that predicts public transport delays from weather conditions, city events, and time-of-day patterns — reaching R² = 0.70 with XGBoost.**

</div>

---

## ◈ Why Delays Happen — And How We Predict Them

```
┌─────────────────────────────────────────────────────────────────────┐
│                     DELAY PREDICTION MODEL                          │
│                                                                     │
│   WEATHER SIGNALS         TIME SIGNALS          EVENT SIGNALS       │
│   ──────────────          ────────────          ─────────────       │
│   Precipitation ──┐       Rush hour    ──┐      Concert    ──┐      │
│   Temperature     │       Hour of day   │      Sports      │       │
│   Wind speed      ├──→    Day of week   ├──→   None         ├──→   │
│   Visibility      │       Weekend flag  │                   │       │
│                   │                     │                   │       │
│                   └─────────────────────┴───────────────────┘       │
│                                   │                                 │
│                                   ▼                                 │
│            ┌──────────────────────────────────────┐                │
│            │  Linear Regression  (baseline, R²~0.41) │              │
│            │  Random Forest      (strong,   R²~0.63) │              │
│            │  XGBoost ✦          (best,     R²~0.70) │              │
│            └──────────────────────────────────────┘                │
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

> **Precipitation and visibility** are the strongest weather predictors of delay.

> **Rush hour combined with rain** produces the highest average delays — a compounding effect.

> **Events** add a moderate but consistent delay signal, especially large events.

> **XGBoost captures non-linear interactions** (e.g. rain matters more during rush hour) that Linear Regression misses entirely.

---

## ◈ Feature Schema

| Feature | Type | Description |
|---|---|---|
| `temperature` | float | Celsius |
| `precipitation` | float | mm of rainfall |
| `wind_speed` | float | km/h |
| `visibility` | float | km |
| `is_event` | int | City event nearby (0/1) |
| `event_type` | str | sports / concert / none |
| `hour` | int | Departure hour (0–23) |
| `is_rush_hour` | int | 7–9 or 17–19 (0/1) |
| `is_weekend` | int | Saturday/Sunday (0/1) |
| `day_of_week` | int | 0=Mon … 6=Sun |
| `delay_minutes` | float | **Target variable** |

---

## ◈ Quick Start

```bash
# 1. Clone
git clone https://github.com/isamkhan1809/predict-transport-delays.git
cd predict-transport-delays

# 2. Virtual environment
python -m venv venv && source venv/bin/activate

# 3. Install
pip install -r requirements.txt

# 4. Launch notebook (synthetic data runs automatically)
jupyter notebook transport_delay_prediction.ipynb
```

### With Real Data

Download from [Kaggle: Public Transport Delays](https://www.kaggle.com/datasets/khushikyad001/public-transport-delays-with-weather-and-events) → place CSV in `data/` → update Cell 3.

---

## ◈ Project Structure

```
predict-transport-delays/
├── transport_delay_prediction.ipynb  ← Full pipeline
├── data/                             ← Place CSV here
├── requirements.txt
└── README.md
```

---

## ◈ Tech Stack

| Layer | Technology |
|---|---|
| Modelling | scikit-learn, XGBoost |
| Data | pandas, numpy |
| Visualisation | matplotlib, seaborn |
| Notebook | Jupyter |

---

<div align="center">

**Every minute counts. Predict it before it happens.**

*MIT License*

</div>
