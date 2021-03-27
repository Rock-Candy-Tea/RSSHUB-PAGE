
---
title: '前端学习日记01——Vue解决跨域问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5768'
author: 掘金
comments: false
date: Fri, 26 Mar 2021 01:55:25 GMT
thumbnail: 'https://picsum.photos/400/300?random=5768'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前端学习日记01——<strong>Vue解决跨域问题</strong><br>
  跨域问题在前端可以说是很常见的，在解决这个问题之前，我们可以先了解为什么需要跨域。以下内容参考自MDN，链接<a href="https://developer.mozilla.org/zh-CN/docs/Web/Security/Same-origin_policy" target="_blank" rel="nofollow noopener noreferrer">：浏览器的同源策略</a>。目前因为我只试过Vue解决跨域，所以只会Vue解决方法，还有一些内容后续会改进啦！<br></p>
<h3 data-id="heading-0">浏览器的同源策略</h3>
<blockquote>
<p>  首先，跨域问题是浏览器的同源策略导致的。<b>同源策略</b>是一个重要的安全策略，它用于限制一个来源的文档或者它加载的脚本如何能与另一个源的资源进行交互。它能帮助阻隔恶意文档，减少可能被攻击的媒介。</p>
</blockquote>
<p>  简单来说就是判断脚本是不是和自己同源，只有和自己同源的脚本才会被执行，否则浏览器就会在控制台报错并且提示拒绝访问。</p>
<h3 data-id="heading-1">同源的定义</h3>
<blockquote>
<p>  如果两个 URL 的协议、端口(如果有指定的话)和域名都相同的话，则这两个 URL 是同源。这个方案也被称为“协议/主机/端口元组”，或者直接是 “元组”。（“元组” 是指一组项目构成的整体，双重/三重/四重/五重/等的通用形式）</p>
</blockquote>
<p>下表展示是否与<code>http://beijing.company.com/home/index.html</code>同源的对比</p>



































<table><thead><tr><th>被请求url</th><th>结果</th><th>原因</th></tr></thead><tbody><tr><td><code>http://beijing.company.com/company/index.html</code></td><td>同源</td><td>只有路径不同</td></tr><tr><td><code>http://beijing.company.com/company/other.html</code></td><td>同源</td><td>只有路径不同</td></tr><tr><td><code>https://beijing.company.com/company/index.html</code></td><td>不同源</td><td>协议不同</td></tr><tr><td><code>https://beijing.company.com/company:81/index.html</code></td><td>不同源</td><td>端口不同(<code>http://默认端口是80</code>)</td></tr><tr><td><code>https://shanghai.company.com/company/index.html</code></td><td>不同源</td><td>域名（主机）不同</td></tr></tbody></table>
<h3 data-id="heading-2">Vue解决跨域</h3>
<p>  在vue中一般使用proxy代理解决跨域问题。我使用的vue cli版本是4.5.9的，新版本没有原来的config文件夹，所以我们需要在项目文件夹的根目录下新建一个叫vue.config.js的配置文件，然后在里面配置proxy，代码如下。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">proxy</span>: &#123;
      <span class="hljs-string">'/api'</span>: &#123; <span class="hljs-comment">// 这里最好有一个 /</span>
        <span class="hljs-attr">target</span>: <span class="hljs-string">'http://192.168.119.193:8080'</span>, <span class="hljs-comment">// 后台接口域名</span>
        <span class="hljs-attr">changeOrigin</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 是否允许跨域 设置为true</span>
        <span class="hljs-attr">pathRewrite</span>: &#123;  <span class="hljs-comment">// 重写域名</span>
          <span class="hljs-string">'^/api'</span>: <span class="hljs-string">'/'</span>
        &#125;
      &#125;,
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在配置完之后我们用新的域名来代替原来的ip和端口就行了，如下</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">//  比如原来我们这样访问接口</span>
<span class="hljs-built_in">this</span>.$axios.get(<span class="hljs-string">"http://192.168.119.193:8080/addUser"</span>).then (
   <span class="hljs-function">(<span class="hljs-params">response</span>) =></span> &#123;
     <span class="hljs-comment">// handle success</span>
   &#125;).catch(<span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
     <span class="hljs-comment">// handle error</span>
   &#125;)
   
   <span class="hljs-comment">//  现在将接口替换成这样就行了</span>
<span class="hljs-built_in">this</span>.$axios.get(<span class="hljs-string">"/api/addUser"</span>).then (
   <span class="hljs-function">(<span class="hljs-params">response</span>) =></span> &#123;
     <span class="hljs-comment">// handle success</span>
   &#125;).catch(<span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
     <span class="hljs-comment">// handle error</span>
   &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">总结</h3>
<p>  在实现的过程中也遇到一些可能出现的问题，记得配置完之后<strong>一定要重启一下项目</strong>，我第一次弄的时候就因为这个原因浪费了很多时间，然后记得一定要在项目文件的根目录下创建配置文件。另外遇到的一些奇怪的问题：比如我在写接口的时候如果我写的是<code>api/addUser</code>我在index组件下也是可以正常访问的，但是如果在index的一个子路由组件中访问的话就会失效，但是加上前面的"/"就没问题，因此，建议大家还是写成<code>/api/addUser</code>吧！</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            