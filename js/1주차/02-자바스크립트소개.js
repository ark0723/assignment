// 입력 - 처리 - 출력
/* 여러줄 주석 처리*/

/*
명령문은 한줄에 하나씩 쓰는 것이 좋다. 
다만, 명령문의 끝에 세미콜론을 붙이면 한줄에 두개 이상의 명령문을 쓸 수 있음
*/

// window(브라우저를 가리킴)야, method-alert()를 수행해라
window.alert("warning!")

//기록하기: window.console.log(자료형)
let num = 5
window.console.log(num)
console.log(num)
console.log(num)
//산술 연산
//반환: 명령문이 결과값처럼 사용되는 것을 뜻함
console.log(num%2)

// 자료형 확인하기
console.log(typeof num) 


let int;
int = 3;
console.log(int)

int += num
console.log(int)

/*
변수 선언
let 변수이름 = 데이터;

or 

let variable_name;
variable_name = data;

변수 만들기 룰: 
1. 변수명에는 오직 문자와 숫자, $, _ 만 포함될 수 있다.
2. 변수명의 첫글자는 숫자가 올 수 없다

상수 만드는 법
const 상수이름 = 데이터;
*/

const age = 37
alert(age)

/* 
window 객체의 prompt(x) 메소드는 사용자로부터 
문자열을 입력받을 수 있는 다이얼로그 박스를 열어주는 메소드
*/

let string;
string = window.prompt("당신이 좋아하는 과일은? ")
console.log(string)

let apple;
apple = "사과"

let banana;
banana="바나나"

alert(apple + " & " + banana)

/* 
템플릿 리터럴: 문자열을 표현하는 또 다른 방법으로, 백틱을 이용해 표현
const str3 = `백틱`

백틱 입력법(맥북)
영문상태에서는 ₩키를 누르면 됨
한글상태에서는 option + ₩키를 누르면 된다.

템플릿 리터럴은 반환값이 존재하는 코드로 표현식을 내장할 수 있는 문자열 표현법
문자열의 내용에 데이터를 삽입한다는 의미

예:
const data1 = "데이터"
const str1 = `문자열 중간에 ${data1} 삽입하기`
console.log(str1)
*/

let order;
order = window.prompt("붕어빵을 몇마리 주문하시겠습니까?")
let print;
print = `주문하신 붕어빵 ${order}마리를 준비하고 있습니다. 잠시만 기다려주세요.`
alert(print)

let name;
console.log(name) //undefined
name = null;
console.log(name)


/*
window.confirm(x)는 사용자에게 확인과 취소 둘 중 하나를 선택하게 하고, 
선택에 따라 true or false를 번환한다.
*/
confirmed = window.confirm("A가 사실입니까?")
console.log(confirmed)

/*
DOM: 브라우저는 HTML코드를 해석해서 요소들을 트리 형태로 구조화 표현하는 문서를 생성. 
이를 DOM 이라고 하며, DOM 을 통해 화면에 웹 콘텐츠들을 렌더링 함

DOM(Document Object Model): 웹 콘텐츠를 추가, 수정, 삭제하거나 
마우스클릭, 키보드 타이핑 등 이벤트에 대한 처리를 정의할 수 있도록 제공되는 프로그래밍 인터페이스다. 

window.document: 현재 브라우저에 렌더링 되고 있는 문서를 뜻하며, 
이를 이용해 js에서 문서 접근 가능

documment의 querySelector 메소드: 선택자("css선택자")를 인자로 입력받아 
선택자와 일치하는 문서 내 첫번째 요소(element)를 반환함. 일치하는 요소가 없을 경우 null반환

p 태그 선택
document.querySelector("p")

id가 text인 요소
document.querySelector("#text")

class가 text인 요소
document.querySelector(".text")

textContent속성: 해당 객체가 포함하고 있는 텍스트 콘텐츠를 표현하는 속성으로 
요소가 포함한 텍스트를 읽을 수도, 변경할 수도 있다. 

//p요소를 반환받아 상수로 이름을 붙인다.
const p_text = document.querySelector("p");

//p 요소의 textContent 속성을 콘솔에 출력
console.log(p_text.textContent)

// p 요소의 textContent 값을 변경
p_text.textContent = "텍스트를 이걸로 바꿔!"

*/