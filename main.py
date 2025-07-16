from engine.simulator import load_fighter, simulate_fight

f1 = load_fighter("fighters/jon_jones.json")
f2 = load_fighter("fighters/khabib.json")

result = simulate_fights(f1, f2)

print(f"\n {result['winner']} wins the fight!")
print(f"Scores - {f1['name']}: {rsult['score1']} | {f2['name']}: {result['score2']}\n")
