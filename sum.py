def sum(first_number,second_number):
    
    first_number_int=string_to_integer(first_number)
    second_number_int= string_to_integer(second_number)
    result= first_number_int + second_number_int
   
    return result
    
def string_to_integer(number_string):
    
    number_integer=int(number_string)

    return number_integer

answer = sum("1","2")

print(answer)
