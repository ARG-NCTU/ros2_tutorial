from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'ros2_tutorial'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share', package_name, 'launch/robots'),
            glob(os.path.join('launch', '*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'puber = ros2_tutorial.pub_sub.puber:main',
            'suber = ros2_tutorial.pub_sub.suber:main',
            'service_server = ros2_tutorial.server_client.service_server:main',
            'service_client = ros2_tutorial.server_client.service_client:main',
            'Fibonacci_action_server = ros2_tutorial.action_server_client.action_server:main',
            'Fibonacci_action_client = ros2_tutorial.action_server_client.action_client:main',
        ],
    },
)
