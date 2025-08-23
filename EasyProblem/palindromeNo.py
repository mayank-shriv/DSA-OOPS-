class Palindrome:
    # The __init__ method should accept the number and store it
    def __init__(self, number):
        self.original_number = number

    def check(self):
        # Use the number stored in the instance
        number = self.original_number
        reversed_sum = 0
        
        # This loop correctly reverses the number
        while(number > 0):
            last_digit = number % 10
            reversed_sum = reversed_sum * 10 + last_digit
            number = number // 10
            
        # Compare the reversed number with the original number
        if self.original_number == reversed_sum:
            print(f'{self.original_number} is a palindrome number.')
        else:
            print(f'{self.original_number} is not a palindrome number.')


# Get input from the user
n = int(input("Enter the No to check palindrome or not: "))

# Create an object, passing the number 'n' to the constructor
obj1 = Palindrome(n)

# Call the check method
obj1.check()