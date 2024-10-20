import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose, Twist, Point, Quaternion, Vector3

class SimplePuber(Node):
    def __init__(self):
        super().__init__('Simple_puber')
        self.puber = self.create_publisher(Odometry, 'odom_topic', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Odometry puber has been started.')
        self.i = 0.0

    def timer_callback(self):
        # Create Odometry message
        odom_msg = Odometry()

        # Fill in the header information
        odom_msg.header.stamp = self.get_clock().now().to_msg()  # Timestamp
        odom_msg.header.frame_id = "odom"  # Reference frame

        # Fill in the pose (position + orientation)
        odom_msg.pose.pose.position = Point(x=self.i, y=0.0, z=0.0)
        odom_msg.pose.pose.orientation = Quaternion(x=0.0, y=0.0, z=0.0, w=1.0)

        # Fill in the twist (velocity)
        odom_msg.twist.twist.linear = Vector3(x=0.5, y=0.0, z=0.0)  # Linear velocity
        odom_msg.twist.twist.angular = Vector3(x=0.0, y=0.0, z=0.0)  # Angular velocity

        # Publish the message
        self.puber.publish(odom_msg)
        self.get_logger().info(f"Published odometry data x = {self.i}")
        self.i += 1
    
def main(args=None):
    rclpy.init(args=args)

    simplePuber = SimplePuber()

    rclpy.spin(simplePuber)

    simplePuber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()