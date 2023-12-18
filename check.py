import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        variable_from_argument = sys.argv[1]
        print(f"Variable from argument: {variable_from_argument}")
        
    else:
        print("No arguments provided!!!!")
