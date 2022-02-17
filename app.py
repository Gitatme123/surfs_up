# import the flask dependency 
from flask import Flask
 # create a new flask instance ( a singuler version of something in programming)
# # the __name__ variable denotes the name of the current function
# #   we use it to determine if the code is bring run from the terminal or if it was
# #   imported into another piece of code. It's called a magic method in Python
app = Flask(__name__)
# #create the flask routine, define the starting point known as the root
# # the slash notes that we want to put our data at the root of our routes. 
# #     The forward slash is commonly known as the highest level of hierarchy in any computer system
@app.route('/')
def hello_world():
  return 'Hello world'
