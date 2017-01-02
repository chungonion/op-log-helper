def input_time_check(input_time):
    try:
        if int(input_time[0]) >= 0 and int(input_time[0]) <= 24 and int(input_time[1]) >= 0 and int(input_time[1]) < 60 and len(input_time) == 2:
            return True
        else:
            return False
    except:
        return False


def input_time(message):
    while True:
        time = raw_input(message)
        time = time.split(":")
        if input_time_check(time) == True:
            break
        else:
            print "There is an invalid input!"
    return time


def input_pattern():
    while True:
        check_pattern = True
        pattern = raw_input("Break Pattern: ")
        pattern = pattern.split(" ")
        try:
            for i in pattern:
                if int(i) > 0 and int(i) < 13:
                    continue
                else:
                    check_pattern = False
                    break
        except:
            print "Pattern Error!"
            continue
        if check_pattern == True:
            break
        else:
            print "Pattern Error!"
    return pattern


def input_staff_nos():
    while True:
        try:
            staff_nos = int(raw_input("Staff nos?: "))
            break
        except:
            print "Error!"
            continue
    return staff_nos


def result_generation(staff_nos, opening_time, closing_time, break_start_time, pattern):
    break_time = [break_start_time]
    current_break_time = break_start_time
    for i in pattern:
        for j in range(0, staff_nos):
            break_hour = int(current_break_time[0])
            break_min = int(current_break_time[1]) + int(i) * 5
            while break_min >= 60:
                break_min -= 60
                break_hour += 1
            if int(current_break_time[0])>=int(closing_time[0]) and int(current_break_time[1])>int(closing_time[1]):
                print "Pattern is not possible!"
                return
            else:
                current_break_time = [str(break_hour).zfill(2),str(break_min).zfill(2)]
                break_time.append(current_break_time)
    # print break_time
    for i in range(0, staff_nos):
        print "Staff", int(i)+1 ,"'s break:"
        print opening_time[0]+":"+opening_time[1]+" - "+break_time[i][0]+":"+break_time[i][1]
        for j in range(1, len(pattern)):
            print break_time[(j-1)*staff_nos+i+1][0]+":"+break_time[(j-1)*staff_nos+i+1][1]+" - "+break_time[j*staff_nos+i][0]+":"+break_time[j*staff_nos+i][1]
            if j == len(pattern)-1:
                print break_time[j * staff_nos + i + 1][0] + ":" + break_time[j * staff_nos + i + 1][1] + " - " + closing_time[0] + ":" + closing_time[1]



def main():
    opening_time = input_time("Please enter the park opening time: ")
    while True:
        closing_time = input_time("Please enter the park closing time: ")
        if int(opening_time[0])<int(closing_time[0]):
            break
        else:
            print "Park closing time must after park opening time"

    while True:
        break_start_time = input_time("Please enter the break starting time: ")
        if int(break_start_time[0])>int(opening_time[0]) and int(break_start_time[0])<int(closing_time[0]):
            break
        print "Break start time must within park opening hours!"
    staff_nos = input_staff_nos()
    pattern = input_pattern()
    # print pattern
    result_generation(staff_nos, opening_time, closing_time, break_start_time, pattern)

main()
