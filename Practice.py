from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional

class Player(BaseModel):

    name: str
    email:EmailStr
    linkedin: AnyUrl
    age: int
    game: str
    role: str
    weight: float
    playing_status: bool
    injuries: Optional[List[str]] = None
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

player_info= {'name':'Atharva','email': 'yuv@gmail.com', 'age':20, 'game': 'Cricket', 'role':'Lefthand Batsman and Righthand Offspin Bowler', 'weight':70.5, 'playing_status':True, 'injuries':['calf','muscle pull'], 'contact_details':{'profile':'Atharva.being_private', 'phone':'9828489796'}}

player1 = Player(**player_info)

update_player_data(player1)