from ValidationException import ValidationException

def validate_file(file_path):
    # numbers=[0,1,2,3,4,5,6,7,8,9]
    with open(file_path, "r") as file1:
        next(file1)
        # print(file1.read())

        for count, line in enumerate(file1):
            line_values = line.split(',')
            # print(line_values[0])
        try:
                line_values[0].isLetter()
        except:
            raise ValidationException(f"Invalid first name:{line_values[0]}")

def test():
    try:
        validate_file("users.txt")
    except ValidationException as ve:
        print(ve)

test()
