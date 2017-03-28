import os,sys,time



def printLotsOfVariables():
	"""
	 Write a large number of variables with a number following the variable
	 output ex: record1,record2...
	"""
	count = raw_input("Count: ")
	name = raw_input("Name:")
	thing = 1
	while thing <= int(count):
		if thing == int(count):
			sys.stdout.write('%s%d'%(name,thing))
		else:
			sys.stdout.write('%s%d,'%(name,thing))
		
		thing = thing +1

	print "\n\nDone printing %d instances of the variable: %s" % (int(count),name)
	sys.stdout.flush()


			
def allfunctions():
    	"""
		Print out descriptions of functions in this file. Would be better to access and print the docstrings of the functions.
		"""
	functionDict = {
	'printLotsOfVariables':'Prints out a specified number of a numbered variable in a comma separated list: ex: record1,record2...'
	
	}
	print "\n---------------\-\-\-----------------"
	print "------- Functions Available ---------"
	print "---------------\-\-\-----------------\n"
	dumpclean(functionDict)
 	print "\n---------------\-\-\-----------------"
	print "---------------\-\-\-----------------\n"



def dumpclean(obj):
    """
	Prints out dictionaries, lists out cleanly. Got this from a Stack Overflow: http://stackoverflow.com/questions/15785719/how-to-print-a-dictionary-line-by-line-in-python

	"""
    if type(obj) == dict:
        for k, v in obj.items():
            if hasattr(v, '__iter__'):
                print k
                dumpclean(v)
            else:
                print ('%s : %s' % (k, v))
    elif type(obj) == list:
        for v in obj:
            if hasattr(v, '__iter__'):
                dumpclean(v)
            else:
                print v
    else:
        print obj


def menu():
    """
    The menu for the Utility File.
    """
    menubool = True

    while menubool == True:
        print " "
        print "--------------------------\-\-\----\-- | --/----/-/-/-----------------------------"
        print "---------------------------\-\-\--   Menu!   --/-/-/------------------------------"
        print "----------------------------\-\-\----\ | /----/-/-/-------------------------------\n"
        print "Those who forget to script are doomed to repeat their work. -- Jeffery Hicks\n"
        print "\tSelect the utility you would like to perform: "
        print "\t1 - Display all available Utility Functions."
        print "\t2 - Print multiple variable names"
        print "\t6 - Exit."
        menuoption = raw_input("Choice: ")

        if menuoption == '1':
            allfunctions()

        elif menuoption == '2':
            printLotsOfVariables()

        
        elif menuoption =='6':
            exit()        	
        else:
        	time.sleep(1)
        	menu()

      	time.sleep(1)


menu()


