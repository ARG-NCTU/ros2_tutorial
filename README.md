# ROS2_DOCKER

### Create package
create a cmake package
```
ros2 pkg create <package_name> --build-type ament_cmake
```
create a python package
```
ros2 pkg create <package_name> --build_type ament_python
```
### Build the workspace
build everything
```
colcon build
```
Only process a subset of packages and their recursive dependencies
```
colcon build --package-up-to 
```
Use symlinks instead of copying files where possible (ex. install directory)
```
colcon build --symlink-install
```
### environment.sh
source this file for env variable setup
```
source environment.sh
```
### package.xml
Important for linking dependency of the package
```
<depend>...</depend>
<exec_depend>...</depend>
```
### setup.py
Important for install files into ros2 file architecture
ex. launch files, source code .py files

### launch file
launch files are written in python. With file extension such as .launch.py