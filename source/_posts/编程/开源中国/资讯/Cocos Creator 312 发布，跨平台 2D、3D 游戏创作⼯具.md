
---
title: 'Cocos Creator 3.1.2 发布，跨平台 2D、3D 游戏创作⼯具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-96ad31afc14135471e169130946b1ab7e4f.png'
author: 开源中国
comments: false
date: Thu, 22 Jul 2021 06:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-96ad31afc14135471e169130946b1ab7e4f.png'
---

<div>   
<div class="content">
                                                                                            <p>Cocos Creator 3.1.2 已于上周发布。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-96ad31afc14135471e169130946b1ab7e4f.png" referrerpolicy="no-referrer"></p> 
<p>Cocos Creator 是以内容创作为核心，实现了脚本化、组件化和数据驱动的游戏开发工具。 具备了易于上手的内容生产工作流，以及功能强大的开发者工具套件，可用于实现游戏逻辑和高性能游戏效果。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e622ff52598dc6383c70d6d03fb9a963de8.png" referrerpolicy="no-referrer"></p> 
<p><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cocos.com%2Fcreator" target="_blank">其开发团队在发布公告写道</a>：</strong></p> 
<blockquote> 
 <p><strong>v3.1.2 是在 v3.1.1 上优化体验和性能的版本，这个版本的更新内容是不包含在 v3.2 中的，之后会将 v3.1.2 的更新合并到 v3.2.1 和 v3.3.0。</strong>此外，从 3.1.0 之后引擎组其实一直在并行推进三个版本线，v3.2.0, v3.1.x, v3.3.0，其中 v3.2 由于有配合鸿蒙 2.0 发布的需求，所以发布日早就定下了，为了稳定性其实主要就是在 v3.1.1 基础之上增加了鸿蒙平台支持。而在这之后，我们也在持续收到开发者关于 3.1 的问题反馈，为了更切实解决开发者遇到的痛点问题，并且降低开发者的升级门槛，我们决定继续在 v3.1.2 上优化体验和性能，交付给开发者。</p> 
 <p>目前 Cocos Creator v3.x 作为一个新生的 3D 引擎，距离开发者的期待还有不小的距离，我们希望通过这种持续交付的实际行动来给开发者更强的信心。</p> 
</blockquote> 
<h2>Improvement</h2> 
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
<h2>Bug Fixes</h2> 
<ul> 
 <li>修复 Empty 模板创建项目的问题</li> 
 <li>修复材质编辑器中多 PASS 切换问题和部分属性显示丢失</li> 
 <li>修复 JointTextureLayout 面板无法滚动</li> 
 <li>修复 SplashScreen 设置窗口无法关闭问题</li> 
 <li>修复预制体根节点上的脚本在原生环境中丢失的问题</li> 
 <li>修复重复加载 Morph 模型导致的渲染错误</li> 
 <li>修复 TTF 字体丢失时的崩溃</li> 
 <li>动画编辑器修复 
  <ol> 
   <li>修复动画编辑器节点关键帧无法直接删除</li> 
   <li>修复动画编辑器框选后，按下 Ctrl 添加关键帧后复制粘贴、缩放、排列关键帧功能异常</li> 
   <li>修复动画编辑器属性列表超出不出现滚动条、sample 修改后，当前时间显示未实时更新</li> 
  </ol> </li> 
 <li>环境与光影 
  <ol> 
   <li>修复开启 IBL 之后的材质报错</li> 
   <li>修复天空盒第一次设置无法显示</li> 
   <li>修复开启 ShadowMap 阴影后 GPU 预烘焙骨骼动画失效</li> 
  </ol> </li> 
 <li>粒子模块修复 
  <ol> 
   <li>修复粒子材质在节点未启用的情况下无法显示的问题</li> 
   <li>修复粒子 start speed 效果问题和旋转时的重力效果问题</li> 
  </ol> </li> 
 <li>构建模块修复 
  <ol> 
   <li>修复构建插件重启后报错 (来自论坛反馈： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fforum.cocos.org%2Ft%2Ftopic%2F113448" target="_blank">构建扩展包刷新报错 2</a>)</li> 
   <li>修复自动图集配置修改后构建仍使用缓存 (来自论坛反馈：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fforum.cocos.org%2Ft%2Ftopic%2F114657" target="_blank">CC3.1.1自动图集，打包后会保留原图</a>)</li> 
   <li>修复安卓 abi 无默认值与原生 native 文件夹的 git ignore 配置问题 (来自论坛反馈：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fforum.cocos.org%2Ft%2Ftopic%2F114412" target="_blank">原生native目录需要进行git版本控制吗 2</a>)</li> 
  </ol> </li> 
 <li>Tiledmap 修复 
  <ol> 
   <li>修复使用多图集下的 Tilesets 显示错误</li> 
   <li>修复 TiledLayer getTiledTileAt 函数报错问题</li> 
  </ol> </li> 
 <li>2D 骨骼动画 
  <ol> 
   <li>修复编辑器更新 color，Spine 和 DB 透明度不生效问题</li> 
   <li>修复 web 和 native 上 Spine 使用 blend mode 显示效果不正确的问题</li> 
   <li>修复 Spine 挂点节点在编辑器设置 scale 后不生效的问题</li> 
  </ol> </li> 
</ul> 
<p>以上就是 v3.1.2 的重要更新，优化了大量开发者反馈的问题。</p> 
<p>另外，v3.3.0 版本已进入迭代后期，这个版本有一些非常重要的更新：</p> 
<ol> 
 <li>进一步提高原生化比重，在原生层实现渲染场景，优化性能，为未来的上层原生化和场景管理打好基础</li> 
 <li>渲染管线优化，降低 IO 压力</li> 
 <li>优化大项目使用体验：降低编辑器内存使用，避免崩溃，优化卡顿</li> 
 <li>优化标准光照模型</li> 
 <li>动画数据重构升级：为动画系统升级和动画状态机做好准备</li> 
 <li>各个后端物理行为统一</li> 
 <li>延迟渲染管线优化：光源裁剪、SSPR 等</li> 
</ol> 
<p>除此之外还有各种 Demo 也在制作当中，比如已经上架 Store 的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fforum.cocos.org%2Ft%2Ftopic%2F116334" target="_blank">跑酷 Demo 56</a>。API 文档页面也在进行重新设计。</p>
                                        </div>
                                      
</div>
            