$(function(){
	$('.menus > li').hover(function() {
		$(this).children('a').addClass('current-menu-item');
		$(this).children('ul').show();
	},function() {		
		$(this).find('ul').hide().end().children('a').removeClass();
	});
});
function click_button(n){
	var a = document.getElementById("entry");
	if(n==1){		
		a.style.fontSize="12px";
	}else if(n==2){		
		a.style.fontSize="14px";
	}else{		
		a.style.fontSize="16px";
	}
}