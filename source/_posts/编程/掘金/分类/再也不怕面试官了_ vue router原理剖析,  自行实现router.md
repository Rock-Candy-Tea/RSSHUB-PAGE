
---
title: '再也不怕面试官了_ vue router原理剖析,  自行实现router'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=101'
author: 掘金
comments: false
date: Mon, 31 May 2021 22:21:54 GMT
thumbnail: 'https://picsum.photos/400/300?random=101'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近面试官总喜欢问全家桶原理, 所以有了这篇文章, vue-router原理剖析, 一边讲解原理一边自己实现.看完绝对能让大家有所收获</p>
<p>我们正常使用router, 是在router.js里配置options, 并抛出Router实例</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Router <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
<span class="hljs-comment">// 引入Router</span>
Vue.use(Router)

<span class="hljs-keyword">const</span> routes = [
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'home'</span>
    &#125;
]
<span class="hljs-comment">// 抛出实例</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Router(&#123;
    routes
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在main.js中挂载Router实例</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>
<span class="hljs-comment">// 将带有配置项的Router实例挂载到Vue实例上</span>
<span class="hljs-keyword">new</span> Vue(&#123;
    router,
    <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;).$mounted(<span class="hljs-string">'#app)

</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以看到 一切的起点在于</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Router <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
Vue.use(Router)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>分析第一步, import进来什么东西, 或者说Vue插件是什么样的形式.</p>
<p>答案是 <em><strong>函数或对象</strong></em>  并且里面一定有一个 <em><strong>install方法</strong></em></p>
<p>引入进来之后 Vue.use就是调用<em><strong>函数中的intall方法</strong></em>, 并且传入<em><strong>Vue构造函数</strong></em>, 为什么要传入呢, 因为方便我们<em><strong>修改Vue的原型</strong></em>, 起到扩展的作用</p>
<p>下面用自己的代码写一个router类</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> Vue;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MiniRouter</span> </span>&#123;
&#125;
<span class="hljs-comment">// 首先挂载install方法</span>
MiniRouter.install = <span class="hljs-function"><span class="hljs-title">funciton</span>(<span class="hljs-params">_Vue</span>)</span> &#123;
    Vue = _Vue
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> MiniRouter
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在已经能被引用了, 但还没有任何功能, 我们想一下router都有什么功能</p>
<ol>
<li>可以在Vue里使用this.router操作页面</li>
<li>可以使用<code><router-linke></code>标签和<code><router-view></code>标签</li>
<li>在url发生变化时, 页面内容发生变化</li>
</ol>
<p>首先先来说第一点, 让vue可以在组件中使用this.router, this.route, 那么就需要在this上挂载这两个对象</p>
<p>如何去挂载? 我们很容易就能想到</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.prototype.$router = &#123;&#125;
Vue.prototype.$route = &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可不能是个空对象吧 应该是有相关配置的实例才对啊, 那么问题很明显, 我们需要<em><strong>Router实例</strong></em></p>
<p>再来看一下router.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Router <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
Vue.use(Router) <span class="hljs-comment">// 在这里执行的install方法</span>
<span class="hljs-keyword">const</span> routes = [
    &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'home'</span>
    &#125;
]
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Router(&#123; <span class="hljs-comment">// 在这里创建的Router实例</span>
    routes
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是说在install的时候我们还没有Router实例, 所以我们的目的是延时执行挂载代码,等到创建Router实例之后再执行. router的解决方案是利用Vue的全局混入, mixin, 这里很巧妙. 因为创建Vue实例时, 会把Router实例挂载到自身的options上 我们可以在组件里用<code>this.$options.router</code>访问</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> Vue;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MiniRouter</span> </span>&#123;
&#125;
<span class="hljs-comment">// 首先挂载install方法</span>
MiniRouter.install = <span class="hljs-function"><span class="hljs-title">funciton</span>(<span class="hljs-params">_Vue</span>)</span> &#123;
    Vue = _Vue
    Vue.mixin(&#123; <span class="hljs-comment">// mixin中的函数在触发组件生命周期时才会执行, 此时已可以使用this, 指向组件实例</span>
        <span class="hljs-function"><span class="hljs-title">beforeCreate</span>(<span class="hljs-params"></span>)</span> &#123; 
            <span class="hljs-comment">// 混入到beforeCreate生命周期中, 每个组件的这个生命周期都会执行, 但这显然不对</span>
            <span class="hljs-comment">// 我们只需要在根组件里执行一次挂载操作 我们可以利用this.$options.router, </span>
            <span class="hljs-comment">// 因为只有根组件才会有</span>
            <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.$options.router) &#123;
                Vue.prototype.$router = <span class="hljs-built_in">this</span>.$options.router
            &#125;   
        &#125;
    &#125;)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> MiniRouter
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此我们已经挂载了router实例到vue的$router上, 但没有任何功能</p>
<p>接下来看第二点, 挂载全局组件<code><router-linke></code>和<code><router-view></code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 首先挂载install方法</span>
MiniRouter.install = <span class="hljs-function"><span class="hljs-title">funciton</span>(<span class="hljs-params">_Vue</span>)</span> &#123;
    Vue = _Vue
    Vue.mixin(&#123; <span class="hljs-comment">// mixin中的函数在触发组件生命周期时才会执行, 此时已可以使用this, 指向组件实例</span>
        <span class="hljs-function"><span class="hljs-title">beforeCreate</span>(<span class="hljs-params"></span>)</span> &#123; 
            <span class="hljs-comment">// 混入到beforeCreate生命周期中, 每个组件的这个生命周期都会执行, 但这显然不对</span>
            <span class="hljs-comment">// 我们只需要在根组件里执行一次挂载操作 我们可以利用this.$options.router, </span>
            <span class="hljs-comment">// 因为只有根组件才会有</span>
            <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.$options.router) &#123;
                Vue.prototype.$router = <span class="hljs-built_in">this</span>.$options.router
            &#125;   
        &#125;
    &#125;)
    <span class="hljs-comment">// 注意正常项目中只能用render函数, 不能使用template</span>
    <span class="hljs-comment">// 因为正常项目是runtime环境,没有编译器, 走的是webpack的vue-loader</span>
    Vue.component(<span class="hljs-string">'router-link'</span>, &#123;
        <span class="hljs-comment">// <router-link to="about">jump</router-link></span>
        <span class="hljs-attr">props</span>: &#123;
            <span class="hljs-attr">to</span>: &#123; <span class="hljs-comment">// 接受to属性, 必传参数</span>
                <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
                <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
            &#125;
            
        &#125;
        <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span> &#123;
            <span class="hljs-comment">// h即createElement, 返回vnode</span>
            <span class="hljs-comment">// router-link默认为a标签, 利用 this.$slots.default拿到标签中间的内容, 叫默认插槽</span>
            <span class="hljs-comment">// a标签应有href 跳转to指定地址, </span>
            <span class="hljs-keyword">return</span> h(<span class="hljs-string">'a'</span>, &#123;
                 <span class="hljs-attr">attrs</span>: &#123;
                     <span class="hljs-attr">href</span>: <span class="hljs-string">'#'</span> + <span class="hljs-built_in">this</span>.to
                 &#125;
            &#125;, <span class="hljs-built_in">this</span>.$slots.default)
        &#125;
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code><router-link></code>实现了, 接下来是<code><router-view></code></p>
<p>router-view思路其实也简单, 其实就是通过地址匹配路由, 找到组件, 这个步骤在MiniRouter中完成</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> Vue;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MiniRouter</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
        <span class="hljs-comment">// 传入的options中包含路由配置信息, 保存下来, 这样实例可以拿到配置</span>
        <span class="hljs-built_in">this</span>.$options = options
        <span class="hljs-comment">// 接下来需要监听hashchange事件, 并做出相应</span>
        <span class="hljs-comment">// 如何做出响应? 我们需要一个响应式的数据, 通过改变这个数据的值, 做出响应</span>
        <span class="hljs-comment">// 我们这里使用defineReactive</span>
        Vue.util.defineReactive(
            <span class="hljs-built_in">this</span>, <span class="hljs-comment">// MiniRouter构造函数</span>
            <span class="hljs-string">'current'</span>, <span class="hljs-comment">// 通过改变这个字段的值做出响应</span>
            <span class="hljs-built_in">window</span>.location.hash.slice(<span class="hljs-number">1</span>) || <span class="hljs-string">'/'</span> , 初始值
        )
              
        <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'hashchange'</span>, <span class="hljs-function">() =></span> &#123;
            <span class="hljs-comment">// 拿到的hash前面带'#', slice处理, 去掉'#', 保存下来, 默认值为‘/’</span>
            <span class="hljs-built_in">this</span>.curremt = <span class="hljs-built_in">window</span>.location.hash.slice(<span class="hljs-number">1</span>) || <span class="hljs-string">'/'</span> 
        &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时已经可以响应url的变化了</p>
<pre><code class="hljs language-js copyable" lang="js">Vue.component(<span class="hljs-string">'router-view'</span>, &#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span> &#123;
        <span class="hljs-keyword">let</span> component = <span class="hljs-literal">null</span>; 
        <span class="hljs-comment">// this.$router就是我们之前在Vue.prototype上挂载的Router实例 </span>
        <span class="hljs-comment">// 通过Router实例能获取到上一步保存的options</span>
        <span class="hljs-comment">// options里面有new实例的时候传入的routes配置表</span>
        <span class="hljs-comment">// 查找与上一步保存的当前path相同的项</span>
        <span class="hljs-keyword">const</span> router = <span class="hljs-built_in">this</span>.$router.$options.routes
                            .find(<span class="hljs-function"><span class="hljs-params">route</span> =></span> route.path === <span class="hljs-built_in">this</span>.$router.current)
        <span class="hljs-keyword">if</span> (route) &#123;
            <span class="hljs-comment">// 如果有相同的 取出component组件</span>
            component = route.component
        &#125;
        <span class="hljs-comment">// 渲染匹配的组件, 没有匹配到, 则默认值null, 不渲染</span>
        <span class="hljs-keyword">return</span> h (component)
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时已经可以通过点击<code><router-link></code>切换path, 并渲染不同的组件了</p>
<p>大功告成!</p>
<p>恭喜你, 以后可以和面试官说自己可以手写vue-router了! 举一反三一下, 还可以写出其他插件.</p>
<p>码字不易, 希望小伙伴能给个点赞收藏, 也是我以后更新的动力, 感谢大家!</p></div>  
</div>
            