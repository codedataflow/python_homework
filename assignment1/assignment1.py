# Task 1: Hello 
def hello():
    return "Hello!"

# Task 2: Greet with a Formatted String
def greet(name):
    return f"Hello, {name}!"

# Task 3: Calculator
# math_operation should be an Enum
def calc(arg1, arg2, math_operation = "multiply"):
    try:
        match math_operation:
            case "multiply":
                return arg1 * arg2
            case "add":
                return arg1 + arg2
            case "subtract":
                return arg1 - arg2
            case "divide":
                return arg1 / arg2
            case "modulo":
                return arg1 % arg2
            case "int_divide":
                return arg1 // arg2
            case "power":
                return arg1 ** arg2
            case _:
                print(f"Unsupported math operator. " +
                      "Please use ONLY the valid operator: " +
                      "add, subtract, multiply, divide, modulo, " +
                      "int_divide (for integer division) and power")
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

# Task 4: Data Type Conversion
def  data_type_conversion(value, data_type): # float, str, int
    data_type_final = data_type
    if isinstance(data_type, str):
        if data_type == "float":
            data_type_final = float
        elif data_type == "int":
            data_type_final = int
        elif data_type == "str":
            data_type_final = str
    try:
        return data_type_final(value)
    except TypeError: # value = None
        return f"You can't convert {value} into a {data_type}."
    except ValueError: # value = "str", data_type = float or int
        return f"You can't convert {value} into a {data_type}."

# Task 5: Grading System, Using *args
def grade(*args):
    try:
        avg_grade = sum(args) / len(args)
        if avg_grade >= 90:
            return "A"
        if avg_grade >= 80:
            return "B"
        if avg_grade >= 70:
            return "C"
        if avg_grade >= 60:
            return "D"
        return "F"
    except TypeError: # value = non numeric
        return f"Invalid data was provided."
    except ZeroDivisionError: # empty args list
        return "Invalid data was provided."

# Task 6: Use a For Loop with a Range
def repeat(txt, count):
    result = ""
    for i in range(count):
        result += txt
    return result    
        
# Task 7: Student Scores, Using **kwargs
def student_scores(pos, **kwargs): # where pos is "best" or "mean"
    if pos == "best":
        best_score = -1
        student_name = None
        for name, score in kwargs.items():
            if score > best_score:
                best_score = score
                student_name = name
        return student_name
    if pos == "mean":
        return sum(kwargs.values()) / len(kwargs)

# Task 8: Titleize, with String and List Operations
little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
def titleize(str):
    words = str.split()
    result = []
    # FIRST element in collection should be ALWAYS capitalized
    result.append(words[0].capitalize())
    # iterate collection from the SECOND to the PENULTIMATE element
    for word in words[1:-1]:
        # result.append(word if word in little_words else word.capitalize())
        if word in little_words:
            result.append(word)
        else:
            result.append(word.capitalize())
    # LAST element in collection should be ALWAYS capitalized
    result.append(words[-1].capitalize())
    return " ".join(result)

# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(text):
    vowels = "aeiou"
    words = text.split()
    result = []

    for word in words:
        # Rule 1: starts with a vowel
        if word[0] in vowels:
            result.append(word + "ay")
        
        # Rule 3: special case "qu"
        elif word.startswith("qu"):
            result.append(word[2:] + "quay")
        
        # Rule 2: starts with consonants
        else:
            consonant_cluster = ""
            i = 0
            while i < len(word) and word[i] not in vowels:
                # special case: qu inside a consonant cluster
                if word[i:i+2] == "qu":
                    consonant_cluster += "qu"
                    i += 2
                else:
                    consonant_cluster += word[i]
                    i += 1
            
            result.append(word[i:] + consonant_cluster + "ay")
    
    return " ".join(result)
