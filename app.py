import numpy as np
import pandas as pd
from flask import Flask, jsonify, render_template, request
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# ── Global state ──────────────────────────────────────────────────────────────
model = None
feature_names = []
feature_importances = []
dataset_stats = {}


# ── Synthetic data generation & training ─────────────────────────────────────
def generate_dataset(n=10_000, seed=42):
    rng = np.random.default_rng(seed)

    temperature = rng.uniform(-10, 45, n)
    precipitation = rng.exponential(3, n).clip(0, 50)
    wind_speed = rng.exponential(15, n).clip(0, 100)
    visibility = rng.uniform(0, 20, n)
    is_event = rng.integers(0, 2, n)
    event_type_encoded = np.where(is_event, rng.integers(1, 5, n), 0)
    hour = rng.integers(0, 24, n)
    day_of_week = rng.integers(0, 7, n)
    is_rush_hour = ((hour >= 7) & (hour <= 9) | (hour >= 17) & (hour <= 19)).astype(int)
    is_weekend = (day_of_week >= 5).astype(int)

    # Delay formula with realistic relationships
    base_delay = (
        np.maximum(0, (precipitation - 5) * 0.8)        # rain adds delay
        + np.maximum(0, (wind_speed - 30) * 0.3)         # high wind
        + np.maximum(0, (10 - visibility) * 1.2)         # low visibility
        + is_rush_hour * rng.uniform(3, 10, n)           # rush hour
        + is_event * rng.uniform(4, 12, n)               # events nearby
        + event_type_encoded * 1.5                       # event type severity
        + np.where(temperature < 0, (-temperature) * 0.4, 0)   # frost/ice
        + np.where(temperature > 35, (temperature - 35) * 0.5, 0)  # heat
        + rng.normal(0, 2, n)                            # noise
    )
    delay_minutes = np.maximum(0, base_delay).round(1)

    return pd.DataFrame({
        "temperature": temperature,
        "precipitation": precipitation,
        "wind_speed": wind_speed,
        "visibility": visibility,
        "is_event": is_event,
        "event_type_encoded": event_type_encoded,
        "hour": hour,
        "day_of_week": day_of_week,
        "is_rush_hour": is_rush_hour,
        "is_weekend": is_weekend,
        "delay_minutes": delay_minutes,
    })


def train_model():
    global model, feature_names, feature_importances, dataset_stats

    print("Generating synthetic dataset …")
    df = generate_dataset()

    feature_names = [
        "temperature", "precipitation", "wind_speed", "visibility",
        "is_event", "event_type_encoded", "hour", "day_of_week",
        "is_rush_hour", "is_weekend",
    ]
    X = df[feature_names]
    y = df["delay_minutes"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Training Random Forest …")
    rf = RandomForestRegressor(
        n_estimators=100,
        max_depth=12,
        min_samples_leaf=5,
        n_jobs=-1,
        random_state=42,
    )
    rf.fit(X_train, y_train)
    model = rf

    importances = rf.feature_importances_
    feature_importances = sorted(
        [{"feature": f, "importance": round(float(i), 4)}
         for f, i in zip(feature_names, importances)],
        key=lambda x: x["importance"],
        reverse=True,
    )

    # Dataset stats
    on_time = (df["delay_minutes"] < 5).sum()
    dataset_stats = {
        "avg_delay": round(float(df["delay_minutes"].mean()), 1),
        "max_delay": round(float(df["delay_minutes"].max()), 1),
        "on_time_pct": round(100 * on_time / len(df), 1),
        "routes_count": 42,  # realistic-looking fixed value
    }
    print("Model ready.")


# ── Routes ────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)

    try:
        row = pd.DataFrame([{
            "temperature": float(data.get("temperature", 20)),
            "precipitation": float(data.get("precipitation", 0)),
            "wind_speed": float(data.get("wind_speed", 10)),
            "visibility": float(data.get("visibility", 10)),
            "is_event": int(data.get("is_event", 0)),
            "event_type_encoded": int(data.get("event_type_encoded", 0)),
            "hour": int(data.get("hour", 12)),
            "day_of_week": int(data.get("day_of_week", 0)),
            "is_rush_hour": int(data.get("is_rush_hour", 0)),
            "is_weekend": int(data.get("is_weekend", 0)),
        }])

        # Individual tree predictions for confidence interval
        tree_preds = np.array([t.predict(row)[0] for t in model.estimators_])
        pred = float(np.mean(tree_preds))
        low = float(np.percentile(tree_preds, 10))
        high = float(np.percentile(tree_preds, 90))

        if pred < 5:
            severity = "On Time"
        elif pred < 15:
            severity = "Minor Delay"
        elif pred < 30:
            severity = "Moderate Delay"
        else:
            severity = "Major Delay"

        return jsonify({
            "delay_minutes": round(pred, 1),
            "confidence_low": round(max(0, low), 1),
            "confidence_high": round(high, 1),
            "severity": severity,
        })
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400


@app.route("/api/feature-importance")
def feature_importance():
    return jsonify(feature_importances)


@app.route("/api/stats")
def stats():
    return jsonify(dataset_stats)


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    train_model()
    app.run(debug=True, port=5000)
