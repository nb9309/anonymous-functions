# anonymous-functions

Anonymous OR Lambda Functions--Most IMP
			========================================================
=>Anonymous functions are those which does not contain any Name explicitly.
=>In otherwords Name-Less Functions are called Anonymous Functions.
=>The purpose of Anonymous Functions is that "To Implement OR Perform Instant Operations".
=>Instant Operations are those which are used at that point of time only and No Longer Interested to Use in Other Part 
    of the Project. 
=>The Anonymous  Functions contains Single Executable Statement for Solving tiny Problems But Not Recommended 
     to Solve Big Operations.
=>The Anonymous  Functions returns the Result automatically / Implicitly and Need to use return Statement.
=>To Define Anonymous  Functions, we use a Key word called lambda and hence Anonymous  Functions are called 
    lambda Functions.
------------------------------------------------------------------------------------------------------------------------------------------------------------------
Syntax:		varname = lambda params-list : Expression
------------------------------------------------------------------------------------------------------------------------------------------------------------------
=>here varname Represents an Object of type <class,'function'>. So that we use that Varname as Function Call
=>here lambda is keyword used for Define Anonymous Functions
=>here params-list Represents List of Variables used for Storing the Input(s) coming From Functions.
=>Expression represents single Executable statement and Provides Solution for tiny Problems a dn whose Result 
    Returns automatuically (No Need to use return statement).
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
			Question: Define a Function for addition of two Numbers
***************************************************************************************************************************************************
		Normal Function						Anonymous Function
	--------------------------------------				------------------------------------------------------------
def  sumop(a,b):							addop = lambda a,b : a+b
	return (a+b)

#Main Program							   #Main Program
res=sumop(10,20)							res=addop(4,5) # Anonymous Function Call
print("sum=",res)							print("sum=",res)
