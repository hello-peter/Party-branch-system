function ajaxs(CSRF, URL) {
    var name = $.trim($('#name').val());
    var num = $.trim($('#num').val());
    var message = $.trim($('#message').val());
    if (name.length == 0 || num.length == 0) 
    { 
        alert('手机号或联系方式还没有填呢！'); 
        return;
    }
    $.ajaxSetup({
        data: {
            csrfmiddlewaretoken: CSRF
        }
    });
    $.ajax({
        type: 'post',
        url: URL,
        data: {
            'name': name,
            'num' : num,
            'message' : message
        },
        dataType: 'json',
        success: function(data) {
            alert("感谢您的留言！我们会做得更好！");
        },
        error: function(XMLHttpRequest) {
            var _code = XMLHttpRequest.status;
            if (_code == 404) {
                alert("404 not found")
            } else if (_code == 500) {
                alert("服务器错误，留言失败");
            } else {
                alert("未知错误...");
            }
        }
    })
}


