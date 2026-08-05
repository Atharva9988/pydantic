from pydantic import BaseModel

class Address(BaseModel):
    city: str
    district: str
    pin: str


class Player(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'Karjat', 'district':'Raigad', 'pin': '410203'}

address1 = Address(**address_dict)

player_dict = {'name':'Atharva', 'gender': 'male', 'age':20, 'address': address1}

player1 = Player(**player_dict)

print(player1)
print(player1.name)
print("Sucessfully Executed")