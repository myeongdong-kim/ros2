from setuptools import setup

package_name = 'cat'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='chan',
    maintainer_email='chan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'helloworld_publisher = cat.node.helloworld_publisher:main',
            'helloworld_subscriber = cat.node.helloworld_subscriber:main',
            'camera_publisher = cat.node.camera_publisher:main',
            'camera_subscriber = cat.node.camera_subscriber:main',
            'laser_scan = cat.node.laser_scan:main' 
        ],
    },
)
