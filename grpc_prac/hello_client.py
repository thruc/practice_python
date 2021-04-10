import grpc
import hello_pb2
import hello_pb2_grpc

def hello_server(stub, name):
    messages = []
    messages.append(hello_pb2.HelloMessage(name=name, msg='Hello'))
    responses = stub.HelloServer(iter(messages))
    for response in responses:
        print('Received message {}'.format(response.reply_msg))

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hello_pb2_grpc.HelloServiceStub(channel)
        print('--Please input your name--')
        while True:
            name = input("What's your name? > ")
            hello_server(stub, name)

if __name__ == '__main__':
    run()