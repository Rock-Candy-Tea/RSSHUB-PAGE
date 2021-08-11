
---
title: 'Cocos Creator 3.2.1 发布，跨平台 2D、3D 游戏创作工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-aa58f477f756f803fb7c3ee90e6819dad17.png'
author: 开源中国
comments: false
date: Wed, 11 Aug 2021 07:23:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-aa58f477f756f803fb7c3ee90e6819dad17.png'
---

<div>   
<div class="content">
                                                                                            <p>Cocos Creator 3.2.1 正式发布。其开发团队在发布公告<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cocos.com%2Fcreator" target="_blank">写道</a>：“v3.2.1 是我们将<a href="https://www.oschina.net/news/151693/cocos-creator-3-1-2-released" target="_blank"> v3.1.2 </a>合并到 v3.2.1 而来，继续在大版本分支上给大家带来更稳定的体验，v3.2 用户和 v3.1.x 用户都可以无痛升级。”</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-aa58f477f756f803fb7c3ee90e6819dad17.png" referrerpolicy="no-referrer"></p> 
<p>以下是重要更新说明。</p> 
<p><strong>优化</strong></p> 
<ul> 
 <li>Web & 小游戏 2D 渲染性能优化</li> 
 <li>优化小游戏启动性能</li> 
 <li>优化动画组件运行时性能</li> 
 <li>优化 PCF 阴影虚化效果，对低精度 ShadowMap 更加友好</li> 
 <li>优化 bullet 物理引擎性能</li> 
 <li>增加自动资源扫描开关，大型项目可以手动刷新资源管理器，提升编辑器体验</li> 
 <li>创建项目时默认不开启 TS 严格模式（建议手动开启）</li> 
 <li>解决 Mask 带来的内存泄露</li> 
 <li>解决 MeshRenderer 设置材质导致的内存泄露</li> 
 <li>强化 FBX 模型导入的容错</li> 
 <li>兼容废弃的 AudioClip 播放接口</li> 
</ul> 
<p><strong>重要修复</strong></p> 
<ul> 
 <li>修复部分 iPhone 设备的字节平台上，Shadow map 阴影渲染不出来的问题</li> 
 <li>修复 Empty 模板创建项目的问题</li> 
 <li>修复材质编辑器中多 PASS 切换问题和部分属性显示丢失</li> 
 <li>修复 JointTextureLayout 面板无法滚动</li> 
 <li>修复 SplashScreen 设置窗口无法关闭问题</li> 
 <li>修复预制体根节点上的脚本在原生环境中丢失的问题</li> 
 <li>修复重复加载 Morph 模型导致的渲染错误</li> 
 <li>修复 TTF 字体丢失时的崩溃</li> 
 <li>动画编辑器修复 
  <ul> 
   <li>修复动画编辑器节点关键帧无法直接删除</li> 
   <li>修复动画编辑器框选后，按下 Ctrl 添加关键帧后复制粘贴、缩放、排列关键帧功能异常</li> 
   <li>修复动画编辑器属性列表超出不出现滚动条、sample 修改后，当前时间显示未实时更新</li> 
  </ul> </li> 
 <li>环境与光影 
  <ul> 
   <li>修复开启 IBL 之后的材质报错</li> 
   <li>修复天空盒第一次设置无法显示</li> 
   <li>修复开启 ShadowMap 阴影后 GPU 预烘焙骨骼动画失效</li> 
  </ul> </li> 
 <li>粒子模块修复 
  <ul> 
   <li>修复粒子材质在节点未启用的情况下无法显示的问题</li> 
   <li>修复粒子 start speed 效果问题和旋转时的重力效果问题</li> 
  </ul> </li> 
 <li>构建模块修复 
  <ul> 
   <li>修复构建插件重启后报错 (来自论坛反馈：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fforum.cocos.org%2Ft%2Ftopic%2F113448" target="_blank">构建扩展包刷新报错</a> )</li> 
   <li>修复自动图集配置修改后构建仍使用缓存 (来自论坛反馈：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fforum.cocos.org%2Ft%2Ftopic%2F114657" target="_blank">CC3.1.1自动图集，打包后会保留原图</a>)</li> 
   <li>修复安卓 abi 无默认值与原生 native 文件夹的 git ignore 配置问题 (来自论坛反馈：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fforum.cocos.org%2Ft%2Ftopic%2F114412" target="_blank">原生native目录需要进行git版本控制吗</a> )</li> 
  </ul> </li> 
 <li>Tiledmap 修复 
  <ul> 
   <li>修复使用多图集下的 Tilesets 显示错误</li> 
   <li>修复 TiledLayer getTiledTileAt 函数报错问题</li> 
  </ul> </li> 
 <li>2D 骨骼动画 
  <ul> 
   <li>修复编辑器更新 color，Spine 和 DB 透明度不生效问题</li> 
   <li>修复 web 和 native 上 Spine 使用 blend mode 显示效果不正确的问题</li> 
   <li>修复 Spine 挂点节点在编辑器设置 scale 后不生效的问题</li> 
  </ul> </li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.cocos.com%2FCocosDashboard%2Fv1.0.17%2FCocosDashboard-v1.0.17-win-080719.exe" target="_blank">下载 DASHBOARD</a>。</p> 
<hr> 
<p>Cocos Creator 是以内容创作为核心，实现了脚本化、组件化和数据驱动的游戏开发工具。 具备了易于上手的内容生产工作流，以及功能强大的开发者工具套件，可用于实现游戏逻辑和高性能游戏效果。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e622ff52598dc6383c70d6d03fb9a963de8.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            