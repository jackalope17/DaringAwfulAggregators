class Labs:
  def __init__(self):
    pass

  def runlab2_1_1_7(self):
    #1. use the print() function to print the line Hello, Python! to the screen. Use double quotes around the string;
    print('Hello, Python!')
   
    #2. having done that, use the print() function again, but this time print your first name;
    print('\nKane')
   
    #3. remove the double quotes and run your code. Watch Python's reaction. What kind of error is thrown?
    #print(Kane)  Name error, Kane not defined
       # Traceback (most recent call last):
      #File "main.py", line 6, in <module>
       # labs.runlab2_1_1_7()
     # File "/home/runner/DaringAwfulAggregators/Labs.py", line 11, in runlab2_1_1_7
      # print(Kane)
    #NameError: name 'Kane' is not defined
   
    #4. then, remove the parentheses, put back the double quotes, and run your code again. What kind of error is thrown this time?
    #print'Kane'  Syntax error
       # Traceback (most recent call last):
      #File "main.py", line 2, in <module>
        #from Labs import Labs
     # File "/home/runner/DaringAwfulAggregators/Labs.py", line 22
       # print'Kane'
            #^
    #SyntaxError: invalid syntax


  def runlab2_1_1_19(self):
    #1. Modify the first line of code in the editor, using the sep and end keywords, to match the expected output. Use the two print() functions in the editor.Don't change anything in the second print() invocation.
    #Expected output
    #Programming***Essentials***in...Python
    print("Programming","Essentials","in",sep='***',end='...')
    print("Python")


  def runlab2_1_1_20(self):
    #starting arrow size below
    print("    *","   * *","  *   *"," *     *","***   ***","  *   *","  *   *","  *****", sep='\n')

    #1. minimize the number of print() function invocations by inserting the \n sequence into the strings
    #make the arrow twice as large (but keep the proportions)
    print("       *","    *     *","  *         *"," *           *","****       ****","   *       *","   *       *","   *********", sep='\n'*2)

    #2. duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using the following trick: "string" * 2 will produce "stringstring" (we'll tell you more about it soon)
    print("       *       "*2,"    *     *    "*2,"  *         *  "*2," *           * "*2,"****       ****"*2,"   *       *   "*2,"   *       *   "*2,"   *********   "*2, sep='\n'*2)
    
    #3. remove any of the quotes, and look carefully at Python's response; pay attention to where Python sees an error - is this the place where the error really exists?
      #bad code:  print("       *       "*2,"    *     *    "*2,"  *         *  "*2," *           * "*2,****       *****2,"   *       *   "*2,"   *       *   "*2,"   *********   "*2, sep='\n'*2)
      #yes, it is pointing to where the quotes are gone.

    #4. do the same with some of the parentheses;
      #bad code:  print"       *       "*2,"    *     *    "*2,"  *         *  "*2," *           * "*2,"****       ****"*2,"   *       *   "*2,"   *       *   "*2,"   *********   "*2, sep='\n'*2
    
    #5.change any of the print words into something else, differing only in case (e.g., Print) - what happens now?
      #bad code:  Print("       *       "*2,"    *     *    "*2,"  *         *  "*2," *           * "*2,"****       ****"*2,"   *       *   "*2,"   *       *   "*2,"   *********   "*2, sep='\n'*2)
      #it no longer knows what do with the code
    
    #6. replace some of the quotes with apostrophes; watch what happens carefully.
      #it works as intended


  def runlab2_1_2_11(self):
    #Write a one-line piece of code, using the print() function, as well as the newline and escape characters, to match the expected result outputted on three lines.
    print('"I\'m"')
    print('""learning""')
    print('"""Python"""')


  def runlab2_1_4_7(self):
    #1. create the variables: john, mary, and adam;
    #2. assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
    john = 1
    mary = 2
    adam = 3

    #3. having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma;
    print(john,',',mary,',',adam,sep='')

    #4. now create a new variable named totalApples equal to addition of the three former variables.
    totalApples = john + mary + adam

    #5. print the value stored in totalApples to the console;
    print(totalApples)


  def runlab2_1_4_9(self):
    #1. Bearing in mind that 1 mile is equal to approximately 1.61 kilometers, complete the program in the editor so that it converts:
    #miles to kilometers;
    #kilometers to miles.
    #Do not change anything in the existing code. Write your code in the places indicated by ###. Test your program with the data we've provided in the source code.
    #Starting code
    #kilometers = 12.25
    #miles = 7.38

    #miles_to_kilometers = ###
    #kilometers_to_miles = ###

    #print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
    #print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

    #My code
    kilometers = 12.25
    miles = 7.38

    miles_to_kilometers = miles * 1.61
    kilometers_to_miles = kilometers / 1.61

    print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
    print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
    

  def runlab2_1_4_10(self):
    #1. Take a look at the code in the editor: it reads a float value, puts it into a variable named x, and prints the value of a variable named y. Your task is to complete the code in order to evaluate the following expression:

    #3x3 - 2x2 + 3x - 1

    #The result should be assigned to y.
    #Remember that classical algebraic notation likes to omit the multiplication operator - you need to use it explicitly. Note how we change data type to make sure that x is of type float.
    #Strating code
    #x =  # hardcode your test data here
    #x = float(x)
    # write your code here
    #print("y =", y)

    #My code
    x =  0
    x = float(x)
    y = 3*x**3-2*x**2+3*x-1
    print("y =", y)


  def runlab2_1_6_9(self):
    #1. Your task is to complete the code in order to evaluate the results of four basic arithmetic operations.The results have to be printed to the console.
    varA = float(input('Enter a number here: '))
    varB = float(input('Enter a second number here: '))

    print('\n', varA + varB)
    print('\n', varA - varB)
    print('\n', varA * varB)
    print('\n', varA / varB)

    print("\nThat's all, folks!")


  def runlab2_1_6_10(self):
    #1. Your task is to complete the code in order to evaluate the following expression:
    #The result should be assigned to y. Be careful - watch the operators and keep their priorities in mind. Don't hesitate to use as many parentheses as you need.
    x = float(input("Enter value for x: "))

    y = (1/(x+(1/(x+(1/(x+(1/x)))))))

    print("y =", y)


  def runlab2_1_6_11(self):
    #1. Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.

    #For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.

    #Don't worry about any imperfections in your code - it's okay if it accepts an invalid time - the most important thing is that the code produce valid results for valid input data.

    hour = int(input("Starting time (hours): "))
    mins = int(input("Starting time (minutes): "))
    dura = int(input("Event duration (minutes): "))
    newM = mins+dura
    newH = newM/60
    newH2 = int(newH+hour)
    endM = newM%60
    endH = newH2%24

    print(endH,endM, sep=':')


  def runlab3_1_1_12(self):
    #1. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:

    #*if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was the so-called tax relief)
    #*if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
    #Your task is to write a tax calculator.
    #2. It should accept one floating-point value: the income.
    #3. Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you - you'll find it in the skeleton code in the editor.
    #Note: this happy country never returns money to its citizens. If the calculated tax is less than zero, it only means no tax at all (the tax is equal to zero). Take this into consideration during your calculations.

    income = float(input("Enter the annual income: "))
    
    if income <= 85528:
      tax = (income*.18)-556.02
    else:
      tax = ((income-85528)*.32)+14839.02
    if tax > 0:
      tax = round(tax, 0)
      print("The tax is:", tax, "thalers")
    else:
      print('You have no tax to pay this year.')


  def runlab3_1_1_13(self):
    #1. As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.

    #2. Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

    #*if the year number isn't divisible by four, it's a common year;
    #*otherwise, if the year number isn't divisible by 100, it's a leap year;
    #*otherwise, if the year number isn't divisible by 400, it's a common year;
    #*otherwise, it's a leap year.
    #*Look at the code in the editor - it only reads a year number, and needs to be completed with the instructions implementing the test we've just described.

    #3. The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.

    #4. It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period. Tip: use the != and % operators.

    year = int(input("Enter a year: "))

    if year<1581:
      print('Not within the Gregorian calendar period')
    elif year%4 != 0:
      print('Common Year')
    elif year%100 != 0:
      print('Leap Year')
    elif year%400 != 0:
      print('Common Year')
    else:
      print('Leap Year')


  def runlab3_1_2_3(self):
    #1. A junior magician has picked a secret number. He has hidden it in a variable named secret_number. He wants everyone who run his program to play the Guess the secret number game, and guess what number he has picked for them. Those who don't guess the number will be stuck in an endless loop forever! Unfortunately, he does not know how to complete the code.

    #2. Your task is to help the magician complete the code in the editor in such a way so that the code:

    #3. will ask the user to enter an integer number;
    #4. will use a while loop;
    #5. will check whether the number entered by the user is the same as the number picked by the magician. If the number chosen by the user is different than the magician's secret number, the user should see the message "Ha ha! You're stuck in my loop!" and be prompted to enter a number again. If the number entered by the user matches the number picked by the magician, the number should be printed to the screen, and the magician should say the following words: "Well done, muggle! You are free now."

    secret_number = 777

    print(
    '''
    +================================+
    | Welcome to my game, muggle!    |
    | Enter an integer number        |
    | and guess what number I've     |
    | picked for you.                |
    | So, what is the secret number? |
    +================================+
    ''')

    usernum = int(input('Choose an integer number: '))

    while usernum != secret_number:
      print('Ha Ha! You\'re stuck in my loop!')
      usernum = int(input('Try another integar number: '))

    print(usernum, 'Well done, muggle! You are free now.')


  def runlab3_1_2_6(self):
    #1. Do you know what Mississippi is? Well, it's the name of one of the states and rivers in the United States. The Mississippi River is about 2,340 miles long, which makes it the second longest river in the United States (the longest being the Missouri River). It's so long that a single drop of water needs 90 days to travel its entire length!

    #2. The word Mississippi is also used for a slightly different purpose: to count mississippily.If you're not familiar with the phrase, we're here to explain to you what it means: it's used to count seconds.

    #3. The idea behind it is that adding the word Mississippi to a number when counting seconds aloud makes them sound closer to clock-time, and therefore "one Mississippi, two Mississippi, three Mississippi" will take approximately an actual three seconds of time! It's often used by children playing hide-and-seek to make sure the seeker does an honest count.

    #4. Your task is very simple here: write a program that uses a for loop to "count mississippily" to five. Having counted to five, the program should print to the screen the final message "Ready or not, here I come!"

    #5. Use the skeleton we've provided in the editor.

    #EXTRA INFO
    # Note that the code in the editor contains two elements which may not be fully clear to you at this moment: the import time statement, and the sleep() method. We're going to talk about them soon.
    # For the time being, we'd just like you to know that we've imported the time module and used the sleep() method to suspend the execution of each subsequent print() function inside the for loop for one second, so that the message outputted to the console resembles an actual counting. Don't worry - you'll soon learn more about modules and methods.

    import time

    for i in range(5):
      time.sleep(1)
      print(i + 1, 'Mississippi')

    print('Ready or not, here I come!')


  def runlab3_1_2_10(self):
    #1. Your task here is very special: you must design a vowel eater! Write a program that uses:

    #2. a for loop;
    #3. the concept of conditional execution (if-elif-else)
    #4. the continue statement.
    #5. Your program must:

    #6. ask the user to enter a word; use userWord = userWord.upper() to convert the word entered by the user to upper case; we'll talk about the so-called string methods and the upper() method very soon - don't worry;
    #7. use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
    #8. print the uneaten letters to the screen, each one of them on a separate line.

    userWord = input('Please enter a word: ', )
    userWord = userWord.upper()
    vowels = ('A','E','I','O','U')

    for letter in userWord:
      if letter in vowels:
        userWord = userWord.replace(letter,'')
        continue
    else:
      print(userWord)
      # for letter in userWord:
      #   print(letter)


  def runlab3_1_2_14(self):
    #1. Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.
    # Note: the height is measured by the number of fully completed layers - if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.

    #2. They are building a pyramid. Their pyramid is a bit weird, as it is actually a pyramid-shaped wall - it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.
    #3. must loop, handle bad input for data, 
    run = 1
    while run == 1:      
      
      while True:
        try:
          blocks = int(input("Enter the number of blocks: "))
          break
        except ValueError:
          print("The value entered was not an integer. Please reenter your value.")
      
      height = 0
      inLayer = 1

      while inLayer <= blocks:
        height += 1
        blocks -= inLayer
        inLayer += 1

      print("The height of the pyramid:", height)
      redo = (input('Would you like to recalculate?(y/n): '))
      redo = redo.upper()
      while redo not in 'YN':
        
          redo = input('Please enter either "y" to run the program again, or "n" to stop the program.\nWould you like to recalculate?(y/n): ').upper()

      if redo == 'Y':
          run = 1
      elif redo == 'N':
          run = 0
          

  def runlab3_1_4_6(self):
    #1. There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.
    #2. write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (step 1)
    #3. write a line of code that removes the last element from the list (step 2)
    #4. write a line of code that prints the length of the existing list (step 3.)
    hatList = [1, 2, 3, 4, 5]

    newHatNum = input('Please choose a number to add to the hat: ', )
    newHatNum = int(newHatNum)
    hatList[2] = newHatNum
    
    del hatList[4]

    print('The length of your list is:', len(hatList))
    print(hatList)


  def runlab3_1_4_13(self):
    #1. Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:
    # step 1: create an empty list named beatles;
    # step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
    # step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
    # step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
    # step 5: use the insert() method to add Ringo Starr to the beginning of the list.

    beatles = []
    print("Step 1:", beatles)

    beatles.append('John Lennon')
    beatles.append('Paul McCartney')
    beatles.append('George Harrison')
    print("Step 2:", beatles)

    addition1 = input('Please add "Stu Sutcliffe" to the group:', )
    addition2 = input('Please add "Pete Best" to the group:', )
    for i in beatles:
      beatles.append(addition1)
      beatles.append(addition2)
      break
    print("Step 3:", beatles)

    del beatles[3]
    del beatles[3]
    print("Step 4:", beatles)

    beatles.insert(0, 'Ringo Starr')
    print("Step 5:", beatles)

    print("The Fab", len(beatles))


  def runlab3_1_6_9(self):
    #1. Imagine a list - not very long, not very complicated, just a simple list containing some integer numbers. Some of these numbers may be repeated, and this is the clue. We don't want any repetitions. We want them to be removed.

    #2. Your task is to write a program which removes all the number repetitions from the list. The goal is to have a list in which all the numbers appear not more than once.

    #3. Note: assume that the source list is hard-coded inside the code - you don't have to enter it from the keyboard. Of course, you can improve the code and add a part that can carry out a conversation with the user and obtain all the data from her/him.

    #Hint: we encourage you to create a new list as a temporary work area - you don't need to update the list in situ.

    myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
    print("The original list is: " + str(myList))
    newList = []

    [newList.append(x) for x in myList if x not in newList]

    myList = newList[:]

    print ("The list after removing duplicates: " + str(myList))


  def runlab4_1_3_8(self):
    #1. Your task is to write and test a function which takes one argument (a year) and returns True if the year is a leap year, or False otherwise.

    #2. Your task is to write and test a function which takes two arguments (a year and a month) and returns the number of days for the given month/year pair (while only February is sensitive to the year value, your function should be universal).

    #3. The initial part of the function is ready. Now, convince the function to return None if its arguments don't make sense.

    #4. Of course, you can (and should) use the previously written and tested function (LAB 4.1.3.6). It may be very helpful. We encourage you to use a list filled with the months' lengths. You can create it inside the function - this trick will significantly shorten the code

    #5. Your task is to write and test a function which takes three arguments (a year, a month, and a day of the month) and returns the corresponding day of the year, or returns None if any of the arguments is invalid.
    from datetime import datetime, date
    yr = int(input("Enter a year: "))
    mo = int(input("Enter a month: "))
    dy = int(input("Enter a day: "))

    def isYearLeap(year):

      if yr<1581:
        return False
        #print('Not within the Gregorian calendar period')
      elif yr%4 != 0:
        return False
        #print('Common Year')
      elif yr%100 != 0:
        return True
        #print('Leap Year')
      elif yr%400 != 0:
        return False
        #print('Common Year')
      else:
        return True
        #print('Leap Year')

    # testData = [1900, 2000, 2016, 1987]
    # testResults = [False, True, True, False]
    # for i in range(len(testData)):
    #   yr = testData[i]
    #   print(yr,"->",end="")
    #   result = isYearLeap(yr)
    #   if result == testResults[i]:
    #     print("OK")
    #   else:
    #     print("Failed")

    
    def daysInMonth(year, month):
      leapYr = isYearLeap(year)

      #if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
      if(mo == 1 or mo == 3 or mo == 5 or mo == 7 or mo == 8 or mo == 10 or mo == 12):
        return 31
      elif((mo == 2) and (leapYr == True)):
        return 29
      elif(mo == 2):
        return 28
      else:
        return 30

    # testYears = [1900, 2000, 2016, 1987]
    # testMonths = [2, 2, 1, 11]
    # testResults = [28, 29, 31, 30]
    # for i in range(len(testYears)):
    #   yr = testYears[i]
    #   mo = testMonths[i]
    #   print(yr, mo, "->", end="")
    #   result = daysInMonth(yr, mo)
    #   if result == testResults[i]:
    #     print(result)
    #     print("OK")
    #   else:
    #     print(result)
    #     print("Failed")


    def dayOfYear(year, month, day):

      if isYearLeap(yr):
        K = 1
      else:
        K = 2
      N = int((275 * mo) / 9.0) - K * int((mo + 9) / 12.0) + dy - 30
      return N

    print(dayOfYear(yr, mo, dy))