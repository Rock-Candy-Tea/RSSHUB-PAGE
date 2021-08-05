
---
title: '🔥仿天猫放大镜效果的React组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34e43e1b1b99448d81966870e27e5c3d~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 23:49:34 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34e43e1b1b99448d81966870e27e5c3d~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、基于React+Hooks实现的一个仿天猫的购物放大镜组件</h1>
<blockquote>
<p>之前在项目中有遇到实现购物车放大镜的功能，当时比较着急，没有考虑复用性等。最近项目比较闲，所以就写了这样的一个组件。</p>
</blockquote>
<h1 data-id="heading-1">二、使用方法</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1.</span>安装插件
npm install @parrotjs/react-preview-magnifier

<span class="hljs-number">2.</span>在需要使用的地方进行引用并使用
<span class="hljs-keyword">import</span> Preview <span class="hljs-keyword">from</span> <span class="hljs-string">'@parrotjs/react-preview-magnifier'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"@parrotjs/react-preview-magnifier/dist/index.css"</span> 

<span class="hljs-number">3.</span>使用
<Preview>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">img</span> 
          <span class="hljs-attr">alt</span>=<span class="hljs-string">&#123;</span>''&#125; 
          <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;width:400,height:400&#125;&#125;</span> 
          <span class="hljs-attr">src</span>=<span class="hljs-string">&#123;</span>"<span class="hljs-attr">https:</span>//<span class="hljs-attr">img.alicdn.com</span>/<span class="hljs-attr">imgextra</span>/<span class="hljs-attr">i4</span>/<span class="hljs-attr">3282796868</span>/<span class="hljs-attr">O1CN01gTtB5c20basEyuYsW_</span>!!<span class="hljs-attr">3282796868.jpg_430x430q90.jpg</span>"&#125; 
    /></span></span>
</Preview>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">三、使用注意事项</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">1.需要将img标签作为子元素传入</h2>
<pre><code class="hljs language-js copyable" lang="js">图片需要设置宽高等，便于组件内部进行计算高度等，且必须要是单标签
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">四、开放的API</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">1.offsetLeft</h2>
<pre><code class="hljs language-js copyable" lang="js">右边预览框距离左边的距离,默认为10px
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">2.shrinkProportion</h2>
<pre><code class="hljs language-js copyable" lang="js">选择框内选择区域相较于选择框的占比，默认是<span class="hljs-number">0.5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">3.previewBoxSize</h2>
<pre><code class="hljs language-js copyable" lang="js">预览框相较于原图的大小比例，默认是<span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">4.小伙伴可以提出需求 我会开放更多api</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">五、未来插件</h1>
<pre><code class="hljs language-js copyable" lang="js">如果有小伙伴使用 我会带来更多的功能 丰富完善插件 

<span class="hljs-number">1.</span>增加滚轮放大功能
<span class="hljs-number">2.</span>....
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10">六、预览地址</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fcompetent-bardeen-pe62y%3Ffile%3D%2Fsrc%2FApp.tsx%3A0-562" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/competent-bardeen-pe62y?file=/src/App.tsx:0-562" ref="nofollow noopener noreferrer">codesandbox预览地址</a></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34e43e1b1b99448d81966870e27e5c3d~tplv-k3u1fbpfcp-zoom-crop-mark:1956:0:0:0.image" alt="测试.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-11">七、github地址</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fparrot-design%2Fparrot-rc-preview-magnifier" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/parrot-design/parrot-rc-preview-magnifier" ref="nofollow noopener noreferrer">github地址</a></p></div>  
</div>
            