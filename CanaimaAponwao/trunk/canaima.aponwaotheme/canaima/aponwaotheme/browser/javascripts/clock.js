var arreglo_dia=new Array("Lunes","Martes","Mi&eacute;rcoles",
                          "Jueves","Viernes","S&aacute;bado","Domingo");

var arreglo_mes=new Array("Enero","Febrero","Marzo","Abril","Mayo",
                          "Junio","Julio","Agosto","Septiembre","Octubre",
                          "Noviembre","Diciembre");

function dame_fecha(){

    var a=new Date();
    var b=a.getYear();

    if(b<1000){b+=1900}

    var c=a.getDay();
    var d=a.getMonth();
    var e=a.getDate();
    var f=a.getHours();
    var g=a.getMinutes();
    var h=a.getSeconds();
    var i="AM";

    if(f>=12){i="PM"}
    if(f>12){f=f-12}
    if(f==0){f=12}
    if(g<=9){g="0"+g}
    if(h<=9){h="0"+h}

    var j="Bienvenido! Hoy es "+arreglo_dia[c-1]+", "+e+" de "+arreglo_mes[d]+" y son las "+f+":"+g+" "+i;

    if(document.getElementById){
        document.getElementById("clock").innerHTML=j
    }else{
        document.write(j)
    }
}

function showdate(){
    setInterval("dame_fecha()",1000)
}
