document.getElementById("join").addEventListener("submit", function(event){

  event.preventDefault()
  console.log('submit')

  const name = document.getElementById('name').value;
  const ID = document.getElementById('ID').value;
  const pw = document.getElementById('pw').value;
  const email = document.getElementById('email_address').value;
  const phone = document.getElementById('phone').value;
  const excer = document.getElementById('excercise').value;
  const travel = document.getElementById('travel').value;
  const cook = document.getElementById('cooking').value;
  const read = document.getElementById('reading').value;
  const netflx = document.getElementById('netflix').value;
  const gender = document.querySelector('input[name = "gender"]:checked').value;


  console.log(`이름: ${name}`)
  console.log(`ID: ${ID}`)
  console.log(`PW: ${pw}`)
  console.log(`E-mail: ${email}`)
  console.log(`Phone: ${phone}`)
  console.log(`운동: ${excer}`)
  console.log(`여행: ${travel}`)
  console.log(`요리: ${cook}`)
  console.log(`독서: ${read}`)
  console.log(`넷플릭스: ${netflix}`)
  console.log(`성별: ${gender}`)

  alert("회원가입 되셨습니다.")

  document.getElementById('join').reset()
})
