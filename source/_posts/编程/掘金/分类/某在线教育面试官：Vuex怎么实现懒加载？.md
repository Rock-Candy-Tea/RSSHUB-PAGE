
---
title: '某在线教育面试官：Vuex怎么实现懒加载？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1902387e4b274ff6a28d24343c704c92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 18:03:34 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1902387e4b274ff6a28d24343c704c92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>因为最近在面一家某在线教育公司的时候，被问到了一道印象比较深刻的题，就是如题目所示：“Vuex怎么实现懒加载”，因为之前的确没有考虑到vuex的懒加载问题，所以就没怎么去思考过这个问题，因此也就被问得一头雾水。现在不懂无所谓，以后再不会就感觉丢大人了。所以，回来之后就研究了一下这个问题和vuex的文档，也得到了自己想要的答案。</p>
</blockquote>
<h1 data-id="heading-0">需要知道的知识点</h1>
<ul>
<li>
<p>import方法</p>
</li>
<li>
<p>$store.registerModule方法</p>
</li>
</ul>
<p>这里简单的介绍一下这两个方法👇</p>
<p><strong>import方法</strong>，不是我们经常写的<strong>es6import</strong>,而是<strong>webpack为我们提供的import方法</strong>，它可以让我们按需的加载一个<strong>js模块</strong>;</p>
<p><strong>$store.registerModule方法</strong>是<strong>Vuex</strong>为我们提供的一个可以动态注册一个<strong>vuex modules</strong>。</p>
<h1 data-id="heading-1">未使用懒加载的Vuex</h1>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1902387e4b274ff6a28d24343c704c92~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>未使用懒加载的vuex如上图所以，一初始化就全部模块的数据都加载进来，如果数据少的话还好，如果你的vuex数据超级膨大的呢？那就要炸了。</p>
<h1 data-id="heading-2">Vuex实现懒加载出版</h1>
<p>首先先将之前引进了来vue modules 注释或者移除。</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
<span class="hljs-comment">// import home from './modules/home'</span>
<span class="hljs-comment">// import detail from './modules/detail'</span>

Vue.use(Vuex)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
  &#125;,
  <span class="hljs-attr">actions</span>: &#123;
  &#125;,
  <span class="hljs-attr">modules</span>: &#123;
    <span class="hljs-comment">// home,</span>
    <span class="hljs-comment">// detail</span>
  &#125;
&#125;)


<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d25ee49cd144b078cbffb1b415bd976~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>未注册vuex任何module的state是空的👆</p>
<p>紧接着在你需要用到Vuex的页面进行手动注册。</p>
<p>🌰</p>
<pre><code class="hljs language-js copyable" lang="js"><template></template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">beforeCreate</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">import</span>(<span class="hljs-string">'../store/modules/home'</span>).then(<span class="hljs-function"><span class="hljs-params">res</span>=></span>&#123;
        <span class="hljs-built_in">this</span>.$store.registerModule(<span class="hljs-string">'home'</span>,res.default)
    &#125;)
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">scoped</span>></span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>就是通过<strong>beforeCreate</strong>里面的一句代码就能使用懒加载，是不是超级容易。</p>
<p>效果👇</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88bcf3b2db254655bf3bb54b6873a3ab~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这种方式虽然是可以实现vuex的懒加载，但是要我们在用到vuex的页面一个一个的去手动实现注册，这样挺烦躁，挺笨的，让我们来对它进行一个封装。</p>
<h1 data-id="heading-3">封装后的Vuex懒加载</h1>
<p>这里封装主要是用Vue提供的插件机制的方式实现对<code>Vuex懒加载实现</code>。</p>
<p>🌰</p>
<p><strong>随便定义一个xxx.js文件，写下如下代码</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">install</span>(<span class="hljs-params">Vue</span>)</span>&#123;
  Vue.mixin(&#123;
    <span class="hljs-function"><span class="hljs-title">beforeCreate</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">let</span> vuexModuleName = <span class="hljs-built_in">this</span>.$options.vuexModuleName
      <span class="hljs-keyword">if</span>(vuexModuleName && !<span class="hljs-built_in">this</span>.$store.state[vuexModuleName])&#123;
        <span class="hljs-keyword">import</span>(<span class="hljs-string">`../store/modules/<span class="hljs-subst">$&#123;vuexModuleName&#125;</span>`</span>).then(<span class="hljs-function">(<span class="hljs-params">res</span>)=></span>&#123;
          <span class="hljs-built_in">this</span>.$store.registerModule(<span class="hljs-string">`<span class="hljs-subst">$&#123;vuexModuleName&#125;</span>`</span>,res.default)
        &#125;)
      &#125;
    &#125;
  &#125;)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;install&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>然后在main.js引入</strong></p>
<pre><code class="hljs language-js copyable" lang="js">...
<span class="hljs-keyword">import</span> vuexLazy <span class="hljs-keyword">from</span> <span class="hljs-string">'./plugins/vuexLazy'</span>
Vue.use(vuexLazy)
...

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使用</strong></p>
<p>只需要在某个模块提供一个<code>vuexModuleName</code>的key就可以，比如如下，我们提供一个<strong>vuexModuleName为home</strong>，它就会将<strong>home</strong>模块动态注册。</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;&#123; $store.state &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">vuexModuleName</span>:<span class="hljs-string">'home'</span>
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：提供的<code>vuexModuleName的val值一定要有对应的模块存在</code></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/120bb7b7025c4dc08de32b4792f7177f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">结尾</h1>
<p>以上是对Vuex的懒加载的一个简单实现和封装，也只是为了提供一种思路，如有需要的同学可以自行完善。</p>
<p><strong>遗留问题</strong></p>
<p>通过动态注册的Vuex的module，没有同步到<code>vuedevtools</code>,暂时还没想到解决方案，之后会去研究研究；有方案的同学，欢迎交流交流。</p></div>  
</div>
            