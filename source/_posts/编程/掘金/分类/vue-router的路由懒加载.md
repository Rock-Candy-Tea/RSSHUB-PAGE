
---
title: 'vue-router的路由懒加载'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2781'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 18:11:30 GMT
thumbnail: 'https://picsum.photos/400/300?random=2781'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第25天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>路由懒加载也叫作延迟加载，使用懒加载可以减少我们第一次打开项目首页的时间，不至于页面出现长时间的白屏，即使添加了开场动画也不好看，而使用懒加载的话就可以减少这样的情况发生，优化用户的体验</p>
<p>当打包构建应用时，JavaScript 包会变得非常大，影响页面加载。如果我们能把不同路由对应的组件分割成不同的代码块，然后当路由被访问的时候才加载对应组件，这样就更加高效了。</p>
<p>结合 Vue 的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fguide%2Fcomponents-dynamic-async.html%23%25E5%25BC%2582%25E6%25AD%25A5%25E7%25BB%2584%25E4%25BB%25B6" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/guide/components-dynamic-async.html#%E5%BC%82%E6%AD%A5%E7%BB%84%E4%BB%B6" ref="nofollow noopener noreferrer">异步组件 (opens new window)</a>和 Webpack 的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdoc.webpack-china.org%2Fguides%2Fcode-splitting-async%2F%23require-ensure-%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://doc.webpack-china.org/guides/code-splitting-async/#require-ensure-/" ref="nofollow noopener noreferrer">代码分割功能 (opens new window)</a>，轻松实现路由组件的懒加载。</p>
<p>首先，可以将异步组件定义为返回一个 Promise 的工厂函数 (该函数返回的 Promise 应该 resolve 组件本身)：</p>
<pre><code class="copyable">const NotFound = () =>
  Promise.resolve(&#123;
    /* 组件定义对象 */
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是一些路由懒加载的写法</p>
<p>第一种
在 Webpack 2 中，我们可以使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftc39%2Fproposal-dynamic-import" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/tc39/proposal-dynamic-import" ref="nofollow noopener noreferrer">动态 import (opens new window)</a>语法来定义代码分块点 (split point)：</p>
<p>结合上面的Promise 的工厂函数和import两者，这就是如何定义一个能够被 Webpack 自动代码分割的异步组件</p>
<p>在路由配置中什么都不需要改变，只需要像往常一样使用 <code>NotFound</code>：</p>
<pre><code class="copyable">const NotFound = () => import('../page/404.vue')

export default new Router(&#123;
  routes: [
    &#123;
      path: '*',
      name: 'NotFound',
      component: NotFound
    &#125;,
  ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二种</p>
<pre><code class="copyable">const NotFound = () => import('../page/404.vue')

export default new Router(&#123;
  routes: [
    &#123;
      name: 'userShoppingCart',
      path: '/userShoppingCart/:chatid',
      component: ()=> import('../pages/user/userShoppingCart.vue')
    &#125;,
  ]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-0">把组件按组分块</h3>
<p>有时候我们想把某个路由下的所有组件都打包在同个异步块 (chunk) 中。只需要使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.js.org%2Fguides%2Fcode-splitting-require%2F%23chunkname" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.js.org/guides/code-splitting-require/#chunkname" ref="nofollow noopener noreferrer">命名 chunk (opens new window)</a>，一个特殊的注释语法来提供 chunk name (需要 Webpack > 2.4)。</p>
<pre><code class="copyable">const Foo = () => import(/* webpackChunkName: "group-foo" */ './Foo.vue')
const Bar = () => import(/* webpackChunkName: "group-foo" */ './Bar.vue')
const Baz = () => import(/* webpackChunkName: "group-foo" */ './Baz.vue')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Webpack 会将任何一个异步模块与相同的块名称组合到相同的异步块中。</p></div>  
</div>
            