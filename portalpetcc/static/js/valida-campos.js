
function campo_vazio(field){
	if(field.value.length==0){
		return true;
	}
	return false;
}

function valida_email(email){
	var email_padrao = new RegExp("\D*@inf.ufsm.br");
	if(email_padrao.test(email.value)){
		return true;
	}
	return false;
}