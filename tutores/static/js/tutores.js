$(document).ready(function(){
	if($(document).width() > 479){
        $(".wrapper").css({
            'height': $(document).height() - ($("header").height() + ($("nav").height() * 3) + $("footer").height()),
        });
    }
});