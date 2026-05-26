# Predict Public Transport Delays Using Weather & Events

A machine learning project that predicts public transportation delays based on weather conditions and city events. This project explores how temperature, precipitation, wind speed, visibility, and local events influence bus/train delays across different routes and times of day.

---

## Project Overview

Public transport delays cost cities millions in productivity losses each year. By modeling the relationship between environmental factors (weather) and logistical factors (events, rush hours) with observed delays, transit authorities can proactively alert passengers and adjust schedules.

**Models trained:**
- Linear Regression (baseline)
- Random Forest Regressor
- XGBoost Regressor

**Target variable:** `delay_minutes` — the number of minutes a transport service is delayed.

**Key findings:**
- Weather features (precipitation, visibility) and time-of-day features (rush hour, hour) are the strongest predictors of delay.
- XGBoost outperforms the other models with the lowest RMSE and highest R² score.
- Events add a moderate but consistent delay signal, especially for large events.
- Rush hour combined with rain produces the highest average delays.

---

## Project Structure

```
predict-transport-delays/
├── data/                              # Place downloaded Kaggle CSV here
├── transport_delay_prediction.ipynb   # Main analysis and modeling notebook
├── requirements.txt                   # Python dependencies with pinned versions
└── README.md                          # This file
```

---

## Setup Instructions

### 1. Clone / download the project

```bash
git clone <repo-url>
cd predict-transport-delays
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch Jupyter Notebook

```bash
jupyter notebook
```

Then open `transport_delay_prediction.ipynb` in the browser tab that appears.

---

## Dataset Download Instructions (Kaggle)

The notebook uses **synthetic data by default** so it runs without any downloads. To use the real dataset:

1. Create a free account at [https://www.kaggle.com](https://www.kaggle.com)
2. Go to the dataset page:
   [Public Transport Delays with Weather and Events](https://www.kaggle.com/datasets/khushikyad001/public-transport-delays-with-weather-and-events)
3. Click **Download** and unzip the CSV file into the `data/` folder.
4. In Cell 3 of the notebook, replace the synthetic data generation block with:

```python
df = pd.read_csv('data/<filename>.csv')
```

5. Adjust column names in subsequent cells if they differ from the synthetic schema.

---

## Feature Schema

| Column | Type | Description |
|---|---|---|
| `date` | datetime | Calendar date of the service |
| `time` | str | Scheduled departure time (HH:MM) |
| `route_id` | str | Transit route identifier |
| `delay_minutes` | float | Target: minutes delayed (0 = on time) |
| `temperature` | float | Temperature in Celsius |
| `precipitation` | float | Rainfall in mm |
| `wind_speed` | float | Wind speed in km/h |
| `visibility` | float | Visibility in km |
| `is_event` | int | 1 if a city event is occurring nearby |
| `event_type` | str | Type of event (sports, concert, none, etc.) |
| `day_of_week` | int | 0 = Monday … 6 = Sunday |
| `hour` | int | Hour of scheduled departure (0–23) |
| `is_rush_hour` | int | 1 if hour is 7–9 or 17–19 |
| `is_weekend` | int | 1 if Saturday or Sunday |

---

## Results Summary

| Model | RMSE | MAE | R² |
|---|---|---|---|
| Linear Regression | ~6.8 | ~5.2 | ~0.41 |
| Random Forest | ~5.1 | ~3.9 | ~0.63 |
| XGBoost | ~4.6 | ~3.5 | ~0.70 |

*(Results are from the synthetic dataset and will vary slightly on each run due to random seed.)*

---

## Tech Stack

- **Python 3.10+**
- **pandas** — data manipulation
- **numpy** — numerical operations
- **scikit-learn** — preprocessing, Linear Regression, Random Forest, metrics
- **xgboost** — gradient boosting model
- **matplotlib / seaborn** — visualizations
- **jupyter / notebook** — interactive development environment

---

## License

MIT License. Dataset sourced from Kaggle (see link above) under its respective license.
