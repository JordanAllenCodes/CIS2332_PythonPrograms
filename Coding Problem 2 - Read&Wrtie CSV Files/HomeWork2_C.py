# Jordan Allen
# PSID: 2040697

month_list = {"january": "1", "february": "2", "march": "3", "april": "4", "may": "5",
              "june": "6", "july": "7", "august": "8", "september": "9", "october": "10",
              "november": "11", "december": "12"}

txt_file = open('C:\\Users\\jorda\\OneDrive\\Desktop\\inputDates.txt', 'r')
write_file = open('C:\\Users\\jorda\\OneDrive\\Desktop\\parsedDates.txt', 'w')

for i in txt_file:
    if i != "-1":
        lst = i.split()
        if len(lst) >= 3:
            month = lst[0]
            day = lst[1]
            year = lst[2]

            if month.lower() in month_list:
                comma = day[-1]
                if comma == ',':
                    day = day[:len(day) - 1]
                hold_month = month_list[month.lower()]
                formatDate = hold_month + "/" + day + "/" + year

                write_file.write(formatDate)
                write_file.write("\n")

write_file.close()
txt_file.close()
