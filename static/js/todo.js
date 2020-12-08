$(function(){
    send_response = function(prop){
        let val = $('#userinput').val()
        $('#userinput').parent('.form').replaceWith(`<span class="form">${val}</span>`)
        $.post("message",{key:prop, message:val})
        .done(function(response){
            $('#chat main').append(response);
        })
    }
})