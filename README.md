# FightIQ
FightIQ is a MMA fight simulator (without visual support because "flemme"). It uses fighter profiles with basic states and simulates outcomes using weigthed scoring and a bit of randomness.

## How it works
- Each fighter is defined by a JSON file ('fighters/') with key stats
- The engine ('engine/simulator.py') computes a fight score for each fighter
- The winner is the one with the highest score, with a random factor to simulate unpredictability

## Project Structure 
fightiq/
  fighters/
    jon_jones.json
    khabib.json
    etc...
  engine/
    simulator.py
    __init__.py
  main.py
  README.md
  requirements.txt
