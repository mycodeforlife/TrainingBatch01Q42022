input_num =input("eneter number to check if even or not:")
def return_true_if_even(num):
    if num%2==0:
        return 'true'
    else:
        return 'fales'


if return_true_if_even(int(input_num)):
    print("Congratulation you entered even number")
else:
    print ("please try again, good luck!")

