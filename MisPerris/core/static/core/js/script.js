jQuery(document).ready(function(){
  //Carrusel
    jQuery('#carousel').skdslider({
      slideSelector: '.slide',
      delay:5000,
      animationSpeed:2000,
      showNextPrev:true,
      showPlayButton:true,
      autoSlide:true,
      animationType:'fading'
    });

    //galeria
    $('#whatever').hoverGrid();

    $("#cboRegiones").chained("#cboComuna");
});