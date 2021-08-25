#---------------------------Making Necessary Imports!

#import pandas as pd;
#import numpy as np;

#----------------------------------------------------

#---------------------------Initializing the Constants to be Used in The Program:

# "adult.data" file.
trainingData = "G:\MLDA-1\Proj-1\Data\adult.data"; 
# "adult.test" file.
testData = "G:\MLDA-1\Proj-1\Data\adult.test";
# Attributes in the data.
colNames = ["age","workclass","fnlwgt","education","education-num","marital-status",
            "occupation","relationship","race","sex","captial-gain","capital-loss",
            "hours-per-week","native-country","income"];

#----------------------------------------------------

#--------------------------Reading The Required Data:
def readRequiredData():
    inputData = pd.read_fwf(trainingData, names=colNames);
    return inputData;
# Print the few rows from the inputData as well!
# testData = pd.read_; # Read the test file as well!

#--------------------------Pre-Processing Data:

# Write code for pre-processing the data!

#----------------------------------------------------


#----------------------------Utility Functions:



#-----------------------------------------------------

#-----------------------------Main Method:

def main():
    # Write the main code!
    return 0;

if __name__ == "__main__":
    main();
#------------------------------------------------------
