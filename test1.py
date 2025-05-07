def find_vowels(s):
    cnt = 0
    s1 = s.lower()
    vowels = ['a', 'e', 'u', 'i', 'o']
    for i in s1:
        if i in vowels:
            cnt += 1
    return cnt

'''
문제 2: 리스트 합계 및 평균 구하기

설명: 숫자로 이루어진 리스트를 입력으로 받아, 리스트 요소들의 합계와 평균을 튜플 형태로 반환하는 함수 calculate_sum_average(numbers)를 작성하세요. 
리스트가 비어있으면 (0, 0)을 반환해야 합니다. 평균은 소수점까지 표현될 수 있습니다.
입력 예시: [1, 2, 3, 4, 5]
출력 예시: (15, 3.0)
입력 예시 2: []
출력 예시 2: (0, 0)
힌트: sum(), len(), 빈 리스트 처리'''
def calculate_sum_average(numbers):
    if numbers == []:
        return (0,0)
    else:
        return (sum(numbers), sum(numbers)/len(numbers))
    
'''
문제 3: 딕셔너리에서 특정 값 찾기

설명: 학생 이름과 점수를 담고 있는 딕셔너리가 주어집니다. 
특정 점수 이상을 받은 학생들의 이름만 리스트로 반환하는 함수 get_high_achievers(scores_dict, threshold)를 작성하세요.
입력 예시:
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
threshold = 90
출력 예시: ['Bob', 'David'] (순서는 상관 없음)
힌트: 딕셔너리 반복 (items()), 조건문
'''
def get_high_achievers(scores_dict, threshold):
    name_list = []
    for name, score in scores_dict.items():
        if score >= threshold:
            name_list.append(name)
    return name_list

'''
문제 4: 회문(Palindrome) 판별기
    
설명: 문자열을 입력으로 받아, 해당 문자열이 회문인지 아닌지를 판별하여 True 또는 False를 반환하는 함수 is_palindrome(s)를 작성하세요. 
회문은 앞으로 읽으나 뒤로 읽으나 동일한 문자열을 의미합니다. 비교 시 대소문자는 무시하고, 알파벳과 숫자 외의 문자(공백, 특수문자 등)는 제거하고 판별합니다.
입력 예시: "A man, a plan, a canal: Panama"
출력 예시: True
입력 예시 2: "race a car"
출력 예시 2: False
힌트: 문자열 전처리 (lower(), isalnum()), 문자열 슬라이싱 ([::-1]) 또는 양쪽 끝에서부터 비교
'''
import re
def s_palindrome(s):
    s1 = s.lower()
    s1 = re.sub(r'[^a-z0-9]', '', s1)
    print(s1)
    for temp in range(len(s1)//2):
        if s1[temp] != s1[-temp-1]:
            return False
    return True

'''
문제 5: 숫자 뒤집기

설명: 양의 정수를 입력으로 받아, 그 숫자를 뒤집은 정수를 반환하는 함수 reverse_integer(n)를 작성하세요. 예를 들어 123을 입력받으면 321을 반환합니다.
입력 예시: 12345
출력 예시: 54321
입력 예시 2: 100
출력 예시 2: 1 (001 이므로 1)
힌트: 문자열로 변환 후 처리하거나, 나머지 연산자(%)와 정수 나눗셈(//) 활용'''

def reverse_integer(n):
    numbers = list(str(n))
    numbers.reverse()
    return int(''.join(numbers))

'''alphabet, number = input().split(' ')
number = int(number)
alphabet_number = ord(alphabet) - ord('a')
sum = (alphabet_number+number)%26
print(chr(ord('a')+(sum)))'''

'''initial_name = input()
number = int(input())
print(number*('a')+initial_name)
'''

'''initial_name = input()
N = int(input())
i = list(map(int, input().split(' ')))
print(initial_name, end=' ')
for temp in range(N):
    print('a'*i[temp], end='')
    if temp == N-1:
        break
    else:
        print(' ', end='')'''


'''문제 1: 문자열 내 문자 빈도수 계산하기

설명: 문자열을 입력받아, 해당 문자열에 포함된 각 문자들의 빈도수(등장 횟수)를 계산하여 딕셔너리 형태로 반환하는 함수 char_frequency(s)를 작성하세요. 
대소문자를 구분해야 합니다.
입력 예시: "Hello World"
출력 예시: {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1} (딕셔너리 내 요소들의 순서는 중요하지 않습니다.)
힌트: 딕셔너리를 사용하여 각 문자의 등장 횟수를 저장합니다.'''

def char_frequency(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

'''문제 2: 누락된 숫자 찾기

설명: 1부터 n까지의 정수 중 하나만 빠지고 나머지는 모두 포함하며, 중복되지 않는 숫자들로 이루어진 리스트 nums가 주어집니다. 
(리스트의 길이는 n-1이 됩니다.) 이 리스트에서 빠진 숫자를 찾아 반환하는 함수 find_missing_number(nums, n)을 작성하세요. 
n은 원래 1부터 n까지 숫자가 있었음을 나타내는 값입니다.
입력 예시: nums = [1, 2, 4, 6, 3, 7, 8], n = 8
출력 예시: 5
힌트: 예상되는 총합과 실제 리스트의 총합의 차이를 이용하거나, 집합(set) 자료구조를 활용할 수 있습니다.'''
def find_missing_number(nums, n):
    nums = set(nums)
    for i in range(1,n+1):
        if i not in nums:
            return i
print(find_missing_number([1, 2, 4, 6, 3, 7, 5], 8))

'''
문제 3: 중첩 리스트의 모든 숫자 합계 구하기

설명: 정수 또는 다른 리스트(이 리스트 또한 정수나 다른 리스트를 포함할 수 있음)를 요소로 가질 수 있는 중첩된 리스트 nested_list가 주어집니다. 
이 중첩된 구조 안에 있는 모든 정수들의 합을 반환하는 함수 sum_nested_list(data)를 작성하세요.
입력 예시: [1, 2, [3, 4, [5]], 6, [7, 8]]
출력 예시: 36 (1+2+3+4+5+6+7+8)
힌트: 재귀 함수(Recursion)를 사용하면 효과적으로 해결할 수 있습니다. isinstance() 함수로 요소의 타입을 확인할 수 있습니다.'''

def sum_nested_list(data):
    sum = 0
    for i in data:
        if isinstance(i, list):
            sum += sum_nested_list(i)
        else: sum += i
    return sum

'''
문제 4: 두 수의 합 (Two Sum) - 목표값 찾기

설명: 정수 리스트 nums와 정수 target이 주어집니다. 
리스트 nums 안에서 두 개의 서로 다른 숫자를 뽑아 그 합이 target이 되는 두 숫자를 찾아 튜플이나 리스트 형태로 반환하는 함수
find_two_sum(nums, target)을 작성하세요. 만약 해당하는 쌍이 여러 개 있다면 아무거나 하나만 반환하고, 없다면 None을 반환합니다.
입력 예시: nums = [2, 7, 11, 15], target = 9
출력 예시: (2, 7) 또는 [2, 7] (순서는 상관 없음)
입력 예시 2: nums = [3, 2, 4], target = 6
출력 예시 2: (2, 4) 또는 [2, 4]
입력 예시 3: nums = [3, 3], target = 6
출력 예시 3: (3, 3) 또는 [3, 3]
힌트: 이중 반복문 또는 딕셔너리(해시맵)를 활용한 방법을 생각해 볼 수 있습니다.
'''
def find_two_sum(nums, target):
    check = {}
    for current in nums:
        if (target - current) in check:
            return (target-current, current)
        else:
            check[current] = True
    return None

print(find_two_sum([3, 2, 4], 6))