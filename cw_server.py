from cw_libs import clearwaters_docker as cwd
from cw_libs import daemon
import socket
import sys
import json
from thread import *

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

docker_client = cwd.CWDockerClient()

def doCommand(cmd):
	global docker_client
	if cmd == "TEST":
	    print(docker_client.create_container('echo hello world'))

class ClientDaemon(daemon.Daemon):
    def run(self):
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.bind((HOST, PORT))
            except socket.error as msg:
                print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
                sys.exit(1)
            s.listen(10)
            def clientthread(conn):
                while True:
                    data = conn.recv(4096)
                    if not data: 
                        break
		    d = json.loads(data)
		    if not d:
 		        conn.sendall("Not JSON!")
		    cmd = d.get('CMD')
		    doCommand(cmd)
                conn.close()
            while 1:
                conn, addr = s.accept()
                start_new_thread(clientthread ,(conn,))
            s.close()

if __name__ == "__main__":
    daemon = ClientDaemon('/tmp/cwclientd-daemon.pid', stdout='/home/clearwaters/cw-stdout', stderr='/home/clearwaters/cw-stderr')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown Command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "Usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2) 
