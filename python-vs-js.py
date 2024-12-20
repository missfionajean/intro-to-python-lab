# --- GET NAME ---
def getName():
    name = input("What is your name? ")
    return name

print("Get Name Test:")
print(getName())


# --- REVERSE IT ---
test = "a man, a plan, a canal, panama"

def reverseIt(string):
    reverse = ""
    for letter in string:
        reverse = letter + reverse
    return reverse

print("Reverse It Tests:")
print(reverseIt(test))

# simpler solution
def simpleReverseIt(string):
    return string[::-1]

print(simpleReverseIt(test))


# --- SWAP EM ---
def swapEm():
    a = 10
    b = 30
    temp = a
    a = b
    b = temp
    print(a,b)

print("Swap Em Test:")
swapEm()


# --- MULTIPLY LIST ---
def multiplyList(list):
    total = 1
    if len(list) > 0:
        for num in list:
            total = total * num
    return total
        
test1 = []
test2 = [2,5,7]
test3 = [0,6,25]

print("Multiply List Tests:")
print(multiplyList(test1))
print(multiplyList(test2))
print(multiplyList(test3))


# --- FIZZ BUZZER ---
def fizzBuzzer(x):
    if x % 3 == 0 and x % 5 == 0:
        return "fizzbuzz"
    elif x % 3 == 0:
        return "fizz"
    elif x % 5 == 0:
        return "buzz"
    else:
        return "archer"

print("Fizzbuzz Tests:")
print(fizzBuzzer(15))
print(fizzBuzzer(6))
print(fizzBuzzer(10))
print(fizzBuzzer(7))


# --- NTH FIBONACCI ---
def nthFib():
    fibs = [1,1]
    num = input("Which fibonacci number do you want? (Enter a whole number) ")
    while len(fibs) < int(num):
        next = fibs[-1] + fibs[-2]
        fibs.append(next)
    print(fibs[-1],"is the fibonacci number at position",num)

print("Nth Fib Tests:")
nthFib()


# --- SEARCH LIST ---
def searchList(list,value):
    return value in list

print("Search List Tests:")
print(searchList([1,2,3,4],3))
print(searchList([1,2,3,4],7))


# --- PALINDROME ---
def isPalindrome(str):
    return str == str[::-1]

print("Palindrome Tests:")
print(isPalindrome("tacocat"))
print(isPalindrome("taihlor"))
print(isPalindrome("racecar"))


# --- HAS DUPES ---
def hasDupes(list):
    for val in list:
        if list.count(val) > 1:
            return True
    return False

print("Has Dupes Tests:")
print(hasDupes([1,2,3,4,5]))
print(hasDupes([1,2,3,2,5]))
print(hasDupes([1,5,6,7,10]))