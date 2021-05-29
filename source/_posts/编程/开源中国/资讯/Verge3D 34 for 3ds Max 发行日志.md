
---
title: 'Verge3D 3.4 for 3ds Max 发行日志'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cd5611cc30ddd6c3a18d3ff0acb010bdf36.JPEG'
author: 开源中国
comments: false
date: Sat, 29 May 2021 10:36:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cd5611cc30ddd6c3a18d3ff0acb010bdf36.JPEG'
---

<div>   
<div class="content">
                                                                    
                                                        <blockquote> 
 <p>发布时间：2020年9月25日<br> 下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fverge3d.funjoy.tech%2Fget-verge3d" target="_blank">https://verge3d.funjoy.tech/get-verge3d</a></p> 
</blockquote> 
<p>作为面向艺术家与设计师的WebGL开发套件，Verge3D一直在可用性和易用性角度做出改进与升级。</p> 
<p>Verge3D 3.4 版可通过使用页面滚动、多行文本和脚本拼图，来创建有趣的3D场景转换，改进了对OSL着色器的支持，增加了低延迟音频，实现了无需编码即可引入雾和射线投射。另外，此版本支持AR模式，并新增了许多其他特性和性能改进，请从下文中了解。</p> 
<p> </p> 
<h2>多行拼图和脚本执行</h2> 
<p>现在，“<strong>Text</strong>(文本)”类别中提供用于输入多行文本的拼图，它可与任何接受文本作为输入对象的拼图一起使用。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-cd5611cc30ddd6c3a18d3ff0acb010bdf36.JPEG" width="780" referrerpolicy="no-referrer"></p> 
<p>使用该拼图，您可以在应用中插入大量文本，无论是产品描述，亦或是某些自定义HTML / CSS标记。</p> 
<p>底层的多行拼图基于可嵌入的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Face.c9.io%2F" target="_blank">Ace</a>编辑器，特别用于Amazon的Cloud9代码编辑器。它提供的功能包括语法突出显示、行编号、自动缩进，代码折叠和实时语法检查器。</p> 
<p>另外，还新增执行JavaScript的拼图，位于“<strong>Advanced(</strong><strong>高级</strong>)”类别中。结合上述多行拼图，它使您可以直接在拼图编辑器中使用代码，而无需手动编辑任何脚本。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-9ef856a6cf175824a71a5be1c82a80ad129.JPEG" width="856" referrerpolicy="no-referrer"></p> 
<p>在此拼图中键入的JavaScript代码可以与其余场景交互。 因此，您可以访问变量拼图，也可以从其内部触发程序拼图。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-5af3b7c81f27a09cc10b160b97926c151af.JPEG" width="858" referrerpolicy="no-referrer"></p> 
<p>在JavaScript和拼图之间实现互操作性的原始并更倾向于代码的方法继续有效。有关更多信息和用法详情，请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.soft8soft.com%2Fdocs%2Fmanual%2Fen%2Fintroduction%2FUsing-JavaScript.html" target="_blank">该文档</a>。</p> 
<p> </p> 
<h2><span style="color:#313131">骨骼</span></h2> 
<p>3ds Max中的对象有个称为“<strong>Skeletal Root(根骨骼</strong><strong>)</strong>”的复选框。如果为对象或骨骼启用了该功能，则所有子骨骼都将被视为单个动画骨骼。从而，您只能为根对象或骨骼播放动画，而无需触发所有骨骼的动画。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-6dc9d30a5554650c02096589ab767fbad2a.JPEG" width="717" referrerpolicy="no-referrer"></p> 
<p>为了使用此功能，我们还对“增强现实”演示进行了调整。</p> 
<p> </p> 
<h2>滚动过渡效果</h2> 
<p>现在，您现在可以跟踪用户页面的滚动量，从而可以根据滚动条的位置在3D场景中实现各种变换。这种非常有趣的效果可用于创建精美的网站、登录页面或产品演示。</p> 
<p>参见此<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcdn.soft8soft.com%2Fdemo%2Fapplications%2Fscroll_animation%2Fscroll_animation.html" target="_blank">官方案例</a>，其中滚动量会影响动画、相机位置和颜色变化。</p> 
<p> </p> 
<p>这依赖于event(项目)拼图，它新增了一个新选项——<strong>scrol</strong><strong>l(滚动)</strong>，且<strong>get event property(获取项目属性)</strong>拼图新增<strong>scrollX(水平滚动)</strong>和<strong>scrollY(垂直滚动)</strong>属性。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-d26a16f367dc1424de5649ca9623ec68772.JPEG" width="678" referrerpolicy="no-referrer"></p> 
<h2> </h2> 
<h2>OSL 着色器</h2> 
<p>本版本依旧支持OSL着色器。此次新增OSL节点：<strong>HDRi Environment环境</strong>（仅3ds Max 2021版）。该节点允许创建具有自定义背景和地面的环境照明。<strong>Uber Bitmap</strong><strong>(</strong><strong>位图)</strong>是此次新增的另一个OSL节点。</p> 
<p>您可以创建自定义实时着色器。着色器本身可以使用OSL代码编写，也可以从某些<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FADN-DevTech%2F3dsMax-OSL-Shaders" target="_blank">着色器库</a>中借用。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-28643e1a34f1f40df448bd885c8fc341bc5.JPEG" width="1024" referrerpolicy="no-referrer"></p> 
<p>另外，现在在导出器中使用了新的OSL-to-GLSL转换器。它运行更加强劲并可生成更紧凑的代码。</p> 
<p>如果您对手动转换和调试OSL着色器感兴趣，则可以使用脚本<code>osl2glsl.py</code>运行转换器。 该转换器已根据MIT许可开源，可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSoft8Soft%2Fpyosl" target="_blank">Github</a>上获得。</p> 
<p> </p> 
<h2>其他3ds Max 专属功能</h2> 
<p>支持Arnold节点“<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.arnoldrenderer.com%2Fdisplay%2FA5AF3DSUG%2FMap%2BTo%2BMaterial" target="_blank">Map to Material</a>(映射到材质)”。该节点允许您使用贴图创建自定义着色器。</p> 
<p>除物理材质外，<strong>Standard(标准)</strong>材质也可以支持环境贴图。</p> 
<p>提升了导出速度。</p> 
<p>修复了插件代码，3ds Max 2021中不再显示MaxScript Listener的弃用警告。此外，MaxScript Listener的消息也更加一致。</p> 
<p>“导出设置”中名为“<strong>Export within playback range</strong><strong>(</strong><strong>在播放范围内导出)</strong>”的选项可以使用了。</p> 
<p>修复了场景中存在无顶点的网格（同时应用了UVW贴图修改器）时偶尔发生的导出器崩溃的问题。</p> 
<p>修复了Windows 7特有的导出崩溃问题。</p> 
<p> </p> 
<h2>音频改进</h2> 
<p><strong>load sound(</strong>加载声音)拼图新增切换<strong>sound(声音)</strong>和<strong>music(音乐)</strong>。其中，切换到声音表示启用Web Audio后端，切换到音乐表示启用HTML5音频后端。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-4e9577e3baf49480ac9bfeb83c26dd67d2f.JPEG" width="479" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">Web Audio后端可播放低延迟和无间隙循环的音频。我们已经优化了发型包中所有案例的音频部分。</p> 
<p>因为Web Audio需要消耗更多的内存和更高的处理性能，我们建议您仅将其用于短的音频片段。对于较长的音频片段，例如背景音乐，最好使用HTML5音频方式。</p> 
<p>此外，<strong>feature availab</strong><strong>le(</strong><strong>可用功能)</strong>拼图新增<strong>Web Audio API</strong>选项，您可以在此检查浏览器是否支持此Web标准。 您也可以使用JavaScript API的方式<code>Detector.checkWebAudio()</code> 进行检查。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-f7c29835c36a62c0ec585a4584092310aff.JPEG" width="464" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">拼图编辑器的“<strong>Sound/Video(</strong>声音/视频)”类别已重命名为“<strong>Audio/Video(</strong>音频/视频)”。</p> 
<p>现在可以在拼图编辑器的“<strong>Init(</strong>初始化)”选项卡中使用声音拼图，从而预先加载声音。</p> 
<p> </p> 
<h2>雾和射线投射</h2> 
<p>新增<strong>add fog(</strong><strong>添加雾)</strong>拼图，无需编码即可添加雾效。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-c274e60ac2db5a89ef625d902eff34d5c61.JPEG" width="609" referrerpolicy="no-referrer"></p> 
<p>您也可以指定雾的颜色和密度，将RGB或密度设置为零从而将其删除。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-8e2d0010aeb1c3e1b71d8083a0595a07a22.JPEG" width="783" referrerpolicy="no-referrer"></p> 
<p>新增<strong>ray cast(</strong><strong>射线投射)</strong>拼图，您可以在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.soft8soft.com%2Fdocs%2Fmanual%2Fen%2Fpuzzles%2FScenes.html%23raycast" target="_blank">参考页面</a>找到相关描述和使用示例。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-cd1c054804d29bd00237c0c77fdbffa6d28.JPEG" width="567" referrerpolicy="no-referrer"></p> 
<p> </p> 
<h2>AR 改进</h2> 
<p>目前，<strong>enter AR mode</strong><strong>(进入AR模式)</strong>拼图支持类似于VR对应对象的各种定位模式：<strong>loo</strong><strong>king around(</strong><strong>环顾)，</strong><strong>sitting or standing(</strong><strong>坐/立)，</strong><strong>room(</strong><strong><span style="color:#313131">室内)</span></strong><strong>，walking(步行)和</strong><strong>viewer locked(</strong><strong>观察者锁定)</strong>。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-1bc39dee2d2e4d30019639881883e930402.JPEG" width="580" referrerpolicy="no-referrer"></p> 
<p>为与旧场景兼容，AR的最佳模式是<strong>sitti</strong><strong>ng(坐)</strong>或<strong>standing(立)</strong>，<strong>room(室内)</strong>或<strong>walking</strong><strong>(步行)，</strong>其中默认模式设置是<strong>looking around(</strong><strong>环顾)</strong>（即当用户从场景原点观看）。</p> 
<p> </p> 
<h2>连接器</h2> 
<p>Connectors(连接器)拼图是一个新的便捷拼图，可用于组合具有返回值（例如声音）的拼图。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-d7d23e8685fcdbbf6b5e08cf5e66c883cb6.png" width="381" referrerpolicy="no-referrer"></p> 
<p>您无需再创建辅助变量，也能将这些拼图组合在一起。</p> 
<p> </p> 
<h2>安装程序</h2> 
<p>我们在Windows版安装程序中已使用扩展验证证书进行签名，因此不再显示“未知发布者”的警告。</p> 
<p> </p> 
<h2>其他改进</h2> 
<p><strong>replace texture</strong><strong>(替换纹理)</strong>拼图现在支持将视频纹理分配给与gltf兼容的材质。<strong>replace texture</strong><strong>(替换纹理)</strong>和<strong>get texture param</strong><strong>(</strong><strong>获取纹理参数)</strong>拼图也可以正确地与视频纹理配合使用。</p> 
<p>通过在WebGL纹理中使用RGB格式而非RGBA，减少了JPEG纹理的内存消耗。此外，<strong>export to gltf(</strong><strong>导出到gltf</strong><strong>)</strong>拼图现在可以直接导出JPEG纹理，而无需将其预转为PNG。</p> 
<p>现在可以通过将JavaScript API属性设置 <code>OrbitControls.screenSpacePanning</code> 为<strong>false</strong>来启用水平相机平移（用于实现类似Google Maps的悬停控制），例如：</p> 
<p><code>app.controls.screenSpacePanning = false;</code></p> 
<p><strong>set style(</strong>设置样式)和<strong>set attribute(</strong>设置属性)拼图现在可以在IE 11中使用。<strong>set style(</strong>设置样式)拼图的插槽<strong>@media</strong>现在也可以在macOS和iOS的Safari浏览器中使用。</p> 
<p>我们在<strong>用户手册</strong>中添加了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.soft8soft.com%2Fdocs%2Fmanual%2Fen%2Fintroduction%2FHardware-Related-Issues.html" target="_blank">新的章节</a>，其中概述了创建场景时可能遇到的一些硬件限制。增加了对有关“Too many attributes”的错误的说明。</p> 
<p> </p> 
<h2>故障修复</h2> 
<ul> 
 <li>“活动摄像机”拼图现在可以正确启用/禁用渲染拼图（感谢用户报告<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.soft8soft.com%2Ftopic%2Fproblem-when-switching-active-camera-with-antialias%2F" target="_blank">问题</a>）。</li> 
 <li>现在可以在VR模式下正确切换基于图像的照明（感谢用户报告<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.soft8soft.com%2Ftopic%2Fvr-version-of-my-vehicle-fantasy-timer-and-ibl-lighting-issues%2F" target="_blank">问题</a>）。</li> 
 <li>修复了<strong>export to gltf(</strong><strong>导出至gltf)</strong>拼图时导致UV丢失的问题。</li> 
 <li>修复了未完成回调时相机补间的错误（感谢用户报告<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.soft8soft.com%2Ftopic%2Fbug-orbitcontrol-tween-not-calling-finishcb-if-the-camera-is-already-there%2F" target="_blank">问题</a>）。</li> 
 <li>修复了形状键和分配材质的错误（感谢用户报告<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.soft8soft.com%2Ftopic%2Fassign-material-conflicts-with-morph-factor%2F" target="_blank">问题</a>）。</li> 
 <li>在<strong>event(项目)</strong>拼图中删除了重复的point事件选项。</li> 
 <li>JavaScript方法<code>Material.toJSON()</code>不再因基于节点的材质而出错。</li> 
</ul> 
<p> </p> 
<h2>立即升级</h2> 
<p>一如既往，在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FK-AWZ8smyOUt1pm0lgmpzQ" target="_blank">Verge3D最新发行版下载</a>一文中获取最新预览版的百度盘分享链接吧！欢迎通过<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.soft8soft.com%2Fforums%2F" target="_blank">论坛</a>、微信公众号、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshang.qq.com%2Fwpa%2Fqunwpa%3Fidkey%3Dc31cf6597f3ed7ce68bd47aba6bba23049bf973ac6acc59b0a5a7d1bd933b3ea" target="_blank">QQ群</a>、<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Averge3d%40funjoy.tech" target="_blank">电子邮件</a>提出建议与意见！</p>
                                        </div>
                                      
</div>
            