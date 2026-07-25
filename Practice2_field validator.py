from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Player(BaseModel):
    name: str
    email:EmailStr 
    linkedin: AnyUrl
    age: int
    game: str
    role: str
    weight: float
    playing_status: bool
    injuries: List[str]
    contact_details: Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['icc.com','bcci.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value

    @field_validator('name')
    @classmethod
    def generalize_name(cls, value):
        return value.upper()

    @field_validator('age', mode='before')
    @classmethod
    def age_criteria(cls,value):
        if 10 < value < 50:
            return value
        else:
            raise ValueError('Age should be in between 0 and 50') 

def insert_player_data(player:Player):

    print(player.name)
    print(player.age)
    print(player.game)
    print(player.injuries)
    print('inserted')

def update_player_data (player:Player):

    print(player.name)
    print(player.email)
    print(player.linkedin)
    print(player.age)
    print(player.game)
    print(player.role)
    print(player.weight)
    print(player.playing_status)
    print(player.injuries)
    print(player.contact_details)
    print('Inserted')

player_info= {'name':'Atharva','email': 'shreyash@bcci.com','linkedin':'http://linkedin.com', 'age':20, 'game': 'Cricket', 'role':'Lefthand Batsman and Righthand Offspin Bowler', 'weight':70.5, 'playing_status':True, 'injuries':['calf','muscle pull'], 'contact_details':{'profile':'Atharva.being_private', 'phone':'9828489796'}}

player1 = Player(**player_info)

update_player_data(player1)