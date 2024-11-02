const nodemailer = require('nodemailer');
const formidable = require('formidable');
const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: 'ntrikarwar@gmail.com',
      pass: 'Naymith@123'
    }
  });
  
  const mailOptions = {
    from: 'ntrikarwar@gmail.com',
    to: 'pritishinde3249@gmail.com',
    subject: 'Beware of Chipkalis',
    text: 'Hey Chipkali'
  };
  
  transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
      return console.log(error);
    }
    console.log('Email sent: ' + info.response);
  });
  