const prevButton = document.querySelector(".prev");
const nextButton = document.querySelector(".next");
const carousel = document.querySelector(".carousel");


//클릭시 사진이 넘어가도록: index는 0,1,2(세가지 사진)값을 가질 수 있음

let idx = 0;

//idx가 0일때 prev 버튼은 작동할 수 없어야함
prevButton.addEventListener('click',() => {
    if (idx === 0) return;
    idx -= 1;

    carousel.style.transform = `translate3d(-${800 * idx}px, 0, 0)`;
});

//idx가 2일때 next 버튼은 작동할 수 없어야함
nextButton.addEventListener('click', () => {
    if (idx === 2) return;
    idx += 1;
    carousel.style.transform = `translate3d(-${800 * idx}px, 0, 0)`;
});

