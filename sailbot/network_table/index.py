import zmq
import protobuf
from generated import Reply_pb2
from generated import SubscribeReply_pb2
from generated import Request_pb2
from generated import SubscribeRequest_pb2

sock = zmq.socket('pair')

def subscribe():
    context = zmq.Context()
    init_sock = context.socket(zmq.REQ)
    init_sock.connect('ipc:///tmp/sailbot/NetworkTable')

    init_socket.send("connect")

    filepath = init_socket.recv()

    socket = context.socket(zmq.PAIR)
    socket.connect(filepath)

    while True:
        replyProto = Reply_pb2.Reply()
        encoded_reply = init_sock.recv()
        replyProto.decode(encoded_reply)
        if replyProto["type"] == Reply_pb2.Reply.Type.SUBSCRIBE:
            with open('out.bin', 'wb') as f:
                f.write(replyProto.SerializeToString())
            # update databse with new data

def read_data():
    replyProto = Reply_pb2.Reply()
    replyProto.ParseFromString(f.read())
    return replyProto
