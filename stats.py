"""Statistics for a list of marks."""
def average(marks):
    return sum(marks) / len(marks)
def highest(marks):
    return max(marks)
def lowest(marks):
    return min(marks)
def pass_count(marks, pass_mark):
    return len([mark for mark in marks if mark >= pass_mark])
