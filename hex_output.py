def hex_output(hex_num):
    dec = 0
    for power, num in enumerate((reversed(hex_num))):
        dec += (int(num,16) * (16**power))
    return  dec
print(hex_output("aa"))