import matplotlib.pyplot as plt
import time as t

times = []
mistakes = 0

print("Program to check your typing speed. Type the word 'implementation' for 5 times")
input ("Press enter to continue.")

while len(times) < 5:
    start = t.time()
    word = input ("type the word: ")
    end = t.time()
    time_elapsed =end-start

    times.append(time_elapsed)

    if (word.lower() != "implementation"):
        mistakes +=1

print("You made"+ str(mistakes) + "mistakes.")
print("This is your typing speed")
t.sleep(3)

x =[1,2,3,4,5]
y =times
plt.plot(x,y)
legend = ["1","2","3","4","5"]
plt.xticks(x,legend)
plt.ylabel("Time in seconds")
plt.xlabel("Attempts")
plt.title('Your typing evaluation')
plt.show()
