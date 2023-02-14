# Custom-validation-with-pydantic

#### Das braucht ihr:

fastapi = pip install "fastapi[all]"

pydantic = pip install pydantic

uvicorn = pip install uvicorn

for pure python uvicorn = pip install uvicorn [standard]

## Was ist das eigentlich?

Custom validaters sind class methods, welche für UserModels benutzt werden, um diese auf gewisse validators v zu prüfen,
ob diese richtig/falsch erscheinen oder mit dem originalen Wert matchen und noch vieles mehr.
Zusammengefasst: Sorgt dafür, dass die eingegeben Daten valide sind und sich Nutzer mit mehreren Sicherheitsvorkehrungen
einloggen können.

### Wie programmiere ich es?

1. Erstmals muss von pydantic BaseModel, ValidationError und validator importiert werden. Dazu auch von fastapi... FastAPI
2. Danach bleibt es offen für euch persönlich wie ihr es wollt, man kann verschiedene "custom" validators in einem UserModel einfügen, welche später durch str definiert werden.
3. Nun muss aber auch eingefügt werden, was die requirements sind, dafür, dass die validators was ausspucken. Hier können es matching validators sein, true/false, etc.
4. Danach (geht auch davor) sollte man seine eigenen gewollten Werte einfügen, auf welche geprüft werden muss.
5. Fast am Ende fügt man die UserModels ein, welche durch die Validators überprüft werden.
6. Die Fehlermeldung verfassen, woran ich selbst auch noch sitze.

#### Sonstiges:

Nix

#### Anwendungsschwierigkeit:

Easy, aber kann daran liegen, dass ich nichts checke

##### Aktuelle Probleme

* Nur Favourite Truppe
* Und grafische Darstellung