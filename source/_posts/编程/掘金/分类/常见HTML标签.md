
---
title: '常见HTML标签'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee907364dbbe49dc9d18d5cc7b931b84~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 01:35:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee907364dbbe49dc9d18d5cc7b931b84~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><code>iframe</code>标签</h2>
<ol>
<li>现代前端开发很少用到。</li>
<li>作用：在页面中嵌入一个页面。</li>
</ol>
<pre><code class="copyable"><iframe src="https://www.baidu.com" frameborder="0"></iframe>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>默认高度50，宽度100。所以也是一个<code>可替换标签</code>；宽高可以由自己决定，可以在iframe标签中添加width和hight属性改变尺寸，也可用CSS更改。</li>
<li>默认属性 frameborder="0" ，不显示默认边框。</li>
<li>与<code>a</code>标签结合使用</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee907364dbbe49dc9d18d5cc7b931b84~tplv-k3u1fbpfcp-watermark.image" alt="iframe与a标签搭配使用.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable"><iframe src="#" name="xxx" frameborder="0" width="100%" height="500px"></iframe>
<a href="https://www.baidu.com" target="xxx">百度</a>
<a href="https://www.qq.com" target="xxx">腾讯</a>

a标签中的 target 属性值要与iframe标签的 name 属性值一致
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1"><code>a</code>标签</h2>
<ol>
<li>属性</li>
</ol>
<p><code>target</code></p>
<ul>
<li><code>_blank</code> ：新标签页中打开</li>
<li><code>_self</code> ：a标签当前所在页面打开</li>
<li><code>_parent</code>：当前链接的上一级页面</li>
<li><code>_top</code>：顶级窗口</li>
</ul>
<p><code>download</code></p>
<p>需要让用户下载图片或者文件，可以加上一个<code>download</code>属性，但不是所有浏览器都支持，尤其是手机浏览器。</p>
<p>例如：</p>
<pre><code class="copyable"><a href="https://i.loli.net/2021/06/13/OFfpMbmnHWUYN5d.gif" download>
下载图片
</a>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还可以指定下载文件的名字，例如：</p>
<pre><code class="copyable"><a href="https://i.loli.net/2021/06/13/OFfpMbmnHWUYN5d.gif" download="嗨，大笨蛋">
下载图片
</a>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>补充：</strong></p>
<blockquote>
<p>让浏览器下载文件由两个层面决定</p>
<ol>
<li>
<p>由HTTP响应决定：HTTP响应的<code>Content-Type</code>为<code>Content-Type: application/octet-stream</code>浏览器则会以下载的形式来接收这个请求，而不是在页面上展示。</p>
</li>
<li>
<p>在 a标签 中添加<code>download</code>属性：虽然响应的Content-Type不是<code>application/octet-stream</code>，但是依旧可以让浏览器强制下载。</p>
</li>
</ol>
</blockquote>
<p><code>herf</code></p>
<ol>
<li>网址
<ul>
<li><a href="https://google.com/" target="_blank" rel="nofollow noopener noreferrer">google.com</a></li>
<li><a href="http://google.com/" target="_blank" rel="nofollow noopener noreferrer">google.com</a></li>
<li>//google.com      [无协议网址]浏览器自动选择协议</li>
</ul>
</li>
<li>路径
<ul>
<li>相对路径</li>
<li>绝对路径</li>
</ul>
</li>
<li>伪协议
<ul>
<li><code>javascript:代码;</code></li>
<li><code>mailto:邮件</code></li>
<li><code>tel:电话</code></li>
</ul>
</li>
<li>ID
<ul>
<li>内部锚点<code>herf = "#xxx"</code></li>
</ul>
</li>
</ol>
<h2 data-id="heading-2"><code>img</code>标签</h2>
<p>作用：发出<code>get</code>请求，展示一张图片</p>
<p>常用属性：</p>
<ul>
<li><code>alt</code>：当图片无法显示时，可以显示的图片说明</li>
<li><code>src</code></li>
<li><code>height</code>：宽高只写其中一项，另一项会根据宽高比自适应</li>
<li><code>width</code>：不建议两项都写，图片会变形</li>
</ul>
<p>JS事件</p>
<p><code>onload</code> <code>onerror</code>监听图片是否加载成功</p>
<p>例如：</p>
<pre><code class="hljs language-js copyable" lang="js">html

<img id=<span class="hljs-string">"xxx"</span> src=<span class="hljs-string">"dog.png"</span> alt=<span class="hljs-string">"dog"</span>>

JavaScript

xxx.onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"加载成功"</span>)
&#125;
xxx.onerror = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"加载失败"</span>)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>响应式</p>
<p><code>max-width:100%</code></p>
<h2 data-id="heading-3"><code>table</code>标签</h2>
<p>相关标签</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ee155d3ceee40a98f8ec2e0f978a793~tplv-k3u1fbpfcp-watermark.image" alt="table相关标签.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>其中：</strong></p>
<ul>
<li><code>tr</code>：表行</li>
<li><code>th</code>：表头</li>
<li><code>td</code>：表内容</li>
<li><code><tfoot></code>：可不写</li>
</ul>
<p>相关样式</p>
<ul>
<li><code>table-layout</code>：单元格内容宽度</li>
<li><code>boder-collapse</code>：单元格间间距</li>
<li><code>boder-spacing</code>：表格线条样式</li>
</ul></div>  
</div>
            