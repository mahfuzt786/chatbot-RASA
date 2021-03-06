$(document).ready(function () {

    // Create new link Element 
    var link1 = document.createElement('link');
    var link2 = document.createElement('link');  
    var link3 = document.createElement('link');  
  
    // set the attributes for link element 
    link1.rel = 'stylesheet';
    link1.type = 'text/css';

    link2.rel = 'stylesheet';
    link2.type = 'text/css';

    link3.rel = 'stylesheet';
    link3.type = 'text/css';
  
    link1.href = 'https://www.alegralabs.com/syed/ai/chatbot/bot-server/static/css/chat_interface.css';
    link2.href = 'https://www.alegralabs.com/syed/ai/chatbot/bot-server/static/css/temporary.css';
    link3.href = 'https://www.alegralabs.com/syed/ai/chatbot/bot-server/static/css/api-bot.css';

    // Get HTML head element to append link element to it  
    document.getElementsByTagName('HEAD')[0].appendChild(link1);
    document.getElementsByTagName('HEAD')[0].appendChild(link2);
    document.getElementsByTagName('HEAD')[0].appendChild(link3);

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
                avatar: '<img src="https://www.alegralabs.com/syed/ai/chatbot/bot-server/static/images/bot.png" alt="Bot">'
            });
            message.draw();
            $messages.animate({ scrollTop: $messages.prop('scrollHeight') }, 300);
    }
    function showUserMessage(msg){
            $messages = $('.messages');
            message = new Message({
                text: msg,
                message_side: 'right',
                avatar: '<img src="https://www.alegralabs.com/syed/ai/chatbot/bot-server/static/images/user.png" alt="User">'
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
            var protocols = location.protocol;
            console.log(protocols);
            console.log(text);
            var urlApi = 'https://alegralabs.com:8896/';
            if(protocols == 'http:')
            {
                urlApi = 'http://alegralabs.com:8895/';
            }
            if(protocols == 'https:')
            {
                urlApi = 'https://alegralabs.com:8896/';
            }
            $.ajax({
                type: "GET",
                url: urlApi,
                data: { text:text,
                        usr_email:usr_email,
                        usr_phone_number:usr_phone_number
                },
                //dataType: 'json',
                // xhrFields: {
                //    withCredentials: true
                // },
                crossDomain: true,
                //contentType: 'application/json;',
                success: function(jsondata, status) {
                    if(jsondata["status"]=="success"){
                        console.log(jsondata);
                        response=jsondata["response"];
                        $("#usr_email").val(jsondata["user_email"]);
                        $("#usr_phone_number").val(jsondata["phone_number"]);
                        if(response){
                            showBotMessage(response);
                        }
                    }
                },
                error: function(error) {
                    console.log(error);
                    showBotMessage("My application server may be down, can't help you at the moment!");
                }
            });

            // $.post("http://localhost:8895/",
            //     {
            //         //csrfmiddlewaretoken:csrf,
            //         text:text,
            //         usr_email:usr_email,
            //         usr_phone_number:usr_phone_number,
            //     },
            //     function(jsondata, status) {
            //         if(jsondata["status"]=="success"){
            //             console.log(jsondata);
            //             response=jsondata["response"];
            //             $("#usr_email").val(jsondata["user_email"]);
            //             $("#usr_phone_number").val(jsondata["phone_number"]);
            //             if(response){
            //                 showBotMessage(response);
            //             }
            //         }
            //     });
        }
    }

    getMessageText = function () {
            var $message_input;
            $message_input = $('.message_input');
            return $message_input.val();
        };

    $('body').on('keypress','#say',function(e) {
        if(e.which == 13) {
            $("#saybtn").click();
        }
    });

    $('body').on('click','.chatBotMain .send_message',function (e) {
            msg = getMessageText();
            if(msg){
                showUserMessage(msg);
                sayToBot(msg);
            $('.chatBotMain .message_input').val('');
            }
    });

    $('body').on('keyup',' .message_input',function (e) {
        if (e.which === 13) {
            msg = getMessageText();
            if(msg){
                showUserMessage(msg);
                sayToBot(msg);
                $('.chatBotMain .message_input').val('');
            }
        }
    });

    $('body').on('click','.chatBotMain #botClose',function (e) {
        $('body #alegraBot #chat_window').hide();
        $('body #alegraBot #botClose').hide();
        $('body #alegraBot #botOpen').show();
        $('body #alegraBot').attr('style','height:50px;');
    });

    $('body').on('click','.chatBotMain #botOpen',function (e) {
        $('body #alegraBot #chat_window').show();
        $('body #alegraBot #botClose').show();
        $('body #alegraBot #botOpen').hide();
        $('body #alegraBot').attr('style','height:475px;');
    });

    /** ADD HTML of CHATBOT **/
    var htmlBot = '<div class="chatBotMain" id="alegraBot">'+
                    '<div class="row">'+
                        '<div class="min_window">'+
                                '<span class="botName">'+
                                    '<img src="https://www.alegralabs.com/syed/ai/chatbot/bot-server/static/images/logo-black.png" height="30px"/>'+
                                '</span>'+
                                '<span class="botClose" id="botClose">X</span>'+
                                '<span class="botOpen" id="botOpen" style="display: none;">+</span>'+
                        '</div>'+
                        '<div class="chat_window" id="chat_window">'+
                            '<ul class="messages"></ul>'+
                            '<div class="bottom_wrapper clearfix">'+
                                '<div class="message_input_wrapper">'+
                                    '<input id="msg_input" class="message_input" placeholder="Say Hi to begin chat..." />'+
                                    '<input type="hidden" id="usr_email" name="usr_email"/>'+
                                    '<input type="hidden" id="usr_phone_number" name="usr_phone_number"/>'+
                                '</div>'+
                                '<div class="send_message">'+
                                    '<div class="text">Send</div>'+
                                '</div>'+
                            '</div>'+
                        '</div>'+
                        '<div class="message_template">'+
                            '<li class="message">'+
                                '<div class="avatar"></div>'+
                                '<div class="text_wrapper">'+
                                    '<div class="text"></div>'+
                                '</div>'+
                            '</li>'+
                        '</div>'+
                    '</div>'+
                '</div>';

    $('body').append(htmlBot);

    var alegraBot = $('body #alegraBot');

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
