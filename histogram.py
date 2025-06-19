import matplotlib.pyplot as plt

marks=[60,70,81,23,56,87,89,91,90,100]
ranges = {
    "0-60": range(0, 61),
    "61-70": range(61, 71),
    "71-80": range(71, 81),
    "81-90": range(81, 91),
    "91-100": range(91, 101)
}

def get_histogram(marks,ranges):
    hist={key:0 for key in ranges}
    for mark in marks:
        for key,rng in ranges.items():
            if mark in rng:
                hist[key]=hist[key]+1
                break
    return hist

hist_data = get_histogram(marks, ranges)

plt.bar(hist_data.keys(), hist_data.values(), color='skyblue', edgecolor='black')
plt.xlabel("Grade Ranges")
plt.ylabel("Number of Students")
plt.title("Student Marks Distribution")
plt.xticks(rotation=45)  
plt.show()

        