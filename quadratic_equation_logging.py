
import math
import logging

LOG_FORMAT= "%(levelname)s %(asctime)s- %(message)s"
logging.basicConfig(filename="Customlog.Log",level=logging.DEBUG,format = LOG_FORMAT)

logger = logging.getLogger() # Root logger, we can specify name of this log object as well

def quadratic_formula(a,b,c):
	#compute Disciminant
	logger.info("#Quadratic Formula Params({0},{1},{2})".format(a,b,c))
	disc = b**2 - 4*a*c

	#Compute +ve and -ve roots
	logger.debug("#Compute +ve and -ve roots")
	root1 = (-b + math.sqrt(disc))//(2*a)
	root2 = (-b - math.sqrt(disc))//(2*a)

	#return +ve and -ve roots as tuples
	logger.debug("#Return +ve and -ve roots as tuples")
	return(root1,root2)

roots_1 = quadratic_formula(1,0,-4)
print(roots_1)
#roots_2 = quadratic_formula(1,0,1)
