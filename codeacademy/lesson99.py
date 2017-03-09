grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def all_grades(grades):
    for i in range(len(grades)):
        print grades[i]

def grades_sum(scores):
    total = 0
    for i in range(len(scores)):
        total += scores[i]
    return total


def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average


def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    return variance / len(scores)


def grades_std_deviation(variance):
    return variance ** 0.5

variance = grades_variance(grades)

print all_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)
