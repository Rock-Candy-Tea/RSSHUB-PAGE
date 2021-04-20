
---
title: 'Vue 实现携带 Token 免密登录验证 ——Token使用（二）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1580'
author: 掘金
comments: false
date: Tue, 20 Apr 2021 03:29:40 GMT
thumbnail: 'https://picsum.photos/400/300?random=1580'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p><code>看文章之前，强烈建议先把项目拉取下来！案例来自小弟的开源项目，这是 Token 免密登录验证的前端实现。</code><a href="https://github.com/KiteWorld/KiteBlog" target="_blank" rel="nofollow noopener noreferrer">「项目Github」</a></p>
<p><code>文章内容只是个人学习的一些总结经验，不具有权威性，强烈建议先移步：</code><a href="https://juejin.cn/post/6932374305758167054" target="_blank">NodeJS（Express框架）实现 Token 验证免密登录 (一)</a></p>
<h2 data-id="heading-1">Token 免密登录前端原理</h2>
<p>在用户第一次登录成功的时候，后端会返回一个 <code>Token</code>，这个值<code>Token</code> 主要的作用就是用于识别用户的身份。相当于账号密码。正常情况下，前端给后端发送请求的时候，后端都需要先判断用户的身份，来返回相应的数据给用户。但我们不可能每次请求的时候都要用户输入一次账号和密码。为了便于理解，你可以看成 <code>Token</code> ≈ 用户输入账号和密码 （当然这不太严谨）。获取到<code>Token</code>后，你需要把 <code>Token</code> 存在 <code>Cookie</code>中。接着向服务器发送请求时，你从  <code>Cookie</code> 中取出 <code>Token</code>，在请求头中携带上  <code>Token</code> ，就搞定了！</p>
<p>还可以用 vue-router 提供的<code>beforeEach</code>方法配合 <code>Token</code>进行简单的权限控制。例如：<code>Token</code>过期跳转到登录页。后面说权限控制的时候再写。</p>
<h2 data-id="heading-2">安装  js-cookie  和  安装 axios （http库）</h2>
<p><code>js-cookie</code>一个简化 <code>cookie</code>增删改查的 JS 库，</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//安装js-cookie</span>
npm i js-cookie -S 

<span class="hljs-comment">//安装axios</span>
npm i axios -S 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>js-cookie 和 axios 的使用比较简单，就不详细说明和例子一起看。详细文档：<a href="https://github.com/js-cookie/js-cookie" target="_blank" rel="nofollow noopener noreferrer">「js-cookie」</a><a href="http://www.axios-js.com/zh-cn/docs/" target="_blank" rel="nofollow noopener noreferrer">「axios」</a></p>
<h2 data-id="heading-3">登录并获取 Token</h2>
<p>我们直接看例子</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Cookies <span class="hljs-keyword">from</span> <span class="hljs-string">"js-cookie"</span>;
<span class="hljs-keyword">import</span> &#123; adminLogin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@/api/api"</span>;

<span class="hljs-function"><span class="hljs-title">submit</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.$refs.form.validate(<span class="hljs-keyword">async</span> (valid) => &#123;
        <span class="hljs-comment">// valid 为 false 时，表单校验通过（element-ui Form组件）</span>
        <span class="hljs-keyword">if</span> (!valid) <span class="hljs-keyword">return</span>;
        <span class="hljs-comment">//调用登录接口，并把用户的账号密码传给后端</span>
        <span class="hljs-keyword">let</span> res = <span class="hljs-keyword">await</span> adminLogin(<span class="hljs-built_in">this</span>.loginForm);
        <span class="hljs-keyword">if</span> (res.code !== <span class="hljs-number">0</span>) &#123;
          <span class="hljs-built_in">this</span>.$message.error(res.msg);
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-comment">//在返回的结果中获取到 token，并存放在 Cookie 中</span>
          <span class="hljs-comment">//Cookies.set(key,data) 是 `js-cookie`提供的存放 Cookie 的方法  </span>
          Cookies.set(<span class="hljs-string">"token"</span>, res.data.token); 
          <span class="hljs-comment">//Cookies.set("token", res.data.token, &#123; expires: 7 &#125;);</span>
          <span class="hljs-comment">//这里可以设置一下过期时间，最好比后端规定的时间早</span>
          Cookies.set(<span class="hljs-string">"name"</span>, res.data.name);
          Cookies.set(<span class="hljs-string">"userId"</span>, res.data.userId || <span class="hljs-string">""</span>);
          Cookies.set(<span class="hljs-string">"role"</span>, res.data.role);
          <span class="hljs-comment">//登录成功跳转到网站首页</span>
          <span class="hljs-built_in">this</span>.$router.replace(&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">"/"</span> &#125;);
        &#125;
      &#125;);
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里我们就已经拿到 token了。</p>
<h2 data-id="heading-4">配置 Token</h2>
<p><code>KiteBlog</code> axios 一些全局的配置都存放在<code>src\utils\request.js</code>中，所以像<code>Token</code>这种几乎所有请求都需要携带的数据，放在<code>request.js</code>是比较合适的。</p>
<p><code>axios</code> 提供了拦截器的功能。详细移步：<a href="http://www.axios-js.com/zh-cn/docs/#%E6%8B%A6%E6%88%AA%E5%99%A8" target="_blank" rel="nofollow noopener noreferrer">拦截器</a>。这里只用到<code>请求拦截器「axios.interceptors.request.use()」</code>，顾名思义，就是在发送请求前经进行拦截，然后修改请求的数据，例如：请求头（header）、body 等数据。 前面说过，<code>Token</code>是存在请求头中的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">axios.interceptors.request.use(<span class="hljs-function">(<span class="hljs-params">config</span>) =></span> &#123;
<span class="hljs-comment">//排除登录接口，登录是不需要 Token 的，只有登录了才能获取到 Token</span>
    <span class="hljs-keyword">if</span> (config.url !== <span class="hljs-string">"auth/adminLogin"</span>) &#123;
        <span class="hljs-comment">//给请求头的设置Token, Cookies.get()用于获取存放在 Cookie 的 Token</span>
config.headers[<span class="hljs-string">"authorization"</span>] = <span class="hljs-string">`Bearer <span class="hljs-subst">$&#123;Cookies.get(<span class="hljs-string">"token"</span>)&#125;</span>`</span>;
&#125;
    <span class="hljs-comment">//这一步是必须的！</span>
<span class="hljs-keyword">return</span> config
&#125;, <span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就搞定了，是不是很简单</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            