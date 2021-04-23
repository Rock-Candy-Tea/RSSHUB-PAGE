
---
title: 'canvas深入浅出（一）_ 小测免费学'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d02bd6197c8498b85753cd63be7958a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 22 Apr 2021 17:10:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d02bd6197c8498b85753cd63be7958a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">背景</h4>
<p>canvas是为了解决页面只能显示静态图片而出现的一种可以使用JavaScript绘制的HTML标签，它可以接受两个参数width和height（原来有三个，还有一个<code>moz-opaque</code>控制透明度，已经废弃了）</p>
<p>注意事项：不同于img标签的自闭和，canvas必须要有闭合标签；能直接在canvas标签上设置宽高尽量直接在标签属性设置宽高，其次可以通过js来设置，尽量不要通过css样式来设置宽高，可能会出现拉伸等情况，这一点<a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Canvas_API/Tutorial/Basic_usage#%3Ccanvas%3E_%E5%85%83%E7%B4%A0" target="_blank" rel="nofollow noopener noreferrer">MDN</a>也给出了说明</p>
<blockquote>
<p><strong>注意:</strong> 如果你绘制出来的图像是扭曲的, 尝试用width和height属性为<code><canvas></code>明确规定宽高，而不是使用CSS。</p>
</blockquote>
<p>除了canvas之外你可能还会听过svg，svg是一种使用xml定义的<strong>矢量图</strong>，而canvas是使用JavaScript控制绘制出来的<strong>位图</strong></p>
<p><img alt="1487709-20190809150321714-50339721" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d02bd6197c8498b85753cd63be7958a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>由于主题是canvas，所以这里我们之说canvas，不聊svg</p>
<h4 data-id="heading-1">用途</h4>
<p>canvas最常用的功能是用来绘制图表，比如我们常用的ECharts图标库底层就是使用的canvas，我手上最近的一个项目中就用到了ECharts</p>
<p><img alt="QQ截图20210420183619-3" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca2e6a692e4b4bbe801c988f772e68b0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这是他的DOM文档体现</p>
<p><img alt="QQ截图20210420183634-4" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b1b4f71466c41758932b5af210ae4d8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>由于是通过JavaScript驱动绘制的，所以数据都是可以动态传入的，这是静态图片（jpg/png……）所无法比拟的</p>
<p>此外canvas可以用来制作游戏，这是我以前玩过的魔方游戏（虽然体验完全不如实体）</p>
<p><img alt="QQ截图20210420184354-5" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae7582f1135a4e938bb13bd2aab00d36~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>还可以用来做活动页面，很多商家都会用这种形式来做营销活动</p>
<p><img alt="QQ截图20210420184651-6" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53173c19895e456baaef1d6de3085289~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>你可能还会再某些博客中看到这样的特效，他也是canvas实现的</p>
<p><img alt="QQ截图20210420185247-7" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e6bb742a42c44eebb99391769b94870~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">基本用法</h4>
<p>收先需要在HTML文档中声明canvas标签，标签可以添加后备内容，以防止浏览器不兼容canvas，后备内容可以是一串文本、一张图片或者是动态提娜佳的内容</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"canvas"</span>></span>
很遗憾你的浏览器不支持canvas
<span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>

<span class="hljs-tag"><<span class="hljs-name">canvas</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"canvas"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./img.png"</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">canvas</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在使用canvas之前，我们需要获取canvas的上下文</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> canvas = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'canvas'</span>) 
<span class="hljs-comment">// 标注id属性的元素会自动创建全居变量，可以直接使用id操作，但是不推荐</span>
<span class="hljs-keyword">const</span> context = canvas.getContext(<span class="hljs-string">'2d'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上下文的类型有三种，分别是</p>
<ul>
<li>2d（本小册所有的示例都是 2d 的）：代表一个二维渲染上下文</li>
<li>webgl（或"experimental-webgl"）：代表一个三维渲染上下文</li>
<li>webgl2（或"experimental-webgl2"）：代表一个三维渲染上下文；这种情况下只能在浏览器中实现 WebGL 版本2 (OpenGL ES 3.0)</li>
</ul>
<p>在获取路径之后，我们就可以通过上下文的api来进行绘制路径了，比如你可以使用context.arc(x, y, r,angle1, angle2, direction)来绘制一个圆，其中参数的含义为：</p>
<ul>
<li>x：圆心x坐标</li>
<li>y：圆心y坐标</li>
<li>r：半径</li>
<li>angle1：起始角度，默认水平向右，也就是三点钟</li>
<li>angle2：结束角度，从开始角度旋转的度数</li>
<li>direction：旋转方向，true是逆时针，false是顺时针</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">context.beginPath();       <span class="hljs-comment">// 起始一条路径，或重置当前路径</span>
context.arc(<span class="hljs-number">100</span>, <span class="hljs-number">100</span>, <span class="hljs-number">50</span>, <span class="hljs-number">0</span>, <span class="hljs-built_in">Math</span>.PI * <span class="hljs-number">2</span>, <span class="hljs-literal">true</span>);  <span class="hljs-comment">// 曲线</span>
context.closePath();       <span class="hljs-comment">// 闭合曲线</span>
context.fillStyle = <span class="hljs-string">'rgb(0,0,0)'</span>; <span class="hljs-comment">// 设置填充样式</span>
context.fill();            <span class="hljs-comment">// 填充</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下</p>
<p><img alt="Dingtalk_20210421122914-8" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85edd47277c340d6aa79febe100ad577~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这一节我们大体介绍了canvas的用途，下一节开始我们就开始讲解canvas的具体使用</p>
<p>本文正在参与「掘金小册免费学啦！」活动, 点击查看<a href="https://juejin.cn/post/6943533938090442765" target="_blank">活动详情</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            