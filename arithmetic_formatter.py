import re


def arithmetic_arranger(problems, display=False):

    no_of_equations = len(problems)
    space = "    "
    if no_of_equations > 5:
        return "Error: Too many problems."
    for item in problems:
        if item.find("*") != -1 or item.find("/") != -1:
            return "Error: Operator must be '+' or '-'."
        else:
            continue

    # remove whitespace and group equations
    prob_sort = [i.split(" ") for i in problems]

    for equation in prob_sort:
        # Find any non digit occurances
        if re.findall(r"\D", equation[0]) != [] or re.findall(r"\D", equation[2]) != []:
            return "Error: Numbers must only contain digits."
        # Find any digits greater than 4 in length
        if len(equation[0]) > 4 or len(equation[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        # append length of longest digit to each equation
        max_len = max(len(digit) for digit in equation)
        equation.append(max_len + 1)

    # Create output string
    string1 = []
    string2 = []
    string3 = []
    string4 = []
    for equation in prob_sort:
        string1.append(f"{equation[0]}".rjust(equation[3] + 1))
        string2.append(f"{equation[1]}" + f"{equation[2]}".rjust(equation[3]))
        string3.append("-" * (equation[3] + 1))
        string4.append(
            f"{eval(equation[0] + equation[1] + equation[2])}".rjust(equation[3] + 1)
        )
    string1 = space.join(string1)
    string2 = space.join(string2)
    string3 = space.join(string3)
    string4 = space.join(string4)

    if display == True:
        print(f"{string1}\n{string2}\n{string3}\n{string4}")
    else:
        print(f"{string1}\n{string2}\n{string3}")


print(arithmetic_arranger(["444 + 5", "5554 - 3", "6 + 7", "4447 - 5778", "4 - 1"]))
