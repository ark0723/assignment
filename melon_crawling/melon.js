

// show updated time
let json_file = "melon_20240131 22:00.json"
let f_date = json_file.substr(6,14)
//console.log(f_date)

const time_p = document.getElementById("time")
time_p.textContent = f_date


// update table data
$(document).ready(function(){
	$.getJSON("melon.json",function(data){
		
		//할 일 처리
		let row="";
		$.each(data,function(key,value){
			console.log(key);
			row+="<tr>";
			row+="<td>"+value.ranking+"</td>"
			row+="<td><img src = "+ value.image + " width = '48' height = '48'></td>"
			row+="<td>"+value.title+"</td>"
			row+="<td>"+value.singer+"</td>"

			row+="</tr>";
			
		});
		$("#melon_table").append(row);
	});
});