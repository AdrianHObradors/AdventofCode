# Need to add an exception for numbers shorter than one

def get_lookie(number):
    step = 1
    answer = ""
    for i in range(len(number) - 1):
        if number[i] == number[i+1]:
            step += 1
        else:
            answer += str(step) + number[i]
            step = 1
    answer += str(step) + number[-1]
    return answer


value = "1321131112"
for i in range(50):
    value = get_lookie(value)
print(value)
print(len(value))
