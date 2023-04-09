from setuptools import setup

package_name = 'obstacleavoidance_fsm'

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
    maintainer='magnum',
    maintainer_email='ogunsdavis53@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'finite_state = obstacleavoidance_fsm.obstacle_avoidance:main',
        'fsm= obstacleavoidance_fsm.fsm:main',
        'move=obstacleavoidance_fsm.obstacle:main',
        'move_sub=obstacleavoidance_fsm.move_sub:main',
        'avoidance=obstacleavoidance_fsm.avoidance:main',
        'distance=obstacleavoidance_fsm.obstacle_avoidance:main',
        'transform_object_detctor=obstacleavoidance_fsm.obstacle_detector_using_tf2:main',
        ],
    },  
)
