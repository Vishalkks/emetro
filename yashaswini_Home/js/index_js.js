$(document).ready(function(e){
	$("#mainmenu1 a.nav-container").bind("dblclick",function(){
	    var a= $(this).text();
       // alert(a);
		window.location = "http://localhost/bootstrap-shop/bootstrap-shop/products.php?group="+a;
	}
	);
	$("#mainmenu2 a.nav-container").bind("dblclick",function(){
	    var a= $(this).text();
        //alert(a);
		window.location = "http://localhost/bootstrap-shop/bootstrap-shop/products.php?group="+a;
	}
	);
	
	$("#mainmenu1 a.nav-sub-container").bind("dblclick",function(){
	    var a= $(this).html();
		var b= $("#mainmenu1 a.nav-container").text();
        alert(b);
		window.location = "http://localhost/bootstrap-shop/bootstrap-shop/products.php?group="+b+"&category="+a;
	}
	);
	
	$("#mainmenu2 a.nav-sub-container").bind("dblclick",function(){
	    var a= $(this).html();
		var b=$("#mainmenu2 a.nav-container").text();
        //alert(a);
		window.location = "http://localhost/bootstrap-shop/bootstrap-shop/products.php?group="+b+"&category="+a;
	}
	);
	
	$("#item1 a.i").bind("dblclick",function(){
	    var c= $(this).text();
		var b=$("#mainmenu1 a.nav-container").text();
		var a=$("#submenu11").text();
        //alert(a);
		window.location = "http://localhost/bootstrap-shop/bootstrap-shop/products.php?group="+b+"&category="+a+"&subcategory="+c;
	}
	);
	
	$("#item2 a.i").bind("dblclick",function(){
	    var c= $(this).text();
		var b=$("#mainmenu1 a.nav-container").text();
		var a=$("#submenu12").text();
        alert(a);
		window.location = "http://localhost/bootstrap-shop/bootstrap-shop/products.php?group="+b+"&category="+a+"&subcategory="+c;
	}
	);
	$("#item3 a.i").bind("dblclick",function(){
	    var c= $(this).text();
		var b=$("#mainmenu1 a.nav-container").text();
		var a=$("#submenu13").text();
        //alert(a);
	    window.location = "http://localhost/bootstrap-shop/bootstrap-shop/products.php?group="+b+"&category="+a+"&subcategory="+c;
	}
	);
	$("#item4 a.i").bind("dblclick",function(){
	    var c= $(this).text();
		var b=$("#mainmenu1 a.nav-container").text();
		var a=$("#submenu14").text();
        //alert(a);
		window.location = "http://localhost/bootstrap-shop/bootstrap-shop/products.php?group="+b+"&category="+a+"&subcategory="+c;
	}
	);
	
	$("#item5 a.i").bind("dblclick",function(){
	    var c= $(this).text();
		var b=$("#mainmenu2 a.nav-container").text();
		var a=$("#submenu21").text();
        //alert(a);
		window.location = "http://localhost/bootstrap-shop/bootstrap-shop/products.php?group="+b+"&category="+a+"&subcategory="+c;
	}
	);
	
	$("#item6 a.i").bind("dblclick",function(){
	    var c= $(this).text();
		var b=$("#mainmenu2 a.nav-container").text();
		var a=$("#submenu22").text();
        //alert(a);
		window.location = "http://localhost/bootstrap-shop/bootstrap-shop/products.php?group="+b+"&category="+a+"&subcategory="+c;
	}
	);
	
	$("#item7 a.i").bind("dblclick",function(){
	    var c= $(this).text();
		var b=$("#mainmenu2 a.nav-container").text();
		var a=$("#submenu23").text();
        //alert(a);
		window.location = "http://localhost/bootstrap-shop/bootstrap-shop/products.php?group="+b+"&category="+a+"&subcategory="+c;
	}
	);
	
});

function login_check()
{   var e=document.getElementById("inputEmail").value;
    var p=document.getElementById("inputPassword").value;
    xhr=new XMLHttpRequest();
	xhr.onreadystatechange=show;
	xhr.open("GET","http://localhost/bootstrap-shop/bootstrap-shop/login.php?"+"uemail="+e+"&passwd="+p,true);
	xhr.send();

}
function show()
{
   if(xhr.readyState==4 && xhr.status==200)
   {
       var a=xhr.responseText;
	   //console.log(typeof(a));
	   var r=JSON.parse(xhr.responseText);
	   $(document).ready(function(){
	        $("#login").hide();
			
	   });
	   document.getElementById("user").innerHTML=r.name;
	   document.getElementById("cart_count").innerHTML=r.cart;
	   
	}

}


		