
---
title: '十分钟 带你强势入门 vue3'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb17914f2606439b930d2c8b05c4389b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 17:50:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb17914f2606439b930d2c8b05c4389b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">十分钟 带你强势入门 vue3</h1>
<h2 data-id="heading-1">案例效果图</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb17914f2606439b930d2c8b05c4389b~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210701232414581" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">vue3 介绍</h2>
<p>自从去年v3推出以来，发现我不会 <code>vue3</code> 都没有办法和周边朋友愉快聊天了，不会 <code>vue3</code> 就相等于没有朋友！</p>
<h2 data-id="heading-3">安装启动</h2>
<ol>
<li>
<p>安装</p>
<pre><code class="copyable">npm init @vitejs/app
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>运行</p>
<pre><code class="copyable">npm run dev 
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h2 data-id="heading-4">和 vue2  有什么区别</h2>
<p>开发者最直观的感受应该就是</p>
<p>以前 <code>vue2</code> 是 <code>东市买骏马西市买鞍鞯</code>，分门，虽然要跑一段路，但是起码目标路径清晰。</p>
<p>现在 <code>vue3</code> 是 不管什么分门别类了，专门给你开个 鸡店马店，一个店把配置所有都搞定。 专业术语叫 <strong>组合式API</strong>，放羊屁就是 <strong>Composition API</strong></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue3js.cn%2Fdocs%2Fzh%2Fguide%2Fcomposition-api-introduction.html%23%25E4%25BB%2580%25E4%25B9%2588%25E6%2598%25AF%25E7%25BB%2584%25E5%2590%2588%25E5%25BC%258F-api" target="_blank" rel="nofollow noopener noreferrer" title="https://vue3js.cn/docs/zh/guide/composition-api-introduction.html#%E4%BB%80%E4%B9%88%E6%98%AF%E7%BB%84%E5%90%88%E5%BC%8F-api" ref="nofollow noopener noreferrer">以上见解参考官网</a></p>
<p>一图胜前言</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67509bd71895464291daba8132900042~tplv-k3u1fbpfcp-zoom-1.image" alt="未命名绘图" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>可能小伙伴会有疑问，一个页面 里面很多不同的 <code>data</code>  methods 都放一起不是开玩笑吗，下面会讲到，用封装就可以解决。</p>
</blockquote>
<h2 data-id="heading-5">关键技术</h2>
<h3 data-id="heading-6">setup</h3>
<p>vue3的入口函数，就是在这里负责把当前组件用到的 <code>data</code> <code>methods</code> <code>computed</code> 等  功能进行打包，可以提高给视图使用。setup触发时，组件还没有实例化，因此<strong>不要使用 this</strong></p>
<h3 data-id="heading-7">ref</h3>
<p>用来创建响应式数据， 类似之前 <code>vue2</code> 中的 <code>data</code></p>
<h3 data-id="heading-8">computed</h3>
<p>这货就是以前 vue2 中的计算属性 <code>computed</code>  类似用法还有 <code>watch</code></p>
<h3 data-id="heading-9">onMounted</h3>
<p>这个看单词就秒懂啦。</p>
<h2 data-id="heading-10">封装</h2>
<p>看到 <code>v2</code> 对比 <code>v3</code> 的图，小伙伴很难想象到 一个大页面把 所有的 <code>data</code> method 都移到一个 <code>setup</code>内，岂不是玩死人。</p>
<p>不着急，使用拆分和封装就可以了。</p>
<p>我们可以把同一个功能的代码 都封装到一个 函数内。</p>
<p><code>useInput</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useInput</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> inpValue = ref(<span class="hljs-string">""</span>);
  <span class="hljs-keyword">const</span> setInput = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
    inpValue.value = value;
  &#125;
  <span class="hljs-keyword">return</span> &#123;
    inpValue,
    setInput
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后vue组件做引入即可</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> useInput <span class="hljs-keyword">from</span> <span class="hljs-string">"./composables/useInput"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"App"</span>,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> &#123; inpValue, setInput &#125; = useInput();
    <span class="hljs-keyword">return</span> &#123;
      inpValue, <span class="hljs-comment">// 输入框的值</span>
      setInput, <span class="hljs-comment">// 存储输入框的值</span>
    &#125;;
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">写一个这样的 tudo 来 证明下自己吧</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c2d34f45b3e4998b98a421079da48b1~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210701232414581" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">github代码参考</h2>
<pre><code class="copyable">https://hub.fastgit.org/itcastWsy/v3-tudo
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            