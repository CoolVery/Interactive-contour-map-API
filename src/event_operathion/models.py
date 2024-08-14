
from sqlalchemy import MetaData, Table, Column, Integer, LargeBinary, ForeignKey, String

metadata = MetaData()

WebHistory_event = Table(
    "WebHistory_event",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name_event", String, nullable=False),
    Column("path_img", LargeBinary, nullable=False),
    Column("path_img_map", LargeBinary, nullable=False),
)

WebHistory_directionlines = Table(
    "WebHistory_directionlines",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name_direction_line", String, nullable=False),
    Column("path_img_line", LargeBinary, nullable=False),
    Column("event_id", Integer, ForeignKey(WebHistory_event.c.id) ,nullable=False),
)
WebHistory_sideboundaries = Table(
    "WebHistory_sideboundaries",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name_side_boundaries", String, nullable=False),
    Column("path_img_boundaries", LargeBinary, nullable=False),
    Column("event_id", Integer, ForeignKey(WebHistory_event.c.id), nullable=False),
)