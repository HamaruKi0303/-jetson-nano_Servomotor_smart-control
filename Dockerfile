FROM nvcr.io/nvidia/dli/dli-nano-ai:v2.0.1-r32.5.0

RUN apt-get update 
RUN apt-get install i2c-tools
