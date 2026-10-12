#A number guess
print("====Number Analyser from (1, 51)====")
count_even=0
count_odd=0
divisible_by3=0
divisible_by5=0
divisible_num=0
divisible_time=0
total_by3=0
total_even=0
total_odd=0
for i in range(1, 52):
    print(i)
    if i%10==0:
        continue
    if i>50:
     break
    #even numbers
    if i%2==0:
        count_even+=1
        total_even+=i
        #odd numbers
    if i%2==1:
        count_odd+=1
        total_odd+=i
        #divisible by 3
    if i%3==0:
        divisible_by3+=1
        total_by3+=i
        #divisible by 5
    if i%5==0:
        divisible_by5+=1
        #divisible by three and five
    if i%3==0 and i%5==0:
        divisible_num+=1

        #divisible by 4 and 7
    if i%4==0 or i%7==0:
        divisible_time+=1
        #using the continue formula

print(f"EVEN NUMBERS: {count_even}")

print(f"ODD NUMBERS: {count_odd}")

print(f"TOTAL ODD NUMBERS: {total_odd}")

print(f"TOTAL EVEN NUMBERS: {total_even}")

print(f"TOTAL NUMBERS DIVISIBLE BY 3: {total_by3}")
print(f"Divisible by 3: {divisible_by3}")

print(f"Divisible by 5: {divisible_by5}")

print(f"Divisible by 3 and 5: {divisible_num}")

print(f"Divisible by 4 or 7: {divisible_time}")




