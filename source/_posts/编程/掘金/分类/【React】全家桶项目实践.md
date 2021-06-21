
---
title: '【React】全家桶项目实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: ''
author: 掘金
comments: false
date: Mon, 21 Jun 2021 01:28:37 GMT
thumbnail: ''
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>**这是我参与更文挑战的第3天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a><br>
**</p>
<blockquote>
<p><strong>为什么要学习React?</strong></p>
</blockquote>
<p>选择任何一门语言学习都是有时间和金钱的成本的，那么React值不值得学习呢？我们应该从以下几个方面考虑：</p>
<ol>
<li>
<p>使用组件化开发方式，符合现代Web开发的趋势; 企业前后端项目分离，唯有React是首选；</p>
</li>
<li>
<p>技术成熟，社区完善，配件齐全，适用于大型Web项目（生态系统健全）</p>
</li>
<li>
<p>由Facebook专门的团队维护，技术支持可靠;</p>
</li>
<li>
<p>ReactNative - Learn once, write anywhere: Build mobile apps with React；</p>
</li>
<li>
<p>使用方式简单，性能非常高，支持服务端渲染;</p>
</li>
<li>
<p>React使用前端技术非常全面，有利于整体提高技术水平；此外，有利于求职和晋升，有利于参与潜力大的项目。</p>
</li>
</ol>
<h2 data-id="heading-0">一、React快速入门</h2>
<p>React 起源于 Facebook 的内部项目，因为该公司对市场上所有 JavaScript MVC 框架，都不满意，就决定自己写一套，用来架设他们自己的 Instagram 的网站。做出来以后，发现这套东西很好用，在2013年5月开源了。目前已经成为前端的三大主流框架。</p>
<h3 data-id="heading-1">1.1 什么是React?</h3>
<p>React是用于构建用户界面的JavaScript 库，围绕React的技术栈主要包括：React, redux, rect-redux, react-router, .....</p>
<p>React官网：<a href="https://reactjs.org/" target="_blank" rel="nofollow noopener noreferrer">reactjs.org/</a></p>
<p>React中文：<a href="https://react.docschina.org/" target="_blank" rel="nofollow noopener noreferrer">react.docschina.org/</a></p>
<p><strong>React有哪些特点：</strong></p>
<ol>
<li>
<p>使用JSX语法创建组件，实现组件化开发，为函数式的 UI 编程方式打开了大门;</p>
</li>
<li>
<p>性能高：通过 diff算法 和 虚拟DOM 实现视图的高效渲染和更新;</p>
</li>
</ol>
<blockquote>
<p>JSX --> HTML</p>
<p>JSX --> native ios或android中的组件（XML）</p>
<p>JSX --> VR/AR</p>
<p>JSX --> 区块链/物联网</p>
<p>JSX --TO--> EveryThing</p>
</blockquote>
<p><strong>React核心：虚拟DOM 和 Diff算法</strong></p>
<h3 data-id="heading-2">1.2 简单了解虚拟DOM?</h3>
<p>React将DOM抽象为虚拟DOM，虚拟DOM其实就是用一个对象来描述DOM，通过对比前后两个对象的差异，最终只把变化的部分重新渲染，提高渲染的效率。</p>
<p><strong>为什么用虚拟DOM?</strong></p>
<p>当DOM发生更改时需要遍历DOM对象的属性, 而原生DOM可遍历属性多达200多个个, 而且大部分属性与渲染无关, 导致更新页面代价太大。</p>
<p><strong>虚拟DOM的处理方式？</strong></p>
<p>1） 用 JS对象结构表示 DOM 树的结构，然后用这个树构建一个真正的 DOM 树，插到文档当中。</p>
<p>2）当状态变更的时候，重新构造一棵新的对象树。然后用新的树和旧的树进行比较，记录两棵树差异。</p>
<p>3） 把记录的差异应用到步骤1所构建的真正的DOM树上，视图就更新了。</p>
<h3 data-id="heading-3">1.3 简单了解Diff算法？</h3>
<p><strong><strong>最小化页面重绘</strong></strong></p>
<p>当我们使用React在render() 函数创建了一棵React元素树，在下一个state或者props更新的时候，render() 函数将会创建一棵新的React元素树。</p>
<p>React将对比这两棵树的不同之处，计算出如何高效的更新UI（只更新变化的地方），此处所采用的算法就是diff算法。</p>
<h2 data-id="heading-4">二、React初体验</h2>
<h3 data-id="heading-5">2.1 JSX语法全面入门</h3>
<p><strong>1) Demo1: 往容器中插入一个span标签, 设置clssName和myCnotent。 两种实现方式: a) 通过典型js方式; b) JSX方式?</strong></p>
<pre><code class="copyable">典型JS方式
1，创建虚拟DOM
const Dom = React.createElement('span',&#123;className:myClass&#125;,myContent);
2.渲染虚拟DOM
ReactDom.render(vDom,document.getElementById('app'));

JSX方式
1、创建虚拟DOM
const Dom = <span ClassName = &#123;myClass.toUpperCase()&#125;&#123;myContent&#125;></span>
2、渲染虚拟DOM
ReactDOM.render(Dom,document.getElementById('app'))
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>总结:</p>
<p>1. JSX只是高级语法糖, 最终执行时还是会被转成原生js, 通过babel等方式;</p>
<p>2. 更加语义化, 更加直观, 代码可读性更高;</p>
<p>3. 性能相对原生方式更加好一些!</p>
</blockquote>
<p><strong>2) Demo2: JSX常见的界面操作方式?</strong></p>
<p><strong>a. 多重标签嵌套</strong></p>
<p>核心代码如下:</p>
<pre><code class="copyable">ReactDOM.render( 
<div>
    <h2>多层标签嵌套</h2>
    <img src="" alt="" width="200" />
    <p></p>
</div>
document.getElementById('app'))
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>b. js中的变量, 表达式要写在&#123;&#125;内</strong></p>
<p>核心代码如下:</p>
<pre><code class="copyable">ReactDOM.render( 
<div>
    <p>&#123;2+5+6&#125;</p>
</div>
document.getElementById('app'))
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>c. 内联样式通过对象方式引入</strong></p>
<p>核心代码如下:</p>
<pre><code class="copyable">const MyStyle=&#123;
    backgroundColor:'blue',
    color:'green',
    fontSize:20
&#125;
ReactDOM.render( 
<div>
    <p style=&#123;MyStyle&#125;>颜色</p>
</div>
document.getElementById('app'))
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>d. 数组遍历</strong></p>
<p>核心代码如下:</p>
<pre><code class="copyable">const Arr=[
    &#123;name:'周杰伦',age:38&#125;,
    &#123;name:'刘德华',age:48&#125;
]
ReactDOM.render( 
<ul>
    &#123;Arr.map(
        (data,index)=><li>&#123;index+1&#125;-姓名：&#123;data.name&#125;,年龄：&#123;data.age&#125;岁</li>
    )&#125;
</ul>
document.getElementById('app'))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>页面效果展示:</p>
<p>1-姓名：周杰伦，年龄：38岁</p>
<p>2-姓名：刘德华，年龄：48岁</p>
<blockquote>
<p>案例总结如下:</p>
<p>1. JSX中添加属性时，使用 className 代替 class , 像label中的for属性，使用htmlFor代替；</p>
<p>2. JSX创建DOM的时候，所有的节点，必须有唯一的根元素进行包裹 ；</p>
<p>3. JSX语法中，标签必须成对出现，如果是单标签，则必须自闭和 ；</p>
<p>4. 在 JSX 中可以直接使用 JS代码，直接在 JSX 中通过 &#123;&#125; 中间写 JS代码即可；</p>
<p>5. 在 JSX 中只能使用表达式，不能出现语句；</p>
<p>6. 在 JSX 中注释语法：&#123;/* 中间是注释的内容 */&#125;。</p>
</blockquote>
<h2 data-id="heading-6">三、 React中的组件/模块, 组件化/模块化</h2>
<h3 data-id="heading-7">3.1 组件</h3>
<p>一个应用/版块/页面中用于实现某个局部的功能(包括html, js, css等), 把这些局部功能组装到一起就形成了完整的一个大的功能, 主要目的在于: 复用代码, 提高项目运行效率。</p>
<h3 data-id="heading-8">3.2 组件化</h3>
<p>如果一个应用是用多组件的方式进行综合开发的, 那么这个应用就是一个组件化应用。</p>
<h3 data-id="heading-9">3.3 模块</h3>
<p>多个组件形成模块, 或者是一个提供特定功能的js文件, 主要特点在于耦合性低, 可移植性高, 执行效率好。</p>
<h3 data-id="heading-10">3.4 模块化</h3>
<p>如果一个应用都是用模块的形式来构建的，那么这个应用就是模块化应用。</p>
<h3 data-id="heading-11">3.5 React中组件创建方式</h3>
<p><strong>a. 构造函数创建组件</strong></p>
<p>使用构造函数来创建组件时，如果要接收外界传递的数据，需要在构造函数的参数列表中使用props来接收；</p>
<p>必须要向外return一个合法的JSX创建的虚拟DOM；</p>
<h2 data-id="heading-12">四、 React中的state(状态)</h2>
<h3 data-id="heading-13">4.1 什么是state?</h3>
<p>React 把组件看成是一个状态机（State Machines）, 通过状态 (State) 去操作状态机。在开发中, 通过与用户的交互，实现不同状态，然后渲染 UI，让用户界面和数据保持一致。</p>
<p>在React 中，只需更新组件的 state，然后根据新的 state 重新渲染用户界（不要操作 DOM）。</p>
<h3 data-id="heading-14">4.2 state的使用方式?</h3>
<p>Demo: 更改界面内容</p>
<p>核心代码:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e24a71734b6c46918f4e84b8b9f44063~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>运行结果:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad8d91dd0e8e47488f0ec7c20c728f15~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击后效果:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2c55140486e4950aa4f4265113d9ad7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            