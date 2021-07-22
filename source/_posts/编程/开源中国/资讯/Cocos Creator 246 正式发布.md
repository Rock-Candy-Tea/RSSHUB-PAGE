
---
title: 'Cocos Creator 2.4.6 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-603d560e0233a2c80548defee6264064a52.JPEG'
author: 开源中国
comments: false
date: Thu, 22 Jul 2021 07:00:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-603d560e0233a2c80548defee6264064a52.JPEG'
---

<div>   
<div class="content">
                                                                                            <p>Cocos Creator 2.4.6 现已发布，此次更新修复了一些已知问题，并且优化了性能，以为开发者带来更好的体验。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-603d560e0233a2c80548defee6264064a52.JPEG" referrerpolicy="no-referrer"></p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>新功能 
  <ul> 
   <li>优化了编辑器资源加载速度。在第一次导入资源后，编辑器再次打开的所需时间仅为上一版本的不到 50%，大大优化了启动速度，提高了开发效率</li> 
   <li>优化了编辑器搭建时的卡顿问题。此次更新将引擎编译过程移到了 worker，从而不会阻塞主进程的执行，以便开发者可以在构建的同时继续开发工作</li> 
   <li>优化了 iOS 平台下序列帧动画的性能，在老款 iPhone 6s Plus 机型上性能最高可提升 3 倍</li> 
   <li>预览工具栏新增场景列表，无需切换到对应场景即可快速选择预览场景，提高工作效率</li> 
  </ul> </li> 
 <li>编辑器 bug 修复 
  <ul> 
   <li>修复了 Zip 文件每次构建后 Hash 值不一致的问题</li> 
   <li>修复了拖拽有子类的节点到父类的属性无效的问题</li> 
   <li>修复了点击属性面板上的属性选项无法定位到层级面板上的节点的问题</li> 
   <li>修复了轻节点移动时小 Gizmos 方块偏移到节点外的问题</li> 
   <li>修复资源管理器重命名回车后未进入选中状态的问题</li> 
   <li>修复 3D 粒子纹理动画模块中修改 numTilesX 和 numTilesY 没有立即生效的问题</li> 
   <li>修复 3D 粒子 Rotation 模块无法设置 separateAxes，修改后的 XY 旋转无效的问题</li> 
   <li>修复了在 3D 粒度模块中使用曲线时修改不立即生效的问题</li> 
   <li>新增 VideoClip 类型，视频资源导入后自动识别为 VideoClip 格式</li> 
   <li>修复压缩纹理噪点问题，感谢小胖大成</li> 
   <li>修复内置 Unlit 材质的 depthWrite 值不正确的问题</li> 
   <li>修复富文本组件导致打开场景数据改变的问题</li> 
  </ul> </li> 
 <li>引擎 bug 修复 
  <ul> 
   <li>修复由于顺序统一导致材质哈希值计算错误的问题</li> 
   <li>修复 sp.Skeleton.clearTrack 不重置初始姿势的问题</li> 
   <li>修复 cc.Color.fromHex 计算错误的问题</li> 
   <li>添加 Node.setSelfGroupIndex 接口，用于设置自分组</li> 
   <li>修复 Mark 组件使用向导检查后延迟加载错误的问题</li> 
   <li>修复事件回调中触发其他事件导致事件丢失的问题</li> 
   <li>修复多次打开软键盘后无法上推游戏内容的问题</li> 
   <li>修复触摸节点，然后隐藏节点，释放触摸点后所有触摸事件无效的问题</li> 
   <li>新增 Animation.hasAnimationState API，判断是否存在 AnimationState</li> 
  </ul> </li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cocos.com%2Fcocos-creator-2-4-6-%25e6%259b%25b4%25e6%2596%25b0%25e8%25af%25b4%25e6%2598%258e%239473" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            