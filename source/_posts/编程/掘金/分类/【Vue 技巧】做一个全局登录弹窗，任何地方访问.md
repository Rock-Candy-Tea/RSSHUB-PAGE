
---
title: '【Vue 技巧】做一个全局登录弹窗，任何地方访问'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3124b91bb83844c3a662a09b35321abf~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 08 May 2021 21:52:04 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3124b91bb83844c3a662a09b35321abf~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>需要一个登录弹窗，在任何地方都能使用。</p>
</blockquote>
<h3 data-id="heading-0">需求</h3>
<ol>
<li>在任何页面内能访问</li>
<li>在路由拦截能访问</li>
</ol>
<h3 data-id="heading-1">解决方案</h3>
<p>任何地方都能访问，第一个想到的是挂载原型链<code>Vue.prototype.$someThing</code>。而访问一个实例，一般是<code>ref</code>去访问，路由是在<code>Vue</code>配置时组成了守卫，这时还访问不了<code>vue实例</code>，<code>refs</code>是实例属性，就更访问不了<code>组件实例</code>了，可能可以动态改路由守卫，但是这里准备用单开一个<code>vue实例</code>，这样就可以暴露一个单独实例出来了。</p>
<h3 data-id="heading-2">步骤</h3>
<h4 data-id="heading-3">1. 新建一个<code>js文件</code>，引入<code>main.js</code></h4>
<p>由于我的项目搭建是<code>@/components/index.js</code>负责注册全局组件，所以这里在<code>@/components/index.js</code>引入。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// @/components/index.js</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'@/components/LoginDialog'</span> <span class="hljs-comment">//在这引入全局登录弹窗</span>
<span class="hljs-keyword">import</span> SvgIcon <span class="hljs-keyword">from</span> <span class="hljs-string">'@/components/SvgIcon.vue'</span>

Vue.component(<span class="hljs-string">'SvgIcon'</span>, SvgIcon)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">2. 新建一个实例，挂载到<code>document.body</code></h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> LoginDialog <span class="hljs-keyword">from</span> <span class="hljs-string">'./index.vue'</span>

<span class="hljs-comment">// 这里可以用Vue.extend()创建子类，但是我没打算注册为组件，就直接`new Vue`</span>
<span class="hljs-keyword">const</span> loginDialog = <span class="hljs-keyword">new</span> Vue(LoginDialog) 
loginDialog.$mount(<span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>))
<span class="hljs-built_in">document</span>.body.appendChild(loginDialog.$el)

Vue.prototype.$loginDialog = loginDialog

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> loginDialog
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">3. 在路由守卫里访问</h4>
<p>直接引入实例</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store'</span>
<span class="hljs-keyword">import</span> loginDialog <span class="hljs-keyword">from</span> <span class="hljs-string">'@/components/LoginDialog'</span>

<span class="hljs-keyword">const</span> whiteList = [<span class="hljs-string">'/'</span>]

router.beforeEach(<span class="hljs-function">(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (store.getters.token) next()
    <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (whiteList.indexOf(to.path) > -<span class="hljs-number">1</span>) next()
    <span class="hljs-keyword">else</span> loginDialog.open()
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">4. 在页面内访问</h4>
<pre><code class="hljs language-js copyable" lang="js"><vs-button @click=<span class="hljs-string">"login"</span> transparent>登录</vs-button>
<span class="hljs-function"><span class="hljs-title">login</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.$loginDialog.open()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3124b91bb83844c3a662a09b35321abf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里就有2个<code>根实例</code>了</p></div>  
</div>
            