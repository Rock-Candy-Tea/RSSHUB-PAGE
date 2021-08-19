
---
title: 'vue源码解析之调度原理(响应式原理)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7415'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 23:41:55 GMT
thumbnail: 'https://picsum.photos/400/300?random=7415'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">vue源码解析之调度原理(响应式原理)</h1>
<p>可先看我的前篇会更好理解：<a href="https://juejin.cn/post/6997670497723023390" target="_blank" title="https://juejin.cn/post/6997670497723023390">vue源码解析之编译过程-含2种模式(及vue-loader作用)</a></p>
<p>目录大纲</p>
<ol>
<li>测试文件：<strong>.html文件</strong></li>
<li>测试动作：点击“click me”，触发 qqq函数</li>
<li>调度过程总结</li>
<li>再谈一下vue的双向绑定v-model原理</li>
</ol>
<h2 data-id="heading-1">测试文件：<strong>.html文件</strong></h2>
<ul>
<li>CDN引入vue的未压缩版，在script标签内，直接使用vue
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Title<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  &#123;&#123;aa&#125;&#125; --- 1
  <span class="hljs-tag"><<span class="hljs-name">div</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"qqq"</span>></span>click me<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  &#123;&#123;C_aa&#125;&#125;
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"module"</span>></span><span class="javascript">
  <span class="hljs-keyword">debugger</span>
  <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">aa</span>: <span class="hljs-number">123</span>
    &#125;,
    <span class="hljs-attr">watch</span>: &#123;
      aa (nval, oval) &#123;
        <span class="hljs-built_in">console</span>.log(nval, oval)
      &#125;
    &#125;,
    <span class="hljs-attr">computed</span>: &#123;
      C_aa () &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.aa + <span class="hljs-number">100</span>
      &#125;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      qqq () &#123;
        <span class="hljs-keyword">debugger</span>
        <span class="hljs-built_in">this</span>.aa = <span class="hljs-built_in">this</span>.aa + <span class="hljs-number">1</span>
      &#125;
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-2">测试动作：点击“click me”，触发 qqq函数</h2>
<p>（说明：只截取了主线代码，并略有删减，为的是 更好的关注主线，主线弄明白了，有余力，在去了解支线。 调试方式：debugger一步步往下）</p>
<p>断点在qqq函数内，调试从断点开始，看看 <code>this.aa = this.aa + 1</code> vue底层到底干了哪些事儿，才能把最新的数据 更新到页面上去？</p>
<p>有几个问题点，可以提前思考一下：</p>
<ol>
<li>如果用户一次同步操作，改变了多个data的值，vue是触发一次update，还是多次update?</li>
<li>用户写的watch: &#123;..&#125; 内的回调函数，是在update前执行，还是update之后？
<ol>
<li>watch: &#123;..&#125; 内的回调函数 如果又修改了data，那么还会触发update吗？</li>
</ol>
</li>
</ol>
<h3 data-id="heading-3">开始调试，执行 <code>this.aa = this.aa + 1</code></h3>
<ol>
<li>
<p>第一步，拿到this.aa的值。因为是要取值，所以会<strong>触发aa的get监听函数</strong></p>
<ul>
<li>
<p>在vue中，会对data的做监听（深层对象的话会递归监听，数组会遍历监听），主要是通过<strong>Object.defineProperty</strong>监听 可以设置get和set的监听函数，取this.aa的值 会触发get函数，设置this.aa=xx 会触发set函数</p>
</li>
<li>
<p>以下get的执行步骤，请看注释 （以下dep部分用到了<strong>发布订阅模式</strong>）</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">/**
   * A dep is an observable that can have multiple
   * directives subscribing to it.
   */</span>
  <span class="hljs-keyword">var</span> Dep = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Dep</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.id = uid++;
    <span class="hljs-built_in">this</span>.subs = []; <span class="hljs-comment">// 订阅者队列 subscriber</span>
  &#125;;
  <span class="hljs-comment">/**
   * Define a reactive property on an Object.
   */</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineReactive$$1</span> (<span class="hljs-params">
    obj,
    key,
    val,
    customSetter,
    shallow
  </span>) </span>&#123;
    <span class="hljs-keyword">var</span> dep = <span class="hljs-keyword">new</span> Dep(); <span class="hljs-comment">// 为每个data，绑定一个dep对象（Dep构造函数结构如上）</span>

    <span class="hljs-keyword">var</span> property = <span class="hljs-built_in">Object</span>.getOwnPropertyDescriptor(obj, key);
    <span class="hljs-keyword">if</span> (property && property.configurable === <span class="hljs-literal">false</span>) &#123;
      <span class="hljs-keyword">return</span>
    &#125;

    <span class="hljs-comment">// cater for pre-defined getter/setters</span>
    <span class="hljs-keyword">var</span> getter = property && property.get;
    <span class="hljs-keyword">var</span> setter = property && property.set;
    <span class="hljs-keyword">if</span> ((!getter || setter) && <span class="hljs-built_in">arguments</span>.length === <span class="hljs-number">2</span>) &#123;
      val = obj[key];
    &#125;

    <span class="hljs-keyword">var</span> childOb = !shallow && observe(val);
    <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123;
      <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactiveGetter</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">var</span> value = getter ? getter.call(obj) : val; <span class="hljs-comment">// data存在getter先执行getter</span>
        <span class="hljs-comment">/* 为data收集依赖
         （在vue中，每一个data都会绑定一个对象叫dep，会分配唯一的id。
           如果有依赖内容 会放到data对应的dep内的this.subs的订阅者队列里面），
         依赖内容是：比如：aa有3个依赖 1个watch、1个computed、1个页面渲染的必备的函数"function () &#123; vm._update(vm._render(), hydrating); &#125;" */</span>
        <span class="hljs-keyword">if</span> (Dep.target) &#123; 
          dep.depend(); <span class="hljs-comment">// 为data收集依赖</span>
          <span class="hljs-keyword">if</span> (childOb) &#123; <span class="hljs-comment">// 递归处理child</span>
            childOb.dep.depend();
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(value)) &#123;
              dependArray(value);
            &#125;
          &#125;
        &#125;
        <span class="hljs-keyword">return</span> value <span class="hljs-comment">// 拿到值</span>
      &#125;,
      <span class="hljs-attr">set</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactiveSetter</span> (<span class="hljs-params">newVal</span>) </span>&#123;
        <span class="hljs-keyword">var</span> value = getter ? getter.call(obj) : val; <span class="hljs-comment">// data存在getter先执行getter</span>
        <span class="hljs-comment">// 新旧值一样 没被修改，直接return停止</span>
        <span class="hljs-keyword">if</span> (newVal === value || (newVal !== newVal && value !== value)) &#123;
          <span class="hljs-keyword">return</span>
        &#125;
        <span class="hljs-comment">// #7981: for accessor properties without setter</span>
        <span class="hljs-keyword">if</span> (getter && !setter) &#123; <span class="hljs-keyword">return</span> &#125;
        <span class="hljs-keyword">if</span> (setter) &#123; <span class="hljs-comment">// 只在vue初始化的时候执行</span>
          setter.call(obj, newVal);
        &#125; <span class="hljs-keyword">else</span> &#123;
          val = newVal; <span class="hljs-comment">// 保存一份新值</span>
        &#125;
        childOb = !shallow && observe(newVal); <span class="hljs-comment">// 递归处理child</span>
        <span class="hljs-comment">/* 消息推送，通知订阅者队列 this.subs。实际上会把订阅者队列在处理一遍，
           放在全局queue队列里面去，最终真正执行的是queue队列，
           会过滤掉computed 因为不是异步的，结果是函数的返回值。在model层取值渲染的时候，会去跑函数，得到返回值
         （目前 aa 的订阅者队列this.subs内有：1个watch、1个computed、1个页面渲染的必备的函数"function () &#123; vm._update(vm._render(), hydrating); &#125;"） */</span>
        dep.notify(); 
      &#125;
    &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>第二步，修改this.aa的值。会<strong>触发set监听函数</strong></p>
<p>（代码在上面，详细请看注释）  执行set监听函数 最终会触发 消息推送 <code>dep.notify()</code></p>
</li>
<li>
<p><code>dep.notify()</code> 调度的开始</p>
<p>消息推送，通知订阅者队列 this.subs。实际上会把订阅者队列在处理一遍，放在全局queue队列里面去，最终真正执行的是queue队列（目前 aa 的订阅者队列this.subs内有：1个watch、1个computed、1个页面渲染的必备的函数"function () &#123; vm._update(vm._render(), hydrating); &#125;"）（会过滤掉computed 因为不是异步的，结果是函数的返回值。在model层取值渲染的时候，会去跑computed对应的函数得到返回值）</p>
<ol start="0">
<li>
<p>细节0：页面渲染的必备的函数"function () &#123; vm._update(vm._render(), hydrating); &#125;"）是什么作用，可以先看我的前篇：<a href="https://juejin.cn/post/6997670497723023390" target="_blank" title="https://juejin.cn/post/6997670497723023390">vue源码解析之编译过程-含2种模式(及vue-loader作用)</a></p>
</li>
<li>
<p>细节1：用户写的computed不是异步的，结果是函数的返回值。在model层取值渲染的时候，会去跑computed对应的函数得到返回值值（以下代码暂时没有体现）</p>
<ul>
<li>调度流程只会把this.dirty = true。 把对应的computed改成dirty（脏的）意味着，需要更新。</li>
</ul>
</li>
<li>
<p>细节2：异步事件（比如用户写的watch）都会放到一个全局的queue队列去，队列的最后一个是关键渲染函数vm._update(vm._render())。</p>
</li>
<li>
<p>细节3：什么时候去执行queue队列？</p>
<ul>
<li>在nextTick后去执行，nextTick(flushSchedulerQueue)
<ul>
<li>nextTick原理是一个微任务，等同步任务执行完，在执行 flushSchedulerQueue，最终去run queue队列。</li>
<li>好处：<strong>用户的一次操作，可能会改动多次或多个data的值，不用每改动一次就去更新页面，可以把一次同步任务内的所有改动，都收集起来，放到queue队列内，然后同步任务结束后 执行微任务nextTick内的回调函数， 去执行run queue队列。</strong></li>
</ul>
</li>
</ul>
</li>
<li>
<p>细节4： watch: &#123;..&#125; 内的回调函数 如果又修改了data，那么还会触发update吗？</p>
<ul>
<li>不会有多次vm._update(vm._render())</li>
<li>会用全局变量flushing控制，确保一次同步任务，只会有一次update</li>
</ul>
</li>
</ol>
<p>调度过程：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* 部分非主线代码有删减，为的是 更好的关注主线，主线弄明白了，有余力，在去了解支线 */</span> 

Dep.prototype.notify = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">notify</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> subs = <span class="hljs-built_in">this</span>.subs.slice();
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>, l = subs.length; i < l; i++) &#123;
        subs[i].update();
    &#125;
&#125;;
<span class="hljs-comment">/**
* Subscriber interface. Will be called when a dependency changes.
*/</span>
Watcher.prototype.update = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">update</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">/* istanbul ignore else */</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.lazy) &#123; <span class="hljs-comment">// 用户写的computed会进入这里，不是异步的，结果是函数的返回值。在model层取值渲染的时候，会去跑函数，得到返回值</span>
        <span class="hljs-built_in">this</span>.dirty = <span class="hljs-literal">true</span>; <span class="hljs-comment">// 把对应的computed改成dirty（脏的）意味着，需要更新</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.sync) &#123; <span class="hljs-comment">// 一次同步任务。 比如this.aa=xx触发aa的watch回调函数，回调函数内又非异步的修改了this.bb=xxx，此时是一次同步任务，就会走里面</span>
        <span class="hljs-built_in">this</span>.run();
    &#125; <span class="hljs-keyword">else</span> &#123;
        queueWatcher(<span class="hljs-built_in">this</span>); <span class="hljs-comment">// 用户写的 watch: &#123; aa () &#123;&#125; &#125; 往这里面走</span>
    &#125;
&#125;;

<span class="hljs-comment">/**
* Push a watcher into the watcher queue.  将watcher推入watcher队列。
* Jobs with duplicate IDs will be skipped unless it's pushed when the queue is being flushed.   除非在刷新队列时推送，否则将跳过具有重复 ID 的事件。
*/</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">queueWatcher</span> (<span class="hljs-params">watcher</span>) </span>&#123;
    <span class="hljs-keyword">var</span> id = watcher.id;
    <span class="hljs-keyword">if</span> (has[id] == <span class="hljs-literal">null</span>) &#123;
      has[id] = <span class="hljs-literal">true</span>;
      <span class="hljs-keyword">if</span> (!flushing) &#123; <span class="hljs-comment">// 全局变量flushing，确保一次同步任务，不会有多次vm._update(vm._render())，只会有一次update</span>
        queue.push(watcher); <span class="hljs-comment">// 把watcher加入queue队列</span>
      &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 避免重复的</span>
        <span class="hljs-comment">// if already flushing, splice the watcher based on its id</span>
        <span class="hljs-comment">// if already past its id, it will be run next immediately.</span>
        <span class="hljs-keyword">var</span> i = queue.length - <span class="hljs-number">1</span>;
        <span class="hljs-keyword">while</span> (i > index && queue[i].id > watcher.id) &#123;
          i--;
        &#125;
        queue.splice(i + <span class="hljs-number">1</span>, <span class="hljs-number">0</span>, watcher);
      &#125;
      <span class="hljs-comment">// queue the flush</span>
      <span class="hljs-keyword">if</span> (!waiting) &#123;
        waiting = <span class="hljs-literal">true</span>;
        <span class="hljs-comment">// nextTick原理是一个微任务，等同步任务执行完 把所有的watcher加入queue，在执行 flushSchedulerQueue，最终去run queue队列。</span>
        nextTick(flushSchedulerQueue); <span class="hljs-comment">// 用户写的 watch: &#123; aa () &#123;&#125; &#125; 往这里面走。 是异步的 </span>
      &#125;
    &#125;
&#125;

<span class="hljs-comment">/**
* Flush both queues and run the watchers.
*/</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flushSchedulerQueue</span> (<span class="hljs-params"></span>) </span>&#123;
    flushing = <span class="hljs-literal">true</span>;
    <span class="hljs-keyword">var</span> watcher, id;
    <span class="hljs-comment">// queue 是一个全局的 watcher list，存放了当次同步任务内的所有用户watcher</span>
    <span class="hljs-comment">// 此处我们的watcher有2个， 一个是watch: &#123; aa () &#123;&#125; &#125;，另一个 关键渲染函数 "function () &#123; vm._update(vm._render(), hydrating); &#125;"</span>
    <span class="hljs-keyword">for</span> (index = <span class="hljs-number">0</span>; index < queue.length; index++) &#123;
      watcher = queue[index];
      <span class="hljs-keyword">if</span> (watcher.before) &#123;
        watcher.before(); <span class="hljs-comment">// 执行vm._update(vm._render(), hydrating) 之前，beforeUpdate 在这里先执行 callHook(vm, 'beforeUpdate'); </span>
      &#125;
      id = watcher.id;
      has[id] = <span class="hljs-literal">null</span>;
      watcher.run(); <span class="hljs-comment">// watcher都在这执行，比如 1.开发者写的 watch: &#123; aa () &#123;&#125; &#125; 监听函数，在此行执行。 2. 页面渲染的必备的函数"function () &#123; vm._update(vm._render(), hydrating); &#125;"）</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>watcher.run();</p>
<ul>
<li>watcher都在这执行，比如
<ul>
<li>1.开发者写的 watch: &#123; aa () &#123;&#125; &#125; 监听函数，在此行执行。</li>
<li>2.页面渲染的必备的函数"function () &#123; vm._update(vm._render(), hydrating); &#125;"）
<ul>
<li>会在确保在一次同步任务中的最后执行，因为要避免多次update</li>
</ul>
</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
* Scheduler job interface. Will be called by the scheduler.
*/</span>
Watcher.prototype.run = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">run</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.active) &#123;
      <span class="hljs-comment">/* 这一行很重要，有2个作用
          1. 正常取data的值，比如在watch: &#123;aa(newVal, oldVal) &#123;&#125;&#125;中，newVal的值，就是从 this.get() 里拿到的
          2. 页面渲染的必备的函数"function () &#123; vm._update(vm._render(), hydrating); &#125;"） 就是在此处执行。*/</span>
      <span class="hljs-keyword">var</span> value = <span class="hljs-built_in">this</span>.get(); 
      <span class="hljs-keyword">if</span> (
        value !== <span class="hljs-built_in">this</span>.value ||
        <span class="hljs-comment">// Deep watchers and watchers on Object/Arrays should fire even</span>
        <span class="hljs-comment">// when the value is the same, because the value may</span>
        <span class="hljs-comment">// have mutated.</span>
        isObject(value) ||
        <span class="hljs-built_in">this</span>.deep
      ) &#123;
        <span class="hljs-comment">// set new value</span>
        <span class="hljs-keyword">var</span> oldValue = <span class="hljs-built_in">this</span>.value;
        <span class="hljs-built_in">this</span>.value = value;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.user) &#123;
          <span class="hljs-keyword">var</span> info = <span class="hljs-string">"callback for watcher \""</span> + (<span class="hljs-built_in">this</span>.expression) + <span class="hljs-string">"\""</span>;
          <span class="hljs-comment">// 开发者写的 watch: &#123; aa () &#123;&#125; &#125; 监听函数，在此行执行</span>
          invokeWithErrorHandling(<span class="hljs-built_in">this</span>.cb, <span class="hljs-built_in">this</span>.vm, [value, oldValue], <span class="hljs-built_in">this</span>.vm, info); 
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">this</span>.cb.call(<span class="hljs-built_in">this</span>.vm, value, oldValue);
        &#125;
      &#125;
    &#125;
&#125;;
<span class="hljs-comment">/**
* Evaluate the getter, and re-collect dependencies.
*/</span>
Watcher.prototype.get = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">get</span> (<span class="hljs-params"></span>) </span>&#123;
    pushTarget(<span class="hljs-built_in">this</span>);
    <span class="hljs-keyword">var</span> value;
    <span class="hljs-keyword">var</span> vm = <span class="hljs-built_in">this</span>.vm;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-comment">// 页面渲染的必备的函数"function () &#123; vm._update(vm._render(), hydrating); &#125;"） 就是在此处执行。 this.getter 保存了 vm._update(vm._render(), hydrating）</span>
      value = <span class="hljs-built_in">this</span>.getter.call(vm, vm);
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.user) &#123;
        handleError(e, vm, (<span class="hljs-string">"getter for watcher \""</span> + (<span class="hljs-built_in">this</span>.expression) + <span class="hljs-string">"\""</span>));
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">throw</span> e
      &#125;
    &#125; <span class="hljs-keyword">finally</span> &#123;
      <span class="hljs-comment">// "touch" every property so they are all tracked as</span>
      <span class="hljs-comment">// dependencies for deep watching</span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.deep) &#123;
        traverse(value);
      &#125;
      popTarget();
      <span class="hljs-built_in">this</span>.cleanupDeps();
    &#125;
    <span class="hljs-keyword">return</span> value
&#125;;
<span class="hljs-comment">// 开发者写的 watch: &#123; aa () &#123;&#125; &#125; 监听函数，在此行执行</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">invokeWithErrorHandling</span> (<span class="hljs-params">
    handler,
    context,
    args,
    vm,
    info
</span>) </span>&#123;
    <span class="hljs-keyword">var</span> res;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-comment">// 开发者写的 watch: &#123; aa () &#123;&#125; &#125; 监听函数，在此行执行</span>
      res = args ? handler.apply(context, args) : handler.call(context);
      <span class="hljs-keyword">if</span> (res && !res._isVue && isPromise(res) && !res._handled) &#123;
        res.catch(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123; <span class="hljs-keyword">return</span> handleError(e, vm, info + <span class="hljs-string">" (Promise/async)"</span>); &#125;);
        <span class="hljs-comment">// avoid catch triggering multiple times when nested calls</span>
        res._handled = <span class="hljs-literal">true</span>;
      &#125;
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      handleError(e, vm, info);
    &#125;
    <span class="hljs-keyword">return</span> res
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>nextTick()</p>
<ul>
<li>nextTick原理是一个微任务，用了nextTick的 函数存放在全局callbacks里面</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">nextTick</span> (<span class="hljs-params">cb, ctx</span>) </span>&#123;
    <span class="hljs-keyword">var</span> _resolve;
    callbacks.push(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-comment">// callbacks是全局的，存放 用了nextTick的 函数</span>
      <span class="hljs-keyword">if</span> (cb) &#123;
        <span class="hljs-keyword">try</span> &#123;
          cb.call(ctx);
        &#125; <span class="hljs-keyword">catch</span> (e) &#123;
          handleError(e, ctx, <span class="hljs-string">'nextTick'</span>);
        &#125;
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (_resolve) &#123;
        _resolve(ctx);
      &#125;
    &#125;);
    <span class="hljs-keyword">if</span> (!pending) &#123;
      pending = <span class="hljs-literal">true</span>;
      timerFunc(); <span class="hljs-comment">// nextTick原理是一个微任务，用了nextTick的 函数存放在callbacks里面</span>
    &#125;
    <span class="hljs-keyword">if</span> (!cb && <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Promise</span> !== <span class="hljs-string">'undefined'</span>) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve</span>) </span>&#123;
        _resolve = resolve;
      &#125;)
    &#125;
&#125;

<span class="hljs-keyword">var</span> p = <span class="hljs-built_in">Promise</span>.resolve(); <span class="hljs-comment">// 微任务</span>
timerFunc = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; <span class="hljs-comment">// 微任务</span>
  p.then(flushCallbacks);
  <span class="hljs-keyword">if</span> (isIOS) &#123; <span class="hljs-built_in">setTimeout</span>(noop); &#125;
&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flushCallbacks</span> (<span class="hljs-params"></span>) </span>&#123;
    pending = <span class="hljs-literal">false</span>;
    <span class="hljs-keyword">var</span> copies = callbacks.slice(<span class="hljs-number">0</span>); <span class="hljs-comment">// callbacks是全局的，存放 用了nextTick的 函数</span>
    callbacks.length = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < copies.length; i++) &#123;
      copies[i](); <span class="hljs-comment">// 执行callbacks</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>触发好了用户写的watch:&#123; ... &#125;的回调函数之后，最后要执行 页面渲染的必备的函数"function () &#123; vm._update(vm._render(), hydrating); &#125;"</p>
<ul>
<li>后面就是执行 关键渲染函数vm._update(vm._render(), hydrating)，和编译过程里面的渲染是一样的了，可以看我的另一篇这里：<a href="https://juejin.cn/post/6997670497723023390" target="_blank" title="https://juejin.cn/post/6997670497723023390">vue源码解析之编译过程-含2种模式(及vue-loader作用)</a></li>
</ul>
</li>
</ol>
<h2 data-id="heading-4">调度过程总结</h2>
<p>场景是：修改data里面的数据（假设是修改 this.aa = 123），页面上对应的位子得到update</p>
<p>过程总结：</p>
<ol>
<li>触发aa的set监听函数</li>
<li>处理aa的订阅者队列subs（订阅者队列包含：computed，watch，关键渲染函数）
<ul>
<li>computed对应的 改成 this.dirty = true，下次model层取值的时候，就知道对应computed要重新计算了。否则会用缓存</li>
</ul>
</li>
<li>watch 里面的回调函数会放到全局对象queue队列里面去。并且由nextTick控制，同步任务期间只会一直加入进queue队列，同步任务结束后，才会开始run queue队列
<ul>
<li>queue队列的最后一个是 关键渲染函数 function () &#123; vm._update(vm._render(), hydrating); &#125;"）
<ul>
<li>会有全局变量flushing控制，确保一次同步任务，只会执行一次 关键渲染函数</li>
</ul>
</li>
<li>nextTick原理是微任务，</li>
</ul>
</li>
<li>后面就是执行 关键渲染函数vm._update(vm._render(), hydrating)，和编译过程里面的渲染是一样的了，可以看我的另一篇这里：<a href="https://juejin.cn/post/6997670497723023390" target="_blank" title="https://juejin.cn/post/6997670497723023390">vue源码解析之编译过程-含2种模式(及vue-loader作用)</a></li>
</ol>
<h2 data-id="heading-5">再谈一下vue的双向绑定v-model原理</h2>
<p>实际是一个语法糖（语法糖的意思 可以理解为简写，下面第二行是真实的样子）</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">'abc'</span> /></span> // 语法糖
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">'abc'</span> @<span class="hljs-attr">input</span>=<span class="hljs-string">'abc = $event.target.value'</span> /></span> // 真实的样子

注：value是表单控件的值。以名字/值对的形式随表单一起提交
<span class="copy-code-btn">复制代码</span></code></pre>
<p>过程是： DOM Listeners -> Model -> Data Bindings -> render 到页面上</p>
<ul>
<li>DOM Listeners 比如 input事件，select事件（<strong>所以v-model只支持表单元素</strong>）</li>
<li>Model是Model层（数据层），通过事件，修改this.abc = $event.target.value。然后会触发this.aa的set函数，然后会触发 关键渲染函数vm._update(vm._render(), hydrating)。最终渲染到页面上</li>
</ul>
<hr>
<p>码字不易，点赞鼓励</p></div>  
</div>
            