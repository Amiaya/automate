import re
def dateValidate(cha):
    date = re.compile(r'''((\d{1,2}) #day
                           (\s|\/) #seperator
                            (\d{1,2}) #Month 
                            (\s|\/) #seperator
                            (\d{4}) ) #Year                    ''', re.VERBOSE)
    mo = date.search(cha)

    year = mo.group(6)
    day = mo.group(2)
    month = mo.group(4)
    if int(year) > 1000 and int(year) < 3000:
        if int(month) == 1 or int(month) == 3 or int(month) == 5 or int(month) == 7 or int(month) == 8 or int(month) == 10 or int(month) == 12:
            if int(day) > 31:
                return ("Invalid date")
            return (mo.group())


        elif int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11:
            if int(day) > 30:
                return ("Invalidate")
            return (mo.group())
        else:
            if int(year) % 4 == 0 and int(day) < 30:
                return (mo.group() + " It is a leap year")
            if int(day) > 28:
                return ("Invalid date")
            return (mo.group())
    else:
        return ("valid date")

mo = "gsjjyhsj 29/2/2024"
print(dateValidate(mo))

# Interview Question


# import re
# phone = re.compile(r'\d+')
# mo = phone.findall(r'65howfar6in')
# # mo = phone.search('Cell: 415-555-9999 Work: 212-555-0000')
# print(mo)
# x = 0
# for i in range(len(mo)):
#     x += int(mo[i])
# print(x)
