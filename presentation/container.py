from dependency_injector import containers, providers
from data.matrix import Matrix
from data.vector import Vector
from domain.jacoby import Jacoby
from domain.gauss_seidel import GaussSeidel
from domain.sor import SOR
from presentation.input_provider import InputProvider
from domain.strategy_context import Context


class Container(containers.DeclarativeContainer):
    input_provider = providers.Singleton(InputProvider)
    jacoby = providers.Factory(Jacoby)
    gauss_seidel = providers.Factory(GaussSeidel)
    sor = providers.Factory(SOR)
    strategy_context = providers.Singleton(Context)
    matrix = providers.Factory(Matrix)
    vector = providers.Factory(Vector)