# Custom-validation-with-pydantic

#### Das braucht ihr:

fastapi = pip install "fastapi[all]"

pydantic = pip install pydantic

uvicorn = pip install uvicorn

for pure python uvicorn = pip install uvicorn [standard]

## Was ist das eigentlich?

Custom validaters sind class methods, welche für UserModels benutzt werden, um diese auf gewisse validators v zu prüfen,
ob diese richtig oder falsch erscheinen. 

### Wie programmiere ich es?

1. Erstmals muss von pydantic BaseModel, ValidationError und validator importiert werden. Dazu auch von fastapi... FastAPI
2. 

#### Placeholder