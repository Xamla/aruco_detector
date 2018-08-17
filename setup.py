from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    name='aruco_detector',
    version='0.0.0',
    description='a',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
        ],
    keywords='funniest joke comedy flying circus',
    author='',
    author_email='todo@todo.todo',
    package_dir={'': 'src'},
    url='https://github.com/Xamla/pythonClientLib_XamlaMotion',
    license='TODO',
    install_requires=[
        'numpy >= 1.11.0',
        'pyquaternion >= 0.9.2',
        'asyncio >= 3.4.3',
        'rospkg >= 1.1.4',
        'catkin_pkg >= 0.4.5',
        'rospy >= 1.12.13',
    ],
)

setup(**setup_args)