
# Converte in milioni
def Millions(Obj):
    return round(Obj / 1_000_000, 2)

# Converte in milioni
def M(Obj):
    return Millions(Obj)

# Converte in migliaia
def Tousands(Obj):
    return round(Obj / 1_000, 2)

# Converte in migliaia
def K(Obj):
    return Tousands(Obj)