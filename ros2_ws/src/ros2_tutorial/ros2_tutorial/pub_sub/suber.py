import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose, Twist, Point, Quaternion, Vector3


class SimpleSuber(Node):
    def __init__(self):
        super().__init__('Simple_suber')
        self.subscription = self.create_subscription(
            Odometry,
            'odom_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        # Extract the position and orientation from the Odometry message
        position = msg.pose.pose.position
        orientation = msg.pose.pose.orientation

        # Extract the linear and angular velocity from the Odometry message
        linear_velocity = msg.twist.twist.linear
        angular_velocity = msg.twist.twist.angular

        # Log the position, orientation, and velocities
        self.get_logger().info(f"Position: x={position.x}, y={position.y}, z={position.z}")
        self.get_logger().info(f"Orientation: x={orientation.x}, y={orientation.y}, z={orientation.z}, w={orientation.w}")
        self.get_logger().info(f"Linear Velocity: x={linear_velocity.x}, y={linear_velocity.y}, z={linear_velocity.z}")
        self.get_logger().info(f"Angular Velocity: x={angular_velocity.x}, y={angular_velocity.y}, z={angular_velocity.z}")


def main(args=None):
    rclpy.init(args=args)
    
    simpleSuber = SimpleSuber()

    rclpy.spin(simpleSuber)

    simpleSuber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()