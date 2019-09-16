$(function () {
    $('#input1').change(function(){
        var input_value = this.value;
        var reg1 = /^1\d{10}$/g;
        var yanzheng = reg1.test(input_value);
        if(yanzheng){
            $('#id_span1').text("");
        }else{
            $('#id_span1').text("*非法输入");
        }
    });
});