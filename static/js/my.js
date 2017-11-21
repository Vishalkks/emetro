function validatecard(evt)
{  evt.preventDefault();
   card=document.getElementById("cardNumber").value;
   cvv=document.getElementById("cvv").value;
   var msg=document.getElementById("errmsg").innerHTML;
   var t=false;
   edate=document.getElementById("expiration-date").value;
   var visa = new RegExp("^4[0-9]{12}(?:[0-9]{3})?$");
   var visa_master = new RegExp("^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})$");
   var master = new RegExp("^5[1-5][0-9]{14}$");
   var maestro = new RegExp("^(5018|5020|5038|6304|6759|6761|6763)[0-9]{8,15}$");
	
	if(visa.test(card) && card.length==13)
	{  t=true;
		alert("visa card");
	}
   else if(visa_master.test(card) && card.length==16)
   {
    t=true;  
    alert("visa master");
   }
   else if(master.test(card) && card.length==15)
   {t=true;  
    alert("master");
   }
   else if(maestro.test(card) && card.length==16)
   {  t=true;
   alert("visa master");
   }
   else 
   {  msg="invalid card number";
      return false;
   }
   if(t)
   {
    // alert(card[0]);
	var a=card.split("");
	var result=a.map(Number);
	//alert(result);
	 var l=result.length-2;
	 for(var i=l;i>=0;i=i-2)
	 {
		 result[i]=result[i]*2;
	 }
	 
	//alert(result);
	for(var i=0;i<result.length;++i)
	 {
		 if(result[i]>9)
		 {   var val=result[i];
			 var sum=val.toString().split("")
                 .reduce(function(a,b) {
	                  return a+parseInt(b);
                  },0);
			result[i]=sum;
		 }
		 
	 }
	 //alert(result);
	 var sum1=result.reduce(function(a,b) {
	                  return a+parseInt(b);
                  },0);
	 alert(sum1);
	 if(sum1%10==0)
	 {
		 return true;
	 }
	 else
	 {
		 msg="invalid card number";
		 return false;
	 }
   }
 }
 