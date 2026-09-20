from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    is_active: bool = True
    role: str = "cashier"


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    username: str | None = None
    password: str | None = None
    is_active: bool | None = None
    role: str | None = None


class UserRead(UserBase):
    user_id: int
model_config = ConfigDict(from_attributes=True)