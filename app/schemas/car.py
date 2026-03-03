from pydantic import BaseModel


class Car(BaseModel):
    id: int
    marka: str
    model: str
    year: int
    engine: str
    power: str
    color: str


car_list = [
    Car(
        id=1,
        marka='Skoda',
        model='Octavia',
        year=2018,
        engine='дизель, 2.0 л',
        power='184 л.с.',
        color='серый',
    ),
    Car(
        id=2,
        marka='Honda',
        model='Stream',
        year=2011,
        engine='бензин, 1.8 л',
        power='140 л.с.',
        color='синий',
    ),
    Car(
        id=3,
        marka='Mitsubishi',
        model='Outlander',
        year=2016,
        engine='бензин, 3.0 л',
        power='227 л.с.',
        color='серый',
    ),
    Car(
        id=4,
        marka='Opel',
        model='Insignia',
        year=2014,
        engine='бензин, 1.8 л',
        power='140 л.с.',
        color='белый',
    ),
    Car(
        id=5,
        marka='Kia',
        model='Sorento',
        year=2015,
        engine='дизель, 2.2 л',
        power='200 л.с.',
        color='серый',
    ),
]