const todoList = document.getElementById("todo-list")
const todoForm = document.getElementById("todo-form")

let todoArr = [];


// 할일 추가
todoForm.addEventListener("submit", function(event){
    event.preventDefault() // submit 하면 새로고침이 일어나는데, 이를 막겠다
    //todoArr.push(event.target.todo.value)
    //console.log(todoArr)
    //객체 리터럴 생성
    const toBeAdded = {
        todoText: todoForm.todo.value,
        todoID: new Date().getTime(), // 시간정보를 정수형태로 반환
        todoDone: false
    }
    todoForm.todo.value = ""
    todoArr.push(toBeAdded)
    displayTodo()
    saveTodo() // 로컬 스토리지 저장
    // console.log(todoArr)
})

// 할일 보여주기
function displayTodo(){
    todoList.innerHTML = ""
    todoArr.forEach(function(todo){
        const todoItem = document.createElement("li")        
        //todo 화면에 보여주기
        todoItem.textContent = todo["todoText"]
        todoList.appendChild(todoItem)

        //li가 만들어질때 삭제버튼도 같이 생성하겠다
        const todoDelBtn = document.createElement('span')
        todoDelBtn.textContent ="X"
        todoItem.appendChild(todoDelBtn)

        // title 삽입
        todoItem.title = "클릭하면 완료됨"
        todoDelBtn.title = "클릭하면 삭제됨"

        //todoItem에 클래스 추가하기 : true or false -> 값에 따라 배경색을 다르게 하겠다
        if (todo["todoDone"]){
            todoItem.classList.add("done")
        }else{
            todoItem.classList.add("yet")
        }
        
        // 할일리스트 누르면 발생하는 이벤트 추가
        //이벤트 등록
        todoItem.addEventListener("click", () => handleTodoItemClick(todo["todoID"])) 
        todoDelBtn.addEventListener("click", function(){
            handleTodoDelClick(todo["todoID"])
        })
    })
}

// 할일 수정하기: done or not completed 표시 다르게 하기 
function handleTodoItemClick(clickID){
    //특정할일을 클릭하면, 해당 할일의 todoID를 받아와서 todoDone: true로 바꿔준다
    todoArr = todoArr.map(function(todo){
        if (todo["todoID"] === clickID){
            //기존의 todo item에다가 todoDone을 (true-> false) or false -> true로 바꿔준다
            return { 
                ...todo, todoDone : !todo["todoDone"] 
            }
        }else{
            return todo
        }
    })
    //console.log(todoArr)
    displayTodo()
    saveTodo()
}


//할일 삭제하기 : 클릭시 해당 리스트만 삭제
function handleTodoDelClick(clickID){
    //클릭된 애만 제외하고 나머지만 남겨두겠다
    todoArr = todoArr.filter(function(todo){
        return todo["todoID"] !== clickID
    })

    displayTodo()
    saveTodo()
}

//로컬스토리지에 저장하기
function saveTodo(){
    const todoString = JSON.stringify(todoArr)
    localStorage.setItem("myTodo", todoString)
}
// 로컬스토리지에서 가져오기: 웹페이지 열었을때 가져오면 됨
function loadTodo(){
    const myTodo = localStorage.getItem("myTodo")
    if (myTodos != null){
        todoArr = JSON.parse(myTodo)
        displayTodo()
    }
}

loadTodo()
