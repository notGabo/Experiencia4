$(document).ready(function(){         
    $.ajax({
            url:"http://localhost:8000/api/lista_descuento?format=json", 
                type: "GET",
                success: function(resultado){
                    //codigo 
                    let codigo = resultado.IdCodigo;
                    //porcentaje
                    let porc = resultado.Porcentaje;
                    var id1 = document.getElementById("#campodes");

                    if (id1 = codigo){

                        $("#porc1").html(porc)
                    }
                },
                error: function(error){
                    console.log(error);
                }
    })
})

