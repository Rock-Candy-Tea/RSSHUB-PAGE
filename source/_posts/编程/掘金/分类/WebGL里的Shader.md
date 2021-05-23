
---
title: 'WebGL里的Shader'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9634bb00e7cf4c6a9b365ce326de9ead~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 23 May 2021 02:44:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9634bb00e7cf4c6a9b365ce326de9ead~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">数据类型</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9634bb00e7cf4c6a9b365ce326de9ead~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">修饰符(WebGL1.0)</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/008a415cedc447d89cfd4a6f598cdcae~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">顶点着色器 预定义变量</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f03afa3e15df4be4bd64e6d7e02018a7~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">片段着色器 预定义变量</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/779bf440a1b24ac39145e491a6f9004c~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">Example</h2>
<p>WebGL1.0</p>
<pre><code class="hljs language-js copyable" lang="js">attribute vec4 a_position;  <span class="hljs-comment">//js一般输入的是 n组数组  每一数组大小跟声明有关</span>
uniform vec4 u_offset;      <span class="hljs-comment">//js一般输入的是 一组数组 这个数组大小跟声明有关 uniform这个可以在片元着色器写</span>
uniform float u_kernel[<span class="hljs-number">9</span>];  <span class="hljs-comment">//js一般输入的是 一组数组 这个数组大小跟声明有关</span>
varying vec4 v_positionWithOffset; <span class="hljs-comment">//只是用来传值 不用在js里输入</span>

attribute vec2 a_TexCoord;<span class="hljs-comment">//纹理坐标</span>
varying vec2 v_TexCoord;<span class="hljs-comment">//插值后纹理坐标</span>

<span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span> &#123;
  gl_Position = a_position + u_offset + u_kernel[<span class="hljs-number">0</span>];
  v_positionWithOffset = a_position + u_offset;
  v_TexCoord = a_TexCoord; <span class="hljs-comment">//一般不做处理</span>
&#125;

precision mediump float;
varying vec4 v_positionWithOffset;  <span class="hljs-comment">//要想使用的话 必须要有相同的声明</span>

struct SomeStruct &#123; <span class="hljs-comment">//自定义结构 不过很少这么用吧 声明两个变量比这实用点</span>
  bool active;
  vec2 someVec2;
&#125;;
uniform SomeStruct u_someThing;


uniform sampler2D u_Sampler;  <span class="hljs-comment">//贴图颜色来的</span>
varying vec2 v_TexCoord;  <span class="hljs-comment">//已经是0-1了</span>
<span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span> &#123;
  vec4 color = v_positionWithOffset * <span class="hljs-number">0.5</span> + <span class="hljs-number">0.5</span>
  gl_FragColor = texture2D(u_Sampler,v_TexCoord);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>WebGL2.0</p>
<pre><code class="hljs language-js copyable" lang="js">#version <span class="hljs-number">300</span> es
<span class="hljs-keyword">in</span> vec4 a_position;
<span class="hljs-keyword">in</span> vec2 a_TexCoord;<span class="hljs-comment">//纹理坐标</span>
out vec2 v_TexCoord;<span class="hljs-comment">//插值后纹理坐标</span>

<span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span> &#123;
   gl_Position = a_position;
   v_TexCoord = a_TexCoord; <span class="hljs-comment">//一般不做处理</span>
&#125;


#version <span class="hljs-number">300</span> es
precision highp float;
int vec2 vTexcoord; <span class="hljs-comment">//varing 已经被替代了</span>
out vec4 outColor;  <span class="hljs-comment">// you can pick any name</span>
uniform sampler2D uTexture;
<span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span> &#123;
   outColor = doMathToMakeAColor;
   gl_FragColor = texture2D(uTexture,v_TexCoord);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>-<a href="https://www.yiibai.com/webgl/webgl_shaders.html" target="_blank" rel="nofollow noopener noreferrer">着色器1</a></p></div>  
</div>
            