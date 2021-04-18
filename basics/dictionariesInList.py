aliens = []

for newAlien in range(25):
    newAlien = {"color": "green", "points": newAlien + 5}
    aliens.append(newAlien)

for alien in aliens[-5:]: # making last 5 aliens super aliens
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["points"] = alien["points"] + 100

for alien in aliens:
    print(alien)