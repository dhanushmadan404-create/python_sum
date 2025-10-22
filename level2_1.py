def rain(a):
    if a>0 and a<=15:
        print("Green: No warning, light rain expected.")
    elif a>15 and a<=64:
        print("yellow: moderate rain expected.")
    elif a>64 and a<=115:
        print("orange: heavy rain expected.")
    elif a>115:
        print("Red: Take action  extremely heavy rain expected")
    else:
        print("invalid mm")
    
rain(40)
rain(78)
rain(120)