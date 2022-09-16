
---
title: 'redux在函数组件的正确进入姿势'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/667ca6688ebe4457bb8a5f741e5b5c86~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Thu, 15 Sep 2022 20:22:46 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/667ca6688ebe4457bb8a5f741e5b5c86~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:30px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:60px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:24px 0 12px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li::marker,.markdown-body ul li::marker&#123;color:#a862ea&#125;.markdown-body ol li.task-list-item,.markdown-body ul li.task-list-item&#123;list-style:none&#125;.markdown-body ol li.task-list-item ol,.markdown-body ol li.task-list-item ul,.markdown-body ul li.task-list-item ol,.markdown-body ul li.task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body a,.markdown-body code,.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6,.markdown-body li,.markdown-body p&#123;opacity:.85;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body a:hover,.markdown-body code:hover,.markdown-body h1:hover,.markdown-body h2:hover,.markdown-body h3:hover,.markdown-body h4:hover,.markdown-body h5:hover,.markdown-body h6:hover,.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:1px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;transition:transform .2s ease 0s;background-color:#f8f5ff;box-shadow:0 0 10px #e7daff&#125;.markdown-body img:hover&#123;opacity:1;box-shadow:0 0 20px #e7daff;transform:translateY(-1px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:12px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:3px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body .math&#123;font-style:italic;margin:12px 0;padding:.5em 1em;background-color:#f8f5ff&#125;.markdown-body .math>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:18px;color:#383838;border-radius:2px;scroll-behavior:smooth;box-shadow:0 0 10px #e7daff&#125;.markdown-body pre>code:hover&#123;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;width:100%;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:.5em;border:1px solid #e7daff&#125;.markdown-body tr&#123;background-color:#f8f5ff&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h2 data-id="heading-0">1.redux介绍</h2>
<p>react和vue都已经全面拥抱了hooks,想必大家在使用react函数组件的时候导入redux学习时，却发现网上的redux资料大都是基于react的类组件,这时心里会有许多蛋蛋的忧伤。不要怕，经过多方面的搜集整理，我将介绍如何在函数组件中正确使用redux,本人实力有限，如果介绍不当请多多批评。</p>
<h2 data-id="heading-1">2.redux安装和配置</h2>
<h3 data-id="heading-2">下载</h3>
<pre><code class="hljs language-css copyable" lang="css">npm <span class="hljs-selector-tag">i</span> redux
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">项目初始化</h3>
<p>store目录下创建index.js</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">import</span> &#123;legacy_createStore&#125; from <span class="hljs-string">"redux"</span>

<span class="hljs-comment">//初始的数据</span>
let <span class="hljs-built_in">num</span> = <span class="hljs-number">1</span>

<span class="hljs-comment">//reducer控制数据的修改</span>
function reducers(state=<span class="hljs-built_in">num</span>,action) &#123;
  <span class="hljs-keyword">switch</span>(action.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"add"</span>:
      <span class="hljs-keyword">return</span> state+action.<span class="hljs-built_in">num</span>
    <span class="hljs-keyword">case</span> <span class="hljs-string">"del"</span>:
      <span class="hljs-keyword">return</span> state-action.<span class="hljs-built_in">num</span>
    <span class="hljs-keyword">default</span>:<span class="hljs-keyword">return</span> state
  &#125;
&#125;

<span class="hljs-comment">//核心store</span>
<span class="hljs-keyword">const</span> store = legacy_createStore(reducers)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store

<span class="copy-code-btn">复制代码</span></code></pre>
<p>根目录下的index.js中导入store</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-title class_">React</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-title class_">ReactDOM</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom/client'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-title class_">App</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'./App'</span>;
<span class="hljs-keyword">import</span> &#123;<span class="hljs-title class_">Provider</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-redux"</span>
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">"./store/index"</span>
<span class="hljs-keyword">const</span> root = <span class="hljs-title class_">ReactDOM</span>.<span class="hljs-title function_">createRoot</span>(<span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">'root'</span>));
root.<span class="hljs-title function_">render</span>(
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">App</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">Provider</span>></span></span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用redux数据</p>
<p>函数组件中使用redux组件十分十分的简单，只需要导入useSelector就可以让redux的数据具备响应式，通过useDispatch我们可以完成redux数据的修改操作。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;useDispatch, useSelector&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-redux"</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">const</span> dispatch = <span class="hljs-title function_">useDispatch</span>()
  <span class="hljs-keyword">const</span> num = <span class="hljs-title function_">useSelector</span>(<span class="hljs-function">(<span class="hljs-params">state</span>)=></span>&#123;
    <span class="hljs-keyword">return</span> state
  &#125;)
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;num&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>dispatch(&#123;type:'add',num:1&#125;)&#125;>增加num<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>dispatch(&#123;type:'del',num:1&#125;)&#125;>减少Num<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>页面效果</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/667ca6688ebe4457bb8a5f741e5b5c86~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">3.多个reducer的问题</h2>
<p>看完上面的问题，大家感觉函数组件的redux操作是不是很简单，但是实际我们还有一部分问题没有解决，假设我们现在有多个模块的数据，例如用户信息数据，产品详情数据等。如果我们使用一个reducer函数的switch去操作redux数据，出现的问题如下代码所示，switch判断和数据变得十分臃肿，不利于代码的维护和阅读。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> data = &#123;
    <span class="hljs-attr">user</span>:&#123;&#125;,
    <span class="hljs-attr">list</span>:&#123;&#125;
&#125;
<span class="hljs-keyword">function</span> <span class="hljs-title function_">reducer</span>(<span class="hljs-params">state=data,actions</span>) &#123;
    <span class="hljs-keyword">switch</span>(actions.<span class="hljs-property">type</span>) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"xx"</span> :
        <span class="hljs-keyword">case</span> <span class="hljs-string">"xx"</span> :
        <span class="hljs-keyword">case</span> <span class="hljs-string">"xx"</span> :
        
        .....
        
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于上面的问题，我们通常需要对reducer进行拆分，通常一个模块对应一个reducer,最后我们通过api进行reducer的合并就可以了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ccfa4db87a74268bc7e78350ae2af30~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>1. store目录下新建reducer文件夹</strong></p>
<p><strong>2. reducer文件夹下存放不同的reudcer</strong></p>
<p>我们在reducer文件夹下创建了两个reducer，每个reducer都有自己的数据和自己的数据处理方法。如下</p>
<p>books.js</p>
<pre><code class="hljs language-dart copyable" lang="dart">let <span class="hljs-built_in">num</span> = <span class="hljs-number">1</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> function reducers(state=<span class="hljs-built_in">num</span>,actions) &#123;
  <span class="hljs-keyword">switch</span>(actions.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"addbook"</span>:
      <span class="hljs-keyword">return</span> state+actions.<span class="hljs-built_in">num</span>
    <span class="hljs-keyword">case</span> <span class="hljs-string">"delbook"</span>:
      <span class="hljs-keyword">return</span> state-actions.<span class="hljs-built_in">num</span>
    <span class="hljs-keyword">default</span>:
      <span class="hljs-keyword">return</span> state
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>user.js</p>
<pre><code class="hljs language-dart copyable" lang="dart">let <span class="hljs-built_in">num</span> = <span class="hljs-number">2</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> function reducers(state=<span class="hljs-built_in">num</span>,actions) &#123;
  <span class="hljs-keyword">switch</span>(actions.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"adduser"</span>:
      <span class="hljs-keyword">return</span> state+actions.<span class="hljs-built_in">num</span>
    <span class="hljs-keyword">case</span> <span class="hljs-string">"deluser"</span>:
      <span class="hljs-keyword">return</span> state-actions.<span class="hljs-built_in">num</span>
    <span class="hljs-keyword">default</span>:
      <span class="hljs-keyword">return</span> state
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3. store/reudcer/index.js下进行多个reducer的合并操作</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> books <span class="hljs-keyword">from</span> <span class="hljs-string">"./books"</span>;
<span class="hljs-keyword">import</span> user <span class="hljs-keyword">from</span> <span class="hljs-string">"./user"</span>;

<span class="hljs-keyword">import</span> &#123;combineReducers&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"redux"</span> 

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title function_">combineReducers</span>(&#123;
  books,user
&#125;)


<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>4. store/index.js配置</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;legacy_createStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux'</span>
<span class="hljs-keyword">import</span> rootReducer <span class="hljs-keyword">from</span> <span class="hljs-string">"./reducers/index"</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title function_">legacy_createStore</span>(rootReducer)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>页面数据的测试</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;useDispatch, useSelector&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-redux"</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">const</span> dispatch = <span class="hljs-title function_">useDispatch</span>()
  
  <span class="hljs-comment">//user模块</span>
  <span class="hljs-keyword">const</span> numUsers = <span class="hljs-title function_">useSelector</span>(<span class="hljs-function">(<span class="hljs-params">state</span>)=></span>&#123;
    <span class="hljs-keyword">return</span> state.<span class="hljs-property">user</span>
  &#125;)
  
  <span class="hljs-comment">//books模块</span>
  <span class="hljs-keyword">const</span> numBooks = <span class="hljs-title function_">useSelector</span>(<span class="hljs-function">(<span class="hljs-params">state</span>)=></span>&#123;
    <span class="hljs-keyword">return</span> state.<span class="hljs-property">books</span>
  &#125;)
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>user模块<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>num:&#123;numUsers&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>dispatch(&#123;type:'adduser',num:1&#125;)&#125;>增加num<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>dispatch(&#123;type:'deluser',num:1&#125;)&#125;>减少Num<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>---------------------------------<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>books模块<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>num:&#123;numBooks&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>dispatch(&#123;type:'addbook',num:1&#125;)&#125;>增加num<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>dispatch(&#123;type:'delbook',num:1&#125;)&#125;>减少Num<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们设置了两个不同模块的reducer,并且各自有各自的数据，尽管它们都是num,但是这个num是属于不同模块的，是互相独立的数据。如下是两个模块的测试，可以看到两个模块的num是各自独立的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd07b6a2a8b0434d81a17bcb55923e4c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">4.dispatch的优化</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f0eda7578e94dcfb0841c3d69e690d1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>观察上面dispatch部分，传入一个对象到redux的reducer中，这部分出现了大量重复臃肿设计代码，如果reducer内部发生了改变，我们需要对这些dispatch部分进行逐个的修改。因此在日常开发中，我们会对dispatch传递一个纯函数，函数内部返回一个对象。</p>
<p><strong>旧的设计</strong></p>
<pre><code class="hljs language-php copyable" lang="php"><span class="hljs-title function_ invoke__">dispatch</span>(&#123;<span class="hljs-attr">type</span>:<span class="hljs-string">"addbook"</span>,<span class="hljs-attr">num</span>:<span class="hljs-number">1</span>&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>改造后设计</strong></p>
<pre><code class="hljs language-lua copyable" lang="lua"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addbook</span><span class="hljs-params">(num)</span></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-built_in">type</span>:<span class="hljs-string">'addbook"
        num:num
    &#125;
&#125;

dispatch(addbook(1)
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>项目中的设计</strong></p>
<p>通常我们会在store目录下创建一个actions文件夹保存不同模块的actions函数</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77b298b73890448baf70269bf317b106~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>actions/user.js</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-built_in">export</span> <span class="hljs-keyword">function</span> adduser(num) &#123;
  <span class="hljs-built_in">return</span> &#123;
    <span class="hljs-built_in">type</span>:<span class="hljs-string">"adduser"</span>,
    num
  &#125;
&#125;

<span class="hljs-built_in">export</span> <span class="hljs-keyword">function</span> deluser(num) &#123;
  <span class="hljs-built_in">return</span> &#123;
    <span class="hljs-built_in">type</span>:<span class="hljs-string">"deluser"</span>,
    num
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>项目中使用</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;useDispatch, useSelector&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-redux"</span>
<span class="hljs-keyword">import</span> &#123;adduser,deluser&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./../store/actions/user"</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">const</span> dispatch = <span class="hljs-title function_">useDispatch</span>()
  <span class="hljs-comment">//user模块</span>
  <span class="hljs-keyword">const</span> numUsers = <span class="hljs-title function_">useSelector</span>(<span class="hljs-function">(<span class="hljs-params">state</span>)=></span>&#123;
    <span class="hljs-keyword">return</span> state.<span class="hljs-property">user</span>
  &#125;)
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>user模块<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>num:&#123;numUsers&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>dispatch(adduser(1))&#125;>增加num<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>dispatch(deluser(1))&#125;>减少Num<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">5.actions-type引入</h2>
<p>经过上面的优化，已经完成了99%的工作，还差1%就是优化type参数的传递，上面的type我们都是传递一个字符串，但是实际开发中，随着项目工作量的加剧，很容易在传递type字符串的时候出现错误。因此我们需要使用变量代替字符串，这样我们就可以保证唯一性和正确性。通常在store目录下创建一个type文件夹保存所有的type</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/089037112b4541a9b28f67c26dab114b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>store/types/books.js</strong></p>
<pre><code class="hljs language-arduino copyable" lang="arduino"><span class="hljs-keyword">export</span> <span class="hljs-type">const</span> ADDBOOK = <span class="hljs-string">"addbook"</span>
<span class="hljs-keyword">export</span> <span class="hljs-type">const</span> DELBOOK = <span class="hljs-string">'delbook'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>store/reducer/books.js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;<span class="hljs-variable constant_">ADDBOOK</span>,<span class="hljs-variable constant_">DELBOOK</span>&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../types/books"</span>
<span class="hljs-keyword">let</span> name = <span class="hljs-number">1</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">function</span>(<span class="hljs-params">state=name,action</span>) &#123;
  <span class="hljs-keyword">switch</span>(action.<span class="hljs-property">type</span>) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-attr">ADDBOOK</span>:
      <span class="hljs-keyword">return</span> state+action.<span class="hljs-property">num</span>
    <span class="hljs-keyword">case</span> <span class="hljs-attr">DELBOOK</span>:
      <span class="hljs-keyword">return</span> state-action.<span class="hljs-property">num</span>
    <span class="hljs-attr">default</span>: <span class="hljs-keyword">return</span> state
  &#125;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>store/actions/books.js</strong></p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">import</span> &#123;ADDBOOK,DELBOOK&#125; from <span class="hljs-string">"./../types/books"</span>
<span class="hljs-keyword">export</span> function addbook (<span class="hljs-built_in">num</span>) &#123;
  <span class="hljs-keyword">return</span> &#123;
    type:ADDBOOK,
    <span class="hljs-built_in">num</span>
  &#125;
&#125;

<span class="hljs-keyword">export</span> function delbook (<span class="hljs-built_in">num</span>) &#123;
  <span class="hljs-keyword">return</span> &#123;
    type:DELBOOK,
    <span class="hljs-built_in">num</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使用</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;useDispatch, useSelector&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-redux"</span>
<span class="hljs-keyword">import</span> &#123;addbook,delbook&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./../store/actions/books"</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">const</span> dispatch = <span class="hljs-title function_">useDispatch</span>()
  <span class="hljs-keyword">const</span> numBooks = <span class="hljs-title function_">useSelector</span>(<span class="hljs-function">(<span class="hljs-params">state</span>)=></span>&#123;
    <span class="hljs-keyword">return</span> state.<span class="hljs-property">books</span>
  &#125;)
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>books模块<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>num:&#123;numBooks&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>dispatch(addbook(1))&#125;>增加num<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>dispatch(delbook(1))&#125;>减少Num<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">6.redux-thunk引入（处理异步过程）</h2>
<p>终于来到最后一部分了，如果我们需要在redux引入异步修改数据时，如何解决？此处我们需要使用一个中间件 redux-thunk，有了这个中间件，我们可以在dsipatch修改redux数据的时候，传递一个函数，这个函数内部就可以执行异步修改redux数据的操作。</p>
<p><strong>下载</strong></p>
<pre><code class="hljs language-css copyable" lang="css">npm <span class="hljs-selector-tag">i</span> redux-thunk
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>store/index.js配置</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; applyMiddleware,legacy_createStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'redux'</span>
<span class="hljs-keyword">import</span> rootReducer <span class="hljs-keyword">from</span> <span class="hljs-string">"./reducers/index"</span>
<span class="hljs-keyword">import</span> thunk <span class="hljs-keyword">from</span> <span class="hljs-string">"redux-thunk"</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title function_">legacy_createStore</span>(rootReducer,<span class="hljs-title function_">applyMiddleware</span>(thunk))

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>store/actions/user.js</strong></p>
<p>我们按照上面的规范，在actions中操作dispatch传递的参数。我们直接在books模块添加一个异步模拟。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;<span class="hljs-variable constant_">ADDBOOK</span>,<span class="hljs-variable constant_">DELBOOK</span>&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./../types/books"</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">addbook</span> (num) &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">type</span>:<span class="hljs-variable constant_">ADDBOOK</span>,
    num
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">delbook</span> (num) &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">type</span>:<span class="hljs-variable constant_">DELBOOK</span>,
    num
  &#125;
&#125;

<span class="hljs-comment">//异步的actions</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">asyncAdd</span>(<span class="hljs-params">num</span>) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">function</span>(<span class="hljs-params">dispatch</span>) &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-title function_">dispatch</span>(<span class="hljs-title function_">addbook</span>(num))
    &#125;, <span class="hljs-number">2000</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使用</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;useDispatch, useSelector&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-redux"</span>
<span class="hljs-keyword">import</span> &#123;addbook,delbook,asyncAdd&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./../store/actions/books"</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">const</span> dispatch = <span class="hljs-title function_">useDispatch</span>()

  <span class="hljs-keyword">const</span> numBooks = <span class="hljs-title function_">useSelector</span>(<span class="hljs-function">(<span class="hljs-params">state</span>)=></span>&#123;

    <span class="hljs-keyword">return</span> state.<span class="hljs-property">books</span>
  &#125;)
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>books模块<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>num:&#123;numBooks&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>dispatch(addbook(1))&#125;>增加num<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>dispatch(delbook(1))&#125;>减少Num<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>dispatch(asyncAdd(100))&#125;>异步添加<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>测试</strong></p>
<p>可以看到，当我们点击异步添加的时候，页面在2s后修改了redux的数据。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a05afe7f7beb4e3b9958f422abee1fa2~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">总结</h2>
<p>希望大家认真练习相关redux的操作和规范化设计，如果有任何疑问，评论区留言啊。</p></div>  
</div>
            