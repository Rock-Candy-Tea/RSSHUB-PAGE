
---
title: '我想与你讨论一下Canvas2D 与WebGL'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f49d332cda9849329583bd04000a1894~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 06:12:04 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f49d332cda9849329583bd04000a1894~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">背景</h1>
<p>本篇收录于<a href="https://juejin.cn/column/6966134135991566344" target="_blank">《数据可视化和图形学》</a>专栏</p>
<p>上文谈到在 纠结 中砥砺前行,写下了第一篇专栏文章对于图形学和可视化的认知篇 实现了一个简单的程序。本来打算后续序列已算法和渲染方向为主.但是综合微信/QQ圈内同学反馈晦涩问题 后续文章更多已结论(小节产生效果)为导向进行展开学习。</p>
<blockquote>
<p>本篇不会讨论canvas与webGL的区别  相信大家都懂...</p>
</blockquote>
<h3 data-id="heading-1">本篇大纲</h3>
<ol>
<li>Canvas与WebGL简介</li>
<li>会canvas不会WebGL?俩者如何下手</li>
<li>canvas的API如何用WebGL实现(比较区别)</li>
<li>大道志远,潜心修行(后续大纲)</li>
</ol>
<h2 data-id="heading-2">1. Canvas 2D与WebGL简介</h2>
<h3 data-id="heading-3">Canvas 2D</h3>
<p><strong>基本概念:</strong></p>
<p>Canvas API 提供了一个通过JavaScript 和 HTML的元素来绘制图形的方式。它可以用于动画、游戏画面、数据可视化、图片编辑以及实时视频处理等方面。</p>
<p><strong>渲染(原理)流程:</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f49d332cda9849329583bd04000a1894~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>WebKit为例</p>
<ol>
<li>浏览器(JavaScript) canvas API</li>
<li>底层图形库 Skia(支持CPU/GPU绘制)</li>
<li>根据平台是否支持(策略) 选取绘制方式。</li>
</ol>
<p>可以参考一下WebKit中用来支持Canvas的类(本文不做展开)
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aaf913d9c443475ca42ff1f34986ac84~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">WebGL</h3>
<p><strong>基本概念:</strong>
WebGL（Web图形库）是一个JavaScript API，可在任何兼容的Web浏览器中渲染高性能的交互式3D和2D图形，而无需使用插件。WebGL通过引入一个与OpenGL ES 2.0非常一致的API来做到这一点，该API可以在HTML5 元素中使用。 这种一致性使API可以利用用户设备提供的<strong>硬件图形加速</strong>(与canvas 2D区别)。</p>
<p><strong>渲染(原理)流程:</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69eace7a764748e1bfd95bddd11264bc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>WebKit为例</p>
<ol>
<li>Shader/ res/texture/WebGL API</li>
<li>drawingBuffer (绘制缓冲区)</li>
<li>GL库/GPU绘制</li>
</ol>
<p>可以参考一下WebKit中用来支持Web的类(本文不做展开)
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa71a462887b4823a336d0537a51bcd7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">2. 会canvas不会WebGL?俩者如何下手</h2>
<h3 data-id="heading-6">回答问题为导向:</h3>
<ul>
<li>Canvas 2D API简单 WebGL API看不懂是为何</li>
<li>学习不知道如何入手?(API工程师?啃书?源码?)</li>
<li>...</li>
</ul>
<p>依此的简单回答:</p>
<ol>
<li>首先明白一点API越简单肯定越上层(上层直白来说发挥空间小,局限性大),为什么canvas 2D的API简单呢? 封装的完善 而且大部分工作隐藏在内核的实现上。 WebGL需要考虑shader,buffer,texture,program(程序),link(这块好像透明点)...总之就是难。多看看就好了。</li>
<li>学习这个话题太多人问了,拿我举例说也得看文档 coding 深入的话还得学习一些别人的产出。(直接看文献也是看别人的产出,没什么较真的) 没得办法。如果说那条路更简单的话,看别人的分享(需要是系统的分享 碎片化知识对于学习的路来说并没有多大帮助)。 看框架(库)实现源码什么的,那个也只是API的封装。看的反而怀疑人生 因为那个又牵扯一些别的知识,整体架构设计,数据模型,渲染,事件等等...</li>
<li>...留言讨论吧  有需要加微信也可以</li>
</ol>
<h2 data-id="heading-7">3.Canvas 2D的API如何用WebGL实现(比较区别)</h2>
<p>已一个简单的来学习一下,绘制一个矩形:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20ad6b758e3f47d7aa2e6ce7b9d86b27~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>canvas</p>
</blockquote>
<pre><code class="copyable">// html
<!-- 画布 -->
<canvas id="myDiagram" width="200" height="200"></canvas>

//js
// 获取canvas元素
var canvas = document.getElementById("canvas");
// 获取渲染上下文
var ctx = canvas.getContext("2d");
// 绘制样式  红色
ctx.fillStyle = "red";
// API 绘制rect
ctx.fillRect(10,10,100,100);
    
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>WebGL</p>
</blockquote>
<pre><code class="copyable">// html
<!-- 画布 -->
<canvas id="myDiagram" width="200" height="200"></canvas>
<span class="copy-code-btn">复制代码</span></code></pre>
   
<pre><code class="copyable"><script src="https://webglfundamentals.org/webgl/resources/webgl-utils.js"></script>



// js
// 获取渲染上下文
const gl = document.querySelector('#myDiagram').getContext('webgl');

// 顶点 vertex shader
const vs = `
// vertex shader
void main() &#123;
  gl_Position = vec4(0, 0, 0, 1);  // 坐标  gl_开头都为webgl内置变量
  gl_PointSize = 100.0;      // 大小
&#125; 
`;
//片元 fragment shader
const fs = `
// fragment shader
void main() &#123;
  gl_FragColor = vec4(0, 0, 0, 1);  // 颜色 红色
&#125;
`;

//  shader程序
const program = webglUtils.createProgramFromSources(gl, [vs, fs]);
// 使用 shader程序
gl.useProgram(program);

// offset 偏移 
const offset = 0;
// count 个数
const count = 1;
// gl.POINTS 内置绘制方式 
// 绘制函数 drawArrays 
gl.drawArrays(gl.POINTS, offset, count);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">4. 大道志远,潜心修行(后续大纲)</h2>
<blockquote>
<p>此处应该为填空题(给点意见吧 好难~), 简单说下我的想法吧  顺序待定....</p>
</blockquote>
<ol>
<li>WebGL渲染2D篇</li>
<li>WebGL渲染3D篇</li>
<li>渲染优化手段 quadTree(2d渲染) 3d渲染...</li>
<li>光照和阴影 RayCasting / RayTracing...</li>
<li>其他 (算法类,框架解读类...)</li>
</ol>
<h1 data-id="heading-9">最后</h1>
<blockquote>
<p>需要加微信群的请留言...我看到就会回复的  贴一下上文的一些链接。</p>
</blockquote>
<ol>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Canvas_API/Tutorial" target="_blank" rel="nofollow noopener noreferrer">  Canvas 2D 教程   </a></li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/WebGL_API/Tutorial/Getting_started_with_WebGL" target="_blank" rel="nofollow noopener noreferrer"> WebGL教程 </a></li>
<li><a href="https://blog.csdn.net/sauphy/article/details/49936525" target="_blank" rel="nofollow noopener noreferrer">WebKit之WebGL原理====写的蛮细的</a></li>
</ol></div>  
</div>
            