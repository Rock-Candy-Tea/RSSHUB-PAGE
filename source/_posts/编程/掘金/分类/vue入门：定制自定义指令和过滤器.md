
---
title: 'vue入门：定制自定义指令和过滤器'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5860'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 01:55:20 GMT
thumbnail: 'https://picsum.photos/400/300?random=5860'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>这是我参与 8 月更文挑战的第 14 天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
</blockquote>
<p>本教程为入门教程，如有错误，请各位前端大佬指出。</p>
<h3 data-id="heading-0">1.什么是自定义指令</h3>
<p>Vue中内置了很多的指令，如v-model、v-show、v-html等，但是有时候这些指令并不能满足我们，或者说我们想为元素附加一些特别的功能，例如需要判断按钮是否显示，通常的解决方案就是自定义指令，这时候，我们就需要用到vue中一个很强大的功能了—自定义指令。</p>
<h3 data-id="heading-1">2.全局自定义指令代码实现</h3>
<p>全局指令：在整个项目中都可以使用。下文将教你如何建立全局指令。</p>
<h4 data-id="heading-2">1.创建指令</h4>
<p>在创建指令时，需要在main.js中新建与声明指令。</p>
<pre><code class="copyable">//全局指令
Vue.directive('focus', &#123;
    // 当被绑定的元素插入到 DOM 中时……
    inserted: function(el) &#123;
        // 聚焦元素
        el.focus()
    &#125;
&#125;)

Vue.directive('mycss', &#123;
    // 当被绑定的元素插入到 DOM 中时……
    inserted: function(el) &#123;
        // 聚焦元素
        el.style.color = "#f00"
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">2.添加g-direct.js </h4>
<p>同时我们也需要新建g-direct.js ，并在js中新建自定义指令。</p>
<pre><code class="copyable">import Vue from 'vue'

//全局指令
Vue.directive('focus', &#123;
    // 当被绑定的元素插入到 DOM 中时……
    inserted: function(el) &#123;
        // 聚焦元素
        el.focus()
    &#125;
&#125;)

Vue.directive('mycss', &#123;
    // 当被绑定的元素插入到 DOM 中时……
    inserted: function(el) &#123;
        // 聚焦元素
        el.style.color = "#f00"
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">3.引入g-direct.js </h4>
<p>然后在main.js引入新建立的g-direct.js 。</p>
<pre><code class="copyable">import Vue from 'vue'
import App from './App'
import router from './router'
import g_direct from './g-direct'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue(&#123;
    el: '#app',
    router,
    components: &#123; App &#125;,
    template: '<App/>'
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">4.使用自定义指令</h4>
<p>这样，我们就可以页面中使用我们新建立的自定义指令了。当使用指令后，会执行指令的函数。</p>
<pre><code class="copyable"><template>
<div id="example-3">
  hello
   <input v-focus type = "text" name = ""
   <p v-mycss>aaaa</p>
</div>
</template>

<script>
export default &#123;
name: 'anim',
data () &#123;
  return &#123;
    show: true
&#125;
&#125;,
methods: &#123;
&#125;
&#125;
</script>

<style>
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">3.局部指令实现</h3>
<p>顾名思义，局部指令为当前页面建立，且只能在当前页面使用。下文介绍如何建立和使用局部指令。</p>
<pre><code class="copyable"><template>
<div id="example-3">
  hello
   <input v-test type = "text" name = ""/>
   <p v-mycss>aaaa</p>
</div>
</template>

<script>
export default &#123;
name: 'anim',
data () &#123;
  return &#123;
    show: true
&#125;
&#125;,
methods: &#123;
&#125;,
directives: &#123;
  test: &#123;
    // 指令的定义
    inserted: function (el) &#123;
      el.focus()
    &#125;
  &#125;
&#125;
&#125;
</script>

<style>

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>inserted是什么意思 vue提供了5个勾子函数： 一个指令定义对象可以提供如下几个钩子函数 (均为可选)：</p>
<ul>
<li>bind：只调用一次，指令第一次绑定到元素时调用。在这里可以进行一次性的初始化设置，bind是初始化调用。</li>
<li>inserted：被绑定元素插入父节点时调用 (仅保证父节点存在，但不一定已被插入文档中)。</li>
<li>update：所在组件的 VNode 更新时调用，但是可能发生在其子 VNode 更新之前。指令的值可能发生了改变，也可能没有。但是你可以通过比较更新前后的值来忽略不必要的模板更新 。</li>
</ul>
<h3 data-id="heading-7">4.过滤器</h3>
<p>过滤器是对即将显示的数据做进一步的筛选处理，然后进行显示，值得注意的是过滤器并没有改变原来的数据，只是在原数据的基础上产生新的数据。</p>
<h4 data-id="heading-8">1.全局过滤器</h4>
<p>这里有两种写法，下文分别介绍。</p>
<h5 data-id="heading-9">1.直接写在main.js中</h5>
<pre><code class="copyable">// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import g_direct from './g-direct'

Vue.config.productionTip = false

Vue.filter('capitalize', function(value) &#123;
    if (!value) return ''
    value = value.toString()
    return value.charAt(0).toUpperCase() + value.slice(1)
&#125;)


/* eslint-disable no-new */
new Vue(&#123;
    el: '#app',
    router,
    components: &#123; App &#125;,
    template: '<App/>'
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-10">2.新建.js文件然后引入</h5>
<pre><code class="copyable">main.js
// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import g_direct from './g-direct'
import filter from './filter'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue(&#123;
    el: '#app',
    router,
    components: &#123; App &#125;,
    template: '<App/>'
&#125;)


新建的filter.js文件
import Vue from 'vue'

Vue.filter('capitalize', function(value) &#123;
    if (!value) return ''
    value = value.toString()
    return value.charAt(0).toUpperCase() + value.slice(1)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">3.调用过滤器</h5>
<p>这样就可以执行过滤器中的函数了。</p>
<pre><code class="copyable"><template>
<div id="example-3">
   <p>&#123;&#123;message|capitalize&#125;&#125;</p>
</div>
</template>

<script>
export default &#123;
name: 'anim',
data () &#123;
  return &#123;
    message: "aaaaa"
&#125;
&#125;,
methods: &#123;
&#125;
&#125;
</script>

<style>
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">2.局部过滤器</h4>
<p>只能在本页面中新建使用。以下附上代码。</p>
<pre><code class="copyable"><template>
<div id="example-3">
   &#123;&#123;money|myMoney&#125;&#125;
</div>
</template>

<script>
export default &#123;
name: 'anim',
data () &#123;
  return &#123;
    message: "aaaaa",
    money:11
&#125;
&#125;,
methods: &#123;
&#125;,
filters:&#123;
  myMoney(value)&#123;
     return  "$"+value
  &#125;
&#125;
&#125;
</script>

<style>
</style>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            