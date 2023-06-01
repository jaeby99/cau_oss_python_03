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
    __width = 0
    __height = 0
    def __init__(self, width, height):
        """
        함수(메소드)의 설명은 함수의 선언(def) 바로 아래에 작성한다.
        """
        self.__width = width
        self.__height = height
    def set_length(self, width, height):
        """0으로 초기화된 __length를 인수 length로 바꿔준다
        Args:
            length: 새로운 값
        Returns:
            아무 값도 리턴하지 않음 (혹은 공란으로 비워둠)
        Examples:
            >>> set_length(10) # __length를 10으로 바꾼다
        """
        self.__width = width
        self.__height = height
    def get_length(self):
        """저장하고 있는 __length를 return한다
        Returns:
            self.__length
        Examples:
            >>> new_length = get_length() # new_length 변수를 self.__length값으로 바꾼다
        """
        return self.__width, self.__height
    
def area_rectangle(width, height):
    """너비와 높이의 길이가 widht, height인 직사각형의 넓이를 구한다
        Args:
            width: 직사각형 너비의 길이
            height: 직사각형 높이의 길이
        Returns:
            length*width # 직사각형의 넓이
        Examples:
            >>> square = area_square(5, 4) # square변수를 너비가 5이고, 높이가 4인 직사각형의 넓이로 바꾼다
    """
    if width <= 0 or height <= 0: raise ValueError
    return width*height

def area_ellipse(width, height):
    """너비와 높이의 길이가 width, height인 타원의 넓이를 구한다
        Args:
            width: 타원의 너비
            height: 타원의 높이
        Returns:
            width*height*math.pi # 타원의 넓이
        Examples:
            >>> circle = area_ellipse(3,2) # circle변수를 너비가 3이고 높이가 2인 타원의 넓이로 바꾼다
    """
    if width <= 0 or height <= 0: raise ValueError
    return width*height*math.pi

def area_right_triangle(width, height):
    """너비와 높이가 width, height인 직각삼각형의 넓이를 구한다
        Args:
            width: 직각삼각형 너비의 길이
            height: 직각삼각형 높이의 길이
        Returns:
            width*height/2  # 직각삼각형의 넓이
        Examples:
            >>> triangle = area_regular_triangle(4,3) # triangle변수를 너비가 4, 높이가 3인 직각삼각형의 넓이로 바꾼다
    """
    if width <= 0 or height <= 0: raise ValueError
    return width*height/2