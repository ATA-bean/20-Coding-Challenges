def print_times_tables(times_table: int):
    count = 1
    while count < 13:
        print(count,"x",times_table,"=",(times_table * count))
        count += 1

user = int(input("please enter a number:"))
print_times_tables(user)