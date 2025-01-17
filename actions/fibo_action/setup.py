from setuptools import setup

package_name = 'fibo_action'

setup(
    name=package_name,
    version='0.20.3',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Jacob Perron',
    author_email='jacob@openrobotics.org',
    maintainer='Audrow Nash, Michael Jeronimo',
    maintainer_email='audrow@openrobotics.org, michael.jeronimo@openrobotics.org',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Python action tutorials code.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'server = fibo_action.server:main',
            'client = fibo_action.client:main',
        ],
    },
)
