function getNowDate(){
  const now = new Date();
  const year = now.getFullYear();
  const month = String(now.getMonth()+1).padStart(2, '0');
  const day = String(now.getDate()).padStart(2, '0');
  return `Updated: (${year}-${month}-${day})` 
}
// Update Dates
function ShowDate(){
  const dateDiv = document.getElementById("time_update")
  const p = document.createElement("p")
  p.innerText = getNowDate()
  dateDiv.append(p)
}

// Show date when window uploaded
document.addEventListener("DOMContentLoaded", function(){
  ShowDate()
})

function sortByPrice(order = "0"){
  // form element 불러오기
  const form = document.getElementById("form");
  const price = document.getElementById("price");
  // value = '0' : 오름차순(default), value = '1' : 내림차순
  price.setAttribute('value', order);
  form.submit();
  return true;
}

function hide_row(){
  // checkbox 자신
  const check_btn = document.getElementById(ID)
  // find parent row
  const row = check_btn.parentElement.parentElement;
  if (check_btn.checked == true){
    row.style.display = "none";
  }
}






