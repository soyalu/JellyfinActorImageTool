# JellyfinActorImageTool

## 功能说明
修复TMM下载演员头像在Jellyfin中不显示问题

## 使用方法
1. 将 video_dir 和 jellyfin_actor_dir 替换成实际的视频目录和 Jellyfin 演员头像目录
video_dir = "/volume1/video/Movie"
jellyfin_actor_dir = "/volume1/docker/jellyfin/config/metadata/People"

2. 执行程序
```python
python jellyfin_actor_image_tool.py
```

这个脚本的功能是遍历指定的视频目录，找到所有包含演员信息的视频文件，然后遍历这些视频文件中的演员信息，并检查是否存在对应的演员头像文件。如果找到对应的演员头像文件，则将演员头像文件复制到 Jellyfin 演员头像目录中，并更新 Jellyfin 演员信息。