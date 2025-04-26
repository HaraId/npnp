CXX := g++
CXXFLAGS := -std=c++20 -Wall -Wextra
TARGET := {{project_name}}

SRCS := main.cpp

all: $(TARGET)

$(TARGET): $(SRCS)
	$(CXX) $(CXXFLAGS) -o $@ $^

clean:
	rm -f $(TARGET)
	