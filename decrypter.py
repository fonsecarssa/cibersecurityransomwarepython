import os
import pyaes

file_name = 'test.txt.ransomwaretroll'
file = open(file_name, 'rb')
file_data= file.read()
file.close()

key= b'testeransomwares'
aes= pyaes.AESModeOfOperationCTR(key)
decrypy_data = aes.decrypt(file_data)

os.remove(file_name)

new_file = 'teste.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypy_data)
new_file.close()
