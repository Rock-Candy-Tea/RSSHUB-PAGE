
---
title: '详解 Vue 八大生命周期钩子函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97b2957a51f04e34a4eb5985b4945745~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 19:10:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97b2957a51f04e34a4eb5985b4945745~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>摘要：Vue 为生命周期中的每个状态都设置了钩子函数(监听函数) 。每当 Vue 实例处于不同的生命周期时，对应的函数就会被触发调用。</p>
</blockquote>
<p>本文分享自华为云社区<a href="https://bbs.huaweicloud.com/blogs/278913?utm_source=juejin&utm_medium=bbs-ex&utm_campaign=other&utm_content=content" target="_blank" rel="nofollow noopener noreferrer">《一文带你弄懂Vue八大生命周期钩子函数》</a>，原文作者：北极光之夜。</p>
<h2 data-id="heading-0">一.速识概念：</h2>
<p>我们把一个对象从生成（new）到被销毁（destory）的过程，称为生命周期。而生命周期函数，就是在某个时刻会自动执行的函数。</p>
<p>按照官方的原话，就是每个 Vue 实例在被创建时都要经过一系列的初始化过程——例如，需要设置数据监听、编译模板、将实例挂载到 DOM 并在数据变化时更新 DOM 等。同时在这个过程中也会运行一些叫做生命周期钩子的函数，这给了用户在不同阶段添加自己的代码的机会。</p>
<p>简单来说就是每个 Vue 实例在被创建时都要经过一系列的初始化过程：创建实例，装载模板，渲染模板等。Vue 为生命周期中的每个状态都设置了钩子函数(监听函数) 。每当 Vue 实例处于不同的生命周期时，对应的函数就会被触发调用。</p>
<h2 data-id="heading-1">二.八大生命周期钩子函数：</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97b2957a51f04e34a4eb5985b4945745~tplv-k3u1fbpfcp-zoom-1.image" alt="详解 Vue 八大生命周期钩子函数" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>下面是官方文档里的生命周期图，英语好的同学可以看看：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c362d2ec1564280a264cc06e6368ea9~tplv-k3u1fbpfcp-zoom-1.image" alt="详解 Vue 八大生命周期钩子函数" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">三.结合代码了解：</h2>
<p>先看案例基本代码如下，后面通过如下代码步骤演示一个对象从生成到被销毁的过程各阶段执行的生命周期函数。注意 show 函数的作用。</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="https://unpkg.com/vue/dist/vue.js"></script>
</head>
<body>
    <div id="app">
        &#123;&#123;information&#125;&#125;
    </div>
    <script type="text/javascript">
       //创建vue实例
       var vm = new Vue(&#123;
           el: '#app',
           data: &#123;
               information: '北极光之夜。' 
           &#125;
       &#125;)
       // 各个生命周期函数通过调用下面这个函数了解其所处的生命阶段
       function show(inf,obj)&#123;
          console.log(inf);
          console.log("------------------------------------------");
          console.log('获取vue实例data里的数据:');
          console.log(obj.information);
          console.log("------------------------------------------");
          console.log('挂载的对象，就是DOM：');
          console.log(obj.$el);
          console.log("------------------------------------------");
          console.log('页面上已经挂载的DOM：');
          console.log(document.getElementById('app').innerHTML);
       &#125;


    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">1. beforeCreate：</h3>
<p>这个阶段 vue 实例刚刚在内存中创建，此时 data 和 methods 这些都没初始化好。 </p>
<p>在案例中添加 beforeCreate 钩子函数：</p>
<pre><code class="copyable">var vm = new Vue(&#123;
           el: '#app',
           data: &#123;
               information: '北极光之夜。' 
           &#125;,
           beforeCreate: function()&#123;
             // 传入该阶段简介与this，this就是该阶段的vue实例
                  show('vue实例初始化之前',this);
           &#125;
       &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看运行结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8426c2b3849a46c8bcc925b9d9f1056e~tplv-k3u1fbpfcp-zoom-1.image" alt="详解 Vue 八大生命周期钩子函数" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，此时 vue 实例刚刚在内存中创建，其它什么都 undefined。</p>
<h3 data-id="heading-4">2.created：</h3>
<p>这个阶段 vue 实例在内存中已经创建好了，data 和 methods 也能够获取到了，但是模板还没编译。 </p>
<p>在案例中添加 created 钩子函数：</p>
<pre><code class="copyable"> var vm = new Vue(&#123;
           el: '#app',
           data: &#123;
               information: '北极光之夜。' 
           &#125;,
           created: function()&#123;
                  show('vue实例初始化之后',this);
           &#125;
       &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47ce771505774e6eb18395cbd46de4ff~tplv-k3u1fbpfcp-zoom-1.image" alt="详解 Vue 八大生命周期钩子函数" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看到没，已经知道 data 里的数据了。其它的话都没。</p>
<h3 data-id="heading-5">3.beforeMount：</h3>
<p>这个阶段完成了模板的编译，但是还没挂载到页面上。 </p>
<p>在案例中添加钩子函数：</p>
<pre><code class="copyable">var vm = new Vue(&#123;
           el: '#app',
           data: &#123;
               information: '北极光之夜。' 
           &#125;,
           beforeMount: function()&#123;
             show('挂载之前',this);
           &#125;
       &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/873475c0d180462d8e8e2af324067f69~tplv-k3u1fbpfcp-zoom-1.image" alt="详解 Vue 八大生命周期钩子函数" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看到没，要挂载的对象都编译好了，但是页面的 DOM 树还没挂上去，这个阶段页面还没能显示出来。</p>
<h3 data-id="heading-6">4.mounted：</h3>
<p>这个阶段，模板编译好了，也挂载到页面中了，页面也可以显示了。 </p>
<p>在案例中添加钩子函数：</p>
<pre><code class="copyable"> var vm = new Vue(&#123;
           el: '#app',
           data: &#123;
               information: '北极光之夜。' 
           &#125;,
           mounted: function()&#123;
            show('挂载之后',this);
           &#125;
       &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88b12077d32e44f9a9ebcc74665fba71~tplv-k3u1fbpfcp-zoom-1.image" alt="详解 Vue 八大生命周期钩子函数" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">5.beforeUpdate:</h3>
<p>转态更新之前执行此函数，此时 data 中数据的状态值已经更新为最新的，但是页面上显示的数据还是最原始的，还没有重新开始渲染 DOM 树。</p>
<p>先改变 data 里数据：</p>
<pre><code class="copyable">vm.information = '南极光之夜';
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在案例中添加钩子函数：</p>
<pre><code class="copyable"> var vm = new Vue(&#123;
           el: '#app',
           data: &#123;
               information: '北极光之夜。' 
           &#125;,
          beforeUpdate: function()&#123;
            show('更新之前',this);
           &#125;
       &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37cc19f64a0f42c8aab02a7e3a645ac5~tplv-k3u1fbpfcp-zoom-1.image" alt="详解 Vue 八大生命周期钩子函数" loading="lazy" referrerpolicy="no-referrer"></p>
<p>​看到没，vue 实例里的数据已经变成了南极光之夜。但是此阶段页面 DOM 节点上显示的还是初始的数据北极光之夜。</p>
<h3 data-id="heading-8">6.updated：</h3>
<p>这个阶段是转态更新完成后执行此函数，此时 data 中数据的状态值是最新的，而且页面上显示的数据也是最新的，DOM 节点已经被重新渲染了。</p>
<p>在案例中添加钩子函数：</p>
<pre><code class="copyable">var vm = new Vue(&#123;
           el: '#app',
           data: &#123;
               information: '北极光之夜。' 
           &#125;,
          updated: function()&#123;
            show('更新之后',this);
           &#125;
       &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​看运行结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a643237557374f2985aec5b238536e07~tplv-k3u1fbpfcp-zoom-1.image" alt="详解 Vue 八大生命周期钩子函数" loading="lazy" referrerpolicy="no-referrer"></p>
<p>更新了，全都更新了~</p>
<h3 data-id="heading-9">7.beforeDestroy：</h3>
<p>beforeDestroy 阶段处于 vue 实例被销毁之前，当然，这个阶段 vue 实例还能用。</p>
<p>销毁 Vue 实例：</p>
<pre><code class="copyable">vm.$destroy();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在案例中添加钩子函数：</p>
<pre><code class="copyable">var vm = new Vue(&#123;
           el: '#app',
           data: &#123;
               information: '北极光之夜。' 
           &#125;,
          beforeDestroy: function() &#123;
            show('销毁之前',this);
          &#125;
       &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7421f43fcfea432e8c5aae17d339a3c9~tplv-k3u1fbpfcp-zoom-1.image" alt="详解 Vue 八大生命周期钩子函数" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">​8.destroyed：</h3>
<p>这个阶段在 vue 实例销毁后调用，此时所有实例指示的所有东西都会解除绑定，事件监听器也都移除，子实例也被销毁。</p>
<p>在案例中添加钩子函数：</p>
<pre><code class="copyable">var vm = new Vue(&#123;
           el: '#app',
           data: &#123;
               information: '北极光之夜。' 
           &#125;,
          destroyed: function() &#123;
            show('销毁之后',this);
          &#125;
       &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04c293f7c3da42d69832bb4269276f88~tplv-k3u1fbpfcp-zoom-1.image" alt="详解 Vue 八大生命周期钩子函数" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://bbs.huaweicloud.com/blogs?utm_source=juejin&utm_medium=bbs-ex&utm_campaign=other&utm_content=content" target="_blank" rel="nofollow noopener noreferrer">点击关注，第一时间了解华为云新鲜技术~</a></p></div>  
</div>
            