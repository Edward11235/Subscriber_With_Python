#include"Packet.h"
#include<iostream>

int main(int argc, char **argv){
    PacketSerializer channel("127.0.0.1", 8000);
    int status = channel.start();
    std::cout << "status is " << status << std::endl;
    const char* message = "Hello, world!";
    channel.write(1, message, strlen(message));
}