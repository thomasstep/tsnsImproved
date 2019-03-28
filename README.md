
Compile the code using the provided makefile:

    make

To clear the directory (and remove .txt files):
   
    make clean

To run a server:

    ./startup -r <routerIP> -t <routerPort> -i <thisMachinesIP> -p <thisMachinesPort>

To run the router:

    ./startupRouter -i <thisMachinesIP> -p <thisMachinesPort> -f <serverIP:Port> -s <serverIP:Port> -t <serverIP:Port>

Deadlines: https://blog.codeship.com/using-grpc-in-python/

???: https://grpc.io/grpc/python/grpc.html#grpc.ChannelConnectivity.SHUTDOWN


