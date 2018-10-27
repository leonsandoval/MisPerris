// jQuery(document).ready(function(){
//   //Carrusel
//     jQuery('#carousel').skdslider({
//       slideSelector: '.slide',
//       delay:5000,
//       animationSpeed:2000,
//       showNextPrev:true,
//       showPlayButton:true,
//       autoSlide:true,
//       animationType:'fading'
//     });

//     //galeria
//     $('#whatever').hoverGrid();

//     $("#cboRegiones").chained("#cboComuna");
// });
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.sidenav');
  var instances = M.Sidenav.init(elems);
});

$(document).ready(function(){
  $('.sidenav').sidenav();
  
  $('.carousel').carousel({
    fullWidth: true,
    duration: 200,
    indicators: true
  });
  $('.datepicker').datepicker({
    format:	'yyyy-mm-dd',
    i18n: { months: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"], monthsShort: ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Set", "Oct", "Nov", "Dic"], weekdays: ["Domingo","Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"], weekdaysShort: ["Dom","Lun", "Mar", "Mie", "Jue", "Vie", "Sab"], weekdaysAbbrev: ["D","L", "M", "M", "J", "V", "S"] },
  });
  $('select').formSelect();

  $('.modal').modal();
});

autoplay();

function autoplay() {
    $('.carousel').carousel('next');
    setTimeout(autoplay, 4500);
}

// $('.carousel.carousel-slider').carousel();