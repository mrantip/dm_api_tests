from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, StrictStr, Field, StrictBool


class Roles(Enum):
    GUEST = 'Guest'
    PLAYER = 'Player'
    ADMINISTRATOR = 'Administrator'
    NANNY_MODERATOR = 'NannyModerator'
    REGULAR_MODERATOR = 'RegularModerator'
    SENIOR_MODERATOR = 'SeniorModerator'


class Rating(BaseModel):
    enabled: bool
    quantity: int
    quality: int


class User(BaseModel):
    login: StrictStr
    roles: List[Roles]
    medium_picture_url: Optional[StrictStr] = Field(None)
    small_picture_url: Optional[StrictStr] = Field(None)
    status: Optional[StrictStr] = Field(None)
    rating: Rating
    online: Optional[datetime] = Field(None)
    name: Optional[StrictStr] = Field(None)
    location: Optional[StrictStr] = Field(None)
    registration: Optional[datetime] = Field(None)


class UserEnvelopeModel(BaseModel):
    resource: User
    metadata: Optional[StrictStr] = Field(None)
