from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, StrictStr, Field


class PagingSettings(BaseModel):
    posts_per_page: int
    comments_per_page: int
    topics_per_page: int
    messages_per_page: int
    entities_per_page: int


class ColorSchema(Enum):
    MODERN = 'Modern'
    PALE = 'Pale'
    CLASSIC = 'Classic'
    CLASSIC_PALE = 'ClassicPale'
    NIGHT = 'Night'


class UserSettings(BaseModel):
    color_schema: List[ColorSchema]
    nanny_greetings_message: StrictStr
    paging: PagingSettings


class BdParseMode(Enum):
    COMMON = 'Common'
    INFO = 'Info'
    POST = 'Post'
    CHAT = 'Chat'


class InfoBdText(BaseModel):
    value: StrictStr
    parse_mode: List[BdParseMode]


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
    isq: Optional[StrictStr] = Field(None)
    skype: Optional[StrictStr] = Field(None)
    original_picture_url: Optional[StrictStr] = Field(None)
    info: Optional[InfoBdText]
    settings: Optional[UserSettings]


class UserDetailsEnvelopeModel(BaseModel):
    resource: User
    metadata: Optional[StrictStr] = Field(None)
