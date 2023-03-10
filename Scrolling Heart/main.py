from getkey import getkey

def Ginput(str):
    """
    Now, this function is like the native input() function. It can accept a prompt string, print it out, and when one key is pressed, it will return the key to the caller.
    """
  
    print(str, end='')
    while 1+1==2:
        key = getkey()
        return key


file = open("heart.txt","rt")
content = file.readlines()
file.close()
pointer = 0
fpr = 0
fpc = 0
while True:
  inp = Ginput("")
  if content[fpr][fpc] == "*":
    print("*",end="",flush=True)
    pointer += 1
  else:
    print(" ",end="",flush=True)
  fpc += 1
  if fpc >= len(content[fpr]):
    print("\n",end="",flush=True)
    fpr += 1
    fpc = 0
  if fpr >= len(content):
    break
