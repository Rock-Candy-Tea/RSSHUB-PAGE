
---
title: '认识React的虚拟Dom（1） _ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccab79252b4845bebbe627842793f9a3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 19:25:04 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccab79252b4845bebbe627842793f9a3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style>
<h4 data-id="heading-0">前端技术的快速发展，让现在的vue、react成为主流框架</h4>
<p>一开始的静态页面，到后来的jquery，到现在的vue、react，mvvm、mvc前端开发模式都使用了虚拟dom
但纵观主流框架好像也是对虚拟dom 的各种造作和改进
<strong>为什么要使用虚拟dom呢?</strong></p>
<p>首先我们了解下什么是虚拟dom</p>
<ol>
<li>虚拟 DOM 是 JS 对象</li>
<li>虚拟 DOM 是对真实 DOM 的描述</li>
</ol>
<pre><code class="copyable"><h1 className="greeting">Hello, world! </h1>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个标签在react会展示为如下类型：</p>
<pre><code class="copyable">const element = &#123;
  type: 'h1',
  props: &#123;
    className: 'greeting',
    children: 'Hello, world!'
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>React 中的虚拟 DOM 大致是如何工作的。虚拟 DOM 在 React 组件的挂载阶段和更新阶段工作流程如下：</p>
<ul>
<li>
<p><strong>挂载阶段</strong>，React 将结合 JSX 的描述，构建出虚拟 DOM 树，然后通过 ReactDOM.render 将dom树转换为真实的dom,挂载到页面上；</p>
</li>
<li>
<p><strong>更新阶段</strong>，页面在作用于真实 DOM 之前，会先作用于虚拟 DOM，虚拟 DOM 将在 JS 层借助diff算法先对比出具体有哪些真实 DOM 需要被改变，然后再将这些改变作用于真实 DOM,进行更新渲染。</p>
</li>
</ul>
<p><strong>虚拟DOM保留了真实DOM节点的一些基本属性，和节点之间的层次关系，把它们放在一个对象中，它相当于在javascript和DOM之间的一层“缓存”</strong></p>
<p><strong>虚拟DOM是如何解决问题的</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccab79252b4845bebbe627842793f9a3~tplv-k3u1fbpfcp-watermark.image" alt="屏幕截图 2021-07-30 135240.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>React 使用了 JSX，一种使用体验和模板相似的 JS 语法糖。</p>
<blockquote>
<p>JSX 是 JavaScript 的一种语法扩展，它和模板语言很接近，但是它充分具备 JavaScript 的能力。</p>
</blockquote>
<p>实际上浏览器并没有解析jsx的能力</p>
<p>这里Babel将jsx转换为具有JavaScript的能力，Bable将jsx代码转换为大部分低版本浏览器也能够识别的 ES5 代码</p>
<p>区别就在于多出了一层虚拟 DOM 作为缓冲层。这个缓冲层带来的利好是：当 DOM 操作（渲染更新）比较频繁时，它会先将前后两次的虚拟 DOM 树进行对比，定位出具体需要更新的部分，生成一个“补丁集”，最后只把“补丁”打在需要更新的那部分真实 DOM 上，实现精准的“差量更新”。这个过程对应的虚拟 DOM 工作流如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1104742a2e604fd69299669b600913e0~tplv-k3u1fbpfcp-watermark.image" alt="屏幕截图 2021-07-30 145238.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里对diff算法没有做太多的解释，想了解的可以看看源码</p>
<p><strong>React 选用虚拟 DOM，真的是为了更好的性能吗？</strong></p>
<p>关于这个问题，可以看看大佬的回答(<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F31809713" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhihu.com/question/31809713" ref="nofollow noopener noreferrer">www.zhihu.com/question/31…</a>)</p>
<p>其实虚拟dom的好处是“使得前端开发能够基于函数式 UI 的编程方式实现高效的声明式编程”
虚拟 dom 的存在，不能片面的去说它解决了真实 dom 更新视图带来的性能问题，是提升视图渲染性能存在的。虚拟 dom 是让 diff 算法提供了可能。并且为编译多平台代码提供了可能，我们可以在虚拟 dom 转化为真实节点这一步，做跨平台的文章。还有一点便是提升开发体验和提高开发效率，让 ui=fn（state）这样数据驱动视图的函数式、声明式编程变为可能，JSX 便是其中一个品类。</p>
<h3 data-id="heading-1">码字不易，请大佬指教！</h3></div>  
</div>
            