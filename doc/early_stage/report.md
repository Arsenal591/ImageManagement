#图片分享网站 前期文档  

##一、概述
我们利用Django框架搭建了一个图片分享网站，支持用户注册、上传与社交，并可以对图片进行各种编辑处理。  

##二、功能简述  
###1. 用户管理  
###2. 图片管理
1. 图片的上传  
	* 单独上传  
	* 批量上传  
2. 图片的处理
	* 灰度图
	* 二值化
	* 高斯模糊
	* 缩放
	* 旋转
	* 剪裁
3. 图片的信息标注
	* 自动标注类别
	* 用户手动添加类别
	* 点赞
4. 图片的展示
	* 按照上传时间
	* 按照上传用户
	* 按照赞数
	* 按照类别
	* 按照相似度（以图搜图）  
###3. 界面设计

##三、架构与实现
###1. 用户
###2. 图片管理
####2.1. 数据组织
#####2.1.1 ImagePost
![ImagePost](http://i.imgur.com/m4pYzym.png)
#####2.1.2 ImageTag
![ImageTag](http://i.imgur.com/MSbwSD8.png)
#####2.1.3 ImageComment
![ImageComment](http://i.imgur.com/9ZjjL9a.png)
####2.2 功能实现  
#####2.2.1 基础功能  
* 灰度图：根据公式g = 0.299R + 0.587G + 0.114B
* 高斯模糊：支持设置模糊度，将模糊度与核的大小、高斯分布的方差关联
* 二值化：采用高斯分布，支持设置最大值、核的尺寸、是否反色，高斯分布的方差固定为1（考虑到用户不需要过于繁琐的设置）
* 剪裁、缩放、旋转：参考大多数网站的做法，这部分内容计划在前端进行处理
#####2.2.2 自动标签分类
采用在 ImageNet 数据集上训练的 [SqueezeNet](https://arxiv.org/abs/1602.07360) 对图片进行类别预测，选取 Top5 作为预测标签。
###3. 界面
###4. 总览

##四、实验分工
* 周玉枭 图片相关内容，如上传、处理、编辑等