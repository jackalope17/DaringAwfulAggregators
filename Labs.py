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
    print("       *","    *     *","  *         *"," *           *","****       ****","   *       *","   *       *","   *********", sep='\n'*2)
    print("       *","    *     *","  *         *"," *           *","****       ****","   *       *","   *       *","   *********", sep='\n'*2)
    
    #3. remove any of the quotes, and look carefully at Python's response; pay attention to where Python sees an error - is this the place where the error really exists?
    
    #4. do the same with some of the parentheses;
    
    #5.change any of the print words into something else, differing only in case (e.g., Print) - what happens now?
    
    #6. replace some of the quotes with apostrophes; watch what happens carefully.