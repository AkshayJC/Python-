class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        h = self.hour + other.hour
        m = self.minute + other.minute
        s = self.second + other.second

        m += s // 60
        s = s % 60

        h += m // 60
        m = m % 60

        return Time(h, m, s)

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

print("Time 1")
h1 = int(input("Enter hour: "))
m1 = int(input("Enter minute: "))
s1 = int(input("Enter second: "))
t1 = Time(h1, m1, s1)

print("\nTime 2")
h2 = int(input("Enter hour: "))
m2 = int(input("Enter minute: "))
s2 = int(input("Enter second: "))
t2 = Time(h2, m2, s2)

t3 = t1 + t2
print("\nTotal Time:", t3)