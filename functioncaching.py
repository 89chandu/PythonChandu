import  time
from  functools import lru_cache

    @lru_cache(maxsize=3)
        def some_work(n):
          time.sleep(n)
          return n

      if __name__=='_main_':
            print("now running some work")
            some_work(3)
            print("done............calling again")
            some_work(3)
            print("called again")