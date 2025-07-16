import json
import random

def load_fighter(path):
  with open(path, "r") as f:
    return json.load(f)

def compute_score(fighter):
  stats = fighter["stats"]
  base = (
    stats["striking"] * 0.2 +
    stats["grappling"] * 0.2 +
    stats["takedown_defense"] * 0.1 +
    stats["cardio"] * 0.2 +
    stats["fight_iq"] * 0.3 +
  )
  return base + random.uniform(-5, 5) # randomizer (normalement)

def simulate_fight(f1, f2):
  score1 = compute_score(f1)
  score2 = compute_score(f2)
  winner = f1 if score1 > score2 else f2
  return {
    "winner": winner["name"],
    "score1": round(score1, 2),
    "score2": round(score2, 2)
  }
  
