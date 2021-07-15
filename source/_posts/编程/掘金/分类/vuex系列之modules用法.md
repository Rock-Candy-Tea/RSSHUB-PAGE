
---
title: 'vuex系列之modules用法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1192'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 07:45:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=1192'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>一、在实际开发中，我们如果全部的状态管理都写在一个文件里，那么当项目越来越大时就会很难维护了，所以我们就要用到vuex的modules了。看代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//user.js</span>
<span class="hljs-keyword">const</span> state = &#123;
 <span class="hljs-attr">name</span>:<span class="hljs-string">''</span>
&#125;
<span class="hljs-keyword">const</span> mutations = &#123;
  <span class="hljs-function"><span class="hljs-title">updateUserName</span>(<span class="hljs-params">state,provide</span>)</span>&#123;
  state.name = provide
  &#125;
 
&#125;
<span class="hljs-keyword">const</span> actions = &#123;
  
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">namespaced</span>: <span class="hljs-literal">true</span>,
  state,
  mutations,
  actions
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">date.js
<span class="hljs-keyword">const</span> state = &#123;
 <span class="hljs-attr">date</span>:<span class="hljs-string">''</span>
&#125;
<span class="hljs-keyword">const</span> mutations = &#123;
  <span class="hljs-function"><span class="hljs-title">updateDate</span>(<span class="hljs-params">state,provide</span>)</span>&#123;
  state.date = provide
  &#125;
 
&#125;
<span class="hljs-keyword">const</span> actions = &#123;
  
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">namespaced</span>: <span class="hljs-literal">true</span>,
  state,
  mutations,
  actions
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//index.js</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
<span class="hljs-keyword">import</span> user <span class="hljs-keyword">from</span> <span class="hljs-string">'./modules/user'</span>
<span class="hljs-keyword">import</span> date <span class="hljs-keyword">from</span> <span class="hljs-string">'./modules/date'</span>

Vue.use(Vuex)

<span class="hljs-keyword">const</span> store = <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">modules</span>: &#123;
    user,
    date,
  &#125;,
  
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//index.vue</span>
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">userName</span>(<span class="hljs-params"></span>)</span> &#123;
     <span class="hljs-comment">// 指明是调user模块的属性</span>
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$store.state.user.name
    &#125;,
    <span class="hljs-function"><span class="hljs-title">date</span>(<span class="hljs-params"></span>)</span> &#123;
     <span class="hljs-comment">// 指明是调date模块的属性</span>
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$store.state.date.date
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>:&#123;
  <span class="hljs-function"><span class="hljs-title">updateUserName</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-comment">// 指明是调user模块的方法</span>
  <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">'user/updateUserName'</span>,<span class="hljs-string">'张三'</span>)
  &#125;,
   <span class="hljs-comment">// 指明是调date模块的方法</span>
  <span class="hljs-function"><span class="hljs-title">updateDate</span>(<span class="hljs-params"></span>)</span>&#123;
   <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">'date/updateDate'</span>,<span class="hljs-string">'2021.07.14'</span>)
  &#125;
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面建了两个js文件，然后分别引入到index.j文件中，记得要用namespaced来避免重名属性带来的影响，然后我们在页面调用时要指明是哪个模块的，不然程序不知道你调用的是哪个模块的哦。</p></div>  
</div>
            