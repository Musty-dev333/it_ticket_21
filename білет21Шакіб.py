def geom_term(a1, q, n):
    """n-й член геометричної прогресії (рекурсивно)"""
    if n == 1:
        return a1
    return q * geom_term(a1, q, n - 1)


def geom_sum(a1, q, n):
    """сума перших n членів (рекурсивно)"""
    if n == 1:
        return a1
    # S(n) = a1 + q * S(n-1)
    return a1 + q * geom_sum(a1, q, n - 1)


def main():
    a1 = float(input("Введіть перший член прогресії a1: "))
    q = float(input("Введіть знаменник прогресії q: "))
    n = int(input("Введіть номер члена n (n>=1): "))

    if n < 1:
        print("Помилка: n має бути >= 1")
        return

    an = geom_term(a1, q, n)
    sn = geom_sum(a1, q, n)

    print(f"{n}-й член геометричної прогресії: {an}")
    print(f"Сума перших {n} членів прогресії: {sn}")


if __name__ == "__main__":
    main()
