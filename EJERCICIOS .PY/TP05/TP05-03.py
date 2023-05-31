def frenarCuenta():
    try:
        for i in range(100000):
            print(i)
    except KeyboardInterrupt:
        return "Interrupcion detectada"
print(frenarCuenta())