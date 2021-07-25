
---
title: '带你认识vue3'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6311'
author: 掘金
comments: false
date: Sat, 24 Jul 2021 04:36:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=6311'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>文章内容输出来源：拉勾大前端高薪训练营</p>
</blockquote>
<h4 data-id="heading-0">1、Vue 3.0 性能提升主要是通过哪几方面体现的？</h4>
<p>答：通过3方面体现</p>
<ol>
<li>响应式系统升级，采用Proxy实现</li>
<li>编译优化，通过静态节点检查以及Patch标记等实现</li>
<li>源码体积优化，通过tree-shaking,以及静态提升等实现</li>
</ol>
<p>　</p>
<p>　</p>
<p>　</p>
<h4 data-id="heading-1">2、Vue 3.0 所采用的 Composition Api 与 Vue 2.x使用的Options Api 有什么区别？</h4>
<p>答：有以下区别</p>
<ul>
<li>vue2.x逻辑代码组织分散，vue3逻辑代码组织集中更加方便管理和维护</li>
<li>vue2.x逻辑代码难于重用，vue3逻辑代码易于重用</li>
<li>vue2.x适用于简单的组件，vue3既适用于简单组件也适用于业务复杂的大型组件</li>
<li>vue3的composition api对tree-shaking更友好，代码更加易于压缩</li>
<li>vue3的composition api避免了对this的使用，彻底解决了this的指向问题　</li>
</ul>
<p>　</p>
<h4 data-id="heading-2">3、Proxy 相对于 Object.defineProperty 有哪些优点？</h4>
<p>答：相较Object.defineProperty, Proxy有这些优点</p>
<ul>
<li>Proxy可以直接监听对象而非属性</li>
<li>Proxy可以劫持整个对象</li>
<li>Proxy可以监听动态新增的属性</li>
<li>Proxy可以监听删除的属性</li>
<li>Proxy可以监听数组变化，特别地可以监听数组的索引和length属性</li>
<li>Proxy有多达13种拦截方法，分别是：</li>
</ul>
<blockquote>
<p>get(target, propKey, receiver)：拦截对象属性的读取，比如proxy.foo和proxy['foo']。</p>
</blockquote>
<blockquote>
<p>set(target, propKey, value, receiver)：拦截对象属性的设置，比如proxy.foo = v或proxy['foo'] = v，返回一个布尔值。</p>
</blockquote>
<blockquote>
<p>has(target, propKey)：拦截propKey in proxy的操作，返回一个布尔值。</p>
</blockquote>
<blockquote>
<p>deleteProperty(target, propKey)：拦截delete proxy[propKey]的操作，返回一个布尔值。</p>
</blockquote>
<blockquote>
<p>ownKeys(target)：拦截Object.getOwnPropertyNames(proxy)、Object.getOwnPropertySymbols(proxy)Object.keys(proxy)、for...in循环，返回一个数组。该方法返回目标对象所有自身的属性的属性名，而Object.keys()的返回结果仅包括目标对象自身的可遍历属性。<code>  </code></p>
</blockquote>
<blockquote>
<p>getOwnPropertyDescriptor(target, propKey)：拦截Object.getOwnPropertyDescriptor(proxy, propKey)，返回属性的描述对象。</p>
</blockquote>
<blockquote>
<p>defineProperty(target, propKey, propDesc)：拦截Object.defineProperty(proxy, propKey, propDesc）、Object.defineProperties(proxy, propDescs)，返回一个布尔值。</p>
</blockquote>
<blockquote>
<p>preventExtensions(target)：拦截Object.preventExtensions(proxy)，返回一个布尔值。</p>
</blockquote>
<blockquote>
<p>getPrototypeOf(target)：拦截Object.getPrototypeOf(proxy)，返回一个对象。</p>
</blockquote>
<blockquote>
<p>isExtensible(target)：拦截Object.isExtensible(proxy)，返回一个布尔值。</p>
</blockquote>
<blockquote>
<p>setPrototypeOf(target, proto)：拦截Object.setPrototypeOf(proxy, proto)，返回一个布尔值。如果目标对象是函数，那么还有两种额外操作可以拦截。</p>
</blockquote>
<blockquote>
<p>apply(target, object, args)：拦截 Proxy 实例作为函数调用的操作，比如proxy(...args)、proxy.call(object, ...args)、proxy.apply(...)。</p>
</blockquote>
<blockquote>
<p>construct(target, args)：拦截 Proxy 实例作为构造函数调用的操作，比如new proxy(...args)。</p>
</blockquote>
<p>　</p>
<p>　</p>
<h4 data-id="heading-3">4、Vue 3.0 在编译方面有哪些优化？</h4>
<p>答：vue在编译方面有这些优化</p>
<ul>
<li>支持多根节点,即Fragments（需要升级vetur插件，否则会有红色波浪线）</li>
<li>标记和提升所有的静态根节点</li>
<li>Patch flag</li>
<li>缓存事件处理函数</li>
</ul>
<p>　</p>
<p>　</p>
<h4 data-id="heading-4">5、Vue.js 3.0 响应式系统的实现原理？</h4>
<ul>
<li>Vue3内部采用ES6的Proxy代理对象来实现响应式系统</li>
<li>Proxy用于实现属性嗅探，在初始化过程中不必遍历所有属性来定义它们的属性。</li>
<li>多属性嵌套，在访问属性的过程中处理下一级属性(递归处理)</li>
<li>默认情况下会监视动态添加的属性。</li>
<li>默认侦听属性的删除操作</li>
<li>默认情况下，它侦听数组索引和长度属性的修改。</li>
<li>它可以作为一个单独的模块使用。</li>
</ul>
<p>核心方法：</p>
<ul>
<li>reactive/ref/toRefs/computed</li>
<li>effect(在watch函数中使用的底层函数。)</li>
<li>track(用于收集依赖函数)</li>
<li>trigger(用于触发更新)</li>
</ul>
<p>　</p>
<p>　</p>
<p>　</p></div>  
</div>
            