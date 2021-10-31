def hex(simplehex): # simplehex == '#FFF'
    if isinstance(simplehex, str):
        simplehex = list(simplehex)
        frst = simplehex[1]
        scnd = simplehex[2]
        thrd = simplehex[3]
        return f'#{frst}{frst}{scnd}{scnd}{thrd}{thrd}'
    else: return '#FFFFFF'
