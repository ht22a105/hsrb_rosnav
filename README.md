# hsrb_ros [![Build Status](https://travis-ci.com/tork-a/hsrb_ros.svg?token=Eg7EHKJ8kwE5VZs6TwDp)](https://travis-ci.com/tork-a/hsrb_ros)

This repository contains navigation/mapping packages for Toyota
HSR2015(hsrb).

## Packages

- hsrb_mapping
- hsrb_rosnav_config

## LICENSE

This software is released under the BSD 3-Clause Clear License, see LICENSE.txt.

### オープンキャンパス用 ROS2 Hubmle Navigation2

## 前提条件
ros2 humble navigaton2をインストールしている必要があります

## 使用方法
HSRでナビゲーション以外の必要な機能を起動してください
ナビゲーションを行うPCで以下のコマンドを実行してください

ros2 launch hsrb_rosnav_config navigation_launch.py use_sim_time:=true map_subscribe_transient_local:=true map:=/home/YOUR_DIRECTORY/hsrb_rosnav/maps/tmc_prc2020/map.yaml params_file:=/home/YOUR_DIRECTORY/hsrb_rosnav/hsrb_rosnav_config/config/nav2_params.yaml

正常に起動できたらおそらく
Creating bond timer... 
のログが最後に表示されます

## 各パラメーターの説明
hsrb_rosnav/hsrb_rosnav_config/config/nav2_params.yaml
# xy_goal_tolerance, yaw_goal_tolerance:
ゴールの座標と向きの誤差の許容範囲
小さいほど正確な座標にゴールできますが、小さすぎるとゴール付近をウロウロしてナビゲーションが終了しません
今のところ実機では、0.2ずつだと終了せず、0.25だと終了します

# initial_pose: 
ロボットの初期位置の座標

## マップの説明
使用方法に記入しているコマンドを使用する際は、
hsrb_rosnav/maps/tmc_prc2020/
にマップファイルを入れてください

マップの作成方法は「研究室のノートPCでプログラム開発」と同じですが、保存できない場合は
ros2 run nav2_map_server map_saver_cli -f map
で保存してください

