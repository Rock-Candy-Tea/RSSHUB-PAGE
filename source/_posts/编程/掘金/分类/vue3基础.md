
---
title: 'vue3基础'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c50a723d1ee2412b83efd581d8259639~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 18:25:48 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c50a723d1ee2412b83efd581d8259639~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">一 Vue3基础</h3>
<h4 data-id="heading-1">1 createApp()和mount()方法</h4>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/vue@next"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> app = Vue.createApp(&#123;&#125;)
    app.mount(<span class="hljs-string">"#app"</span>)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>createApp()创建一个Vue的实例。
<ul>
<li>它接受一个对象形式的参数&#123;&#125;。</li>
<li>这个对象就是告诉Vue应该如何展现我们最外层的组件。</li>
</ul>
</li>
<li>mount()挂载到某个html的DOM节点上。
<ul>
<li>如何获取Vue的根组件vm?——const vm = app.mount("#app");console.log(vm);</li>
</ul>
</li>
</ul>
<h4 data-id="heading-2">2 生命周期钩子</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c50a723d1ee2412b83efd581d8259639~tplv-k3u1fbpfcp-watermark.image" alt="2021-06-17_163225_看图王.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">3 插值表达式和v-bind动态赋值</h4>
<ol>
<li>插值表达式：也叫字面量，用来展示在data中定义的数据。使用：&#123;&#123;xxxx&#125;&#125;，支持js表达式</li>
<li>v-bind指令：用来处理html标签的动态属性，即动态赋值。</li>
</ol>
<pre><code class="copyable"><img v-bind:src="imgSrc" /> // 常规写法
<img :src="imgSrc" /> // 缩写
return &#123;    
    imgSrc:'http://liangxinghua.com/img/87.png'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">4 模板动态参数和阻止默认事件</h4>
<ol>
<li>v-on指令：v-on是用来绑定响应事件的。</li>
<li>模板动态参数：也叫动态属性，使用：<code>[]</code>方括号加上data中变量名的形式。</li>
<li>事件动态绑定：使用：<code>[]</code>方括号加上data中变量名的形式。</li>
</ol>
<pre><code class="copyable"><h2 :title="message">&#123;&#123;message&#125;&#125;</h2>
<h2 :[name]="message">&#123;&#123;message&#125;&#125;</h2> // [name]模板动态参数
<button v-on:click="hanldClick">绑定事件</button> // 常规写法
<button @:click="hanldClick">绑定事件</button> // 缩写
<button @[event]="hanldClick">绑定事件</button> // [event]事件动态绑定
data()&#123;
    return&#123;
        message:'这是一个提示信息' ,
        name:'title',
        event:'click',
    &#125;
&#125;,
methods:&#123;
    hanldClick()&#123; 
        alert('欢迎光临红浪漫')
    &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>阻止默认事件</li>
</ol>
<p>最常见的就是表单的默认提交事件：调用e.preventDefault()。<br>
更好的方式是使用事件修饰符直接可以阻止默认行为.prevent</p>
<pre><code class="copyable"><form action="https://jspang.com" @click="hanldeButton">
    <button type="submit">默认提交</button>
</form>
methods:&#123;
    hanldeButton(e)&#123;
        e.preventDefault()
    &#125;,
&#125;,
<form @submit.prevent="onSubmit"></form> // 提交事件不再重载页面
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            