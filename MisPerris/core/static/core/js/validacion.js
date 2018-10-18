
function NumText(string){//solo letras y numeros
    var out = '';
    //Se añaden las letras validas
    var filtro = 'kK1234567890';//Caracteres validos
	
    for (var i=0; i<string.length; i++)
       if (filtro.indexOf(string.charAt(i)) != -1) 
	     out += string.charAt(i);
    return out;
}
function Numeros(string){//Solo numeros
    var out = '';
    var filtro = '1234567890';//Caracteres validos
	
    //Recorrer el texto y verificar si el caracter se encuentra en la lista de validos 
    for (var i=0; i<string.length; i++)
       if (filtro.indexOf(string.charAt(i)) != -1) 
             //Se añaden a la salida los caracteres validos
	     out += string.charAt(i);
	
    //Retornar valor filtrado
    return out;
} 



$(document).ready(function() {
    $("#formularioAuto").validate({
        rules:{
            txtMail:{
                required:true,
                minlength:6,
                maxlength:50,
                email:true
            },
            txtRun:{
                required:true,
                minlength:7,
                maxlength:8,
            },
            txtDV:{
                required:true,
                minlength:1,
                maxlength:1,
            },
            cboRegion:{
                required:true
           },
            txtNacimiento: {
                required:true,
                date:true,
            },
            txtFono:{
                required:true,
                maxlength:10
            }
        },
        messages:{
            txtMail:{
                required:"Este campo es requerido",
                minlength:"Minimo 6 caracteres",
                maxlength:"Maximo 50 caracteres"
            },
            txtRun:{
                required:"Este campo es requerido",
                minlength:"Minimo 7 caracteres",
                maxlength:"Maximo 8 caracteres"
            },
            cboRegion:{
                required:"Seleccione una region"
            },
            txtNacimiento: {
                required:"Este campo es requerido",
                min:"Debe ser mayor o igual a 1950",
                max:"Debe ser menor o igual a 2018"
            }
        }
    });
});