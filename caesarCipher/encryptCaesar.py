import sys
sys.path.append('C:\\git\\DevWhale\\')
from printProgramInformation.printProgramInfo import printProgramInfo

printProgramInfo('카이사르 암호 만들기', '강인구', '2023년 9월 14일', '1.0', 'https://github.com/kig2929kig')

def caesarCipher(plaintext, key):
    first = ord(' ')
    last = ord('~')
    ciphertext =''

    for c in plaintext:
        c = (ord(c) - first + key) % (last - first + 1)
        c = c + first
        ciphertext += chr(c)

    return ciphertext

def main():
    plaintext = input('암호화할 문장을 입력하세요: ')
    cipherKey = int(input('키 값(정수)을 입력하세요: '))
    cipherFile = input('암호문을 저장할 파일명을 입력하세요: ')
    ciphertext = caesarCipher(plaintext, cipherKey)
    print('암호문: ', ciphertext)

    with open('.\\caesarCipher\\' + cipherFile, 'w') as cfile:
       cfile.write(ciphertext)

if __name__ == '__main__' :
    main()
