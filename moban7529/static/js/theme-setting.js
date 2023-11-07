
/*========================
 Dark setting js
 ==========================*/
$("#darkButton").on("click", function () {
    var href = $("#color-link").attr("href");
    $("body").removeClass("light");
    $("body").addClass("dark");
    document
        .getElementById("color-link")
        .setAttribute("href", "assets/css/dark.css");
});

$("#lightButton").on("click", function () {
    var href = $("#color-link").attr("href");
    $("body").removeClass("dark");
    $("body").addClass("light");
    document
        .getElementById("color-link")
        .setAttribute("href", "assets/css/style.css");
    console
});

/*========================
   RTL setting js
   ==========================*/
$(".rtl").on("click", function () {
    if ($("body").hasClass("ltr")) {
        $("html").attr("dir", "rtl");
        $("body").removeClass("ltr");
        $("body").addClass("rtl");
        $("#rtl-link").attr("href", "assets/css/vendors/bootstrap.rtl.css");
    } else {
        $("html").attr("dir", "");
        $("body").removeClass("rtl");
        $("body").addClass("ltr");
        $("#rtl-link").attr("href", "assets/css/vendors/bootstrap.css");
    }
});