from setuptools import find_packages, setup

package_name = 'my_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/my_pkg']),
        ('share/my_pkg', ['package.xml']),
    # 下面这行改成，找到launch文件夹下面所有py文件
        ('share/my_pkg/launch', [
            'launch/demo.launch.py',
        ]),
    ],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kkka',
    maintainer_email='kkka@xample.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'hello=my_pkg.hello_node:main',
            'class_node=my_pkg.class_node:main'
        ],
    },
)
