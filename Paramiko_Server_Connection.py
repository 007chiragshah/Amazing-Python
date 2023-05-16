import paramiko

client =paramiko.SSHClient()   #for SSH Login

client.connect(hostname='hostname_',username='mokgadddi',password='mypaddssword')
#Raises AuthenticationException, socket error , BadHostKeyException ,SSHException


#If you are using private key to connect then use below also
pvt_key = paramiko.RSAKey.from_private_key_file("path/of/pvt_key/key_name", password='pvt_key_pass')

client.set_missing_host_key_policy((paramiko.AutoAddPolicy()))
client.connect(hostname=GCPhost, username=GCPusername, password=GCPpassword, pkey=pvt_key)
_stdin, _stdout, _stderr = client.exec_command("df -Th")
#_stdin = for standard input
#_stdout = for standard output
#_stderr = for standard Error
#client.exec_command("Write commands here")  = to execute the command on server
print(_stdout.read().decode())   #printing output in decoded form, we have multiple methods for _stdout
client.close()  #To close the conenction


#Paramiko FILE TRANSFERS
#The method paramiko.SFTPClient handles the File transfers, which we bring from calling the open_sftp()
#function on an object of Paramiko.SSHClient.

#Script to transfer From Remote Machine, here we Download a File
ftp_client=ssh_client.open_sftp()
ftp_client.get('remotefileth','localfilepath')
ftp_client.close()

#Script to upload From Remote Machine, here we upload a File
ftp_client=ssh.open_sftp()
ftp_client.put('localfilepath',remotefilepath')
ftp_client.close()