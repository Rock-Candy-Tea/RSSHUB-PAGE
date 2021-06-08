
---
title: '记录一些React笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8382'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 05:33:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=8382'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">React 笔记</h1>
<h3 data-id="heading-1">React 简介</h3>
<h4 data-id="heading-2">React 的特点</h4>
<pre><code class="copyable">1. 声明式编码
2. 组件化编码
3. React Native 编写原生应用
4. 高效（优秀的Diffing算法）
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">React 高效的原因</h4>
<pre><code class="copyable">1. 使用虚拟DOM，不总是直接操作页面真实DOM
2. DOM Diffing算法，最小化页面重绘
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">虚拟 DOM 与真实 DOM</h4>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-number">1.</span> React 提供了一些 API 来创建一种“特别”的一般js对象
<span class="hljs-keyword">const</span> VDOM = React.createElement(<span class="hljs-string">'xx'</span>, &#123;<span class="hljs-attr">id</span>: <span class="hljs-string">'xx'</span>&#125;, <span class="hljs-string">'xx'</span>);
<span class="hljs-number">2.</span> 虚拟 DOM 对象最终都会被 React 转换为真实的 DOM
<span class="hljs-number">3.</span> 我们编码时基本只需要操作 react 的虚拟 DOM 相关数据，react 会转换为真实 DOM 变化而更新界面
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">React JSX</h4>
<h5 data-id="heading-6">JSX</h5>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-number">1.</span> 全称：JavaScript XML
<span class="hljs-number">2.</span> react 定义的一种类似于 XML 的 JS 扩展语法：JS + XML 本质是
React.createElement(component, props, ...children)方法的语法糖
<span class="hljs-number">3.</span> 作用：用来简化创建虚拟 DOM
<span class="hljs-number">1</span>). 写法： <span class="hljs-keyword">var</span> ele = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello JSX!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
    <span class="hljs-number">2</span>). 注意<span class="hljs-number">1</span>：它不是字符串，也不是 HTML/XML 标签
    <span class="hljs-number">3</span>). 注意<span class="hljs-number">2</span>：它最终产生的就是一个 JS 对象
<span class="hljs-number">4.</span> 标签名任意：HTML 标签或其他标签
<span class="hljs-number">5.</span> 标签属性任意：HTML 标签属性或其他
<span class="hljs-number">6.</span> 基本语法规则
    <span class="hljs-number">1</span>). 遇到 <开头的代码, 以标签的语法解析: html同名标签转换为html同名元素, 其它标签需要特别解析
    <span class="hljs-number">2</span>).遇到以 &#123; 开头的代码，以JS语法解析: 标签中的js表达式必须用&#123; &#125;包含
<span class="hljs-number">7.</span> babel.js的作用
    <span class="hljs-number">1</span>).浏览器不能直接解析JSX代码, 需要babel转译为纯JS的代码才能运行
    <span class="hljs-number">2</span>).只要用了JSX，都要加上type=<span class="hljs-string">"text/babel"</span>, 声明需要babel来处理
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">渲染虚拟 DOM（元素）</h4>
<pre><code class="copyable">1. 语法：ReactDOM.render(virtualDOM, containerDOM);
2. 作用：将虚拟 DOM 元素渲染到页面中的真实容器 DOM 中显示
3. 参数说明：
1). 参数一：纯 js 或 jsx 创建的虚拟 dom 对象
2). 参数二：用来包含 DOM 元素的真实 dom 元素对象（一般是一个div）
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">事件处理</h4>
<pre><code class="copyable">1. 通过 onXxx（列如：onClick） 属性指定事件处理函数（注意大小写）
1). React 使用的是自定义（合成）事件，而不是使用的原生 DOM 事件（原生例如：onclick）----- 为了更好的兼容性
2). React 中的事件是通过事件委托方式处理的（委托给组件最外层的元素）----- 为了高效
2. 通过 event.target 得到发生事件的 DOM 元素对象
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">React 面向组件编程</h3>
<h4 data-id="heading-10">渲染类组件标签的基本流程</h4>
<pre><code class="copyable">1. React 内部会创建组件实例对象
2. 调用 render() 得到虚拟 DOM，并解析为真实 DOM
3. 插入到指定的页码元素内部
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">组件的三大核心属性</h4>
<h5 data-id="heading-12">state</h5>
<pre><code class="copyable">// 理解
1. state 是组件对象最重要的属性，值是对象（可以包含多个 key-value的组合）
2. 组件被称为“状态机”，通过更新组件的 state 来更新对应的页面显示（重新渲染组件）

// 强烈注意
1. 组件中 render 方法中的 this 为组件实例对象
2. 组件自定义的方法中 this 为 undefined，如何解决？
1). 强制绑定 this：通过函数对象的 bind()
2). 箭头函数
3. 状态数据，不能直接修改或更新
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-13">props</h5>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 理解</span>
<span class="hljs-number">1.</span> 每个组件对象都会有 props(properties的简写)属性
<span class="hljs-number">2.</span> 组件标签的所有属性都保存在 props 中

<span class="hljs-comment">// 作用</span>
<span class="hljs-number">1.</span> 通过标签属性从组件外向组件内部传递变化的数据
<span class="hljs-number">2.</span> 注意：组件内部不要修改 props 数据

<span class="hljs-comment">// 编码操作</span>
<span class="hljs-number">1.</span> 内部读取某个属性值
<span class="hljs-built_in">this</span>.props.name
<span class="hljs-number">2.</span> 对 props 中的属性值进行类型限制和必要性限制
<span class="hljs-number">1</span>). 第一种方式(React v15<span class="hljs-number">.5</span> 开始已弃用)
Person.propTypes = &#123;
<span class="hljs-attr">name</span>: React.PropTypes.string.isRequired,
        <span class="hljs-attr">age</span>: React.PropTypes.number
    &#125;
<span class="hljs-number">2</span>). 第二种方式（新）：使用 prop-types 库进行限制（需要引入 prop-types 库）
    Person.propTypes = &#123;
<span class="hljs-attr">name</span>: PropTypes.string.isRequired,
        <span class="hljs-attr">age</span>: PropTypes.number
    &#125;
<span class="hljs-number">3.</span>扩展属性：将对象的所有属性通过 porps 传递
<Person &#123;...person&#125; />
<span class="hljs-number">4.</span> 默认属性值
Person.propTypes = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'略略略'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>
&#125;
<span class="hljs-number">5.</span> 组件类的构造函数
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14">refs</h5>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 理解</span>
组件内的标签可以定义 ref 属性来标识自己

<span class="hljs-comment">// 编码</span>
<span class="hljs-number">1.</span> 字符串形式的 ref
<input ref=<span class="hljs-string">"input1"</span> />
取值：<span class="hljs-built_in">this</span>.refs.inputVal.value

<span class="hljs-number">2.</span> 回调形式的 ref
<input ref=&#123;<span class="hljs-function"><span class="hljs-params">val</span> =></span> <span class="hljs-built_in">this</span>.inputVal = val&#125; />
取值：<span class="hljs-built_in">this</span>.inputVal.value

<span class="hljs-number">3.</span> createRef 创建 ref 容器
myRef = React.createRef()
<input ref=&#123;<span class="hljs-built_in">this</span>.myRef&#125; />
取值：<span class="hljs-built_in">this</span>.myRef.current.value

<span class="hljs-comment">// 注意点</span>
通过 event.target 得到发生事件的 DOM 元素对象 ----- 不要过度使用 ref
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">组件的声明周期</h3>
<h4 data-id="heading-16">理解</h4>
<pre><code class="copyable">1. 组件从创建到死亡它会进行一些特定的阶段
2. React 组件中包含一系列钩子函数（生命周期回调函数），会在特定的时刻调用
3. 我们在定义组件时，会在特定的生命周期回调函数中，做特定的工作
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">生命周期（旧）</h4>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 声明周期的三个阶段（旧）</span>
<span class="hljs-number">1.</span> 初始化阶段：由 ReactDOM.render() 触发 ----- 初次渲染
<span class="hljs-number">1</span>). <span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)
2). <span class="hljs-title">componentWillMount</span>(<span class="hljs-params"></span>)
3). <span class="hljs-title">render</span>(<span class="hljs-params"></span>)
4). <span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)
2. 更新阶段：由组件内部 <span class="hljs-title">this</span>.<span class="hljs-title">setState</span>(<span class="hljs-params"></span>) 或父组件重新 <span class="hljs-title">render</span> 触发
1). <span class="hljs-title">shouldComponentUpdate</span>(<span class="hljs-params"></span>)
2). <span class="hljs-title">componentWillUpdate</span>(<span class="hljs-params"></span>)
3). <span class="hljs-title">render</span>(<span class="hljs-params"></span>)
4). <span class="hljs-title">componentDidUpdate</span>(<span class="hljs-params"></span>)
3. 卸载组件：由 <span class="hljs-title">ReactDOM</span>.<span class="hljs-title">umountComponentAtNode</span>(<span class="hljs-params"></span>) 触发
1). <span class="hljs-title">componentWillUnmount</span>(<span class="hljs-params"></span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">生命周期（新）</h4>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 生命周期的三个阶段（新）</span>
<span class="hljs-number">1.</span> 初始化阶段：由 ReactDOM.render() 触发 ----- 初次渲染
<span class="hljs-number">1</span>). <span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)
2). <span class="hljs-title">getDerivedStateFromProps</span>
    3). <span class="hljs-title">render</span>(<span class="hljs-params"></span>)
4). <span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)
2. 更新阶段：由组件内部 <span class="hljs-title">this</span>.<span class="hljs-title">setState</span>(<span class="hljs-params"></span>) 或父组件重新 <span class="hljs-title">render</span> 触发
1). <span class="hljs-title">getDerivedStateFromProps</span>
    2). <span class="hljs-title">shouldComponentUpdate</span>(<span class="hljs-params"></span>)
3). <span class="hljs-title">render</span>(<span class="hljs-params"></span>)
4). <span class="hljs-title">getSnapshotBeforeUpdate</span>
    5). <span class="hljs-title">componentDidUpdate</span>(<span class="hljs-params"></span>)
3. 卸载组件：由 <span class="hljs-title">ReactDOM</span>.<span class="hljs-title">unmountComponentAtNode</span>(<span class="hljs-params"></span>) 触发
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">重要的钩子</h4>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-number">1.</span> render：初始化渲染或更新渲染调用
<span class="hljs-number">2.</span> componentDidMount：开启监听，发送 ajax 请求
<span class="hljs-number">3.</span> componentWillUnmount：做一些收尾工作，如：清理定时器
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">即将废弃的钩子</h4>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-number">1.</span> componentWillMount
<span class="hljs-number">2.</span> componentWillReceiveProps
<span class="hljs-number">3.</span> componentWillUpdate
现在使用会出现警告，下一个大版本需要加上 UNSAFE_ 前缀才能使用，以后可能会被彻底废弃，不建议使用
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">React 应用(基于React脚手架)</h3>
<h4 data-id="heading-22">react 脚手架</h4>
<pre><code class="copyable">1. 脚手架：用来帮助程序员快速创建一个基于 xxx 库的模板项目
1). 包含了所有需要的配置（语法检查、jsx编译、devServer...）
2). 下载好了所有相关的依赖
3). 可以直接运行一个简单效果
2. react 提供了一个用于创建 react 项目的脚手架库：create-react-app
3. 项目的整体技术架构为：react + webpack + es6 + eslint
4. 使用脚手架开发的项目的特点：模块化，组件化，工程化
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23">创建项目并启动</h4>
<pre><code class="copyable">第一步：全局安装：npm i -g create-react-app
第二步：切换到想要创建项目的目录，使用命令：npx create-react-app hello-react
第三步：进入项目文件夹：cd hello-react
第四步：启动项目：npm start
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24">react 脚手架项目结构</h4>
<pre><code class="hljs language-jsx copyable" lang="jsx">public ---- 静态资源文件夹
favicon.icon ------ 网站页签图标
index.html -------- 主页面
logo192.png ------- logo图
logo512.png ------- logo图
manifest.json ----- 应用加壳的配置文件
robots.txt -------- 爬虫协议文件
src ---- 源码文件夹
App.css -------- App组件的样式
App.js --------- App组件
App.test.js ---- 用于给App做测试
index.css ------ 样式
index.js ------- 入口文件
logo.svg ------- logo图
reportWebVitals.js --- 页面性能分析文件(需要web-vitals库的支持)
setupTests.js ---- 组件单元测试的文件(需要jest-dom库的支持)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">React ajax</h3>
<h4 data-id="heading-26">理解</h4>
<h5 data-id="heading-27">前置说明</h5>
<pre><code class="copyable">1. React 本身只关注于界面，并不包含发送 ajax 请求的代码
2. 前端应用需要通过 ajax 请求与后台进行交互（json数据）
3. react 应用中需要集成第三方 ajax 库（或自己封装）
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-28">常用的 ajax 请求库</h5>
<pre><code class="copyable">1. jQuery：比较重，如果需要另外引入不建议使用
2. axios：轻量级，建议使用
1). 封装 XMLHttpRequest 对象的 ajax
2). promise 风格
3). 可以用在浏览器端和 node 服务器端
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-29">axios</h4>
<h5 data-id="heading-30">GET 请求</h5>
<pre><code class="hljs language-jsx copyable" lang="jsx">axios.get(<span class="hljs-string">'/user?ID=12345'</span>)
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">response</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(response.data);
  &#125;)
  .catch(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(error);
  &#125;);

axios.get(<span class="hljs-string">'/user'</span>, &#123;
    <span class="hljs-attr">params</span>: &#123;
      <span class="hljs-attr">ID</span>: <span class="hljs-number">12345</span>
    &#125;
  &#125;)
  .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">response</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(response);
  &#125;)
  .catch(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(error);
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-31">POST 请求</h5>
<pre><code class="hljs language-jsx copyable" lang="jsx">axios.post(<span class="hljs-string">'/user'</span>, &#123;
  <span class="hljs-attr">firstName</span>: <span class="hljs-string">'Fred'</span>,
  <span class="hljs-attr">lastName</span>: <span class="hljs-string">'Flintstone'</span>
&#125;)
.then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">response</span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(response);
&#125;)
.catch(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(error);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-32">扩展：Fetch</h4>
<h5 data-id="heading-33">特点</h5>
<pre><code class="copyable">1. fetch：原生函数，不再使用 XMLHttpRequest 对象提交 ajax 请求
2. 老版本浏览器可能不支持
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-34">GET 请求</h5>
<pre><code class="hljs language-jsx copyable" lang="jsx">fetch(url).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">response</span>) </span>&#123;
    <span class="hljs-keyword">return</span> response.json()
  &#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(data)
  &#125;).catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(e)
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-35">POST 请求</h5>
<pre><code class="hljs language-jsx copyable" lang="jsx">fetch(url, &#123;
    <span class="hljs-attr">method</span>: <span class="hljs-string">"POST"</span>,
    <span class="hljs-attr">body</span>: <span class="hljs-built_in">JSON</span>.stringify(data),
  &#125;).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">data</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(data)
  &#125;).catch(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(e)
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-36">React 路由</h3>
<h4 data-id="heading-37">SPA 的理解</h4>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-number">1.</span> 单页 Web 应用 （single page web application, SPA）
<span class="hljs-number">2.</span> 整个应用只有一个完整的页面
<span class="hljs-number">3.</span> 点击页面中的连接不会刷新页面，只会做页面的局部更新
<span class="hljs-number">4.</span> 数据都需要通过 ajax 请求获取，并在前端异步展现
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-38">路由的理解</h4>
<h5 data-id="heading-39">什么是路由？</h5>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-number">1.</span> 一个路由就是一个映射关系（key: value）
<span class="hljs-number">2.</span> key 为路径，value 可能是 <span class="hljs-function"><span class="hljs-keyword">function</span> 或 <span class="hljs-title">component</span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-40">路由分类</h5>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-number">1.</span> 后端路由：
<span class="hljs-number">1</span>). 理解：value 是 <span class="hljs-function"><span class="hljs-keyword">function</span>，用来处理客户端提交的请求
    2). 注册路由：<span class="hljs-title">router</span>.<span class="hljs-title">get</span>(<span class="hljs-params">path, <span class="hljs-keyword">function</span>(req, res)</span>)
    3). 工作过程：当 <span class="hljs-title">node</span> 接收到一个请求时，根据请求路径找到匹配的路由，调用路由中的函数来处理请求，返回响应数据
2. 前端路由：
1). 浏览器端路由，<span class="hljs-title">value</span> 是 <span class="hljs-title">component</span>，用于展示页面内容
    2). 注册路由：<<span class="hljs-title">Route</span> <span class="hljs-title">path</span>="/<span class="hljs-title">test</span>" <span class="hljs-title">component</span>=</span>&#123;Test&#125; />
    <span class="hljs-number">3</span>). 工作过程：当浏览器的 path 变为 /test 时，当前路由组件就会变为 Test 组件    
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-41">react-router-dom 的理解</h4>
<pre><code class="copyable">1. react 的一个插件库
2. 专门用来实现一个 SPA 应用
3. 基于 react 的项目基本都会用到此库
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-42">react-router-dom 相关 API</h4>
<h5 data-id="heading-43">内置组件</h5>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-number">1.</span> <BrowserRouter>
<span class="hljs-number">2.</span><HashRouter>
<span class="hljs-number">3.</span><Route>
<span class="hljs-number">4.</span><Redirect>
<span class="hljs-number">5.</span><Link>
<span class="hljs-number">6.</span><NavLink>
<span class="hljs-number">7.</span><Switch>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-44">其他</h5>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-number">1.</span>history对象
<span class="hljs-number">2.</span>match对象
<span class="hljs-number">3.</span>withRouter函数
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-45">路由的基本使用</h4>
<h5 data-id="heading-46">准备</h5>
<pre><code class="copyable">下载 react-router-dom: npm install --save react-router-dom
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-47">状态管理</h2>
<h4 data-id="heading-48">状态管理目录结构</h4>
<pre><code class="hljs language-jsx copyable" lang="jsx">文件夹目录
<span class="hljs-comment">//状态管理根目录</span>
redux
<span class="hljs-comment">//存放各种action对象</span>
actions
    test1.js<span class="hljs-comment">//对象1</span>
test1.js<span class="hljs-comment">//对象2</span>
<span class="hljs-comment">//用于初始化状态、加工状态</span>
reducers
    index.js<span class="hljs-comment">//该文件用于汇总所有的reducer为一个总的reducer</span>
test1.js<span class="hljs-comment">//存放的信息1</span>
test2.js<span class="hljs-comment">//存放的信息2</span>
<span class="hljs-comment">//该模块是用于定义action对象中type类型的常量值，目的只有一个：便于管理的同时防止程序员单词写错</span>
constant.js
<span class="hljs-comment">//redux 库最核心的管理对象</span>
store.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-49">store.js 的配置</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/** 该文件专门用于暴露一个store对象，整个应用只有一个store对象 */</span>

<span class="hljs-comment">//引入createStore，专门用于创建redux中最为核心的store对象</span>
<span class="hljs-keyword">import</span> &#123;createStore,applyMiddleware&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux'</span>
<span class="hljs-comment">//引入汇总之后的reducer</span>
<span class="hljs-keyword">import</span> reducer <span class="hljs-keyword">from</span> <span class="hljs-string">'./reducers'</span>
<span class="hljs-comment">//引入redux-thunk，用于支持异步action </span>
<span class="hljs-comment">//需要安装：npm i redux-thunk</span>
<span class="hljs-keyword">import</span> thunk <span class="hljs-keyword">from</span> <span class="hljs-string">'redux-thunk'</span>
<span class="hljs-comment">//引入redux-devtools-extension</span>
<span class="hljs-comment">//需要安装：npm i redux-devtools-extension</span>
<span class="hljs-keyword">import</span> &#123;composeWithDevTools&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux-devtools-extension'</span>

<span class="hljs-comment">//暴露store </span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> createStore(reducer,composeWithDevTools(applyMiddleware(thunk)))
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-50">constant.js 的配置</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* 该模块是用于定义action对象中type类型的常量值，目的只有一个：便于管理的同时防止程序员单词写错 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> TEST1 = <span class="hljs-string">'test1'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> TEST2 = <span class="hljs-string">'test2'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> TEST3 = <span class="hljs-string">'test3'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-51">action 中的每一个 对象js 配置</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* 
该文件专门为Count组件生成action对象
*/</span>
<span class="hljs-keyword">import</span> &#123;INCREMENT,DECREMENT&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../constant'</span>

<span class="hljs-comment">//同步action，就是指action的值为Object类型的一般对象</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> increment = <span class="hljs-function"><span class="hljs-params">data</span> =></span> (&#123;<span class="hljs-attr">type</span>:INCREMENT,data&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> decrement = <span class="hljs-function"><span class="hljs-params">data</span> =></span> (&#123;<span class="hljs-attr">type</span>:DECREMENT,data&#125;)

<span class="hljs-comment">//异步action，就是指action的值为函数,异步action中一般都会调用同步action，异步action不是必须要用的。</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> incrementAsync = <span class="hljs-function">(<span class="hljs-params">data,time</span>) =></span> &#123;
<span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">dispatch</span>)=></span>&#123;
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
dispatch(increment(data))
&#125;,time)
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-52">reducers 中的文件</h4>
<h5 data-id="heading-53">index.js 的配置</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* 
该文件用于汇总所有的reducer为一个总的reducer
*/</span>
<span class="hljs-comment">//引入combineReducers，用于汇总多个reducer</span>
<span class="hljs-keyword">import</span> &#123;combineReducers&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux'</span>
<span class="hljs-comment">//引入为Count组件服务的reducer</span>
<span class="hljs-keyword">import</span> count <span class="hljs-keyword">from</span> <span class="hljs-string">'./count'</span>
<span class="hljs-comment">//引入为Person组件服务的reducer</span>
<span class="hljs-keyword">import</span> persons <span class="hljs-keyword">from</span> <span class="hljs-string">'./person'</span>

<span class="hljs-comment">//汇总所有的reducer变为一个总的reducer</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>  combineReducers(&#123;
count,
persons
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-54">其他的reducer 的配置</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* 
1.该文件是用于创建一个为Count组件服务的reducer，reducer的本质就是一个函数
2.reducer函数会接到两个参数，分别为：之前的状态(preState)，动作对象(action)
*/</span>
<span class="hljs-keyword">import</span> &#123;INCREMENT,DECREMENT&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../constant'</span>

<span class="hljs-keyword">const</span> initState = <span class="hljs-number">0</span> <span class="hljs-comment">//初始化状态</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">countReducer</span>(<span class="hljs-params">preState=initState,action</span>)</span>&#123;
<span class="hljs-comment">// console.log('countReducer@#@#@#');</span>
<span class="hljs-comment">//从action对象中获取：type、data</span>
<span class="hljs-keyword">const</span> &#123;type,data&#125; = action
<span class="hljs-comment">//根据type决定如何加工数据</span>
<span class="hljs-keyword">switch</span> (type) &#123;
<span class="hljs-keyword">case</span> INCREMENT: <span class="hljs-comment">//如果是加</span>
<span class="hljs-keyword">return</span> preState + data
<span class="hljs-keyword">case</span> DECREMENT: <span class="hljs-comment">//若果是减</span>
<span class="hljs-keyword">return</span> preState - data
<span class="hljs-attr">default</span>:
<span class="hljs-keyword">return</span> preState
   <!-- 如果加工的是对象 可以 - &#123;...preState, ...data&#125; -->
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-55">在redux中的使用</h4>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./redux/store'</span>;
<span class="hljs-keyword">import</span> &#123; userAction1 &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./redux/actions/user1'</span>;
<span class="hljs-keyword">import</span> &#123; userAction2 &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./redux/actions/user2'</span>;



<span class="hljs-comment">//获取到存放在redux中的数据</span>
store.getState();
<span class="hljs-comment">//分发 action，触发 reducer 调用，产生新的state</span>
dispatch(action);<span class="hljs-comment">//示例：dispatch(userAction1(里面可以放需要修改的值，也可忽略))</span>
<span class="hljs-comment">//注册监听，当产生新的 state 时，自动调用</span>
subscribe(listener)
<span class="hljs-comment">//示例：store.subscribe(() => &#123;</span>
进行一些操作
    比如说可以：
<span class="hljs-built_in">this</span>.setState(&#123;&#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-56">在react-redux中的使用</h4>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">//在App.js中引入 </span>
<span class="hljs-comment">//可以不再App.js中引入 目的是包裹</span>
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./redux/store'</span>;
<span class="hljs-keyword">import</span> &#123; Provider &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-redux'</span>;
<span class="hljs-comment">//并包裹</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"App"</span>></span>
        一些组件...
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">Provider</span>></span></span>

<span class="hljs-comment">//在组件中引入</span>
<span class="hljs-keyword">import</span> &#123; connect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-redux'</span>;
<span class="hljs-comment">//暴露的方式不再是 export default class Home extends Component</span>
<span class="hljs-comment">//改成</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Home</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
    ....内容
&#125;
<span class="hljs-comment">//如果是发送action的一方</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> connect(<span class="hljs-literal">null</span>, mapDispatchToProps)(Home);
<span class="hljs-comment">//接收信息的话就是</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> connect(mapStateToProps)(Home);

<span class="hljs-comment">//两个函数的实现 - 简单示例</span>
<span class="hljs-comment">//第一个函数 - 之后在 this.props。。。。中可以看到数据</span>
<span class="hljs-keyword">const</span> mapStateToProps = <span class="hljs-function">(<span class="hljs-params">state</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> state;
&#125;
<span class="hljs-comment">//第二个函数 - 需要在其他地方调用里面的函数 sendAction， </span>
<span class="hljs-keyword">const</span> mapDispatchToProps = <span class="hljs-function">(<span class="hljs-params">dispatch</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">sendAction</span>: <span class="hljs-function">(<span class="hljs-params">这里可以带参数，比如说 value</span>) =></span> &#123;
            dispatch(&#123;
                <span class="hljs-comment">//这里的对象其实就是一个action</span>
                <span class="hljs-attr">type</span>: <span class="hljs-string">'add_action'</span>,
                <span class="hljs-attr">data</span>: <span class="hljs-number">1</span> <span class="hljs-comment">//然后在这里替换 value</span>
            &#125;)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-57">redux</h3>
<h4 data-id="heading-58">redux 理解</h4>
<h5 data-id="heading-59">redux 是什么？</h5>
<pre><code class="copyable">1. redux 是一个专门用于做状态管理的 JS 库（不是 react 插件库）
2. 它可以用在 react，angular，vue 等项目中，但基本与 react 配合使用
3. 作用：集中式管理 react 应用中多个组件共享的状态
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-60">什么情况下需要使用 redux</h5>
<pre><code class="copyable">1. 某个组件的状态，需要让他组件可以随时拿到（共享）
2. 一个组件需要改变另一个组件的状态（通信）
3. 总体原则：能不用就不用，如果不用比较吃力才考虑使用
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-61">redux 的三个核心概念</h4>
<h5 data-id="heading-62">aciton</h5>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-number">1.</span> 动作的对象
<span class="hljs-number">2.</span> 包含<span class="hljs-number">2</span>个属性：
<span class="hljs-number">1</span>). type：标识属性，值为字符串，唯一，必要属性
<span class="hljs-number">2</span>). data：数据属性，值类型任意，可选属性
<span class="hljs-number">3.</span> 例子：&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'ADD_STUDENT'</span>, <span class="hljs-attr">data</span>: &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'LueLueLue'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">20</span>&#125; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-63">reducer</h5>
<pre><code class="copyable">1. 用于初始化状态、加工状态
2. 加工时，根据旧的 state 和 action，产生新的 state 的纯函数
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-64">store</h5>
<pre><code class="copyable">1. 将 state、action、reducer 联系在一起的对象
2. 如何得到此对象？
1). import &#123; createStore &#125; from 'redux'
2). import reducer from './reducers'
3). const store = createStore(reducer)
3. 此对象的功能？
1). getState()：得到 state
2). dispatch(action)：分发 action，触发 reducer 调用，产生新的state
3). subscribe(listener)：注册监听，当产生新的 state 时，自动调用
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-65">redux 的核心 API</h4>
<h5 data-id="heading-66">createStore()</h5>
<pre><code class="copyable">作用：创建包含指定 reducer 的 store 对象
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-67">store 对象</h5>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-number">1.</span> 作用：redux 库最核心的管理对象
<span class="hljs-number">2.</span> 它内部维护着：
<span class="hljs-number">1</span>). state
<span class="hljs-number">2</span>). reducer
<span class="hljs-number">3.</span> 核心用法：
<span class="hljs-number">1</span>). getState()
<span class="hljs-number">2</span>). dispatch(action)
<span class="hljs-number">3</span>). subscribe(listener)
<span class="hljs-number">4.</span> 具体编码：
<span class="hljs-number">1</span>). store.getState()
<span class="hljs-number">2</span>). store.dispatch(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'INCREMENT'</span>, number &#125;)
<span class="hljs-number">3</span>). store.subscribe(render)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-68">applyMiddleware()</h4>
<pre><code class="copyable">作用：应用上基于 redux 的中间件(插件库)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-69">combineReducers()</h4>
<pre><code class="copyable">作用：合并多个 reducer 函数
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-70">redux 异步编程</h4>
<h5 data-id="heading-71">理解</h5>
<pre><code class="copyable">1. redux 默认时不能进行异步处理的
2. 某些时候应用中需要在 redux 中执行异步任务（ajax，定时器）
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-72">使用异步中间件</h5>
<pre><code class="copyable">npm install --save redux-thunk
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-73">react-redux</h3>
<h4 data-id="heading-74">理解</h4>
<pre><code class="copyable">1. 一个 react 插件库
2. 专门用来简化 react 应用中使用 redux
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-75">React-Redux将所有组件分成两大类</h4>
<h5 data-id="heading-76">UI组件</h5>
<pre><code class="copyable">1. 只负责 UI 的呈现，不带有任何业务逻辑
2. 通过props接收数据(一般数据和函数)
3. 不使用任何 Redux 的 API
4. 一般保存在components文件夹下
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-77">容器组件</h5>
<pre><code class="copyable">1. 负责管理数据和业务逻辑，不负责UI的呈现
2. 使用 Redux 的 API
3. 一般保存在containers文件夹下
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-78">相关 API</h4>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// Provider：让所有组件都可以得到 state 数据</span>
<Provider store=&#123;store&#125;>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span>/></span></span>
</Provider>

<span class="hljs-comment">// connect：用于包装 UI 组件生成容器组件</span>
<span class="hljs-keyword">import</span> &#123; connect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-redux'</span>;
connect(
mapStateToprops,
    mapDispatchToProps
)(Hello);

<span class="hljs-comment">// mapStateToprops：将外部的数据（即state对象）转换为UI组件的标签属性</span>
<span class="hljs-keyword">const</span> mapStateToprops = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">state</span>) </span>&#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">value</span>: state
  &#125;
&#125; 

<span class="hljs-comment">// mapDispatchToProps：将分发action的函数转换为UI组件的标签属性</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-79">使用上redux调试工具</h4>
<h5 data-id="heading-80">安装chrome浏览器插件</h5>
<pre><code class="copyable">Redux DevTools
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-81">下载工具依赖包</h5>
<pre><code class="copyable">npm install --save-dev redux-devtools-extension
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-82">纯函数和高阶函数</h3>
<h4 data-id="heading-83">纯函数</h4>
<pre><code class="copyable">1. 一类特别的函数: 只要是同样的输入(实参)，必定得到同样的输出(返回)
2. 必须遵守以下一些约束  
    1).不得改写参数数据
    2).不会产生任何副作用，例如网络请求，输入和输出设备
    3).不能调用Date.now()或者Math.random()等不纯的方法  
3. redux的reducer函数必须是一个纯函数

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-84">高阶函数</h4>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 理解: 一类特别的函数</span>
    <span class="hljs-number">1</span>)情况<span class="hljs-number">1</span>: 参数是函数
    <span class="hljs-number">2</span>)情况<span class="hljs-number">2</span>: 返回是函数
    
<span class="hljs-comment">// 常见的高阶函数: </span>
    <span class="hljs-number">1</span>)定时器设置函数
    <span class="hljs-number">2</span>)数组的forEach()/map()/filter()/reduce()/find()/bind()
    <span class="hljs-number">3</span>)promise
    <span class="hljs-number">4</span>)react-redux中的connect函数

<span class="hljs-comment">// 作用: 能实现更加动态, 更加可扩展的功能</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            