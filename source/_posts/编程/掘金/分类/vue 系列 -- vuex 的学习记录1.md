
---
title: 'vue 系列 -- vuex 的学习记录1'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abacc6327d8f4513814c806a5e0e7e80~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 24 Jul 2021 01:30:01 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abacc6327d8f4513814c806a5e0e7e80~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">vuex 是什么</h2>
<p>官方文档：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abacc6327d8f4513814c806a5e0e7e80~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>形象比喻：</p>
<p>vuex 就相当于一个放置物品的仓库（对象），所有人（组件）都可以把东西（属性及其值）放到仓库里面（存数据）和拿走仓库里的东西（取数据）</p>
</blockquote>
<h2 data-id="heading-1">vuex 要解决什么问题</h2>
<p>官方文档：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81614c0f83a745b9b9014746fa897a8b~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>通俗理解：</p>
<p>这些物品是大家共用的，如果没有这个仓库，大家拿来拿去很不方便，所以建了个公共的仓库去放这些物品，大家都统一到这里存取</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/705c6a98528845db88eee45f1f2bb676~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>也就是说，开发大型单页应用的时候使用 vuex 能够更好地解决问题</p>
<h2 data-id="heading-2">用 vue 去类比 vuex</h2>
<p>我们用 vue 去类比 vuex 会更加的好理解一点，这里借用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fsinat_23958625%2Farticle%2Fdetails%2F88365986" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/sinat_23958625/article/details/88365986" ref="nofollow noopener noreferrer">通俗理解vuex原理---通过vue例子类比</a> 这篇文章来解读</p>
<p><strong>先来看一个简单的 vue 响应式的例子</strong></p>
<p>vue 中的 data 、methods、computed 三者可以实现响应式</p>
<ol>
<li>视图通过点击事件，触发 methods 中的 increment 方法</li>
<li>该方法更改 data 中 count 的值</li>
<li>一旦 count 值发生变化，computed 中的函数能够把 getCount 更新到视图</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"increment"</span>></span><span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        &#123;&#123;getCount&#125;&#125;
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
        <span class="hljs-comment">// state</span>
        data () &#123;
         <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
         &#125;
        &#125;,
        
        <span class="hljs-comment">// actions</span>
        <span class="hljs-attr">methods</span>: &#123;
         increment () &#123;
            <span class="hljs-built_in">this</span>.count++
         &#125;
        &#125;,
        
         <span class="hljs-comment">// view</span>
        <span class="hljs-attr">computed</span>: &#123;
          <span class="hljs-function"><span class="hljs-title">getCount</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.count
          &#125;
        &#125;,
    &#125;)
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>用 vuex 来实现同样的功能</strong></p>
<p>二者类比如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f7c6841ed31489e8d20e7d08ff4cabb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>假设没有 actions，他们的对应关系是这样的：</p>
<ul>
<li>更改数据 mutations → methods</li>
<li>获取数据 getters → computed</li>
<li>数据  state → data</li>
</ul>
</blockquote>
<p>然后用 vuex 来实现以上的功能：</p>
<ol>
<li>视图通过点击事件，触发 mutations 中的 increment 方法</li>
<li>该方法更改 state 中 count 的值</li>
<li>一旦 count 值发生变化，getters 中的函数能够把 getCount 更新到视图</li>
</ol>
<p>我们看官网的图片：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbe3fab0e1ad404dbe050704cb7ea1cc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>另外的 action、dispatch、commit 是干嘛的？</p>
<ul>
<li>action 可以理解是为了处理异步而多加的一层</li>
<li>组件通过 dispatch 可以触发 actions 中的方法</li>
<li>actions 中的 commit 可以触发 mulations 中的方法</li>
</ul>
<p>用 vuex 实现的代码：</p>
<p>store.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">        <span class="hljs-keyword">const</span> store =  <span class="hljs-keyword">new</span> Vuex.Store(&#123;
        <span class="hljs-attr">state</span>: &#123;
            <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
        &#125;,
        <span class="hljs-attr">mutations</span>: &#123;
            <span class="hljs-function"><span class="hljs-title">incrementMutations</span>(<span class="hljs-params">state</span>)</span> &#123;
            <span class="hljs-keyword">return</span> state.count++
            &#125;
        &#125;,
            
        <span class="hljs-attr">actions</span>: &#123;
            <span class="hljs-function"><span class="hljs-title">incrementActions</span>(<span class="hljs-params">&#123;commit&#125;</span>)</span> &#123;
            commit(<span class="hljs-string">"incrementMutations"</span>); 
            &#125;
         
        &#125;,
        
        <span class="hljs-comment">//通过getter中的方法来获取state值</span>
        <span class="hljs-attr">getters</span>: &#123;
            <span class="hljs-function"><span class="hljs-title">getCount</span>(<span class="hljs-params">state</span>)</span> &#123;
            <span class="hljs-keyword">return</span> state.count
            &#125;
        &#125;
        &#125;)
         
        <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store
<span class="copy-code-btn">复制代码</span></code></pre>
<p>main.js</p>
<pre><code class="hljs language-js copyable" lang="js">        <span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
        <span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
        <span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>
         
        Vue.config.productionTip = <span class="hljs-literal">false</span>
         
        <span class="hljs-keyword">new</span> Vue(&#123;
          store,
          <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
        &#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>APP.store</p>
<pre><code class="hljs language-html copyable" lang="html">       <span class="hljs-tag"><<span class="hljs-name">template</span>></span>
       <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
           <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
               <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"incrementClick"</span>></span>增加<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
               &#123;&#123;this.$store.getters.getCount&#125;&#125;
           <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
       <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
       <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
        
       <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
       <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
           <span class="hljs-attr">methods</span>: &#123;
             <span class="hljs-function"><span class="hljs-title">incrementClick</span>(<span class="hljs-params"></span>)</span>&#123;
               <span class="hljs-built_in">this</span>.$store.dispatch(<span class="hljs-string">"incrementActions"</span>)
             &#125;
           &#125;
       &#125;
       </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">参考文章</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvuex.vuejs.org%2Fzh%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vuex.vuejs.org/zh/" ref="nofollow noopener noreferrer">Vuex 官方文档</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fsinat_23958625%2Farticle%2Fdetails%2F88365986" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/sinat_23958625/article/details/88365986" ref="nofollow noopener noreferrer">通俗理解vuex原理---通过vue例子类比</a></li>
<li><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a></li>
</ul></div>  
</div>
            