
---
title: '【前端 · input优化】关于 input file 文件控件的优化（三）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8cfe07679274e5d9cce8f072049cb0e~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 04:34:38 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8cfe07679274e5d9cce8f072049cb0e~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第4天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<blockquote>
<p>这是一个关于 input file 文件控件的优化系列，感兴趣的朋友可以关注我。对于文章有任何问题欢迎大家指正、交流。</p>
</blockquote>
<h2 data-id="heading-0">目标</h2>
<p>操作栏事件：图片放大预览，下载图片，删除图片</p>
<h2 data-id="heading-1">交互逻辑</h2>
<p>第一步：在 <code>parseDom</code> 方法里添加操作栏的 Dom 结构</p>
<pre><code class="hljs language-js copyable" lang="js">+ <span class="hljs-string">"<span class='upload__item-actions'>"</span>
+ <span class="hljs-string">"<span class='upload__icon'><i class='bi bi-zoom-in'></i></span>"</span>
+ <span class="hljs-string">"<span class='upload__icon'><i class='bi bi-download'></i></span>"</span>
+ <span class="hljs-string">"<span class='upload__icon'><i class='bi bi-trash'></i></span>"</span>
+ <span class="hljs-string">"</span>"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8cfe07679274e5d9cce8f072049cb0e~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第二步：添加样式</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.upload-list--picture-card</span> <span class="hljs-selector-class">.upload__item-actions</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">cursor</span>: default;
    <span class="hljs-attribute">text-align</span>: center;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">35px</span> <span class="hljs-number">0</span>;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,.<span class="hljs-number">5</span>);
    <span class="hljs-attribute">transition</span>: opacity .<span class="hljs-number">3s</span>;
&#125;
<span class="hljs-selector-class">.upload-list--picture-card</span> <span class="hljs-selector-class">.upload__item-actions</span> <span class="hljs-selector-tag">span</span> &#123;
    <span class="hljs-attribute">display</span>: none;
    <span class="hljs-attribute">cursor</span>: pointer;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> <span class="hljs-number">7.5px</span>;
&#125;
<span class="hljs-selector-class">.upload-list--picture-card</span> <span class="hljs-selector-class">.upload__item-actions</span><span class="hljs-selector-pseudo">:hover</span> &#123;
    <span class="hljs-attribute">opacity</span>: <span class="hljs-number">1</span>;
&#125;
<span class="hljs-selector-class">.upload-list--picture-card</span> <span class="hljs-selector-class">.upload__item-actions</span><span class="hljs-selector-pseudo">:hover</span> <span class="hljs-selector-tag">span</span> &#123;
    <span class="hljs-attribute">display</span>: inline-block;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第三步：给每个图标添加操作事件</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5d798d28e0443358d710673f3bf9ea7~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注意：三个事件都要用到<strong>事件代理</strong>，防止后面追加图片时事件无效</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">$(<span class="hljs-string">".upload-list--picture-card"</span>).on(<span class="hljs-string">'click'</span>, <span class="hljs-string">'.icon-preview'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-comment">// 图片预览</span>

&#125;);

$(<span class="hljs-string">".upload-list--picture-card"</span>).on(<span class="hljs-string">'click'</span>, <span class="hljs-string">'.icon-download'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-comment">// 图片下载</span>

&#125;);

$(<span class="hljs-string">".upload-list--picture-card"</span>).on(<span class="hljs-string">'click'</span>, <span class="hljs-string">'.icon-trash'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123; <span class="hljs-comment">// 图片删除</span>

&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">1. 图片放大预览</h3>
<blockquote>
<p>思路：1、获取图标元素的父级元素的上一个同胞元素的 <code>src</code> 属性值，2、把获取到的 <code>src</code> 属性值赋值到要预览的标签里，3、显示模态框</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mask"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mask-content"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* mask */</span>
<span class="hljs-selector-class">.mask</span> &#123;
    <span class="hljs-attribute">display</span>: none;
    <span class="hljs-attribute">position</span>: fixed;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, .<span class="hljs-number">5</span>);
&#125;
<span class="hljs-selector-class">.mask</span> <span class="hljs-selector-class">.mask-content</span> &#123;
    <span class="hljs-attribute">position</span>: fixed;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(-<span class="hljs-number">50%</span>, -<span class="hljs-number">50%</span>);
    <span class="hljs-attribute">width</span>: <span class="hljs-number">600px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">background-repeat</span>: no-repeat;
    <span class="hljs-attribute">background-size</span>: <span class="hljs-number">100%</span> <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">background-clip</span>: border-box;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">8px</span>;
    <span class="hljs-attribute">overflow</span>: hidden;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">$(<span class="hljs-string">".upload-list--picture-card"</span>).on(<span class="hljs-string">'click'</span>, <span class="hljs-string">'.icon-preview'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> preSrc = $(<span class="hljs-built_in">this</span>).parent().prev().attr(<span class="hljs-string">"src"</span>);
    $(<span class="hljs-string">".mask .mask-content"</span>).attr(<span class="hljs-string">"style"</span>, <span class="hljs-string">"background-image: url("</span> + preSrc + <span class="hljs-string">")"</span>);
    $(<span class="hljs-string">".mask"</span>).fadeIn(<span class="hljs-string">"fast"</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终效果</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eabae5a347d244eeaad5bfc105267d3f~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">2. 图片下载</h3>
<blockquote>
<p>思路：创建 <code>a</code> 标签，把 <code>src</code> 属性值赋值给 <code>a</code> 标签</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">$(<span class="hljs-string">".upload-list--picture-card"</span>).on(<span class="hljs-string">'click'</span>, <span class="hljs-string">'.icon-download'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> a = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'a'</span>);
    <span class="hljs-keyword">var</span> imgUrl = $(<span class="hljs-built_in">this</span>).parent().prev().attr(<span class="hljs-string">"src"</span>);
    a.href = imgUrl
    a.setAttribute(<span class="hljs-string">'download'</span>, imgUrl);
    a.click();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">3. 图片删除</h3>
<blockquote>
<p>思路：把 <code>uploadFile</code> 设置成全局变量，把 files 存到 uploadFile 里。 删除相应序号的图片，移除相应序号的元素节点</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba95490685704bcea35b09f3219a9040~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">$(<span class="hljs-string">".upload-list--picture-card"</span>).on(<span class="hljs-string">'click'</span>, <span class="hljs-string">'.icon-trash'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> $parent = $(<span class="hljs-built_in">this</span>).parent().parent();
    <span class="hljs-keyword">var</span> curIndex = $parent.index();
    <span class="hljs-built_in">console</span>.log(curIndex , uploadFile)
    uploadFile.splice(curIndex, <span class="hljs-number">1</span>);
    $parent.fadeOut(<span class="hljs-number">500</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        $parent.remove()
    &#125;);
    $(<span class="hljs-string">"input[type='file']"</span>).value = <span class="hljs-string">""</span>;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">未完待续</h2>
<p>三个操作事件已经完成了哈，期待下一遍，猜猜是什么</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74ee55bc869643c89b0fde321f92f6d7~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">（求关注）</h2>
<blockquote>
<p>欢迎关注我的公众号：A纲 Coder，获得日常干货推送。最后再次感谢您的阅读，我是<strong>程序猿憨憨</strong></p>
</blockquote></div>  
</div>
            