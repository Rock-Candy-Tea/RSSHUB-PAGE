
---
title: 'Vue _ 路由守卫面试常考'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d173fa64f014b00b8664c304520fc16~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 27 Mar 2021 00:20:56 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d173fa64f014b00b8664c304520fc16~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<blockquote>
<p>最近在整理基础，欢迎掘友们一起交流学习,关注公众号<a href="https://z3.ax1x.com/2021/03/27/6zmqSI.jpg" target="_blank" rel="nofollow noopener noreferrer">前端自学社区</a> <br> 结尾有彩蛋哦！ 🎉🎉🎉</p>
</blockquote>
<h2 data-id="heading-1">Vue Router 路由守卫</h2>
<h3 data-id="heading-2">导图目录</h3>
<blockquote>
<ul>
<li>
<ol>
<li>路由守卫分类</li>
</ol>
</li>
<li>
<ol start="2">
<li>全局路由守卫</li>
</ol>
</li>
<li>
<ol start="3">
<li>单个路由守卫</li>
</ol>
</li>
<li>
<ol start="4">
<li>组件路由守卫</li>
</ol>
</li>
<li>
<ol start="5">
<li>路由守卫执行的完整过程</li>
</ol>
</li>
</ul>
</blockquote>
<hr>
<h3 data-id="heading-3">路由守卫分类</h3>
<blockquote>
<ul>
<li>全局路由</li>
<li>单个路由独享</li>
<li>组件内部路由</li>
</ul>
<p>每个路由守卫的钩子函数都有 3 个参数：</p>
<blockquote>
<p><code> to</code> :  进入的目标路由</p>
<p><code> from</code> : 离开的路由</p>
<p><code>next</code>   :  控制路由 在跳转时进行的操作，一定要执行。</p>
<blockquote>
<p>它有 4 个行为：</p>
<p><code> next()</code> :  钩子都执行完了，进入到下一个路由当中。</p>
<p><code> next(false)</code>: 中断路由进入下一个路由。</p>
<p><code> next('/')</code> : 根据你路由跳转判断条件来进入对应的路由， <code>/</code> 为路由的 <code> path</code> 。</p>
<p><code>next(new Error)</code> :  中断路由跳转，错误会被传递给 <a href="https://router.vuejs.org/zh/api/#router-onerror" target="_blank" rel="nofollow noopener noreferrer"><code>router.onError()</code></a> 注册过的回调。</p>
</blockquote>
</blockquote>
</blockquote>
<h3 data-id="heading-4">全局路由守卫</h3>
<blockquote>
<ul>
<li><code> beforeEach（to，from， next）</code></li>
<li><code> beforeResolve（to，from， next）</code></li>
<li><code> afterEach（to，from）</code></li>
</ul>
<p>全局路由直接挂载到 <code> router</code> 实例上。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//全局验证路由</span>
<span class="hljs-keyword">const</span> router = createRouter(&#123;
  <span class="hljs-attr">history</span>: createWebHashHistory(),
  routes
&#125;);

<span class="hljs-comment">// 白名单， 不需要验证的路由</span>
<span class="hljs-keyword">const</span> whiteList = [<span class="hljs-string">'/'</span>,<span class="hljs-string">'/register'</span>]

router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to,<span class="hljs-keyword">from</span>,next</span>)=></span>&#123;
  <span class="hljs-keyword">if</span>(whiteList.indexOf(to.path) === <span class="hljs-number">0</span>) &#123;
    <span class="hljs-comment">// 放行，进入下一个路由</span>
    next()
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(!(sessionStorage.getItem(<span class="hljs-string">'token'</span>)))&#123;
    next(<span class="hljs-string">'/'</span>);     
  &#125; <span class="hljs-keyword">else</span> &#123;
    next()
  &#125;  
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5"><code>beforeEach</code></h4>
<blockquote>
<h5 data-id="heading-6">使用场景</h5>
<p><strong>路由跳转前触发</strong></p>
<h5 data-id="heading-7">作用</h5>
<p><strong>常用于登录验证</strong></p>
</blockquote>
<h4 data-id="heading-8"><code> beforeResolve</code></h4>
<blockquote>
<h5 data-id="heading-9">使用场景</h5>
<p><strong>在 beforeEach 和 组件内beforeRouteEnter 之后，afterEach之前调用。</strong></p>
</blockquote>
<h4 data-id="heading-10"><code> afterEach</code></h4>
<blockquote>
<h5 data-id="heading-11">使用场景</h5>
<ol>
<li><strong>发生在beforeEach和beforeResolve之后，beforeRouteEnter之前。</strong></li>
<li><strong>路由在触发后执行</strong></li>
</ol>
</blockquote>
<h3 data-id="heading-12">单个路由独享</h3>
<blockquote>
<p>它只有一个 钩子函数， <code>beforeEnter（to,from,next）</code></p>
</blockquote>
<h4 data-id="heading-13"><code> beforeEnter</code></h4>
<blockquote>
<h5 data-id="heading-14">使用场景</h5>
<p><strong>在beforeEach之后执行，和它功能一样</strong> ，不怎么常用</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">      &#123;
        <span class="hljs-attr">path</span>:<span class="hljs-string">'/superior'</span>,
        <span class="hljs-attr">component</span>: Superior,
        <span class="hljs-attr">meta</span>:&#123;
          <span class="hljs-attr">icon</span>:<span class="hljs-string">'el-icon-s-check'</span>,
          <span class="hljs-attr">title</span>:<span class="hljs-string">'上级文件'</span>
        &#125;,
        <span class="hljs-attr">beforeEnter</span>:<span class="hljs-function">(<span class="hljs-params">to,form,next</span>) =></span>&#123;
          
        &#125;
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">组件路由守卫</h3>
<blockquote>
<h5 data-id="heading-16">特点：</h5>
<p>组件内执行的钩子函数</p>
<h5 data-id="heading-17">钩子函数：</h5>
<ul>
<li><code> beforeRouteEnter(to,from,next)</code></li>
<li><code> beforeRouteUpdate(to,from,next)</code></li>
<li><code> beforeRouteLeave(to,from,next)</code></li>
</ul>
</blockquote>
<h4 data-id="heading-18"><code> beforeRouteEnter</code></h4>
<blockquote>
<h5 data-id="heading-19">使用场景：</h5>
<ol>
<li>路由进入之前调用。</li>
<li>不能获取组件 <code> this</code> 实例 ，因为路由在进入组件之前，组件实例还没有被创建。</li>
</ol>
<h5 data-id="heading-20">执行顺序</h5>
<p><code> beforeEach</code> 和独享守卫<code> beforeEnter</code>之后，全局<code> beforeResolve</code>和全局<code>afterEach</code>之前调用.</p>
</blockquote>
<h4 data-id="heading-21"><code> beforeRouteUpdate</code></h4>
<blockquote>
<h5 data-id="heading-22">使用场景：</h5>
<ol>
<li>在当前路由改变时，并且该组件被复用时调用，可以通过this访问实例。</li>
<li>当前路由query变更时，该守卫会被调用。</li>
</ol>
</blockquote>
<h4 data-id="heading-23"><code> beforeRouteLeave</code></h4>
<blockquote>
<h5 data-id="heading-24">使用场景：</h5>
<p>导航离开该组件的对应路由时调用，可以访问组件实例this</p>
</blockquote>
<h3 data-id="heading-25">路由守卫执行的完整过程</h3>
<blockquote>
<ol>
<li>导航被触发</li>
<li>执行  组件内部路由守卫： <code>beforeRouteLeave</code></li>
<li>执行 全局路由守卫  <code>beforeEach</code></li>
<li>在重用组件内部路由守卫钩子 <code> beforeRouteUpdate</code></li>
<li>执行 路由中的钩子 <code> beforeEnter</code></li>
<li>在被激活的组件里调用 beforeRouteEnter</li>
<li>执行 全局的 beforeResolve 守卫 。</li>
<li>执行  全局的 afterEach 钩子</li>
<li>beforeCreate</li>
<li>created</li>
<li>beforeMount</li>
<li>mounted</li>
<li>执行 beforeRouteEnter的next的回调 ，创建好的组件实例会作为回调函数的参数传入。</li>
</ol>
</blockquote>
<p><img alt="Vue  路 由 守  卫    前端自学社区.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d173fa64f014b00b8664c304520fc16~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-26">结语</h3>
<blockquote>
<p>❤️关注+点赞+收藏+评论+转发❤️，原创不易，鼓励笔者创作更好的文章<br><br>关注公众号 <a href="https://z3.ax1x.com/2021/03/27/6zmqSI.jpg" target="_blank" rel="nofollow noopener noreferrer">前端自学社区</a>，即可获取更多前端高质量文章！<br><br>关注后回复关键词“加群”， 即可加入 “前端自学交流群”，共同学习进步。<br><br>关注后添加我微信拉你进技术交流群<br><br>欢迎关注公众号，更多精彩文章只在公众号推送</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            