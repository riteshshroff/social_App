$(document).ready(function(){
    CKEDITOR.replace( 'editor1' );
    $('#home_btn').click(function(){
        $('#home_block').hide();
    });
    $('#post_btn').click(function(){
        $('#post_form').toggle();
    });    
});