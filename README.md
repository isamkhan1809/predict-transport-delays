<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,8,15&height=200&section=header&text=Transport%20Delays&fontSize=72&fontColor=fff&animation=twinkling&fontAlignY=35&desc=Weather.%20Events.%20Rush%20Hour.%20Predicted.&descAlignY=60&descSize=20" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-4FC3F7?style=for-the-badge&logo=python&logoColor=white&labelColor=0D0D0D)](https://python.org)
[![XGBoost](https://img.shields.io/badge/XGBoost-R²%3D0.70-4FC3F7?style=for-the-badge&logoColor=white&labelColor=0D0D0D)](https://xgboost.readthedocs.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-3%20Models-4FC3F7?style=for-the-badge&logo=scikit-learn&logoColor=white&labelColor=0D0D0D)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-4FC3F7?style=for-the-badge&labelColor=0D0D0D)](LICENSE)

<br/>

<a href="https://github.com/isamkhan1809/predict-transport-delays">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=22&pause=1000&color=4FC3F7&center=true&vCenter=true&width=700&lines=XGBoost+Delay+Predictor+%E2%80%94+R%C2%B2+%3D+0.70;Rain+%2B+Rush+Hour+%3D+Maximum+Signal;Weather+%C2%B7+Events+%C2%B7+Time+of+Day;Predict+Delays+Before+They+Happen." alt="Typing SVG" />
</a>

</div>

---

<br/>

<div align="center">

```
  ╔══════════════════════════════════════════════════════════════╗
  ║                                                              ║
  ║   Every morning, millions board buses and trains.            ║
  ║   Every delay ripples — missed meetings, late arrivals.      ║
  ║                                                              ║
  ║       This model sees the delay coming before it does.       ║
  ║                                                              ║
  ╚══════════════════════════════════════════════════════════════╝
```

</div>

<br/>

## `>_ The Story`

> *A rainstorm hits during rush hour. A concert ends at 10pm. Visibility drops to 2km on a Friday.*
>
> *Individually, these signals are noise. Combined, they predict delays with an R² of 0.70 and an RMSE of 4.6 minutes.*
>
> *This project builds that model — from raw weather and event data, through three competing algorithms, to a final XGBoost regressor that outperforms the baseline by 70%.*

<br/>

## `>_ Predictions`

<table>
<tr>
<td width="50%">

**Conditions in:**
```
precipitation:  8mm
temperature:    7°C
visibility:     2.1km
is_rush_hour:   1
is_event:       1 (concert)
hour:           18
```

</td>
<td width="50%">

**Delay out:**
```
Linear Regression:  8.2 min  (R² 0.41)
Random Forest:      6.1 min  (R² 0.63)
XGBoost ✦:          5.4 min  (R² 0.70)

Predicted delay: 5.4 minutes
```

</td>
</tr>
</table>

<br/>

## `>_ The Pipeline`

```
┌─────────────────────────────────────────────────────────────┐
│                 DELAY PREDICTION PIPELINE                   │
│                                                             │
│  WEATHER              TIME                 EVENTS           │
│  ─────────            ────────             ──────           │
│  Precipitation ─┐     Rush hour   ─┐       Concert ─┐       │
│  Temperature    │     Hour of day  │       Sports   │       │
│  Wind speed     ├───▶ Day of week  ├──────▶ None    ├──────▶│
│  Visibility     │     Weekend      │                │       │
│                 └──────────────────┘────────────────┘       │
│                                   │                         │
│                                   ▼                         │
│              ┌────────────────────────────────────┐         │
│              │  Linear Regression   R² ~ 0.41     │         │
│              │  Random Forest       R² ~ 0.63     │         │
│              │  XGBoost ✦           R² ~ 0.70     │         │
│              └────────────────────────────────────┘         │
└─────────────────────────────────────────────────────────────┘
```

<br/>

## `>_ Model Performance`

<div align="center">

| Model | RMSE | MAE | R² |
|---|---|---|---|
| Linear Regression | ~6.8 min | ~5.2 min | ~0.41 |
| Random Forest | ~5.1 min | ~3.9 min | ~0.63 |
| **XGBoost** ✦ | **~4.6 min** | **~3.5 min** | **~0.70** |

</div>

<br/>

## `>_ Get Running`

```bash
# Clone
git clone https://github.com/isamkhan1809/predict-transport-delays.git
cd predict-transport-delays

# Install
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Launch notebook (synthetic data auto-generated)
jupyter notebook transport_delay_prediction.ipynb
```

<br/>

## `>_ Tech Stack`

<div align="center">

| Layer | Technology |
|---|---|
| **Modelling** | scikit-learn, XGBoost |
| **Data** | pandas, numpy |
| **Visualisation** | matplotlib, seaborn |
| **Notebook** | Jupyter |

</div>

<br/>

## `>_ Project Structure`

```
predict-transport-delays/
├── transport_delay_prediction.ipynb  ← Full pipeline
├── data/                             ← Optional real dataset
└── requirements.txt
```

<br/>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,8,15&height=120&section=footer&animation=twinkling" width="100%"/>

<br/>

*Every minute counts. Predict it before it happens.*
*Weather · Events · Rush Hour — modelled and forecasted.*

<br/>

[![GitHub](https://img.shields.io/badge/github-isamkhan1809-4FC3F7?style=for-the-badge&logo=github&logoColor=white&labelColor=0D0D0D)](https://github.com/isamkhan1809)

</div>
