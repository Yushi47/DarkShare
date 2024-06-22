$(document).on("touchstart mousedown", "button", function (e) {
    $(this).addClass("clicked");
});

$(document).on("touchend mouseup", "button", function (e) {
    $(this).removeClass("clicked").blur();
});
