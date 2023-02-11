
# EasyVideoPlayer

使用Unity开发的用于处理载具采样视频的GUI程序  
主要包含显示视频、渲染3D点云、视频关键帧的Annotation三部分功能  
此程序仅为功能演示Demo，故没有实现输入输出API，请利用文件系统进行测试  

实现细节见脚本内注释


## 目录结构

├── Assets                      // 资源目录  
│   ├── Editor  
│   ├── JL_Pro_Data               
│   │   └── Resources           
│   ├── Output                  // 输出结果  
│   ├── PointCloud              
│   │   ├── Materials             
│   │   ├── Scripts             // 3D点云部分脚本   
│   │   └── Shaders           
│   ├── Resources               // GUI资源  
│   ├── Scenes                  // 采样视频部分脚本  
│   │   ├── Measure             // Annotation部分脚本   
│   │   └── Title               // 其他GUI功能脚本        
│   └── StreamingAssets  
├── Build_Assets                // build目录   
│   ├── JL_Pro_Data          
│   │   ├── Managed             
│   │   ├── Resources           // 程序输入(API)   
│   │   │   ├── input           // 采样视频  
│   │   │   ├── integrated.off  // 3D点云数据  
│   │   │   └── Measurement.py   
│   │   └── StreamingAssets     // 运行temp        
│   └── MonoBleedingEdge          
├── Library   
├── Logs                        // 测试日志   
├── Packages  
├── ProjectSettings  
└── UserSettings    

## 环境参数

`Screen resolution：1920*1440`  
`System：Win10 + Python3`  


## 使用流程

1.进入build目录    
2.将按照规范命名的采样视频、深度数据和3D点云数据放置于Input目录  

![pic1](https://github.com/WddBlessU/EasyVideoPlayer/blob/main/Image/01.png)    

![pic2](https://github.com/WddBlessU/EasyVideoPlayer/blob/main/Image/02.png)    
 
3.执行根目录的exe文件  

```bash
  JL_Pro.exe
```
4.加载对应的视频文件，找到需要处理的关键帧后点击Intercept进入Annotation界面  

![pic3](https://github.com/WddBlessU/EasyVideoPlayer/blob/main/Image/gif_01.gif)   

5.点击Annotation按钮后按住右键拖动可以绘制Bounding Box，之后在下方键入label内容  

![pic4](https://github.com/WddBlessU/EasyVideoPlayer/blob/main/Image/gif_02.gif)   

6.点击Measurement按钮后右键点击两次可以绘制Crack Distance线，上方可以切换结果为公制或英制  

![pic5](https://github.com/WddBlessU/EasyVideoPlayer/blob/main/Image/gif_03.gif)   

7.点击Load按钮，可以加载3D点云数据(与加载视频文件相互独立)，点击Camera可以切换到点云相机  

![pic6](https://github.com/WddBlessU/EasyVideoPlayer/blob/main/Image/gif_04.gif)   



## 待处理事项

1.可能需要添加ffmepg来将输入视频或图片帧统一？  
2.可能需要添加MeshLab来将输入点云数据统一？  
3.明确Web接入方式后需要实现规范的API  
4.GUI视觉元素需要改善  
5.可能需要整合GPR Migration？  


## 参考blog

 - [Unity快速入门](https://blog.csdn.net/zhousanxi123/article/details/121233746)
 - [Unity动态资源加载](https://kuroha.vip/unity/unity_load_assets.html)
 - [Unity布局模式](https://www.cnblogs.com/rainmj/p/5437395.html)
 - [使用VideoPalyer播放本地视频](https://www.cnblogs.com/nanyang0310/p/9188066.html)
 - [解析OBJ模型并将其加载到场景中](https://blog.csdn.net/qinyuanpei/article/details/49991607)
 - [3D模型展示旋转缩放](https://blog.csdn.net/u013509878/article/details/125294558)
 - [使用Mesh实现实时点云](https://blog.csdn.net/zhudaokuan/article/details/119609315)

