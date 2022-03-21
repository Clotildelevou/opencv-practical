# ==========================================
#            Various definitions
# ==========================================

cmake_minimum_required(VERSION 3.8)
project(argos VERSION 1.0.0 LANGUAGES CXX)
set (CXX_STANDARD 17)
  
SET("OpenCV_DIR" "/usr/share/OpenCV")
find_package( OpenCV REQUIRED )

MESSAGE(STATUS "Include dirs ${OpenCV_INCLUDE_DIRS}")
MESSAGE(STATUS "LINK LIBRARIES ${OpenCV_LIBS}")

include_directories( ${OpenCV_INCLUDE_DIRS} )

# ==========================================
#           Final executable
# ==========================================

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR})
add_executable(argos src/cpp/main.cpp)
target_link_libraries(argos ${OpenCV_LIBS}) # you can add other librairies path if necessary
