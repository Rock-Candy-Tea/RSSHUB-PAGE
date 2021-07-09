
---
title: '手写Vue-router核心原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3326'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 20:09:53 GMT
thumbnail: 'https://picsum.photos/400/300?random=3326'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、如何实现前端路由</h2>
<h3 data-id="heading-1">1、什么是前端路由？</h3>
<p>URL 变化引起 UI 更新（无需刷新页面）</p>
<p>所以要思考两个问题：</p>
<ol>
<li>改变URL，却不会引起页面的刷新</li>
<li>如何检测URL变化</li>
</ol>
<h3 data-id="heading-2">2、实现方案</h3>
<p><strong>hash实现</strong></p>
<p>hash是URL中#后面那部分，同时修改hash值不会引起页面的刷新，也不会向服务器重新发送请求。通过hashchange事件可以监听它的变化。改变hash值有以下三种方式：</p>
<ul>
<li>浏览器前进后退改变URL</li>
<li>通过a标签改变URL</li>
<li>通过window.location.hash改变URL</li>
</ul>
<p><strong>备注</strong>：以上三种方式均可以触发hashchang事件</p>
<p><strong>history实现</strong></p>
<p>history是HTML5新增的，提供了两个方法用来修改浏览器的历史记录，且都不会引起页面的刷新</p>
<ul>
<li>pushState，向浏览器中新增一条历史记录，同时修改地址栏</li>
<li>replaceState，直接替换浏览器中当前的历史记录，同时修改地址栏</li>
</ul>
<p>history提供了popstate监听事件，但是只有以下两种情况会触发该事件</p>
<ul>
<li>点击浏览器前进后退的按钮</li>
<li>显示调用history的back、go、forward方法</li>
</ul>
<p><strong>备注</strong>：pushState与replaceState均不会触发popstate事件</p>
<h2 data-id="heading-3">二、原生方式实现</h2>
<p><strong>hash实现方式</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<body>
<ul>
    <ul>
        <!-- 定义路由 -->
        <li><a href="#/home">home</a></li>
        <li><a href="#/about">about</a></li>

        <!-- 渲染路由对应的 UI -->
        <div id="routeView"></div>
    </ul>
</ul>
<script>
    let routerView = document.querySelector('#routeView')
    window.addEventListener('DOMContentLoaded', ()=>&#123;
      if(!location.hash)&#123;//如果不存在hash值，那么重定向到#/
        location.hash="/"
      &#125;else&#123;//如果存在hash值，那就渲染对应UI
        let hash = location.hash;
        routerView.innerHTML = hash
      &#125;
    &#125;)
    window.addEventListener('hashchange', ()=>&#123;
      let hash = location.hash;
      routerView.innerHTML = hash
      console.log('hashChange')
    &#125;)
</script>
</body>

</html>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码解析：</p>
<ol>
<li>页面第一次加载完毕，并不会触发hashchange事件，所以需要手动的给routeView(UI)赋值</li>
<li>点击A链接触发hashchange事件需要做两件事儿
<ul>
<li>修改location中的hash值</li>
<li>给routeView(UI)赋值</li>
</ul>
</li>
</ol>
<p><strong>history实现</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<body>
<div>
    <ul>
        <!-- 定义路由 -->
        <li><a href="/home">home</a></li>
        <li><a href="/about">about</a></li>

        <!-- 渲染路由对应的 UI -->
        <div id="routeView"></div>
    </ul>
</div>
<script>
    let routerView = document.querySelector('#routeView')
    window.addEventListener('popstate', ()=>&#123;
      let pathName = location.pathname;
      routerView.innerHTML = pathName
      console.log('popstate');
      
    &#125;)
    window.addEventListener('DOMContentLoaded', load, false)
    function load (e) &#123;
      !location.pathname && (location.pathname="/") //如果不存在hash值，那么重定向到/
      let ul = document.querySelector('ul')
      ul.addEventListener('click', function (e) &#123;
        e.preventDefault()
        if (e.target.nodeName === 'A') &#123;
          let src = e.target.getAttribute('href')
          history.pushState(src, null, src)     // 修改URL中的地址
          routerView.innerHTML = src            // 更新UI
        &#125;
      &#125;, false)
    &#125;
  
</script>
</body>

</html>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码解析：</p>
<ol>
<li>页面加载完毕后，给A链接绑定事件（这里我通过事件代理的方式来实现），同时要阻止A标签的默认事件</li>
<li>点击A标签并不会触发popstate事件，所有需要手动的去修改URL地址，然后更新routeView(UI)</li>
<li>当我们点击浏览器的前进后退安按钮会触发popstate事件，同样事件触发后，修改URL地址，然后更新routeView(UI)</li>
</ol>
<p><strong>总结：</strong></p>
<ol>
<li>页面第一次加载，需要以下两件事儿：
<ul>
<li>需要判断URL中hash｜pathname是否有值，为空的话，需要为他们赋值（/）</li>
<li>由于第一次加载并不会触发hashchange｜popstate事件，所以需要手动更新UI</li>
</ul>
</li>
<li>事件触发后，需要做两件事儿
<ul>
<li>修改URL中的值(为location.hash、history.pushState赋值)</li>
<li>更新UI</li>
</ul>
</li>
</ol>
<h2 data-id="heading-4">三、Vue-router实现</h2>
<p>这里只实现了hash模式部分，history部分也大相径庭，可以自行补充。实现Vue-router之前先看看Vue中的插件机制是什么样的，它是如何注册的？</p>
<h3 data-id="heading-5">1、Vue.use() 全局注册插件</h3>
<p>先贴上Vue.use代码</p>
<pre><code class="copyable">Vue.use = function(plugin) &#123;
    // 全局维护一个插件列表，防止多次注册相同的插件
    const installedPlugins = this._installedPlugins || (this._intalledPlugins = [])
    if (installedPlugin.indexOf(plugin) > -1) return this
    const args = toArray(argumens, 1) // 将类数组转换成数组，并从1开始截取
    args.unshift(this)                // 将vue的构造函数放置args的第一位
    if (typeof plugin.install === 'function') &#123;
      plugin.install.applay(plugin, args)
    &#125; else if(typeof plugin === 'function') &#123;
      plugin.apply(null, args)
    &#125;
  &#125;

  /**
  *  将类数组转化成数组
  */
  function toArray (list, start) &#123;
    start = start || 0
    let i = list.length - start
    const ret = new Array(i)
    while (i--) &#123;
      console.log('i=', i)
      ret[i] = list[i + start]
    &#125;
    return ret
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码解析：</p>
<ol>
<li>首先接收一个插件构造函数plugin</li>
<li>判断传入的插件在Vue的全局插件列表(_intalledPlugins)是否存在，不存就加入，存在则返回</li>
<li>拼接参数列表args，截取use函数第一个后面是插件的参数，然后将Vue构造函数unshit到数组中的第一位</li>
<li>执行install或可执行函数，并传入args参数列表</li>
</ol>
<p><strong>小结</strong>：</p>
<ol>
<li>Vue会全局维护一个installedPlugins插件列表，防止插件被多次注册</li>
<li>Vue的插件必须是一个带有install方法的对象，或者可执行函数，它会被被当作install方法来执行。同时install方法或者可执行函数，可接收两个参数，分别是：
<ul>
<li>第一个参数用来接受Vue的构造函数</li>
<li>第二个参数是可选的选项对象</li>
</ul>
</li>
</ol>
<h3 data-id="heading-6">2、VueRouter.install方法</h3>
<pre><code class="copyable">// eslint-disable-next-line no-unused-vars
let _Vue
export function install (Vue) &#123;
  _Vue = Vue
  Vue.mixin(&#123;
    beforeCreate () &#123;
      // 1、将router挂在根组件上
      // 2、使每个vue实例上都有一个_routerRoot指向根组件实例
      if (this.$options && this.$options.router) &#123; // 只有根组件才有router
        this._routerRoot = this
        this._router = this.$options.router
        this._router.init(this) // 调用router实例的init方法
        Vue.util.defineReactive(this, '_route', this._router.history.current)
      &#125; else &#123; // 子组件(这里是一级一级传入的)
        this._routerRoot = (this.$parent && this.$parent._routerRoot) || this
      &#125;
    &#125;
  &#125;)

  // 3、this.$router -> this._routerRoot.router  this.$route -> this._routerRoot.router._route
  Object.defineProperty(Vue.prototype, '$router', &#123;
    get () &#123;
      return this._routerRoot._router
    &#125;
  &#125;)
  Object.defineProperty(Vue.prototype, '$route', &#123;
    get () &#123;
      return this._routerRoot._route
    &#125;
  &#125;)

  // 4、组册router-link 与 router-view两个组建
  Vue.component('router-link', &#123;
    props: &#123;
      to: String
    &#125;,
    render (h) &#123;
      var mode = this._routerRoot._router.mode
      let to = mode === 'hash' ? '#' + this.to : this.to
      return h('a', &#123; attrs: &#123; href: to &#125; &#125;, this.$slots.default)
    &#125;
  &#125;)
  Vue.component('router-view', &#123;
    render (h) &#123;
      var component = this._routerRoot._route.component
      return h(component)
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码解析：</p>
<ol>
<li>将Vue作为参数传入在插件内部使用(你总不想打包的时候将Vue打包进去吧！）</li>
<li>使用Vue.mixin主要做以下几件事儿：
<ul>
<li>将router挂在根组件上</li>
<li>使每个vue实例上都有一个_routerRoot指向根组件实例</li>
<li>通过Vue.util.defineReactive()定义了响应式的_route属性，通过修改Vue实例上的_route，会自动调用Vue实例的render()方法，RouteView组件内容会更新</li>
<li>调用router实例的init方法，并将vue实例作为参数传入</li>
</ul>
</li>
<li>将Vue实例的$router、$route分别代理到router、router._route上
(也就是我们平时调用this.<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>r</mi><mi>o</mi><mi>u</mi><mi>t</mi><mi>e</mi><mi>r</mi><mo stretchy="false">(</mo><mtext>路由实例</mtext><mo stretchy="false">)</mo><mtext>、</mtext><mi>t</mi><mi>h</mi><mi>i</mi><mi>s</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">router(路由实例)、this.</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">o</span><span class="mord mathnormal">u</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mopen">(</span><span class="mord cjk_fallback">路</span><span class="mord cjk_fallback">由</span><span class="mord cjk_fallback">实</span><span class="mord cjk_fallback">例</span><span class="mclose">)</span><span class="mord cjk_fallback">、</span><span class="mord mathnormal">t</span><span class="mord mathnormal">h</span><span class="mord mathnormal">i</span><span class="mord mathnormal">s</span><span class="mord">.</span></span></span></span></span>route(当前路由对象))</li>
<li>组册router-link 与 router-view两个组件</li>
</ol>
<h3 data-id="heading-7">3、VueRouter类实现</h3>
<p>上文中，我们已经实现了VueRouter.install方法，且方法里面调用了VueRouter实例上的init方法，现在我们一起实现一个VueRouter类</p>
<h4 data-id="heading-8">constructor构造函数</h4>
<p>构造函数主要做以下几件事儿：</p>
<ul>
<li>接收options参数，保存mode、路由列表(options.routes)在实例上</li>
<li>将路由列表映射成key-value形式，方便后面使用</li>
<li>根据mode类别( HashHistory | HTML5History | AbstractHistory )来实例化一个history（我这里就写一个hash模式的）</li>
</ul>
<h4 data-id="heading-9">init方法实现</h4>
<p><strong>实现思路：</strong></p>
<ol>
<li>保存Vue实例app在router实例上</li>
<li>获取当前路径location(#后面那边分)</li>
<li>通过location获取当前route</li>
<li>保存当前路由(history.current = route)</li>
<li>执行history中的cb回调，并传入参数route（这里就是修改Vue实例上的_route），由于Vue实例上的_route被修改，Vue根组件上的render被执行，RouteView内容被更新</li>
<li>设置hashchange路由监听事件，当路由变化时，重新执行第2步--第5步</li>
</ol>
<p><strong>执行流程</strong></p>
<ul>
<li>保存Vue实例</li>
<li>调用history.transitionTo(以上的第2步--第5步)</li>
<li>执行history.listen(cb)（Ps：cb是一个回调函数，用来修改Vue实例的_route值）</li>
</ul>
<pre><code class="copyable">// init方法中
history.listen(route => &#123;
    this.app._route = route
&#125;)
.....

// History类中的listen
listen (cb) &#123;
    this.cb = cb
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>具体实现如下：</strong></p>
<pre><code class="copyable">import &#123; install &#125; from './install.js'
import History from './history'

class VueRouter &#123;
  constructor (options) &#123;
    this.app = null
    this.mode = options.mode || 'hash'
    this.routes = options.routes
    this.history = new History(options.routes)
  &#125;
  init (app) &#123;
    this.app = app // 保存vue的实例
    var history = this.history
    // history 暂时不考虑 -- 没法测试
    // !location.pathname && (location.pathname = '/')
    // window.addEventListener('popstate', e => &#123;
    //   let path = location.pathname
    //   this.history.transitionTo(
    //     this.history.getCurrentRoute(path),
    //     route => this.history.updateRoute(route)
    //   )
    // &#125;)
    history.transitionTo(// 这里主要做两件事儿 1）初始化的时候更新路由，待用vue实例render 2）给hash做事件监听
      history.getCurrentLocation(),
      (route) => &#123;
        history.setupListener(route)
      &#125;
    )
    history.listen(route => &#123;
      this.app._route = route
    &#125;)
  &#125;
  push (location) &#123;
    this.history.push(location)
  &#125;
  replace (location) &#123;
    this.history.replace(location)
  &#125;
&#125;

VueRouter.install = install

export default VueRouter
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">4、History类实现</h3>
<pre><code class="copyable">class History &#123;
  constructor (routes) &#123;
    this.current = null
    this.cb = null
    this.routerMap = this.createRouterMap(routes)
    this.ensureHash() // 判断URL中是否带有#/，没有的话就给URL重置一下
  &#125;
  ensureHash () &#123;
    !location.hash && (location.hash = '/')
  &#125;
  transitionTo (location, onComplete) &#123;
    let route = this.routerMap[location]
    this.updateRoute(route)
    onComplete && onComplete(route)
  &#125;
  updateRoute (route) &#123;
    this.current = route
    this.cb && this.cb(route)
  &#125;
  getCurrentRoute (location) &#123;
    return this.routerMap[location]
  &#125;
  createRouterMap (routes = []) &#123;
    return routes.reduce((module, route) => &#123;
      module[route.path] = route
      return module
    &#125;, &#123;&#125;)
  &#125;
  setupListener (route) &#123;
    window.addEventListener('hashchange', e => &#123;
      this.transitionTo(
        this.getCurrentLocation()
      )
    &#125;)
  &#125;
  getCurrentLocation () &#123;
    var href = window.location.href
    var index = href.indexOf('#')
    return index > -1 ? href.slice(index + 1) : '/'
  &#125;
  push (location) &#123;
    this.transitionTo(
      location,
      () => &#123;
        // 修改window中的hash
        pushHash(location)
      &#125;
    )
  &#125;

  replace (location) &#123;
    this.transitionTo(
      location,
      () => &#123;
        replaceHash(location)
      &#125;
    )
  &#125;

  listen (cb) &#123;
    this.cb = cb
  &#125;
&#125;

export default History

// 直接替换hash（可以理解为重定向）
function pushHash (hash) &#123;
  location.hash = hash
&#125;

// 替换url后面那部分的hash
function replaceHash (hash) &#123;
  var href = window.location.href
  var index = href.indexOf('#')
  var base = index > -1 ? href.slice(0, index) : href
  window.location.replace(base + '#' + hash)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">四、参考</h2>
<p><a href="https://juejin.cn/post/6854573222231605256#heading-16" target="_blank" title="https://juejin.cn/post/6854573222231605256#heading-16">juejin.cn/post/685457…</a>
<a href="https://juejin.cn/post/6844903612930326541" target="_blank" title="https://juejin.cn/post/6844903612930326541">juejin.cn/post/684490…</a></p></div>  
</div>
            