var indicador = 0;

$(document).ready(function(){
    $('.prev').click(function(e){
        e.preventDefault();
        moverSlider('left');
    });

    $('.next').click(function(e){
        e.preventDefault();
        moverSlider('right');
    });
    defineSizes();

    $(".posicionado").parent().css({
        'box-shadow':' 0.1rem 0.1rem 0.1rem black'
    });
});

$(window).resize(defineSizes);

function defineSizes(){
    $('.slider_container .slide').each(function(i, e){
       $(e).css({
           'background-image': 'url(' + $(e).data("background") + ')',
           'height' : ($('.slider_container').width() * 0.25) + 'px',
           'width' : '100%'//($('.slider_container').width() * 1) + 'px'
       });
    });
    
    $('.slider_container .slide_container').css({
        'margin-left' : -(indicador * $('.slider_container').width()) + 'px'
    });
}

function moverSlider(dir){
    var limite = $('.slider_container .slide').length;
    indicador = ( dir == 'right' ) ? indicador + 1 : indicador - 1;
    indicador = ( indicador >= limite ) ? 0 : indicador;
    indicador = ( indicador < 0 ) ? limite - 1 : indicador;
    
    $('.slider_container .slide_container').animate({
        'margin-left' : -(indicador * $('.slider_container').width()) + 'px'
    });
}
