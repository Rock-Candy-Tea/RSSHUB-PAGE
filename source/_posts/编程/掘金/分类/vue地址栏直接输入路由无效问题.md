
---
title: 'vue地址栏直接输入路由无效问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9669'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 00:29:28 GMT
thumbnail: 'https://picsum.photos/400/300?random=9669'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>vue 项目只要不是静态页面，一般都会和官方的路由管理器 vue-router 一起使用。</p>
<p>最近项目有一个需求，是在地址栏输入路由，跳转到对应路由组件，在开发环境中这样做是可以跳转的，但是项目打包后，通过地址栏跳转会报错。</p>
<p>因为 vue 在页面上显示哪个组件是根据 vue-router 进行控制的，在地址栏上直接输入路由名称，并不能触发 vue-router 的规则，所以只能通过监听地址的改变，利用回调函数在组件内部进行动态修改路由。</p>
<h4 data-id="heading-0">方式一：history 模式</h4>
<p>vue-router 默认是 hash 模式，通过更改模式为 history 模式可以解决这个问题，但是这需要后端配合，更改服务端配置，虽然过程稍麻烦但也是一个办法，有兴趣的朋友可以查看往期文章 。</p>
<h4 data-id="heading-1">方式二：hashchange 事件</h4>
<p>什么是 hash？</p>
<p>hash 就是 URL 地址中 # 字符后面的字符串。</p>
<p>更改它不会导致整个页面重新加载，而且可以定位到元素 id 或 name 与之相同的位置（锚点）。</p>
<p><code>window.location.hash</code> 可以获取到 hash。比如 localhost:8080/#/abcde 的 location.hash="#/abcde"。</p>
<p>通过监听 hash 的状态，来动态修改 vue-router 的路由，是页面进行组件切换，这样就不会导致页面报错或 404 了。</p>
<p>当 hash 被修改时，将触发 hashchange 事件（<strong>IE8 +支持</strong>）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'hashchange'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(e.oldURL); 
<span class="hljs-built_in">console</span>.log(e.newURL)
&#125;,<span class="hljs-literal">false</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以在 App.vue 中添加此事件：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'hashchange'</span>,<span class="hljs-function">()=></span>&#123;
<span class="hljs-keyword">var</span> currentPath = <span class="hljs-built_in">window</span>.location.hash.slice(<span class="hljs-number">1</span>); <span class="hljs-comment">// 获取输入的路由</span>
<span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.$router.path !== currentPath)&#123;
<span class="hljs-built_in">this</span>.$router.push(currentPath); <span class="hljs-comment">// 动态跳转</span>
&#125;
&#125;,<span class="hljs-literal">false</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样即可解决，在地址栏输入路由跳转无效问题。</p></div>  
</div>
            