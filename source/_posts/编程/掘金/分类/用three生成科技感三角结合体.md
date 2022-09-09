
---
title: '用three生成科技感三角结合体'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b44940ab7d44c6d9ec4321238968f3d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 03:03:07 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b44940ab7d44c6d9ec4321238968f3d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>在正文的第一句加入“我正在参加「码上掘金挑战赛」详情请看：<a href="https://juejin.cn/post/7139728821862793223" title="https://juejin.cn/post/7139728821862793223" target="_blank">码上掘金挑战赛来了！</a>”</p>
</blockquote>
<p>主要是用到了three.js BufferGeometry这方法，我是在本地启动的服务，所以就不贴官网链接了，</p>
<p>BufferGeometry是面片、线或点几何体的有效表述。包括顶点位置，面片索引、法相量、颜色值、UV 坐标和自定义缓存属性值。使用 BufferGeometry 可以有效减少向 GPU 传输上述数据所需的开销。(官网的解释)
这是截图</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b44940ab7d44c6d9ec4321238968f3d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="three10.png" loading="lazy" referrerpolicy="no-referrer">
主要规则就是三点创建一个平面和两点创建一条线</p>
<p>创建场景</p>
<pre><code class="hljs language-ini copyable" lang="ini">const <span class="hljs-attr">scene</span> = new THREE.Scene()<span class="hljs-comment">;</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建相机</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// 创建相机(透视相机)</span>
<span class="hljs-keyword">const</span> camera = <span class="hljs-keyword">new</span> THREE.PerspectiveCamera(
    <span class="hljs-number">75</span>, <span class="hljs-comment">// 摄像机角度</span>
    <span class="hljs-built_in">window</span>.innerWidth/<span class="hljs-built_in">window</span>.innerHeight, <span class="hljs-comment">// 宽高比</span>
    <span class="hljs-number">0.1</span>,<span class="hljs-comment">// 最近位置</span>
    <span class="hljs-number">1000</span>, <span class="hljs-comment">// 最远位置</span>
); <span class="hljs-comment">// </span>

<span class="hljs-comment">// 相机位置</span>
camera.position.<span class="hljs-keyword">set</span>(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">10</span>) <span class="hljs-comment">// x y z</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比较麻烦的就是创建物体 我们要创建50个三角形物体</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 创建50个物体</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<<span class="hljs-number">50</span>;i++) &#123;
    <span class="hljs-comment">// 50个物体，一个面有三个点，一个点的坐标是xyz</span>
    <span class="hljs-keyword">const</span> geometry = <span class="hljs-keyword">new</span> <span class="hljs-variable constant_">THREE</span>.<span class="hljs-title class_">BufferGeometry</span>(); <span class="hljs-comment">// 创建 BufferGeometry界面</span>
    
    <span class="hljs-keyword">const</span> positionArray = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Float32Array</span>(<span class="hljs-number">9</span>);  <span class="hljs-title class_">Float32Array</span>类型数组需要指定长度才可以
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> j=<span class="hljs-number">0</span>;j<<span class="hljs-number">9</span>;j++) &#123; <span class="hljs-comment">// 三个点的坐标</span>
        positionArray[j] = <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">random</span>()*<span class="hljs-number">10</span> -<span class="hljs-number">5</span> <span class="hljs-comment">// 0-5</span>
    &#125;
    <span class="hljs-comment">// 设置点坐标及绘画面</span>
    geometry.<span class="hljs-title function_">setAttribute</span>(<span class="hljs-string">'position'</span>, <span class="hljs-keyword">new</span> <span class="hljs-variable constant_">THREE</span>.<span class="hljs-title class_">BufferAttribute</span>( positionArray, <span class="hljs-number">3</span> ) );
    <span class="hljs-keyword">let</span> color = <span class="hljs-keyword">new</span> <span class="hljs-variable constant_">THREE</span>.<span class="hljs-title class_">Color</span>(<span class="hljs-title class_">Math</span>.<span class="hljs-title function_">random</span>(),<span class="hljs-title class_">Math</span>.<span class="hljs-title function_">random</span>(),<span class="hljs-title class_">Math</span>.<span class="hljs-title function_">random</span>()) <span class="hljs-comment">// 随机颜色</span>
    <span class="hljs-keyword">const</span> cun = <span class="hljs-keyword">new</span> <span class="hljs-variable constant_">THREE</span>.<span class="hljs-title class_">MeshBasicMaterial</span>(&#123; <span class="hljs-comment">// 材质</span>
       <span class="hljs-attr">color</span>: color, 
       <span class="hljs-attr">transparent</span>: <span class="hljs-literal">true</span>,
       <span class="hljs-attr">opacity</span>: <span class="hljs-number">0.5</span>

    &#125;) 
    <span class="hljs-keyword">const</span> cube = <span class="hljs-keyword">new</span> <span class="hljs-variable constant_">THREE</span>.<span class="hljs-title class_">Mesh</span>(geometry,cun)
    scene.<span class="hljs-title function_">add</span>(cube);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>渲染器</p>
<pre><code class="hljs language-scss copyable" lang="scss">const renderer = new THREE<span class="hljs-selector-class">.WebGL1Renderer</span>();
<span class="hljs-comment">// 设置渲染尺寸大小</span>
renderer<span class="hljs-selector-class">.setSize</span>(window.innerWidth,window.innerHeight);
<span class="hljs-comment">// 渲染器添加到canvas画布</span>
document<span class="hljs-selector-class">.body</span><span class="hljs-selector-class">.appendChild</span>(renderer.domElement) <span class="hljs-comment">// 把body上追加</span>
function <span class="hljs-built_in">render</span>() &#123;

    renderer<span class="hljs-selector-class">.render</span>(scene,camera)
    <span class="hljs-comment">// 渲染下一桢</span>
    <span class="hljs-built_in">requestAnimationFrame</span>(render)
&#125;
<span class="hljs-built_in">render</span>()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实这个在three的官网也有相对应的demo，但是比我的这个复杂，这个只是简版，但是也相对简单好理解</p>
<p>代码块</p>
<p><span href="https://code.juejin.cn/pen/7140959969578483748" target="_blank" class="code-editor-container"><iframe class="code-editor-frame" data-code="code-editor-element" data-code-id="7140959969578483748" data-src="https://code.juejin.cn/pen/7140959969578483748" style="display: none" loading="lazy"></iframe></span></p></div>  
</div>
            