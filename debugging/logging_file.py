import logging
logging.basicConfig(filename="./logs/myProgramLog.txt", level=logging.DEBUG, format="%(asctime)s - %(levelname)s -  %(message)s")


logging.debug("Start of the program.")
def factorial(num):
    logging.debug(f"Start of the factorial calculation for: {num=}")
    total = 1
    if num <= 1:
        return total
    else:
        for i in range(1, num+1):
            total *= i
            logging.debug(f"i is {i} and total is {total}")
        
        logging.debug(f"End of factorial calculation for: {num=}")
        return total


if __name__ == "__main__":
    # num = int(input("Enter the number: "))
    num = 6
    print(f"{num}! = {factorial(num)}")
    logging.debug(f"End of the program.")