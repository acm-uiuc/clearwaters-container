clearwaters-container
Container Management for the Clearwaters Cluster

A Brief Description of Docker and Current Goals
Docker is  a software technology providing operating-system-level virtualization also known as containers. A normal virtual machine exists as a separate system, a sandbox, in userspace that has its own operating system (libraries, file system, etc.). What differentiates Docker from other virtual machines is that the Docker software shares the majority of its operating system features with its host computer, except for its own file system. This allows for the sandbox to be both smaller in memory-size and faster as it can use the host’s operating system to do most of the work. For instance, if you “install” some software in a container that already exists on the host’s memory, then Docker will just link the file in the container to the one in the host, taking up none of the container’s memory and making “installation” speed instantaneous. 

For SIGOps, through the magic of hardware, multiple containers have been linked together physically through a head node. The head node connects these containers to the internet and users and vice versa (all jobs will be done through this head node). Docker containers have been built with these hardware pieces but have not yet been linked. It would be equivalent to the concept of each being in their own separate universe and unable to communicate with anywhere else.

Difference between node and container: Each node is an independent computer (separate hardware and everything) and the container is as described above.

Current goal: Able to ping nodes together but cannot access the docker container to ping other containers. Ask Tanshiq what to do. Once we figure that out, start writing Python code that builds network, utilizing ping-ing principles (accessing IP address, etc). 
