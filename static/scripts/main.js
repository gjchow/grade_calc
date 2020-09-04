$(document).ready(function() {
    let num = 1;
    let len = 1;
    let temp = "";
    $("button").click(function() {
        if ($(this).attr("class") == "add"){
            alert("Clicked add");
        }
        else if($(this).attr("class") == "remove"){
            alert("Clicked remove " + this.id);
        }
    });
});
