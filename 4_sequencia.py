def completar_sequencia():
    # a) Sequência: 1, 3, 5, 7, ___ (ímpares)
    a = [1, 3, 5, 7]
    proximo_a = a[-1] + 2

    # b) Sequência: 2, 4, 8, 16, 32, 64, ____ (potências de 2)
    b = [2, 4, 8, 16, 32, 64]
    proximo_b = b[-1] * 2

    # c) Sequência: 0, 1, 4, 9, 16, 25, 36, ____ (inteiros elevados a 2)
    c = [0, 1, 4, 9, 16, 25, 36]
    proximo_c = (int(len(c)) ** 2)

    # d) Sequência: 4, 16, 36, 64, ____ (pares elevados a 2)
    d = [4, 16, 36, 64]
    proximo_d = ((len(d) + 1) * 2) ** 2

    # e) Sequência: 1, 1, 2, 3, 5, 8, ____ (fibonacci)
    e = [1, 1, 2, 3, 5, 8]
    proximo_e = e[-1] + e[-2]

    # f) Sequência: 2, 10, 12, 16, 17, 18, 19, ____ (começam com 'd')
    proximo_f = 200

    print(f"Próximo elemento de (a): {proximo_a}")
    print(f"Próximo elemento de (b): {proximo_b}")
    print(f"Próximo elemento de (c): {proximo_c}")
    print(f"Próximo elemento de (d): {proximo_d}")
    print(f"Próximo elemento de (e): {proximo_e}")
    print(f"Próximo elemento de (f): {proximo_f}")

completar_sequencia()
