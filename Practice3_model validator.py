from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
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
    injuries: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age < 18 and 'emergency' not in model.contact_details:
            raise ValueError('Players younger than 18 must have an emergency contact')
        return model

def insert_player_data (player:Player):

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

player_info= {'name':'Atharva','email': 'shreyash@gmail.com','linkedin':'http://linkedin.com', 'age':18, 'game': 'Cricket', 'role':'Lefthand Batsman and Righthand Offspin Bowler', 'weight':70.5, 'playing_status':True, 'injuries':['calf','muscle pull'], 'contact_details':{'profile':'Atharva.being_private', 'phone':'9828489796'}}

player1 = Player(**player_info)

update_player_data(player1)