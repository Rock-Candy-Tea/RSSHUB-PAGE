
---
title: '前端基础四之JavaScriptDOM与事件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dded780bef8e4b548f49b456ecab1d7e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 18:20:38 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dded780bef8e4b548f49b456ecab1d7e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第17天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dded780bef8e4b548f49b456ecab1d7e~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">前言</h1>
<p>身为一个合格的后端开发人员</p>
<p>前端的基础知识也是需要了解的</p>
<h1 data-id="heading-1">1. JavaScriptDOM</h1>
<p>DOM是文档对象模型。</p>
<p>在我的理解里，这个类似于css的选择器。</p>
<p>你可以通过语法找到与之对应的标签，并修改其中的内容。</p>
<p>当然，DOM不仅可以匹配到HTML标签，他也能匹配到css的语法，并且可以修改。</p>
<h2 data-id="heading-2">1.1 HTML的DOM</h2>
<p>可以通过HTML的id和标签名改变HTML内容，与css只能改变样式不同</p>
<p>js的含有一个方法，<code>document.getElementById();</code>可以绑定拥有该id属性的标签</p>
<p>然后可以通过别的函数来修改HTML的内容</p>
<p>代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Title<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"ate"</span>></span>
    阿达是大大大是灵魂法师法哦
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"https://www.baidu.com"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"at"</span>></span>
    百度
<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> ate = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"ate"</span>);
    ate.innerHTML=<span class="hljs-string">"通过js修改！！！！！！"</span>;
    <span class="hljs-keyword">let</span> at = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"at"</span>);
    at.href=<span class="hljs-string">"https://blog.csdn.net/m0_52883898"</span>;  <span class="hljs-comment">// 修改属性</span>
    at.innerText=<span class="hljs-string">"这也可以改"</span>;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>显示效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18064f014bed4113bd877dce526c79d6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">1.2 css的DOM</h2>
<p>js的DOM不仅可以修改HTML的内容，还能修改css</p>
<p>格式就是：<code>document.ElementsById("idName").style.样式=XXX;</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Title<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-tag">p</span>&#123;
        collapse: red;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"ate"</span>></span>
    阿达是大大大是灵魂法师法哦
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> ate = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"ate"</span>);
    ate.innerHTML=<span class="hljs-string">"通过js修改！！！！！！"</span>;
    ate.style.color=<span class="hljs-string">"blue"</span>;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">1.3 事件</h2>
<p>事件就是，单击，双击，鼠标悬停，等</p>
<p>而事件需要先注册（绑定），才能进行操作</p>
<p>比如说我们可以对一个按钮设置单击后会怎么样之类的</p>
<h3 data-id="heading-5">1.3.1 注册</h3>
<p>事件分为静态注册和动态注册</p>
<p>静态注册就是直接在HTML代码的属性中写js的事件函数</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Title<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span> <span class="hljs-attr">onload</span>=<span class="hljs-string">"alert('加载完成，感谢等待');"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>aaa<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>而动态注册就是先通过获取DOM对象，然后再编写函数</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Title<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"bu1"</span>></span>请点击<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> bu1=<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'bu1'</span>);
    bu1.onclick=<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;
        alert(<span class="hljs-string">"让你点你就点啊，哈哈"</span>);
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">1.3.2 事件</h3>
<p>事件有很多，这里只讲其中的部分以作了解</p>
<ul>
<li>onload事件：页面加载完成后执行</li>
<li>onclick事件：单击后执行</li>
<li>onmouseover事件：鼠标悬停至目的地后执行</li>
<li>onchange事件：离开输入框后执行</li>
</ul>
<ol>
<li>
<p>onload事件实例</p>
<p>会在页面加载完html文件后，先执行onload代码，再显示段落</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Title<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span> <span class="hljs-attr">onload</span>=<span class="hljs-string">"alert('加载完成，感谢等待');"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>aaa<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>onclick事件</p>
<p>在点击按钮后，会执行下面的函数</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Title<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"bu1"</span>></span>请点击<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> bu1=<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'bu1'</span>);
    bu1.onclick=<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;
        alert(<span class="hljs-string">"让你点你就点啊，哈哈"</span>);
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>onmoseover鼠标移过去后会执行</p>
<p>会将<strong>请宠幸我</strong>变为<strong>谢谢宠幸</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Title<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"rete"</span>></span>请宠幸我<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">let</span> rete=<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'rete'</span>);
  rete1=<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;
    rete.innerText=<span class="hljs-string">"谢谢宠幸"</span>;
  &#125;
  rete.onmousemove=rete1;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>onchange事件</p>
<p>在你输入完成后，会将你的输入更改</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Title<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">label</span>></span>
  账号：<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"input1"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>></span>
  密码：<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"input2"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"password"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">label</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> input1=<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'input1'</span>);
  <span class="hljs-keyword">const</span> input2=<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'input1'</span>);
  inputChange = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;
    input1.value=<span class="hljs-string">"强行更改了账号"</span>;
    input2.value=<span class="hljs-string">"强行更改了密码"</span>;
  &#125;
  input1.onchange=inputChange;
  input2.onchange=inputChange;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h1 data-id="heading-7">结语</h1>
<p>兴趣是最好的老师，坚持是不变的真理。
学习不要急躁，一步一个脚印，踏踏实实的往前走。
每天进步一点点，日积月累之下，你就会发现自己已经变得很厉害了。</p>
<p>我是布小禅，一枚自学萌新，跟着我每天进步一点点吧！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c322d219427e46cabccb715684b326c0~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            