def hanoi_solver(numero):
    varillas = [list(range(numero, 0, -1)), [], []]
    movimientos = [" ".join(str(v) for v in varillas)]

    def mover(n, origen, destino, auxiliar):
        if n == 0:
            return
        mover(n - 1, origen, auxiliar, destino)
        disco = varillas[origen].pop()
        varillas[destino].append(disco)
        movimientos.append(" ".join(str(v) for v in varillas))
        mover(n - 1, auxiliar, destino, origen)

    mover(numero, 0, 2, 1)
    return "\n".join(movimientos)