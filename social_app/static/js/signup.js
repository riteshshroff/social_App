$(document).ready(function(){                                                                                                               
    $("#mobile").on("blur change", function(){
        var mobNum = $(this).val();
        var filter = /^\d*(?:\.\d{1,2})?$/;
        if (filter.test(mobNum)) {
            if(mobNum.length==10){                                               
                console.log('Mobile no. is correct'); 
                $('#mobileerror').hide();                                    
            } 
            else {
                $('#mobileerror').text('Enter 10 digit mobile number.');                                            
                return false;
            }
        }
        else {
            $('#mobileerror').text('Not a valid');        
            return false;
        }                                    
    });                                  
    $('#email').on('change',function() {                                                                                   
        var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
        var emailaddressVal = $("#email").val();
        if(emailaddressVal == '') {
            $("#email").text('Please enter email address.');                                            
        }
        else if(!emailReg.test(emailaddressVal)) {
            $("#emailerror").text('Enter a valid email address.');                                            
        }       
        else{
            $('#emailerror').hide();
        }                                 
    });
});