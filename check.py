import sys

if __name__ == "__main__":
    n = len(sys.argv)
    result = 1
    for i in range(1, n):
        print(sys.argv[i])
    for i in range(1, n):
        result *= float(sys.argv[i])
    print("Result:", result)
