$(document).on("touchstart mousedown touchend mouseup", "button", function (e) {
    e.preventDefault();
    if (e.type === "touchstart" || e.type === "mousedown") {
        $(this).addClass("clicked");
    } else {
        $(this).removeClass("clicked").blur();
    }
});
