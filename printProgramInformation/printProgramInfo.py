import unicodedata

def signLine(sign, length):
  for i in range(length):
    print(sign, end='')

def txtLength(text) :
  textLength = 0
  for txt in text:
    if unicodedata.east_asian_width(txt) == 'W':
      textLength = textLength + 2 # txt 한글이면 길이를 +2
    else :
      textLength = textLength + 1 # txt 한글이 아니면 길이를 +1
  return textLength


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
  titleLength = txtLength(title)
  authorLength = txtLength(author)
  dateLength = txtLength(date)
  codeVersionLength = txtLength(codeVersion)
  addressLength = txtLength(address)
  signLineLength = max(titleLength, authorLength, dateLength, codeVersionLength, addressLength) + 10
  
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
