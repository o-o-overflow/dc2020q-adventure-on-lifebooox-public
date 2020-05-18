# dc2020q-adventure-on-lifebooox-public


Adventure on LifeBooox is a pwn and reversing challenge where you have to work on a computer inside of Conway's Game of Life simulator. 

In the GoL, we created a dual-cpu gaming system. The first CPU boots the system and loads the game map and copies it to the game.  The second CPU is used for running the game, issuing movement commands, and storing the state of the game.

![Overview of LifeBooox](https://github.com/o-o-overflow/dc2020q-adventure-on-lifebooox-public/raw/master/gol2cpu.png)

Some of the source code in src/lang/ was borrowed and inspired by https://github.com/QuestForTetris.

To better undertand the bootloader and Adventure cpus checkout their source code.

The intended method of interaction with Lifebooox was for the users to upload their input that would manipulate the CPUs in the area marked by read on the upper right hand side of the map. 

![Overview of Solution](https://github.com/o-o-overflow/dc2020q-adventure-on-lifebooox-public/raw/master/solution.png)

The solution is located in /adventure_lifebooox_SOLVED.mc

Enjoy

