
---
title: 'vue+element-统一管理线上线下接口'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8569'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 22:47:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=8569'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h5 data-id="heading-0"><a href="https://juejin.cn/post/6943479646008639519"></a>需求分析</h5>
<blockquote>
<p>我们在使用后端提供的接口的过程中，都是先在线下测试结束，没有问题以后才会将代码部署到线上，这样才保证线上的代码是没有问题的。所以如果只有一个接口和一个页面的话，那么是无所谓的， 要不要统一管理都是一样的，但是一旦接口和页面多的话，就会比较麻烦了，所以我们需要统一一个文件进行管理这些接口，这样可以不管是线上还是线下的跑项目，都是可以直接执行的，也不会出现更改过多的问题。</p>
</blockquote>
<h5 data-id="heading-1"><a href="https://juejin.cn/post/6943479646008639519"></a>实现思路</h5>
<blockquote>
<p>我们在config文件里面新建一个管理api的js，这样可以进行统一设置，在我们系统目录下面进行更改dev.env.js和prod.env.js里面进行添加自己需要的线上和线下的接口</p>
</blockquote>
<h5 data-id="heading-2"><a href="https://juejin.cn/post/6943479646008639519"></a>代码实现</h5>
<h6 data-id="heading-3"><a href="https://juejin.cn/post/6943479646008639519"></a>dev.env.js</h6>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">'use strict'</span>
<span class="hljs-keyword">const</span> merge = <span class="hljs-built_in">require</span>(<span class="hljs-string">'webpack-merge'</span>)
<span class="hljs-keyword">const</span> prodEnv = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./prod.env'</span>)

<span class="hljs-comment">/*module.exports = merge(prodEnv, &#123;
 NODE_ENV: '"development"'
&#125;)*/</span>
<span class="hljs-built_in">module</span>.exports = merge(prodEnv, &#123;
 <span class="hljs-attr">NODE_ENV</span>: <span class="hljs-string">'"development"'</span>,<span class="hljs-comment">//开发环境</span>
 <span class="hljs-attr">api_9101</span> : <span class="hljs-string">'"http://47.98.113.173:9101"'</span>,  <span class="hljs-comment">//房价码的线下接口</span>
 <span class="hljs-attr">api_9102</span> : <span class="hljs-string">'"http://47.98.113.173:9102"'</span>,  <span class="hljs-comment">//会员的线下接口</span>
 <span class="hljs-attr">api_9519</span> : <span class="hljs-string">'"http://47.98.113.173:9519"'</span>,  <span class="hljs-comment">//登陆的线下接口</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-4"><a href="https://juejin.cn/post/6943479646008639519"></a>prod.env.js</h6>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">'use strict'</span>
<span class="hljs-comment">/*module.exports = &#123;
 NODE_ENV: '"production"'
&#125;*/</span>
<span class="hljs-built_in">module</span>.exports = &#123;
 <span class="hljs-attr">NODE_ENV</span>: <span class="hljs-string">'"production"'</span>,<span class="hljs-comment">//生产环境</span>
 <span class="hljs-attr">api_price</span> : <span class="hljs-string">'"http://price.crowncrystalhotel.com"'</span>,   <span class="hljs-comment">//房价码的线上接口</span>
 <span class="hljs-attr">api_member</span> : <span class="hljs-string">'"http://member.crowncrystalhotel.com"'</span>, <span class="hljs-comment">//会员的线上接口</span>
 <span class="hljs-attr">api_9022</span> :<span class="hljs-string">'"http://47.98.113.173:9022"'</span>,<span class="hljs-comment">//登陆的线上接口</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-5"><a href="https://juejin.cn/post/6943479646008639519"></a>api.js</h6>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">/**
* 线下接口
* <span class="hljs-doctag">@type <span class="hljs-type">&#123;string&#125;</span></span>
*/</span>
<span class="hljs-keyword">const</span> api_9519 = process.env.api_9519;  <span class="hljs-comment">//登陆的线下接口  徐哥的所有的线下接口</span>
<span class="hljs-keyword">const</span> api_9101 = process.env.api_9101;  <span class="hljs-comment">//房价码的线下接口</span>
<span class="hljs-keyword">const</span> api_9102 = process.env.api_9102;  <span class="hljs-comment">//会员的线下接口</span>

<span class="hljs-comment">/**
* 线上接口
* <span class="hljs-doctag">@type <span class="hljs-type">&#123;string&#125;</span></span>
*/</span>

<span class="hljs-keyword">const</span> api_9022 = process.env.api_9022;         <span class="hljs-comment">//登陆的线上接口   徐哥所有的线下接口</span>
<span class="hljs-keyword">const</span> api_price = process.env.api_price;       <span class="hljs-comment">//房价码的线上接口</span>
<span class="hljs-keyword">const</span> api_member = process.env.api_member;     <span class="hljs-comment">//会员的线上接口</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
 <span class="hljs-comment">/**
  * 线上接口
  */</span>
  <span class="hljs-attr">api_9022_9519</span> : api_9022,
  <span class="hljs-attr">api_price_9101</span> : api_price,
  <span class="hljs-attr">api_member_9102</span> : api_member,
  
 <span class="hljs-comment">/**
  * 线下接口
  */</span>
  <span class="hljs-comment">/*api_9022_9519 : api_9519,
  api_price_9101 : api_9101,
  api_member_9102 : api_9102,*/</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>当然这里的接口的数量是不上限的，可以一直加，只要是你们的环境是存在的接口。api.js<br>
是我自己新建的，你们自己喜欢用什么都可以。</p>
</blockquote>
<h6 data-id="heading-6"><a href="https://juejin.cn/post/6943479646008639519"></a>main.js</h6>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> api <span class="hljs-keyword">from</span> <span class="hljs-string">'../config/api'</span>
Vue.prototype.api = api;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7"><a href="https://juejin.cn/post/6943479646008639519"></a>引用</h5>
<pre><code class="hljs language-js copyable" lang="js">handleLogin : <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
&#123;
        <span class="hljs-keyword">let</span> that = <span class="hljs-built_in">this</span>;
        <span class="hljs-comment">/**
         * 常规登录  && code.trim().length > 0
         */</span>
        <span class="hljs-keyword">if</span>(that.check_login === <span class="hljs-string">'login_flag'</span>)&#123;
          <span class="hljs-keyword">let</span> url =  that.api.api_9022_9519 + <span class="hljs-string">'/v1/common/employee/login'</span>;
          <span class="hljs-keyword">let</span> username = <span class="hljs-built_in">this</span>.account.username;
          <span class="hljs-keyword">let</span> pwd = <span class="hljs-built_in">this</span>.account.pwd;
          <span class="hljs-keyword">let</span> code = <span class="hljs-built_in">this</span>.account.code;
          <span class="hljs-keyword">if</span>(username.trim().length > <span class="hljs-number">0</span> && pwd.trim().length > <span class="hljs-number">0</span>)&#123;
            <span class="hljs-built_in">this</span>.$axios(&#123;
              <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,
              <span class="hljs-attr">url</span>: url,
              <span class="hljs-attr">data</span>: &#123;
                <span class="hljs-attr">code</span>: code,
                <span class="hljs-attr">user_name</span>: username,
                <span class="hljs-attr">password</span>: that.getmd5(pwd),
              &#125;
            &#125;).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
              <span class="hljs-built_in">console</span>.info(res);
              <span class="hljs-keyword">if</span>(res.data.message === <span class="hljs-string">"success"</span>) &#123;
                sessionStorage.setItem(<span class="hljs-string">"root_level"</span>,res.data.root_level);
                sessionStorage.setItem(<span class="hljs-string">"rules"</span>,<span class="hljs-built_in">JSON</span>.stringify(res.data.rules));
                <span class="hljs-built_in">localStorage</span>.setItem(<span class="hljs-string">'access-user'</span>, <span class="hljs-built_in">JSON</span>.stringify(res.data.real_name));
                <span class="hljs-built_in">localStorage</span>.setItem(<span class="hljs-string">'userInfo'</span>, <span class="hljs-built_in">JSON</span>.stringify(res.data.user_info));
                that.$router.push(&#123;
                  <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>
                &#125;);
              &#125; <span class="hljs-keyword">else</span> &#123;
                that.$message(&#123;
                  <span class="hljs-attr">message</span>: <span class="hljs-string">'登录失败'</span>,
                  <span class="hljs-attr">type</span>: <span class="hljs-string">'warning'</span>
                &#125;);
                <span class="hljs-comment">//this.loading = false;</span>
                <span class="hljs-comment">//console.info(data.data.message);</span>
                <span class="hljs-comment">//this.$message.error("登录失败，账号或密码错误");</span>
              &#125;
            &#125;).catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err</span>) </span>&#123;
              that.$message(&#123;
                <span class="hljs-attr">message</span>: <span class="hljs-string">'登录失败'</span>,
                <span class="hljs-attr">type</span>: <span class="hljs-string">'warning'</span>
              &#125;);
            &#125;)
          &#125;
      &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>当然你的url也可以在你的return里面定义，这样一个页面上的所有就可以再次统一一下，举个例子：</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">return</span> &#123;
<span class="hljs-attr">url</span> : <span class="hljs-built_in">this</span>.api_9022_9519,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么下面用的就可以直接that.url就可以了。<br>
<em>哪里不明白的可以私信我，或者下方留言，看到了都会回复的，或者关注一下，一起学习！</em></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            