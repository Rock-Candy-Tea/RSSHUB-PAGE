
---
title: 'Verge3D 3.4 for Blender 发行说明'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-12b5464b970a4ed664424621c14a113d3fa.JPEG'
author: 开源中国
comments: false
date: Tue, 13 Apr 2021 16:26:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-12b5464b970a4ed664424621c14a113d3fa.JPEG'
---

<div>   
<div class="content">
                                                                    
                                                        <p>作为面向艺术家与设计师的WebGL开发套件，Verge3D一直在可用性和易用性角度做出改进与升级。</p> 
<p>Verge3D 3.4 版的新特性包括：页面滚动效果、多行文本和脚本拼图、支持OSL着色器、新的Blender集成、低延迟音频、引入拼图方式增加雾和射线投射效果、AR模式，以及许多其他特性和性能改进。详见下文。</p> 
<h2>滚动过渡效果</h2> 
<p>通过在拼图中跟踪用户的页面滚动变化量，可以根据滚动条的位置在3D场景中实现各种变换。您可用这种效果创建有趣的网站、登录页或产品演示等。例如，在此<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcdn.soft8soft.com%2Fdemo%2Fapplications%2Fscroll_animation%2Fscroll_animation.html" target="_blank">官方案例</a>中，页面滚动量会影响动画、相机位置和颜色变化。</p> 
<p>此特性基于<strong>event(事件</strong><strong>)</strong><strong>拼图</strong>的新选项——<strong>scrol</strong><strong>l(滚动)</strong>实现。同时，<strong>get event property(获取项目属性</strong><strong>)</strong><strong>拼图</strong>新增了<strong>scrollX(水平滚动)</strong>和<strong>scrollY(垂直滚动)</strong>属性。</p> 
<p style="text-align:center"><img alt="Verge3D" src="https://oscimg.oschina.net/oscnet/up-12b5464b970a4ed664424621c14a113d3fa.JPEG" width="678" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#fadb14">有关详细说明，请参见以下教程：</span></p> 
<p>B站地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1pa4y1L79t%2F" target="_blank">https://www.bilibili.com/video/BV1pa4y1L79t/</a></p> 
<p>此案例<strong>“</strong><strong>Scroll Animation</strong><strong>”</strong>的源文件包含在Verge3D 3.4版的发行包中。</p> 
<h2>多行文本和脚本拼图</h2> 
<p style="text-align:left">现在，<strong>“</strong><strong>Text(</strong><strong>文本)”类别</strong>中提供用于输入多行文本的拼图，它可与任何接受文本作为输入对象的拼图一起使用。</p> 
<p style="text-align:center"><img alt="多行拼图" src="https://oscimg.oschina.net/oscnet/up-c100e5040433874530ebef33e495d745b47.JPEG" width="780" referrerpolicy="no-referrer"></p> 
<p>使用该拼图，您可以在应用中插入大量文本，如产品描述，或某些自定义的HTML / CSS标记。</p> 
<p>多行拼图基于可嵌入的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Face.c9.io%2F" target="_blank">Ace</a>编辑器开发。Ace因用于Amazon的Cloud9的集成开发环境而被人熟知。它提供的特色功能包括语法突出显示、行编号、自动缩进，代码折叠和实时语法检查器等。</p> 
<p>另外，“<strong>Advanced(</strong><strong>高级</strong>)”<strong>类别中</strong>新增了可执行JavaScript脚本的拼图。您可将与<strong>多行文本</strong><strong>拼图</strong>连用，直接在拼图编辑器中使用代码功能，无需手动编辑脚本文件。</p> 
<p style="text-align:center"><img alt="执行代码拼图" src="https://oscimg.oschina.net/oscnet/up-bf9d40c74d830abb3126fb90ab6622d069d.JPEG" width="856" referrerpolicy="no-referrer"></p> 
<p>在此拼图中键入的JavaScript代码可以与场景的其他元素交互。 因此，您可以访问变量拼图，并从其内部触发规程拼图。</p> 
<p style="text-align:center"><img alt="执行代码拼图2" src="https://oscimg.oschina.net/oscnet/up-fefa4272f7de1c6f96933414342bf990cbb.JPEG" width="858" referrerpolicy="no-referrer"></p> 
<p>直接通过编辑JavaScript脚本来实现拼图交互的旧方法依然有效。关于此类用法的相信信息，请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.soft8soft.com%2Fdocs%2Fmanual%2Fen%2Fintroduction%2FUsing-JavaScript.html" target="_blank">用户手册</a>中的相关章节。</p> 
<h2>OSL 着色器</h2> 
<p>现在，您可以使用开放着色语言（Open Shading Language）创建自定义的实时着色器。您可在Blender的“<strong>Scene</strong><strong>(</strong><strong>场景)</strong>”选项卡中启用此<span style="background-color:transparent">功能，请先切换到“</span><strong>Cycles渲染器</strong><span style="background-color:transparent">”，然后勾选下方的复选框：</span></p> 
<p> </p> 
<p style="text-align:center"><img alt="在Blender中启用OSL着色器" src="https://oscimg.oschina.net/oscnet/up-616b28b3aa05c35b9321dd2a39bbc6b347d.JPEG" width="374" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p>接下来，即可以在材质中使用“<strong>Script</strong><strong>(</strong><strong>脚本)</strong>”节点来调用自定义OSL文件。</p> 
<p style="text-align:center"><img alt="OSL着色器示例" src="https://oscimg.oschina.net/oscnet/up-518e57d06cfc383aba3d6b8107c9a0e3377.JPEG" width="845" referrerpolicy="no-referrer"></p> 
<p>着色器本身可以使用OSL代码编写，也可以从某些<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FADN-DevTech%2F3dsMax-OSL-Shaders" target="_blank">着色器库</a>中直接借用。 例如，3ds Max的检查着色器的代码如下：</p> 
<div> 
 <div> 
  <div> 
   <pre><span style="color:#595959"><span style="color:#595959"><span style="color:#595959">shader</span> <span style="color:#595959">Checker</span>
</span></span><span style="color:#595959"><span style="color:#595959"><span style="color:#ff0000">[</span><span style="color:#ff0000">[</span> <span style="color:#6f42c1">string</span> <span style="color:#595959">help</span> <span style="color:#d73a49">=</span> <span style="color:#669900">"A simple Checkboard OSL sample shader"</span>,
</span></span><span style="color:#595959"><span style="color:#595959">   <span style="color:#6f42c1">string</span> <span style="color:#595959">category</span> <span style="color:#d73a49">=</span> <span style="color:#669900">"Textures"</span>
</span></span><span style="color:#595959"><span style="color:#595959"><span style="color:#ff0000">]</span><span style="color:#ff0000">]</span>
</span></span><span style="color:#595959"><span style="color:#595959"><span style="color:#999977">(</span>
</span></span><span style="color:#595959"><span style="color:#595959">  <span style="color:#595959">point</span> <span style="color:#595959">UVW</span>   <span style="color:#d73a49">=</span> <span style="color:#595959">vector</span><span style="color:#999977">(</span><span style="color:#595959">u</span>,<span style="color:#595959">v</span>,<span style="color:#005cc5">0</span><span style="color:#999977">)</span> 
</span></span><span style="color:#595959"><span style="color:#595959">    <span style="color:#ff0000">[</span><span style="color:#ff0000">[</span> <span style="color:#6f42c1">string</span> <span style="color:#595959">help</span><span style="color:#d73a49">=</span><span style="color:#669900">"The position to shade. Default to the standard UV space."</span> <span style="color:#ff0000">]</span><span style="color:#ff0000">]</span>,
</span></span><span style="color:#595959"><span style="color:#595959">  <span style="color:#595959">float</span> <span style="color:#595959">Scale</span> <span style="color:#d73a49">=</span> <span style="color:#005cc5">0.25</span>, 
</span></span><span style="color:#595959"><span style="color:#595959">  <span style="color:#595959">color</span> <span style="color:#595959">Color1</span> <span style="color:#d73a49">=</span> <span style="color:#595959">color</span><span style="color:#999977">(</span><span style="color:#005cc5">1</span>,<span style="color:#005cc5">1.0</span>,<span style="color:#005cc5">0.2</span><span style="color:#999977">)</span>,   
</span></span><span style="color:#595959"><span style="color:#595959">  <span style="color:#595959">color</span> <span style="color:#595959">Color2</span> <span style="color:#d73a49">=</span> <span style="color:#595959">color</span><span style="color:#999977">(</span><span style="color:#005cc5">0.2</span>,<span style="color:#005cc5">0.2</span>,<span style="color:#005cc5">1.0</span><span style="color:#999977">)</span>,  
</span></span><span style="color:#595959"><span style="color:#595959">
</span></span><span style="color:#595959"><span style="color:#595959">  <span style="color:#595959">output</span> <span style="color:#595959">color</span> <span style="color:#595959">Col</span> <span style="color:#d73a49">=</span> <span style="color:#005cc5">0</span>
</span></span><span style="color:#595959"><span style="color:#595959"><span style="color:#999977">)</span>
</span></span><span style="color:#595959"><span style="color:#595959"><span style="color:#ff0000">&#123;</span>
</span></span><span style="color:#595959"><span style="color:#595959">    <span style="color:#595959">point</span> <span style="color:#595959">p</span> <span style="color:#d73a49">=</span> <span style="color:#595959">UVW</span> <span style="color:#d73a49">/</span> <span style="color:#595959">Scale</span><span style="color:#ff0000">;</span>
</span></span><span style="color:#595959"><span style="color:#595959">    <span style="color:#6f42c1">int</span> <span style="color:#595959">x</span> <span style="color:#d73a49">=</span> <span style="color:#999977">(</span><span style="color:#6f42c1">int</span><span style="color:#999977">)</span><span style="color:#d73a49">mod</span><span style="color:#999977">(</span><span style="color:#595959">p</span><span style="color:#ff0000">[</span><span style="color:#005cc5">0</span><span style="color:#ff0000">]</span>,<span style="color:#005cc5">2.0</span><span style="color:#999977">)</span><span style="color:#ff0000">;</span>
</span></span><span style="color:#595959"><span style="color:#595959">    <span style="color:#6f42c1">int</span> <span style="color:#595959">y</span> <span style="color:#d73a49">=</span> <span style="color:#999977">(</span><span style="color:#6f42c1">int</span><span style="color:#999977">)</span><span style="color:#d73a49">mod</span><span style="color:#999977">(</span><span style="color:#595959">p</span><span style="color:#ff0000">[</span><span style="color:#005cc5">1</span><span style="color:#ff0000">]</span>,<span style="color:#005cc5">2.0</span><span style="color:#999977">)</span><span style="color:#ff0000">;</span>
</span></span><span style="color:#595959"><span style="color:#595959">    <span style="color:#6f42c1">int</span> <span style="color:#595959">z</span> <span style="color:#d73a49">=</span> <span style="color:#999977">(</span><span style="color:#6f42c1">int</span><span style="color:#999977">)</span><span style="color:#d73a49">mod</span><span style="color:#999977">(</span><span style="color:#595959">p</span><span style="color:#ff0000">[</span><span style="color:#005cc5">2</span><span style="color:#ff0000">]</span>,<span style="color:#005cc5">2.0</span><span style="color:#999977">)</span><span style="color:#ff0000">;</span>
</span></span><span style="color:#595959"><span style="color:#595959">
</span></span><span style="color:#595959"><span style="color:#595959">    <span style="color:#d73a49">if</span><span style="color:#999977">(</span> <span style="color:#999977">(</span><span style="color:#999977">(</span><span style="color:#595959">x</span><span style="color:#ff0000">%</span><span style="color:#005cc5">2</span><span style="color:#999977">)</span> <span style="color:#d73a49">^</span> <span style="color:#999977">(</span><span style="color:#595959">y</span><span style="color:#ff0000">%</span><span style="color:#005cc5">2</span><span style="color:#999977">)</span><span style="color:#999977">)</span> <span style="color:#d73a49">=</span><span style="color:#d73a49">=</span> <span style="color:#999977">(</span><span style="color:#595959">z</span><span style="color:#ff0000">%</span><span style="color:#005cc5">2</span><span style="color:#999977">)</span> <span style="color:#999977">)</span><span style="color:#ff0000">&#123;</span>
</span></span><span style="color:#595959"><span style="color:#595959">        <span style="color:#595959">Col</span> <span style="color:#d73a49">=</span> <span style="color:#595959">Color1</span><span style="color:#ff0000">;</span>
</span></span><span style="color:#595959"><span style="color:#595959">    <span style="color:#ff0000">&#125;</span> <span style="color:#d73a49">else</span> <span style="color:#ff0000">&#123;</span>
</span></span><span style="color:#595959"><span style="color:#595959">        <span style="color:#595959">Col</span> <span style="color:#d73a49">=</span> <span style="color:#595959">Color2</span><span style="color:#ff0000">;</span>
</span></span><span style="color:#595959"><span style="color:#595959">    <span style="color:#ff0000">&#125;</span>
</span></span><span style="color:#595959"><span style="color:#595959"><span style="color:#ff0000">&#125;</span></span></span></pre> 
  </div> 
 </div> 
</div> 
<p>如果您对手动转换和调试OSL着色器感兴趣，可使用脚本<code>osl2glsl.py</code>运行转换器。 该转换器已在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSoft8Soft%2Fpyosl" target="_blank">Github</a>上基于MIT许可开源。</p> 
<h2>Blender集成</h2> 
<p>修复了与最近发布的Blender 2.9的节点材质相关的各种兼容性问题。此外，我们还为即将发布的Blender 2.91兼容做了一些准备工作。<span style="background-color:#fbfbfb; color:#444444">支持了</span>Cycles节点<strong>Wavelength</strong><strong>(</strong><strong>波长)</strong>，它将波长值转换为RGB值，可用于获得光谱上的特定颜色。</p> 
<p style="text-align:center"><img alt="Blender波长节点" src="https://oscimg.oschina.net/oscnet/up-d77e441e804325376615e3e9362940c4db2.JPEG" width="943" referrerpolicy="no-referrer"></p> 
<p>“相机设置"中增加了From Cursor按钮，可用于通过3D光标设置相机目标。</p> 
<p style="text-align:center"><img alt="from cursor" src="https://oscimg.oschina.net/oscnet/up-22f4eaf5f47866a1f612f55cc6eb4bd4fbd.JPEG" width="666" referrerpolicy="no-referrer"></p> 
<p>最后，现在有可能在兼容gltf的材质中使用外部遮挡贴图（在AO必须始终打包到ORM纹理之前）。</p> 
<h2>网络音频</h2> 
<p><strong>load sound</strong><strong>(</strong><strong>加载声音)拼图</strong>新增切换<strong>sound(声音)</strong>和<strong>music(音乐)</strong>。其中，切换到声音表示启用Web Audio后端，切换到音乐表示启用HTML5音频后端。</p> 
<p style="text-align:center"><img alt="声音与音乐节点" src="https://oscimg.oschina.net/oscnet/up-5890ef5260bf59677e595f14edcb1c39e57.JPEG" width="479" referrerpolicy="no-referrer"></p> 
<p>Web Audio后端可播放低延迟和无间隙循环的音频。我们已经优化了发型包中所有案例的音频部分。</p> 
<p>因为Web Audio需要消耗更多的内存和更高的处理性能，我们建议您仅将其用于短的音频片段。对于较长的音频片段，例如背景音乐，最好使用HTML5音频方式。</p> 
<p>此外，<strong>feature availab</strong><strong>le(</strong><strong>可用功能)</strong>拼图新增<strong>Web Audio API</strong>选项，您可以在此检查浏览器是否支持此Web标准。 您也可以使用JavaScript API的方式<code>Detector.checkWebAudio()</code> 进行检查。</p> 
<p style="text-align:center"><img alt="web audio api" src="https://oscimg.oschina.net/oscnet/up-99876610e0f452632abf5c7ad808986ec9d.JPEG" width="464" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">拼图编辑器的“<strong>Sound/Video(</strong>声音/视频)”类别已重命名为“<strong>Audio/Video(</strong>音频/视频)”。</p> 
<p>现在可以在拼图编辑器的“<strong>Init(</strong>初始化)”选项卡中使用声音拼图，从而预先加载声音。</p> 
<h2>AR 模式</h2> 
<p>目前，<strong>enter AR mode</strong><strong>(进入AR模式)</strong>拼图支持类似于VR对应对象的各种定位模式：<strong>loo</strong><strong>king around(</strong><strong>环顾)，</strong><strong>sitting or standing(</strong><strong>坐/立)，</strong><strong>room(</strong><strong><span style="color:#313131">室内)</span></strong><strong>，walking(步行)和</strong><strong>viewer locked(</strong><strong>观察者锁定)</strong>。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-5b0b7d1228039cdb330ae1aa4934f79ecec.JPEG" width="580" referrerpolicy="no-referrer"></p> 
<p>为与旧场景兼容，AR的最佳模式是<strong>sitti</strong><strong>ng(坐)</strong>或<strong>standing(立)</strong>，<strong>room(室内)</strong>或<strong>walking</strong><strong>(步行)，</strong>其中默认模式设置是<strong>looking around(</strong><strong>环顾)</strong>（即当用户从场景原点观看）。</p> 
<h2>雾和射线投射拼图</h2> 
<p>新增<strong>add fog(</strong><strong>添加雾)</strong>拼图，无需编码即可添加雾效。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-a5ccee9c413174690f3bd47687b120a7495.JPEG" width="609" referrerpolicy="no-referrer"></p> 
<p>您也可以指定雾的颜色和密度，将RGB或密度设置为零从而将其删除。</p> 
<p style="text-align:center"><img alt="添加雾效" src="https://oscimg.oschina.net/oscnet/up-4e772e049be58b127250b6ac404d3b11b67.JPEG" width="783" referrerpolicy="no-referrer"></p> 
<p>新增<strong>ray cast(</strong><strong>射线投射)</strong>拼图，您可以在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.soft8soft.com%2Fdocs%2Fmanual%2Fen%2Fpuzzles%2FScenes.html%23raycast" target="_blank">参考页面</a>找到相关描述和使用示例。</p> 
<p style="text-align:center"><img alt="射线投射拼图" src="https://oscimg.oschina.net/oscnet/up-2432492060f284f31e5f0ae14d85e858684.JPEG" width="567" referrerpolicy="no-referrer"></p> 
<h2>连接器拼图</h2> 
<p>Connectors(连接器)拼图是一个新的便捷拼图，可用于组合具有返回值（例如声音）的拼图。</p> 
<p style="text-align:center"><img alt="拼图连接器" src="https://oscimg.oschina.net/oscnet/up-60f8cbd0e00b597860e777aaae46d4b90c2.png" width="381" referrerpolicy="no-referrer"></p> 
<p>您无需再创建辅助变量，也能将这些拼图组合在一起。</p> 
<h2>安装程序签名</h2> 
<p>我们在Windows版安装程序中已使用扩展验证证书进行签名，因此不再显示“未知发布者”的警告。</p> 
<h2>其他改进</h2> 
<p><strong>replace texture</strong><strong>(替换纹理)</strong>拼图现在支持将视频纹理分配给与gltf兼容的材质。<strong>replace texture</strong><strong>(替换纹理)</strong>和<strong>get texture param</strong><strong>(</strong><strong>获取纹理参数)</strong>拼图也可以正确地与视频纹理配合使用。</p> 
<p>通过在WebGL纹理中使用RGB格式而非RGBA，减少了JPEG纹理的内存消耗。此外，<strong>export to gltf(</strong><strong>导出到gltf</strong><strong>)</strong>拼图现在可以直接导出JPEG纹理，而无需将其预转为PNG。</p> 
<p>现在可以通过将JavaScript API属性设置 <code>OrbitControls.screenSpacePanning</code> 为<strong>false</strong>来启用水平相机平移（用于实现类似Google Maps的悬停控制），例如：</p> 
<p><code>app.controls.screenSpacePanning = false;</code></p> 
<p><strong>set style(</strong>设置样式)和<strong>set attribute(</strong>设置属性)拼图现在可以在IE 11中使用。<strong>set style(</strong>设置样式)拼图的插槽<strong>@media</strong>现在也可以在macOS和iOS的Safari浏览器中使用。</p> 
<p>我们在<strong>用户手册</strong>中添加了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.soft8soft.com%2Fdocs%2Fmanual%2Fen%2Fintroduction%2FHardware-Related-Issues.html" target="_blank">新的章节</a>，其中概述了创建场景时可能遇到的一些硬件限制。增加了对有关“Too many attributes”的错误的说明。</p> 
<h2>故障修复</h2> 
<ul> 
 <li>“活动摄像机”拼图现在可以正确启用/禁用渲染拼图（感谢用户报告<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.soft8soft.com%2Ftopic%2Fproblem-when-switching-active-camera-with-antialias%2F" target="_blank">问题</a>）。</li> 
 <li>现在可以在VR模式下正确切换基于图像的照明（感谢用户报告<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.soft8soft.com%2Ftopic%2Fvr-version-of-my-vehicle-fantasy-timer-and-ibl-lighting-issues%2F" target="_blank">问题</a>）。</li> 
 <li>修复了<strong>export to gltf(</strong><strong>导出至gltf)</strong>拼图时导致UV丢失的问题。</li> 
 <li>修复了未完成回调时相机补间的错误（感谢用户报告<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.soft8soft.com%2Ftopic%2Fbug-orbitcontrol-tween-not-calling-finishcb-if-the-camera-is-already-there%2F" target="_blank">问题</a>）。</li> 
 <li>修复了形状键和分配材质的错误（感谢用户报告<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.soft8soft.com%2Ftopic%2Fassign-material-conflicts-with-morph-factor%2F" target="_blank">问题</a>）</li> 
 <li>在<strong>event(项目)</strong>拼图中删除了重复的point事件选项。</li> 
 <li>修复了Blender当前不受支持的<strong>BSDF Toon</strong>着色器带来的引擎崩溃。</li> 
 <li>JavaScript方法<code>Material.toJSON()</code>不再因基于节点的材质而出错。</li> 
</ul> 
<blockquote> 
 <p>发布时间：2020年9月24日<br> 下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fverge3d.funjoy.tech%2Fget-verge3d" target="_blank">https://verge3d.funjoy.tech/get-verge3d</a></p> 
</blockquote>
                                        </div>
                                      
</div>
            