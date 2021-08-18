
---
title: '_ 浅谈前端 _ Vue基本使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3729'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 22:44:16 GMT
thumbnail: 'https://picsum.photos/400/300?random=3729'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第17天，活动详情查看：</strong> <a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<blockquote>
<p>微信公众号搜索【程序媛小庄】 - 没有白走的路，每一步都算数</p>
</blockquote>
<h2 data-id="heading-0">Vue & jQuery</h2>
<ul>
<li>jquery的定位是获取元素完成特效</li>
<li>vue的定位是方便操作和控制数据完成特效</li>
</ul>
<h2 data-id="heading-1">VUE介绍</h2>
<p>vue.js是目前前端web开发最流行的工具库，由尤雨溪在2014年2月发布的。</p>
<p>另外几个常见的工具库：react.js /angular.js/jQuery</p>
<p>官方网站：</p>
<p>中文：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/" ref="nofollow noopener noreferrer">cn.vuejs.org/</a></p>
<p>英文：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvuejs.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vuejs.org/" ref="nofollow noopener noreferrer">vuejs.org/</a></p>
<p>官方文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fguide%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/guide/" ref="nofollow noopener noreferrer">cn.vuejs.org/v2/guide/</a></p>
<p>vue.js目前有1.x、2.x和3.x 版本，我们学习2.x版本的。</p>
<h2 data-id="heading-2">vue两种开发模式</h2>
<ul>
<li>脚本化引入(vue.js文件在项目根目录下)</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>组件化开发，drf组件化开发</li>
</ul>
<h2 data-id="heading-3">vue基本使用</h2>
<ul>
<li>基本使用步骤</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html">1.在head标签内引入vue.js文件 --- 脚本化引入
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">'vue.js'</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

2.创建标签，为其设置id
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'app'</span>></span><span class="hljs-tag"><<span class="hljs-name">div</span>></span>

3.在body标签中创建script标签对html页面上的其他标签进行操作
3.1 vue的使用是从创建Vue对象开始的
var vm = new Vue();
3.2 创建vue对象的时候需要传递参数，传递的参数必须是json格式的数据，并且此数据至少有两个属性成员el以及data
var vm = new Vue(&#123;
el:'#app',
data:&#123;
数据变量:'变量值'，
message:'哈哈'，

&#125;,
&#125;)
        
        el:设置vue可以操作的html内容范围，值一般就是css的id选择器
        data:保存vue对象中要显示到html页面的数据
    3.3 将vue对象中保存的数据通过模版语法展示到html页面
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'app'</span>></span>
            &#123;&#123;message&#125;&#125;
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>注意事项</li>
</ul>
<pre><code class="copyable">1.实例化vue对象时每个对象名必须是唯一的，一个页面有多个vue对象，每个对象对应一个功能
2.js中所有的变量和语法都是区分大小写的
3.script标签的位置
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">VUE的框架思想 --- MVVM</h2>
<p>MVVM 是Model-View-ViewModel 的缩写，它是一种基于前端开发的架构模式。</p>
<p><code>Model</code>:指代的就是vue对象的data属性里面的数据。这里的数据要显示到页面中。</p>
<p><code>View</code>:指代的就是vue中数据要显示的HTML页面，在vue中，也称之为“视图模板” 。</p>
<p><code>ViewModel</code>:指代的是vue.js中我们编写代码时的vm对象了，它是vue.js的核心，负责连接 View 和 Model，保证视图和数据的一致性，所以前面代码中，data里面的数据被显示在p标签中就是vm对象自动完成的。</p>
<p>在代码中标识每一部分</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Title<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-comment"><!-- View --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        &#123;&#123;message&#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-comment">// View Model</span>
        <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
            <span class="hljs-comment">// Model </span>
            <span class="hljs-attr">data</span>:&#123;
                <span class="hljs-attr">message</span>:<span class="hljs-string">'hahah'</span>
            &#125;
        &#125;);
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在浏览器中可以在 console.log通过 vm对象可以直接访问el和data属性,甚至可以访问data里面的数据</p>
<p>$表示vm对象的属性，这些属性都是vm对象初始化的时候进行赋值的</p>
<pre><code class="hljs language-html copyable" lang="html">console.log(vm.$el)      //  vm对象可以控制的范围
console.log(vm.$data);  // vm对象要显示到页面中的数据
console.log(vm.$data.message);  // 访问data里面的数据
console.log(vm.message);  // 这个 message就是data里面声明的数据,也可以使用 vm.变量名显示其他数据,message只是举例.
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">模版语法显示数据</h2>
<ul>
<li>文本插值：<code>&#123;&#123;&#125;&#125;</code> or  指令<code>v-text</code></li>
</ul>
<p>在双标签中显示纯文本数据要通过&#123;&#123;  &#125;&#125; or  指令<code>v-text</code>来完成数据显示，双括号中还可以支持js表达式和符合js语法的代码</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    &#123;&#123;message&#125;&#125;
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-text</span>=<span class="hljs-string">"message"</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>    
<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-once</span>></span>&#123;&#123; message &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-comment"><!--
&#123;&#123;&#125;&#125;和属性v-text等价
无论何时，绑定的数据对象上 msg变量发生了改变，插值处的内容都会更新。
如果使用了指令v-once则数据仅仅执行一次插值，当数据改变时，插值处的内容不会更新
--></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">双大括号内可以使用变量、表达式、函数等合法的js语法，以下都是合法的
    &#123;&#123; number + 1 &#125;&#125;
    &#123;&#123; ok ? 'YES' : 'NO' &#125;&#125;
    &#123;&#123; message.split('').reverse().join('') &#125;&#125;
    <div v-bind:id="'list-' + id"></div>
但是，每个绑定都只能包含单个表达式，所以下面的例子都不会生效。
    <!-- 这是语句，不是表达式 -->
    &#123;&#123; var a = 1 &#125;&#125;
    <!-- 流控制也不会生效，请使用三元表达式 -->
    &#123;&#123; if (ok) &#123; return message &#125; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在表单输入框中显示data中的数据要添加v-model属性来完成数据显示</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"message"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">textarea</span> <span class="hljs-attr">name</span>=<span class="hljs-string">""</span> <span class="hljs-attr">id</span>=<span class="hljs-string">""</span> <span class="hljs-attr">cols</span>=<span class="hljs-string">"30"</span> <span class="hljs-attr">rows</span>=<span class="hljs-string">"10"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"message"</span>></span><span class="hljs-tag"></<span class="hljs-name">textarea</span>></span>
<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-comment"><!--
使用v-model把data里面的数据显示到表单元素以后，一旦用户修改表单元素的值，则data里面对应数据的值也会随之发生改变，甚至，页面中凡是使用了这个数据都会发生变化。
--></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果双标签的内容要显示的数据包含html代码则需要使用v-html属性</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-html</span>=<span class="hljs-string">"message"</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">span</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
        <span class="hljs-attr">data</span>:&#123;
            <span class="hljs-attr">message</span>:<span class="hljs-string">'<h1>msg</h1>'</span>
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">指令</h2>
<h3 data-id="heading-7">指令介绍</h3>
<p>指令 (Directives) 是带有“v-”前缀的特殊属性。每一个指令在vue中都有固定的作用。</p>
<p>在vue中，提供了很多指令，常用的有：v-if、v-model、v-for等等。</p>
<p>指令会在vm对象的data属性的数据发生变化时，会同时改变元素中的其控制的内容或属性。</p>
<p>因为vue的历史版本原因，所以有一部分指令都有两种写法：</p>
<pre><code class="copyable">vue1.x写法             vue2.x的写法
v-html         ---->   v-html
&#123;&#123; 普通文本 &#125;&#125;          &#123;&#123;普通文本&#125;&#125;
v-bind:属性名   ---->   :属性
v-on:事件名     ---->   @事件名
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">绑定指令</h3>













<table><thead><tr><th align="center">vue1.x写法</th><th align="center">vue2.x的写法</th></tr></thead><tbody><tr><td align="center">v-bind:属性名</td><td align="center">:属性名</td></tr></tbody></table>
<p>v-bind的作用：就是绑定，动态的将标签的属性值与vue对象中的数据变量绑定到一块，实现在vue对象中对标签的属性、样式、class类等进行操作</p>
<h4 data-id="heading-9">属性操作</h4>
<p>将vue对象data属性中的值动态渲染给标签的属性值，相当于告诉属性名你的值是一个来自于vue对象中的变量而不是字符串</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-comment"><!--  vue1.x版本  --></span>
    <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">v-bind:href</span>=<span class="hljs-string">"url"</span>></span>百度<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
    <span class="hljs-comment"><!--  vue2.x版本  --></span>
    <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">:href</span>=<span class="hljs-string">"url"</span>></span>百度<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
        <span class="hljs-attr">data</span>:&#123;
            <span class="hljs-attr">url</span>:<span class="hljs-string">'http://www.baidu.com'</span>,
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">类操作</h4>
<p>类的值可以是字符串/对象/对象名/数组</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
<span class="hljs-comment"><!--  :的意思是告诉属性名你的值是来自vue对象的变量所对应的值  --></span>

    <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"cls1"</span>></span>类的值是字符串<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"&#123;cls1:false&#125;"</span>></span>类的值是对象,对象的值是false,cls1对应的样式就不会生效<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"cls3"</span>></span>类的值是对象名称<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"[cls1,cls2]"</span>></span>类的值是数组，数组中的样式会同时生效,批量给元素增加多个class样式类<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
        <span class="hljs-attr">data</span>:&#123;
            <span class="hljs-attr">cls1</span>:<span class="hljs-string">'box1'</span>,
            <span class="hljs-attr">cls2</span>:<span class="hljs-string">'box2'</span>,
            <span class="hljs-attr">cls3</span>:&#123;<span class="hljs-string">'box1'</span>:<span class="hljs-literal">false</span>,<span class="hljs-string">'box2'</span>:<span class="hljs-literal">true</span>&#125;,

        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">样式(style)操作</h4>
<p>样式的值可以是字符串/对象/对象名/数组</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"box"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"color: red; background: blue"</span>></span>style1,普通的样式写法<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123;color:fc,backgroundColor:'blue'&#125;"</span>></span>vue修改行内样式,值是对象<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"sty"</span>></span>vue修改行内样式,值是对象名<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"[sty,sty1]"</span>></span>vue修改行内样式,值是数组<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>:<span class="hljs-string">'#box'</span>,
        <span class="hljs-attr">data</span>:&#123;
            <span class="hljs-attr">fc</span>:<span class="hljs-string">'red'</span>,
            <span class="hljs-attr">ac</span>:<span class="hljs-string">'blue'</span>,
            <span class="hljs-attr">sty</span>:&#123;<span class="hljs-attr">color</span>:<span class="hljs-string">'yellow'</span>,<span class="hljs-attr">backgroundColor</span>:<span class="hljs-string">'black'</span>&#125;,
            <span class="hljs-attr">sty1</span>:&#123;<span class="hljs-attr">fontSize</span>:<span class="hljs-string">'50px'</span>,<span class="hljs-attr">border</span>:<span class="hljs-string">'5px solid blue'</span>&#125;


        &#125;,
        
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">条件指令</h3>
<h4 data-id="heading-13">条件指令介绍</h4>
<p>条件指令 是用来控制元素的显示与隐藏的（条件为真显示，条件为假不显示），即用于条件性的渲染某一块内容</p>
<h4 data-id="heading-14">v-if & v-else-if & v-else</h4>
<p>可以出现多个v-else-if语句，但是v-else-if之前必须有一个v-if开头。后面可以跟着v-else，也可以没有。</p>
<p>v-else指令来表示 v-if 的“else 块”，v-else 元素必须紧跟在带 v-if 或者 v-else-if 的元素的后面，否则它将不会被识别。</p>
<pre><code class="hljs language-html copyable" lang="html">
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"num==0"</span>></span>&#123;&#123;num&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-else-if</span>=<span class="hljs-string">"num==1"</span>></span>one<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-else</span>></span>else<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>


    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
            <span class="hljs-attr">data</span>:&#123;
                <span class="hljs-attr">num</span>:<span class="hljs-number">1</span>
            &#125;
        &#125;)
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">v-show</h4>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">"num==1"</span>></span>v-show&#123;&#123;num&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">v-if与v-show的异同</h4>
<p>用法和v-if大致一样，区别在于2点：</p>
<ol>
<li>v-show后面不能有v-else或者v-else-if</li>
<li>v-show隐藏元素时，使用的是display:none来隐藏的，而v-if是直接从HTML文档中移除元素[ DOM操作中的remove ]</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html">  标签元素：
<span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">"ok"</span>></span>Hello!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
  data数据：
  data:&#123;
      ok:false    // true则是显示，false是隐藏
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">循环指令</h3>
<p>在vue中，可以通过v-for指令将一组数据渲染到页面中，数据可以是数组或者对象</p>
<ul>
<li>循环数组</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"goods"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">table</span> <span class="hljs-attr">border</span>=<span class="hljs-string">"3"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">tr</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">td</span>></span>序号<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">td</span>></span>id<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">td</span>></span>name<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">td</span>></span>price<span class="hljs-tag"></<span class="hljs-name">td</span>></span>

        <span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
<span class="hljs-comment"><!--第一个元素是数据，第二个元素是索引下标--></span>
        <span class="hljs-tag"><<span class="hljs-name">tr</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"goods,index in book_list"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">td</span>></span>&#123;&#123;index&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">td</span>></span>&#123;&#123;goods.id&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">td</span>></span>&#123;&#123;goods.title&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">td</span>></span>&#123;&#123;goods.price&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">td</span>></span>

        <span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">table</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>:<span class="hljs-string">'#goods'</span>,
        <span class="hljs-attr">data</span>:&#123;
            <span class="hljs-attr">book_list</span>:[
            &#123;<span class="hljs-string">"id"</span>:<span class="hljs-number">1</span>,<span class="hljs-string">"title"</span>:<span class="hljs-string">"图书名称1"</span>,<span class="hljs-string">"price"</span>:<span class="hljs-number">200</span>&#125;,
            &#123;<span class="hljs-string">"id"</span>:<span class="hljs-number">2</span>,<span class="hljs-string">"title"</span>:<span class="hljs-string">"图书名称2"</span>,<span class="hljs-string">"price"</span>:<span class="hljs-number">200</span>&#125;,
            &#123;<span class="hljs-string">"id"</span>:<span class="hljs-number">3</span>,<span class="hljs-string">"title"</span>:<span class="hljs-string">"图书名称3"</span>,<span class="hljs-string">"price"</span>:<span class="hljs-number">200</span>&#125;,
            &#123;<span class="hljs-string">"id"</span>:<span class="hljs-number">4</span>,<span class="hljs-string">"title"</span>:<span class="hljs-string">"图书名称4"</span>,<span class="hljs-string">"price"</span>:<span class="hljs-number">200</span>&#125;,
                    ]
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>循环对象</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html">
<span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
    <span class="hljs-comment"><!--第一个元素是值，第二个元素是键--></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"value, attr in book"</span>></span>&#123;&#123;attr&#125;&#125;:&#123;&#123;value&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>总结：循环取值时，不显示数组的索引或者键的方式是循环是只使用一个变量接收</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"book in book_list"</span>></span>&#123;&#123;book.title&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"value in book"</span>></span>&#123;&#123;value&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">事件绑定指令</h3>
<h4 data-id="heading-19">事件指令介绍</h4>













<table><thead><tr><th align="center">vue1.x版本</th><th align="center">vue2.x版本</th></tr></thead><tbody><tr><td align="center">v-on:事件名称</td><td align="center">@事件名称</td></tr></tbody></table>
<p>vue中的事件名称全部都是js的事件名</p>

























<table><thead><tr><th align="center">js中的事件</th><th align="center">vue中的事件名称</th></tr></thead><tbody><tr><td align="center">onsubmit</td><td align="center">@submit</td></tr><tr><td align="center">onfocus</td><td align="center">@focus</td></tr><tr><td align="center">onblur</td><td align="center">@blur</td></tr><tr><td align="center">onclick</td><td align="center">@click</td></tr></tbody></table>
<h4 data-id="heading-20">简单事件</h4>
<p>简单事件处理逻辑直接写在字符串中即可</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-comment"><!--实现输入框内数据加减操作--></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"num++"</span>></span>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"num"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"num--"</span>></span>-<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
        <span class="hljs-attr">data</span>:&#123;
            <span class="hljs-attr">num</span>:<span class="hljs-number">0</span>
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">复杂事件</h4>
<p>复杂事件的处理逻辑，单独写在一个函数放在vue对象的methods中通过函数命名调用执行</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"myalert"</span>></span>alert<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
        <span class="hljs-attr">data</span>:&#123;
            <span class="hljs-attr">num</span>:<span class="hljs-number">0</span>,
            <span class="hljs-attr">name</span>:<span class="hljs-string">'hello'</span>
        &#125;,
        <span class="hljs-attr">methods</span>:&#123;
            <span class="hljs-function"><span class="hljs-title">myalert</span>(<span class="hljs-params"></span>)</span>&#123;
                alert(<span class="hljs-built_in">this</span>.name + <span class="hljs-string">'!'</span>)
            &#125;
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">Vue对象属性功能</h2>
<h3 data-id="heading-23">过滤器</h3>
<p>自定义过滤器用于一些常见的文本格式化，过滤器可以用在两个地方：双花括号插值和绑定指令的后面</p>
<h4 data-id="heading-24">全局过滤器</h4>
<ul>
<li>语法格式</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html">Vue.filter('过滤器的名字','fucntion(args)&#123;return args.方法&#125;')
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>代码案例 --- 将vue对象data中的price属性保留两位小数输出到前端页面</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    &#123;&#123;price&#125;&#125;
    &#123;&#123;price|foo&#125;&#125;
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="handlebars"><span class="xml">
<span class="hljs-comment"><!--  toFixed()是js提供保留小数点的方法  --></span>
    Vue.filter('foo',function(price)&#123;return price.toFixed(2)&#125;);
    let vm = new Vue(&#123;
        el:'#app',
        data:&#123;
            price:2.31456
        &#125;
    &#125;)
</span></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>全局过滤器总结</li>
</ul>
<pre><code class="hljs language-markdown copyable" lang="markdown">  全局过滤器：语法格式Vue.filter('过滤器的名字'，'function(args)&#123;return args.方法&#125;&#125;')
  将data中某一个数据当作过滤器的参数，传给过滤器函数，然后返回过滤器处理后的结果
  处理后的结果可以通过模版语法输出，模版语法+过滤器的语法格式&#123;&#123;需要处理的数据|过滤器的函数名&#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">局部过滤器</h4>
<ul>
<li>语法格式</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html">filters:&#123;
函数名(args)&#123;return args.方法&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>代码案例</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    &#123;&#123;price&#125;&#125;
    &#123;&#123;price|format&#125;&#125;
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
        <span class="hljs-attr">data</span>:&#123;
            <span class="hljs-attr">price</span>:<span class="hljs-number">8.1536</span>
        &#125;,
        <span class="hljs-comment">// 局部过滤器</span>
        <span class="hljs-attr">filters</span>:&#123;
            <span class="hljs-function"><span class="hljs-title">format</span>(<span class="hljs-params">money</span>)</span>&#123;
                <span class="hljs-keyword">return</span> money.toFixed(<span class="hljs-number">2</span>)+<span class="hljs-string">'元'</span>
            &#125;
        &#125;,

    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>局部过滤器总结</li>
</ul>
<pre><code class="copyable">局部过滤器只对当前vue对象中的数据产生效果
局部过滤器是放在当前的vue对象中的filters属性中定义的函数
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">vue对象的计算属性</h3>
<p>计算属性：相当于创建一个新的变量保存数据计算的结果</p>
<pre><code class="hljs language-html copyable" lang="html">
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"num"</span>></span>+
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"num1"</span>></span>=
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123;mySum&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
        <span class="hljs-attr">data</span>:&#123;
            <span class="hljs-attr">num</span>:<span class="hljs-number">0</span>,
            <span class="hljs-attr">num1</span>:<span class="hljs-number">1</span>
        &#125;,
        <span class="hljs-attr">computed</span>:&#123;
            <span class="hljs-comment">// mySum接收计算结果</span>
            <span class="hljs-function"><span class="hljs-title">mySum</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-comment">// this指代vue对象</span>
                <span class="hljs-keyword">return</span> <span class="hljs-built_in">parseFloat</span>(<span class="hljs-built_in">this</span>.num)+<span class="hljs-built_in">parseFloat</span>(<span class="hljs-built_in">this</span>.num1)
            &#125;
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">vue对象的侦听属性</h3>
<p>侦听属性，可以帮助我们侦听data中某个数据的变化，从而做相应的自定义操作。</p>
<p>侦听属性是一个对象，它的键是要监听的对象或者变量，值一般是一个函数，当侦听的data数据发生变化时，会自动执行对应的函数，这个函数在被调用的时候，需要两个形参，第一个是变化前的数据值，第二个是变化后的数据值。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"num"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"num++"</span> ></span>+<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
        <span class="hljs-attr">data</span>:&#123;
            <span class="hljs-attr">num</span>:<span class="hljs-number">0</span>
        &#125;,
        <span class="hljs-attr">watch</span>:&#123;
            <span class="hljs-comment">// 可以简写为num(v1,v2)&#123;&#125;</span>
            <span class="hljs-attr">num</span>:<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">v1,v2</span>) </span>&#123;
                <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.num>=<span class="hljs-number">5</span>)&#123;<span class="hljs-built_in">this</span>.num=<span class="hljs-number">5</span>&#125;
                <span class="hljs-built_in">console</span>.log(v1,v2)
            &#125;
        &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-28">vue对象的生命周期</h2>
<p>每个 Vue 实例在被创建时都要经过一系列的初始化过程——例如，需要设置数据监听、编译模板、将实例挂载到 DOM 并在数据变化时更新 DOM 等。同时在这个过程中也会运行一些叫做<strong>生命周期钩子</strong>的函数，这给了用户在不同阶段添加自己的代码的机会</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Title<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"js/vue.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-built_in">window</span>.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
            <span class="hljs-attr">data</span>:&#123;
                <span class="hljs-attr">num</span>:<span class="hljs-number">0</span>
            &#125;,
            <span class="hljs-attr">beforeCreate</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"beforeCreate,vm对象尚未创建,num="</span>+ <span class="hljs-built_in">this</span>.num);  <span class="hljs-comment">//undefined</span>
                <span class="hljs-built_in">this</span>.name=<span class="hljs-number">10</span>; <span class="hljs-comment">// 此时没有this对象呢，所以设置的name无效，被在创建对象的时候被覆盖为0</span>
            &#125;,
            <span class="hljs-attr">created</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"created,vm对象创建完成,设置好了要控制的元素范围,num="</span>+<span class="hljs-built_in">this</span>.num );  <span class="hljs-comment">// 0</span>
                <span class="hljs-built_in">this</span>.num = <span class="hljs-number">20</span>;
            &#125;,
            <span class="hljs-attr">beforeMount</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-built_in">console</span>.log( <span class="hljs-built_in">this</span>.$el.innerHTML ); <span class="hljs-comment">// <p>&#123;&#123;num&#125;&#125;</p></span>
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"beforeMount,vm对象尚未把data数据显示到页面中,num="</span>+<span class="hljs-built_in">this</span>.num ); <span class="hljs-comment">// 20</span>
                <span class="hljs-built_in">this</span>.num = <span class="hljs-number">30</span>;
            &#125;,
            <span class="hljs-attr">mounted</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-built_in">console</span>.log( <span class="hljs-built_in">this</span>.$el.innerHTML ); <span class="hljs-comment">// <p>30</p></span>
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"mounted,vm对象已经把data数据显示到页面中,num="</span>+<span class="hljs-built_in">this</span>.num); <span class="hljs-comment">// 30</span>
            &#125;,
            <span class="hljs-attr">beforeUpdate</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-comment">// this.$el 就是我们上面的el属性了，$el表示当前vue.js所控制的元素#app</span>
                <span class="hljs-built_in">console</span>.log( <span class="hljs-built_in">this</span>.$el.innerHTML );  <span class="hljs-comment">// <p>30</p></span>
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"beforeUpdate,vm对象尚未把更新后的data数据显示到页面中,num="</span>+<span class="hljs-built_in">this</span>.num); <span class="hljs-comment">// beforeUpdate----31</span>
                
            &#125;,
            <span class="hljs-attr">updated</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-built_in">console</span>.log( <span class="hljs-built_in">this</span>.$el.innerHTML ); <span class="hljs-comment">// <p>31</p></span>
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"updated,vm对象已经把过呢更新后的data数据显示到页面中,num="</span> + <span class="hljs-built_in">this</span>.num ); <span class="hljs-comment">// updated----31</span>
            &#125;,
        &#125;);
    &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123;num&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"num++"</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>总结</li>
</ul>
<pre><code class="copyable">在vue使用的过程中，如果要初始化操作，把初始化操作的代码放在 mounted 中执行。
mounted阶段就是修改页面的数据，在vm对象已经把data数据实现到页面以后。一般页面初始化使用。例如，用户访问页面加载成功以后，就要执行的ajax请求。

另一个就是created，这个阶段就是在 vue对象创建以后，把ajax请求后端数据的代码放进 created

在页面加载完成之前，对后台发起http请求获取数据，代码写在created中
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-29">阻止事件冒泡和刷新页面</h2>
<p>事件冒泡：指代js中子元素的事件触发以后，会导致父级元素的同类事件一并被触发到。</p>
<p>事件冒泡有好处，也有坏处。</p>
<p>好处：如果能正确利用这种现象，可以实现事件委托，提升特效的性能</p>
<p>坏处：如果没有正确使用，则会导致不必要的bug出现。</p>
<ul>
<li>@click.stop来阻止事件冒泡</li>
<li>@click.prevent来阻止表单提交</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Title<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-class">.box1</span>&#123;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
            <span class="hljs-attribute">background</span>: <span class="hljs-number">#ccc</span>;
        &#125;
        <span class="hljs-selector-class">.box2</span>&#123;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
            <span class="hljs-attribute">background</span>: pink;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-built_in">window</span>.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
            <span class="hljs-attr">data</span>:&#123;&#125;
        &#125;)
    &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box1"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"alert('box1')"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box2"</span> @<span class="hljs-attr">click.stop.prevent</span>=<span class="hljs-string">"alert('box2')"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>   <span class="hljs-comment"><!-- @click.stop来阻止事件冒泡 --></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

        <span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">action</span>=<span class="hljs-string">"#"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"submit"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"submit"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"提交02"</span> @<span class="hljs-attr">click.prevent</span>=<span class="hljs-string">""</span>></span> <span class="hljs-comment"><!-- @click.prevent来阻止表单提交 --></span>
        <span class="hljs-tag"></<span class="hljs-name">form</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-30">综合案例 --- TODOLIST</h2>
<ul>
<li>源html代码</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>todolist<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
<span class="hljs-selector-class">.list_con</span>&#123;
<span class="hljs-attribute">width</span>:<span class="hljs-number">600px</span>;
<span class="hljs-attribute">margin</span>:<span class="hljs-number">50px</span> auto <span class="hljs-number">0</span>;
&#125;
<span class="hljs-selector-class">.inputtxt</span>&#123;
<span class="hljs-attribute">width</span>:<span class="hljs-number">550px</span>;
<span class="hljs-attribute">height</span>:<span class="hljs-number">30px</span>;
<span class="hljs-attribute">border</span>:<span class="hljs-number">1px</span> solid <span class="hljs-number">#ccc</span>;
<span class="hljs-attribute">padding</span>:<span class="hljs-number">0px</span>;
<span class="hljs-attribute">text-indent</span>:<span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.inputbtn</span>&#123;
<span class="hljs-attribute">width</span>:<span class="hljs-number">40px</span>;
<span class="hljs-attribute">height</span>:<span class="hljs-number">32px</span>;
<span class="hljs-attribute">padding</span>:<span class="hljs-number">0px</span>;
<span class="hljs-attribute">border</span>:<span class="hljs-number">1px</span> solid <span class="hljs-number">#ccc</span>;
&#125;
<span class="hljs-selector-class">.list</span>&#123;
<span class="hljs-attribute">margin</span>:<span class="hljs-number">0</span>;
<span class="hljs-attribute">padding</span>:<span class="hljs-number">0</span>;
<span class="hljs-attribute">list-style</span>:none;
<span class="hljs-attribute">margin-top</span>:<span class="hljs-number">20px</span>;
&#125;
<span class="hljs-selector-class">.list</span> <span class="hljs-selector-tag">li</span>&#123;
<span class="hljs-attribute">height</span>:<span class="hljs-number">40px</span>;
<span class="hljs-attribute">line-height</span>:<span class="hljs-number">40px</span>;
<span class="hljs-attribute">border-bottom</span>:<span class="hljs-number">1px</span> solid <span class="hljs-number">#ccc</span>;
&#125;

<span class="hljs-selector-class">.list</span> <span class="hljs-selector-tag">li</span> <span class="hljs-selector-tag">span</span>&#123;
<span class="hljs-attribute">float</span><span class="hljs-selector-pseudo">:left</span>;
&#125;

<span class="hljs-selector-class">.list</span> <span class="hljs-selector-tag">li</span> <span class="hljs-selector-tag">a</span>&#123;
<span class="hljs-attribute">float</span><span class="hljs-selector-pseudo">:right</span>;
<span class="hljs-attribute">text-decoration</span>:none;
<span class="hljs-attribute">margin</span>:<span class="hljs-number">0</span> <span class="hljs-number">10px</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list_con"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">h2</span>></span>To do list<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">""</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"txt1"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"inputtxt"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">""</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"增加"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btn1"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"inputbtn"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"list"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list"</span>></span>
<span class="hljs-comment"><!-- javascript:; # 阻止a标签跳转 --></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">span</span>></span>学习html<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"javascript:;"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"up"</span>></span> ↑ <span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"javascript:;"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"down"</span>></span> ↓ <span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"javascript:;"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"del"</span>></span>删除<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span>学习css<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"javascript:;"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"up"</span>></span> ↑ <span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"javascript:;"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"down"</span>></span> ↓ <span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"javascript:;"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"del"</span>></span>删除<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span>学习javascript<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"javascript:;"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"up"</span>></span> ↑ <span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"javascript:;"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"down"</span>></span> ↓ <span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"javascript:;"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"del"</span>></span>删除<span class="hljs-tag"></<span class="hljs-name">a</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>实现效果代码</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">title</span>></span>todolist<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
      <span class="hljs-selector-class">.list_con</span>&#123;
         <span class="hljs-attribute">width</span>:<span class="hljs-number">600px</span>;
         <span class="hljs-attribute">margin</span>:<span class="hljs-number">50px</span> auto <span class="hljs-number">0</span>;
      &#125;
      <span class="hljs-selector-class">.inputtxt</span>&#123;
         <span class="hljs-attribute">width</span>:<span class="hljs-number">550px</span>;
         <span class="hljs-attribute">height</span>:<span class="hljs-number">30px</span>;
         <span class="hljs-attribute">border</span>:<span class="hljs-number">1px</span> solid <span class="hljs-number">#ccc</span>;
         <span class="hljs-attribute">padding</span>:<span class="hljs-number">0px</span>;
         <span class="hljs-attribute">text-indent</span>:<span class="hljs-number">10px</span>;
      &#125;
      <span class="hljs-selector-class">.inputbtn</span>&#123;
         <span class="hljs-attribute">width</span>:<span class="hljs-number">40px</span>;
         <span class="hljs-attribute">height</span>:<span class="hljs-number">32px</span>;
         <span class="hljs-attribute">padding</span>:<span class="hljs-number">0px</span>;
         <span class="hljs-attribute">border</span>:<span class="hljs-number">1px</span> solid <span class="hljs-number">#ccc</span>;
      &#125;
      <span class="hljs-selector-class">.list</span>&#123;
         <span class="hljs-attribute">margin</span>:<span class="hljs-number">0</span>;
         <span class="hljs-attribute">padding</span>:<span class="hljs-number">0</span>;
         <span class="hljs-attribute">list-style</span>:none;
         <span class="hljs-attribute">margin-top</span>:<span class="hljs-number">20px</span>;
      &#125;
      <span class="hljs-selector-class">.list</span> <span class="hljs-selector-tag">li</span>&#123;
         <span class="hljs-attribute">height</span>:<span class="hljs-number">40px</span>;
         <span class="hljs-attribute">line-height</span>:<span class="hljs-number">40px</span>;
         <span class="hljs-attribute">border-bottom</span>:<span class="hljs-number">1px</span> solid <span class="hljs-number">#ccc</span>;
      &#125;

      <span class="hljs-selector-class">.list</span> <span class="hljs-selector-tag">li</span> <span class="hljs-selector-tag">span</span>&#123;
         <span class="hljs-attribute">float</span><span class="hljs-selector-pseudo">:left</span>;
      &#125;

      <span class="hljs-selector-class">.list</span> <span class="hljs-selector-tag">li</span> <span class="hljs-selector-tag">a</span>&#123;
         <span class="hljs-attribute">float</span><span class="hljs-selector-pseudo">:right</span>;
         <span class="hljs-attribute">text-decoration</span>:none;
         <span class="hljs-attribute">margin</span>:<span class="hljs-number">0</span> <span class="hljs-number">10px</span>;
      &#125;
   </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list_con"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>To do list<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"content"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"txt1"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"inputtxt"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"add"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"增加"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btn1"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"inputbtn"</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"list"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"list"</span>></span>
         <span class="hljs-comment"><!-- javascript:; # 阻止a标签跳转 --></span>
         <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item,index in todolist"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123;item&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"javascript:;"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"up"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"up(index)"</span>></span> ↑ <span class="hljs-tag"></<span class="hljs-name">a</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"javascript:;"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"down"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"down(index)"</span>></span> ↓ <span class="hljs-tag"></<span class="hljs-name">a</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"javascript:;"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"del"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"del(index)"</span>></span>删除<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
         <span class="hljs-tag"></<span class="hljs-name">li</span>></span>

      <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
   <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-keyword">let</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">el</span>:<span class="hljs-string">'#app'</span>,
            <span class="hljs-attr">data</span>:&#123;
                <span class="hljs-attr">content</span>:<span class="hljs-string">''</span>,
                <span class="hljs-attr">todolist</span>:[<span class="hljs-string">'学习html'</span>,<span class="hljs-string">'学习css'</span>,<span class="hljs-string">'学习javascript'</span>,<span class="hljs-string">'学习c'</span>],
            &#125;,
            <span class="hljs-attr">methods</span>:&#123;
                <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span>&#123;
                    <span class="hljs-comment">// js中追加一个数组成员使用push,添加</span>
                    <span class="hljs-built_in">this</span>.todolist.push(<span class="hljs-built_in">this</span>.content);
                    <span class="hljs-comment">// 添加之后将输入框中的信息清空</span>
                    <span class="hljs-built_in">this</span>.content=<span class="hljs-string">''</span>
                &#125;,
                <span class="hljs-function"><span class="hljs-title">del</span>(<span class="hljs-params">index</span>)</span>&#123;
                    <span class="hljs-comment">// js中splice高阶函数可以指定从指定下标的位置删除成员的个数，在指定位置替换成员</span>
                    <span class="hljs-comment">// splice(删除开始的下标,删除成员的数量,替代被删除的元素)</span>
                    <span class="hljs-built_in">this</span>.todolist.splice(index,<span class="hljs-number">1</span>);
                &#125;,
                <span class="hljs-function"><span class="hljs-title">up</span>(<span class="hljs-params">index</span>)</span>&#123;
                    <span class="hljs-comment">// 上移</span>
                    <span class="hljs-comment">// 首先删除移动的元素保存到内存中，再将删除的元素插入到数组的指定位置，即下标减一，splice会返回一个内容 --- 被操作的数据对象</span>
                    <span class="hljs-keyword">let</span> currentItem = <span class="hljs-built_in">this</span>.todolist.splice(index,<span class="hljs-number">1</span>)[<span class="hljs-number">0</span>];
                    <span class="hljs-built_in">this</span>.todolist.splice(index-<span class="hljs-number">1</span>,<span class="hljs-number">0</span>,currentItem)
                &#125;,
                <span class="hljs-function"><span class="hljs-title">down</span>(<span class="hljs-params">index</span>)</span>&#123;
                    <span class="hljs-comment">// 下移</span>
                    <span class="hljs-comment">// 原理和上移是类似的</span>
                    <span class="hljs-keyword">let</span> currentItem = <span class="hljs-built_in">this</span>.todolist.splice(index,<span class="hljs-number">1</span>)[<span class="hljs-number">0</span>];
                    <span class="hljs-built_in">this</span>.todolist.splice(index+<span class="hljs-number">1</span>,<span class="hljs-number">0</span>,currentItem)
                &#125;
            &#125;
        &#125;)
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-31">结语</h2>
<blockquote>
<p>文章首发于微信公众号<strong>程序媛小庄</strong>，同步于<a href="https://juejin.cn/user/298666235012894/activities" target="_blank" title="https://juejin.cn/user/298666235012894/activities">掘金</a>。</p>
<p>码字不易，转载请说明出处，走过路过的小伙伴们伸出可爱的小指头点个赞再走吧(<em>╹▽╹</em>)</p>
</blockquote></div>  
</div>
            