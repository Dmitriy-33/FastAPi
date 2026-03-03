from fastapi import APIRouter, Query, HTTPException, status, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.schemas.car import Car, car_list

router = APIRouter(prefix="/api")

templates = Jinja2Templates(directory="app/templates")

@router.get("/cars/", response_class=HTMLResponse,  name='html_car_list')
async def html_cars(
    request: Request
):
    result = car_list

    context = {
        "request": request,
        "cars": result,
        "title": "Список автомобилей"}
    return templates.TemplateResponse("cars/car_list.html", context=context)


@router.get("/cars/{car_id}/", response_class=HTMLResponse, name='html_car_detail')
async def car_details(request: Request, car_id: int):
    car_id -= 1
    if car_id < 0 or car_id >= len(car_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Автомобиль с таким id не найден")
    context = {
        "request": request,
        "car": car_list[car_id],
        "title": "Детализация"
    }
    return templates.TemplateResponse("cars/car_detail.html", context=context)


@router.get("/car_create/", response_class=HTMLResponse, name='html_car_create')
async def car_create(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse("cars/car_create.html", context=context)


@router.post("/car_create/", response_class=HTMLResponse)
async def add_car(
        request: Request,
        marka: str = Form(...),
        model: str = Form(...),
        year: int = Form(...),
        engine: str = Form(...),
        power: str = Form(...),
        color: str = Form(...)
):
    new_car = Car(
        id=len(car_list) + 1,
        marka=marka,
        model=model,
        year=year,
        engine=engine,
        power=power,
        color=color
    )

    car_list.append(new_car)

    context = {
        "request": request,
        "cars": car_list,
        "title": "Список автомобилей"}
    return templates.TemplateResponse("cars/car_list.html", context=context)