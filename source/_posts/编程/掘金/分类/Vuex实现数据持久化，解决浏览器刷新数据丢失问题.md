
---
title: 'Vuex实现数据持久化，解决浏览器刷新数据丢失问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6417'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 23:18:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=6417'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">vuex的 store 中的数据是保存在运行内存中的，当页面刷新时，页面会重新加载 vue 实例，vuex 里面的数据就会被重新赋值，这样就会出现页面刷新vuex中的数据丢失的问题。 如何解决浏览器刷新数据丢失问题呢？</h4>
<h5 data-id="heading-1">方法一：全局监听，页面刷新的时候将 store 里 state 的值存到 sessionStorage 中，然后从sessionStorage 中获取，再赋值给 store ，并移除 sessionStorage 中的数据。在 app.vue 中添加以下代码：</h5>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'beforeunload'</span>,<span class="hljs-function">()=></span>&#123;
       sessionStorage.setItem(<span class="hljs-string">'list'</span>, <span class="hljs-built_in">JSON</span>.stringify(<span class="hljs-built_in">this</span>.$store.state))
    &#125;)
    
    <span class="hljs-keyword">try</span>&#123;
      sessionStorage.getItem(<span class="hljs-string">'list'</span>) && <span class="hljs-built_in">this</span>.$store.replaceState(<span class="hljs-built_in">Object</span>.assign(&#123;&#125;,<span class="hljs-built_in">this</span>.$store.state,<span class="hljs-built_in">JSON</span>.parse(sessionStorage.getItem(<span class="hljs-string">'list'</span>))))
    &#125;<span class="hljs-keyword">catch</span>(err) &#123;
      <span class="hljs-built_in">console</span>.log(err);
    &#125;
  
    sessionStorage.removeItem(<span class="hljs-string">"list"</span>);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code> 注意!!! storage 只能存储字符串的数据，对于 JS 中常用的数组或对象不能直接存储。但我们可以通过JSON 对象提供的 parse 和 stringify 方法将其他数据类型转化成字符串，再存储到storage中就可以了。</code></p>
<h5 data-id="heading-2">方法二：安装 vuex-persistedstate 插件</h5>
<pre><code class="copyable">1. npm install vuex-persistedstate -S //安装插件
2. 在 store/index.js 文件中添加以下代码：
import persistedState from 'vuex-persistedstate'
const store = new Vuex.Store(&#123;
 state:&#123;&#125;,
 getters:&#123;&#125;,
 ...
 plugins: [persistedState()] //添加插件
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>注意!!! vuex-persistedstate 默认使用 localStorage 来存储数据，若要实现无痕浏览该如何实现呢？</code></p>
<p>这时候就需要使用 sessionStorage 进行存储，修改 plugins 中的代码</p>
<pre><code class="hljs language-js copyable" lang="js">plugins: [
    persistedState(&#123; <span class="hljs-attr">storage</span>: <span class="hljs-built_in">window</span>.sessionStorage &#125;)
]
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            