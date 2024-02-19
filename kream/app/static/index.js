function getNowDate(){
  const now = new Date();
  const year = now.getFullYear();
  const month = String(now.getMonth()+1).padStart(2, '0');
  const day = String(now.getDate()).padStart(2, '0');
  return `Updated on: (${year}-${month}-${day})` 
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

//checkbox
const checkBoxes = document.getElementsByClassName("check_btn")
checkBoxes.forEach(box => {
  if (box.checked === true){
    var row = box.parentNode.parentNode;
    row.style.display = "none";
  }
});

if (element.checked == true) {
  condt1[i].parentElement.closest('tr').style = ""
} else {
  condt1[i].parentElement.closest('tr').style = "display:none"
}


const rows = document.getElementById("data-table").rows
rows.forEach(function(row){
  const checkbox = row.firstChild.firstChild;
  checkbox.addEventListener("change", function(event){
    if (event.clicked){
      row.style.display = "none";
    }else{
      row.style.display = "block";
    }
  })
})



document.querySelectorAll(
 
  // Select all rows except the first one 
  "tr:not(:first-child)").forEach(function (e) {

    // Add onClick event listener
    // to selected rows
    e.addEventListener("click", function () {

        // Get all rows except the first one 
        var rows = 
            [...document.querySelectorAll(
              "tr:not(:first-child)"
            )];

        var notSelectedRows = 
            rows.filter(function (element) {
             
            // Hide the rows that have
            // not been clicked
            if (element !== e) {
                element.style.display = "none";
            }
        });
    });
});

