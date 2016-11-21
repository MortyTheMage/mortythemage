var nav = $('#nav');
var menu = $('#menu_wrapper');
var menu_toggle = $('#menu_toggle');
var navigation = function(){
	nav.attr('style','top:-' + menu.height() + 'px');
};
var menuToggle = function(){
	console.log(nav.offset().top)
	if(nav.offset().top == 0){
		nav.animate({
			top: '-' + menu.height() + 'px'
		},400)
	} else {
		nav.animate({
			top: '0px'
		},200);
	}
};