from fastapi import FastAPI
from infrastructure.repositories import RepositorioFactoresEmisionLocal
from domain.services import CalculadoraCarbono
from application.use_cases import CalcularHuellaUseCase
from presentation.controllers import router

app = FastAPI(title="Microservicio Cálculo Huella de Carbono")

repositorio = RepositorioFactoresEmisionLocal()
calculadora = CalculadoraCarbono(repositorio)
use_case = CalcularHuellaUseCase(calculadora)

app.dependency_overrides[CalcularHuellaUseCase] = lambda: use_case

app.include_router(router)