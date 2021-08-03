
---
title: 'vue之vue-router加深印象'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://juejin.cn/post/6992022783102287908'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 18:19:27 GMT
thumbnail: 'https://juejin.cn/post/6992022783102287908'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">定义</h4>
<p>单页面之间的跳转，建立并管理url与组件之间的映射关系</p>
<h4 data-id="heading-1">使用</h4>
<pre><code class="copyable"><!--跳转组件 相当于a标签  to相当于href  -->
 <router-link to="/foo">Go to Foo</router-link>
​
<!--路由出口 组件渲染在这里-->
 <router-view></router-view>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">模式</h4>
<p>history模式：不在url中显示#,而是和平常的html路径链接一样，底层是利用了HTML5 History新增的<strong>pushState()和replaceState()方法。</strong> 需要后端支持，暂未用到。</p>
<p><strong><code>History模式就是通过pushState()方法来对浏览器的浏览记录进行修改,来达到不用请求后端来渲染的效果.</code></strong></p>
<p>hash模式：vue的默认路由模式，#代表url中的锚点，通过改变#后面的参数，不会重新加载界面，二是替换组件</p>
<p><strong><code>Hash模式就是通过改变#后面的值,实现浏览器渲染指定的组件.</code></strong></p>
<h4 data-id="heading-3">路由懒加载</h4>
<p>将组件拆分成代码块，防止打包过大</p>
<pre><code class="copyable">const Foo = () => import('./Foo.vue')
​
const router = new VueRouter(&#123;
  routes: [&#123; path: '/foo', component: Foo &#125;]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">路由守卫钩子函数</h4>
<h5 data-id="heading-5">全局守卫</h5>
<pre><code class="copyable">//前置守卫
const router = new VueRouter(&#123; ... &#125;)
//to: Route: 即将要进入的目标 路由对象
//from: Route: 当前导航正要离开的路由
//next: Function: 一定要调用该方法来 resolve 这个钩子。执行效果依赖 next 方法的调用参数
router.beforeEach((to, from, next) => &#123;
  // ...
&#125;)
​
​
//后置守卫
router.afterEach((to, from) => &#123;
  // ...
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">路由独享的守卫</h5>
<pre><code class="copyable">const router = new VueRouter(&#123;
  routes: [
    &#123;
      path: '/foo',
      component: Foo,
      beforeEnter: (to, from, next) => &#123;
        // ...
      &#125;
    &#125;
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">组件内的守卫</h5>
<pre><code class="copyable">beforeRouteEnter(to, from, next) &#123;
    // 在渲染该组件的对应路由被 confirm 前调用
    // 不！能！获取组件实例 `this`
    // 因为当守卫执行前，组件实例还没被创建
  &#125;,
  beforeRouteUpdate(to, from, next) &#123;
    // 在当前路由改变，但是该组件被复用时调用
    // 举例来说，对于一个带有动态参数的路径 /foo/:id，在 /foo/1 和 /foo/2 之间跳转的时候，
    // 由于会渲染同样的 Foo 组件，因此组件实例会被复用。而这个钩子就会在这个情况下被调用。
    // 可以访问组件实例 `this`
  &#125;,
  beforeRouteLeave(to, from, next) &#123;
    // 导航离开该组件的对应路由时调用
    // 可以访问组件实例 `this`
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">组件传参</h4>
<pre><code class="copyable">//router.js
const router = new VueRouter(&#123;
  routes: [
    &#123; 
      path: '/user/:id', 
      component: User,
      props: true 
    &#125;,
​
    // 对于包含命名视图的路由，你必须分别为每个命名视图添加 `props` 选项：
    &#123;
      path: '/user/:id',
      components: &#123; default: User, sidebar: Sidebar &#125;,
      props: &#123; default: true, sidebar: false &#125;
    &#125;
  ]
&#125;)
​
​
​
//user.vue
//获取路由参数
this.id =this.$route.params.id
​
//组件跳转传参
 this.$router.push(&#123;
   path: '/user/10'
 &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">router,route,routers区别</h4>
<p>1、 router:一般指的就是路由实例.如$router。</p>
<p><img src="https://juejin.cn/post/6992022783102287908" alt="image-20210803101607310" loading="lazy" referrerpolicy="no-referrer"></p>
<p>2、 route:指的就是路由对象.例如;$route指的就是当前路由对象。</p>
<p><img src="https://juejin.cn/post/6992022783102287908" alt="image-20210803101410731" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">引用链接：</h4>
<blockquote>
<p>vue官网： <a href="https://link.juejin.cn/?target=https%3A%2F%2Frouter.vuejs.org%2Fzh%2Fguide%2F%23html" target="_blank" rel="nofollow noopener noreferrer" title="https://router.vuejs.org/zh/guide/#html" ref="nofollow noopener noreferrer">router.vuejs.org/zh/guide/#h…</a></p>
</blockquote>
<blockquote>
<p>掘金： <a href="https://juejin.cn/post/6844903665388486664#heading-27" target="_blank" title="https://juejin.cn/post/6844903665388486664#heading-27">juejin.cn/post/684490…</a></p>
</blockquote></div>  
</div>
            