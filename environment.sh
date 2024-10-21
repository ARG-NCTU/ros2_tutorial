# check REPO_NAME is set
if [ -z "$REPO_NAME" ]; then
    echo "REPO_NAME is not set. Please set REPO_NAME to the name of the repository."
    return
fi

source /opt/ros/humble/setup.bash
source ./ros2_ws/install/setup.bash
export ROS_DOMAIN_ID=0
# export ROS_LOCALHOST_ONLY=1
