import sys

def linux_interaction():
  assert('linux' in sys.platform),"Function only runs on linux"

try:
  linux_interaction()
except AssertionError as error:
    print(error)
    print('that function does not run here')

try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as error:
    print(error)
    print('Could not open file.log')


