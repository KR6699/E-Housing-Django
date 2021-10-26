$(".button").mouseenter(function() {
    $(this).css("background-color", 'orange');
    // $(this).css("font-size", '18px');

})
$(".button").mouseleave(function() {
    $(this).css("background-color", '#e3f2fd');
    // $(this).css("font-size", '');
})

$(".slist,.hreport,.mreport,.slist,.rlist,.complainlist").mouseenter(function() {
    $(this).css("background-color", 'chartreuse');
    $(this).css("color", "black");
})
$(".slist,.hreport,.mreport,.slist,.rlist,.complainlist").mouseleave(function() {
    $(this).css("background-color", '');
    $(this).css("color", "");
})