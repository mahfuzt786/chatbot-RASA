$(document).ready(function () {
var data=[];

function addBr(text){
    return text.replace(/\n/g, "<br />");

}
var Message;
Message = function (arg) {
    this.text = arg.text, this.message_side = arg.message_side, this.avatar = arg.avatar;
    this.draw = function (_this) {
        return function () {
            var $message;
            $message = $($('.message_template').clone().html());
            $message.addClass(_this.message_side).find('.text').html(addBr(_this.text));
            $message.addClass(_this.message_side).find('.avatar').html(_this.avatar);
            $('.messages').append($message);
            return setTimeout(function () {
                return $message.addClass('appeared');
            }, 0);
        };
    }(this);
    return this;
};

function showBotMessage(msg){
        message = new Message({
             text: msg,
             message_side: 'left',
             avatar: '<img src="static/images/bot.png" alt="Bot">'
        });
        message.draw();
        $messages.animate({ scrollTop: $messages.prop('scrollHeight') }, 300);
}
function showUserMessage(msg){
        $messages = $('.messages');
        message = new Message({
            text: msg,
            message_side: 'right',
            avatar: '<img src="static/images/user.png" alt="User">'
        });
        message.draw();
        $messages.animate({ scrollTop: $messages.prop('scrollHeight') }, 300);
        $('#msg_input').val('');
}
function IsEmail(email) {
	var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
	return regex.test(email);
}

function IsPhone(phone) {
	var regexPhone = /^\+?([0-9]{2})\)?[-. ]?([0-9]{5})[-. ]?([0-9]{5})$/;
	return regexPhone.test(phone);
}
function sayToBot(text){
    document.getElementById("msg_input").placeholder = "Type your messages here...";
    var usr_email = $("#usr_email").val();
    var usr_phone_number = $("#usr_phone_number").val();

    if(usr_email == '')
    {
        if(!IsEmail(text)) {
            showBotMessage('Greetings! Please provide me your email id, in case we disconnect.');
        }
        else {
            $("#usr_email").val(text);
            showBotMessage('Please provide us your phone number and than we are ready to start our conversation.');
        }
    }
    else if(usr_email !== '' && usr_phone_number == '')
    {
        if(!IsPhone(text))
            showBotMessage('Not a valid Phone Number. <br> Please provide like +XX XXXX XXXX format.');
        else {
            $("#usr_phone_number").val(text);
            showBotMessage('Thank you for having patience! Now you can ask your queries');
        }
    }
    else if(usr_phone_number !== '' && $.isNumeric(text))
    {
        showBotMessage('Sorry, What is this number?');
    }
    else {
        text = text.replace(/\?/g,'');
        console.log(text);
        $.post("/chat",
            {
                //csrfmiddlewaretoken:csrf,
                text:text,
                usr_email:usr_email,
                usr_phone_number:usr_phone_number,
            },
            function(jsondata, status) {
                if(jsondata["status"]=="success"){
                    console.log(jsondata);
                    response=jsondata["response"];
                    $("#usr_email").val(jsondata["user_email"]);
                    $("#usr_phone_number").val(jsondata["phone_number"]);
                    if(response){
                        showBotMessage(response);
                    }
                }
            });
    }
}

getMessageText = function () {
            var $message_input;
            $message_input = $('.message_input');
            return $message_input.val();
        };

$("#say").keypress(function(e) {
    if(e.which == 13) {
        $("#saybtn").click();
    }
});

$('.send_message').click(function (e) {
        msg = getMessageText();
        if(msg){
        showUserMessage(msg);
        sayToBot(msg);
    $('.message_input').val('');}
});

$('.message_input').keyup(function (e) {
    if (e.which === 13) {
        msg = getMessageText();
        if(msg){
        showUserMessage(msg);
        sayToBot(msg);
    $('.message_input').val('') ;}
    }
});

var alertBox = '<div class="alert alert-success" id="bsalert" style="display: none;">'+
                '<span class="text"></span>'+
            '</div>';

$('body').append(alertBox);

$('body').on('click','.send_mail',function (e) {
    var usr_email = $("#usr_email").val();
    var usr_phone_number = $("#usr_phone_number").val();

    $('body .send_mail .text').text('Mailing... ');
    $.post("/mail",
    {
        usr_email:usr_email,
        usr_phone_number:usr_phone_number,
    },
    function(jsondata, status) {
        $('body .send_mail .text').text('Mail Chat Transcript');
        console.log(jsondata);
        $('body #bsalert').show();
        if(jsondata["status"] == "success") {
            response=jsondata["response"];
            $('body #bsalert span').text(response);
        }
        else {
            $('body #bsalert span').text(jsondata["response"]);
        }
        setTimeout(function(){ $('body #bsalert').hide(); }, 2500);
    });
});
});
