
---
title: 'HTML5+CSS3学习总结(完结)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f0e2211cfe44714b1066db740db834c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 21 Jul 2021 22:31:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f0e2211cfe44714b1066db740db834c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>前端小白简单总结，参考黑马课程以及其他内容整合，还望各位大佬多多指教~</p>
</blockquote>
<h3 data-id="heading-0">一、HTML5</h3>
<h4 data-id="heading-1">1）什么是HTML5</h4>
<h5 data-id="heading-2">1. HTML5简介</h5>
<p>万维网的核心语言、标准通用标记语言下的一个应用超文本标记语言(HTML)的第五次重大修改，作为HTML语言，具有新的元素、属性和行为。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f0e2211cfe44714b1066db740db834c~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-3">2. 广义的HTML5</h5>
<ul>
<li>广义的HTML5是HTML5本身 + CSS3 + JavaScript</li>
<li>这个集合有时称为HTML5和朋友，通常缩写为HTML5</li>
<li>虽然HTML5的一些特性仍然不被某些浏览器支持，但是它是一种发展趋势</li>
<li>HTML5 MDN介绍：</li>
</ul>
<h4 data-id="heading-4">2）H5新增语义化标签</h4>
<p>以前布局，我们基本用div来做，div对于搜索引擎来说，是没有语义的
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66c957f5610344639617962d266c5652~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-5">新增语义化标签</h5>
<ul>
<li><code>header</code>   ---  头部标签</li>
<li><code>nav</code>        ---  导航标签</li>
<li><code>article</code> ---   内容标签</li>
<li><code>section</code> ---   块级标签</li>
<li><code>aside</code>     ---   侧边栏标签</li>
<li><code>footer</code>   ---   尾部标签</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee35123c02894a57b480b508b9cf5d22~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><strong>注意</strong></p>
<ul>
<li>这种语义化标签主要针对<strong>搜索引擎</strong>的</li>
<li>这些新标签在页面中可以使用<strong>多次</strong></li>
<li>在 <code>IE9</code> 浏览器中，需要把这些语义化标签都转换为<strong>块级元素</strong></li>
<li>语义化标签，在移动端支持比较友好</li>
</ul>
</blockquote>
<h4 data-id="heading-6">3）H5新增多媒体标签</h4>
<p>多媒体标签包含两个：</p>
<ul>
<li>音频：<audio></li>
<li>视频：<video></li>
</ul>
<p>使用它们可以很方便的在页面中嵌入音频和视频，而不再去使用落后的flash和其他浏览器插件。</p>
<h5 data-id="heading-7">1. <audio>音频标签</h5>
<p>HTML5在不使用插件的情况下也可以原生的支持音频格式文件的播放，当然支持格式是有限的。</p>
<ul>
<li>音频格式</li>
</ul>
<p>当前， <audio>元素支持三种音频格式：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06dc429b2d304ec29f61269d6f60f9a1~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
语法格式：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">audio</span> <span class="hljs-attr">src</span>=<span class="hljs-string">'media/test.mp3 '</span> <span class="hljs-attr">controls</span>=<span class="hljs-string">'controls'</span>></span><span class="hljs-tag"></<span class="hljs-name">audio</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为不同浏览器支持不同格式，我们采取的解决方案是我们为这个音频准备多个格式</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 谷歌浏览器把autoplay属性给我们禁用了 --></span>
<span class="hljs-tag"><<span class="hljs-name">audio</span> <span class="hljs-attr">controls</span>=<span class="hljs-string">"controls"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">source</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"media/test.mp3"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"audio/mpeg"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">source</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"media/test.mp3"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"audio/ogg"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">audio</span>></span>
您的浏览器不支持audio标签播放音频
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">2. <video>视频标签</h5>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fc6e1a662b542b7916df713f03237f1~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>语法格式：</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">video</span> <span class="hljs-attr">src</span>=<span class="hljs-string">'media/video.mp4 '</span> <span class="hljs-attr">controls</span>=<span class="hljs-string">'controls'</span>></span><span class="hljs-tag"></<span class="hljs-name">video</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 谷歌浏览器把autoplay属性给我们禁用了 有解决方案：给视频添加静音属性--></span>
<span class="hljs-tag"><<span class="hljs-name">video</span> <span class="hljs-attr">muted</span> = <span class="hljs-string">"muted"</span> <span class="hljs-attr">loop</span> = <span class="hljs-string">"loop"</span> <span class="hljs-attr">poster</span>=<span class="hljs-string">"media/pig.jpg"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">source</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"media/move.ogg"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"video/mpeg"</span>/></span>
<span class="hljs-tag"><<span class="hljs-name">source</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"media/move.mp4"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"video/ogg"</span>/></span>
<span class="hljs-tag"></<span class="hljs-name">video</span>></span>
您的浏览器不支持video标签播放视频
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><video>视频标签常见属性</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad02b54c190b4035bd22fa6bf125c74e~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
3. 总结：</p>
<ul>
<li>音频标签和视频标签使用基本一致</li>
<li>浏览器支持情况不同</li>
<li>谷歌浏览器把音频和视频自动播放禁止了</li>
<li>我们可以给视频标签添加muted属性可以自定义播放视频，音频不可以</li>
<li>视频标签是重点，我们经常设置自动播放，不使用controls控件，循环和设置大小属性</li>
</ul>
<h4 data-id="heading-9">4）、HTML5新增input表单、表单属性</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61366fcd0cda4f4792ba067b646db192~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>邮箱：<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"email"</span> /></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>网址：<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"url"</span> /></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>日期：<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"date"</span> /></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>时间：<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"date"</span> /></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>数量：<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"number"</span> /></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>手机号码：<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"tel"</span> /></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>搜索：<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"search"</span> /></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>颜色：<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"color"</span> /></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"submit"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"提交"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d48a5a74558644bc911bb63ae02aa7f2~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f208d1623d74cf1b7c1170c9d55c3ea~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">action</span>=<span class="hljs-string">""</span>></span>
用户名：<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">required</span>=<span class="hljs-string">"required"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"请输入用户名"</span> <span class="hljs-attr">autofocus</span>=<span class="hljs-string">"autofocus"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"username"</span> <span class="hljs-attr">autocomplete</span>=<span class="hljs-string">"off"</span> ></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"submit"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"提交"</span>></span>
上传头像：<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"file"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">""</span> <span class="hljs-attr">id</span>=<span class="hljs-string">""</span> <span class="hljs-attr">multiple</span>=<span class="hljs-string">"multiple"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d0d61318b6c4ceebf121e102d5e1eff~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">二、CSS3</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40514bb235234439862f3495ae8233c4~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">CSS3现状</h4>
<ul>
<li>在CSS2的基础上新增（扩展）样式</li>
<li>移动端支持优于PC端</li>
<li>不断改进中</li>
<li>应用相对广泛</li>
</ul>
<h4 data-id="heading-12">1. CSS3属性(结构)选择器</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdae14aeb39d4090a16cbfa68fb473af~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-13">2. CSS3结构伪类选择器</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ebe898882cd48a5b2df6c2bf0d10958~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
nth-child 详解</p>
<ul>
<li>
<p>注意：本质上就是选中第几个子元素</p>
</li>
<li>
<p>n 可以是数字、关键字、公式</p>
</li>
<li>
<p>n 如果是数字，就是选中第几个</p>
</li>
<li>
<p>常见的关键字有 <code>even</code> 偶数、<code>odd</code> 奇数</p>
</li>
<li>
<p>常见的公式如下(如果 n 是公式，则从 0 开始计算)</p>
</li>
<li>
<p>但是第 0 个元素或者超出了元素的个数会被忽略</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fe5a998e1b64b56996c215630f64743~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<code>nth-child</code> 和  <code>nt-of-type</code> 的区别</p>
<ul>
<li><code>nth-child</code>  选择父元素里面的第几个子元素，不管是第几个类型</li>
<li><code>nt-of-type</code>  选择指定类型的元素</li>
</ul>
<h4 data-id="heading-14">3. CSS3伪元素选择器</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbce1ed97c0e40c69b85623e20b2793e~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
注意事项：</p>
<ul>
<li><code>before</code> 和 <code>after</code> 必须有 <code>content</code> 属性</li>
<li><code>before</code> 在内容前面，after 在内容后面</li>
<li><code>before</code> 和 <code>after</code> 创建的是一个元素，但是属于行内元素</li>
<li>创建出来的元素在 <code>Dom</code> 中查找不到，所以称为伪元素</li>
<li>伪元素和标签选择器一样，权重为 1</li>
</ul>
<p>典型应用：
添加字体图标</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">p</span> &#123;
   <span class="hljs-attribute">width</span>: <span class="hljs-number">220px</span>;
   <span class="hljs-attribute">height</span>: <span class="hljs-number">22px</span>;
   <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid lightseagreen;
   <span class="hljs-attribute">margin</span>: <span class="hljs-number">60px</span>;
   <span class="hljs-attribute">position</span>: relative;
&#125;
<span class="hljs-selector-tag">p</span><span class="hljs-selector-pseudo">::after</span> &#123;
  <span class="hljs-attribute">content</span>: <span class="hljs-string">'\ea50'</span>;
  <span class="hljs-attribute">font-family</span>: <span class="hljs-string">'icomoon'</span>;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">top</span>: -<span class="hljs-number">1px</span>;
  <span class="hljs-attribute">right</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">4. CSS3过渡(非常重要)</h4>
<p>过渡动画：是从一个状态渐渐的过渡到另外一个状态，IE9以下不支持，经常和:hover一起搭配使用
语法格式：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">transition</span>:要过渡的属性 花费时间 运动曲线 何时开始
<span class="copy-code-btn">复制代码</span></code></pre>




























































<table><thead><tr><th>属性</th><th>描述</th><th>CSS</th></tr></thead><tbody><tr><td>transition</td><td>简写属性，用于在一个属性中设置四个过渡属性。</td><td>3</td></tr><tr><td>transition-property</td><td>规定应用过渡的 CSS 属性的名称。属性就是你想要变化的 css 属性，  宽度高度 背景颜色 内外边距都可以 。如果想要所有的属性都变化过渡， 写一个all 就可以。</td><td>3</td></tr><tr><td>transition-duration</td><td>定义过渡效果花费的时间(必须写单位)。默认是 0。</td><td>3</td></tr><tr><td>transition-timing-function</td><td>规定过渡效果的时间曲线。默认是 "ease"。</td><td>3</td></tr><tr><td>transition-delay</td><td>规定过渡效果何时开始，可以设置 延迟触发时间。默认是 0，鼠标触发就立即开始。</td><td>3</td></tr><tr><td>运动曲线示意图：</td><td></td><td></td></tr><tr><td><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d21b7fe921345848cb761a0c00f5131~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></td><td></td><td></td></tr><tr><td>样例：</td><td></td><td></td></tr><tr><td>```css</td><td></td><td></td></tr><tr><td>div &#123;</td><td></td><td></td></tr></tbody></table>
<pre><code class="copyable">width: 200px;
height: 100px;
background-color: pink;
/* transition: 要过渡的属性  花费时间  运动曲线  何时开始; */
/* transtion 过渡的意思  这句话写到div里面而不是 hover里面 
过渡写到本身上，谁做动画，给谁加*/
transition: width 0.6s ease 0s, height 0.3s ease-in 1s;



<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;
div:hover &#123;  /* 鼠标经过盒子，我们的宽度变为400 */</p>
<pre><code class="copyable">width: 600px;
height: 300px
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>transition: all 0.6s;  /* 所有属性都变化用all 就可以了  后面俩个属性可以省略 */</p>
<pre><code class="copyable">常见效果：
  按钮变换底色     图片移动      小米效果 （阴影效果）   传智导航栏效果 等等
#### 5. CSS3 2D转换
**转换**（transform）是CSS3中具有颠覆性的特征之一，可以实现元素的位移、旋转、缩放等效果。
转换（transform）可以简单理解为变形
- 移动：translate
- 旋转：rotate
- 缩放：scale
##### 1）二维坐标系
2D转换是改变标签在二维平面上的位置和形状的一种技术，
![在这里插入图片描述](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/001e34182aaf4d649e746a592bf9f778~tplv-k3u1fbpfcp-zoom-1.image)
##### 2）2D转换之移动translate
2D移动是2D转换里的一种功能，可以改变元素在页面中的位置，类似**定位**
![在这里插入图片描述](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2a8fecaecf5460f879e5c62283f8a0d~tplv-k3u1fbpfcp-zoom-1.image)
1. 语法：
```css
transform: translate(x, y);
            /* 或者分开写 */
    transform: translateX(x);
    transform: translateY(y);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>重点</li>
</ol>
<ul>
<li>定义2D转换中的移动，沿着X和Y轴移动元素</li>
<li>translate最大的优点：不会影响到其他元素的位置</li>
<li>translate中的百分比单位是相对于自身元素的translate:(50%, 50%);</li>
<li>对行内标签没有效果</li>
</ul>
<h5 data-id="heading-16">3）2D转换之旋转rotate</h5>
<p>2D旋转指的是让元素在2维平面内顺时针旋转或者逆时针旋转。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cebd0b0445a04e84b3031bcb4297e056~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>语法</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(度数);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>重点</li>
</ol>
<ul>
<li>rotate里面跟度数，单位是deg比如rotate(45deg)</li>
<li>角度为正时为顺时针，负时为逆时针</li>
<li>默认旋转的中心点是元素的中心点</li>
</ul>
<h5 data-id="heading-17">案例：三角形</h5>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f597674681494e7e88aabca1f1be70d5~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>三角形<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">div</span> &#123;
            <span class="hljs-attribute">position</span>: relative;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">249px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">35px</span>;
            <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#000</span>;
        &#125;
        
        <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">::after</span> &#123;
            <span class="hljs-attribute">content</span>: <span class="hljs-string">""</span>;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">top</span>: <span class="hljs-number">8px</span>;
            <span class="hljs-attribute">right</span>: <span class="hljs-number">15px</span>;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">10px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">10px</span>;
            <span class="hljs-attribute">border-bottom</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#000</span>;
            <span class="hljs-attribute">border-right</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#000</span>;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">45deg</span>);
            <span class="hljs-attribute">transition</span>: all <span class="hljs-number">0.2s</span>;
        &#125;
        <span class="hljs-comment">/* 鼠标经过div 里面的三角旋转 */</span>
        <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:hover</span><span class="hljs-selector-pseudo">::after</span> &#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">225deg</span>);
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>结果如图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eaf324367f9643b1bbe0b9cdbe504df6~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h5 data-id="heading-18">4）2D转换中心点transform-origin</h5>
<p>我们可以设置元素转换的中心点</p>
<ol>
<li>语法</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">transform-origin</span>: x y;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>重点</li>
</ol>
<ul>
<li>注意后面的参数x和y用空格隔开</li>
<li>x y默认的中心点是元素的中心点（50% 50%）</li>
<li>还可以给x y设置像素或者方位名词（top bottom left right center）</li>
</ul>
<h5 data-id="heading-19">案例：旋转案例</h5>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>旋转案例<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">div</span> &#123;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
            <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid pink;
            <span class="hljs-attribute">margin</span>: <span class="hljs-number">100px</span> auto;
            <span class="hljs-attribute">overflow</span>: hidden;
        &#125;
        
        <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">::before</span> &#123;
            <span class="hljs-attribute">content</span>: <span class="hljs-string">"黑马"</span>;
            <span class="hljs-attribute">display</span>: block;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
            <span class="hljs-attribute">background-color</span>: lightgreen;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">180deg</span>);
            <span class="hljs-attribute">transform-origin</span>: left bottom;
            <span class="hljs-attribute">transition</span>: all <span class="hljs-number">0.2s</span>;
        &#125;
        <span class="hljs-comment">/* 鼠标经过div 里面的before复原 */</span>
        
        <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:hover</span><span class="hljs-selector-pseudo">::before</span> &#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0deg</span>);
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>结果如图：</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/796a7e50572d4f66a511bd0fdd3a84bb~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cb0fb9c38de4afc85fcfd8ace6e01ab~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-20">5）2D转换之缩放scale</h5>
<p>可以放大和缩小，只要给元素添加上了这个属性就能控制它放大还是缩小
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93f7963482de411391d5efc6f3b0c867~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>语法</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(x, y);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>注意</li>
</ol>
<ul>
<li>注意其中的x和y用逗号分隔，里面的数字不跟单位就是倍数</li>
<li>transform: scale(1, 1)：宽和高都放大一倍，相当于没有放大</li>
<li>transform: scale(2, 2)：宽和高都放大了2倍</li>
<li>transform: scale(2)：只写一个参数，第二个参数则和第一个参数一样</li>
<li>transform: scale(0.5, 0.5)：缩小</li>
<li>scale缩放最大的优势：可以设置转换中心点缩放，默认以中心点缩放的，而且不影响其他盒子</li>
</ul>
<h5 data-id="heading-21">案例：图片放大</h5>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>图片放大<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">div</span> &#123;
            <span class="hljs-attribute">overflow</span>: hidden;
            <span class="hljs-attribute">float</span>: left;
            <span class="hljs-attribute">margin</span>: <span class="hljs-number">10px</span>;
        &#125;
        
        <span class="hljs-selector-tag">div</span> <span class="hljs-selector-tag">img</span> &#123;
            <span class="hljs-attribute">transition</span>: all .<span class="hljs-number">4s</span>;
        &#125;
        
        <span class="hljs-selector-tag">div</span> <span class="hljs-selector-tag">img</span><span class="hljs-selector-pseudo">:hover</span> &#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">1.1</span>);
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"media/scale.jpg"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span><span class="hljs-tag"></<span class="hljs-name">a</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"media/scale.jpg"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span><span class="hljs-tag"></<span class="hljs-name">a</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"media/scale.jpg"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span><span class="hljs-tag"></<span class="hljs-name">a</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>结果如图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8227ec4acf184710b71ec6299c513a67~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h5 data-id="heading-22">案例：分页按钮</h5>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>分页按钮案例<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">li</span> &#123;
            <span class="hljs-attribute">float</span>: left;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">30px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">30px</span>;
            <span class="hljs-attribute">line-height</span>: <span class="hljs-number">30px</span>;
            <span class="hljs-attribute">text-align</span>: center;
            <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">10px</span>;
            <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">20px</span>;
            <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
            <span class="hljs-attribute">list-style</span>: none;
            <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid green;
            <span class="hljs-attribute">cursor</span>: pointer;
            <span class="hljs-attribute">transition</span>: all .<span class="hljs-number">4s</span>;
        &#125;
        
        <span class="hljs-selector-tag">li</span><span class="hljs-selector-pseudo">:hover</span> &#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">1.2</span>);
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>3<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>4<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>5<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>6<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span>7<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>结果如图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c675e2e809564b30925d3060161218d0~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h5 data-id="heading-23">6）2D转换综合写法</h5>
<p>注意：</p>
<ol>
<li>同时使用多个转换，其格式为：transform: translate() rotate() scale()……等</li>
<li>其顺序会影响转换的效果（先旋转会改变坐标轴的方向）</li>
<li><strong>当我们同时有位移和其他属性的时候，记得要将位移放到最前面</strong></li>
</ol>
<h4 data-id="heading-24">6. CSS3动画</h4>
<p>动画（animation）是CSS3中具有颠覆性的特征之一，可通过设置多个节点来精确控制一个或一组动画，常用来实现复杂的动画效果。
相比较过渡，动画可以实现更多的变化，更多的控制，连续自动播放等效果。</p>
<h6 data-id="heading-25">1）动画的基本使用</h6>
<p>制作动画分为两步：</p>
<ol>
<li>先用keyframes定义动画(类似定义类选择器)</li>
</ol>
<p>动画序列</p>
<ul>
<li>0%是动画的<strong>开始</strong>，100%是动画的<strong>完成</strong>，这样的规则就是动画序列</li>
<li>在**@keyframes**中规定某项CSS样式，就能创建由当前样式逐渐改为新样式的动画效果</li>
<li>动画是使元素从一种样式逐渐便化为另一种样式的效果，你可以改变任意多的样式任意多的<strong>次数</strong>。</li>
<li>请用百分比来规定变化发生的时间，或用关键词 " <strong>form</strong> " 和  '' <strong>to</strong> " ，等同于<strong>0%<strong>和</strong>100%</strong></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb4343b73ec7449f84ed198895a131dd~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@keyframes</span> 动画名称 &#123;
<span class="hljs-number">0%</span>&#123;
<span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
&#125;
<span class="hljs-number">100%</span>&#123;
<span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
&#125;   
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>再使用（调用）动画</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css">  <span class="hljs-selector-tag">div</span>&#123;
       <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
       <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
       <span class="hljs-attribute">background-color</span>: green;
       <span class="hljs-attribute">margin</span>: <span class="hljs-number">100px</span> auto;
       <span class="hljs-comment">/* 调用动画 */</span>
       <span class="hljs-attribute">animation-name</span>: 动画名称;
       <span class="hljs-comment">/* 持续时间 */</span>
       <span class="hljs-attribute">animation-duration</span>: 持续时间;
   &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-26">2）动画常用属性</h6>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0a20043b3bf449abd90d3004cb6b2a4~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h6 data-id="heading-27">3）动画简写属性</h6>
<p>animation：动画名称  持续时间  运动曲线  何时开始  播放次数  是否反方向  动画起始或者结束的状态；
animation: name duration timing-function delay iteration-count direction fill-mode;</p>
<ul>
<li>简写属性里面不包含animation-play-state，如需使用，单独写</li>
<li>暂停动画：animation-play-state：puased;经常和鼠标经过等其他配合使用</li>
<li>想要动画走回来，而不是直接就回来：animation-direction: alternate</li>
<li>盒子动画结束后，停在结束位置：animation-fill-mode: forwards</li>
</ul>
<h6 data-id="heading-28">案例：热点图</h6>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>热点图<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">body</span>&#123;
            <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#333</span>;
        &#125;
        <span class="hljs-selector-class">.map</span>&#123;
            <span class="hljs-attribute">position</span>: relative;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">747px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">616px</span>;
            <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> auto;
            <span class="hljs-attribute">background</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">'media/map.png'</span>) no-repeat;
        &#125;
        <span class="hljs-selector-class">.city</span>&#123;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">top</span>: <span class="hljs-number">227px</span>;
            <span class="hljs-attribute">right</span>: <span class="hljs-number">191px</span>;
        &#125;
        <span class="hljs-selector-class">.tb</span>&#123;
            <span class="hljs-attribute">top</span>: <span class="hljs-number">499px</span>;
            <span class="hljs-attribute">right</span>: <span class="hljs-number">80px</span>;
        &#125;
        <span class="hljs-selector-class">.dotted</span>&#123;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">8px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">8px</span>;
            <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
            <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#09f</span>;
        &#125;
        <span class="hljs-selector-tag">div</span><span class="hljs-selector-attr">[class^=<span class="hljs-string">'pulse'</span>]</span>&#123;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
            <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">10px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">10px</span>;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(-<span class="hljs-number">50%</span>, -<span class="hljs-number">50%</span>);
            <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
            <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">12px</span> <span class="hljs-number">#009dfd</span>;
            <span class="hljs-attribute">animation</span>: pulse <span class="hljs-number">1.2s</span> linear infinite;
        &#125;
        <span class="hljs-selector-class">.city</span> <span class="hljs-selector-class">.pulse2</span>&#123;
            <span class="hljs-attribute">animation-delay</span>: <span class="hljs-number">0.4s</span>;
        &#125;
        <span class="hljs-selector-class">.city</span> <span class="hljs-selector-class">.pulse3</span>&#123;
            <span class="hljs-attribute">animation-delay</span>: <span class="hljs-number">0.8s</span>;
        &#125;
        <span class="hljs-keyword">@keyframes</span> pulse &#123;
            <span class="hljs-number">0%</span>&#123;&#125;
            <span class="hljs-number">70%</span>&#123;
                <span class="hljs-comment">/* 用scale会导致阴影也放大 */</span>
                <span class="hljs-comment">/* transform: scale(2); */</span>
                <span class="hljs-attribute">width</span>: <span class="hljs-number">40px</span>;
                <span class="hljs-attribute">height</span>: <span class="hljs-number">40px</span>;
                <span class="hljs-attribute">opacity</span>: <span class="hljs-number">1</span>;
            &#125; 
            <span class="hljs-number">100%</span>&#123;
                <span class="hljs-attribute">width</span>: <span class="hljs-number">70px</span>;
                <span class="hljs-attribute">height</span>: <span class="hljs-number">70px</span>;
                <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0</span>;
            &#125;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"map"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"city"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dotted"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pulse1"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pulse2"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pulse3"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"city tb"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dotted"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pulse1"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pulse2"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pulse3"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>结果如图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7160163cf5ab4a8e9f42c4423e6388ee~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<blockquote>
<p>如果用scale结果如图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83647c797b60451f92bd165b812fbd37~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h6 data-id="heading-29">4）速度曲线细节</h6>
<p>animation-timing-function：规定动画的速度曲线，默认是ease
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf076140296445baaca0a29e1b4df3e5~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>速度曲线案例<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">div</span>&#123;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">20px</span>;
            <span class="hljs-attribute">background-color</span>: lightgreen;
            <span class="hljs-attribute">font-size</span>: <span class="hljs-number">12px</span>;
            <span class="hljs-comment">/* 让文字强制一行显示 */</span>
            <span class="hljs-attribute">white-space</span>: nowrap;
            <span class="hljs-comment">/* steps就是分几步来完成动画 */</span>
            <span class="hljs-attribute">animation</span>: move <span class="hljs-number">5s</span> <span class="hljs-built_in">steps</span>(<span class="hljs-number">8</span>) forwards;
            
        &#125;
        <span class="hljs-keyword">@keyframes</span> move &#123;
            <span class="hljs-number">0%</span>&#123;
                <span class="hljs-attribute">width</span>: <span class="hljs-number">0</span>;
            &#125;
            <span class="hljs-number">100%</span>&#123;
                <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
            &#125;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        是日前端欢迎您！
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-30">案例：奔跑的熊</h6>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>奔跑的熊<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">body</span>&#123;
            <span class="hljs-attribute">background</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">'media/bg1.png'</span>) no-repeat;
            <span class="hljs-attribute">animation</span>: bgback <span class="hljs-number">6s</span> <span class="hljs-built_in">steps</span>(<span class="hljs-number">8</span>) infinite;
        &#125;
        <span class="hljs-selector-tag">div</span>&#123;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
            <span class="hljs-attribute">background</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">'media/bear.png'</span>) no-repeat;
            <span class="hljs-attribute">animation</span>: bear <span class="hljs-number">0.4s</span> <span class="hljs-built_in">steps</span>(<span class="hljs-number">8</span>) infinite, move <span class="hljs-number">2s</span> <span class="hljs-built_in">steps</span>(<span class="hljs-number">8</span>) forwards; 
        &#125;
        <span class="hljs-keyword">@keyframes</span> bear &#123;
            <span class="hljs-number">0%</span>&#123;
                <span class="hljs-attribute">background-position</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span>;
            &#125;
            <span class="hljs-number">100%</span>&#123;
                <span class="hljs-attribute">background-position</span>: -<span class="hljs-number">1600px</span> <span class="hljs-number">0</span>;
            &#125;
        &#125;
        <span class="hljs-keyword">@keyframes</span> move &#123;
            <span class="hljs-number">0%</span>&#123;
                <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
                <span class="hljs-attribute">top</span>: <span class="hljs-number">200px</span>;
            &#125;
            <span class="hljs-number">100%</span>&#123;
                <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
                <span class="hljs-attribute">top</span>: <span class="hljs-number">200px</span>;
                <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateX</span>(-<span class="hljs-number">50%</span>);
            &#125;
        &#125;
        <span class="hljs-keyword">@keyframes</span> bgback &#123;
            <span class="hljs-number">0%</span>&#123;
                <span class="hljs-attribute">background-position</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span>;
            &#125;
            <span class="hljs-number">100%</span>&#123;
                <span class="hljs-attribute">background-position</span>: -<span class="hljs-number">1600px</span> <span class="hljs-number">0</span>;
            &#125;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>结果如图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef9cfda1d8de4c86801fbde7342caefb~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h4 data-id="heading-31">7. 3D转换</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32145258be1b462e84cffa1606c16680~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-32">特点</h5>
<ul>
<li>近大远小</li>
<li>物体后面遮挡不可见</li>
</ul>
<h5 data-id="heading-33">1. 三维坐标系</h5>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec5f64cd6f9c46c3b4082793bc339349~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
三维坐标系其实就是指立体空间，立体空间是由3个轴共同组成的。</p>
<ul>
<li>x轴：水平向右     注意：x右边是正值</li>
<li>y轴：垂直向下    注意：y下面是正值</li>
<li>z轴：垂直屏幕     注意：往外面是正值</li>
</ul>
<h5 data-id="heading-34">2. 3D移动 translate3d</h5>
<p>3D移动在2D移动的基础上多加了一个可以移动的方向，就是z轴方向</p>
<ul>
<li>transform: translateX(100px)：仅仅是在X轴上移动</li>
<li>transform: translateY(100px)：仅仅是在Y轴上移动</li>
<li>transform: translateZ(100px)：仅仅是在Z轴上移动（注意：translateZ一般用px单位）</li>
<li>transform: translate3d(x,y,z)：其中x、y、z分别要移动的轴的方向的距离（x、y、z没有不可省略，写0）</li>
</ul>
<h5 data-id="heading-35">3. 透视perspective（一般给父盒子添加）</h5>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aab6c2ccce934a0c8e29cee885f8af6a~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
在2D平面产生近大远小视觉立体，但是只是效果是二维的</p>
<ul>
<li>如果想要在网页产生3D效果需要透视（可理解成3D物体投影在2D平面内）</li>
<li>模拟人类的视觉位置，可认为安排一只眼睛去看</li>
<li>透视也称为视距：视距就是人的眼睛到屏幕的距离</li>
<li>距离视觉点越近的在电脑平面成像就越大，越远成像就越小</li>
<li>透视的单位是像素</li>
</ul>
<p><strong>透视写在被观察元素的父盒子上面的</strong>
d：就是视距，视距就是一个距离人的眼睛到屏幕的距离
z：就是z轴，物体距离屏幕的距离，z轴越大（正值）我们看到的物体就越大。</p>
<h5 data-id="heading-36">4. translateZ（一般给里面的盒子添加）</h5>
<p>transform: translateZ(100px)：仅仅是在Z轴上移动，有了透视，就能看到translateZ引起的变化了。</p>
<h5 data-id="heading-37">5. 3D旋转rotate3d</h5>
<p>3D旋转指可以让元素在三维平面内沿着x轴，y轴，z轴或者自定义轴进行旋转。
语法</p>
<ul>
<li>transform: rotateX(45deg)：沿着x轴正方向旋转45度</li>
<li>transform: rotateY(45deg)：沿着y轴正方向旋转45度</li>
<li>transform: rorateZ(45deg)：沿着z轴正方向旋转45deg</li>
<li>transform: rotate3d(x, y, z, deg)：沿着自定义轴旋转，deg为角度（了解）</li>
</ul>
<p>沿x轴旋转：单杠
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa70eb1faf2f4fa2a3ce46eb89d082c3~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
对于元素旋转的方向的判断，需要用到左手准则
左手准则</p>
<ul>
<li>左手的手拇指指向x轴的正方向</li>
<li>其余手指的弯曲方向就是该元素沿着x轴旋转的方向</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3dc52bccc404570900d0ffff24b11ac~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
沿y轴旋转：钢管舞
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0fd3e5014394639b3bb9c3584860d81~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
对于元素旋转的方向的判断，需要用到左手准则</p>
<p>左手准则</p>
<ul>
<li>左手的手拇指指向y轴的正方向</li>
<li>其余手指的弯曲方向就是该元素沿着y轴旋转的方向(正值)</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c97b39ec30eb40fdae16c089f74e07fd~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
沿z轴旋转：抽奖转盘
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62d9e727ba804b7db7b396d266765235~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
transform: rotate3d(x, y, z, deg)：沿着自定义轴旋转deg为角度（了解即可）
xyz是表示旋转轴的矢量，是标识你是否希望沿着该轴旋转，最后一个标示旋转的角度。</p>
<h5 data-id="heading-38">6. 3D呈现transform-style</h5>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b764b0a9c3f440a294f7abf79d2503bb~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>控制子元素是否开启三维立体环境</li>
<li>transform-style: flat子元素不开启3d立体空间，默认的</li>
<li>transform-style: preserve-3d;子元素开启立体空间</li>
<li>代码写给父级，但是影响的是子盒子</li>
<li>这个属性很重要</li>
</ul>
<h5 data-id="heading-39">案例：两面翻转的盒子</h5>
<h6 data-id="heading-40">实现步骤</h6>
<ol>
<li>搭建HTML结构</li>
</ol>
<ul>
<li>box父盒子里面包含两个子盒子</li>
<li>box是翻转的盒子，front是前面盒子，back是后面盒子</li>
</ul>
<ol start="2">
<li>CSS样式</li>
</ol>
<ul>
<li>box指定大小，切记要添加3d呈现</li>
<li>back盒子要沿着Y轴翻转180度</li>
<li>最后鼠标经过box沿着Y旋转180deg</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>3D导航栏<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">body</span> &#123;
            <span class="hljs-attribute">perspective</span>: <span class="hljs-number">400px</span>;
        &#125;
        
        <span class="hljs-selector-class">.box</span> &#123;
            <span class="hljs-attribute">position</span>: relative;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
            <span class="hljs-attribute">margin</span>: <span class="hljs-number">200px</span> auto;
            <span class="hljs-attribute">transition</span>: all .<span class="hljs-number">5s</span>;
            <span class="hljs-comment">/* 让背面的盒子保留立体空间，给父级添加 */</span>
            <span class="hljs-attribute">transform-style</span>: preserve-<span class="hljs-number">3</span>d;
        &#125;
        
        <span class="hljs-selector-class">.front</span>,
        <span class="hljs-selector-class">.back</span> &#123;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
            <span class="hljs-attribute">font-size</span>: <span class="hljs-number">24px</span>;
            <span class="hljs-attribute">text-align</span>: center;
            <span class="hljs-attribute">line-height</span>: <span class="hljs-number">300px</span>;
        &#125;
        
        <span class="hljs-selector-class">.front</span> &#123;
            <span class="hljs-attribute">background-color</span>: lightcoral;
            <span class="hljs-attribute">z-index</span>: <span class="hljs-number">1</span>;
        &#125;
        
        <span class="hljs-selector-class">.back</span> &#123;
            <span class="hljs-attribute">background-color</span>: lightgreen;
            <span class="hljs-comment">/* 像手机一样背靠背旋转 */</span>
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">180deg</span>);
        &#125;
        
        <span class="hljs-selector-class">.box</span><span class="hljs-selector-pseudo">:hover</span> &#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">180deg</span>);
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"front"</span>></span>是日前端<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"back"</span>></span>在这里等你<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-41">案例：3D导航栏</h5>
<h6 data-id="heading-42">实现步骤：</h6>
<ol>
<li>搭建HTML结构</li>
</ol>
<ul>
<li>li做导航栏</li>
<li>.box是翻转的盒子，front是前面的盒子，bottom是底下的盒子</li>
</ul>
<p>思路：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d998e2d77a7743a596e8b9d5e298a969~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>3D导航栏<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">li</span> &#123;
            <span class="hljs-attribute">list-style</span>: none;
            <span class="hljs-attribute">perspective</span>: <span class="hljs-number">500px</span>;
        &#125;
        
        <span class="hljs-selector-tag">ul</span> &#123;
            <span class="hljs-attribute">margin</span>: <span class="hljs-number">100px</span>;
        &#125;
        
        <span class="hljs-selector-tag">ul</span> <span class="hljs-selector-tag">li</span> &#123;
            <span class="hljs-attribute">float</span>: left;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
            <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">10px</span>;
        &#125;
        
        <span class="hljs-selector-class">.box</span> &#123;
            <span class="hljs-attribute">position</span>: relative;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">transition</span>: all .<span class="hljs-number">5s</span>;
            <span class="hljs-attribute">transform-style</span>: preserve-<span class="hljs-number">3</span>d;
        &#125;
        
        <span class="hljs-selector-class">.front</span>,
        <span class="hljs-selector-class">.bottom</span> &#123;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">line-height</span>: <span class="hljs-number">50px</span>;
            <span class="hljs-attribute">text-align</span>: center;
        &#125;
        
        <span class="hljs-selector-class">.front</span> &#123;
            <span class="hljs-attribute">background-color</span>: lightgreen;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">25px</span>);
        &#125;
        
        <span class="hljs-selector-class">.bottom</span> &#123;
            <span class="hljs-attribute">background-color</span>: yellowgreen;
            <span class="hljs-comment">/* 这里的x轴一定是负值 */</span>
            <span class="hljs-comment">/* 如果有移动或者其他样式，必须先写移动 */</span>
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateY</span>(<span class="hljs-number">25px</span>) <span class="hljs-built_in">rotateX</span>(-<span class="hljs-number">90deg</span>);
        &#125;
        
        <span class="hljs-selector-class">.box</span><span class="hljs-selector-pseudo">:hover</span> &#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateX</span>(<span class="hljs-number">90deg</span>);
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"front"</span>></span>是日前端<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"bottom"</span>></span>在这里等你<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"front"</span>></span>是日前端<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"bottom"</span>></span>日拱一卒<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"front"</span>></span>是日前端<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"bottom"</span>></span>在这里等你<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>结果如图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6ab0a842d6b4980abdf258b359d3434~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h5 data-id="heading-43">H5C3综合案例：旋转木马</h5>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>旋转木马<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">body</span>&#123;
            <span class="hljs-attribute">perspective</span>: <span class="hljs-number">800px</span>;
        &#125;
        <span class="hljs-selector-tag">section</span>&#123;
            <span class="hljs-attribute">position</span>: relative;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
            <span class="hljs-attribute">margin</span>: <span class="hljs-number">100px</span> auto;
            <span class="hljs-attribute">transform-style</span>: preserve-<span class="hljs-number">3</span>d;
            <span class="hljs-attribute">animation</span>: rotate <span class="hljs-number">8s</span> linear infinite;
            <span class="hljs-attribute">background</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">images/pig.jpg</span>) no-repeat;
        &#125;
        <span class="hljs-selector-tag">section</span> <span class="hljs-selector-tag">div</span> &#123;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">background</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">images/dog.jpg</span>) no-repeat;
        &#125;
        <span class="hljs-selector-tag">section</span> <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:first</span>-child&#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">0deg</span>) <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">300px</span>);
        &#125;
        <span class="hljs-selector-tag">section</span> <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">2</span>)&#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">60deg</span>) <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">300px</span>);
        &#125;
        <span class="hljs-selector-tag">section</span> <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">3</span>)&#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">120deg</span>) <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">300px</span>);
        &#125;
        <span class="hljs-selector-tag">section</span> <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">4</span>)&#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">180deg</span>) <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">300px</span>);
        &#125;
        <span class="hljs-selector-tag">section</span> <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:nth-child</span>(<span class="hljs-number">5</span>)&#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">240deg</span>) <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">300px</span>);
        &#125;
        <span class="hljs-selector-tag">section</span> <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:last-child</span>&#123;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">320deg</span>) <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">300px</span>);
        &#125;
        <span class="hljs-selector-tag">section</span><span class="hljs-selector-pseudo">:hover</span>&#123;
            <span class="hljs-attribute">animation-play-state</span>: paused;
        &#125;
        <span class="hljs-keyword">@keyframes</span> rotate &#123;
            <span class="hljs-number">0%</span>&#123;
                <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">0</span>);
            &#125;
            <span class="hljs-number">100%</span>&#123;
                <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateY</span>(<span class="hljs-number">360deg</span>);
            &#125;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">section</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">section</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>结果如图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4958c94525fd436e9d4740aec92e98de~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h3 data-id="heading-44">练习1</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e31c4a5c86c41c1aea5231f6d0910f3~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
HTML结构：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>01.《阴阳师》二维码<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"css/index.css"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"scan"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"qrcode"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"images/57b280b496dee47507111c56NRN73rVj.png"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"line"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"images/line_dd0b705.png"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CSS样式：</p>
<pre><code class="hljs language-css copyable" lang="css">*&#123;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
&#125;
<span class="hljs-selector-tag">body</span>&#123;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">50px</span>;
&#125;
<span class="hljs-selector-class">.scan</span>&#123;
    <span class="hljs-attribute">position</span>: relative;
    <span class="hljs-comment">/* margin: 50px; */</span>
    <span class="hljs-attribute">width</span>: <span class="hljs-number">145px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">297px</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">../images/index_z_71df05e.png</span>) <span class="hljs-number">0</span> <span class="hljs-number">0</span> no-repeat;
&#125;
<span class="hljs-selector-class">.qrcode</span>&#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">display</span>: block;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">19px</span>;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">45px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">107px</span>;
&#125;
<span class="hljs-selector-class">.line</span>&#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">9px</span>;
    <span class="hljs-attribute">top</span>: -<span class="hljs-number">3px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">120px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">15px</span>;
    -webkit-<span class="hljs-attribute">animation</span>: sao <span class="hljs-number">4s</span> linear infinite;
    -moz-<span class="hljs-attribute">animation</span>: sao <span class="hljs-number">4s</span> linear infinite;
    -ms-<span class="hljs-attribute">animation</span>: sao <span class="hljs-number">4s</span> linear infinite;
    <span class="hljs-attribute">animation</span>: sao <span class="hljs-number">4s</span> linear infinite;
&#125;
<span class="hljs-keyword">@keyframes</span> sao&#123;
    <span class="hljs-number">0%</span>&#123;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">42px</span>;
    &#125;
    <span class="hljs-number">50%</span>&#123;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">145px</span>;
    &#125;
    <span class="hljs-number">100%</span>&#123;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">42px</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>结果如图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7347227ba31482dbdf3ac9e10f1f56e~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h3 data-id="heading-45">练习2</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4fd1c3b9b2c94894915849a6523e473b~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-46">7. 浏览器私有前缀</h4>
<p>浏览器私有前缀是为了兼容老版本的写法，比较新版本的浏览器无需添加。</p>
<h5 data-id="heading-47">7.1 私有前缀</h5>
<ul>
<li>-moz-：代表firefox浏览器私有属性</li>
<li>-ms-：代表ie浏览器私有属性</li>
<li>-webkit-：代表safari、chrome私有属性</li>
<li>-o-：代表Opera私有属性</li>
</ul>
<h5 data-id="heading-48">7.2 提倡的写法</h5>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea042ab9deec430f9306748552e08a94~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            