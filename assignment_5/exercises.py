
#def to_fahrenheit(degrees_celsius):
#    return degrees_celsius


#def to_celsius(degrees_fahrenheit):
#    return degrees_fahrenheit


def to_fahrenheit(degrees_celcius):
	output = degrees_celcius * (9 / 5) + 32
	return output 


def to_celcius(degrees_fahrenheit):
	output = (degrees_fahrenheit - 32) * (5 / 9)
	return output

print(to_fahrenheit(0))
print(to_fahrenheit(50))
print(to_fahrenheit(100))
print(to_fahrenheit(150))

print(to_celcius(32))
