from pydantic import BaseModel, Field


class WebHistory_event(BaseModel):
    id: int
    name_event: str
    path_img: bytes = Field(..., example="base64")
    path_img_map: bytes = Field(..., example="base64")

    class Config:
        orm_mode = True
        from_attributes = True


class WebHistory_directionlines(BaseModel):
    id: int
    name_direction_line: str
    path_img_line: bytes = Field(..., example="base64")
    event_id: int

    class Config:
        orm_mode = True
        from_attributes = True


class WebHistory_sideboundaries(BaseModel):
    id: int
    name_side_boundaries: str
    path_img_boundaries: bytes = Field(..., example="base64")
    event_id: int

    class Config:
        orm_mode = True
        from_attributes = True

