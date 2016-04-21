function AjaxRequest(){
	if (window.XMLHttpRequest){
		try{
	        this.request = new XMLHttpRequest(); // Outros Navegadores
	    }catch(e){
	    	this.request = null;
	    }
    }
}

AjaxRequest.prototype.openGET = function(url, funcao){
	this.request.open('GET',url,true);
	this.request.send(null);
	this.request.onreadystatechange = funcao;
}

AjaxRequest.prototype.getReadyState = function() {
  return this.request.readyState;
}

AjaxRequest.prototype.getStatus = function() {
  return this.request.status;
}

AjaxRequest.prototype.getResponseText = function() {
  return this.request.responseText;
}

AjaxRequest.prototype.getResponseXML = function() {
  return this.request.responseXML;
}


function create_participacao(){
    $.ajax({
        url : "/create_participacao/", // the endpoint
        type : "POST", // http method
        data : { nome : $('#nome').val(),
                 sobrenome : $('#sobrenome').val(),
                 matricula : $('#matricula').val(),
                 email: $('#email').val(),
                 curso: $('#curso').val(),
                 minicurso: $('#select_minicurso').val(),
                 csrfmiddlewaretoken: $('#csrfmiddlewaretoken').val()
               }, // data sent with the post request
        // handle a successful response
        success : function(json) {
            $('#alert_ji').fadeOut(200);
            $('#alert_le').fadeOut(200);
            $('#alert_ic').fadeOut(200);
            $('#alert_err').fadeOut(200);
            $('#alert_mi').fadeOut(200);
            switch(json['result']){
                case 'JI':
                    $('#alert_ji').slideDown(400);
                    break;
                case 'LE':
                    $('#alert_le').slideDown(400);
                    break;
                case 'IC':
                    $('#alert_ic').slideDown(400);
                    $('#nome').val('');
                    $('#matricula').val('');
                    $('#email').val('');
                    break;
                case 'MI':
                    $('#alert_mi').slideDown(400);
                    break;
            }
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#alert_ji').fadeOut(200);
            $('#alert_le').fadeOut(200);
            $('#alert_ic').fadeOut(200);
            $('#alert_err').fadeOut(200);
            $('#alert_mi').fadeOut(200);
            $('#alert_err').slideDown(400);
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

function abre_lat(elemento){
    if (elemento=='ultimas_lat'){
        if($('#bt_ultimas_lat').hasClass("ativa")){
            return;
        }else{
            $('#bt_populares_lat').removeClass('ativa');
            $('#bt_ultimas_lat').addClass('ativa');

            $('#ultimas_lat').css('display', 'block');
            $('#populares_lat').css('display', 'none');
        }
    }else{
        if($('#bt_populares_lat').hasClass("ativa")){
            return;
        }else{
            $('#bt_ultimas_lat').removeClass('ativa');
            $('#bt_populares_lat').addClass('ativa');

            $('#populares_lat').css('display', 'block');
            $('#ultimas_lat').css('display', 'none');
        }
    }
}

function muda_ano(elem) {

    var anoselecionado = elem.value;
    var it = 0;
    $('select[name="cert_atividade"] option').each(function(){
        var $this = $(this);
        if(it == 0){
                $('select[name="cert_atividade"]').val($this);
            }
            it = it+1;
        if($this.data('ano') == anoselecionado){

            $this.show();
        }else {
            $this.hide();
        }
    });
};

function buscaCertificados(){
    $.ajax({
        url : "/busca_certificados/", // the endpoint
        type : "POST", // http method
        data : { matricula : $('#matr_aluno').val(),
                 atividade: $('#cert_atividade').val(),
                 ano: $('#cert_ano').val(),
                 csrfmiddlewaretoken: $('#csrfmiddlewaretoken').val()
               }, // data sent with the post request
        // handle a successful response
        success : function(json) {
            $('#matricula').val('');
            //var data_resp = JSON.parse(json);
            var encontrado = false;
            $('#resultado_pesquisa_certificado').html('');
            $('#resultado_pesquisa_certificado').fadeOut(200);

            $.each(json, function(i, itemData){
                encontrado=true;
                console.log(itemData);
                var hora = itemData['horas']==1?"hora":"horas";
                var tipo_atv = ""
                $('#resultado_pesquisa_certificado').append('<div class="row linha_cert"><div class="small-12 columns"><div class="row"><div class="small-5 columns text_cert">'+ itemData['atividade'] + tipo_atv  +'</div><div class="small-3 columns text_cert">'+itemData['data_inicial']+" - "+itemData['data_final']+'</div><div class="small-2 columns text_cert">'+itemData['horas']+ " " +hora+'</div><div class="small-2 columns" ><a href=""><div class="row"><div class="small-12 columns small-centered text-center link_cert">Certificado <img src="/media/img/icons/doc.jpg" width="20" alt=""></div></div></a></div></div></div></div>');


            });
            if(!encontrado){
                $('#resultado_pesquisa_certificado').append('<div class="row linha_cert cert_indisp"><div class="small-12 columns">Certificado não encontrado!</div></div>');
            }

            $('#resultado_pesquisa_certificado').slideDown(600);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText + " - " + errmsg); // provide a bit more info about the error to the console
        }
    });
}