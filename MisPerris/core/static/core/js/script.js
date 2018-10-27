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
    language: 'es',
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