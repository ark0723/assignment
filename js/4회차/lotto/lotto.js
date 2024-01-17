const todaySpan = document.querySelector("#today")
const numbersDiv = document.querySelector(".numbers")
const drawBtn = document.querySelector("#draw")
// const resetBtn = document.querySelector("#reset")

const today = new Date()
let year = today.getFullYear()
let month = today.getMonth() + 1 // 0부터 11까지 반환 -> 1 더해줘야
let date = today.getDate()
todaySpan.textContent = `${year}년 ${month}월 ${date}일 `



function paintNum(n){
    const eachNumDiv = document.createElement("div")
    eachNumDiv.classList.add = "eachnum"
    eachNumDiv.textContent = n
    numbersDiv.append(eachNumDiv)
}

// click: create five random numbers between 1 and 45, 중복 허용 안함
drawBtn.addEventListener("click", function(){
    //initialize
    let lottoNumbers = []
    numbersDiv.innerHTML = ""
    //set parameters
    max_num = 45
    min_num = 1

    while (lottoNumbers.length < 6){
        let num = Math.floor(Math.random() * max_num) + min_num
        // lottoNumbers array에 생성된 random number가 없으면(-1)
        if (lottoNumbers.indexOf(num) === -1){
            lottoNumbers.push(num)
            paintNum(num)
        }
    }
})

/*
resetBtn.addEventListener("click", function(){
    lottoNumbers = [] // lottoNumbers.splice(0,6)
    numbersDiv.innerHTML = ""
})
*/