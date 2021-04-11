
---
title: 'JavaScript—事件函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd513456e2734848acce1cc0ee027b26~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 07 Apr 2021 22:14:46 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd513456e2734848acce1cc0ee027b26~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><a href="https://juejin.cn/post/6948666460617048072"></a>汇总表格</h2>

































<table><thead><tr><th>函数名</th><th>作用</th></tr></thead><tbody><tr><td>onmousemove</td><td>检测鼠标是否移动</td></tr><tr><td>clientX</td><td>鼠标的X坐标</td></tr><tr><td>clientY</td><td>鼠标的Y坐标</td></tr><tr><td>pageX</td><td>相对于当前页面的X坐标</td></tr><tr><td>pageY</td><td>相对于当前页面的Y坐标</td></tr><tr><td>target</td><td>触发事件的对象，使用event.target可以调用</td></tr></tbody></table>
<h2 data-id="heading-1"><a href="https://juejin.cn/post/6948666460617048072"></a>事件对象</h2>
<p>当事件的响应函数被触发时，浏览器每次都会将一个事件对象作为实参，传递进响应函数，在事件对象中封装了当前对象的一切信息，比如：鼠标的坐标，当前键盘按下了那个键，鼠标滚动的方向等等。<br>
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd513456e2734848acce1cc0ee027b26~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2"><a href="https://juejin.cn/post/6948666460617048072"></a>事件冒泡</h2>
<p>什么是事件冒泡？</p>
<blockquote>
<p>所谓的事件冒泡，指的是触发了内部事件，造成外部事件也跟着一起触发了。</p>
</blockquote>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7312d41e7e044edb9cce3faf5e6adf3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3"><a href="https://juejin.cn/post/6948666460617048072"></a>取消事件冒泡</h3>
<pre><code class="hljs language-js copyable" lang="js">event.cancelBubble = <span class="hljs-literal">true</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4"><a href="https://juejin.cn/post/6948666460617048072"></a>事件的委派</h2>
<blockquote>
<p>定义： 指将事件统一绑定给元素的共同的祖先元素，这样后代元素的事件触发时，会一直冒泡到祖先元素，从而通过祖先元素的响应函数来处理事件。事件委派是利用了冒泡，通过委派可以减少事件的绑定次数，提高程序的性能。</p>
</blockquote>
<h2 data-id="heading-5"><a href="https://juejin.cn/post/6948666460617048072"></a>事件绑定</h2>
<ul>
<li>事件被覆盖的情况<br>
<img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b4be7435b544e36be649117e1d3d84c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>
解决上述问题的方法：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">btn01.addEventListener(<span class="hljs-string">"click"</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;这里写语句&#125;,<span class="hljs-literal">false</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a6bf50c1b0c4acda0af7b0a8d4d0c65~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>
使用上面的方法不会被覆盖掉。但是IE8不支持addEventListener这个方法，需要考虑兼容性的问题。IE8可以使用attachEvent方法。</p>
<h3 data-id="heading-6"><a href="https://juejin.cn/post/6948666460617048072"></a>addEventListener和attachEvent中this指向的问题</h3>
<ul>
<li>addEventListener中的this指的是绑定事件的对象</li>
<li>attachEvent中的this指的是window</li>
</ul>
<h3 data-id="heading-7"><a href="https://juejin.cn/post/6948666460617048072"></a>解决兼容性的方法：</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3974f405be9e4374a2d69338d1a76477~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            