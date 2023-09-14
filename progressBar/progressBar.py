import random, time

BAR = chr(9608) # Character 9608 is █


def progressBar(progress, total, barWidth=40):
    progressBarStr = '['
    if progress > total :
        progress = total
    if progress < 0 :
        progress = 0
    
    numberOfBars = int((progress / total) * barWidth)
    progressBarStr += BAR * numberOfBars
    progressBarStr += ' ' * (barWidth - numberOfBars)
    progressBarStr += ']'

    percentComplete = round(progress / total * 100, 1)
    progressBarStr += ' ' + str(percentComplete) + '%'

    progressBarStr += ' ' + str(progress) + "/" + str(total)

    return progressBarStr

def main():
    import sys
    sys.path.append('C:\\git\\DevWhale\\')
    from printProgramInformation.printProgramInfo import printProgramInfo

    printProgramInfo('프로그레스 바 만들기', '강인구', '2023년 9월 14일', '1.0', 'https://github.com/kig2929kig')

    downloadSize = 4096
    bytesDownloaded = 0

    while bytesDownloaded < downloadSize :
        bytesDownloaded += random.randint(0, 100)
        barStr = progressBar(bytesDownloaded, downloadSize)
        print(barStr, end='', flush=True)

        time.sleep(0.2)
        print('\r', end='', flush=True)

if __name__ == '__main__':
    main()