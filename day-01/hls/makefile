IFLAG += -g 
CFLAG += -fPIC -O3
CFLAG += -lm
CFLAG += -std=c++11 -Wno-unused-result

CC := g++

result: *.cpp *.hpp
	$(CC) *.cpp -o result $(CFLAG) $(IFLAG)

build: result
	result

run: result
	./result.exe

all: build run


clean:
	rm -f *.o result