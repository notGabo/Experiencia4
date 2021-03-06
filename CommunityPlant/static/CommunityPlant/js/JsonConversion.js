$(document).ready(function(){         
    $.ajax({
            url:"https://mindicador.cl/api", 
                type: "GET",
                success: function(resultado){
                    //fecha 
                    let fecha = resultado.dolar.fecha.slice(0,10);
                    
                    //hora
                    
                    let hora = resultado.dolar.fecha.slice(11,-5)
                    
                    //variable que guarda el valor del dolar en clp
                    var valores = resultado.dolar.valor;

                    //interiores
                    
                    //primera planta
                    
                    var clp1 = 23990;
                    var resultado1 =  clp1 / valores;
                    final1 = resultado1.toFixed(2);
                    $("#clp1").html("Precio USD: "+"<b>"+"$"   +final1 +"</b>" );
                    
                    //segunda planta
                    
                    var clp2 = 20990;
                    var resultado2 = clp2 / valores;
                    final2 = resultado2.toFixed(2);
                    $("#clp2").html("Precio USD: "+"<b>"+"$"   +final2 +"</b>" );
                    
                    //tercera planta

                    var clp3 = 35990;
                    var resultado3 = clp3 / valores;
                    final3 = resultado3.toFixed(2);
                    $("#clp3").html("Precio USD: "+"<b>"+"$"   +final3 +"</b>" );
                    
                    //exteriores
                    
                    //primera planta

                    var clp4 = 30990;
                    var resultado4 =clp4 / valores ;
                    final4 = resultado4.toFixed(2);
                    $("#clp4").html("Precio USD: "+"<b>"+"$"   +final4 +"</b>" );
                    
                    //segunda planta

                    var clp5 = 15990;
                    var resultado5 = clp5 / valores  ;
                    final5 = resultado5.toFixed(2);
                    $("#clp5").html("Precio USD: "+"<b>"+"$"   +final5 +"</b>" );
                   
                    //tercera planta

                    var clp6 = 30000;
                    var resultado6 = clp6 /valores ;
                    final6 = resultado6.toFixed(2);
                    $("#clp6").html("Precio USD: "+"<b>"+"$"   +final6 +"</b>" );

                    //arboles
                    //primer arbol

                    var clp7 = 45990;
                    var resultado7 = clp7 /valores ;
                    final7 = resultado7.toFixed(2);
                    $("#clp7").html("Precio USD: "+"<b>"+"$"   +final7 +"</b>" );

                    //primer arbol

                    var clp8 = 55990;
                    var resultado8 = clp8 /valores ;
                    final8 = resultado8.toFixed(2);
                    $("#clp8").html("Precio USD: "+"<b>"+"$"   +final8 +"</b>" );

                    //primer arbol

                    var clp9 = 60000;
                    var resultado9 = clp9 /valores ;
                    final9 = resultado9.toFixed(2);
                    $("#clp9").html("Precio USD: "+"<b>"+"$"   +final9 +"</b>" );


                    $("#valorDolar").html("Valor dolar = $"+valores)

                    $("#fecha").html("Ultima actualizacion: "+fecha+" "+hora )

                       
                },
                error: function(error){
                    console.log(error);
                }
    })
})

