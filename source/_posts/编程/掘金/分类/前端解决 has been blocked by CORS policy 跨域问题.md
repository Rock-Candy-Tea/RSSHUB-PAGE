
---
title: '前端解决 has been blocked by CORS policy 跨域问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eee3c281ea604b739c3fd77f4c477034~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 01:58:28 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eee3c281ea604b739c3fd77f4c477034~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">在初学Vue，今天碰到一个让我脑壳疼的跨域问题，但是在我自己写的时候，百度出了好几种方法，都试过了，没啥太大的帮助。所以想借掘金记录一下这个错误，希望下次碰到时能快速的解决问题，也希望能够给和我一样的小白，在遇到这种问题时，带来帮助。虽然掘金大部分发表作品的人都是大神级别，不过，这是我在掘金上发表的第一篇文章，不喜还请勿喷，感谢！</h4>
<p>下图为浏览器报错信息：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eee3c281ea604b739c3fd77f4c477034~tplv-k3u1fbpfcp-watermark.image" alt="00.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>错误提示信息的结果为：已被CORS策略阻止，也就是指浏览器的安全策略 <strong>同源策略</strong>。</p>
<p>同源策略规定：1. 协议名，2. 域名/ip地址，3. 端口号，要求三者完全一致。
只要有一个不一样，就是违背同源策略，产生<strong>跨域</strong>，只有全部一样，才符合同源策略。嘿嘿，不好意思，和标题扯得有点远了，那么我们继续返回正题。</p>
<p><strong>我的情况是这样的：</strong>
我用了一个百度搜索的接口，用watch去监视，然后得到它的数据。</p>
<p><strong>以下是我写的代码：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 我用的是线上引入</span>
<span class="hljs-comment">// <script src="https://cdn.bootcss.com/vue/2.6.11/vue.js"></script></span>
<span class="hljs-comment">// <script src="https://cdn.bootcdn.net/ajax/libs/axios/0.21.0/axios.js"></script></span>

<span class="hljs-comment">// html代码</span>
<div id=<span class="hljs-string">"app"</span>>
     <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"inputValue"</span> /></span></span>
     <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">""</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"百度一下"</span> /></span></span>
</div>

<span class="hljs-comment">// 网络接口(百度搜索)：https://www.baidu.com/sugrec?prod=pc&wd=1</span>
<span class="hljs-comment">// vue代码</span>
<span class="hljs-keyword">const</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">inputValue</span>: <span class="hljs-string">''</span>,
      &#125;;
    &#125;,
    <span class="hljs-comment">// 监视</span>
    <span class="hljs-attr">watch</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">inputValue</span>(<span class="hljs-params"></span>)</span> &#123;
        axios(&#123;
          <span class="hljs-attr">method</span>: <span class="hljs-string">'GET'</span>,
          <span class="hljs-attr">url</span>: <span class="hljs-string">`https://www.baidu.com/sugrec`</span>,
          <span class="hljs-attr">params</span>: &#123;
            <span class="hljs-attr">prod</span>: <span class="hljs-string">'pc'</span>,
            <span class="hljs-attr">wd</span>: <span class="hljs-built_in">this</span>.inputValue,
          &#125;,
        &#125;)
          .then(<span class="hljs-function">(<span class="hljs-params">response</span>) =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'请求成功:'</span>, response);
          &#125;)
          .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'请求失败:'</span>, err);
          &#125;);
      &#125;,
    &#125;,
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码看似没问题，但还是出现了图一中的跨域问题。</p>
<p><strong>解决方案：</strong></p>
<p>1、在桌面找到你调试用的浏览器，2、点击右键创建一个新的浏览器快捷方式，3、找到桌面快捷方式→右键→属性→快捷方式选项卡→目标，在后面追加以下 参数</p>
<blockquote>
<p>--user-data-dir="c:\ChromeDebug" --test-type --disable-web-security</p>
</blockquote>
<p>确认保存。点击快捷方式打开浏览器，在地址栏输入原来的链接地址、回车</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25cda6cfcc1b43e994e5a5315b564189~tplv-k3u1fbpfcp-watermark.image" alt="001.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Chrome浏览器如何开启Ajax跨域访问调试？<a href="https://link.juejin.cn/?target=https%3A%2F%2Fjingyan.baidu.com%2Farticle%2F148a1921c9dbf24d71c3b11f.html" target="_blank" rel="nofollow noopener noreferrer" title="https://jingyan.baidu.com/article/148a1921c9dbf24d71c3b11f.html" ref="nofollow noopener noreferrer">点击查看</a></p></div>  
</div>
            