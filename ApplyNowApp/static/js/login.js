$( ".Indexinputcontent" ).focusin(function() {
    $( this ).find( "span" ).animate({"opacity":"0"}, 200);
  });
  
  $( ".Indexinputcontent" ).focusout(function() {
    $( this ).find( "span" ).animate({"opacity":"1"}, 300);
  });

  $( ".inputcontent" ).focusin(function() {
    $( this ).find( "span" ).animate({"opacity":"0"}, 200);
  });
  
  $( ".inputcontent" ).focusout(function() {
    $( this ).find( "span" ).animate({"opacity":"1"}, 300);
  });

  $( ".changepass" ).focusin(function() {
    $( this ).find( "span" ).animate({"opacity":"0"}, 200);
  });
  
  $( ".changepass" ).focusout(function() {
    $( this ).find( "span" ).animate({"opacity":"1"}, 300);
  });

  $( ".changepass" ).focusin(function() {
    $( this ).find( ".icon" ).animate({"opacity":"1"}, 300);
  });
  
  $( ".changepass" ).focusout(function() {
    $( this ).find( ".icon" ).animate({"opacity":"0"}, 200);
  });

  
  
  $(".login").submit(function(){
    $(this).find(".submit i").removeAttr('class').addClass("fa fa-check").css({"color":"#fff"});
    $(".submit").css({"background":"#2ecc71", "border-color":"#2ecc71"});
    $(".feedback").show().animate({"opacity":"1", "bottom":"-80px"}, 400);
    $("input").css({"border-color":"#2ecc71"});
    return false;
  });

  function refrescarPagina()
{
  window.location.reload();
};

$(document).ready(function () {

  $('.increment-btn').click(function (e) {
    var inc_value = $(this).closest('.accesorio_data').find('.qty-input').val();
    var limite_accesorio = $(this).closest('.accesorio_data').find('.accesorio_cantidad').val();
    var value = parseInt(inc_value,limite_accesorio);
    value = isNaN(value) ? 0 : value;
    if(value < 10)
    {
        value++;
        $(this).closest('.accesorio_data').find('.qty-input').val(value);
    }
  });

  $('.decrement-btn').click(function (e) {

      var dec_value = $(this).closest('.accesorio_data').find('.qty-input').val();
      var value = parseInt(dec_value,10);
      value = isNaN(value) ? 0 : value;
      if(value > 1)
      {
          value--;
          $(this).closest('.accesorio_data').find('.qty-input').val(value);
      }
  });


  $('.solicitudAccesorio').click(function (e) {
    var accesorio_id= $(this).closest('.accesorio_data').find('.accesorio_id').val();
    var accesorio_qty = $(this).closest('.accesorio_data').find('.qty-input').val();
    var accesorio_tipo = $(this).closest('.accesorio_data').find('.accesorio_tipo').val();
    console.log(accesorio_tipo);
    var token = $('input[name=csrfmiddlewaretoken]').val();
    
    $.ajax({
        method: "POST",
        url: "../solicitarsolicitud_accesorio",
        data: {
            'accesorio_id' : accesorio_id,
            'accesorio_qty' : accesorio_qty,
            'accesorio_tipo' : accesorio_tipo,
            csrfmiddlewaretoken : token
        },
        success: function (response) {
            console.log(response)
            document.location.href='../';
        }
    });

  });

  $(document).on('click','.entregarAccesorio', function (e) {

    var accesorio_id= $(this).closest('.accesorio_data').find('.accesorio_id').val();
    var accesorio_user= $(this).closest('.accesorio_data').find('.accesorio_user').val();
    var accesorio_tipo= $(this).closest('.accesorio_data').find('.accesorio_tipo').val();
    var accesorio_cantidad= $(this).closest('.accesorio_data').find('.accesorio_cantidad').val();
    var token = $('input[name=csrfmiddlewaretoken]').val();
    console.log(accesorio_tipo);
    
    $.ajax({
        method: "POST",
        url: "../solicitarentregar_accesorio",
        data: {
            'accesorio_id' : accesorio_id,
            'accesorio_user' : accesorio_user,
            'accesorio_tipo' : accesorio_tipo,
            'accesorio_cantidad' : accesorio_cantidad,
            csrfmiddlewaretoken : token
        },
        success: function (response) {
            console.log(response);
            alertify.success(response.estado);
            $('.cartdata').load(location.href + " .cartdata");
        }
    });

});

});

$(document).ready(function () {

  $('.increment-btn2').click(function (e) {
    var inc_value = $(this).closest('.entretenimiento_data').find('.qty-input').val();
    var limite_accesorio = $(this).closest('.entretenimiento_data').find('.entretenimiento_cantidad').val();
    var value = parseInt(inc_value,limite_accesorio);
    value = isNaN(value) ? 0 : value;
    if(value < 10)
    {
        value++;
        $(this).closest('.entretenimiento_data').find('.qty-input').val(value);
    }
  });

  $('.decrement-btn2').click(function (e) {

      var dec_value = $(this).closest('.entretenimiento_data').find('.qty-input').val();
      var value = parseInt(dec_value,10);
      value = isNaN(value) ? 0 : value;
      if(value > 1)
      {
          value--;
          $(this).closest('.entretenimiento_data').find('.qty-input').val(value);
      }
  });

  $('.solicitudEntretenimiento').click(function (e) {
    var entretenimiento_id= $(this).closest('.entretenimiento_data').find('.entretenimiento_id').val();
    var entretenimiento_qty = $(this).closest('.entretenimiento_data').find('.qty-input').val();
    var entretenimiento_tipo = $(this).closest('.entretenimiento_data').find('.entretenimiento_tipo').val();
    var token = $('input[name=csrfmiddlewaretoken]').val();
    
    $.ajax({
        method: "POST",
        url: "../solicitarsolicitud_entretenimiento",
        data: {
            'entretenimiento_id' : entretenimiento_id, 
            'entretenimiento_qty' : entretenimiento_qty,
            'entretenimiento_tipo' : entretenimiento_tipo,
            csrfmiddlewaretoken : token
        },
        success: function (response) {
            console.log(response)
            document.location.href='../';
        }
    });

  });

  $(document).on('click','.entregarEntretenimiento', function (e) {

    var entretenimiento_id= $(this).closest('.entretenimiento_data').find('.entretenimiento_id').val();
    var entretenimiento_user= $(this).closest('.entretenimiento_data').find('.entretenimiento_user').val();
    var entretenimiento_tipo= $(this).closest('.entretenimiento_data').find('.entretenimiento_tipo').val();
    var entretenimiento_cantidad= $(this).closest('.entretenimiento_data').find('.entretenimiento_cantidad').val();
    var token = $('input[name=csrfmiddlewaretoken]').val();
    
    $.ajax({
        method: "POST",
        url: "../solicitarentregar_entretenimiento",
        data: {
            'entretenimiento_id' : entretenimiento_id,
            'entretenimiento_user' : entretenimiento_user,
            'entretenimiento_tipo' : entretenimiento_tipo,
            'entretenimiento_cantidad' : entretenimiento_cantidad,
            csrfmiddlewaretoken : token
        },
        success: function (response) {
            console.log(response);
            alertify.success(response.estado);
            $('.cartdata').load(location.href + " .cartdata");
        }
    });

});

});

/*PERFIL */
$(document).ready(function(){
  $("#hide").on('click', function() {
      /*Campos vizualizar datos */
      $("#element1").hide();
      $("#element1-1").hide();
      $("#element1-2").hide();
      $("#element1-3").hide();
      $("#element1-4").hide();
      $("#element1-5").hide();
      $("#element1-6").hide();
      $("#elementC").show();
      $("#---").show();
      $("#show").show();
      $("#hide").hide();
      /*Campos modificar datos */
      $("#element2").show();
      $("#element2-1").show();
      $("#element2-2").show();
      $("#element2-3").show();
      $("#element2-4").show();
      $("#element2-5").show();
      $("#element2-6").show();
      return false;
  });

  $("#elementC").on('click', function() {
      /*Campos vizualizar datos */
      $("#element1").show();
      $("#element1-1").show();
      $("#element1-2").show();
      $("#element1-3").show();
      $("#element1-4").show();
      $("#element1-5").show();
      $("#element1-6").show();
      $("#elementC").hide();
      $("#---").hide();
      $("#show").hide();
      $("#hide").show();
      /*Campos modificar datos */
      $("#element2").hide();
      $("#element2-1").hide();
      $("#element2-2").hide();
      $("#element2-3").hide();
      $("#element2-4").hide();
      $("#element2-5").hide();
      $("#element2-6").hide();
    return false;
  });

  $("#passHide").on('click', function() {
      /*Campos modificar datos */
      $("#pass1").show();
      $("#pass1-1").show();
      $("#pass1-2").show();
      $("#passSave").show();
      $("#passCancel").show();
      $("#passHide").hide();
      return false;
  });

  $("#passCancel").on('click', function() {
    /*Campos modificar datos */
    $("#pass1").hide();
    $("#pass1-1").hide();
    $("#pass1-2").hide();
    $("#passSave").hide();
    $("#passCancel").hide();
    $("#passHide").show();
    return false;
  });

  $("#dropdownLogin").on('click', function() {
    /*Campos modificar datos */
    $("#drop").hide();
    $("#drop1").show();
    $("#drop2").show();
    return false;
  });
});


/*SHOW PASSWORD */
function mostrarPassword(){
  var cambio = document.getElementById("passwordN");
  if(cambio.type == "password"){
    cambio.type = "text";
    $('.icon').removeClass('fa fa-eye-slash').addClass('fa fa-eye');
  }else{
    cambio.type = "password";
    $('.icon').removeClass('fa fa-eye').addClass('fa fa-eye-slash');
  }
} 

function mostrarPassword1(){
  var cambio = document.getElementById("password");
  if(cambio.type == "password"){
    cambio.type = "text";
    $('.icon').removeClass('fa fa-eye-slash').addClass('fa fa-eye');
  }else{
    cambio.type = "password";
    $('.icon').removeClass('fa fa-eye').addClass('fa fa-eye-slash');
  }
} 

function verificarPassword() {
  var inputName = document.getElementById("passwordN");
  if (inputName.length >= 8) {

  }
}
