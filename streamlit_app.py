import streamlit as st

name = ""

st.title("객체지향 프로그래밍 알아보기!")
st.markdown(":technologist:  \n제작자: [C_code 동아리] 31112 유민아")
st.subheader(':question:객체지향 프로그래밍이란')
st.markdown('객체지향 프로그래밍은 프로그래밍에서 필요한 데이터를 상태와 행위를 가진 :red[객체]로 만들고 객체들간의 상호작용을 중심으로 하는 프로그래밍 방법을 말해요.  \n여기서 우리는 객체지향 프로그래밍의 네 가지 특징을 살펴보려고 합니다. 이해하기 쉽게 성화여고를 주제로 설명해보려고 해요:sweet_potato:')


st.markdown('먼저, 성화여자고등학교 학생들을 설명하는 속성으로는 어떤 것이 있을까요?')
text = """

- 학년
- 반
- 번호
- 이름

"""
st.write(text)

st.markdown('이 속성을 가지고 성화여자고등학교를 다니는 여러분의 캐릭터를 만들려고 해요.  \n 학년, 반, 번호, 이름을 적어주세요.  \n:point_up:번호와 이름을 입력한 후에 꼭 enter키를 눌러주세요.')

col1, col2, col3, col4 = st.columns(4)

with col1:
  grade = st.selectbox("학년", ("1", "2", "3"))

with col2:
  classroom = st.selectbox("반", ("1", "2", "3","4", "5", "6","7", "8", "9","10", "11"))

with col3:
  number = st.text_input('번호', '1')

with col4:
  name = st.text_input('이름(영어로 입력)', "Mina")













st.header('1. 캡슐화 Encapsulation  \n')
st.subheader('예제로 몸풀기')

st.markdown('객체지향 프로그래밍에서는 이 속성들을 모아서 성화여자고등학교 학생을 설명하는 일종의 틀을 만들 수 있어요!  \n이 틀을 :red[클래스]라고 합니다.  \n 그럼 파이썬으로 성화여자고등학교 학생 클래스를 한번 만들어볼까요?  \n  \n 우선, "shstudent"라는 이름의 클래스를 만들어줍니다.')
code = '''
class shstudent:
    
    '''
st.code(code, language='python')
st.divider()
st.markdown('성화여자고등학교 학생의 특징을 나타내는 속성을 부여해줘요! __init__ 메서드를 활용할 수 있어요.  \n')
code = '''
class shstudent:
  def __init__(self, grade, classroom, number, name):
    self.grade = grade
    self.classroom = classroom
    self.number = number
    self.name = name
    
    '''
st.code(code, language='python')


st.divider()


st.markdown('  \n성화여자고등학교 학생이 자기소개를 하는 함수도 클래스에 추가해보아요.  \n')
code = '''
class shstudent:
  def __init__(self, grade, classroom, number, name):
    self.grade = grade
    self.classroom = classroom
    self.number = number
    self.name = name
  def introduce(self):
    print('안녕하세요. 저는 성화여자고등학교',self.grade,'학년'
    ,self.classroom,'반',self.number,'번',self.name,'라고 합니다.')
    '''
st.code(code, language='python')


st.divider()


st.markdown('그럼 이제 성화여자고등학교 소속의 학생을 만들어넣어볼까요? 여러분의 이름을 가진 캐릭터를 성화여자고등학교 소속으로 만들어서 자기소개를 시켜볼게요:wink:')
code = f'''
class shstudent:
  def __init__(self, grade, classroom, number, name):
    self.grade = grade
    self.classroom = classroom
    self.number = number
    self.name = name
  def introduce(self):
    print('안녕하세요. 저는 성화여자고등학교',self.grade,'학년'
    ,self.classroom,'반',self.number,'번',self.name,'입니다.')

{name} = shstudent({grade}, {classroom}, {number}, "{name}")
{name}.introduce()
    '''
st.code(code, language='python')

if st.button(":large_green_circle:실행하기", key = 1):
  st.success(f"안녕하세요. 저는 성화여자고등학교 {grade}학년 {classroom}반 {number}번 {name}입니다.")




st.divider()

st.subheader(":smiley:아하! 캡슐화란 이런 것이군요")
st.markdown("실행해보셨나요? 지금까지  \n:one:성화여고 학생이라는 shstudent 클래스를 만들어서,  \n:two: shstudent의 :green[속성](학년, 반, 번호, 이름)을 부여해주고   \n:three: shstudent가 자기소개를 하는 :green[메서드]를 지정해주었어요.  \n:four:그리고 shstudent 클래스의 속성과 메서드를 가져와서 성화여고 소속인 여러분의 캐릭터를 만들었습니다.  \n  \n이렇게 데이터와 해당 데이터를 처리하는 메서드를 하나로 묶어 캡슐 형태로 만드는 것을 :red[캡슐화]라고 합니다. 객체지향 프로그래밍의 네 가지 특징 중 하나예요. 여기서 이 shstudent라는 클래스는 학생이라는 :red[객체]를 만드는 설계도이다~~! 라고 생각하면 돼요:smile:")

st.divider()






st.header('2. 상속 Inheritance  \n')
st.subheader('예제로 몸풀기  \n')

st.subheader(':shrug:')
st.markdown('"그런데... 성화여고 학생은 어쨌든 고등학생이잖아요? 학년 반 번호 이름이 어떻게 성화여고 학생만의 특징이죠?"  \n 그렇습니다. 학년 반 번호 이름은 고등학생이라면 모두에게 주어지는 속성이죠? 성화여고 학생은 고등학생의 하위 개념이라는겁니다.  \n그럼 고등학생이라는 클래스를 빨리 만들어볼게요.')
code = '''
class student:
  def __init__(self, grade, classroom, number, name):
    self.grade = grade
    self.classroom = classroom
    self.number = number
    self.name = name
  
    '''
st.code(code, language='python')
st.divider()

st.markdown('이제 성화여고 학생은 고등학생 클래스의 속성을 :green[물려받으면] 됩니다. student 클래스를 만들어준 뒤, shstudent 클래스를 만들어 student 클래스의 속성을 모두 물려받아줍니다.')

code = '''
class student:
  def __init__(self, grade, classroom, number, name):
    self.grade = grade
    self.classroom = classroom
    self.number = number
    self.name = name

#class 새로운클래스(속성을 물려받을 클래스)
class shstudent(student):
  pass
  
    '''
st.code(code, language='python')
st.divider()

st.subheader(":smirk:상속, 감 잡았어요")
st.markdown('상속이란 앞선 예시처럼 기존 클래스(부모클래스)의 특성을 그대로 물려받아 새로운 클래스(자식 클래스)를 생성하는 것을 의미합니다. 상속이라는 객체지향의 특징 덕분에 반복적인 코드를 계속해서 쓸 필요가 없어요. 또, 클래스 간에 계층적인 구조를 형성하기 때문에 객체지향 프로그래밍에서 가장 중요한 객체의 관계를 명확하게 표현할 수 있게 됩니다!')

st.divider()
st.header('3. 추상화 abstract  \n')
st.subheader('예제로 몸풀기  \n')
st.markdown('아까 상속에서 살펴본  \n"성화여고 학생은 학생이다"  \n이 과정을 더 해볼까요?')
text= '''

- 성화여고 학생은 학생
- 학생은 사람
- 사람은 영장류
- 영장류는 생물
.
.
.

'''
st.write(text)

st.markdown('추상화가 무엇인지 눈치 채셨나요?  \n성화여고 학생에서 출발해서 추상화 라는 것을 통해 생물로까지 확장시켰습니다. 그리고 성화여고 학생은 학생, 사람, 영장류, 생물에 속하기 때문에 그 특징을 모두 잘 갖추고 있죠.')

code = '''
#추상 클래스
from abc import ABC, abstractmethod

#생물 클래스는 추상 클래스에 넣어줍니다
class 생물(ABC):
    @abstractmethod
    def 살아있기(self):
        pass

#영장류 클래스는 생물 클래스에 속하고,
class 영장류(생물):
    @abstractmethod
    def 다섯_갈래의_손과_발로_물건_집기(self):
        pass

#사람 클래스는 영장류 클래스에 속하고,
class 사람(영장류):
    @abstractmethod
    def __init__(self, name):
      self.name = name
    
    def 직립보행(self):
        pass

#학생 클래스는 사람 클래스에 속하고,
class 학생(사람):
    @abstractmethod
    def __init__(self, name, grade, classroom, number):
      #사람의 이름을 상속받고 학년 반 번호 추가
      super().__init__(name)
      self.grade = grade
      self.classroom = classroom
      self.number = number
    
    def 공부하기(self):
        pass

#성화여고생 클래스는 학생 클래스에 속합니다.
class 성화여고생(학생):
    @abstractmethod
    def __init__(self, name, grade, classroom, number, uniform):
      #학년 반 번호를 상속받고 교복 색 추가
      super().__init__(name, grade, classroom, number)
      self.uniform_color = "고구마색"

  
    '''
st.code(code, language='python')


st.subheader(":raising_hand:추상화 이해했다!")
st.markdown('추상화란 이렇게 개체의 핵심적인 특성을 간추려서 복잡성을 감소시키는 것을 뜻합니다. 추상화를 사용하면 사용자는 복잡한 내부 구조를 알 필요없이 개체를 이해하고 사용할 수 있어요.')









st.divider()
st.header('4. 다형성 Polymorphism  \n')
st.subheader('예제로 몸풀기  \n')
st.markdown('마지막 다형성입니다!  \n사람 중에서도 학생은 공부를 열심히 해야합니다(...) 개발자는 개발을 열심히 해야겠죠? 학생이 공부를 열심히 하는 것과, 개발자가 개발을 열심히 하는 것은 모두 자신의 역할에 최선을 다해 일을 하는 것입니다. 사람은 누구나 자신의 본분을 지켜 해야할 일을 하며 살아갑니다. 이것을 파이썬의 클래스와 함수를 이용해 나타내볼까요?  \n사람 클래스를 만들고 열심히 일을 하는 메서드를 넣어줍니다.')

code = '''
class 사람:
    def __init__(self, name):
        self.name = name

    def work(self):
        print (self.name + "일을 열심히 한다.")        

class 학생(사람):
    def work(self):
        print (self.name + " 공부를 열심히 한다.")

class 개발자(사람):
    def work(self):
        print (self.name + " 개발을 열심히 한다.")        
    '''
st.code(code, language='python')

st.divider()
st.markdown('학생과 개발자는 모두 사람입니다. 사람 클래스에 속하는 학생 클래스와 개발자 클래스를 만들어줍니다.  \n사람 클래스에서 선언했던 work 함수가 있죠? 학생 클래스에서 work함수는 공부를 열심히 하는 것, 개발자 클래스에서 work함수는 개발을 열심히 하는 것이므로 각각의 클래스 안에서 work함수가 어떤 것을 의미하는지 재정의해주면 돼요!')
code = '''
class 사람:
    def __init__(self, name):
        self.name = name

    def work(self):
        print (self.name + "일을 열심히 한다.")        

class 학생(사람):
    def work(self):
        print (self.name + " 공부를 열심히 한다.")

class 개발자(사람):
    def work(self):
        print (self.name + " 개발을 열심히 한다.")


    '''
st.code(code, language='python')

st.divider()
st.markdown('클래스만 만들면 뭐가 와닿나요? 바로 클래스에 속하는 객체를 생성해줄게요!')


code = f'''
class 사람:
    def __init__(self, name):
        self.name = name

    def work(self):
        print (self.name + "일을 열심히 한다.")        

class 학생(사람):
    def work(self):
        print (self.name + " 공부를 열심히 한다.")

class 개발자(사람):
    def work(self):
        print (self.name + " 개발을 열심히 한다.")

student1 = 학생("{name}")
developer1 = 개발자("Mina")
student1.work()
developer1.work()
    '''
st.code(code, language='python')



message = f"{name} 공부를 열심히 한다. Mina 개발을 열심히 한다."
if st.button(":large_green_circle: 실행하기", key=2):
    st.success(message)

st.subheader(":sunglasses:다형성, 이해했어요")
st.markdown('다형성은 이렇듯 한 가지 인터페이스로 다양한 타입의 객체를 다룰 수 있는 능력을 의미합니다. work라는 동일한 메서드를 호출하더라도 학생과 개발자라는 객체에 따라 다르게 동작하도록 하는 것이에요.  \n방금 한 것처럼 부모 클래스로부터 상속받은 메서드의 내용을 재정의하는 과정을 :red[오버라이딩]이라고 해요!')
st.divider()

st.subheader(":yum:야호! 객체지향 프로그래밍의 네 가지 특징을 모두 살펴보았어요")
text = """

- 캡슐화
- 상속성
- 추상화
- 다형성

"""
st.write(text)

st.markdown("객체지향 프로그래밍의 특징을 잘 기억하고 익혀두세요! 객체지향 프로그래밍은 개발자로 취업할 시 입사 면접에서 많이 물어보는 질문이라고도 합니다.	:writing_hand:그럼 글을 마무리할게요!")
