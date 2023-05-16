# %%
import math
"""
help() 함수를 위한 docstring 문서작성은
작은따옴표 혹은 큰따옴표 3개를 묶어 작성한다.
따옴표3개 사이는 여러줄 주석이 가능하다.
모듈에 대한 설명은 소스코드 최상단에 기재한다.
"""
class line:
    """
    class에 대한 설명은 class의 선언부 바로 아래에 작성한다.
    """
    def __init__(self, length=0):
        """
        함수(메소드)의 설명은 함수의 선언(def) 바로 아래에 작성한다.
        """
        self.__length = length
    def set_length(self, length):
        """0으로 초기화된 __length를 인수 length로 바꿔준다
        Args:
            length: 새로운 값
        Returns:
            아무 값도 리턴하지 않음 (혹은 공란으로 비워둠)
        Examples:
            >>> set_length(10) # __length를 10으로 바꾼다
        """
        self.__length = length
    def get_length(self):
        """저장하고 있는 __length를 return한다
        Returns:
            self.__length
        Examples:
            >>> new_length = get_length() # new_length 변수를 self.__length값으로 바꾼다
        """
        return self.__length
    
def area_square(length):
    """한변의 길이가 length인 정사각형의 넓이를 구한다
        Args:
            length: 정사각형 한변의 길이
        Returns:
            length**2 # 정사각형의 넓이
        Examples:
            >>> square = area_square(5) # square변수를 한변의 길이가 5인 정사각형의 넓이로 바꾼다
    """
    return length**2

def area_circle(length):
    """반지름의 길이가 length인 원의 넓이를 구한다
        Args:
            length: 반지름 길이
        Returns:
            length**2 * math.pi # 원의 넓이
        Examples:
            >>> circle = area_circle(3) # circle변수를 반지름의 길이가 3인 원의 넓이로 바꾼다
    """
    return length**2 * math.pi

def area_regular_triangle(length):
    """한변의 길이가 length인 정삼각형의 넓이를 구한다
        Args:
            length: 정삼각형 한변의 길이
        Returns:
            (math.sqrt(3)/4) * (length**2)  # 정삼각형의 넓이
        Examples:
            >>> triangle = area_regular_triangle(4) # triangle변수를 한변의 길이가 4인 삼각형의 넓이로 바꾼다
    """
    return (math.sqrt(3)/4) * (length**2)  