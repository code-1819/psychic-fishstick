from socket import *
import time

startTime = time.time()

if __name__ == '__main__':
    target = input("Enter Host for Scanning: ")  # Use input() to get user input
    t_IP = gethostbyname(target)  # Pass the target to gethostbyname()
    print("Starting Scanning on Host: ", t_IP)

    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        if conn == 0:
            print("Port %d: OPEN" % (i,))  # Fix formatting
        s.close()

print("Time Taken: ", time.time() - startTime)
