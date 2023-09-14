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

def lineTitle(index):
  linettl =['* 제  목 :', '* 만든이 :', '* 날  짜 :', '* 버  전 :', '* 깃허브 :' ]
  return linettl[index]

def printProgramInfoLine(text, singLineLength, textLength, index):
  print(lineTitle(index), end='')
  textSpace = (singLineLength - textLength) 
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
  signLineLength = max(titleLength, authorLength, dateLength, codeVersionLength, addressLength) + 20
  
  signLine('*', signLineLength+7);print()
  printProgramInfoLine(title, signLineLength -4, titleLength, 0)
  printProgramInfoLine(author, signLineLength-4, authorLength, 1)
  printProgramInfoLine(date, signLineLength-4, dateLength, 2)
  printProgramInfoLine(codeVersion, signLineLength-4, codeVersionLength, 3)
  printProgramInfoLine(address, signLineLength-4, addressLength, 4)
  signLine('*', signLineLength+7)
  print()
  
def main():
  title = input('program title : ')
  author = input('author : ')
  date = input('date : ')
  codeVersion = input('version : ')
  address = input('address : ')
  
  printProgramInfo(title, author, date, codeVersion, address)

if __name__ == '__main__':
  main()
