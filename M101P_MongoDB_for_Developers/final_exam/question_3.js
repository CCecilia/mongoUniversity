var msg = db.messages.findOne({"headers.Message-ID": "<8147308.1075851042335.JavaMail.evans@thyme>"});
msg.headers.To.push("mrpotatohead@mongodb.com");
db.messages.replaceOne({"headers.Message-ID": "<8147308.1075851042335.JavaMail.evans@thyme>"}, msg);
db.messages.findOne({"headers.Message-ID": "<8147308.1075851042335.JavaMail.evans@thyme>"}).pretty();
