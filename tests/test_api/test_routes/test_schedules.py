import pytest

from fastapi import FastAPI
from httpx import AsyncClient


pytestmark = pytest.mark.asyncio


async def test_schedules_wrong_input(app: FastAPI, client: AsyncClient) -> None:
    response = await client.post(
        app.url_path_for("schedules:opening-hours"), data={"opening_hours": {}}
    )

    assert response.status_code == 422


async def test_schedules_invalid_week_days(app: FastAPI, client: AsyncClient) -> None:
    response = await client.post(
        app.url_path_for("schedules:opening-hours"),
        data={
            "opening_hours": {
                "monday": [],
            }
        },
    )

    assert response.status_code == 422


async def test_schedules_invalid_week_day_wrong_opening_type(
    app: FastAPI, client: AsyncClient
) -> None:
    response = await client.post(
        app.url_path_for("schedules:opening-hours"),
        json={
            "opening_hours": {
                "monday": [],
                "tuesday": [
                    {"type": "foo", "value": 36000},
                    {"type": "close", "value": 64800},
                ],
                "wednesday": [],
                "thursday": [
                    {"type": "open", "value": 37800},
                    {"type": "close", "value": 64800},
                ],
                "friday": [{"type": "open", "value": 36000}],
                "saturday": [
                    {"type": "close", "value": 3600},
                    {"type": "open", "value": 36000},
                ],
                "sunday": [
                    {"type": "close", "value": 3600},
                    {"type": "open", "value": 43200},
                    {"type": "close", "value": 75600},
                ],
            }
        },
    )

    assert response.status_code == 422


async def test_schedules_invalid_week_day_wrong_combination(
    app: FastAPI, client: AsyncClient
) -> None:
    response = await client.post(
        app.url_path_for("schedules:opening-hours"),
        json={
            "opening_hours": {
                "monday": [
                    {"type": "close", "value": 64800},
                ],
                "tuesday": [
                    {"type": "open", "value": 36000},
                    {"type": "close", "value": 64800},
                ],
                "wednesday": [],
                "thursday": [
                    {"type": "open", "value": 37800},
                    {"type": "close", "value": 64800},
                ],
                "friday": [{"type": "open", "value": 36000}],
                "saturday": [
                    {"type": "close", "value": 3600},
                    {"type": "open", "value": 36000},
                ],
                "sunday": [
                    {"type": "close", "value": 3600},
                    {"type": "open", "value": 43200},
                    {"type": "close", "value": 75600},
                ],
            }
        },
    )

    assert response.status_code == 400
    assert response.json() == {
        "errors": ["Invalid opening hour detected: None - close"]
    }


async def test_schedules(app: FastAPI, client: AsyncClient) -> None:
    response = await client.post(
        app.url_path_for("schedules:opening-hours"),
        json={
            "opening_hours": {
                "monday": [],
                "tuesday": [
                    {"type": "open", "value": 36000},
                    {"type": "close", "value": 64800},
                ],
                "wednesday": [],
                "thursday": [
                    {"type": "open", "value": 37800},
                    {"type": "close", "value": 64800},
                ],
                "friday": [{"type": "open", "value": 36000}],
                "saturday": [
                    {"type": "close", "value": 3600},
                    {"type": "open", "value": 36000},
                ],
                "sunday": [
                    {"type": "close", "value": 3600},
                    {"type": "open", "value": 43200},
                    {"type": "close", "value": 75600},
                ],
            }
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "opening_hours": {
            "monday": "Closed",
            "tuesday": "10:00:00 AM - 06:00:00 PM",
            "wednesday": "Closed",
            "thursday": "10:30:00 AM - 06:00:00 PM",
            "friday": "10:00:00 AM - 01:00:00 AM",
            "saturday": "10:00:00 AM - 01:00:00 AM",
            "sunday": "12:00:00 PM - 09:00:00 PM",
        }
    }
