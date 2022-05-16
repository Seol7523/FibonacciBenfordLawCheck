"""
n 진법에서의 피보나치수열의 벤포드의 법칙(Benford's law) 성립여부 확인 프로그램

made by Seolmango
"""
import matplotlib.pyplot as plt
import numpy as np
import os

# tools
def int_to_n(n : int, x : int) -> list:
    """
    10진법으로 입력된 수 n을 x진법으로 변환하여 리스트로 반환하는 함수
    
    :param n: 10진법으로 입력된 수
    :param x: 몇진법인지 입력
    :return: x진법으로 변환된 수를 리스트로 반환
    """
    result = []
    while n > 0:
        result.append(n % x)
        n //= x
    return result[::-1]

# Main class 정의
class tester_main():
    """
    n 진법에서의 피보나치수열의 벤포드의 법칙(Benford's law) 성힙여부 테스트하는 클래스
    """
    
    def __init__(self, x : int, test_limit : int = 1000):
        """
        초기화 함수
        
        :param x: 몇진법인지 입력
        """
        self.base = x
        self.dataset = {}
        for i in range(1,x):
            self.dataset[i] = 0
        self.limit = test_limit
        self.run_count = 0
        self.run_cache = []
        self.last_error = 0
        self.now = os.getcwd()
        return None
    
    def run(self):
        """
        테스트를 실행하는 함수
        """
        test = self.next_num()
        while(test != -1):
            self.dataset[int_to_n(test, self.base)[0]] += 1
            test = self.next_num()
        return 0
        
        
    
    def next_num(self) -> int:
      """
      다음 피보나치 수열의 값을 반환하는 함수
      self.run_count와 self.run_cache를 이용합니다
      
      :return: 다음 피보나치 수열의 값(-1 인 경우 limit도달)
      """
      if(self.run_count <= self.limit):
          if(self.run_count == 0):
              self.run_cache.append(1)
              self.run_count += 1
              return 1
          elif(self.run_count == 1):
              self.run_cache.append(1)
              self.run_count += 1
              return 1
          else:
              self.run_count += 1
              function_cache = self.run_cache[0] + self.run_cache[1]
              self.run_cache[0] = self.run_cache[1]
              self.run_cache[1] = function_cache
              return function_cache
      else:
          return -1
        
    def make_result(self) -> int:
        """
        테스트 결과를 그래프로 저장하는 함수
        """
        total = 0
        for i in self.dataset.values():
            total += i
        result_data_x = []
        result_data_y = []
        for i in self.dataset.keys():
            if(i % (round(self.base/10)) == 0):
                result_data_x.append(i)
            else:
                result_data_x.append('')
            result_data_y.append((self.dataset[i]/total)*100)
        x = np.arange(self.base-1)
        plt.clf()
        
        plt.bar(x, result_data_y, align='center')
        plt.xticks(x, result_data_x)
        
        plt.suptitle('Benford\'s law test result',size='xx-large')
        plt.title(f'base : {self.base} test_limit : {self.limit}')
        
        plt.savefig(f'{self.now}\\results\\result(Base{self.base}_{self.limit}).png')
        return 0


if(__name__ == "__main__"):
    for i in range(1,21):
        print("start test : ", i)
        test = tester_main(i*10,10000)
        test.run()
        test.make_result()
    print("end")
        
        