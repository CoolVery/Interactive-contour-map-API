from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from event_operathion.models import WebHistory_event as Model_WebHistory_event, WebHistory_directionlines as Model_WebHistory_directionlines
from event_operathion.schemas import WebHistory_event as Schema_WebHistory_event, WebHistory_directionlines as Schema_WebHistory_directionlines

router = APIRouter(
    prefix="/event_operathion",
    tags=["Event"]
)


async def get_events(
        session: AsyncSession = Depends(get_async_session),
        name_event: str = Query(None)
):
    query = select(Model_WebHistory_event).where(Model_WebHistory_event.c.name_event == name_event)
    event = await session.execute(query)
    result = event.first()
    return Schema_WebHistory_event.from_orm(result)

async def get_lines(
        session: AsyncSession = Depends(get_async_session),
        event: Schema_WebHistory_event = Query(None)
):
    query = select(Model_WebHistory_directionlines).where(Model_WebHistory_directionlines.c.event_id == event.id)
    event = await session.execute(query)
    result = event.all()
    return [Schema_WebHistory_directionlines.from_orm(line) for line in result]
@router.get("/line/", response_model=List[Schema_WebHistory_directionlines])
async def get_event_directionlines(
        session: AsyncSession = Depends(get_async_session),
        name_event: str = Query(None)
):
    event = await get_events(session, name_event)
    result = await get_lines(session, event)
    return result