
function log(str){
  var log = document.getElementById("log")
  if (log){ 
	 // let's be safe...
     log.innerHTML += str + "<br/>";
     }
};
