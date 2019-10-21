
function goToMenards(){
	window.location.replace('/menards');
}

function goHome(){
	window.location.replace('/home');
}

function goToTarget(){

	window.location.replace('/target');
}

function goToCostco(){
	window.location.replace('/costco');
}

function goSignOut(){
	window.location.replace('/')
}



function setup(){
	$("#MENARDS").click(goToMenards);
	$('#home').click(goHome);
	$("#TARGET").click(goToTarget);
	$('#COSTCO').click(goToCostco);
	$('#signout').click(goSignOut);
}

$(document).ready(setup);

