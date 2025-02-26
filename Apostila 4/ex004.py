class Erro(Exception):
    pass
try:
    raise Erro("Ocorreu um erro personalizado!")
except Erro as e:
    print("Erro capturado:", e)