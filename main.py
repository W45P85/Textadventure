name = input("Wie lautet dein Name? ")
print(f"Willkommen {name}. Ich lade dich auf eine spannende Reise voller Gefahren und aufregender Entdeckungen in Glückstadt ein.")

answer = input("Du befindest dich mitten auf sperrlich beleuchteten Marktplatz. In welche Richtung möchtest du den Marktplatz verlassen? (Rechts/Links) ").lower()

if answer == "links":
    answer = input("Du verlässt den Marktplatz in Richtung der Nübelstraße. Dort begegnest du dem wütenden Fischverkäufer Johannes. Willst du den Kampf aufnehmen oder fliehen? (Kämpfen/Flucht) ").lower()
    if answer == "kämpfen":
        print("Du kämpfst heldenhaft und besiegst den Johannes den Fischverkäufer mit Leichtigkeit.")
    elif answer == "flucht":
        print("Du Feigling bist abgehauen. Allerdings musstest du so lange rennen, dass du dich vollkommen verlaufen hast. Du hast verloren!")
    else:
        print("Falsche Eingabe. Du hast verloren!")
            
        
elif answer =="rechts":
    answer = input("Du verlässt den Marktplatz in Richtung Rathaus. Dort begegnest du dem Bürgermeister. Er sieht friedlich aus, hat dich aber noch nicht entdeckt. Möchtest du dich an ihm vorbei schleichen oder suchst du den direkten Kontakt? (schleichen/ansprechen) ").lower()
    if answer == "schleichen":
        print("Du schleichst dich an dem Bürgermeister vorbei. Das schein eine gute Wahl gewesen zu sein, denn irgendetwas stimmt mit dem Bürgermeister nicht...")
    elif answer == "ansprechen":
        print("Der Bürgermeister sieht auf einmal nicht meht so freundlich aus und verfällt in Raserei. Bewaffnet mit einem Messer rennt er schreiend auf dich zu und tötet dich.")
    else:
        print("Falsche Eingabe. Du hast verloren!")
else:
    print("Falsche Eingabe. Du hast verloren!")
    quit()
    
print("Danke fürs spielen. :)")
