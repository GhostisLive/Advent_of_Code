with open('input.in')as file:
    dat=[i for i in file.read().split('\n')]    #Pulling the data
#print(dat)  
max=0
sec_max = 0  # Elf with second greatest calories
thir_max=0   # Elf with third greatest cals
count=0
for cal in dat:
    if cal == '':
        count=0  # Resetting the count | skipping to next Elf
    else:
        dat_int = int(cal)   #Turning string to integer (so we can add)
        count += dat_int      # Adding to the count if its a number


    # Finding max values
    # EDIT: We need to shift the previous max values found
    # before setting new values!!
    if count > max:
        thir_max=sec_max
        sec_max=max
        max = count
    elif count > sec_max:
        thir_max=sec_max
        sec_max = count
    elif count > thir_max:
          thir_max = count




sum_cal = max+sec_max+thir_max # sum of 3 greatest calories
    
#ANSWERS
print(f"Day 1 \n Part 1 : {max}")
print(f"Part 2: {sum_cal} ")

