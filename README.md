# ping_of_death_DOS
Computer Security project where the goal is to create raw IP (and ICMP) packets to trigger a remote DOS vulnerability 

Specs:

The goal of this project was to remotely trigger a denial of service (DoS) vulnerability in a network stack. To this end, I had to create IP fragments that, when reassembled by the network stack, exceeded the maximum size of an IP packet. This lead to a buffer overflow in the network stack, triggering a crash.
