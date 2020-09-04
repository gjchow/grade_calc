$(document).ready(function() {
    let num = 1;
    let len = 1;
    let temp = "";
    $("button").click(function() {
        if ($(this).attr("class") == "add"){
//            alert("Clicked add");
            num += 1;
            len += 1
            temp = '<div class="in'+num+'"><p><input type="text" id="mark'+num+'" name="mark'+num+'" placeholder="Mark"><input type="text" id="percent'+num+'" name="percent'+num+'" placeholder="Percentage of grade"><br></p></div>';
            $(".main").append(temp);
        }
        else if($(this).attr("class") == "remove"){
            if (num == 1){
                alert("Must have at least 1 entry")
            }
            else {
            len -= 1
            num -= 1
            $(".in"+num).remove()
            }
        }
    });
});
