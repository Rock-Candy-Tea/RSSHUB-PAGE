
---
title: '手摸手教你用qiankun开发微前端项目（一）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26e2daab5b31429fa2d629dc8419c22c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 21:55:10 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26e2daab5b31429fa2d629dc8419c22c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>  在做中后台的前端时，经常会遇到这样的痛点：</p>
<p>（1）中后台的系统很多，功能上比较独立，但是运营人员在使用的时候还是希望统一入口。这样多个项目就不得不在一个仓库中来维护，久而久之，项目代码就会变得越来越庞大，难以管理。<br>
（2）涉及到基础组建的升级，由于多个项目可能用到的都是同一个基础组件，所以不得不所有项目都对组件的升级做适配后，新组件才能被使用，不太灵活。<br>
（3）有时我们想把不同技术栈的项目整合到一个前端入口页面中。</p>
<p>  所以，我们可以通过微前端的思想来解决，微前端可以把每个系统拆成独立的服务，有自己独立的仓库，最后通过一个基座项目来在各个独立的子项目之间切换，并且可以给用户类似于一个单页面应用的顺滑体验。</p>
<p>  效果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26e2daab5b31429fa2d629dc8419c22c~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-06-13 下午2.05.20.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>  下面我们就通过从0到1的搭建和部署一个极简微前端架构的过程，手把手教大家如何使用微前端。本文将会分两个流程来讲解：1.开发流程。2.部署流程。每个流程分三个步骤来介绍：1.基座项目。2.react子系统。3.vue子系统。</p>
<h1 data-id="heading-0">开发流程</h1>
<h2 data-id="heading-1">基座项目</h2>
<p>  主应用（基座）不限技术栈，只需要提供一个容器 DOM，然后注册微应用并 start 即可。先安装 qiankun ：</p>
<pre><code class="copyable">$ yarn add qiankun # 或者 npm i qiankun -S
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  然后写打包入口文件index.js:
文件开头我们需要引入qiankun的一些库函数，引入主应用的样式文件和render函数。</p>
<pre><code class="hljs language-d copyable" lang="d"><span class="hljs-comment">// index.js</span>

<span class="hljs-keyword">import</span> &#123; registerMicroApps, runAfterFirstMounted, setDefaultMountApp, start, initGlobalState &#125; from <span class="hljs-string">'qiankun'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'./index.less'</span>;

<span class="hljs-comment">/**
 * 主应用 **可以使用任意技术栈**
 * 以下分别是 React 和 Vue 的示例，可切换尝试
 */</span>
<span class="hljs-keyword">import</span> render from <span class="hljs-string">'./render/ReactRender'</span>;
<span class="hljs-comment">// import render from './render/VueRender';</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  插一小段来介绍一下render函数，这里render函数可以使用react也可以使用vue，两种写法如下：</p>
<pre><code class="hljs language-d copyable" lang="d"><span class="hljs-comment">// render/ReactRender.jsx </span>

<span class="hljs-keyword">import</span> React from <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> ReactDOM from <span class="hljs-string">'react-dom'</span>;

<span class="hljs-comment">/**
 * 渲染子应用
 */</span>
<span class="hljs-built_in">function</span> Render(props) &#123;
  <span class="hljs-keyword">const</span> &#123; loading &#125; = props;

  <span class="hljs-keyword">return</span> (
    <>
      &#123;loading && <h4 className=<span class="hljs-string">"subapp-loading"</span>>Loading...</h4>&#125;
      <div id=<span class="hljs-string">"subapp-viewport"</span> />
    </>
  );
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-built_in">function</span> render(&#123; loading &#125;) &#123;
  <span class="hljs-keyword">const</span> container = document.getElementById(<span class="hljs-string">'subapp-container'</span>);
  ReactDOM.render(<Render loading=&#123;loading&#125; />, container);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-d copyable" lang="d"><span class="hljs-comment">// render/VueRender.js</span>

<span class="hljs-keyword">import</span> Vue from <span class="hljs-string">'vue/dist/vue.esm'</span>;

<span class="hljs-built_in">function</span> vueRender(&#123; loading &#125;) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-keyword">template</span>: <span class="hljs-string">`
      <div id="subapp-container">
        <h4 v-if="loading" class="subapp-loading">Loading...</h4>
        <div id="subapp-viewport"></div>
      </div>
    `</span>,
    el: <span class="hljs-string">'#subapp-container'</span>,
    data() &#123;
      <span class="hljs-keyword">return</span> &#123;
        loading,
      &#125;;
    &#125;,
  &#125;);
&#125;

let app = <span class="hljs-literal">null</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-built_in">function</span> render(&#123; loading &#125;) &#123;
  <span class="hljs-keyword">if</span> (!app) &#123;
    app = vueRender(&#123; loading &#125;);
  &#125; <span class="hljs-keyword">else</span> &#123;
    app.loading = loading;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  这里渲染函数的功能就是，定义出子系统挂载的元素：id='subapp-viewport'。并且在子系统真正挂载到目标元素之前，渲染loading状态。这里两个应用所挂载到的元素为id='subapp-container'，是在html模版中定义的：</p>
<pre><code class="hljs language-d copyable" lang="d"><span class="hljs-comment">//index.html</span>

<!DOCTYPE html>
<html lang=<span class="hljs-string">"en"</span>>

<head>
  <meta charset=<span class="hljs-string">"UTF-8"</span>>
  <title>全栈编程</title>
</head>

<<span class="hljs-keyword">body</span>>
  <div <span class="hljs-keyword">class</span>=<span class="hljs-string">"mainapp"</span>>
    <!-- 标题栏 -->
    <header <span class="hljs-keyword">class</span>=<span class="hljs-string">"mainapp-header"</span>>
      <h1>全栈编程</h1>
    </header>
    <div <span class="hljs-keyword">class</span>=<span class="hljs-string">"mainapp-main"</span>>
      <!-- 侧边栏 -->
      <ul <span class="hljs-keyword">class</span>=<span class="hljs-string">"mainapp-sidemenu"</span>>
        <li onclick=<span class="hljs-string">"push('/reactapp')"</span>>reactapp</li>
        <li onclick=<span class="hljs-string">"push('/vue')"</span>>Vue</li>
      </ul>
      <!-- 子应用  -->
      <main id=<span class="hljs-string">"subapp-container"</span>></main>
    </div>
  </div>
  
  <script>
    <span class="hljs-built_in">function</span> push(subapp) &#123; history.pushState(<span class="hljs-literal">null</span>, subapp, subapp) &#125;
  </script>
</<span class="hljs-keyword">body</span>>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  两个render函数中的app会挂载到“子应用”元素之中。样式如下：</p>
<pre><code class="hljs language-d copyable" lang="d"><span class="hljs-comment">// index.less</span>

<span class="hljs-comment">// 主应用慎用 reset 样式</span>
<span class="hljs-keyword">body</span> &#123;
  margin: <span class="hljs-number">0</span>;
&#125;

.mainapp &#123;
  <span class="hljs-comment">// 防止被子应用的样式覆盖</span>
  font-family: -apple-system, BlinkMacSystemFont, Segoe UI, PingFang SC, Hiragino Sans GB, Microsoft YaHei, Helvetica Neue, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol;
  line-height: <span class="hljs-number">1</span>;
&#125;

.mainapp-header &#123;
  >h1 &#123;
    color: #<span class="hljs-number">333</span>;
    font-size: <span class="hljs-number">36</span>px;
    font-weight: <span class="hljs-number">700</span>;
    margin: <span class="hljs-number">0</span>;
    padding: <span class="hljs-number">36</span>px;
  &#125;
&#125;

.mainapp-main &#123;
  display: flex;

  .mainapp-sidemenu &#123;
    width: <span class="hljs-number">130</span>px;
    list-style: none;
    margin: <span class="hljs-number">0</span>;
    margin-left: <span class="hljs-number">40</span>px;
    padding: <span class="hljs-number">0</span>;
    border-right: <span class="hljs-number">2</span>px solid #aaa;

    >li &#123;
      color: #aaa;
      margin: <span class="hljs-number">20</span>px <span class="hljs-number">0</span>;
      font-size: <span class="hljs-number">18</span>px;
      font-weight: <span class="hljs-number">400</span>;
      cursor: pointer;

      &:hover &#123;
        color: #<span class="hljs-number">444</span>;
      &#125;

      &:first-child &#123;
        margin-top: <span class="hljs-number">5</span>px;
      &#125;
    &#125;
  &#125;
&#125;

<span class="hljs-comment">// 子应用区域</span>
#subapp-container &#123;
  flex-grow: <span class="hljs-number">1</span>;
  position: relative;
  margin: <span class="hljs-number">0</span> <span class="hljs-number">40</span>px;

  .subapp-loading &#123;
    color: #<span class="hljs-number">444</span>;
    font-size: <span class="hljs-number">28</span>px;
    font-weight: <span class="hljs-number">600</span>;
    text-<span class="hljs-keyword">align</span>: center;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>  由于我们在主应用中使用的是react方式，所以还需要install相关的包：</p>
<pre><code class="hljs language-d copyable" lang="d">npm install react react-dom -S
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  整个package.json文件如下,可以参考：</p>
<pre><code class="hljs language-d copyable" lang="d"><span class="hljs-comment">//package.json</span>

&#123;
  <span class="hljs-string">"name"</span>: <span class="hljs-string">"main"</span>,
  <span class="hljs-string">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-string">"description"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-string">"main"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"start"</span>: <span class="hljs-string">"webpack-dev-server"</span>,
    <span class="hljs-string">"test"</span>: <span class="hljs-string">"echo \"Error: no test specified\" && exit 1"</span>
  &#125;,
  <span class="hljs-string">"author"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-string">"devDependencies"</span>: &#123;
    <span class="hljs-string">"@babel/core"</span>: <span class="hljs-string">"^7.7.2"</span>,
    <span class="hljs-string">"@babel/plugin-transform-react-jsx"</span>: <span class="hljs-string">"^7.7.0"</span>,
    <span class="hljs-string">"@babel/preset-env"</span>: <span class="hljs-string">"^7.7.1"</span>,
    <span class="hljs-string">"babel-loader"</span>: <span class="hljs-string">"^8.0.6"</span>,
    <span class="hljs-string">"css-loader"</span>: <span class="hljs-string">"^3.2.0"</span>,
    <span class="hljs-string">"html-webpack-plugin"</span>: <span class="hljs-string">"^3.2.0"</span>,
    <span class="hljs-string">"less-loader"</span>: <span class="hljs-string">"^6.2.0"</span>,
    <span class="hljs-string">"style-loader"</span>: <span class="hljs-string">"^1.0.0"</span>,
    <span class="hljs-string">"webpack"</span>: <span class="hljs-string">"^4.41.2"</span>,
    <span class="hljs-string">"webpack-cli"</span>: <span class="hljs-string">"^3.3.10"</span>,
    <span class="hljs-string">"webpack-dev-server"</span>: <span class="hljs-string">"^3.9.0"</span>,
    <span class="hljs-string">"cross-env"</span>: <span class="hljs-string">"^7.0.2"</span>
  &#125;,
  <span class="hljs-string">"dependencies"</span>: &#123;
    <span class="hljs-string">"qiankun"</span>: <span class="hljs-string">"^2.4.1"</span>,
    <span class="hljs-string">"react"</span>: <span class="hljs-string">"^16.13.1"</span>,
    <span class="hljs-string">"react-dom"</span>: <span class="hljs-string">"^16.13.1"</span>,
    <span class="hljs-string">"vue"</span>: <span class="hljs-string">"^2.6.11"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  下面我们再回来说最重要的入口文件index.js，引入必要的包和函数后，第一步需要先加载loading状态和定义loader函数:</p>
<pre><code class="hljs language-d copyable" lang="d"><span class="hljs-comment">//index.js</span>

<span class="hljs-comment">/**
 * Step1 初始化应用（可选）
 */</span>
render(&#123; loading: <span class="hljs-literal">true</span> &#125;);

<span class="hljs-keyword">const</span> loader = loading => render(&#123; loading &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  第二步通过registerMicroApps注册子应用，其中参数有子系统名称、入口，由于我们在开发流程中是分多个端口起的服务，所以开发阶段分别定为3000端口和9000端口。container即为上面render函数定义的渲染子系统的id。loader即为所定义的render函数，有一个参数为是否正在加载。activeRule即为激活子系统的路由。</p>
<pre><code class="hljs language-d copyable" lang="d"><span class="hljs-comment">//index.js</span>

<span class="hljs-comment">/**
 * Step2 注册子应用
 */</span>
registerMicroApps(
  [
    &#123;
      name: <span class="hljs-string">'reactapp'</span>,
      <span class="hljs-comment">// entry: '/child/reactapp/',</span>
      entry: <span class="hljs-string">'http://localhost:3000'</span>,
      container: <span class="hljs-string">'#subapp-viewport'</span>,
      loader,
      activeRule: <span class="hljs-string">'/reactapp'</span>,
    &#125;,
    &#123;
      name: <span class="hljs-string">'vue'</span>,
      <span class="hljs-comment">// entry: '/child/vue/',</span>
      entry: <span class="hljs-string">'http://localhost:9000'</span>,
      container: <span class="hljs-string">'#subapp-viewport'</span>,
      loader,
      activeRule: <span class="hljs-string">'/vue'</span>,
    &#125;
  ],
  &#123;
    beforeLoad: [
      app => &#123;
        console.log(<span class="hljs-string">'[LifeCycle] before load %c%s'</span>, <span class="hljs-string">'color: green;'</span>, app.name);
      &#125;,
    ],
    beforeMount: [
      app => &#123;
        console.log(<span class="hljs-string">'[LifeCycle] before mount %c%s'</span>, <span class="hljs-string">'color: green;'</span>, app.name);
      &#125;,
    ],
    afterUnmount: [
      app => &#123;
        console.log(<span class="hljs-string">'[LifeCycle] after unmount %c%s'</span>, <span class="hljs-string">'color: green;'</span>, app.name);
      &#125;,
    ],
  &#125;,
);

<span class="hljs-keyword">const</span> &#123; onGlobalStateChange, setGlobalState &#125; = initGlobalState(&#123;
  user: <span class="hljs-string">'qiankun'</span>,
&#125;);

onGlobalStateChange((value, prev) => console.log(<span class="hljs-string">'[onGlobalStateChange - master]:'</span>, value, prev));

setGlobalState(&#123;
  ignore: <span class="hljs-string">'master'</span>,
  user: &#123;
    name: <span class="hljs-string">'master'</span>,
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  第三步为设置默认激活的子系统：</p>
<pre><code class="copyable">//index.js

/**
 * Step3 设置默认进入的子应用
 */
setDefaultMountApp('reactapp');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  第四步调用start(),并且设置runAfterFirstMounted钩子：</p>
<pre><code class="copyable">//index.js

/**
 * Step4 启动应用
 */
start();

runAfterFirstMounted(() => &#123;
  console.log('[MainApp] first app mounted');
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下一篇，我们继续讲解如何配置react子系统。</p></div>  
</div>
            