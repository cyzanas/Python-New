def main():
    ask=input("What time is it? ")
    ask=convert(ask)
    if ask>=7 and  ask<12:
        print("breakfast time")
    elif ask>=12 and ask<18:
        print("Lunch time")
    elif ask>=18:
        print("Dinner Time")
    else:
        print("Go and sleep")
    


def convert(time):
    hours,minutes=time.split(":")
    hours=int(hours)
    minutes=int(minutes)
    actual=hours+(minutes/60)
    actual=float(actual)
    return actual
    


if __name__ == "__main__":
    main()