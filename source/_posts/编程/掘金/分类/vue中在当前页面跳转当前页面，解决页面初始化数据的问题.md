
---
title: 'vue中在当前页面跳转当前页面，解决页面初始化数据的问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bed93c5c29544c32ac80e7e7827c174f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 27 Apr 2021 01:39:56 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bed93c5c29544c32ac80e7e7827c174f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bed93c5c29544c32ac80e7e7827c174f~tplv-k3u1fbpfcp-watermark.image" alt="1619516224(1).jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">引言</h2>
<p>相信在大多数人的页面开发中，渲染页面所需的数据都是在created中进行接口调用来获取。然后呢，小编在最近的开发中有这样一个需求，在菜单栏中选择进入该页面时，不论处于任何场景下，都要渲染最初的数据展示。用一句话说呢，就是在当前页面再次跳转进入当前页面，要触发我们的渲染数据的流程。</p>
<p>但是呢，vue-router中的特性是：只有在页面进行更新跳转后，才会重新触发我们的created,mounted生命
周期。所以，要实现我们的从/routeA => /routeA，并且触发初始化的接口函数，要怎么做呢？</p>
<h2 data-id="heading-1">1.无痕刷新</h2>
<p>这种场景，常见的是我们可以刷新一下页面就会触发相应流程。但是刷新页面会有白屏，用户体验不好。所以就尝试做尽量无痕的刷新效果。
vue中做无痕刷新，我是通过这篇博客学习的proviede和inject结合的方法。
<a href="https://blog.csdn.net/yangxiaodong88/article/details/81387672?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~aggregatepage~first_rank_v2~rank_aggregation-2-81387672.pc_agg_rank_aggregation&utm_term=vue+%E4%BB%8E%E5%BD%93%E5%89%8D%E9%A1%B5%E9%9D%A2%E8%B7%B3%E8%BD%AC%E5%88%B0%E5%BD%93%E5%89%8D%E9%A1%B5%E9%9D%A2&spm=1000.2123.3001.4430" target="_blank" rel="nofollow noopener noreferrer">=>vue 刷新当前页面或者跳转页面时候刷新</a></p>
<p>在App.vue中</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">router-view</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"isRouterAlive"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"App"</span>,
  <span class="hljs-function"><span class="hljs-title">provide</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">reload</span>: <span class="hljs-built_in">this</span>.reload
    &#125;;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">isRouterAlive</span>: <span class="hljs-literal">true</span>
    &#125;;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">reload</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.isRouterAlive = <span class="hljs-literal">false</span>;
      <span class="hljs-built_in">this</span>.$nextTick(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">this</span>.isRouterAlive = <span class="hljs-literal">true</span>;
      &#125;);
    &#125;
  &#125;
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在要用到刷新的组件中,</p>
<pre><code class="hljs language-js copyable" lang="js"><script>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">inject</span>: [<span class="hljs-string">'reload'</span>],
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;&#125;;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">refresh</span>(<span class="hljs-params"></span>)</span>&#123;
          <span class="hljs-built_in">this</span>.reload();
      &#125;
      &#125;,
  &#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0690d5cb8c74aed879eeeccc2b0c456~tplv-k3u1fbpfcp-watermark.image" alt="refresh_network.gif" loading="lazy" referrerpolicy="no-referrer">
这种无痕刷新的弊端在于，他只是消除了手动刷新时的白屏，但是还是重新加载了图片等文件。时间较长，体验也并不好。</p>
<h2 data-id="heading-2">2.通过router-view和ref，以父子组件通信的方式来调取相关API。</h2>
<pre><code class="hljs language-js copyable" lang="js">DOM：
<router-view ref=<span class="hljs-string">"Router_Son"</span> />
JS：
首页：
<span class="hljs-function"><span class="hljs-title">menu_select</span>(<span class="hljs-params">index, indexPath</span>)</span> &#123;
     <span class="hljs-keyword">var</span> path = <span class="hljs-string">"/portal/"</span> + index;
     <span class="hljs-keyword">if</span> (indexPath && indexPath[<span class="hljs-number">1</span>] == <span class="hljs-string">"hole_query"</span>) &#123;
        <span class="hljs-built_in">this</span>.$router.push(&#123;
          <span class="hljs-attr">path</span>: path
        &#125;);
        <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">"Hole_ListStatus"</span>);
        <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">"Hole_CurrentPage"</span>, <span class="hljs-literal">null</span>);
        <span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">"Hole_Back"</span>, <span class="hljs-literal">false</span>);
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.$refs.Router_Son.holeList_inital) &#123;
          <span class="hljs-built_in">this</span>.$refs.Router_Son.holeList_inital();
        &#125;
      &#125; 
&#125;,
漏洞查询：
<span class="hljs-attr">method</span>:&#123;
    <span class="hljs-function"><span class="hljs-title">holeList_inital</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
&#125;,
<span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.holeList_inital();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当时的思路是：我需要的是在我点击菜单中的漏洞查询时，改变vuex存储的数据，然后在调用漏洞查询页面的初始化函数，即可达到我需要的功能。而vue的实现方式，就是在我的父组件（写有这些公共菜单，页脚等）中，以路由的方式来调用的漏洞查询这一子组件中的页面。这不就是父子组件通信吗~ emm</p>
<p>然后呢，抛去event bus的通信方式，更优雅一点的就是通过ref来实现<code>this.$refs.Router_Son.holeList_inital();</code></p>
<p>这里需要注意的一个小细节是：Router_Son相当于子路由中的子组件（我的表述并不专业），在漏洞查询该页面时中点击菜单栏中的漏洞查询进行跳转，此时我们的子组件中包含<strong>holeList_inital</strong>这个函数。如果在其他页面时点击菜单栏中的漏洞查询进行跳转，此时并不包含该函数。为了减少一些报错，所以需要一个if判断。
效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49a116e29e574744b289bbed8e026c5b~tplv-k3u1fbpfcp-watermark.image" alt="son.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">3.路由守卫的方式来进行判断</h2>
<p>因为小编也是刚毕业，主要是面向百度开发，哈哈。然后当时了解到的是，还有一种思路是通过路由守卫来进行判断。<code>组件内的守卫有：beforeRouteEnter，beforeRouteUpdate，beforeRouteLeave</code>，但是对于我的这种场景并不适用。<a href="https://router.vuejs.org/zh/guide/advanced/navigation-guards.html#%E7%BB%84%E4%BB%B6%E5%86%85%E7%9A%84%E5%AE%88%E5%8D%AB" target="_blank" rel="nofollow noopener noreferrer">=>路由守卫的官方文档</a></p>
<pre><code class="hljs language-js copyable" lang="js">beforeRouteUpdate:官方的描述是这样：
<span class="hljs-function"><span class="hljs-title">beforeRouteUpdate</span>(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>)</span> &#123;
    <span class="hljs-comment">// 在当前路由改变，但是该组件被复用时调用</span>
    <span class="hljs-comment">// 举例来说，对于一个带有动态参数的路径 /foo/:id，在 /foo/1 和 /foo/2 之间跳转的时候，</span>
    <span class="hljs-comment">// 由于会渲染同样的 Foo 组件，因此组件实例会被复用。而这个钩子就会在这个情况下被调用。</span>
    <span class="hljs-comment">// 可以访问组件实例 `this`</span>
  &#125;,

针对的是这种场景:  <span class="hljs-regexp">/portal/</span>hole_query?id=<span class="hljs-number">1</span>   =>  <span class="hljs-regexp">/portal/</span>hole_query?id=<span class="hljs-number">666</span>

但是由于我们是安全行业，以前做的项目中，测试报告比较严格。然后我为了不明显暴露参数，就在项目中统一采用了vuex，
不使用query传参等。所以这种方式我不适用，大家如果有这种情景的话，可以试试路由守卫的方式。
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">4.尾言</h2>
<p>感谢您能看到这里，哈哈。第一次写，不足之处希望大家不吝赐教。 =</p></div>  
</div>
            