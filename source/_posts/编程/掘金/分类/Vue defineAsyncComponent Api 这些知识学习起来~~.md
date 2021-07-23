
---
title: 'Vue defineAsyncComponent Api 这些知识学习起来~~'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e76001b7c2b49359bcda0f10cfa09d0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 16:23:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e76001b7c2b49359bcda0f10cfa09d0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>作者：Apoorv Tyagi
译者：前端小智
来源：dev</p>
</blockquote>
<blockquote>
<p>有梦想，有干货，微信搜索 <strong>【大迁世界】</strong> 关注这个在凌晨还在刷碗的刷碗智。</p>
<p>本文 GitHub  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fqq449245884%2Fxiaozhi" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/qq449245884/xiaozhi" ref="nofollow noopener noreferrer">github.com/qq449245884…</a> 已收录，有一线大厂面试完整考点、资料以及我的系列文章。</p>
</blockquote>
<p>使用 Vue3 的 <code>DefileAsyncComponent</code>功能可让我们懒加载组件，说白了就是创建一个只有在需要时才会加载的异步组件。</p>
<p>这是改进初始页面加载的好方法，因为我们的应用程序将加载到较小的块中而不是必须在页面加载时加载每个组件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e76001b7c2b49359bcda0f10cfa09d0~tplv-k3u1fbpfcp-watermark.image" alt="01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在本文中，我们将学习有关<code>defineAsyncComponent</code>的所有知识，并学习一个懒加载弹出窗口的例子。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/806c5adba32d49159363b7df99feeb28~tplv-k3u1fbpfcp-watermark.image" alt="02.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">defineAsyncComponent 是啥？</h3>
<pre><code class="copyable">const AsyncComp = defineAsyncComponent(
  () =>
    new Promise((resolve, reject) => &#123;
      resolve(&#123;
        template: '<div>I am async!</div>'
      &#125;)
    &#125;)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>defineAsyncComponent</code> 可以接受一个返回 <code>Promise</code> 的工厂函数。Promise 的 <code>resolve</code> 回调应该在服务端返回组件定义后被调用。你也可以调用 <code>reject(reason)</code> 来表示加载失败。</p>
<p><code>defineAsyncComponent</code> 可以从 vue 中导入，并使用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; defineAsyncComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span> 

<span class="hljs-comment">// simple usage </span>
<span class="hljs-keyword">const</span> LoginPopup = defineAsyncComponent(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">"./components/LoginPopup.vue"</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是<code>defineAsyncComponent</code>的最简单方法，对于高阶用法，<code>defineAsyncComponent</code> 可以接受一个对象：</p>
<pre><code class="copyable">const AsyncPopup = defineAsyncComponent(&#123; 
  loader: () => import("./LoginPopup.vue"),
   // 加载异步组件时要使用的组件
  loadingComponent: LoadingComponent,
   // 加载失败时要使用的组件
  errorComponent: ErrorComponent, 
  // 在显示 loadingComponent 之前的延迟 | 默认值：200（单位 ms）
  delay: 1000, 
  // 如果提供了 timeout ，并且加载组件的时间超过了设定值，将显示错误组件
  // 默认值：Infinity（即永不超时，单位 ms）
  timeout: 3000 
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基础已经介绍完了，接着，我们来做个例子。</p>
<h3 data-id="heading-1">使用 defineAsyncComponent 异步加载 Popup 组件</h3>
<p>在这个例子中，我们将使用一个由点击按钮触发的登录弹框。</p>
<p>我们不需要我们的应用程序在每次加载时都加载这个组件，因为只有在用户执行特定的动作时才需要它。</p>
<p>下面是 login 组件的实现：</p>
<pre><code class="copyable">// LoginPopup.vue
<template>
   <div class="popup">
       <div class="content">
           <h4> Login to your account </h4>
           <input type="text" placeholder="Email" />
           <input type="password" placeholder="Password" />
           <button> Log in </button>
       </div>
   </div>
</template>

<script>
</script>

<style scoped>
.popup &#123;
    position: fixed;
    width: 100%;
    top: ; 
    left: ;
    height: 100%;
    background-color: rgba(, , , 0.2);
    display: flex;
    justify-content: center;
    align-items: center;
&#125;
.content &#123;
   min-width: 200px;
   width: 30%;
   background: #fff;
   height: 200px;
   padding: 10px;
   border-radius: 5px;
&#125;
input[type="text"], input[type="password"] &#123;
    border: ;
    outline: ;
    border-bottom: 1px solid #eee;
    width: 80%;
    margin:  auto;
    font-size: 0.5em;
&#125;
button &#123;
   border: ;
   margin-top: 50px;
   background-color:#8e44ad;
   color: #fff;
   padding: 5px 10px;
   font-size: 0.5em;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9859443ceb514b16ae6247c181583540~tplv-k3u1fbpfcp-watermark.image" alt="03.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在其它组件中导入它：</p>
<pre><code class="copyable"><template>
  <button @click="show = true"> Login </button>
  <login-popup v-if="show" />
</template>

<script>
import LoginPopup from './components/LoginPopup.vue'
export default &#123;
  components: &#123; LoginPopup &#125;,
  data() &#123;
    return &#123;
      show: false
    &#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以使用 <code>defineAsyncComponent</code>，只在需要的时候加载它（按钮被点击时使用<code>v-if</code>来切换）。</p>
<pre><code class="copyable"><!-- Use defineAsyncComponent  -->
<template>
  <button @click="show = true"> Login </button>
  <login-popup v-if="show" />
</template>

<script>
import &#123; defineAsyncComponent &#125; from 'vue'
export default &#123;
  components: &#123; 
    "LoginPopup" : defineAsyncComponent(() => import('./components/LoginPopup.vue'))
  &#125;,
  data() &#123;
    return &#123;
      show: false
    &#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个用法看起来和上面的差不多，不急，我们 <code>F12</code> 打开控制台。</p>
<p>如果我们不使用<code>defineAsyncComponent</code>，一旦我们的页面加载，我们就会看到我们的应用程序从服务器上获得<code>LoginPopup.vue</code>。虽然在这个例子中，性能问题不那么严重，但如果我们有几十个组件这样做，性能上多多少少还是有影响的。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d536f9932b04faeb0d031141b0d204a~tplv-k3u1fbpfcp-watermark.image" alt="04.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然而，如果我们使用<code>defineAsyncComponent</code>查看同一个标签，会注意到，当我们的页面加载时，<code>LoginPopup.vue</code>是没有的，这是因为它还没有被加载。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52f93830b1d24b6ba170dcf1efe68ad7~tplv-k3u1fbpfcp-watermark.image" alt="05.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但，如果切换按钮，我们就可以看到它了：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd334338a81542b0a2b538c4831f09f6~tplv-k3u1fbpfcp-watermark.image" alt="06.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这有助于我们实现最佳性能。我们只想在我们的页面初始加载时加载需要的组件。有条件渲染的组件在我们的页面加载时往往是不需要的，所以为什么要让我们的应用程序加载它们呢？</p>
<h3 data-id="heading-2">如何与异步的 setup  方法一起使用？</h3>
<p>不管我们是否用<code>defineAsyncComponent</code>来异步加载，任何具有异步 <code>setup</code> 方法的组件都必须用<code><Suspense></code>来包装。</p>
<p>简而言之，创建一个异步 <code>setup</code> 函数是我们的一种选择，可以让我们的组件在渲染前等待一些API 调用或其他异步操作。</p>
<p>下面是带有异步<code>setup</code>的组件，使用<code>setTimeout()</code>模拟API调用</p>
<pre><code class="copyable"><template>
   <div class="popup">
       <div class="content">
            <p> Loaded API: &#123;&#123; article &#125;&#125; </p>
           <h4> Login to your account </h4>
           <input type="text" placeholder="Email" />
           <input type="password" placeholder="Password" />
           <button> Log in </button>
       </div>
   </div>
</template>

<script>
const getArticleInfo = async () => &#123;
     // wait 3 seconds to mimic API call
    await new Promise(resolve => setTimeout(resolve, 1000));
    const article = &#123;
        title: 'My Vue 3 Article',
        author: 'Matt Maribojoc'
    &#125;
    return article
&#125;
export default &#123;
    async setup() &#123;
        const article = await getArticleInfo()
        console.log(article)
        return &#123;
            article
        &#125;
    &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以使用或不使用<code>defineAsyncComponent</code>将它导入到组件中:</p>
<pre><code class="copyable">import LoginPopup from './components/LoginPopup.vue'

// OR 

const LoginPopup = defineAsyncComponent(() => import("./components/LoginPopup.vue"))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但如果我们想让它在我们的模板中渲染，我们需要把它包在一个<code>Suspense</code>元素中。这将等待我们的<code>setup</code> 解析后，然后再尝试渲染我们的组件。</p>
<p><code>Suspense</code>的一个很好的特点是，我们可以使用槽和模板显示回退内容。回退内容将显示，直到<code>setup</code>函数解析，我们的组件准备好渲染。 请注意，<code>v-if</code>已经从组件本身移到了我们的Suspense 组件上，所以所有回退内容都会显示。</p>
<pre><code class="copyable"><template>
  <button @click="show = true"> Login </button>
  <Suspense v-if="show">
    <template #default>
      <login-popup  />
    </template>
    <template #fallback>
      <p> Loading... </p>
    </template>
  </Suspense>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是运行结果，会看到 <code>"Loading…"</code>，然后在<code>3</code>秒后(<code>setTimeout</code>的硬编码值）组件渲染。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5b72ac7de804ae2b83af1dc82a83c1b~tplv-k3u1fbpfcp-watermark.image" alt="08.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>默认情况下，我们使用<code>defineAsyncComponent</code>定义的所有组件都是可<code>Suspense</code>的。</p>
<p>这意味着如果一个组件的父链中有Suspense，它将被视为该Suspense的一个异步依赖。我们的组件的加载、错误、延迟和超时选项将被忽略，而是由Suspense来处理。</p>
<h3 data-id="heading-3">总结</h3>
<p>当构建包许多组件的大型项目时，<code>defineAsyncComponent</code>是非常有用的。当我们使用懒加载组件时，可以更快地加载页面，改善用户体验，最终提高应用的留存率和转换率。</p>
<p>我很想知道大家对这个特性的看法。如果你已经在你的应用中使用它了，记得下面留言分享一下哦。</p>
<p>完，我是小智，今天准备去干点啥~</p>
<hr>
<p><strong>代码部署后可能存在的BUG没法实时知道，事后为了解决这些BUG，花了大量的时间进行log 调试，这边顺便给大家推荐一个好用的BUG监控工具 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.fundebug.com%2F%3Futm_source%3Dxiaozhi" target="_blank" rel="nofollow noopener noreferrer" title="https://www.fundebug.com/?utm_source=xiaozhi" ref="nofollow noopener noreferrer">Fundebug</a>。</strong></p>
<p>原文：<a href="https://link.juejin.cn/?target=https%3A%2F%2Flearnvue.co%2F2021%2F06%2Flazy-load-components-in-vue-with-defineasynccomponent%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://learnvue.co/2021/06/lazy-load-components-in-vue-with-defineasynccomponent/" ref="nofollow noopener noreferrer">learnvue.co/2021/06/laz…</a></p>
<h2 data-id="heading-4">交流</h2>
<blockquote>
<p>有梦想，有干货，微信搜索 <strong>【大迁世界】</strong> 关注这个在凌晨还在刷碗的刷碗智。</p>
<p>本文 GitHub  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fqq449245884%2Fxiaozhi" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/qq449245884/xiaozhi" ref="nofollow noopener noreferrer">github.com/qq449245884…</a> 已收录，有一线大厂面试完整考点、资料以及我的系列文章。</p>
</blockquote></div>  
</div>
            