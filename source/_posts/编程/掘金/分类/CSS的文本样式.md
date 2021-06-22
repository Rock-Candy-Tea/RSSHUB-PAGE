
---
title: 'CSS的文本样式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdf1c1b8e37d4232935d11824d73d1f7~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 22 Jun 2021 01:18:56 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdf1c1b8e37d4232935d11824d73d1f7~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">CSS的文本样式</h3>
<ul>
<li><a href="https://juejin.cn/post/6976545307764981767#_1">文本样式</a></li>
<li>
<ul>
<li><a href="https://juejin.cn/post/6976545307764981767#_9">设置文本颜色</a></li>
<li><a href="https://juejin.cn/post/6976545307764981767#_52">设置元素水平对齐方式</a></li>
<li><a href="https://juejin.cn/post/6976545307764981767#_82">设置首行文本的缩进</a></li>
<li><a href="https://juejin.cn/post/6976545307764981767#_119">设置文本的行高</a></li>
<li><a href="https://juejin.cn/post/6976545307764981767#_149">设置文本的装饰</a></li>
</ul>
</li>
</ul>
<h1 data-id="heading-1"><a href="https://juejin.cn/post/6976545307764981767"></a>文本样式</h1>



































<table><thead><tr><th>属性名</th><th>含义</th><th>举例</th></tr></thead><tbody><tr><td>color</td><td>设置文本颜色</td><td>color:#00C</td></tr><tr><td>text-align</td><td>设置元素水平对齐方式</td><td>text-align:right</td></tr><tr><td>text-indent</td><td>设置首行文本的缩进</td><td>text-indent:20px</td></tr><tr><td>line-height</td><td>设置文本的行高</td><td>line-height:25px</td></tr><tr><td>text-decoration</td><td>设置文本的装饰</td><td>text-decoration:underline</td></tr></tbody></table>
<h2 data-id="heading-2"><a href="https://juejin.cn/post/6976545307764981767"></a>设置文本颜色</h2>
<blockquote>
<p>​取值方法：<br>
1.颜色名字<br>
2.十六进制记法<br>
3.R G B 三原色<br>
4.RGBA 三原色，A是控制透明度 Alpha 0 -1 , 1完全不透明，0 完全透明</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"color: red;"</span>></span>使用颜色名称<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"color: #006699;"</span>></span>使用十六进制<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"color: rgb(0,0,0);"</span>></span>使用十六进制<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"color: rgba(0,0,0,1);"</span>></span>rgba透明度为1<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"color: rgba(0,0,0,0);"</span>></span>rgba透明度为0<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>样例代码：</strong></em></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"color: red;"</span>></span>使用颜色名称<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"color: #006699;"</span>></span>使用十六进制<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"color: rgb(0,0,0);"</span>></span>使用十六进制<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"color: rgba(0,0,0,1);"</span>></span>rgba透明度为1<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"color: rgba(0,0,0,0);"</span>></span>rgba透明度为0<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>效果截图：</strong></em></p>
<blockquote>
<p>最后一行是完全透明看不到↓</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdf1c1b8e37d4232935d11824d73d1f7~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这样就可以看到了↓</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/232fab33242e4004ac0df6d7ea9ba414~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3"><a href="https://juejin.cn/post/6976545307764981767"></a>设置元素水平对齐方式</h2>
<blockquote>
<p>文本的对齐方式 left right center</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"text-align: left;"</span>></span>文字对齐方向 left<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"text-align: right;"</span>></span>文字对齐方向 right<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"text-align: center;"</span>></span>文字对齐方向 center<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>样例代码：</strong></em></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"text-align: left;"</span>></span>文字对齐方向 left<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"text-align: right;"</span>></span>文字对齐方向 right<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"text-align: center;"</span>></span>文字对齐方向 center<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>效果截图：</strong></em><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1e8cc5261764af2ae5a48331eb25123~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4"><a href="https://juejin.cn/post/6976545307764981767"></a>设置首行文本的缩进</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"text-indent: 50px;"</span>></span>这里写一段话<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>样例代码：</strong></em></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> ></span>中国专业IT社区CSDN (Chinese Software Developer Network) 创立于1999年，致力于为中国软件开发者提供知识传播、在线学习、职业发展等全生命周期服务。
旗下拥有：专业的中文IT技术社区： CSDN.NET；移动端开发者专属APP： CSDN APP、CSDN学院APP；
新媒体矩阵微信公众号：CSDN资讯、程序人生、GitChat、CSDN学院、AI科技大本营、区块链大本营、CSDN云计算、GitChat精品课、人工智能头条、CSDN企业招聘；
IT技术培训学习平台： CSDN学院；技术知识移动社区： GitChat；IT人力资源服务：科锐福克斯；
高校IT技术学习成长平台：高校俱乐部。<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"text-indent: 50px;"</span>></span>中国专业IT社区CSDN (Chinese Software Developer Network) 创立于1999年，致力于为中国软件开发者提供知识传播、在线学习、职业发展等全生命周期服务。
旗下拥有：专业的中文IT技术社区： CSDN.NET；移动端开发者专属APP： CSDN APP、CSDN学院APP；
新媒体矩阵微信公众号：CSDN资讯、程序人生、GitChat、CSDN学院、AI科技大本营、区块链大本营、CSDN云计算、GitChat精品课、人工智能头条、CSDN企业招聘；
IT技术培训学习平台： CSDN学院；技术知识移动社区： GitChat；IT人力资源服务：科锐福克斯；
高校IT技术学习成长平台：高校俱乐部。<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>效果截图：</strong></em></p>
<blockquote>
<p>效果很明显吧，第一段话没有加缩进，第二段话加了缩进</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f925642814a43b293fea04dbf18f755~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5"><a href="https://juejin.cn/post/6976545307764981767"></a>设置文本的行高</h2>
<blockquote>
<p>行高,一般用于配合着垂直居中使用, 将文本的 line-height 和容器的高度一致</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"border: solid 1px red;height: 100px;line-height: 100px;"</span>></span>
CSDN
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>样例代码：</strong></em></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"border: solid 1px red;height: 100px;line-height: 100px;"</span>></span>
CSDN
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>效果截图：</strong></em><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8df5089e1e34e188cc1cb91ab0be864~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6"><a href="https://juejin.cn/post/6976545307764981767"></a>设置文本的装饰</h2>

























<table><thead><tr><th>text-decoration-line属性值</th><th>说明</th></tr></thead><tbody><tr><td>none</td><td>默认值定义的标准文本</td></tr><tr><td>underline</td><td>设置文本的下划线</td></tr><tr><td>overline</td><td>设置文本的上划线</td></tr><tr><td>line-through</td><td>设置文本的删除线</td></tr></tbody></table>





























<table><thead><tr><th>text-decoration-style属性值</th><th>说明</th></tr></thead><tbody><tr><td>solid</td><td>默认值线条将显示为单线</td></tr><tr><td>double</td><td>线条将显示为双线</td></tr><tr><td>dotted</td><td>线条将显示为点状线</td></tr><tr><td>dashed</td><td>线条将显示为虚线</td></tr><tr><td>wavy</td><td>线条将显示为波浪线</td></tr></tbody></table>













<table><thead><tr><th>text-decoration-color属性值</th><th>说明</th></tr></thead><tbody><tr><td>选择颜色</td><td>线条显示相应的颜色</td></tr></tbody></table>
<p><em><strong>样例代码：</strong></em></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>  <span class="hljs-attr">style</span>=<span class="hljs-string">"text-decoration-line: none;"</span>></span>CSDN<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>/></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>  <span class="hljs-attr">style</span>=<span class="hljs-string">"text-decoration-line: line-through;"</span>></span>CSDN<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>/></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>  <span class="hljs-attr">style</span>=<span class="hljs-string">"text-decoration-line: underline;"</span>></span>CSDN<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>/></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>  <span class="hljs-attr">style</span>=<span class="hljs-string">"text-decoration-line: overline;"</span>></span>CSDN<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>/></span>

<span class="hljs-tag"><<span class="hljs-name">div</span>  <span class="hljs-attr">style</span>=<span class="hljs-string">"text-decoration-line: underline;text-decoration-style: solid;"</span>></span>CSDN<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>/></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>  <span class="hljs-attr">style</span>=<span class="hljs-string">"text-decoration-line: underline;text-decoration-style: dashed;"</span>></span>CSDN<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>/></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>  <span class="hljs-attr">style</span>=<span class="hljs-string">"text-decoration-line: underline;text-decoration-style: dotted;"</span>></span>CSDN<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>/></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>  <span class="hljs-attr">style</span>=<span class="hljs-string">"text-decoration-line: underline;text-decoration-style: wavy;"</span>></span>CSDN<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>/></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>  <span class="hljs-attr">style</span>=<span class="hljs-string">"text-decoration-line: underline;text-decoration-style: unset;"</span>></span>CSDN<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>/></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>  <span class="hljs-attr">style</span>=<span class="hljs-string">"text-decoration-line: underline;text-decoration-style: double;"</span>></span>CSDN<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>/></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>  <span class="hljs-attr">style</span>=<span class="hljs-string">"text-decoration-line: underline;text-decoration-style: none;"</span>></span>CSDN<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>/></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>  <span class="hljs-attr">style</span>=<span class="hljs-string">"text-decoration-line: underline;text-decoration-style: solid;text-decoration-color: red;"</span>></span>CSDN<span class="hljs-tag"></<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>/></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>效果截图：</strong></em><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03bd51a0ebc048d99d4850ad359d9ac2~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>效果可以叠加使用，如上↑</p>
</blockquote>
<p><strong>写作不易，读完如果对你有帮助，感谢点赞支持！<br>
如果你是电脑端，看见右下角的“<em>一键三连</em>”了吗，没错点它[哈哈]</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2855387a529b4cf6857307374444a97f~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>加油！</strong></p>
<p><strong>共同努力！</strong></p>
<p><strong>Keafmd</strong></p></div>  
</div>
            