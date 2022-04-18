import os

def readClasses (fileName):
    ClassDict = {}
    inFile = open("./local_data/" + fileName, 'r')
    for line in inFile:
        line = line.strip()
        key, value = line.split('\t')
        ClassDict[key] = int(value)
    return ClassDict
    
def totalCredits (theDictionary):
    totalCredits = sum(theDictionary.values())
    return print("Total number of credits this semester: ", totalCredits)

def classesByDepartment(theDictionary, department):
    num = 0
    for item in theDictionary:
        if item.startswith(department):
            num += 1
    return print("The number of classes for this department is: ", num)

def isFullTime(theDictionary):
    return sum(theDictionary.values()) >= 12

def numOfClasses(theDictionary):
    return len(theDictionary)

def upperLevelCredits (theDictionary):
    creds = 0
    for k, v in theDictionary.items():
        if (courses := k.rsplit(' ')) and (len(courses) >= 2 and int(courses[1]) >= 300):
            creds+= v
    return print("Number of upper level classes is: ", creds)

def printClasses(theDictionary):
    width = 8
    print("%-5s % 20s" % ("\nClass Name", "Number of Credits"))
    print("-------------------------------")
    for k , v  in theDictionary.items():
        print("%-5s %15s" % (f'{k:<{width}}' , f'{v:>{width}}'))

def main():
    dictionary_file = os.getenv('DICTIONARY') or 'ClassDictionary.txt'
    ClassDict = readClasses(dictionary_file)
    totalCredits (ClassDict)
    classesByDepartment(ClassDict, 'CSCI')
    isFullTime(ClassDict)
    numOfClasses(ClassDict)
    upperLevelCredits (ClassDict)
    printClasses(ClassDict)
    print(ClassDict)
main()