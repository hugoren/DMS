#!/usr/bin/env python
#conding:utf-8

import paramiko,threading,os


class ssh_client(threading.Thread):

    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir,'command_list')
    command_list = open(file_path,'r')
    commands = []
    threads = []
    for each_command in command_list:
        commands.append(each_command)

    def __init__(self,ip,username,password):
        threading.Thread.__init__(self)
        self.ip = ip
        self.username = username
        self.password = password
        # self.commands = commands


    def ssh_exce_cmd(self):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.ip,22,self.username,self.password,timeout=5)
            # stdin,stdout,stderr = ssh.exec_command(self.commands)


            for command in ssh_client.commands:
                print  command
                stdin,stdout,stderr = ssh.exec_command(command)
                # return_code = ssh.subprocess.Popen('echo "90909" >>/Users/hugo/test.txt', shell=True)
            stdin.write("Y")
            # print (stdout.read()).split('\n')
            ssh_list = []
            ssh_list.extend((stdout.read()).split('\n'))
            print stdout.read()
            print ssh_list[0]
            print ssh_list
            ssh.close()
            return ssh_list


        except IOError as e :
            print e.message

        except Exception as e:
            print '%s ip ssh err'%e.message


if __name__ == '__main__':
    # ip = sys.argv[1]
    # username = sys.argv[2]
    # password = sys.argv[3]
    ip = "119.29.101.41"
    username = "admin"
    password = "y298FTgS8Y"
    command_list = open('./command_list','r')
    commands = []
    # threads = []
    for each_command in command_list:
        commands.append(each_command)
        temp_thread = ssh_client(ip,username,password)
        # threads.append(temp_thread.ssh_exce_cmd())
    threading.Thread(temp_thread.ssh_exce_cmd()).start()

