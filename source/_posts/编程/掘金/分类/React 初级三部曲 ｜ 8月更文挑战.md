
---
title: 'React 初级三部曲 ｜ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=460'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 07:59:21 GMT
thumbnail: 'https://picsum.photos/400/300?random=460'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">1， 什么是React</h4>
<p>React 是一个用于构建用户界面的JavaScript库，</p>
<p>用户界面： HTML页面</p>
<p>React 主要用来写HTML页面，或构建Web应用</p>
<p>如果从MVC的角度来看，React不仅仅是视图层，也就是只负责视图的渲染，而并非提供了完整的M和C的功能。</p>
<p>React起源于Facebook的内部项目，与2013年5月开源</p>
<h4 data-id="heading-1">2， React的特点</h4>
<p>1，声明式</p>
<pre><code class="copyable">const jsx = <div className = "app">
<h1>HellO React</h1>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2，基于组件</p>
<pre><code class="copyable">组件是react中最重要的内容
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3，学习一次，随处使用</p>
<ul>
<li>使用react可以开发web应用</li>
<li>使用react可以开发移动端原生应用（react-native)</li>
<li>使用react可以开发VR应用（react 360）</li>
</ul>
<h4 data-id="heading-2">3，React的安装</h4>
<p>安装命令<code>npm install react react-dom</code></p>
<ul>
<li>react 包是核心， 提供创建元素，组件等功能</li>
<li>react-dom 包提供DOM相关功能</li>
</ul>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="root"></div>
  <script src="./node_modules/react/umd/react.development.js"></script>
  <script src="./node_modules/react-dom/umd/react-dom.development.js"></script>
  <script>
    // 创建react 元素
    const title = React.createElement('h1', null, 'Hello World')
    // 渲染react 元素，并寻找挂载点
    ReactDOM.render(title, document.getElementById('root'))
  </script>
</body>
</html> 
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>React.createElement()说明</li>
</ul>
<p>React.createElement()说明</p>
<pre><code class="copyable">返回值： react元素
第一个参数： 要创建的react的元素名称
第二个参数： 该react元素的属性
第三个参数及其之后的参数： 该react元素的子节点
const title = React.createElement('h1', &#123; title: '标题' &#125;, 'Hello World') 
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">1, 脚手架是开发，现代web应用的必备
2, 充分的利用webpack, babel, eslint等工具辅助项目开发
3, 零配置，而不是工具配置
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">2， React项目初始化</h4>
<h4 data-id="heading-4">1， React脚手架意义</h4>
<h3 data-id="heading-5">二：第二节：React 脚手架</h3>
<ul>
<li>
<p>ReactDOM.render()说明</p>
<pre><code class="copyable">第一个参数： 要渲染的元素名称
第二个参数： DOM对象，用于指定渲染到页面中的位置
 ReactDOM.render(title, document.getElementById('root'))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>npx create-react-app my-app</p>
</li>
</ul>
<p>cd my-app</p>
<p>yarn start</p>
<h4 data-id="heading-6">3， npx 命令介绍</h4>
<p>npm v5.2.0引入的一条命令，目的是提升包内提供的命令行工具的使用体验。</p>
<p>原来：需要先安装脚手架包，现在无需安装脚手架包，可以直接使用这个包提供的命令。</p>
<p>推荐使用</p>
<pre><code class="copyable">npx create-react-app myProject
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2, yarn create react-app myProject</p>
<p>1, npm init react-app myProject</p>
<p>还有另外两种方式：</p>
<h4 data-id="heading-7">4， JSX的基本使用</h4>
<p>1, createElement()的问题</p>
<pre><code class="copyable">繁琐不简洁， 不直观，无法一眼看出所描述的结构，不优雅，用户体验不爽
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">React.createElement(
 'div',
 &#123;className: 'shopping-list'&#125;,
 React.createElement('h1', null, 'shopping-list'),
 React.createElement(
  'ul',
  null,
  React.createElemenet('li', null, 'Instagegram'),
  React.createElemenet('li', null, 'WhatApp')
 )
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同一的页面结构，用JSX语法实现</p>
<p>2, JSX 语法，等同于HTML语法</p>
<pre><code class="copyable"><div className="shopping-list">

  <h1>Shopping-list</h1>
  <ul>

    <li>Instagegram</li>

    <li>WhatSapp></li>

  </ul>

</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>JSX就是JavaScript XML的简写，表示在JavaScript代码中写XML格式的代码，与HTML结构相同，降低了学习成本，提升了开发效率，JSX是React的核心内容</p>
<p>3，JSX的基本使用步骤</p>
<p>（1）使用JSX语法，创建react元素</p>
<pre><code class="copyable">const title = <h1>Hello JSX</h1>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">ReactDOM.render(title, root)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">1, JSX 不是标准的ECMAScript语法，需要使用babel编译处理后，才能在浏览器中使用，
2, create-react-app脚手架中已经默认有该配置，无需手动配置
3, 编译JSX的语法包： @babel/preset-react
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">5， JSX 语法</h4>
<p>4，为什么脚手架中可以使用JSX语法？</p>
<p>(2) 使用ReactDOM.render()渲染react元素到页面中
注意点</p>
<p>1， React元素的属性名使用：驼峰命名法</p>
<p>2，特殊属性名：</p>
<p>class —> className</p>
<p>for—> htmlFor</p>
<p>tabindex—> tabIndex</p>
<p>3, 没有子节点的React 元素可以用 />结束</p>
<p>4，推荐： 使用小括号包裹JSX，从而避免JS中的自动插入分号陷阱</p>
<pre><code class="copyable">const div = (
  <div>使用小括号包裹</div>
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>三元表达式</p>
<p>注意： 是单大括号， 不是双大括号</p>
<p>1, 语法： &#123; javaScript &#125;</p>
<p><strong>条件渲染</strong></p>
<h4 data-id="heading-9">6， JSX 中使用JavaScript</h4>
<p>\</p>
<pre><code class="copyable"><span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">const isLoading = true
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">const loadData = () => &#123;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">  return isLoading ? (<div>loading....</div>) : (<div>加载成功之后的数据</div>)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>逻辑与运算符</p>
<pre><code class="copyable">const loadData = () => &#123;
  return isLoading && (<div>loading...</div>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">const lista = (
  <ul>
    &#123;
      songs.map( item => &#123;
       return <li key=&#123;item.id&#125;>&#123;item.name&#125;</li>
      &#125;)
    &#125;
  </ul>
)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"> <ul style=&#123;&#123;color: 'red', background: 'skyblue'&#125;&#125;>
  JSX的行内样式
 </ul>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(2) 类名— className(推荐)</p>
<p>(1) 行内样式 —style</p>
<p><strong>JSX样式处理</strong></p>
<ul>
<li>如果要渲染一组数据，应该使用数组的map()方法</li>
<li>注意： 渲染列表时，应该添加key属性，key属性的值要保证唯一</li>
<li>原则： map()遍历谁，就给谁添加key属性</li>
</ul>
<p><strong>列表渲染</strong></p>
<h4 data-id="heading-10">7， 总结</h4>
<p>1, JSX 是React的核心内容</p>
<p>2, JSX表示在JS代码中写HTML结构，是React声明式的体现</p>
<p>3, 使用JSX配合嵌入的JS表达式，条件渲染，列表渲染，可以描述任意UI结构</p>
<p>4, 推荐使用className的方式给JSX添加样式</p>
<p>5, React 完全利用JS语言自身的能力来编写UI，而不是造轮子增强HTML功能</p></div>  
</div>
            