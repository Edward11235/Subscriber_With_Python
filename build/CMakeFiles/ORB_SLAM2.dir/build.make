# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.26

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/bin/cmake

# The command to remove a file.
RM = /usr/local/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/nerf-bridge/Desktop/Packet_python

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/nerf-bridge/Desktop/Packet_python/build

# Include any dependencies generated for this target.
include CMakeFiles/ORB_SLAM2.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/ORB_SLAM2.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/ORB_SLAM2.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/ORB_SLAM2.dir/flags.make

CMakeFiles/ORB_SLAM2.dir/src/Packet.cc.o: CMakeFiles/ORB_SLAM2.dir/flags.make
CMakeFiles/ORB_SLAM2.dir/src/Packet.cc.o: /home/nerf-bridge/Desktop/Packet_python/src/Packet.cc
CMakeFiles/ORB_SLAM2.dir/src/Packet.cc.o: CMakeFiles/ORB_SLAM2.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/nerf-bridge/Desktop/Packet_python/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/ORB_SLAM2.dir/src/Packet.cc.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/ORB_SLAM2.dir/src/Packet.cc.o -MF CMakeFiles/ORB_SLAM2.dir/src/Packet.cc.o.d -o CMakeFiles/ORB_SLAM2.dir/src/Packet.cc.o -c /home/nerf-bridge/Desktop/Packet_python/src/Packet.cc

CMakeFiles/ORB_SLAM2.dir/src/Packet.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/ORB_SLAM2.dir/src/Packet.cc.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/nerf-bridge/Desktop/Packet_python/src/Packet.cc > CMakeFiles/ORB_SLAM2.dir/src/Packet.cc.i

CMakeFiles/ORB_SLAM2.dir/src/Packet.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/ORB_SLAM2.dir/src/Packet.cc.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/nerf-bridge/Desktop/Packet_python/src/Packet.cc -o CMakeFiles/ORB_SLAM2.dir/src/Packet.cc.s

# Object files for target ORB_SLAM2
ORB_SLAM2_OBJECTS = \
"CMakeFiles/ORB_SLAM2.dir/src/Packet.cc.o"

# External object files for target ORB_SLAM2
ORB_SLAM2_EXTERNAL_OBJECTS =

libORB_SLAM2.so: CMakeFiles/ORB_SLAM2.dir/src/Packet.cc.o
libORB_SLAM2.so: CMakeFiles/ORB_SLAM2.dir/build.make
libORB_SLAM2.so: CMakeFiles/ORB_SLAM2.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/nerf-bridge/Desktop/Packet_python/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library libORB_SLAM2.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/ORB_SLAM2.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/ORB_SLAM2.dir/build: libORB_SLAM2.so
.PHONY : CMakeFiles/ORB_SLAM2.dir/build

CMakeFiles/ORB_SLAM2.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/ORB_SLAM2.dir/cmake_clean.cmake
.PHONY : CMakeFiles/ORB_SLAM2.dir/clean

CMakeFiles/ORB_SLAM2.dir/depend:
	cd /home/nerf-bridge/Desktop/Packet_python/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/nerf-bridge/Desktop/Packet_python /home/nerf-bridge/Desktop/Packet_python /home/nerf-bridge/Desktop/Packet_python/build /home/nerf-bridge/Desktop/Packet_python/build /home/nerf-bridge/Desktop/Packet_python/build/CMakeFiles/ORB_SLAM2.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/ORB_SLAM2.dir/depend

