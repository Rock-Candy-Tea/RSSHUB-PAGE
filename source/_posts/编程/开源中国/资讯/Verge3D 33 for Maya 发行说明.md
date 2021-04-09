
---
title: 'Verge3D 3.3 for Maya 发行说明'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-009af79ef5fb23e23ca7d653830b39d0e23.JPEG'
author: 开源中国
comments: false
date: Thu, 08 Apr 2021 19:55:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-009af79ef5fb23e23ca7d653830b39d0e23.JPEG'
---

<div>   
<div class="content">
                                                                                            <p>作为面向艺术家与设计师的WebGL开发套件，Verge3D一直在可用性和易用性角度做出改进与升级。</p> 
<p>Verge3D 3.3 版引入几个新材质节点，显著加快了应用的加载速度及整体性能，引入了用拼图将Verge3D场景导出为glTF格式的方式，并实现了动态画布纹理。此版本还增加了一些新的拼图，支持了Woocommerce的全局产品属性。请阅读全文了解新增特性及性能改进详情。</p> 
<h2>Maya节点</h2> 
<p>此次更新支持多个新的Maya节点。节点<strong>colorCompos</strong><strong>i</strong><strong>te(颜色</strong><strong><span style="color:#333333">合成</span></strong><strong>)</strong>节点和<strong>floatComposit(浮动合成)</strong>节点可用于在材质中混合遮挡贴图。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-009af79ef5fb23e23ca7d653830b39d0e23.JPEG" width="685" referrerpolicy="no-referrer"></p> 
<p>同时，<strong>Color Constant</strong><strong>(颜色恒定)</strong>节点，<strong>Float Constant(浮动恒定)</strong>节点和<strong>Unit Conversion(</strong><strong>单元转换)</strong>节点现在可以在Verge3D中使用。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-d7fe26dd96d6cb6c257b3d24c7a97bd079c.JPEG" width="426" referrerpolicy="no-referrer"></p> 
<h2>Maya glTF导出器</h2> 
<p>为纹理添加了Verge3D的各向异性过滤设置。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-ecec50b4324faf474872672b3b552df8acb.JPEG" width="1024" referrerpolicy="no-referrer"></p> 
<p>修复了节点材质中多对一连接的错误，例如，当多个<strong>Float(</strong>浮动)节点连接到单一<strong>Color(</strong>颜色)输入时会产生错误。</p> 
<p>修复了与导出的网格物体（此处报告）中缺少UV数据有关的导出器崩溃<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.soft8soft.com%2Ftopic%2Fmodel-wont-load-as-sneal-peek-or-gltf-how-do-i-proceed%2F" target="_blank">问题</a>，以及UV的其他一些问题。</p> 
<h2>加载速度更快</h2> 
<p>基于用户的关注，此版本我们将优化的重心放在优化加载效率方向。着色器编译通常是加载过程中的瓶颈，经过新版本对此执行的一系列优化，场景的加载速度有了显著地提升（部分场景可达3倍）。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-6cbe877e9cceedcb21e352bcb84868d03d4.JPEG" width="720" referrerpolicy="no-referrer"></p> 
<p>这些优化措施包括：</p> 
<ul> 
 <li>引入了并行着色器编译，（在着色器逐个编译之前）若存在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.khronos.org%2Fregistry%2Fwebgl%2Fextensions%2FKHR_parallel_shader_compile%2F" target="_blank">KHR_parallel_shader_compile</a> WebGL扩展，编译将更高效；</li> 
 <li>优化了代表环境光的着色器；</li> 
 <li>优化了与实时阴影有关的着色器；</li> 
 <li>优化了材质着色器（例如<strong>Lambert</strong><span style="color:#333333">材质）</span>；</li> 
 <li>重组了加载流程，整个加载过程更为平滑和快速；</li> 
</ul> 
<p>其中一些优化还提高了Verge3D的渲染性能，尤其是在低端硬件或移动设备上。</p> 
<h2>从应用中导出</h2> 
<p>现在可以以glTF格式导出对象、对象组或整个场景，可用.gltf或.glb（二进制）两种格式。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-95e26e56c7e43899f65823448652b618d86.JPEG" width="635" referrerpolicy="no-referrer"></p> 
<p>此拼图可用于保存应用中的配置好的物体。</p> 
<p>为了获得最佳效果，以及创建可由第三方glTF查看器（如Microsoft Windows 10的默认glTF查看器）打开的标准glTF文件（不带Soft8Soft/Verge3D扩展），我们建议您使用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.soft8soft.com%2Fdocs%2Fmanual%2Fen%2Fintroduction%2FFAQ.html%23gltf_materials" target="_blank">与glTF兼容的材质</a>。</p> 
<h2>摄影机补间轨迹</h2> 
<p>您现在可以在<strong>tween camera(摄影机补间)</strong>拼图中选择球形轨迹了。球形轨迹意味着摄影机将围绕中心轴，以插值距离作为半径，旋转到新位置。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-cf337a45e628aeda22060b40aac512e4994.JPEG" width="720" referrerpolicy="no-referrer"></p> 
<p>当新的视点位于模型后面时，此功能尤其有用。对于轨道摄影机，球面轨迹更为自然，可以防止摄影机在移动途中与模型发生交叉现象。</p> 
<p>另外，<strong>tween camera(摄影机补间)</strong>拼图现在可以使用附近物体的坐标，坐标可以用列表或向量方式提供给拼图。</p> 
<h2>动态画布纹理</h2> 
<p>HTML画布现在可以作为材质纹理使用了。可以使用新引入的HTML拼图<strong>create canvas elem</strong>来创建<code><canvas></code>元素，并如之前一样为材质指定纹理，即使用<strong>replace texture(替换纹理)</strong>拼图。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-6c70ddceb393bc9fb4b8b7b6137f7cdde0b.JPEG" width="557" referrerpolicy="no-referrer"></p> 
<p>一旦创建好，画布即可通过JavaScript进行绘制。您可以在以应用名开头的js文件（<em>your_app_name.js</em>）的<code>runCode()</code> 功能更新画布。为此，请在此处使用拼图中指定的ID来检索画布纹理：</p> 
<div> 
 <div> 
  <div> 
   <pre><span style="color:#595959"><span style="color:#595959"><span style="color:#d73a49">var</span> <span style="color:#005cc5">canvasTex</span> <span style="color:#d73a49">=</span> <span style="color:#595959">v3d</span>.<span style="color:#005cc5">puzzles</span>.<span style="color:#005cc5">canvasTextures</span>[<span style="color:#669900">'my_canvas'</span>];</span></span></pre> 
  </div> 
 </div> 
</div> 
<p>之后，您可以按如下方式访问HTML画布元素：</p> 
<div> 
 <div> 
  <div> 
   <pre><span style="color:#595959"><span style="color:#595959"><span style="color:#d73a49">var</span> <span style="color:#005cc5">canvas</span> <span style="color:#d73a49">=</span> <span style="color:#595959">canvasTex</span>.<span style="color:#005cc5">image</span>;</span></span></pre> 
  </div> 
 </div> 
</div> 
<p><span style="color:#333333">您可以使用可用于在HTML画布上绘制的</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.w3schools.com%2Fgraphics%2Fcanvas_reference.asp" target="_blank">标准方法</a><span style="color:#333333">。例如，如下代码即在白色背景上画了一个蓝色的笑脸:</span></p> 
<div> 
 <div> 
  <div> 
   <pre><span style="color:#595959"><span style="color:#595959"><span style="color:#d73a49">var</span> <span style="color:#005cc5">ctx</span> <span style="color:#d73a49">=</span> <span style="color:#595959">canvas</span>.<span style="color:#005cc5">getContext</span>(<span style="color:#669900">"2d"</span>);
</span></span><span style="color:#595959"><span style="color:#595959">
</span></span><span style="color:#595959"><span style="color:#595959"><span style="color:#595959">ctx</span>.<span style="color:#005cc5">fillStyle</span> <span style="color:#d73a49">=</span> <span style="color:#669900">'white'</span>;
</span></span><span style="color:#595959"><span style="color:#595959"><span style="color:#595959">ctx</span>.<span style="color:#005cc5">strokeStyle</span> <span style="color:#d73a49">=</span> <span style="color:#669900">'blue'</span>;
</span></span><span style="color:#595959"><span style="color:#595959">
</span></span><span style="color:#595959"><span style="color:#595959"><span style="color:#595959">ctx</span>.<span style="color:#005cc5">fillRect</span>(<span style="color:#005cc5">0</span>, <span style="color:#005cc5">0</span>, <span style="color:#595959">canvas</span>.<span style="color:#005cc5">width</span>, <span style="color:#595959">canvas</span>.<span style="color:#005cc5">height</span>);
</span></span><span style="color:#595959"><span style="color:#595959">
</span></span><span style="color:#595959"><span style="color:#595959"><span style="color:#595959">ctx</span>.<span style="color:#005cc5">beginPath</span>();
</span></span><span style="color:#595959"><span style="color:#595959"><span style="color:#595959">ctx</span>.<span style="color:#005cc5">arc</span>(<span style="color:#005cc5">75</span>, <span style="color:#005cc5">75</span>, <span style="color:#005cc5">50</span>, <span style="color:#005cc5">0</span>, <span style="color:#595959">Math</span>.<span style="color:#005cc5">PI</span> <span style="color:#d73a49">*</span> <span style="color:#005cc5">2</span>, <span style="color:#990055">true</span>); <span style="color:#6a737d">// Outer circle</span>
</span></span><span style="color:#595959"><span style="color:#595959"><span style="color:#595959">ctx</span>.<span style="color:#005cc5">moveTo</span>(<span style="color:#005cc5">110</span>, <span style="color:#005cc5">75</span>);
</span></span><span style="color:#595959"><span style="color:#595959"><span style="color:#595959">ctx</span>.<span style="color:#005cc5">arc</span>(<span style="color:#005cc5">75</span>, <span style="color:#005cc5">75</span>, <span style="color:#005cc5">35</span>, <span style="color:#005cc5">0</span>, <span style="color:#595959">Math</span>.<span style="color:#005cc5">PI</span>, <span style="color:#990055">false</span>);  <span style="color:#6a737d">// Mouth (clockwise)</span>
</span></span><span style="color:#595959"><span style="color:#595959"><span style="color:#595959">ctx</span>.<span style="color:#005cc5">moveTo</span>(<span style="color:#005cc5">65</span>, <span style="color:#005cc5">65</span>);
</span></span><span style="color:#595959"><span style="color:#595959"><span style="color:#595959">ctx</span>.<span style="color:#005cc5">arc</span>(<span style="color:#005cc5">60</span>, <span style="color:#005cc5">65</span>, <span style="color:#005cc5">5</span>, <span style="color:#005cc5">0</span>, <span style="color:#595959">Math</span>.<span style="color:#005cc5">PI</span> <span style="color:#d73a49">*</span> <span style="color:#005cc5">2</span>, <span style="color:#990055">true</span>);  <span style="color:#6a737d">// Left eye</span>
</span></span><span style="color:#595959"><span style="color:#595959"><span style="color:#595959">ctx</span>.<span style="color:#005cc5">moveTo</span>(<span style="color:#005cc5">95</span>, <span style="color:#005cc5">65</span>);
</span></span><span style="color:#595959"><span style="color:#595959"><span style="color:#595959">ctx</span>.<span style="color:#005cc5">arc</span>(<span style="color:#005cc5">90</span>, <span style="color:#005cc5">65</span>, <span style="color:#005cc5">5</span>, <span style="color:#005cc5">0</span>, <span style="color:#595959">Math</span>.<span style="color:#005cc5">PI</span> <span style="color:#d73a49">*</span> <span style="color:#005cc5">2</span>, <span style="color:#990055">true</span>);  <span style="color:#6a737d">// Right eye</span>
</span></span><span style="color:#595959"><span style="color:#595959"><span style="color:#595959">ctx</span>.<span style="color:#005cc5">stroke</span>(); </span></span></pre> 
  </div> 
 </div> 
</div> 
<p>最后，如果您希望更新在3D渲染中立即可见，则应该将画布纹理标记为动态</p> 
<div> 
 <div> 
  <div> 
   <pre><span style="color:#595959"><span style="color:#595959"><span style="color:#595959">canvasTex</span>.<span style="color:#005cc5">needsUpdate</span> <span style="color:#d73a49">=</span> <span style="color:#990055">true</span>;</span></span>
</pre> 
  </div> 
 </div> 
</div> 
<h2>新拼图</h2> 
<p>将拼图库中的<strong>Misc(杂项)</strong>类重命名为了<strong>Advanced(高级)</strong>，并在此类中新增<strong>wait promise</strong>和<strong>promise value</strong>拼图<strong>。</strong></p> 
<p>可以使用这些拼图取回来自<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FPromise" target="_blank">JavaScript promises</a> 中检索的数据，这些数据由<strong>generate normal map(生成法线贴图)</strong>和<strong>export glTF(导出glTF)</strong>拼图返回。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-ab8b7d64128451ecdb1b4570e45e3abd2c6.JPEG" width="657" referrerpolicy="no-referrer"></p> 
<p>部署了新的<strong>Material(材质)</strong>拼图：<strong>get color(获取颜色)</strong>和<strong>get value(获取值)</strong>先前可用的<strong>set color(设置颜色)</strong>和<strong>set value(设置值)</strong>拼图在一起。</p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-7a372c818f3cb77a181523ec84b56a9edd0.JPEG" width="457" referrerpolicy="no-referrer"></p> 
<p>拼图<strong>get object transform(获取对象位移)</strong>现在可以使用列表同时检索三个坐标系信息。</p> 
<p style="text-align:center"> </p> 
<p style="text-align:center"><img alt="image" src="https://oscimg.oschina.net/oscnet/up-1ce4da67e3da02b1519b5774ece2218e9bd.JPEG" width="705" referrerpolicy="no-referrer"></p> 
<p>这个选项可以用于直接为矢量拼图提供输出。</p> 
<p style="text-align:center"><img alt height="104" src="https://oscimg.oschina.net/oscnet/up-05e8b98f395b0a52a79c2dd72a23a731cf8.JPEG" width="705" referrerpolicy="no-referrer"></p> 
<h2>JavaScript <span style="color:#313131">应用程序接口</span></h2> 
<p>现在在JavaScript方法 <code>Geometry.fromBufferGeometry()</code> 中可以正常使用顶点色了。</p> 
<p>新版提供了之前仅在企业版中提供的Verge3D运行时(run-time)变体<strong>v3d.module.js</strong>。这一方式修复了运行示例代码时遇到的大部分问题。</p> 
<p>如果需要在JavaScript代码中<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fimport" target="_blank">导入</a>声明，，可以使用此运行时。这个模块也简化了您在自己的编程项目中嵌入Verge3D代码的过程。</p> 
<h2>更多特性</h2> 
<p>在Verge3D WordPress插件中支持了WooCommerce的全局产品属性。此外，WordPress插件现在不会上载Maya场景文件（*.ma和*.mb），类似于Blender和3ds Max场景文件。</p> 
<p>为3.2版本中引入的高级代码合并功能做了进一步的改进、加速和稳定性优化。</p> 
<p>为引擎着色器代码做了一些代码清理和重构。</p> 
<p>在稳定中做了各种小的改进，包括修复失效链接、缺失的媒体文件等。</p> 
<h2>故障修复</h2> 
<p>修复了应用管理器中与应用更新功能相关的一些错误，同时提高了更新的稳定性。</p> 
<p>修复了退出应用时的内存泄漏错误。</p> 
<p>修复了论坛中上报使用JavaScript为对象指定自定义材质时的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.soft8soft.com%2Ftopic%2Fcannot-read-property-dispose-of-null%2F" target="_blank">崩溃问题</a>。</p> 
<p>修复了论坛中上报的create environment(创建环境)拼图出现的翻转<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.soft8soft.com%2Ftopic%2Fcreate-environment-puzzle-issuewrong-direction-of-the-background-texture%2F" target="_blank">问题</a>。</p> 
<h2>Verge3D 旗舰版</h2> 
<p>此次更新最终完结Verge3D 3.3 for Blender，3ds Max和Maya的新版本发布。因此，我们更新了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fverge3d.funjoy.tech%2Fshop%2Fproduct%2Fultimate-verge3d-24%23attr%3D" target="_blank">Verge3D旗舰版</a>，以同步这些版本的所有更新。</p> 
<h2>立即升级</h2> 
<p>一如既往，在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FK-AWZ8smyOUt1pm0lgmpzQ" target="_blank">Verge3D最新发行版下载</a>一文中获取最新预览版的百度盘分享链接吧！欢迎通过<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.soft8soft.com%2Fforums%2F" target="_blank">论坛</a>、微信公众号、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshang.qq.com%2Fwpa%2Fqunwpa%3Fidkey%3Dc31cf6597f3ed7ce68bd47aba6bba23049bf973ac6acc59b0a5a7d1bd933b3ea" target="_blank">QQ群</a>、<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Averge3d%40funjoy.tech" target="_blank">电子邮件</a>提出建议与意见！</p> 
<blockquote> 
 <p>发布时间：2020年7月29日<br> 下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fverge3d.funjoy.tech%2Fget-verge3d" target="_blank">https://verge3d.funjoy.tech/get-verge3d</a></p> 
</blockquote>
                                        </div>
                                      
</div>
            