
---
title: '在页面离开前提醒你的beforeunload事件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2653510e49a04ec0918f64752e00694a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 00:40:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2653510e49a04ec0918f64752e00694a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第7天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p>大家好，我是前端队长Daotin，想要获取更多前端精彩内容，关注我，解锁前端成长新姿势。</p>
<p>以下正文：</p>
<h2 data-id="heading-0">问题描述</h2>
<p>有些需要填写用户信息的界面，当用户点击返回，或者刷新界面，关闭界面的时候，需要及时提醒用户当前的页面填写了内容，如果返回或者刷新的话，会导致内容丢失。提醒用户后让用户自行决定后续的操作。</p>
<h2 data-id="heading-1">解决办法</h2>
<p><code>beforeunload</code>事件就可以帮你做到这件事。</p>
<p>当<code>浏览器窗口关闭</code>或者<code>刷新</code>时，会触发<code>beforeunload</code>事件。当前页面不会直接关闭，可以点击确定按钮关闭或刷新，也可以取消。</p>
<p>该事件使网页能够触发一个<code>确认对话框</code> ，询问用户是否真的要离开该页面。如果用户确认，浏览器将导航到新页面，否则导航将会取消。</p>
<p>根据规范，要显示确认对话框，事件处理程序需要在事件上调用<code>preventDefault()</code>。</p>
<blockquote>
<p>注意，并非所有浏览器都支持此方法，而有些浏览器需要事件处理程序实现两个遗留方法中的一个作为代替：</p>
<ul>
<li>将字符串分配给事件的<code>returnValue</code>属性</li>
<li>从事件处理程序返回一个字符串。</li>
</ul>
<p>这两个方法以前是用于自定义确认对话框要显示的文本信息，现在已经废弃，且大部分浏览器不支持自定义对话框文本消息。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2653510e49a04ec0918f64752e00694a~tplv-k3u1fbpfcp-zoom-1.image" alt="微信截图_20201020134452" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">代码示例</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'beforeunload'</span>, <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
  <span class="hljs-comment">// 显示确认对话框</span>
  event.preventDefault();
  <span class="hljs-comment">// 为了兼容处理，Chrome需要设置returnValue</span>
  event.returnValue = <span class="hljs-string">''</span>;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">特别提醒</h2>
<ul>
<li>
<p>为避免意外弹出窗口，<code>除非页面已交互（鼠标点击了此页面）</code>，否则在刷新或者关闭的时候，不会触发beforeunload事件。</p>
</li>
<li>
<p>确认对话框不可以显示自定义字符串。某些浏览器以前可以显示用户自定义消息。但是，<code>此方法已被弃用</code>，并且在大多数浏览器中不再支持。</p>
</li>
</ul>
<hr>
<blockquote>
<p><strong>最近热门文章</strong>：</p>
<ul>
<li><a href="https://juejin.cn/post/6963071339108237319" target="_blank">图片瀑布流，就是如此简单（so easy）</a></li>
<li><a href="https://juejin.cn/post/6961968236837470216" target="_blank">梳理ajax跨域常用4种解决方案（简单易懂）</a></li>
<li><a href="https://juejin.cn/post/6961226664869101605" target="_blank">Vue.js命名风格指南（易记版）</a></li>
</ul>
</blockquote>
<p><em><strong>以上，如果你看了觉得对你有所帮助，就点个赞叭，这样Daotin也有更新下去的动力，跪谢各位父老乡亲啦~~~ 听说喜欢点赞的人，一个月内都会有好运降临哦 ~~</strong></em></p></div>  
</div>
            