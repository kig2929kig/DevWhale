from tqdm import tqdm
import time, random

#for i in tqdm(range(100)):
#    time.sleep(0.2)

class Download:
    def __init__(self, total, increment):
        self.progress = 0
        self.total = total
        self.increment = increment

    def __iter__(self):
        return self
    
    def __next__(self):
        self.progress += random.randint(0, self.increment)
        if self.progress >=  self.total:
            self.progress = self.total
            raise StopIteration
        return self.progress
    

def main():
    downloadSize = 4096
    bytsDownloaded = 0
    incrementMax = 100

    for i in tqdm(Download(downloadSize, incrementMax)):
        time.sleep(0.2)


if __name__ == '__main__':
    main()
