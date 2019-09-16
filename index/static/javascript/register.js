value1 =false;
value2 =false;
value3 =false;
value4 =false;
value5 =false;
value6 =false;


//验证函数
function button_yanzhengma() {
    function yanzhengma(n) {
        var zhi1 = ["1","2","3","4","5","6","7","8","9",
                    "q","w","e","r","t","y","u","i","p","a","s",
                    "d","f","g","h","j","k","l","z","x","c","v","b",
                    "n","m","Q","W","E","R","T","Y","U","I","P",
                    "A","S","D","F","G","H","J","K","L","Z","X","C",
                    "V","B","N","M"];
        var zhi = "";
        for (var ci=1;ci <= n;ci++){
            zhi += zhi1[parseInt(zhi1.length*Math.random())];
        }
        return zhi
    }
    var shu = parseInt(Math.random()*5+4);
    var zhi = yanzhengma(shu);
    $('#register_span_5').text(zhi);
}
//设定密码默认值为NAN,设定验证验证码
$(function () {
    input_value_passw1 = NaN;
    button_yanzhengma();
});

$(function () {
    //注册按钮激活
    var func = function () {
        if(value1&&value2&&value3&&value4&&value5&&value6){
            $("#register_button_2").show();
        }else{
            $("#register_button_2").hide();
        }};
    //验证注册手机号规则
    $('#register_input_1').change(function(){
        var input_value1 = this.value;
        var reg1 = /^1\d{10}$/g;
        var yanzheng = reg1.test(input_value1);
        if(yanzheng){
            $('#register_span_1').text("√");
            //验证通过
            value1 =true;
            func()
        }else{
            $('#register_span_1').text("*非法输入");
            value1 =false;
            func()
        }
    });
    //验证密码规则
    $('#register_input_2').change(function(){
        input_value_passw1 = this.value;
        var reg1 = /^[a-zA-Z][\w]{7,19}$/g;
        var yanzheng = reg1.test(input_value_passw1);
        if(yanzheng){
            $('#register_span_2').text("√");
             value2 =true;
             func()
        }else{
            $('#register_span_2').text("*以首字母开始,必须包含大小写字母,数字,'_'四种中的任意两种,组合的8-20位密码");
            value2 =false;
            func()
        }
    });
    //验证两次密码匹配
    $('#register_input_3').change(function(){
        var input_value_passw2 = this.value;
        if(input_value_passw1==input_value_passw2){
            $('#register_span_3').text("√");
            //验证通过
            value3 =true;
            func()
        }else{
            $('#register_span_3').text("*密码不一致");
            value3 =false;
            func()
        }
    });
    //身份证验证
    $('#register_input_4').change(function(){
        var input_value1 = this.value;
        var reg1 = /^[0-9]{17}[0-9X]$/g;
        var yanzheng = reg1.test(input_value1);
        if(yanzheng){
            $('#register_span_4').text("√");
            //验证通过
            value4 =true;
            func()
        }else{
            $('#register_span_4').text("*请正确输入身份证号");
            value4 =false;
            func()
        }
    });
    //刷新验证码
    $('#register_button_1').click(function(e){
        button_yanzhengma();
        e.preventDefault();
    });
    //验证码设置
    $('#register_input_5').change(function(){
        var input_value2 = this.value;
        var input_span5_value = $('#register_span_5').text();
        if(input_value2==input_span5_value){
            $('#register_span_6').text("验证码通过");
            $('#register_span_6').css('background-color','green');
            //验证通过
            value5 = true;
            func()
        }else{
            $('#register_span_6').text("验证码错误");
            $('#register_span_6').css('background-color','red');
            value5 = false;
            func()
        }
    });
    //姓名匹配规则
    $('#register_input_7').change(function(){
        var input_value3 = this.value;
        var reg2 = /^[\u4e00-\u9fa5]+$/g;
        var yanzheng2 = reg2.test(input_value3);
        if(yanzheng2){
            $('#register_span_7').text("√");
            //验证通过
            value6 = true;
            func()
        }else{
            $('#register_span_7').text("*请输入汉字");
            value6 = false;
            func()
        }});
});

// $(function () {
//     $('#register_input_8_2').append('<option value=0 >--空--</option>');
// });
// function move() {
//     var s1=document.getElementById("register_input_8_1");
//     var s2=document.getElementById("register_input_8_2"); <!-- 获取一级和二级的属性-->
//     var add;
//     var long = {{ udepartment2|safe }};
//     if(s1.value=="5") {
//         add=long['5']; <!--比对value值，实现对应二级text值的动态生成-->
//     }else if(
//         s1.value=="6") {
//         add=long['6'];<!--比对value值，实现对应二级text值的动态生成-->
//     }else if(s1.value=="7") {
//         add=long['7']; <!--比对value值，实现对应二级text值的动态生成-->
//     }else {
//         add=new Array("--空--",); <!--若没有就为空，当然不可能出现的-->
//         $('#register_input_8_2').append('<option value=0 def>--空--</option>');
//     }
//     s2.length=0;
//     for(var i=0; i<add.length;i++) {
//         $('#register_input_8_2').append('<option value='+(i+1)+'>'+(add[i].split()[0])+'</option>');
//     }}