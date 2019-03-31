
Compile the code using the provided makefile:

    make

To clear the directory (and remove .txt files):
   
    make clean

Deadlines: https://blog.codeship.com/using-grpc-in-python/

???: https://grpc.io/grpc/python/grpc.html#grpc.ChannelConnectivity.SHUTDOWN

The directory structure of your VM should place the `tsnsImproved` folder underneath `/home/csce438`. There is a script that directly calls `/home/csce438/tsnsImproved`. You can change this if you want in the `startupRouter` and `startup` scripts.
To run, you will need at least 2 machines (one for the router and at least one master):
On router run:
`./startupRouter -i <localIP> -p <routersPort> -f <firstMachinesIP:Port> -s <secondMachinesIP:Port> -t <thirdMachinesIP:Port>`

On server machine run:
`./startup -i <localIP> -p <machinesPort> -r <routersIP> -t <routersPort>`
