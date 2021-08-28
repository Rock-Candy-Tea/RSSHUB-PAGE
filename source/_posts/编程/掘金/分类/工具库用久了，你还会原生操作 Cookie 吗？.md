
---
title: '工具库用久了，你还会原生操作 Cookie 吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7a9fb26970f4802a8e56d3f2385aec3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 04:41:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7a9fb26970f4802a8e56d3f2385aec3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第28天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<blockquote>
<p>用得好了，工具库和框架确实是一大助力，但就怕我们会因此习惯了走捷径，而忘了自己的根本依靠是什么。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7a9fb26970f4802a8e56d3f2385aec3~tplv-k3u1fbpfcp-watermark.image" alt="Cookie" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">前言</h2>
<p>前端技术的飞速发展，给从业人员不可避免地带来了“疲劳”感，我们常常会感叹学不动了。于是，为了给我们“减压”，各种工具库和框架们诞生了。</p>
<p>对公司来说，通过工具库和框架的引入，一方面是约束了代码风格，提高了可维护性，最重要的是可以缩短开发周期，早日出成品。</p>
<p>对个人来说，各种工具库和框架用起来简直不要太爽，再也不用哼哧哼哧地啃那些原生的操作方法了，既解放了脑力，又多出了摸鱼的时间，还不用考虑方法的准确性……一箭多雕的买卖简直是太划算了！</p>
<p>公司是追求效益的，主张引入工具库和框架无可厚非，可如果我们个人也沉迷于此，那就真的有问题了。</p>
<p>固然，我们不能否认工具库和框架的优势，但能作为我们前进基石的永远不可能是工具库和框架。</p>
<p>用得好了，工具库和框架确实是一大助力，但就怕我们会因此习惯了走捷径，而忘了自己的根本依靠是什么。</p>
<p>感慨有点多，但确实是有感而发。今天有测试组的同事找我给他们写一个记住密码的脚本，因为考虑到功能简单，没必要引入工具库，就使用原生操作来实现，结果，我竟然写地磕磕绊绊，中途还不得不上网查资料。就这么一个简单的实现，何至于此啊！？</p>
<p>饭来张口的日子过多了，就忘了怎么做饭了！我真想知道，如果当某一天没了“饭源”时，我们会有多少人被“饿死”？</p>
<h2 data-id="heading-1">Cookie 的操作</h2>
<p>关于 Cookie 的相关概念，若有需要，可查看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FHTTP%2FCookies" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Cookies" ref="nofollow noopener noreferrer">这里</a> 和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2Fcookie%2F1119" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/cookie/1119" ref="nofollow noopener noreferrer">这里</a>。</p>
<h3 data-id="heading-2">设置 Cookie</h3>
<p>Cookie 的设置需要包含以下属性：</p>
<ul>
<li><strong>key</strong>    String 类型</li>
<li><strong>value</strong>    String 类型</li>
<li><strong>expires</strong>   可选，符合 HTTP-date 规范的时间戳，也可设置 max-age（数字，单位为秒）。设置则为<strong>持久性 Cookie</strong>，缺省则为<strong>会话期 Cookie</strong>。</li>
<li><strong>path</strong>  可选，String 类型</li>
<li><strong>domain</strong>  可选，String 类型</li>
<li><strong>secure</strong> 可选，String 类型</li>
</ul>
<p>一个简单的设置 Cookie 的方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setCookieItem</span>(<span class="hljs-params">sKey, sValue, vEnd, sPath, sDomain, bSecure</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!sKey || <span class="hljs-regexp">/^(?:expires|max\-age|path|domain|secure)$/i</span>.test(sKey)) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
    &#125;
    <span class="hljs-keyword">var</span> sExpires = <span class="hljs-string">""</span>;
    <span class="hljs-keyword">if</span> (vEnd) &#123;
        <span class="hljs-keyword">switch</span> (vEnd.constructor) &#123;
            <span class="hljs-keyword">case</span> <span class="hljs-built_in">Number</span>:
                sExpires = vEnd === <span class="hljs-literal">Infinity</span> 
                    ? <span class="hljs-string">"; expires=Fri, 31 Dec 9999 23:59:59 GMT"</span> 
                : <span class="hljs-string">"; max-age="</span> + vEnd;
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> <span class="hljs-built_in">String</span>:
                sExpires = <span class="hljs-string">"; expires="</span> + vEnd;
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> <span class="hljs-built_in">Date</span>:
                sExpires = <span class="hljs-string">"; expires="</span> + vEnd.toUTCString();
                <span class="hljs-keyword">break</span>;
        &#125;
    &#125;
    <span class="hljs-built_in">document</span>.cookie = <span class="hljs-built_in">encodeURIComponent</span>(sKey) 
        + <span class="hljs-string">"="</span> + <span class="hljs-built_in">encodeURIComponent</span>(sValue) 
        + sExpires 
        + (sDomain ? <span class="hljs-string">"; domain="</span> + sDomain : <span class="hljs-string">""</span>) 
        + (sPath ? <span class="hljs-string">"; path="</span> + sPath : <span class="hljs-string">""</span>) 
        + (bSecure ? <span class="hljs-string">"; secure"</span> : <span class="hljs-string">""</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">是否存在 Cookie</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isCookieItemExisted</span>(<span class="hljs-params">sKey</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">"(?:^|;\\s*)"</span> + <span class="hljs-built_in">encodeURIComponent</span>(sKey).replace(<span class="hljs-regexp">/[-.+*]/g</span>, <span class="hljs-string">"\\$&"</span>) + <span class="hljs-string">"\\s*\\="</span>).test(<span class="hljs-built_in">document</span>.cookie);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">删除 Cookie</h3>
<p>删除  Cookie 只需要将其过期时间expires 设为过去的时间即可，也可以通过设置 max-age 为 0 或 -1 来删除 Cookie：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">removeCookieItem</span>(<span class="hljs-params">sKey, sPath, sDomain</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!sKey || !isCookieItemExisted(sKey)) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
    &#125;
    <span class="hljs-built_in">document</span>.cookie = <span class="hljs-built_in">encodeURIComponent</span>(sKey) 
        + <span class="hljs-string">"=; expires=Thu, 01 Jan 1970 00:00:00 GMT"</span> 
        + (sDomain ? <span class="hljs-string">"; domain="</span> + sDomain : <span class="hljs-string">""</span>) 
        + (sPath ? <span class="hljs-string">"; path="</span> + sPath : <span class="hljs-string">""</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">查找 Cookie</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getCookieByKey</span>(<span class="hljs-params">sKey</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">decodeURIComponent</span>(<span class="hljs-built_in">document</span>.cookie.replace(<span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">"(?:(?:^|.*;)\\s*"</span> + <span class="hljs-built_in">encodeURIComponent</span>(sKey).replace(<span class="hljs-regexp">/[-.+*]/g</span>, <span class="hljs-string">"\\$&"</span>) + <span class="hljs-string">"\\s*\\=\\s*([^;]*).*$)|^.*$"</span>), <span class="hljs-string">"$1"</span>)) || <span class="hljs-literal">null</span>;
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">总结</h2>
<p>别人造的轮子或许好用，但为了提升自己，我们最好也应该试着自己造造轮子，即使粗糙，但那也是自己的。</p>
<p>~</p>
<p>~本文完，感谢阅读！</p>
<p>~</p>
<blockquote>
<p>学习有趣的知识，结识有趣的朋友，塑造有趣的灵魂！</p>
<p>大家好，我是〖<a href="https://juejin.cn/user/2893570333750744/posts" target="_blank" title="https://juejin.cn/user/2893570333750744/posts">编程三昧</a>〗的作者 <strong>隐逸王</strong>，我的公众号是『<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fyinyiwang%2FblogImages%2Fraw%2Fmaster%2Fimages%2F20210604%2520%2F19-26-03-txvEvM.png" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/yinyiwang/blogImages/raw/master/images/20210604%20/19-26-03-txvEvM.png" ref="nofollow noopener noreferrer">编程三昧</a>』，欢迎关注，希望大家多多指教！</p>
<p>你来，怀揣期望，我有墨香相迎！ 你归，无论得失，唯以余韵相赠！</p>
<p>知识与技能并重，内力和外功兼修，理论和实践两手都要抓、两手都要硬！</p>
</blockquote></div>  
</div>
            