# This is the main program.

#To import module of the main package
import Package.PackageModule

#To import display function from the sp1.py module
# from Package.SubPackage1.sp1 import display
# display()

# Way 1: To import the function from the Package->subpackage->sp->class
import Package.SubPackage1.sp1
b = Package.SubPackage1.sp1.SubpackageClass
b.displayclass()

# Way 2: To import Every  function from the Package->subpackage->sp->class
from Package.SubPackage1.sp1 import *
displayFun1()
displayFun2()
displayFun3()
displayFun4()

