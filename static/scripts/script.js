$(document).ready(function() {}
    $(".add").click(function() {
        $("form > p:first-child").clone(true).insertBefore("form > p:last-child");
    });

    $(".remove").click(function() {
        $(this).parent().remove();
    });
});