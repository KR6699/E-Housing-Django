console.log('hii');


// $.fn.menter = function(id) {

//     $(id).mouseenter(function() {
//         console.log("entered");
//         $(id).css("background-color", 'orange');
//     });
//     // }
//     // $.fn.mleave = function(id) {

//     $(id).mouseleave(function() {
//         console.log("eleave");
//         $(id).css("background-color", '');
//     });
// }
$("#home,#logout,#slist,#rlist,#myaccount,#myhome,#mymessage,#admin,#complain").mouseenter(function() {
    $(this).css("background-color", 'orange');
    $(this).css("font-size", '18px');

})
$("#home,#logout,#slist,#rlist,#myaccount,#myhome,#mymessage,#admin,#complain").mouseleave(function() {
    $(this).css("background-color", '');
    $(this).css("font-size", '');
})

$(".slist").mouseenter(function() {
    $(this).css("background-color", 'orange');
    $(this).css("color", "green");
})
$(".slist").mouseleave(function() {
    $(this).css("background-color", '#0072b5');
    $(this).css("color", "#f5df4d");
})

$(".sname").mouseenter(function() {
    $(this).css("color", "white");
})
$(".sname").mouseleave(function() {
    $(this).css("color", "#f5df4d");
})

$(".society,.myaccount,.rentlist,.selllist,.rhview,.shview,.myhome").mouseenter(function() {
    $(this).css({
        "background-color": 'chartreuse',
        "color": "#000000FF"
    });
})
$(".society,.myaccount,.rentlist,.selllist,.rhview,.shview,.myhome").mouseleave(function() {
    $(this).css({
        "background-color": '#000000FF',
        "color": "#FFFFFF"
    });
})
$('.mymsgs').mouseenter(function() {
    $(this).css({
        "background-color": 'chartreuse',
        // "color": "#000000FF"
    })
})
$('.mymsgs').mouseleave(function() {
    $(this).css({
        "background-color": '#FCF6F5FF',
        // "color": "#000000FF"
    })
})
$('.sub').mouseenter(function() {
    $(this).css("font-size", '18px');
})
$('.sub').mouseleave(function() {
    $(this).css("font-size", '');
})