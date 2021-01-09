import threading, time

def calc_square(number):
    time.sleep(100)
    print('Square:' , number * number)

def calc_quad(number):
    print('Quad:' , number * number * number * number)

if __name__ == "__main__":
    number = 7
    thread1 = threading.Thread(target=calc_square, args=(number,))
    thread2 = threading.Thread(target=calc_quad, args=(number,))

    # Will execute both in parallel
    thread1.start()
    thread2.start()

    print("Main process....")

    # Joins threads back to the parent process, which is this
    # program
    thread1.join()
    thread2.join()
    # This program reduces the time of execution by running tasks in              parallel