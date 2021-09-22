from typing import Optional, Union
from pydantic import BaseModel, validator


class Main(BaseModel):
    error_name: str
    apps: Union[list, str]
    delay: Optional[int] = 360
    max_ram: Optional[float] = 12.0

    @validator('error_name', 'apps')
    def must_contain_extention(cls, value: Union[list, str]):
        if isinstance(value, list):
            for obj in value:
                if '.' not in obj:
                    raise ValueError('Must contain extention')
        else:
            if '.' not in value:
                raise ValueError('Must contain extention')

        return value
