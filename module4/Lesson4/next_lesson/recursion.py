def our_pow(base, exp):
    """

    :param base: основа степені
    :param exp: степень повинна бути більше або рівне 0
    :return: результат base**exp
    """
    print(base, exp)
    if exp <= 0:
        return
    if exp == 1:
        return base
    return base * our_pow(base, exp - 1)


if __name__ == '__main__':
    print(our_pow(3, 4))
    help(our_pow)
    print(our_pow.__doc__)




# 2 * 2 * 2
