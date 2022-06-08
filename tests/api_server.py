import socket
import asyncio
sock = socket.socket()
sock.bind(('', 0))

import pproxy

server = pproxy.Server('ss://chacha20:123@localhost:10')
# remote = pproxy.Connection('ss://1.2.3.4:5678')
remote = pproxy.DIRECT
args = dict( rserver = [remote],
             verbose = print )

loop = asyncio.get_event_loop()
print(sock.getsockname())
handler = loop.run_until_complete(server.start_server(args, sock))
try:
    loop.run_forever()
except KeyboardInterrupt:
    print('exit!')

handler.close()
loop.run_until_complete(handler.wait_closed())
loop.run_until_complete(loop.shutdown_asyncgens())
loop.close()
