
import time
class TokenBucket:

    def __init__(self, maxsize, rate):
        self.maxsize = maxsize
        self.rate = rate
        self.currentsize = self.maxsize
        self.lastrefill = time.time()
    
    def __str__(self):
        return "{},{},{},{}".format(self.maxsize, self.rate, self.currentsize, self.lastrefill)

    def allow_request(self, tokens):
        self.refill()
        print('allow request, currentsize - {}, tokens requested - {}'.format(self.currentsize, tokens))
        if self.currentsize >= tokens:
            self.currentsize -= tokens   
            return True
        else:
            return False
    
    def refill(self):
        tokens_gained = int((time.time() - self.lastrefill) * self.rate)
        print('refill, tokens gained - {}'.format(tokens_gained))
        self.currentsize = min(self.currentsize + tokens_gained, self.maxsize)
        self.lastrefill = time.time()

if __name__ == '__main__':
    bucket = TokenBucket(10, 1)
    print(bucket)
    #print(time.asctime( time.localtime(time.time()) ))
    for i in range(3):
        print(bucket.allow_request(4))
        time.sleep(1)