# initial_pose_publisher.py
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped
import tf_transformations


class InitialPosePublisher(Node):
    def __init__(self):
        super().__init__('initial_pose_publisher')

        # Yaw, Pitch, Roll の設定（必要に応じて変更）
        yaw = -1.5
        pitch = 0.0
        roll = 0.0

        # クォータニオンへの変換
        qx, qy, qz, qw = tf_transformations.quaternion_from_euler(roll, pitch, yaw)

        # 初期位置メッセージの設定
        initial_pose = PoseWithCovarianceStamped()
        initial_pose.header.frame_id = 'map'
        initial_pose.pose.pose.position.x = -1.0
        initial_pose.pose.pose.position.y = 2.0
        initial_pose.pose.pose.position.z = 0.0
        initial_pose.pose.pose.orientation.x = qx
        initial_pose.pose.pose.orientation.y = qy
        initial_pose.pose.pose.orientation.z = qz
        initial_pose.pose.pose.orientation.w = qw

        # パブリッシャの設定
        self.publisher_ = self.create_publisher(PoseWithCovarianceStamped, '/initialpose', 10)
        
        # 一度だけパブリッシュ
        self.timer = self.create_timer(1.0, lambda: self.publish_initial_pose(initial_pose))

    def publish_initial_pose(self, initial_pose):
        self.publisher_.publish(initial_pose)
        self.get_logger().info('Initial pose published.')
        self.timer.cancel()


def main(args=None):
    rclpy.init(args=args)
    node = InitialPosePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
