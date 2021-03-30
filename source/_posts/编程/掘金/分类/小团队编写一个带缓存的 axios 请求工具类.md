
---
title: '小团队编写一个带缓存的 axios 请求工具类'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1411'
author: 掘金
comments: false
date: Tue, 30 Mar 2021 01:15:58 GMT
thumbnail: 'https://picsum.photos/400/300?random=1411'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">背景</h4>
<p>公司小项目尤其多，每次新建项目都要封装一次axios，每个人封装方法也不一样，有的时候也会用到uniapp写小程序，所以为了统一使用体验，封装了一个符合公司风格的小框架。</p>
<h4 data-id="heading-1">功能</h4>
<ul>
<li>警告和错误回调</li>
<li>Loading回调</li>
<li>返回结果格式化</li>
<li>请求缓存</li>
</ul>
<h4 data-id="heading-2">使用</h4>
<ol start="0">
<li>
<p>安装</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install bdjf_http -s
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>初始化</p>
</li>
</ol>
<ul>
<li>
<p>引入 HttpUtil 和 axios</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123;HttpUtil&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"bdjf_http"</span>;
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">"axios"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>初始化 HttpUtil 的 axios，你需要传入一个 axios 实例给 HttpUtil</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 使用自己的baseUrl</span>
<span class="hljs-keyword">const</span> baseUrl = process.env.VUE_APP_SERVER;
<span class="hljs-keyword">const</span> axiosInstance = axios.create(&#123;
<span class="hljs-attr">baseURL</span>: baseUrl,
<span class="hljs-attr">timeout</span>: <span class="hljs-number">5000</span>,
<span class="hljs-attr">headers</span>: &#123;<span class="hljs-string">'Content-Type'</span>: <span class="hljs-string">'application/x-www-form-urlencoded'</span>&#125;
&#125;);
HttpUtil.setAxios(axiosInstance);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>设置HttpUtil，通过 initConfig 方法设置如何解析后端返回的数据和数据错误时如何弹出提示</p>
<ul>
<li>initConfig 传参说明</li>
</ul>


















































<table><thead><tr><th align="left">字段</th><th align="left">类型</th><th align="left">说明</th></tr></thead><tbody><tr><td align="left">codeName</td><td align="left">string</td><td align="left">用于匹配接口返回字段中的'code'</td></tr><tr><td align="left">msgName</td><td align="left">string</td><td align="left">用于匹配接口返回字段中的'msg'</td></tr><tr><td align="left">dataName</td><td align="left">string</td><td align="left">用于匹配接口返回字段中的'data'</td></tr><tr><td align="left">successCode</td><td align="left">number</td><td align="left">回复正常时code的值</td></tr><tr><td align="left">showError</td><td align="left">(string)=>&#123;&#125;</td><td align="left">调用报错时的回调，一般为网络错误</td></tr><tr><td align="left">showWarn</td><td align="left">(string)=>&#123;&#125;</td><td align="left">接口抛出的错误，code不为0时会走此回调</td></tr><tr><td align="left">codeshowLoadingName</td><td align="left">()=>&#123;&#125;</td><td align="left">发送请求前回调</td></tr><tr><td align="left">hideLoading</td><td align="left">()=>&#123;&#125;</td><td align="left">请求结束后回调</td></tr></tbody></table>
<pre><code class="hljs language-typescript copyable" lang="typescript">HttpUtil.initConfig(&#123;
   <span class="hljs-attr">codeName</span>:<span class="hljs-string">'code'</span>,
   <span class="hljs-attr">msgName</span>:<span class="hljs-string">'msg'</span>,
   <span class="hljs-attr">dataName</span>:<span class="hljs-string">'data'</span>,
   <span class="hljs-attr">successCode</span>:<span class="hljs-number">0</span>,
   <span class="hljs-function"><span class="hljs-title">showError</span>(<span class="hljs-params">error</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.error(error);
   &#125;,
   <span class="hljs-function"><span class="hljs-title">showWarn</span>(<span class="hljs-params">msg</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.warn(msg);
   &#125;,
   <span class="hljs-function"><span class="hljs-title">showLoading</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'----showLoading----'</span>);
   &#125;,
   <span class="hljs-function"><span class="hljs-title">hideLoading</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'----loadComplete----'</span>);
   &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<ol start="2">
<li>设置 HEADER</li>
</ol>
<p>你可以选择在初始化时通过给 axios 设置 header，但是很多时候还需要在登录完成后在header里添加自定义的token来鉴权</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">HttpUtil.setAxiosHeader(<span class="hljs-string">'token'</span>,<span class="hljs-string">'123456'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>
<p>简单封装</p>
<p>完成上面的初始化设置，我们就可以正式使用了。为了方便使用，我们可以创建一个 API 清单，API类的每一个方法都会返回一个
RequestBean 对象
RequestBean 的构造函数接受三个参数:</p>





























<table><thead><tr><th align="left">参数</th><th align="left">类型</th><th align="left">说明</th><th align="left">必填</th></tr></thead><tbody><tr><td align="left">url</td><td align="left">string</td><td align="left">接口的url</td><td align="left">是</td></tr><tr><td align="left">requestOpt</td><td align="left">RequestOption</td><td align="left">用于配置接口调用</td><td align="left">否</td></tr><tr><td align="left">cacheOpt</td><td align="left">CacheOption</td><td align="left">用于配置缓存功能</td><td align="left">否</td></tr></tbody></table>
<p> RequestOption 详细信息</p>








































<table><thead><tr><th align="left">属性</th><th align="left">类型</th><th align="left">说明</th><th align="left">必填</th><th align="left">默认值</th></tr></thead><tbody><tr><td align="left">method</td><td align="left">string</td><td align="left">接口请求的方法，可选值与axios支持的相同</td><td align="left">否</td><td align="left">POST</td></tr><tr><td align="left">attributeMapping</td><td align="left">AttributeMapping</td><td align="left">用于配置单独的数据映射</td><td align="left">否</td><td align="left">null</td></tr><tr><td align="left">showLoading</td><td align="left">boolean</td><td align="left">用于配置缓存功能</td><td align="left">否</td><td align="left">true</td></tr><tr><td align="left">catchErrorToast</td><td align="left">boolean</td><td align="left">用于配置缓存功能</td><td align="left">否</td><td align="left">true</td></tr></tbody></table>
<p> AttributeMapping 详细信息</p>





























<table><thead><tr><th align="left">属性</th><th align="left">类型</th><th align="left">说明</th><th align="left">必填</th></tr></thead><tbody><tr><td align="left">code</td><td align="left">string</td><td align="left">映射接口数据中的code</td><td align="left">是</td></tr><tr><td align="left">msg</td><td align="left">string</td><td align="left">映射接口数据中的msg</td><td align="left">是</td></tr><tr><td align="left">data</td><td align="left">string</td><td align="left">映射接口数据中的data</td><td align="left">是</td></tr></tbody></table>
<p> CacheOption 详细信息</p>

































<table><thead><tr><th align="left">属性</th><th align="left">类型</th><th align="left">说明</th><th align="left">必填</th><th align="left">默认值</th></tr></thead><tbody><tr><td align="left">needCache</td><td align="left">boolean</td><td align="left">是否需要缓存</td><td align="left">是</td><td align="left">true</td></tr><tr><td align="left">bindCacheKey</td><td align="left">string[]</td><td align="left">缓存数据时所依据的字段</td><td align="left">[]</td><td align="left"></td></tr><tr><td align="left">conflictCacheUrl</td><td align="left">RequestBean[]</td><td align="left">配置调用哪些接口要清空缓存当前url下面的</td><td align="left">[]</td><td align="left"></td></tr></tbody></table>
<p>一个简单的例子</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; RequestBean &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'bdjf_http'</span>
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">API</span></span>&#123;
   <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> loginWithCode(): RequestBean&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> RequestBean(<span class="hljs-string">'/wxapi/loginWithCode'</span>,&#123;<span class="hljs-attr">showLoading</span>:<span class="hljs-literal">true</span>&#125;)
   &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你还需要再次封装 HttpUtil 的请求方法，比如你需要在每次请求时在数据中加上userId，可以这么做</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123;HttpUtil, ResponseBean&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'bdjf_http'</span>
<span class="hljs-keyword">import</span> Store <span class="hljs-keyword">from</span> <span class="hljs-string">"../store"</span>;
<span class="hljs-keyword">import</span> qs <span class="hljs-keyword">from</span> <span class="hljs-string">'qs'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">post</span>(<span class="hljs-params">requestBean: RequestBean,params:Record<<span class="hljs-built_in">string</span>, unknown> = &#123;&#125;</span>): <span class="hljs-title">Promise</span><<span class="hljs-title">ResponseBean</span>></span>&#123;
   <span class="hljs-comment">// 在 store 中取出userid</span>
   <span class="hljs-keyword">if</span>(Store.state.isLogin)&#123;
      params[<span class="hljs-string">'userid'</span>] = Store.getters.getUser.userid;
   &#125;
   <span class="hljs-keyword">return</span> HttpUtil.request(requestBean,qs.stringify(params));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>HttpUtil.request 会接收两个参数</p>
<ol>
<li>requestBean</li>
<li>params 你需要发送的数据(可选)</li>
</ol>
<p>返回值是一个 Promise 对象，带的数据为 ResponseBean 类型的对象</p>
</li>
<li>
<p>正式使用</p>
</li>
</ol>
<p>经过上面的准备工作，现在已经可以开始正式使用了</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 假设你将API类和post方法都在 src/http/index.ts 文件中暴露出来</span>
<span class="hljs-keyword">import</span> &#123;API, post&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/http'</span>
<span class="hljs-keyword">const</span> params = &#123;
   <span class="hljs-string">'userid'</span>: <span class="hljs-string">'123'</span>,
   <span class="hljs-string">'pwd'</span>: <span class="hljs-string">'123'</span>
&#125;
post(API.login(), params)
.then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
   <span class="hljs-keyword">if</span>(res.success)&#123;
      <span class="hljs-built_in">console</span>.log(res);
   &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>结语
别看上面的字多，其实需要自己写的代码是很少的，而且需要配置也很少，单看这个请求工具类的话，其实功能并不多，下一篇博文，我会介绍轻松撘配骨架屏使用，让你几行代码便可以完成一个请求处理，无需烦心再处理loading，error和空数据</li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            