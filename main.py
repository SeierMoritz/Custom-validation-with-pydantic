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
    def clan_role_there(cls, v):
        if v not in ['Member', 'Elder', 'Vize-Leader']:
            raise ValueError('must contain the role')
        return v

    @validator('favourite_truppe')
    def favourite_troupe_needs_to_match(cls, v, values, **kwargs):
        if 'favourite_truppe' in values and v != values['favourite_truppe']:
            raise ValueError('Unsympathisch')
        return v



user = UserModel(
    name='Moritz Seier',
    username='ProgrammierenMemo',
    password1='12345789',
    password2='246810',
    clan_role='Elder',
    favourite_truppe='giant'
)
print(user)
#> name='Moritz Seier' username='ProgrammierenMemo' password1='123456789' password2='13579' clan_role="Elder" favourite_truppe="Lumberjack"

try:
    UserModel(
        name='Moritz Seier',
        username='ProgrammierenMemo',
        password1='123456789',
        password2='13579',
        clan_role='Elder',
        favourite_truppe='lumberjack'
    )
except ValidationError as e:
    print(e)
    """
    Validation errors for UserModel.
    Try again.
    """