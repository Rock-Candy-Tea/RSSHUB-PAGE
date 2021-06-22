
---
title: 'js 防抖——教你对象好好聊天法宝'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c5a983206384461a088483fb7c45b13~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 02:26:38 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c5a983206384461a088483fb7c45b13~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>emmm...,在文章开始前，我想问大家一个问题，就是 <code>当你对象在和你发消息时，把一句完整的话，拆分成一个字一个字发给你时，你当时的感受会是什么样的呢？</code></p>
<blockquote>
<p>我想，大部分的当事人内心都应该是想：我TM的怕不是找了个傻子吧！</p>
</blockquote>
<p>我们来模拟一下憨憨的对象发送信息时的场景：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- html代码片段 --></span>
<span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"wrapper"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// js代码片段</span>
<span class="hljs-keyword">const</span> input = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'input'</span>);
input.oninput = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.value)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果动图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c5a983206384461a088483fb7c45b13~tplv-k3u1fbpfcp-watermark.image" alt="demo.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>假设我们正在玩着游戏，突然你的憨憨对象一直这样在对你进行消息轰炸，我想你应该会让他(她)见识一下什么叫做砂锅大的拳头吧~</p>
<p>那么我们换位思考一下，当我们和后端进行数据请求的时候，请求的数据一直处于一个高频率更新的状态，可能会导致页面的延迟或者是卡顿，特别影响用户的体验。所以我们今天请来了一位老大哥好好的解决这个问题(让你的对象好好聊天！)</p>
<p>老大哥的自我介绍：<br>
姓名：防抖<br>
英文名：debounce<br>
真身：一个函数<br>
特长：教会你的对象怎么好好聊天~ <strong>（当你触发事件后，如果在 n 秒内，没有再次触发该事件，那么就执行函数；如果在 n 秒内，再次触发了该事件，那么就取消计时器，重新开始计时）</strong></p>
<p>我们先来看看老大哥的真身吧~</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">debounce</span>(<span class="hljs-params">fn, time</span>) </span>&#123;
    <span class="hljs-keyword">let</span> timer = <span class="hljs-literal">null</span>; <span class="hljs-comment">// 定时器的引用</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">const</span> _this = <span class="hljs-built_in">this</span>; <span class="hljs-comment">// 防止 this 指向错误，所以这边需要存一下 this 的值</span>
        <span class="hljs-keyword">const</span> args = <span class="hljs-built_in">Array</span>.from(<span class="hljs-built_in">arguments</span>);
        <span class="hljs-keyword">if</span> (timer) &#123;
            <span class="hljs-built_in">clearTimeout</span>(timer);
        &#125;
        timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            fn.apply(_this, args)
        &#125;, time)
    &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们的对象经过老大哥的教训，终于会好好聊天啦~，具体看下面的代码片段和效果图：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- html代码片段 --></span>
<span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"wrapper"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// js代码片段</span>
<span class="hljs-keyword">const</span> input = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'input'</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">debounce</span>(<span class="hljs-params">fn, time</span>) </span>&#123;
    <span class="hljs-keyword">let</span> timer = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">const</span> _this = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">const</span> args = <span class="hljs-built_in">Array</span>.from(<span class="hljs-built_in">arguments</span>);
        <span class="hljs-keyword">if</span> (timer) &#123;
            <span class="hljs-built_in">clearTimeout</span>(timer);
        &#125;
        timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            fn.apply(_this, args)
        &#125;, time)
    &#125;;
&#125;

input.oninput = debounce(
    <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.value)
    &#125;,
    <span class="hljs-number">1000</span>
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果动图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02ec5c37aadd42a281f1471c4aee4463~tplv-k3u1fbpfcp-watermark.image" alt="动画.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>嘻嘻，经过老大哥的帮助，我们那个憨憨的对象终于会好好聊天啦~</p>
<p>你们的对象还有什么小问题呀，评论区留言，下次帮你解决~<br>
公众号： 前端小轩，欢迎来给你的对象挂号治疗呀~</p></div>  
</div>
            