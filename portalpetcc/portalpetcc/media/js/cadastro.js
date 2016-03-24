function validaMatricula(matr){
	var modelmatr = new RegExp("^20[0-9]{2}[0-9]{5}",'ig');
	if(modelmatr.test(matr)){
		ajax1 = new AjaxRequest();
		return true;
	}
	return false;
}


function cadastrarParticipante(nomep,matr,minicurso){
	if(validaMatricula(matr)){
		iniciarPesquisa('resultado_inscricao');
		//document.getElementById('inform_error_cad').innerHTML = "";
		ajax1.openGET("formulario_inscricao_get.php?nomep="+nomep+"&nomem="+minicurso+"&nomemat="+matr, innerCadastro);
	}else{
		document.getElementById('resultado_inscricao').innerHTML = "";
		document.getElementById('inform_error_cad').innerHTML = "<div id='erro'><center><img height=19 width=19 src='#' /> Matricula Invalida!</center></div>";
	}
}

function innerCadastro(){
	if(ajax1.getReadyState()==4){
		document.getElementById('resultado_inscricao').innerHTML = "";
		document.getElementById('resultado_inscricao').innerHTML = ajax1.getResponseText();
		ajax1=null;
	}
	if(ajax1.getReadyState()==1){
		document.getElementById('resultado_inscricao').innerHTML = "<center><img id='imgloading' src='img/icons/load.gif'/></center>";
	}
}
