            
# https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html                 

import os, sys
sys.path.append('C:\\Users\\잉구탱구\\Desktop\\ui programming\\header')
from header import printHeader

FIRST_CHAR_ORD = ord(' ')
LAST_CHAR_ORD = ord('~')
KEY_MAX = (LAST_CHAR_ORD - FIRST_CHAR_ORD) + 1

def readCiphertext(filename) :
    if not os.path.isfile('.//caesar_cipher//' + filename) :
        print('>>> [ERROR] 암호문 파일이 없습니다.')
    else :
        with  open('.//caesar_cipher//' + filename, 'r') as cfile:
            ciphertext = cfile.readline()
    return ciphertext

def brutalforceDecipher(ciphertext) :
    for i in range(KEY_MAX):
        print(i, ": ", end='')
        for c in ciphertext :
            c = ((ord(c) - FIRST_CHAR_ORD + i)  % KEY_MAX) + FIRST_CHAR_ORD
            print(chr(c), end='')
        print()

def makeFreqList(ciphertext) :
    alphaFreq = {}
    for i in range(KEY_MAX) :
        alphaFreq[chr(FIRST_CHAR_ORD + i)] = 0

    for c in ciphertext :
        alphaFreq[c] += 1
    
    #for i in alphaFreq.items() :
    #    print(i)
    
    freqList = sorted(alphaFreq.items(), key=lambda x:x[1], reverse=True)
    #print(freqList)
    return freqList

def frequencyDecipher(ciphertext):
    freqChars = [' ', 'e', 'a', 'r', 'i', 'o', 't', 'n', 's', 'l']

    freqList = makeFreqList(ciphertext)
    freqCh = freqList[0][0] #가장 빈도수가 높은 문자

    for i, ch in enumerate(freqChars):
        diff = ord(ch) - ord(freqCh)
        print(str(i+1)+': ', end='')
        for c in ciphertext:
            print(chr((ord(c)+diff-FIRST_CHAR_ORD)%KEY_MAX + FIRST_CHAR_ORD), end='')
        print()

def main() :
    # 헤더
    printHeader('Decryption of Caesar cipher', '2023-09-13', 'made by kig2929kig')

    cipherFile = input('암호문 파일명을 입력하세요: ')
    ciphertext = readCiphertext(cipherFile)

    print('\n<Brutal Force 기법의 해독 결과>')
    brutalforceDecipher(ciphertext)
    
    print('\n<알파벳 빈도수에 의한 해독 결과>')
    frequencyDecipher(ciphertext)

if __name__ == '__main__' :
    main()