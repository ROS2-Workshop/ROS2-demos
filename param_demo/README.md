```bash
cd ~/ros2_ws
colcon build --packages-select param_demo --symlink-install
source install/setup.bash
ros2 launch param_demo param_demo.launch.py
```
