
---
title: 'Cocos Creator 3.4.2 今日发布！本年度版本规划抢先看'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cf8196b41f18896c203027cdc5a9a95e675.png'
author: 开源中国
comments: false
date: Fri, 11 Mar 2022 07:07:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cf8196b41f18896c203027cdc5a9a95e675.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Cocos Creator 3.4.2 已发布。在 v3.4.1 中开发团队完善了 2D 渲染组件的数据提交和合批策略，由于这些是触及基础的改动，所以引发了一些 Tiledmap，Graphics 的问题。并且 Spine 和 Dragonbones 在 Android 浏览器上性能没有得到提升，这些问题都在 v3.4.2 版本中得到了集中的解决。</p> 
<p>另外，在社区的积极测试和反馈下，开发团队也修复了一些编辑器相关的体验问题，比如脚本重新编译时导致的内存泄露、大项目构建 iOS 平台时资源拷贝的卡顿问题。</p> 
<p>请所有使用 v3.4 的用户升级到 v3.4.2，将得到更优秀的稳定性和开发体验。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-cf8196b41f18896c203027cdc5a9a95e675.png" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong> 版本预告 </strong></p> 
<p style="margin-left:0; margin-right:0"><span>开发团队表示，<strong>针对近期用户们集中反馈的部分产品可用性问题，他们规划了 v3.5 版本以尽快处理，不久就会开启公测。</strong>v3.5 将在 v3.4 的基础上小步迭代，提升产品的可用性和易用性，并尽可能确保稳定性和兼容性。</span>特别是一些项目遇到的发热、原生性能、包体，以及编辑器稳定性、工作流问题，今年都会重点解决。</p> 
<hr> 
<p><strong><span>以下是 Cocos Creator 3.4.2 重点更新说明：</span></strong></p> 
<p><span><strong>重要更新 </strong></span></p> 
<ol start="1" style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">修复脚本重新加载导致的内存泄漏问题，在脚本更新过程中编辑器不再有持续性的内存增长。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复一些编辑器构建相关问题：</p> 
  <ul> 
   <li> <p style="margin-left:0; margin-right:0">修复勾选首包为远程包后取消，可能导致原生平台构建失败的问题；</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">项目配置更改，可能导致构建后 md5 变化的问题；</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">修复勾选 MD5 后重复构建两次 hash 值发生变化的问题。</p> </li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">iOS 平台选择 “跳过 XCode 工程更新” 时避免拷贝资源文件夹，修复打包时无资源的问题。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">提升原生平台稳定性：</p> 
  <ul> 
   <li> <p style="margin-left:0; margin-right:0">修复 Vulkan 后端在 Android 12 上的崩溃问题；</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">避免游戏在 Android Surface 销毁时（进入后台等情况）引发的崩溃和黑屏问题；</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">修复游戏从 Camera 返回时可能出现的崩溃问题。</p> </li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">在 Spine 和 DragonBones 中使用共享的 VertexBufferAccessor，提升 GPU 提交 buffer 的性能。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复一些 v3.4.1 重构引入的问题：</p> 
  <ul> 
   <li> <p style="margin-left:0; margin-right:0">修复 SkeletalAnimation 在不调用 play 的情况下直接 setTime 无效的问题；</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">修复 2D 粒子在部分情况下会产生闪烁的渲染表现问题；</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">修复 Tiledmap 的渲染问题；</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">修复 Dragonbones 在设置位置后需要调用 `ArmatureDisplay.markForUpdateRenderData` 才可以正确更新的问题；</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">修复 Mask 对 Spine 和 Dragonbones 无效的问题。</p> </li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">给引擎创建的默认场景添加天空盒（如果不需要天空盒的项目，请记得删除场景中 LDR 和 HDR 的两套天空盒资源）。</p> </li> 
</ol> 
<p style="margin-left:0; margin-right:0"><span><strong> Editor </strong></span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复动画时间轴右键事件帧后，查看红线随鼠标滑动而移动的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复编辑器重启后，需要点击运行才能预览 web 项目的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复编译原生模拟器 UI_GPU_DRIVEN 的报错</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复勾选 MD5 后重复构建两次 hash 值发生变化的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复 prefab 数据里根节点 root 为 null 会导致报错的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>优化属性检查器上部分属性的顺序</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复 Canvas Camera 在编辑器中 resize 的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复选中节点后层级管理器不会自动展开的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复 Mac 上 num-input shift + wheel 功能失效的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复动画编辑切换属性轨道后偶现未及时更新数据的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复动画编辑部分特殊分量轨道无法粘贴的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复脚本重新加载导致的内存泄漏问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复项目配置更改，可能导致构建后 md5 变化的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复属性检查器上 resetComponent 后无法删除的问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复构建插件机制 BuildResult 查询图集资源路径时的返回值错误问题</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复勾选首包为远程包后取消，可能导致原生平台构建失败的问题</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><span><strong> Engine</strong></span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>Shared vertex buffer accessor for Spine and DragonBones [10077]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix skeletal animation sample() does not work as intended [10006]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix DragonBones node can’t be moved in editor [10031]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix 2d particle rendering issue [10038]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix Tiled map rendering issue [10059]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix TiledLayer culling row and col [10035]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix MotionStreak updateColor bug [10055]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Add default skybox [10021]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix planar shadow z-fighting [10026]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Add OHOS platform detection [10028]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix skybox stretch in ortho projection [10045]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix releaseMapInfo error. [10062]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Add protection for invalid node.uiProps [10060]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix native platform mesh-render-data index error. [10071]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Optimize multi-touch on ByteDance platform [10086]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix canvas widget bug in editor [10052]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix renderData update bug when renderable2d is not rendering [10101]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix interface checking [10109]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix pointer event list manager [10084]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix custom class missing when the instantiate error [10128]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix bug for compress texture usage under Sprite grayscale mode [10129]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix getTiledTileAt cause layer show wrong. [10137]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix Node rotate API doc [10140]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Ensure RenderData.clear won’t break usability [10177]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Update editBox size when node resize [10188]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix iOS version detection on Wechat platform [10159]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix mask is not working for spine/db [10201]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Improve touch event performance by caching system info on ByteDance platform [10218]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix merge batches issue with multi canvas [10232]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Add JsbBridgeWrapper for OHOS [4204]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>VK: fix android 12 crash [4217]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Supply a default context when surface destroyed [4222]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Use same mtx for write [4220]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>iOS/mac skip POST_BUILD copy Resources folder procedure [4216]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix spine binary data read issue. [4229]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix loop audio would stop for ios system [4254]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix restart view size [4256]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix spirv incorrect name on binding [4259]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix app crash after switch back from Camera [4268]</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>Fix incorrect resize behavior on iOS [4265]</span></p> </li> 
</ul> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cocos.com%2Fcreator" target="_blank">https://www.cocos.com/creator</a></p> 
<hr> 
<p>Cocos Creator 是以内容创作为核心，实现了脚本化、组件化和数据驱动的游戏开发工具。 具备了易于上手的内容生产工作流，以及功能强大的开发者工具套件，可用于实现游戏逻辑和高性能游戏效果。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e622ff52598dc6383c70d6d03fb9a963de8.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            