from behave import *

from src.models.client import Client
from src.models.savingAccount import SavingAccount

use_step_matcher("re")


@step("que Miguel tiene una cuenta de ahorros con \$(?P<saldo_origen>.+) USD de saldo")
def step_impl(context, saldo_origen):
    """
    :type context: behave.runner.Context
    :parameter saldo_origen: float
    """
    saldo_origen = float(saldo_origen)
    account = SavingAccount(saldo_origen)
    context.origin_client = Client("Miguel", account)
    assert context.origin_client.account.balance == saldo_origen


@step("que Gabriel tiene otra cuenta de ahorros con \$(?P<saldo_destino>.+) USD de saldo")
def step_impl(context, saldo_destino):
    """
    :type context: behave.runner.Context
    :parameter saldo_destino: float
    """
    saldo_destino = float(saldo_destino)
    account = SavingAccount(saldo_destino)
    context.destination_client = Client("Gabriel", account)
    assert context.destination_client.account.balance == saldo_destino


@step("Miguel transfiere un monto de \$(?P<monto>.+) USD a Gabriel")
def step_impl(context, monto):
    """
    :type context: behave.runner.Context
    :parameter monto: float
    """
    monto = float(monto)
    context.origin_client.account.transfer(monto, context.destination_client.account)


@step("Miguel tendrá \$(?P<saldo_origen_final>.+) USD de saldo")
def step_impl(context, saldo_origen_final):
    """
    :type context: behave.runner.Context
    :parameter saldo_origen_final: float
    """
    saldo_origen_final = float(saldo_origen_final)
    assert context.origin_client.account.balance == saldo_origen_final


@step("Gabriel tendrá \$(?P<saldo_destino_final>.+) USD de saldo\.")
def step_impl(context, saldo_destino_final):
    """
    :type context: behave.runner.Context
    :parameter saldo_destino_final: float
    """
    saldo_destino_final = float(saldo_destino_final)
    assert context.destination_client.account.balance == saldo_destino_final
