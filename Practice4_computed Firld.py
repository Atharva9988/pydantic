from pydantic import BaseModel, EmailStr, computed_field, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Player(BaseModel):
    name: str
    email: EmailStr
    linkedin: AnyUrl
    age: int
    game: str
    role: str
    weight: float
    height: float
    playing_status: bool
    injuries: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

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
    print(player.height)
    print(player.playing_status)
    print('BMI =', player.bmi)
    print(player.injuries)
    print(player.contact_details)
    print('Inserted')

player_info= {'name':'Atharva','email': 'shreyash@gmail.com','linkedin':'http://linkedin.com', 'age':18, 'game': 'Cricket', 'role':'Lefthand Batsman and Righthand Offspin Bowler', 'weight':70.5,'height':1.86, 'playing_status':True, 'injuries':['calf','muscle pull'], 'contact_details':{'profile':'Atharva.being_private', 'phone':'9828489796'}}

player1 = Player(**player_info)

update_player_data(player1)