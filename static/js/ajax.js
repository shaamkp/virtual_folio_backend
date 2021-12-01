$(document).ready(function(){
    $("a").on("click", "div.done", function(e){
        e.preventDefault(); 
        console.log("done");
    })
})
