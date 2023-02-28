

## Creating a launch package


```bash
cd ~/ros2_ws/src
ros2 pkg create bringup --build-type ament_python
cd ~/bringup
mkdir launch && cd launch
touch workshop_launch.py
```

## Edit workshop_launch.py file
```python
import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='demo_nodes_cpp',
            executable='talker',
            name='talker'),
  ])
```

## Editing the setup.py file 
```python
import os
from glob import glob
from setuptools import setup

package_name = 'py_launch_example'

setup(
    # Other parameters ...
    data_files=[
        # ... Other data files
        # Include all launch files.
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*'))
    ]
)
```


```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
ros2 launch bringup workshop_launch.py
```
