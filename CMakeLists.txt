cmake_minimum_required(VERSION 3.29)
project(Leetcode_Solutions)

set(CMAKE_CXX_STANDARD 14)

file(GLOB SOURCE_FILES "leetcode/editor/en/*.cpp")

add_executable(Leetcode_Solutions ${SOURCE_FILES})
