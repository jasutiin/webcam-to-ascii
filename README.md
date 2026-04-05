learning how to create python packages that were implemented in C++ under the hood. will be doing this to implement numpy's `.mean()` in CUDA for parallel calculations

steps for compiling C++ source code:
1. search for "x64 Native Tools Command Prompt for VS 20XX"
2. navigate to `webcam-to-ascii/add-numbers`
3. run `cl /LD src/add.cpp /Fe:add.dll`
    - `cl`: use the MSVC compiler to compile C++ source code into an object file
    - `/LD`: produce a `.dll` file instead of an executable
    - `/Fe:add.dll`: specify output file's name to be `add.dll`
4. this should create four files, one of them being the `.dll` file

the reason why we're using MSVC as the compiler instead of GNU's g++ is because for Windows, CUDA uses nvcc, which uses MSVC under the hood. i don't have a Linux computer soooo