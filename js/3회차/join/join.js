
const form = document.getElementById("form")
// 제출 이벤트 받는다 (이벤트 핸들링)
form.addEventListener("submit", function(event){
    event.preventDefault() //submit 후 새로고침 되는걸 방지하겠다

    let userID = event.target.id.value //폼에 있는 아이디 값을 받아오겠다
    let pw = event.target.pw.value
    let pw2 = event.target.pw2.value
    let name = event.target.name.value
    let phone = event.target.phone.value
    let position =event.target.position.value
    let gender = event.target.gender.value
    let email = event.target.email.value
    let intro = event.target.intro.value

    // console.log(userID, pw, pw2, name, phone, position, gender, email, intro)
    // ID 길이가 8자 이상이 되어야한다.
    if (userID.length < 8){
        alert("아이디는 8자 이상이어야합나다. 다시 입력해주세요.")
        return // 해당 문제가 발생한 경우, 함수를 강제 종료한다
    }

    // 비밀번호 pw1과 pw2 동일한지 확인
    if (pw !== pw2){
        alert("비밀번호가 일치하지 않습니다. 다시 입력해주세요.")
        return // 해당 문제가 발생한 경우, 함수를 강제 종료한다.
    }

    // 가입환영인사 출력: body에 있는 내용을 모두 지워주고, 환영글을 띄운다
    /*
    userID님 환영합니다. 
    회원가입시 입력하신 내용은 다음과 같습니다.
    아이디: userID
    이름: name
    전화번호: phone
    원하는 직부: position
    */
    document.body.innerHTML = ""
    document.write(`<p>${userID}님, 가입을 환영합니다!</p><br>`)
    document.write("회원가입시 입력하신 내용은 다음과 같습니다.<br>")
    document.write(`아이디: ${userID}<br>`)
    document.write(`이름:${name}<br>`)
    document.write(`전화번호:${phone}<br>`)
    document.write(`원하는 직무:${position}<br>`)


})

//제출된 입력값들을 참조한다

// 입력값에 문제가 있는 경우 이를 감지한다. 

//가입 환영 인사를 제공한다.