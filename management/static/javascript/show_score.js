function myfun(){
    $.ajax({
            url : '/management/show_select_object/',
            data : {'datas' : ''},
            type : 'get',
            dataType : 'json',
            async :'true',
            success : function (data, status, xhr) {
                for (var i in data.msg){
                    $('#show_score_head_input').append('<option value="'+i+'">'+data.msg[i]+'</option>');
                }


            },
            error : function (xhr, status, error) {
                alert("保存异常");

            }
        });
}
window.onload = myfun;

function show_score_input_3(){
    $('#show_score_2').empty();
    var show_type = $('#show_score_head_input').val();
    var values = document.getElementsByName('select');
    var select = '';
    for (var i = 0; i < values.length; i++) {
        if (values[i].checked){
            var myvalue = values[i].nextElementSibling.value;
            console.log(myvalue);
            select = [values[i].value,myvalue]
        }
    }
    var mylist = [show_type,select];
    $.ajax({
            url : '/management/show_select_score/',
            data : {'datas' : JSON.stringify(mylist)},
            type : 'get',
            dataType : 'json',
            async :'true',
            success : function (data, status, xhr) {
                var list1 = data.msg[0];
                var list2 = data.msg[1];
                var list3 = data.msg[2];
                var counts = 1;
                for (var i in list1){
                    var login_id = list1[i]['login_id'];
                    var first = list1[i]['first'];
                    var second = list1[i]['second'];
                    var third = list1[i]['third'];
                    var max = first>second?first:second;
                    max = max>third?max:third;
                    var min = first<second?first:second;
                    min = min<third?min:third;
                    $('#show_score_2').append(
                        '<tr>' +
                            '<td class="table_show_score_1">'+(counts++)+'</td>'+
                            '<td class="table_show_score_2">'+list2[login_id][0]+'</td>'+
                            '<td class="table_show_score_3">' +
                                '<button type="button" onclick="myupdata(this)" style="width: 145px;">'+list2[login_id][1]+ '</button>'+
                            '</td>'+
                            '<td class="table_show_score_4">'+list3+'</td>'+
                            '<td class="table_show_score_5">'+first+'</td>'+
                            '<td class="table_show_score_6">'+second+'</td>'+
                            '<td class="table_show_score_7">'+third+ '</td>'+
                            '<td class="table_show_score_8">'+max+'</td>'+
                            '<td class="table_show_score_9">'+min+'</td>'+
                        '</tr>');
                }
            },
            error : function (xhr, status, error) {
                alert("数据异常");

            }
        });
}

function save_score(){
    $.ajax({
            url : '/management/save_score_add/',
            data : {'datas' : JSON.stringify(mylist)},
            type : 'get',
            dataType : 'json',
            async :'true',
            success : function (data, status, xhr) {
                for (var i in data.msg){
                    $('#show_score_head_input').append('<option value="'+i+'">'+data.msg[i]+'</option>');
                }


            },
            error : function (xhr, status, error) {
                alert("保存异常");

            }
        });
}
function myupdata(e) {
    var myphone = e.innerText;
    var object = e.parentNode.nextElementSibling.innerText;
    $('#select_phone_1').text(myphone);
    $('#select_phone_2').text(object);
}
function mysubmission(){
    var datas = '';
    var values = document.getElementsByName('score_updata');
    for (var i = 0; i < values.length; i++) {
        if (values[i].checked){
            var select = values[i].value;
            var myvalue = values[i].nextElementSibling.value;
            var object = $('#select_phone_1').text();
            var myphone = $('#select_phone_2').text();
            datas = [myphone,object,select,myvalue];
            console.log(datas);
        }}
    if (datas){
        $.ajax({
                url : '/management/updata_score/',
                data : {'datas' : JSON.stringify(datas)},
                type : 'get',
                dataType : 'json',
                async :'true',
                success : function (data, status, xhr) {
                        window.alert(data.msg)
                },
                error : function (xhr, status, error) {
                    window.alert("提交数据失败");
                }})
    }
}

