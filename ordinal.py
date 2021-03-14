def fgr(num: int) -> str:
    """ordinal figures :)

    converts 23 -> 23rd
    """
    try:
        n = str(num)
    except:
        return num

    if not n.isdigit():
        return n

    def _():
        nonlocal n
        if len(n) == 2 and n[0] == '1':
            return 'th'
        elif n[-1] == '1':
            return 'st'
        elif n[-1] == '2':
            return 'nd'
        elif n[-1] == '3':
            return 'rd'
        else:
            return 'th'
    return n + _()
