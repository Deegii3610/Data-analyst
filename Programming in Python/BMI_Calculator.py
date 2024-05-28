fn = str(input("First name: "))
sn = str(input("Second name: "))
gen = str(input("Gender (M/F): "))
old = int(input("Old: "))

if old<20:
    print("You are younger than 20")
    
else:
    print("Hi ",fn[0]+sn[0])
    wei = float(input("Weight: "))
    hei = float(input("Height (m): "))
    BMI = wei / (hei*hei)
    print("Your body mass index (BMI) is :", BMI)
    if gen == 'F':
        if BMI<= 19.6:
            print("Percentile: 5th")
        elif BMI>19.6 and BMI<=21:
            print("Percentile: 10th")
        elif BMI>21 and BMI<=22:
            print("Percentile: 15th")
        elif BMI>22 and BMI<=23.6:
            print("Percentile: 25th")
        elif BMI>23.6 and BMI<=27.7:
            print("Percentile: 50th")
        elif BMI>27.7 and BMI<=33.2:
            print("Percentile: 75th")
        elif BMI>33.2 and BMI<=36.5:
            print("Percentile: 85th")
        elif BMI>36.5 and BMI<=39.3:
            print("Percentile: 90th")
        elif BMI>39.3 and BMI<=43.3:
            print("Percentile: 95th")
        else: print("Check your data")
    elif gen == 'M':
        if BMI<= 20.7:
            print("Percentile: 5th")
        elif BMI>20.7 and BMI<=22.2:
            print("Percentile: 10th")
        elif BMI>22.2 and BMI<=23:
            print("Percentile: 15th")
        elif BMI>23 and BMI<=24.6:
            print("Percentile: 25th")
        elif BMI>24.6 and BMI<=27.7:
            print("Percentile: 50th")
        elif BMI>27.7 and BMI<=31.6:
            print("Percentile: 75th")
        elif BMI>31.6 and BMI<=34:
            print("Percentile: 85th")
        elif BMI>34 and BMI<=36.1:
            print("Percentile: 90th")
        elif BMI>36.1 and BMI<=39.8:
            print("Percentile: 95th")
        else: print("Check your data")
    else: print("Check your gender data")









