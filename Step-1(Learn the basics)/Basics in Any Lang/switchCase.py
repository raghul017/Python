from pygments.lexer import default


def whichWeekDay(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case default:
            return "invalid input"

day = int(input("Enter your day"))
result = whichWeekDay(day)
print(result)