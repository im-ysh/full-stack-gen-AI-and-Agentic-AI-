seattype = input("Enter the type of seat you want : ").lower()

match seattype:
    case "sleeper" : 
        print("sleeper - No AC beds available")
    case "ac":
        print("ac - ac comfortable ride") 
    case "general":
        print("general - general ride no beds only sitting")
    case  "luxury":
        print("luxury - premium and extra luxury features") 
    case _:
        print("Invalid seat type")
