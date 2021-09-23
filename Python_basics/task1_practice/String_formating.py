data = ("John", "Doe", 53.44)
format_string = "Hello"

print(format_string, "{} {}. Your current balance is ${}".format(*data))
