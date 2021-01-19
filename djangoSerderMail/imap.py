import imaplib

# Conections
server = imaplib.IMAP4_SSL(host='imap.gmail.com', port=993, keyfile=None, certfile=None, ssl_context=None)
server.login('jjxcero@gmail.com', 'S3b4st14n2017*')