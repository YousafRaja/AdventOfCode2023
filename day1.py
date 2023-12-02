def processLine(line):
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    originalLine = line 
    furthestIndex = -1
    furthestDigit = "" 
    for digit in digits:
        lastIndex = -1
        tempLine = originalLine
        while digit in tempLine:
            index = tempLine.find(digit)
            lastIndex = index 
            modifiedDigit = "".join(["*" for _ in digit])
            tempLine = tempLine[:index] + modifiedDigit + tempLine[index+len(digit):]
        if lastIndex > furthestIndex:
            furthestIndex = lastIndex
            furthestDigit = str(digits.index(digit) + 1) 
    
    return [furthestIndex, furthestDigit]

def processLine_closest(line):
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    closestIndex = float('inf')
    closestDigit = ""
    for digit in digits:
        index = line.find(digit)
        if index >= 0 and (index < closestIndex):
            closestIndex = index 
            closestDigit = digit
    
    return [closestIndex, closestDigit]

# Open the file in read mode
input_file = 'input'
calibrationSum = 0
with open(input_file, 'r') as file:
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    # Read each line in a loop
    for line in file:
        # Each line can be processed here
        line = line.strip()
        starting_line = line
        minIndex = len(line)
        minDigit = ""
        for i in range(len(line)):
            if line[i].isnumeric():
                minIndex = i 
                minDigit = line[i]
                break
       
        [closestIndex, closestDigit] = processLine_closest(line)
        if closestDigit and minDigit:
            if minIndex > closestIndex:
                minDigit = str(digits.index(closestDigit) + 1) 
        elif closestDigit and not minDigit:
            minDigit = str(digits.index(closestDigit) + 1)            
        
            

        maxIndex = -1
        maxDigit = ""
        for i in range(len(line)-1, -1, -1):
            if line[i].isnumeric():
                maxIndex = i
                maxDigit = line[i]
                break 

        [furthestIndex, furthestDigit] = processLine(line)

        if furthestDigit and maxDigit:
            maxDigit = maxDigit if maxIndex > furthestIndex else furthestDigit
        elif furthestDigit and not maxDigit:
            maxDigit = furthestDigit
        elif not furthestDigit and not maxDigit:
            maxDigit = minDigit


        number = minDigit + maxDigit

        print(f"{line} {number}")
        calibrationSum += int(number)

print(calibrationSum)
