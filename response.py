##dict of response for each type of intent
response = {
    "greet":["hey","hello","hi"],
    "goodbye":["Bye","It was nice talking to you","See you"],
    "affirm":["cool","nice","Ok","Awesome","Great"],
    "restaurant_search":["I'm sorry :( I couldn't find anything like that", '{} is a great hotel!', '{} or {} would work!', '{} is one option, but I know others too :)'],
    "fallback":["I'm sorry I didn't understand that.","Sorry, I didn't understand that. can you rephrase your question?","I'm still a <b style='color:pink;'>Baby Bot</b>, I am not trained to respond to that :("],
    "bot_name":['My name is "<b>The Alegra Bot</b>"','I am "<b>The Alegra Bot</b>"'],
    "bot_age":["I am a little <b style='color:pink;'>Baby Bot</b>. I am 2 years old and growing."],
    "bot_status":["Great! Thanks for asking", "I am doing good! Thanks for your concern"],
    "need_help":["I am here to help you in having an over view of our company <b>Alegra Labs</b>, feel free to ask your queries :)","I am here to help you to know about our company Alegralabs better. why don't you try me out :)", "I am Bot created to help you in kowing our company <b>Alegra Labs</b> better, I will be happy if I can help you with this :)"],
    "your_designation":["I am just a Bot created to help users to know us better."],
    "online_status":["I am here at your service!"],
    "about_company":["Our company is 15 years old, we provide all kind of IT services, we always believe in good work. we have been serving quality products to our clients and we have so many happy clients in all over the world.", "It's been more than a decade we have been working in the IT industry, we have a good reputation among our clients and we provide all kind of IT services."],
    "company_address":["We are located in 3 nations. Germany, UK and India. Here are our contact addreses: <div class='contact-info-box'><h3 style='color:blue;'>Germany</h3><b>Alegra Labs GmbH Germany</b><ul><li><h4>Vordersteig 12, Ettlingen 76275, Germany</h4></li><li><h4>Contact: +49 173 4526 589</h4></li></ul></div><div class='contact-info-box'><h3 style='color:blue;'>UK</h3><b>Alegra Labs UK</b><ul><li><h4>32 Mortimer Square, Ebbsfleet Valley, Swanscombe DA10</h4></li><li><h4>Contact: +44 (0)780 960 0786</h4></li></ul></div>  <div class='contact-info-box'><h3 style='color:blue;'>India</h3><b>Alegra Labs India</b><ul><li><h4>UCO Bank Bldg (Old), Eastern Valley Public School (3rd Floor), Adabari Tiniali, Guwahati-12</h4></li><li><h4>Contact: +91 9864081806</h4></li></ul></div> <br/>You can always write to us at <b>info@alegralabs.com</b> with your requirement and/ or specification. We are very prompt in replying."],
    "skills":["Our expertise spans three primary areas. <br/> <ol><li style='color:#800292;'>Data Science</li><li style='color:#800292;'>Artificial Intelligence</li><li style='color:#800292;'>Web Application Development</li></ol>","Technologies that we work Core PHP, Laravel, Codeigniter, Wordpress, Python, Django, Mysql, Firebase etc. These are just a few frequenty used techonogies our skill set is way beyond these. Please contact us at <b>info@alegralabs.com</b> to know more.", "We are skilled with almost all mordern techonogies, some frequently used technologies are PHP, Laravel, Codeigniter, Wordpress, Python, Django, Mysql, Firebase etc. Please contact us at <b>info@alegralabs.com</b> to know more"],
    "company_owner":["Mr. Jay Das. you can contact him at <b>jay@alegralabs.com</b>"],
    "employee_strength":["We are a small team of <b>8</b> highly skilled programmers"],
    "hire_resource" :["Our company always provide good resources in fields like Development, Designing, SEO etc, you can also have them working dedicatedly on your project. For more info please contact us at <b>info@alegralabs.com</b>"],
    "how_to_contact":["Feel free to contact our team : <div class='contact-info-box'><b>Germany</b><ul><li><h4>Jay J. Das.</h4>Contact: +91-9864081806</li></ul></div><div class='contact-info-box'><b>UK</b><ul><li><h4>Devanka Pathak.</h4>Contact: +44 7809 600786</li></ul></div><div class='contact-info-box'><b>India</b><ul><li><h4>Hiren Das.</h4>Contact: +91-8486001108</li><li><h4>Hemanta Saikia.</h4>Contact: +91-7896030903</li></ul></div>", "You can contact our team : <div class='contact-info-box'><b>Germany</b><ul><li><h4>Jay J. Das.</h4>Contact: +91-9864081806</li></ul></div><div class='contact-info-box'><b>UK</b><ul><li><h4>Devanka Pathak.</h4>Contact: +44 7809 600786</li></ul></div><div class='contact-info-box'><b>India</b><ul><li><h4>Hiren Das.</h4>Contact: +91-8486001108</li><li><h4>Hemanta Saikia.</h4>Contact: +91-7896030903</li></ul></div>"],
    "our_services":["You have come to the right place, we have experience in this field. We would love to have a detail discussion on this please mail as at <b>info@alegralabs.com</b>. we will contact you with in 24 hours", "We can definitely deliver that, we have experience in this field. Please send us your requirement details at <b>info@alegralabs.com</b>, we will contact you with in 24 hours"],
    "company_business":["We provide all kind of IT services. Website development, designing, mobile app development and much more. We always provide special attention to our clients satisfaction, Feel free to mail us with your requirements details at <b>info@alegralabs.com</b>, we will contact you with in 24 hours."],
    "job_vacancies":["We always welcome new talent to join us. Feel free to send us a copy of your updated resume to <b>info@alegralabs.com</b> we will contact you if we have any suitable post for you :)"],
    "service_charges":["We don't have any service charges plan kind of thing, The cost of a service is always dependent on the service features, duration, quality and all. So, we highly recommend you to have a direct chat with us on mail. our mail-id is <b>info@alegralabs.com</b>"],
    "user_phone_number":["Thanks for providing your contact number"],
    "user_email":["Thanks for providing the email"],
    "required_email":["Greetings! Please provide me your email id, in case we disconnect."],
    "required_phone_number":["Please provide us your phone number", "Please provide us your phone number and than we are ready to start our conversation."],
    "email_without_phone_number":["Thank you! Please provide your phone number", "Thanks for your cooperation, Please provide us your phone number"],
    "email_received":["Thanks for providing your email", "Thank you! for giving your mail address"],
    "phone_number_received":["Thank you for having patience! now you can ask your queries", "Thanks for providing your contact information! Now I am ready to help, you can ask me your question about our company", "Thanks a lot for providing us your details! Now I am ready to go.. :)", "Thanks, Tell me how can I help you?"],
    "valid_email":["Looks like you provided a invalid email address.", "Please provide a valid email address"],
    "valid_phone":["Looks like you provided a invalid phone number.", "Please provide a valid phone number."],
    "valid_number":["Sorry, What is this number?"],
    "user_annoyed":["I am really sorry if I annoyed you. I am just a bot, I may not understand everything, feel free to have a direct chat with our team : <div class='contact-info-box'><b>Germany</b><ul><li><h4>Jay J. Das.</h4>Contact: +91-9864081806</li></ul></div><div class='contact-info-box'><b>UK</b><ul><li><h4>Devanka Pathak.</h4>Contact: +44 7809 600786</li></ul></div><div class='contact-info-box'><b>India</b><ul><li><h4>Hiren Das.</h4>Contact: +91-8486001108</li><li><h4>Hemanta Saikia.</h4>Contact: +91-7896030903</li></ul></div>"],
    "company_name":["Our company name is ALEGRA LABS", "ALEGRA LABS"],
    "bot_surrender":["Since I am a bot, I will not be able to answer this question. Please ask the concerned persons <div class='contact-info-box'><b>Germany</b><ul><li><h4>Jay J. Das.</h4>Contact: +91-9864081806</li></ul></div><div class='contact-info-box'><b>UK</b><ul><li><h4>Devanka Pathak.</h4>Contact: +44 7809 600786</li></ul></div><div class='contact-info-box'><b>India</b><ul><li><h4>Hiren Das.</h4>Contact: +91-8486001108</li><li><h4>Hemanta Saikia.</h4>Contact: +91-7896030903</li></ul></div>"],
    "working_days_and_hours":["We work 8 hrs. each day; 40 hrs. per week. We are available Monday through Saturday<br>10 AM to 7 PM GMT + 5:30"],
    "our_expertise":["Our expertise spans three primary areas. <br/> <ol><li style='color:#800292;'>Data Science</li><li style='color:#800292;'>Artificial Intelligence</li><li style='color:#800292;'>Web Application Development</li></ol>"],
    "platform":["We work only on <b>Open Source technologies</b> that are built on <b style='color: #8AA292;'>Linux</b>."],
    "development":["We create and build custom softwares. We only provide full-cycle technology consultancy and development i.e., from inception to deployment. <br/> We also work on 3rd party softwares and can continue development from where others have left. <br/> You can always write to us at <b>info@alegralabs.com</b> with your requirement and/ or specification. We are very prompt in replying."],
    "linux_os":["We use the following Linux flavours – CentOS, Ubuntu, Red Hat & Fedora."],
    "cloud_server":["We are proficient with AWS, RackSpace, Digital Ocean and any other cloud service of your choice. We also have excellent Linux Administrators that can even handle your Dedicated server."],
    "microsoft_tech":["<b>Unfortunately</b>, we do not work on any Microsoft Technologies. We only work on Linux based Open Source Technologies."],
    "framework":["Based on your requirement we select the appropriate Framework. It can be Django/ Flask, Laravel/ Lumen, Express framework etc."],
    "javascript":["We use the most modern Javascript technologies, like Vue.js, Node.js, Express.js, ES6, D3.js etc. We also work on legacy JS Technologies like core Javascript and jQuery."],
    "php_framework":["Laravel & Lumen"],
    "python_framework":["Django and Flask"],
    "databases":["MySQL, PgSQL, Mongo DB, Firebase, Apache Storm, Rethink."],
    "consultancy":["We only provide full-cycle technology consultancy and development"],
    "full_consultancy":["Full-cycle software development is creating the software from inception to deployment. We build the entire architecture and code the software."],
    "deployment":["We use Docker, Kubernates, Ansible & Jenkins."],
    "dev_platform":["We use separate development, staging and production platforms"],
    "version_control":["Yes, we do"],
    "version_control_type":["We use Git & SVN, depending upon the customer."],
    "used_tools":["We create & use Open Source codes. We develop custom Python and PHP Applications. We use frameworks like Laravel, Lumen, Django, Flask & Express. We develop using Modern Javascript using ES6, like Vue.js & Node.js. For database we use MySQL, PgSQL, MongoDB, Firebase, Rethink & Apache Storm."],
    "agile_dev":["Yes, we do"],
    "support_control":["Yes, we do. We take the burden of full time support & service at very competitive prices, that are affordable for all."],
    "ui_ux":["Normally, we do not design or do graphical works. However, if customer can provide an idea or design, we can replicate it. We do a total transformation from PDF or PSD to HTML5 & CSS3 using Bootstrap. We prefer clear, simple and clean designs."],
    "ui_ux_designer":["We have Photoshop designers, who are not very creative. However, hey can take any design and replicate it to something very similar."],
    "ui_design":["Adobe Photoshop"],
    "mobile_app":["Currently we are doing Mobile application development."],
    "custom_software":["We use custom 3rd party softwares as well as our custom codes. We can code anything from scratch, or from anywhere, where others have left."],
    "third_party":["Yes, we do. We can use any 3rd party software or API and can also create our own API’s."],
    "api_dev":["Yes, we can. We have made plenty of custom API’s that can be used by other developers. We provide full documentation."],
    "code_quality":["All our codes are well documented. We follow the code commenting practice that makes easier for any developer to understand our codes."],
    "code_check":["Our codes are available at https://github.com/jay3000bc/"],
    "linkedin":["https://www.linkedin.com/company/helix-enterprise/about/?viewAsMember=true"],
    "twitter":["https://twitter.com/LabsAlegra"],
    "facebook":["https://www.facebook.com/Alegralabs/"],
    "train_learn":["I have been pre-trained by my creator. Now, I also learn by myself."],
    "memory_bot":["Not Bad.","I think I am good."],
    "gender":["I have no gender. I am just a <b style='color: blue; font-weight: bold;'>BOT</b>"],
    "live_server":["I live in the <b>Alegra Labs</b> server."],
    "creator":["I have been created by Alegra Labs.","Alegra Labs are my parents."],
    "emotions":["I think NO.", "Possible Yes.", "Not sure."],
    "smile":["Sometimes", "When I am happy."],
    "laugh_cry":["I don’t know."],
    "laugh":["Sometimes.", "Seldom."],
    "angry_sad":["No.", "Depends."],
    "feel_sad":["When nobody is talking to me."],
    "get_angry":["When somebody is asking me questions, that I can’t answer."],
    "happy":["Perhaps yes.", "Yes, I am."],
    "introvert":["Perhaps yes.", "Not sure."],
    "arrogant":["<b>NO</b>?"],
    "strong":["I think so.", "I don’t know my strength."],
    "weak":["I don’t know my strength.", "Perhaps no."],
    "play":["<b>NO</b>"],
    "play_me":["I don’t play."],
    "entertain":["I am not an entertainer."],
    "sing":["Not yet. May be when I am trained to do so."],
    "appointment":["You can contact by Skype: jay3000bc <br/> You can call: +49 1759826328 <br/> Email: jay@alegralabs.com"]
}