const apiRandomDogs = "https://dog.ceo/api/breeds/image/random/42"
const apiAllBreeds = "https://dog.ceo/api/breeds/list/all"
const request1 = new XMLHttpRequest()
const request2 = new XMLHttpRequest()

const header = document.getElementById("header")
const main = document.getElementById("main")
const imgs = document.getElementById("images")
const input = document.getElementById("filter-text")
const button = document.getElementById("filter-button")
const select = document.getElementById("filter-select")
const more = document.getElementById("more")
const tothetop = document.getElementById("tothetop")
const reset = document.getElementById("reset")
// 현재 화면에 나타나고 있는 개 사진array
let currentDogs = []


function displayDogs(item){
    const dogImgDiv = document.createElement("div")
    dogImgDiv.classList.add("flex-item")
    dogImgDiv.innerHTML = `<img src = ${item}>`
    imgs.appendChild(dogImgDiv)
}

//웹브라우저가 로드 됐을때 화면 구성
window.addEventListener("load", function(){
    //강아지 사진 뿌리기
    request1.open("get", apiRandomDogs)
    //응답이 로드 되었을때(성공시)
    request1.addEventListener("load", function(){
        //응답을 읽어온다
        const response = JSON.parse(request1.response)
        response.message.forEach(function(item){
            currentDogs.push(item)
            displayDogs(item)
        })

    })
    request1.send()

    //select에 모든 견종정보 담기
    request2.open("get", apiAllBreeds)
    request2.addEventListener("load", function(){
        const response = JSON.parse(request2.response)
        // console.log(response) - message: {breed: ["sub-breed"]}
        breedList = Object.keys(response.message) // key 값들만 반환
        breedList.forEach(function(item){
            const option = document.createElement("option")
            option.textContent = item
            option.value = item
            select.appendChild(option)
        })

    })
    request2.send()
})

// 필터링 버튼 누르면, 쓰여진 내용에 맞춰 필터링 된다
button.addEventListener("click", function(){
    imgs.innerHTML = "" 
    let filteredDog = currentDogs.filter(function(item){
        return (item.indexOf(input.value) !== -1)
    })

    input.value = "" //한번 클릭하고 나면, 쓰여진 내용 빈칸으로 복구

    //필터된 강아지 사진 뿌리기
    filteredDog.forEach(function(item){
        displayDogs(item)
    })
})

//select 기능 구현 (change 이벤트)
select.addEventListener("change", function(){
    imgs.innerHTML = "" 
    let filteredDog = currentDogs.filter(function(item){
        return (item.indexOf(select.value) !== -1)
    })


    //필터된 강아지 사진 뿌리기
    filteredDog.forEach(function(item){
        displayDogs(item)
    })
})

// more 버튼: 강아지 사진 추가로 보여주기
more.addEventListener("click", function(){
    request1.open("get", apiRandomDogs)
    request1.addEventListener("load", function(){
        const response = JSON.parse(request1.response)
        response.message.forEach(function(item){
            currentDogs.push(item)
            displayDogs(item)
        })
    })
    request1.send()
})

// top 버튼 누르면 페이지 위로 올라가야
tothetop.addEventListener("click", function(){
    // scroll은 윈도우 객체가 지님
    //scrollTo: 주어진 위치로 스크롤을 이동한다는 window의 메소드(y축 값(px)을 주면 됨)
    //JS에서 위치정보는 객체 리터럴 형태로 줌
    window.scrollTo({top: 0})
})

/*
과제 
1. 견종 고르는 셀렉트 옆에다 버튼을 하나 추가한다. 
2. 버튼에는 리셋이라고 쓴다. 
3. 해당버튼을 누르면 강아지 42마리의 소스를 새롭게 용청해 받아온다. 
4. 기존에 뿌려진 강아지는 모두 사라지고, 새로운 강아지 42마리로 채워진다. 
*/

//reset button 
// 추가사항: reset, select, filter시에 more과 top 버튼이 사라지지 않도록 HTML에 태그 추가함

reset.addEventListener("click", function(){
    imgs.innerHTML = ""
    currentDogs = []
    request1.open("get", apiRandomDogs)
    request1.addEventListener("load", function(){
        const response = JSON.parse(request1.response)
        console.log(response.message)
        response.message.forEach(function(item){
            currentDogs.push(item)
            displayDogs(item)
        })
    })
    request1.send()
})