

var ajax1;

function iniciarPesquisa(elem){
	ajax1 = new AjaxRequest();
	elem.innerHTML = "<center><img id='imgloading' src='img/icons/load.gif' /></center>";
}

function submit(elem,email,senha){
	elem.innerHTML="";
	if(!campo_vazio(email)){
		if(!campo_vazio(senha)){
			if(!valida_email(email)){
				elem.innerHTML="Formato de e-mail não reconhecido!";
			}else{
				login(elem,email,senha);
			}
		}else{
			elem.innerHTML="Campo Vazio";
		}
	}else{
		elem.innerHTML="Campo Vazio";
	}
	
}

function login(elem,email,senha){
		iniciarPesquisa(elem);
		document.getElementById('erros_login').innerHTML = "";
		ajax1.openGET("login-post.php?emailp="+email.value+"&senhap="+senha.value, innerLogin);
}

function innerLogin(){
	if(ajax1.getReadyState()==4){
		document.getElementById('erros_login').innerHTML = "";
		document.getElementById('erros_login').innerHTML = ajax1.getResponseText();
		ajax1=null;
	}
	if(ajax1.getReadyState()==1){
		document.getElementById('erros_login').innerHTML = "<center><img id='imgloading' src='img/icons/load.gif'/></center>";
	}
}