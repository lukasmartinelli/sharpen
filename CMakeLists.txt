cmake_minimum_required(VERSION 2.8.11)
project(sharpen)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -pedantic -std=c++11")
#----------------------------------------------------------------------
add_executable(array_duplicate challenges/array/array_duplicate.cpp)
add_executable(max_consecutive_gap challenges/array/max_consecutive_gap.cpp)

