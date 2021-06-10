
---
title: 'index.vue的无法承受之重'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f327ab056de34be6b9f2eb630b8f8256~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 02:25:52 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f327ab056de34be6b9f2eb630b8f8256~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>项目中有一个<code>index.vue</code>文件有1000多行代码，还是把css独立出来的，这暴露了很多问题。</p>
<h1 data-id="heading-0">命名问题</h1>
<p>已<code>index</code>命名的文件，里面的内容应该是"言健意骇"，<strong>表示当前文件夹下的资源是怎么对外提供的</strong>，换言之，不是用来写业务逻辑的，比如element的<code>index.js</code></p>
<pre><code class="copyable">import ElAutocomplete from './src/autocomplete';

/* istanbul ignore next */
ElAutocomplete.install = function(Vue) &#123;
  Vue.component(ElAutocomplete.name, ElAutocomplete);
&#125;;

export default ElAutocomplete;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以，如果需要有一个<code>index</code>命名的文件，也应是<code>index.js</code>才对</p>
<p>一些开发人员喜欢已"具名文件夹/index.vue"的形式对应一个页面级别的路由，诚然，再Visual Studio Code中，通过"具名文件夹"能快速关联出对应的<code>index.vue</code>。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f327ab056de34be6b9f2eb630b8f8256~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>出于参考写法、几个页面之间有交互等缘由，我打开了多个文件
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/866163fbed4b49e2bf610eab5a09ed7a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
想在开发者工具调试时候
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73b96b442831441494fcf3048fee04a7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
<strong>命名最重要的就是区分性</strong>，而<code>index.vue</code>唯一的好处可能是导入组件的时候能够少写一层路径，对于自动导入来讲，区别不大</p>
<h1 data-id="heading-1">代码分割问题</h1>
<p><strong>为了代码分割而独立出来的组件是有必要的</strong>，可以已后缀区分 Page、Dialog、Tabpane、Panel、Block等，自然要结合功能点，切割太多也很头疼。</p>
<p>结构的清晰保证了代码的清晰，定位问题也方便，分工合作方便。</p>
<p>通常让一些开发者厌恶这种方法的，可能是在于诸多"麻烦"，就像使用TS一样。
其实对于这种组件之间的交互，可以舍弃传统的<code>props</code>和<code>emit</code>，它们更适用于公共组件，现在的场景下，<code>provide</code>和<code>inject</code>会更合适，这样就会少去诸多模板代码。</p>
<p>element 的   <code>Form</code>和<code>FormItem</code>组件是这样操作的。</p>
<h1 data-id="heading-2">总结</h1>
<p>尽管网上的一些开源项目，不免有使用<code>index.vue</code>的，<strong>可衡量一种命名策略合不合适要结合项目本身</strong></p>
<ol>
<li>文件的体量</li>
<li>文件之间的关系</li>
<li>项目的用途。</li>
</ol>
<p>另外一点，组件名的首字母是要大写的，其中的一个要素是为了和一些纯js的东西区分开。</p>
<p>我看vue的官网中，并没有组件首字母小写的例子，不知道这种写法是怎么流行起来的
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d0721d35d784b6397d1c7c26475cdaf~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3090b08104c4d3bbff718aadac4cd11~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这可能类似vue的读音</p>
<blockquote>
<p>Vue (读音 /vjuː/，类似于 view)</p>
</blockquote>
<p>尽管官网明确指出，但仍有很多人喜欢一个字母一个字母的读，我第一次认识到这个问题的时候觉得没什么，双方知道意思就好了，可最近多发个e的音，总感觉怪怪的。</p>
<p><a href="https://www.zhihu.com/question/68760209/answer/267083767" target="_blank" rel="nofollow noopener noreferrer">Vue该怎么念？</a>，在我看来，本质上是人很难改变已有的认知。</p></div>  
</div>
            