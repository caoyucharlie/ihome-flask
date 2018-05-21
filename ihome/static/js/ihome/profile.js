function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$("#form-avatar").submit(function() {
    alert('1')

    $.ajax({
        url: '/user/profile/',
        type: 'PUT',
        dataType: 'json',
        data: {'avatar': avatar},
        success: function (data) {
            if (data.code == '200') {
                location.href = '/user/profile/';
            }
        },

        error: function (data) {
            alert(data)
        }
    })
}