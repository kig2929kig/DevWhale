'''
*************************************
*     print Program informaion      *
*            Ingoo Kang             *
*            2023.09.13             *
*                1.0                *
*   https://github.com/kig2929kig   *
*************************************
'''
def signLine(sign, length):
  for i in range(length):
    print(sign, end='')
    
def printProgramInfoLine(text, singLineLength, textLength):
  print('*', end='')
  textSpace = (singLineLength - textLength) -2 # -2 -> front and back asterisk marks
  textLeftSpace = int(textSpace / 2)
  textRightSpace = textSpace - textLeftSpace
  signLine(' ', textLeftSpace)
  print(text, end='')
  signLine(' ', textRightSpace)
  print('*')
    
def printProgramInfo(title, author, date, codeVersion, address):
  titleLength = len(title)
  authorLength = len(author)
  dateLength = len(date)
  codeVersionLength = len(codeVersion)
  addressLength = len(address)
  signLineLength = max(titleLength, authorLength, dateLength, codeVersionLength, addressLength) + 8
  
  signLine('*', signLineLength);print()
  printProgramInfoLine(title, signLineLength, titleLength)
  printProgramInfoLine(author, signLineLength, authorLength)
  printProgramInfoLine(date, signLineLength, dateLength)
  printProgramInfoLine(codeVersion, signLineLength, codeVersionLength)
  printProgramInfoLine(address, signLineLength, addressLength)
  signLine('*', signLineLength)
  
def main():
  title = input('program title : ')
  author = input('author : ')
  date = input('date : ')
  codeVersion = input('version : ')
  address = input('address : ')
  
  printProgramInfo(title, author, date, codeVersion, address)

if __name__ == '__main__':
  main()
