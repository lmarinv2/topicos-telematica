
import socket

host , port = '0.0.0.0' , 80

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
print('***********************************')
print('Server is running...')
print('Dir IP:',host )
print('Port:', port)
serversocket.bind((host , port))
serversocket.listen(5)

while True:
    connection , address = serversocket.accept()
    request = connection.recv(1024).decode('utf-8')
    print(request)
    string_list = request.split(' ')
    method = string_list[0]
    requesting_file = string_list[1]

    print('Client request',requesting_file)

    myfile = requesting_file.split('?')[0]
    myfile = myfile.lstrip('/')

    if(myfile == ''):
        myfile = 'index.html'

    try:
        file = open(myfile , 'rb')
        response = file.read()
        file.close()

        header = 'HTTP/1.1 200 OK\n'

        if(myfile.endswith('.jpg')):
            mimetype = 'image/jpg'
        elif(myfile.endswith('.css')):
            mimetype = 'text/css'
        elif(myfile.endswith('.pdf')):
            mimetype = 'application/pdf'
        else:
            mimetype = 'text/html'

        header += 'Content-Type: '+str(mimetype)+'\n\n'

    except Exception as e:
        print("-")
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body>Error 404: File not found</body></html>'.encode('utf-8')

    final_response = header.encode('utf-8')
    final_response += response
    connection.send(final_response)
    connection.close()
