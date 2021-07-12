
---
title: '学会这些CSS技巧让你写样式更加丝滑'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/604b329709ba4a33a41f9bc9b9e4e05e~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 17:40:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/604b329709ba4a33a41f9bc9b9e4e05e~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1，前言</h1>
<hr>
<p>记录一些很好用的css属性</p>
<h1 data-id="heading-1">1，calc()</h1>
<hr>
<p>calc()函数用于动态计算长度值，任何长度值都可以使用calc()函数进行计算，需要注意的是，运算符前后都需要保留一个空格，例如：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span>&#123;
<span class="hljs-attribute">width</span>: <span class="hljs-built_in">calc</span>(<span class="hljs-number">100%</span> - <span class="hljs-number">10px</span>)
height: <span class="hljs-built_in">calc</span>(<span class="hljs-number">100%</span> - <span class="hljs-number">2rem</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>兼容性</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/604b329709ba4a33a41f9bc9b9e4e05e~tplv-k3u1fbpfcp-zoom-1.image" alt="兼容性" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">2，min()</h1>
<hr>
<p>min()函数允许你从逗号分隔符表达式中选择一个最小值作为css的属性值，例如：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span>&#123;
<span class="hljs-attribute">width</span>: <span class="hljs-built_in">min</span>(<span class="hljs-number">1vw</span>, <span class="hljs-number">4em</span>, <span class="hljs-number">80px</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的例子中，宽度最多是80px。如果视口的宽度小于800px，或者一个em的宽度小于20px，则会更窄。换句话说，最大宽度是80px。</p>
<p>当min() 用于控制文本大小时，要保证文本足够大以便于阅读。建议把 min() 方法嵌入到 max() 中</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">p</span>&#123;
<span class="hljs-attribute">font-size</span>: <span class="hljs-built_in">max</span>(<span class="hljs-built_in">min</span>(<span class="hljs-number">0.5vw</span>, <span class="hljs-number">0.5em</span>), <span class="hljs-number">1rem</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这用于保证最小值是1rem，这样在页面缩放时文本也会缩放</p>
<p><strong>兼容性</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55382ebb187748fba01d70fb11fc9150~tplv-k3u1fbpfcp-zoom-1.image" alt="兼容性" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">3，max()</h1>
<hr>
<p>max()函数让你可以从一个逗号分隔的表达式列表中选择最大（正方向）的值作为属性的值</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span>&#123;
<span class="hljs-attribute">width</span>: <span class="hljs-built_in">max</span>(<span class="hljs-number">10vw</span>, <span class="hljs-number">4em</span>, <span class="hljs-number">80px</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面这个例子中，宽度最小会是80px，除非视图宽度大于800px或者是一个em比20px宽。简单来说，最小宽度是80px。你也可以认为max()的值提供了一个属性最小可能的值。</p>
<p>当max()用于控制文本大小时，确保文本总是足够大以供阅读。一个建议是使用min()嵌套在 max()中的函数，该函数的第二个值是一个相对长度单位，该单位总是足够大以读取</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">p</span>&#123;
<span class="hljs-attribute">font-size</span>: <span class="hljs-built_in">max</span>(<span class="hljs-built_in">min</span>(<span class="hljs-number">0.5vw</span>, <span class="hljs-number">0.5em</span>), <span class="hljs-number">1rem</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这确保了1rem的最小大小，如果页面缩放，文本大小会缩放</p>
<p><strong>兼容性</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/477fe97ef89449f5b13baaa4e383331b~tplv-k3u1fbpfcp-zoom-1.image" alt="兼容性" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">4，clamp()</h1>
<hr>
<p>clamp() 函数的作用是把一个值限制在一个上限和下限之间，当这个值超过最小值和最大值的范围时，在最小值和最大值之间选择一个值使用。它接收三个参数：最小值、首选值、最大值clamp(MIN, VAL, MAX)，当首选值比最小值要小时，则使用最小值，当首选值介于最小值和最大值之间时，用首选值，当首选值比最大值要大时，则使用最大值，表达式中的每一个值都可以用不同的单位。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span>&#123;
<span class="hljs-attribute">width</span>: <span class="hljs-built_in">clamp</span>(<span class="hljs-number">200px</span>, <span class="hljs-number">50vw</span>, <span class="hljs-number">600px</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>兼容性</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67c166edacd14031b2d25294ccb80165~tplv-k3u1fbpfcp-zoom-1.image" alt="兼容性" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-5">5，gap</h1>
<hr>
<p>gap属性是用来设置网格行与列之间的间隙，该属性是row-gap和column-gap的简写形式，适用于Flex，Grid和multi-column布局的元素</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-id">#flex</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
  <span class="hljs-attribute">display</span>: flex;
  gap: <span class="hljs-number">20px</span> <span class="hljs-number">5px</span>;
&#125;
<span class="hljs-selector-id">#grid</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">display</span>: grid;
  grid-template: <span class="hljs-built_in">repeat</span>(<span class="hljs-number">3</span>, <span class="hljs-number">1</span>fr) / <span class="hljs-built_in">repeat</span>(<span class="hljs-number">3</span>, <span class="hljs-number">1</span>fr);
  gap: <span class="hljs-number">20px</span> <span class="hljs-number">5px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>兼容性</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6497da1d8334b9999ac2d6d6006c61f~tplv-k3u1fbpfcp-zoom-1.image" alt="兼容性" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8d037bc52234731b9e63f96274ba0d8~tplv-k3u1fbpfcp-zoom-1.image" alt="兼容性" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">6，writing-mode</h1>
<hr>
<p>writing-mode 属性定义了文本在水平或垂直方向上如何排布。
语法格式如下：</p>
<pre><code class="hljs language-css copyable" lang="css">writing-mode: horizontal-tb | vertical-rl | vertical-lr | sideways-rl | sideways-lr
<span class="copy-code-btn">复制代码</span></code></pre>
<p>horizontal-tb：水平方向自上而下的书写方式。即 left-right-top-bottom</p>
<p>vertical-rl：垂直方向自右而左的书写方式。即 top-bottom-right-left</p>
<p>vertical-lr：垂直方向内内容从上到下，水平方向从左到右</p>
<p>sideways-rl：内容垂直方向从上到下排列</p>
<p>sideways-lr：内容垂直方向从下到上排列</p>
<p><strong>兼容性</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65daecbf17d34b57a60a7df9dd6423f9~tplv-k3u1fbpfcp-zoom-1.image" alt="兼容性" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>如果看了觉得有帮助的，我是@鹏多多，欢迎 点赞 关注 评论；
END</strong></p>
<blockquote>
</blockquote>
<p><code>往期文章</code></p>
<ul>
<li><a href="https://juejin.cn/post/6953803916484018206" target="_blank" title="https://juejin.cn/post/6953803916484018206">使用nvm管理node.js版本以及更换npm淘宝镜像源</a></li>
<li><a href="https://juejin.cn/post/6921527102273650695" target="_blank" title="https://juejin.cn/post/6921527102273650695">细数JS中实用且强大的操作符&运算符</a></li>
<li><a href="https://juejin.cn/post/6944950213538742279" target="_blank" title="https://juejin.cn/post/6944950213538742279">微信小程序实现搜索关键词高亮</a></li>
<li><a href="https://juejin.cn/post/6956491743537659941" target="_blank" title="https://juejin.cn/post/6956491743537659941">vue中利用.env文件存储全局环境变量，以及配置vue启动和打包命令</a></li>
<li><a href="https://juejin.cn/post/6942281834893934629" target="_blank" title="https://juejin.cn/post/6942281834893934629">javaScript中try和catch的使用和跳出forEach循环</a></li>
</ul>
<p><code>个人主页</code></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fpdd11997110103%3Fspm%3D1010.2135.3001.5421" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/pdd11997110103?spm=1010.2135.3001.5421" ref="nofollow noopener noreferrer">CSDN</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpdd11997110103" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pdd11997110103" ref="nofollow noopener noreferrer">GitHub</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fu%2Fb7a8536bff06" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/u/b7a8536bff06" ref="nofollow noopener noreferrer">简书</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2F-pdd%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/-pdd/" ref="nofollow noopener noreferrer">博客园</a></li>
<li><a href="https://juejin.cn/user/747323639737191" target="_blank" title="https://juejin.cn/user/747323639737191">掘金</a></li>
</ul></div>  
</div>
            