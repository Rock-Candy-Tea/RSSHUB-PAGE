
---
title: 'Vue2.X复盘'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4025'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 19:01:58 GMT
thumbnail: 'https://picsum.photos/400/300?random=4025'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<p>使用vue也一年多了，这是对之前的一次复盘，内容没有官方文档详细，对于vue大概也只是停留在使用的阶段，对于源码也没有过多的关注(这也是之后需要提升的),本文的内容可能存在很多的不足之处，希望大佬们可以帮忙指正，让我可以完善一下。真的是提笔容易下笔难，复盘感觉也没有那么清晰，但是也算是一次小总结吧</p>
<h4 data-id="heading-0">数据处理</h4>
<p>推荐几个库<br>
时间处理推荐<a href="https://dayjs.fenxianglu.cn/" target="_blank" rel="nofollow noopener noreferrer">Day.js</a><br>
数据处理<a href="https://www.lodashjs.com/docs/lodash.mapKeys" target="_blank" rel="nofollow noopener noreferrer">lodash</a></p>
<h4 data-id="heading-1">指令</h4>
<details>
<summary>vue中有哪几种指令?</summary>
<pre><code class="hljs language-vue copyable" lang="vue">v-html v-text v-if v-else v-else-if v-show v-for v-on v-bind v-model v-slot v-pre v-cloak v-once
<span class="copy-code-btn">复制代码</span></code></pre>
</details>
<h5 data-id="heading-2">v-text 和 v-html</h5>
<p>相同点两者都可以渲染数据,但是v-html可以解析标签</p>
<pre><code class="hljs language-vue copyable" lang="vue"><span v-text="msg"></span>
<span v-html="htmlMsg"></span>
data()&#123;return&#123;
    msg:'我是一个span标签'
    htmlMsg:'<strong>我是一个span标签</strong>'
&#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">v-if和v-for不推荐在同一元素上连用</h5>
<p>当它们处于同一节点，v-for 的优先级比 v-if 更高，这意味着 v-if 将分别重复运行于每个 v-for 循环中。</p>
<h5 data-id="heading-4">v-if vs v-show</h5>
<p>v-show是通过css display去控制dom节点的显示或隐藏，v-if则是控制dom节点是否存在，频繁使用v-show,否则使用v-if</p>
<h5 data-id="heading-5">v-for与key</h5>
<p>给dom节点增加唯一标识符，可以高效的更新虚拟dom</p>
<h5 data-id="heading-6">v-model</h5>
<p>本质上是语法糖，会根据标签的不同生成不同的事件和属性</p>
<pre><code class="hljs language-vue copyable" lang="vue"><input v-model="currentValue">等同于下面的
<input v-bind:value="currentValue" v-on:input="currentValue = $event.target.value">
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">v-cloak</h5>
<p>防止在页面加载时先出现变量名闪烁的情况</p>
<h4 data-id="heading-8">生命周期</h4>
<h5 data-id="heading-9">概述</h5>
<details>
<summary>vue中有哪几个生命周期?</summary>
<pre><code class="hljs language-vue copyable" lang="vue">beforeCreate 实例初始化之后
created 完成了data数据的初始化
beforeMount 相关的render函数呗调用,当还未挂载html到页面上
mounted 挂载完成
beforeUpdate 数据更新前
updated 数据更新后
beforeDestroy 实例销毁前调用,重置操作,清除定时器和监听操作
destroyed 销毁后
<span class="copy-code-btn">复制代码</span></code></pre>
</details>
<h5 data-id="heading-10">在组件外部监听内部的生命周期</h5>
<p>之前我们想监听组件内部的生命周期，可能会选择在对应的生命钩子内emit，然后外部监听,其实我们可以通过hook事件直接监听到对应的生命周期</p>
<pre><code class="hljs language-vue copyable" lang="vue"><base-button @hook:created="createBtn" label="主要按钮"></base-button>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">mounted和created谁更适合ajax请求</h5>
<p>之前一直没在意过这个，直到有次看到关于这个的问题，建议放在mounted里使用，顿感是我一直放错了地方吗?
通过一些资料，感觉差异性不大，为了避免闪屏和一致性(ssr)放在created，需要操作dom放在mounted中。</p>
<h5 data-id="heading-12">created中操作dom</h5>
<p>可以使用$nextTick,将回调延迟到下次DOM更新循环之后执行</p>
<pre><code class="hljs language-vue copyable" lang="vue">this.$nextTick(()=>&#123;...&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-13">nextTick</h5>
<p>Promise.then、MutationObserver 和 setImmediate都不支持的情况下使用setTimeout,前两个是微任务后两个是宏任务，vue通过判断原生环境是否支持，并且不断降级最后使用setTimeout完成</p>
<h4 data-id="heading-14">样式绑定</h4>
<p>对我们可以通过对象的形式以及数组的形式，通过条件来显示相应的样式</p>
<pre><code class="hljs language-vue copyable" lang="vue">对象语法
<div class="base-button-container" :class="[&#123;'disabled':disabled&#125;]" :style="&#123;'margin':margin&#125;">
data()&#123;return&#123;
    margin:'15px',
    disabled:false
&#125;&#125;
数组语法
<div class="base-button-container" :class="[disabled]" :style="[baseStyle]">
data()&#123;return&#123;
    baseStyle:&#123;
        color:'red'
    &#125;,
    disabled:'disabled'
&#125;&#125;
使用三目运算符,控制样式
<div class="base-button-container" :style="&#123;'margin':isBorder?'0':'15px'&#125;">
data()&#123;return&#123;
    isBorder:false
&#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">vue-router</h4>
<h5 data-id="heading-16">beforeEach</h5>
<p>处理身份验证(查看是否存在token)
根据用户的权限过滤路由表</p>
<pre><code class="hljs language-js copyable" lang="js">来源于vue-element-admin
router.beforeEach(<span class="hljs-keyword">async</span>(to, <span class="hljs-keyword">from</span>, next) => &#123;
  <span class="hljs-comment">// start progress bar</span>
  NProgress.start()

  <span class="hljs-comment">// set page title</span>
  <span class="hljs-built_in">document</span>.title = getPageTitle(to.meta.title)

  <span class="hljs-comment">// determine whether the user has logged in</span>
  <span class="hljs-keyword">const</span> hasToken = getToken()

  <span class="hljs-keyword">if</span> (hasToken) &#123;
    <span class="hljs-keyword">if</span> (to.path === <span class="hljs-string">'/login'</span>) &#123;
      <span class="hljs-comment">// if is logged in, redirect to the home page</span>
      next(&#123; <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span> &#125;)
      NProgress.done() <span class="hljs-comment">// hack: https://github.com/PanJiaChen/vue-element-admin/pull/2939</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// determine whether the user has obtained his permission roles through getInfo</span>
      <span class="hljs-keyword">const</span> hasRoles = store.getters.roles && store.getters.roles.length > <span class="hljs-number">0</span>
      <span class="hljs-keyword">if</span> (hasRoles) &#123;
        next()
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">try</span> &#123;
          <span class="hljs-comment">// get user info</span>
          <span class="hljs-comment">// note: roles must be a object array! such as: ['admin'] or ,['developer','editor']</span>
          <span class="hljs-keyword">const</span> &#123; roles &#125; = <span class="hljs-keyword">await</span> store.dispatch(<span class="hljs-string">'user/getInfo'</span>)

          <span class="hljs-comment">// generate accessible routes map based on roles</span>
          <span class="hljs-keyword">const</span> accessRoutes = <span class="hljs-keyword">await</span> store.dispatch(<span class="hljs-string">'permission/generateRoutes'</span>, roles)

          <span class="hljs-comment">// dynamically add accessible routes</span>
          router.addRoutes(accessRoutes)

          <span class="hljs-comment">// hack method to ensure that addRoutes is complete</span>
          <span class="hljs-comment">// set the replace: true, so the navigation will not leave a history record</span>
          next(&#123; ...to, <span class="hljs-attr">replace</span>: <span class="hljs-literal">true</span> &#125;)
        &#125; <span class="hljs-keyword">catch</span> (error) &#123;
          <span class="hljs-comment">// remove token and go to login page to re-login</span>
          <span class="hljs-keyword">await</span> store.dispatch(<span class="hljs-string">'user/resetToken'</span>)
          Message.error(error || <span class="hljs-string">'Has Error'</span>)
          next(<span class="hljs-string">`/login?redirect=<span class="hljs-subst">$&#123;to.path&#125;</span>`</span>)
          NProgress.done()
        &#125;
      &#125;
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">/* has no token*/</span>

    <span class="hljs-keyword">if</span> (whiteList.indexOf(to.path) !== -<span class="hljs-number">1</span>) &#123;
      <span class="hljs-comment">// in the free login whitelist, go directly</span>
      next()
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// other pages that do not have permission to access are redirected to the login page.</span>
      next(<span class="hljs-string">`/login?redirect=<span class="hljs-subst">$&#123;to.path&#125;</span>`</span>)
      NProgress.done()
    &#125;
  &#125;
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-17">hash和history模式的区别</h5>
<p>最直观的区别就是hash模式下url中带了'#',history模式下需要前端的URL和后端发起请求的URL一致，默认是hash模式</p>
<h5 data-id="heading-18">路由传值</h5>
<p>场景：路由跳转显示商品详情</p>
<pre><code class="hljs language-js copyable" lang="js">页面刷新时，数据不会丢失
$router.push(&#123;<span class="hljs-attr">query</span>:&#123;&#125;&#125;)
组件内部获取值
$route.query.X

使用$router.push(&#123;<span class="hljs-attr">params</span>:&#123;&#125;&#125;)刷新页面携带的数据会丢失
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">vueX</h4>
<p>Vuex 是一个专为 Vue.js 应用程序开发的状态管理模式
使用场景：
多个视图依赖于同一状态。
来自不同视图的行为需要变更同一状态。</p>
<details>
<summary>五个核心属性?</summary>
<pre><code class="hljs language-vue copyable" lang="vue">state、getters、mutations、actions、modules 。
<span class="copy-code-btn">复制代码</span></code></pre>
</details>
<p>vuex在界面刷新的时候会初始化导致数据重置，这时候需要将数据存放在localStorage或者sessionStorage中</p>
<pre><code class="hljs language-js copyable" lang="js">初始化的时候优先使用sessionStorage内的数据
<span class="hljs-keyword">const</span> state = &#123;
  <span class="hljs-attr">state1</span>: <span class="hljs-built_in">JSON</span>.parse(sessionStorage.getItem(<span class="hljs-string">'state1'</span>)) || <span class="hljs-literal">null</span>,
&#125;
mutations中去更新sessionStorage内的数据
  <span class="hljs-attr">SET_STATE1</span>: <span class="hljs-function">(<span class="hljs-params">state, keyData</span>) =></span> &#123;
    sessionStorage.setItem(<span class="hljs-string">'state1'</span>, <span class="hljs-built_in">JSON</span>.stringify(keyData))
    state.state1 = keyData
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-20">组件内使用</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.$store.state.xx
<span class="hljs-built_in">this</span>.$store.getters.xx <span class="hljs-comment">//类似于计算属性</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-21">修改</h5>
<p>显示的commit(提交)mutation或者dispatch action来修改state中的数据</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.$store.commit(<span class="hljs-string">'SET_STATE1'</span>, keyData) <span class="hljs-comment">//SET_STATE1为mutations定义的</span>
<span class="hljs-built_in">this</span>.$store.dispatch(<span class="hljs-string">'SET_STATE1'</span>, <span class="hljs-literal">null</span>) <span class="hljs-comment">//SET_STATE1为actions定义的</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">axios</h4>
<h5 data-id="heading-23">params传参</h5>
<p>传递数组的时候，需要a=1&a=2&a=3</p>
<pre><code class="hljs language-js copyable" lang="js">qs.stringify 将对象序列化成URL的形式
qs.stringify(&#123; <span class="hljs-attr">a</span>: [<span class="hljs-string">'1'</span>, <span class="hljs-string">'2'</span>, <span class="hljs-string">'3'</span>] &#125;, &#123; <span class="hljs-attr">indices</span>: <span class="hljs-literal">false</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-24">封装</h5>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">return</span> request(&#123;
    <span class="hljs-attr">url</span>: <span class="hljs-string">''</span>,
    <span class="hljs-attr">method</span>: <span class="hljs-string">'get'</span>,
    params
  &#125;)
  
  request.js
  创建一个axios请求，并且在request的时候添加token，reponse中处理请求返回的内容，下面内容来自于vue-element-admin用这个的话都是现成的
  <span class="hljs-keyword">const</span> service = axios.create(&#123;
  <span class="hljs-attr">baseURL</span>: process.env.VUE_APP_BASE_API, <span class="hljs-comment">// url = base url + request url</span>
  <span class="hljs-comment">// withCredentials: true, // send cookies when cross-domain requests</span>
  <span class="hljs-attr">timeout</span>: <span class="hljs-number">5000</span> <span class="hljs-comment">// request timeout</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">组件化</h4>
<details>
<summary>组件传值的几种方式?</summary>
<pre><code class="hljs language-vue copyable" lang="vue">父子间 props和emit 实例$parent,$children[节制地使用]
跨组件 Event Bus
vuex 状态管理实现通信
<span class="copy-code-btn">复制代码</span></code></pre>
</details>
<h5 data-id="heading-26">attrs和listeners</h5>
<p>在项目中，难免要去二次封装element组件,如果所有的属性都需要通过props传递给内部的element组件，会显得很繁杂，利用<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>a</mi><mi>t</mi><mi>t</mi><mi>r</mi><mi>s</mi><mtext>和</mtext></mrow><annotation encoding="application/x-tex">attrs和</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal">a</span><span class="mord mathnormal">t</span><span class="mord mathnormal">t</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">s</span><span class="mord cjk_fallback">和</span></span></span></span></span>listeners就可以跨层级的传递和监听了</p>
<pre><code class="hljs language-vue copyable" lang="vue">    <div class="base-table-container">
        <el-table :data="list" v-on="$listeners" v-bind="$attrs" >
            <slot></slot>
        </el-table>
    </div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-27">结语</h4>
<p>还是再次推荐文档的阅读，对于理念上和一些细节的认知都会更加清晰，这次复盘写文章好像遗落了蛮多东西的，争取之后完善起来。</p></div>  
</div>
            