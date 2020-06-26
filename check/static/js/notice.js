function test(){
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    var info = $.trim($('#names').val());
    if (info.length == 0) 
    { 
        alert('请输入查询内容'); 
        $('#list').html("");
        return;
    }
    $.ajax({
    url:'/infoajax/', 
    type:'post',  
    datatype: 'json',
    data:{'info':info},
    success:function(data) {
        $('#list').html("");
        
        var str = "";
        if (JSON.stringify(data.content) === '[]') {
            alert('查询结果为空');
            return false // 如果为空,返回false
        }
        for(var i in data.content){
            
            str += '<div class="item">' + '<a class="title" href="/infodetail/?id='+data.content[i].id + '">' + data.content[i].title + '</a>'
            +'<div class="desc">发布者：' + data.content[i].author + '</div>'+'</div>' ;
        }
        document.getElementById("list").innerHTML = str;

    },
    error : function(XMLHttpRequestn) {
        alert("false");
    }
})
}
