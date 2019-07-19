Subject = ['Bangla','English','Information Technology', 'Religion', 'Math','Bangladesh & World', 'Group 1', 'Group 2', 'Group 3', 'Optional']
GPA_all = []

for GPA in Subject:
    GPA = float(input(GPA + ": "))
    GPA_all.append(GPA)

Total_without_optional = sum(GPA_all[0:9])
Optional_extra = GPA_all[-1] - 2.00

if Optional_extra <= 0.00:
    calculation1 = Total_without_optional/9
    print("GPA: {:.2f}" .format(calculation1))

elif Optional_extra > 0.00:
    calculation2 = (Total_without_optional + Optional_extra) / 9
    print("\nGPA: {:.2f}".format(calculation2))

