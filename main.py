from fastapi import FastAPI
from pydantic import BaseModel, ValidationError, validator

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Werden Sie gesund."}

class UserModel(BaseModel):
    name: str
    username: str
    password1: str
    password2: str
    clan_role: str
    favourite_truppe: str

    @validator('name')
    def name_must_contain_space(cls, v):
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title()

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match')
        return v

    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v

    @validator('clan_role')
    def clan_role_needs_to_be_elder(cls,v):
        if 'clan_role' is 'Elder':
            return v
        else:
            return 'Not high enough'

    @validator('favourite_leviathan')
    def favourite_troupe_needs_to_be_giant(cls,v):
        if 'favourite_truppe' is 'giant':
            return v
        if 'favourite_truppe' is 'bowler':
            return 'naja'
        else:
            return 'no'



user = UserModel(
    name='Moritz Seier',
    username='ProgrammierenMemo',
    password1='12345789',
    password2='246810',
    clan_role='Elder',
    favourite_truppe='Lumberjack'
)
print(user)
#> name='Moritz Seier' username='ProgrammierenMemo' password1='123456789' password2='13579' clan_role="Elder" favourite_truppe="Lumberjack"

try:
    UserModel(
        name='Moritz',
        username='ProgrammierenMemo',
        password1='123456789',
        password2='13579',
        clan_role='Elder',
        favourite_leviathan="Frostworm"
    )
except ValidationError as e:
    print(e)
    """
    2 validation errors for UserModel
    name
      must contain a space (type=value_error)
    password2
      passwords do not match (type=value_error)
    """