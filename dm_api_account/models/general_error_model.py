from typing import Optional

from pydantic import BaseModel, Extra, StrictStr, Field


class GeneralError(BaseModel):
    class Config:
        extra = Extra.forbid

    message: Optional[StrictStr] = Field(None, description='Client message')
