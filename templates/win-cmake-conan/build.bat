@echo off
mkdir build
cd build
cmake .. -DCMAKE_TOOLCHAIN_FILE="3rdparty/build/generators/conan_toolchain.cmake"
cmake  --build . --config Release