
var ajax1;

function iniciarPesquisa(elem){
	ajax1 = new AjaxRequest();
	document.getElementById(elem).innerHTML = "<center><img id='imgloading' src='img/icons/load.gif' style='margin-bottom: 10px;' /></center>";
}

function pesquisaCertificados(elem,nomep,nomem,tipo){
	if(tipo=="M"){
		if(validaMatricula(nomep.value)){
			iniciarPesquisa(elem);
			//document.getElementById('inform_error').innerHTML = "";
			ajax1.openGET("pesquisa_certificados_get.php?nomep="+nomep.value+"&nomem="+nomem.value, innerBusca);
		}else{
			document.getElementById('resultado_pesquisa_certificado').innerHTML = "";
			//document.getElementById('inform_error').innerHTML = "<div id='erro'><center><img height=19 width=19 src='#' /> Matricula Invalida!</center></div>";
		}
	}else if(tipo=="S"){
			iniciarPesquisa(elem);
			//document.getElementById('inform_error').innerHTML = "";
			ajax1.openGET("pesquisa_certificados_seminario_get.php?nomep="+nomep.value+"&nomes="+nomem.value, innerBuscaSeminario);
	}
}

function innerBuscaSeminario(){
	if(ajax1.getReadyState()==4){
		document.getElementById('resultado_pesquisa_certificado_seminario').innerHTML = "";
		document.getElementById('resultado_pesquisa_certificado_seminario').innerHTML = ajax1.getResponseText();
		ajax1=null;
	}
	if(ajax1.getReadyState()==1){
		document.getElementById('resultado_pesquisa_certificado_seminario').innerHTML = "<center><img id='imgloading' src='img/icons/load.gif'/></center>";
	}
}

function innerBusca(){
	if(ajax1.getReadyState()==4){
		document.getElementById('resultado_pesquisa_certificado').innerHTML = "";
		document.getElementById('resultado_pesquisa_certificado').innerHTML = ajax1.getResponseText();
		ajax1=null;
	}
	if(ajax1.getReadyState()==1){
		document.getElementById('resultado_pesquisa_certificado').innerHTML = "<center><img id='imgloading' src='img/icons/load.gif'/></center>";
	}
}