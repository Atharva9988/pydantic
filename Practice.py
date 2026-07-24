from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Player(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='give the name of the patient in less than 50 chars', examples=['Shreyash','Harshal'])] 
    email:EmailStr
    linkedin: AnyUrl
    age: int = Field(gt=0, lt=120)
    game: str
    role: str
    weight: float =Field(gt=0)
    playing_status: Annotated[bool, Field(default=None, description='Is the player playing today')]
    injuries: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str,str]

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

player_info= {'name':'Atharva','email': 'shreyash@gmail.com','linkedin':'http://linkedin.com', 'age':20, 'game': 'Cricket', 'role':'Lefthand Batsman and Righthand Offspin Bowler', 'weight':70.5, 'playing_status':True, 'injuries':['calf','muscle pull'], 'contact_details':{'profile':'Atharva.being_private', 'phone':'9828489796'}}

player1 = Player(**player_info)

update_player_data(player1)