function apagaTexto(elem){
	elem.value="";
}

function restauraTexto(elem,text){
	if(elem.value==""){
		elem.value=text;
	}
}

function campoVazio(elem){
	if(elem.value==""){
		return false;
	}
	return true;
}

function gerarPDF(idp,idm){
	location.href="gerador.php?idm="+idm+"&idp="+idp;
}

function gerarPDFSeminario(){
	location.href="gerador_seminario.php";
}

function changeView(elem){
	if(elem.className=="hidden"){
		elem.className="show";
	}else{
		elem.className="hidden";
	}
}

function limparForm(form){
	for (var i=0; i < form.length; i++) {
		if(form[i].nodeName=="INPUT"){
			form[i].value="";
		}else{
			form[i].innerHTML="";
		}
	}
}

function abreCardProjeto(elem, icone){
	
	$(icone).children().first().children().css("-webkit-transition", "transform 0.5s");
	$(icone).children().first().children().css("-moz-transition", "transform 0.5s");
	$(icone).children().first().children().css("-o-transition", "transform 0.5s");
	$(icone).children().first().children().css("transition", "transform 0.5s");

	var disp = document.getElementById(elem).style.display;

	if(disp == 'block'){
		$(icone).children().first().children().css("-webkit-transform", "rotate(360deg)");
		$(icone).children().first().children().css("-moz-transform", "rotate(360deg)");
		$(icone).children().first().children().css("-o-transform", "rotate(360deg)");
		$(icone).children().first().children().css("transform", "rotate(360deg)");
	}else{
		$(icone).children().first().children().css("-webkit-transform", "rotate(180deg)");
		$(icone).children().first().children().css("-moz-transform", "rotate(180deg)");
		$(icone).children().first().children().css("-o-transform", "rotate(180deg)");
		$(icone).children().first().children().css("transform", "rotate(180deg)");
	}

	$("#"+elem).slideToggle();

}

