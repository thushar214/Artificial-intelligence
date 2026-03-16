from pydantic import BaseModel


class stu(BaseModel):
    name: str
    age : int


data ={"name" : "Thushar","age":50}
# dict = ["Thushar",50]
print(stu(**data))