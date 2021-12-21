def direction(facing, turn):
    rose = {
        "N": 0,
        "NE": 45,
        "E": 90,
        "SE": 135,
        "S": 180,
        "SW": 225,
        "W": 270,
        "NW": 315
        }
    t = abs(rose[facing]+turn)
    if t > 361 : t %= 360
    for key, value in rose.items():
        if t == value:
            return key
        elif t==360:
            return 'N'

print(direction("S", 180))
print(direction("SE", -45))
print(direction("W", -495))
print(direction("N", 180))
