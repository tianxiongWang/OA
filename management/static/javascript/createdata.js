//全局变量,共计生成数据库排序
var counts = 1;

//单选题增加表单样式
function radiozengjia() {
    var table1_1 = $('#table1_1').text();
    var table1_2 = $('#table1_2').val();
    $('#table1_2').val('');
    var table1_3 = $('#table1_3').val();
    $('#table1_3').val('');
    var table1_4 = $('#table1_4').val();
    $('#table1_4').val('');
    var table1_5 = $('#table1_5').val();
    $('#table1_5').val('');
    var table1_6 = $('#table1_6').val();
    $('#table1_6').val('');
    var table1_7 = $('#table1_7').val();
    var $create1 =$('<tr >' +
                        '<td>'+counts+'</td>'+
                        '<td>'+table1_1+'</td>'+
                        '<td>'+table1_2+'</td>'+
                        '<td>'+table1_3+'</td>'+
                        '<td>'+table1_4+'</td>'+
                        '<td>'+table1_5+'</td>'+
                        '<td>'+table1_6+'</td>'+
                        '<td>'+table1_7+'</td>'+
                        '<td>' +
                            '<div class="style2">' +
                                '<button onclick="shanchu(this)" type="button">删除</button>'+
                            '</div>'+
                        '</td>'+
                    '</tr>');
    $('#tbody1').prepend($create1);
    counts++;
}

//删除样式
function shanchu(ss){
    ss = ss.parentNode.parentNode.parentNode;
    ss.parentNode.removeChild(ss)
}

//单,多选题表单保存数据库
function submission(object_type){
    var values = document.getElementById('tbody1').children;
    var datas = [];
    for(var n = 0; n < values.length; n++){
        var value = document.getElementById('tbody1').children[n].children;
        var object_class = object_type;
        var object = value[2].innerText;
        var select_A = value[3].innerText;
        var select_B = value[4].innerText;
        var select_C = value[5].innerText;
        var select_D = value[6].innerText;
        var answer = value[7].innerText;
        datas[n] = [object_class, object,select_A,select_B,select_C,select_D,answer];
    }

    $.ajax({
            url : '/management/saveobject/',
            data : {'datas' : JSON.stringify(datas)},
            type : 'get',
            dataType : 'json',
            async :'false',
            success : function (data, status, xhr) {
                alert("成功保存"+data.msg+'组数据');
                location.reload()
            },
            error : function (xhr, status, error) {
                alert("保存异常");
                location.reload()
            }
        });
}

//删除数据库信息
function mydelete(ss){
    ss = ss.parentNode.parentNode.parentNode;
    var mydata = ss.children[0].getAttribute('id');
    $.ajax({
            url : '/management/delete_data/',
            data : {'mydata' : JSON.stringify(mydata)},
            type : 'get',
            dataType : 'json',
            async :'false',
            success : function (data, status, xhr) {
                alert(data.msg);
                location.reload()
            },
            error : function (xhr, status, error) {
                alert("删除异常");
                location.reload()
            },
    });
}

//多选题增加表单样式
function selectzengjia() {
    var table1_1 = $('#table1_1').text();
    var table1_2 = $('#table1_2').val();
    $('#table1_2').val('');
    var table1_3 = $('#table1_3').val();
    $('#table1_3').val('');
    var table1_4 = $('#table1_4').val();
    $('#table1_4').val('');
    var table1_5 = $('#table1_5').val();
    $('#table1_5').val('');
    var table1_6 = $('#table1_6').val();
    $('#table1_6').val('');
    var obj = document.getElementsByName('select_object');
    var table1_7 = '';
     for (var i = 0; i < obj.length; i++) {
         if (obj[i].checked) table1_7 += obj[i].value;
    }
    var $create1 =$('<tr >' +
                        '<td>'+counts+'</td>'+
                        '<td>'+table1_1+'</td>'+
                        '<td>'+table1_2+'</td>'+
                        '<td>'+table1_3+'</td>'+
                        '<td>'+table1_4+'</td>'+
                        '<td>'+table1_5+'</td>'+
                        '<td>'+table1_6+'</td>'+
                        '<td>'+table1_7+'</td>'+
                        '<td>' +
                            '<div class="style2">' +
                                '<button onclick="shanchu(this)" type="button">删除</button>'+
                            '</div>'+
                        '</td>'+
                    '</tr>');
    $('#tbody1').prepend($create1);
    counts++;
}

//判断题增加表单样式
function judgezengjia() {
    var table1_1 = $('#table1_1').text();
    var table1_2 = $('#table1_2').val();
    $('#table1_2').val('');
    var obj = document.getElementsByName('judge_object');
    var table1_3 = '';
    for (var i = 0; i < obj.length; i++) {
        if (obj[i].checked) table1_3 += obj[i].value;
    }
    var $create1 =$('<tr >' +
                        '<td>'+counts+'</td>'+
                        '<td>'+table1_1+'</td>'+
                        '<td>'+table1_2+'</td>'+
                        '<td>'+table1_3+'</td>'+
                        '<td>' +
                            '<div class="style2">' +
                                '<button onclick="shanchu(this)" type="button">删除</button>'+
                            '</div>'+
                        '</td>'+
                    '</tr>');
    $('#tbody1').prepend($create1);
    counts++;

}

//简单题增加表单样式
function short_answerzengjia() {
    var table1_1 = $('#table1_1').text();
    var table1_2 = $('#table1_2').val();
    $('#table1_2').val('');
    var table1_3 = $('#table1_3').val();
    $('#table1_3').val('');
    var $create1 =$('<tr >' +
                        '<td>'+counts+'</td>'+
                        '<td>'+table1_1+'</td>'+
                        '<td>'+table1_2+'</td>'+
                        '<td>'+table1_3+'</td>'+
                        '<td>' +
                            '<div class="style2">' +
                                '<button onclick="shanchu(this)" type="button">删除</button>'+
                            '</div>'+
                        '</td>'+
                    '</tr>');
    $('#tbody1').prepend($create1);
    counts++;

}

//判断题表单保存数据库
function submission1(object_type){
    var values = document.getElementById('tbody1').children;
    var datas = [];
    for(var n = 0; n < values.length; n++){
        var value = document.getElementById('tbody1').children[n].children;
        var object_class = object_type;
        var object = value[2].innerText;
        var answer = value[3].innerText;
        //匹配数据库存储填充空值
        var select_A = '';
        var select_B = '';
        var select_C = '';
        var select_D = '';
        if (answer == '正确'){
            answer = 'A';
        }else{
            answer = 'B';
        }

        datas[n] = [object_class, object,select_A,select_B,select_C,select_D,answer];
    }

    $.ajax({
            url : '/management/saveobject/',
            data : {'datas' : JSON.stringify(datas)},
            type : 'get',
            dataType : 'json',
            async :'false',
            success : function (data, status, xhr) {
                alert("成功保存"+data.msg+'组数据');
                location.reload()
            },
            error : function (xhr, status, error) {
                alert("保存异常");
                location.reload()
            }
        });
}

function submission2(object_type){
    var values = document.getElementById('tbody1').children;
    var datas = [];
    for(var n = 0; n < values.length; n++){
        var value = document.getElementById('tbody1').children[n].children;
        var object_class = object_type;
        var object = value[2].innerText;
        var answer = value[3].innerText;
        //匹配数据库存储填充空值
        var select_A = '';
        var select_B = '';
        var select_C = '';
        var select_D = '';
        datas[n] = [object_class, object,select_A,select_B,select_C,select_D,answer];
    }

    $.ajax({
            url : '/management/saveobject/',
            data : {'datas' : JSON.stringify(datas)},
            type : 'get',
            dataType : 'json',
            async :'false',
            success : function (data, status, xhr) {
                alert("成功保存"+data.msg+'组数据');
                location.reload()
            },
            error : function (xhr, status, error) {
                alert("保存异常");
                location.reload()
            }
        });
}