import os
from flask import Flask, jsonify, request

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

members = [
    {"id": 1, "name": "Aarav Sharma", "plan": "Gold", "active": True},
    {"id": 2, "name": "Priya Nair", "plan": "Platinum", "active": True},
]

workouts = [
    {"id": 1, "title": "HIIT Cardio", "duration_mins": 30},
    {"id": 2, "title": "Strength Training", "duration_mins": 45},
]

@app.route("/")
def home():
    return jsonify({
        "service": "ACEest Fitness & Gym API",
        "version": APP_VERSION,
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "version": APP_VERSION}), 200

@app.route("/members", methods=["GET", "POST"])
def handle_members():
    if request.method == "POST":
        data = request.get_json()
        if not data or "name" not in data:
            return jsonify({"error": "Name is required"}), 400
        new_member = {
            "id": len(members) + 1,
            "name": data["name"],
            "plan": data.get("plan", "Standard"),
            "active": True
        }
        members.append(new_member)
        return jsonify(new_member), 201
    return jsonify(members), 200

@app.route("/workouts", methods=["GET"])
def get_workouts():
    return jsonify(workouts), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
