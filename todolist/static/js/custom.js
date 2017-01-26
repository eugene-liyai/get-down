$(document).ready(function(){


	clear();

	// signup and login 
	var uname = "";
	var email = "";
	var password = "";
	var repassword = "";

	var lguname = "";
	var lgpass = "";

	// add card, list, and task
	var listnm = "";
	var cardnm = "";
	var cardds = "";
	var taskName = ""

	function validateEmail(email) {
	    var emailTest = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	    //var emailTest = "/^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/"
	    return emailTest.test(email);
	}

	function clear(){
		$('.form-group input').each(function(){
			$(this).val("");
		});
		$('.form-group input').first().focus();
	};


	// signup validation section
	$('#s_uname').keyup(function(){
		var vall = $(this).val();

		if(vall == ""){
			$("#unameError").html("username cannot be blank");
			uname = "";
		}else if(vall.length < 4){
			$("#unameError").html("username too short");
			uname = "";
		}else{
			uname = vall;
			$("#unameError").html("");
		}
	});

	$('#s_email').keyup(function(){
		var vall = $(this).val();

		if(vall == ""){
			$("#emailError").html("email cannot be blank");
			email = "";
		}else if(vall.length < 3){
			$("#emailError").html("email too short");
			email = "";
		}else if(validateEmail(vall) == false){
			$("#emailError").html("Invalid email");
			email = "";
		}else{
			email = vall;
			$("#emailError").html("");
		}
	});

	$("#s_password").keyup(function(){
		var vall = $(this).val();
		if(vall == ""){
			$("#passError").html("password cannot be blank");
			password = "";
		}else if(vall.length < 4){
			$("#passError").html("password must be atleast 4 characters");
			password = "";
		}else{
			password = vall;
			$("#passError").html("");
		}
	});

	$("#s_rpassword").keyup(function(){
		var vall = $(this).val();
		if(vall == ""){
			$("#rpassError").html("password cannot be blank");
			repassword = "";
		}else if(vall.length < 4){
			$("#rpassError").html("password must be atleast 4 characters");
			repassword = "";
		}else if(password !== vall){
			$("#rpassError").html("password mismatch");
			repassword = "";
		}else{
			repassword = vall;
			$("#rpassError").html("");
		}
	});

	$('#submitBtn').click(function(e){
		if(uname == "" || email == ""|| password == "" || repassword ==""){
			e.preventDefault();
			$('#subError').html('Error in the form');
		}else{
			$('#subError').html('');
		}
	});

	// login validation section
	$('#l_uname').keyup(function(){
		var vall = $(this).val();

		if(vall == ""){
			$("#lunameError").html("username cannot be blank");
			lguname = "";
		}else if(vall.length < 4){
			$("#lunameError").html("username too short");
			lguname = "";
		}else{
			lguname = vall;
			$("#lunameError").html("");
		}
	});

	$("#l_password").keyup(function(){
		var vall = $(this).val();
		if(vall == ""){
			$("#lpassError").html("password cannot be blank");
			lgpass = "";
		}else if(vall.length < 4){
			$("#lpassError").html("password must be atleast 4 characters");
			lgpass = "";
		}else{
			lgpass = vall;
			$("#lpassError").html("");
		}
	});

	$('#lg_submit').click(function(e){
		if(lguname == "" || lgpass == ""){
			e.preventDefault();
			$('#sublError').html('Error in the form');
		}else{
			$('#sublError').html('');
		}
	});


	// add card validation
	$('#cd_name').keyup(function(){
		var vall = $(this).val();
		if(vall == ""){
			$("#cdnmError").html("card name cannot be blank");
			cardnm = "";
		}else{
			$("#cdnmError").html("");
			cardnm = vall
		}
	});

	$('#cd_desc').keyup(function(){
		var vall = $(this).val();
		if(vall == ""){
			$("#cddesError").html("card description cannot be blank");
			cardds = "";
		}else{
			$("#cardds").html("");
			cardds = vall
		}
	});

	$('#add_card_submit').click(function(e){
		if(cardds == "" || cardnm == ""){
			e.preventDefault();
			$('#cdsubError').html('Error in the form');
		}else{
			$('#cdsubError').html('');
		}
	});

	//add list validation
	$('#cat_name').keyup(function(){
		var vall = $(this).val();
		if(vall == ""){
			$("#catNmError").html("list name cannot be blank");
			listnm = "";
		}else{
			$("#catNmError").html("");
			listnm = vall
		}
	});

	$('#subCat').click(function(e){
		if(listnm == "" ){
			e.preventDefault();
			$('#catSubError').html('Error in the form');
		}else{
			$('#catSubError').html('');
		}
	});

	//add task validation
	$('#tk_name').keyup(function(){
		var vall = $(this).val();
		if(vall == ""){
			$("#taskNmError").html("todo item name cannot be blank");
			taskName = "";
		}else{
			$("#taskNmError").html("");
			taskName = vall
		}
	});

	$('#sub_task').click(function(e){
		if(taskName == "" ){
			e.preventDefault();
			$('#subTaskError').html('Error in the form');
		}else{
			$('#subTaskError').html('');
		}
	});
 

});