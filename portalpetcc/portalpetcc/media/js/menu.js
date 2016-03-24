function menufixo() {
 	var nav = document.getElementById("menn");

    $(window).scroll(function () {
      	if ($(this).scrollTop() > 320 && !nav.hasClass("fixo")) {
	        nav.addClass("fixo");
        } else {
            nav.removeClass("fixo");
        }
    });
 }