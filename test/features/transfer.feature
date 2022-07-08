Feature: Transferencia bancaria
    Como titular de una cuenta,
    deseo realizar una transferencia bancaria,
    para mantener la confianza en el banco.

  Scenario Outline: Transferencia entre cuentas del mismo banco con saldo suficiente
    Given que Miguel tiene una cuenta de ahorros con $<saldo_origen> USD de saldo
    Given que Gabriel tiene otra cuenta de ahorros con $<saldo_destino> USD de saldo

    When Miguel transfiere un monto de $<monto> USD a Gabriel

    Then Miguel tendrá $<saldo_origen_final> USD de saldo
    Then Gabriel tendrá $<saldo_destino_final> USD de saldo.
    Examples:
      | saldo_origen | saldo_destino | monto | saldo_origen_final | saldo_destino_final |
      | 100| 10| 50| 50| 60|
      | 10| 0| 10| 0| 10|