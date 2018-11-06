def ohms(str):
    colors = {
       "0": 'black',
       "1": 'brown',
       "2": 'red',
       "3": 'orange',
       "4": 'yellow',
       "5": 'green',
       "6": 'blue',
       "7": 'violet',
       "8": 'gray',
       "9": 'white'
   }
    first_color  = colors[str[0]]
    second_color = colors[str[1]]
    third_color  = colors[str[2]]

    print(first_color +" "+ second_color+ " " + third_color)

ohms("540")
