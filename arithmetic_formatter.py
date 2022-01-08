import re


def arithmetic_arranger(problems, display="True"):
    no_of_equations = len(problems)
    space = "    "
    if no_of_equations > 5:
        return "Error: Too many problems"
    for item in problems:
        if item.find("*") != -1 or item.find("/") != -1:
            return print("Error: Operator must be '+' or '-'")
        else:
            continue

    # remove whitespace
    prob_sort = [i.split(" ") for i in problems]

    for equation in prob_sort:
        # Find any non digit occurances
        if re.findall(r"\D", equation[0]) != [] or re.findall(r"\D", equation[2]) != []:
            return print("Error: Numbers must only contain digits.")
        # Find any digits greater than 4 in length
        if len(equation[0]) > 4 or len(equation[2]) > 4:
            return print("Error: Numbers cannot be more than four digits.")
        # append length of longest digit to each equation
        max_len = max(len(digit) for digit in equation)
        equation.append(max_len + 1)

    # Create output strings
    string1 = ""
    string2 = ""
    string3 = ""
    string4 = ""
    for equation in prob_sort:
        string1 = string1 + f"{equation[0]}".rjust(equation[3] + 1) + space
        string2 = (
            string2 + f"{equation[1]}" + f"{equation[2]}".rjust(equation[3]) + space
        )
        string3 = string3 + "-" * (equation[3] + 1) + space
        string4 = (
            string4
            + f"{eval(equation[0] + equation[1] + equation[2])}".rjust(equation[3] + 1)
            + space
        )

    if display == True:
        return print(f"{string1}\n{string2}\n{string3}\n{string4}\n")
    else:
        return None


arithmetic_arranger(["444 + 5", "5554 - 3", "6 + 7", "4447 - 5778", "4 - 1"])
