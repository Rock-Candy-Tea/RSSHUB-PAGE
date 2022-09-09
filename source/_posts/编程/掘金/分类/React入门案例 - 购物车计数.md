
---
title: 'React入门案例 - 购物车计数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89014b57d0d44b048469256c15b293a9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 16:58:05 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89014b57d0d44b048469256c15b293a9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;font-family:-apple-system,system-ui,Segoe UI,Roboto,Ubuntu,Cantarell,Noto Sans,sans-serif,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial;color:#00325e&#125;.markdown-body ::selection&#123;background-color:#00325e;color:#fff&#125;.markdown-body blockquote&#123;padding:10px 20px;background-color:#fffaf0;box-shadow:0 3px 10px 0 rgba(255,172,194,.24);border:1px solid #f3ca8e;transition:all .2s;margin:1em 0;border-radius:5px&#125;.markdown-body blockquote p&#123;font-size:14px;line-height:25px;color:#795548&#125;.markdown-body blockquote p:last-child&#123;margin:0&#125;.markdown-body blockquote:hover&#123;border-color:#ff9800;background-color:#fff8e0;box-shadow:0 6px 10px -5px rgba(225,173,98,.3803921569)&#125;.markdown-body blockquote code&#123;color:#ff502c&#125;.markdown-body pre&#123;border:1px solid #8cc0f3;box-shadow:0 3px 10px 0 rgba(255,198,198,.28);border-radius:5px;transition:all .2s;overflow-x:auto;white-space:pre-wrap&#125;.markdown-body pre:hover&#123;border-color:#6d9dce&#125;.markdown-body pre>code&#123;padding:10px 20px;color:#00325e;background:#f0f8ff;font-size:12px;line-height:1.6;display:block&#125;.markdown-body code&#123;background:#f6fbff;color:#0b5393;padding:2px 4px;border-radius:4px;font-size:12px&#125;.markdown-body p&#123;font-size:14px;line-height:28px;text-align:justify;margin-bottom:17px;color:#595959&#125;.markdown-body a&#123;color:#00325e;text-decoration:none&#125;.markdown-body a:after&#123;content:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAQdJREFUKFNt0DtLA0EUBeBzZle0Eks7rcUfEfBRCha7NorYa6NmVJzgyi4smUgKtdZGCJktLMVH4Y8QeztLWyE7VyLEuNFbXj4Oh0P8c8mZm+uJrEN4BJFTeP/MUVe3bnocfALwkOlo1zS7iZAzf6Cx7oXgbaqjxiDEWCcVaGyxQ8pSWo9XhqhoQ/xUFbaKjhe5V+CmR7mnSplEEF6GSmJ+F/d0KHvbCIIJCLc85U6BC5mONgbJNM3uFag++sX7z8O8MzsWBucifMx0dDGE1kmm458KDVukAlnNdDz/exEeW3dNkbfsYC0xtmgDWP6ELLZ0/F6BJu/UoFQN5AkoeUjeJPvx6+i+X5Sjah4tA6gYAAAAAElFTkSuQmCC);margin-left:2px&#125;.markdown-body a:hover&#123;box-shadow:0 1px&#125;.markdown-body table&#123;max-width:100%;border-collapse:collapse;border-spacing:0;box-shadow:0 3px 10px 0 rgba(255,238,172,.24);transition:all .2s&#125;.markdown-body table:hover&#123;box-shadow:0 3px 10px 0 rgba(185,169,103,.24)&#125;.markdown-body table tr th&#123;border:1px solid #8cc0f3;background-color:#f0f8ff;padding:12px 15px&#125;.markdown-body table tr td&#123;border:1px solid rgba(243,202,142,.4);padding:12px 15px&#125;.markdown-body table tbody tr&#123;transition:all .2s&#125;.markdown-body table tbody tr:hover td&#123;border-color:#f3ca8e;background-color:#fff8e0;z-index:1&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body h1&#123;font-size:20px;margin-top:30px;margin-bottom:10px;padding-left:30px;position:relative&#125;.markdown-body h1>code&#123;font-size:20px&#125;.markdown-body h1:before&#123;content:"🍺";display:block;font-size:18px;width:18px;height:18px;left:0;position:absolute&#125;.markdown-body h2&#123;font-size:18px;margin-top:30px;margin-bottom:10px;padding-left:28px;position:relative&#125;.markdown-body h2>code&#123;font-size:18px&#125;.markdown-body h2:before&#123;content:"🍻";display:block;font-size:16px;width:16px;height:16px;left:0;position:absolute&#125;.markdown-body h3&#123;font-size:16px;margin-top:30px;margin-bottom:10px;padding-left:26px;position:relative&#125;.markdown-body h3>code&#123;font-size:16px&#125;.markdown-body h3:before&#123;content:"🥂";display:block;font-size:14px;width:14px;height:14px;left:0;position:absolute&#125;.markdown-body h4&#123;font-size:14px;margin-top:30px;margin-bottom:10px;padding-left:24px;position:relative&#125;.markdown-body h4>code&#123;font-size:14px&#125;.markdown-body h4:before&#123;content:"🥃";display:block;font-size:12px;width:12px;height:12px;left:0;position:absolute&#125;.markdown-body h5&#123;font-size:12px;margin-top:30px;margin-bottom:10px&#125;.markdown-body h5>code&#123;font-size:12px&#125;.markdown-body h6&#123;font-size:10px;margin-top:30px;margin-bottom:10px&#125;.markdown-body h6>code&#123;font-size:10px&#125;.markdown-body h1,.markdown-body h2&#123;color:#ff502c&#125;.markdown-body hr&#123;height:4px;border:none;margin-top:32px;margin-bottom:32px;background-size:4px 1px;background-image:linear-gradient(270deg,#6d9dce,#8cc0f3 25%,transparent 50%)&#125;.markdown-body hr:nth-child(2n)&#123;background-image:linear-gradient(270deg,#ff9800,#fff8e0 25%,transparent 50%)&#125;.markdown-body ul&#123;padding-inline-start:20px&#125;.markdown-body ul li&#123;list-style-type:"🔸"&#125;.markdown-body ul li li&#123;list-style-type:"◻️"&#125;.markdown-body ul li li li&#123;list-style-type:"▫️"&#125;.markdown-body ol&#123;padding-inline-start:20px&#125;.markdown-body ol ::marker&#123;color:#ff9800&#125;.markdown-body ol,.markdown-body ul&#123;line-height:2em&#125;.markdown-body li&#123;padding-inline-start:1ch&#125;.markdown-body li.task-list-item&#123;list-style:none;padding-inline-start:0&#125;.markdown-body li input&#123;padding-right:2px&#125;.markdown-body li input[type=checkbox i]&#123;appearance:none&#125;.markdown-body li input:before&#123;content:"🟩";display:block;width:13px;height:13px&#125;.markdown-body li input:checked:before&#123;content:"✅"&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>开始学习react，先从react官网的案例开始，，学习react中的组件，数据传递，还有JSX</p>
<h1 data-id="heading-0">项目地址</h1>
<ul>
<li>官网案例地址 - <a href="https://link.juejin.cn/?target=https%3A%2F%2Freactjs.org%2Fcommunity%2Fexamples.html" target="_blank" rel="nofollow noopener noreferrer" title="https://reactjs.org/community/examples.html" ref="nofollow noopener noreferrer">reactjs.org/community/e…</a></li>
<li>Counter App（本文案例） - <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Farnab-datta%2Fcounter-app" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/arnab-datta/counter-app" ref="nofollow noopener noreferrer">github.com/arnab-datta…</a></li>
</ul>
<h1 data-id="heading-1">预备知识</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F00226a584eff" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/00226a584eff" ref="nofollow noopener noreferrer">react组件的 render 方法</a></p>
<ul>
<li><strong>必须要有render</strong></li>
<li><strong>外层仅有一个div</strong></li>
<li><strong>&#123;&#125; 内可以放任何JavaScript代码</strong>，如表达式，函数等</li>
<li>class 用 <strong>className</strong></li>
<li>label的for属性 用 <strong>htmlFor</strong></li>
</ul>
<hr>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FLearn%2FTools_and_testing%2FClient-side_JavaScript_frameworks%2FReact_getting_started" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/React_getting_started" ref="nofollow noopener noreferrer">MDN - react入门</a></p>
<ul>
<li><strong>所有的React模块都要引用React</strong>（import React from 'react'），是为了将代码中的JSX转为React.createElement()</li>
<li>React 组件使用<strong>帕斯卡命名法</strong>，又称为"大驼峰式命名法"，如“HelloWorld”</li>
<li>React 的组件要用<strong>export导出</strong>，这样其他文件可以使用</li>
<li><strong>prop</strong> 是任何传入 React 组件的数据</li>
<li>通过把变量放在<strong>大括号</strong>中，您可以读取 JSX 的变量，如<code>&#123;so&#125;</code></li>
</ul>
<hr>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F71fc61b35047" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/71fc61b35047" ref="nofollow noopener noreferrer">react里的 index.js 是怎么跟 index.html 结合起来的?</a></p>
<ul>
<li>
<blockquote>
<p>你可以在项目下运行<strong>npm run eject</strong>，被隐藏的配置文件就会暴露到项目根路径下。把请求转发到index.html原因是，你<strong>执行npm run start</strong>时，启动的webpack-dev-server，<strong>会加载react-script项目config文件夹下的配置（paths.js）</strong>,<strong>里面定义了请求的默认转发路径是public文件夹</strong>，自然就找到了public下的index.html。</p>
</blockquote>
</li>
</ul>
<h1 data-id="heading-2">案例分析</h1>
<h2 data-id="heading-3">视图结构</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89014b57d0d44b048469256c15b293a9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">文件结构</h2>
<ul>
<li>src
<ul>
<li>components - 组件
<ul>
<li>counter.jsx</li>
<li>counters.jsx</li>
<li>navbar.jsx</li>
</ul>
</li>
<li>App.js - <strong>组件集合</strong></li>
<li>index.css - 全局样式</li>
<li>index.js - <strong>文件入口</strong></li>
</ul>
</li>
</ul>
<h2 data-id="heading-5">代码细节</h2>
<h3 data-id="heading-6">index.js</h3>
<p><strong>index.js主要作用</strong></p>
<ul>
<li>把App组件渲染到页面中，</li>
<li><strong>使用的是ReactDOM</strong>，把App组件的内容，放到root里！</li>
<li>引入<strong>全局样式</strong>，这样组件就能使用了</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d0ea8f1a5364322aeeeb132f1eb9ad9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">App.js</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> <span class="hljs-title class_">React</span>, &#123; <span class="hljs-title class_">Component</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>; <span class="hljs-comment">// 必须要引入React！</span>
<span class="hljs-keyword">import</span> <span class="hljs-title class_">NavBar</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"./components/navbar"</span>; <span class="hljs-comment">// 引入组件</span>
<span class="hljs-keyword">import</span> <span class="hljs-title class_">Counters</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"./components/counters"</span>;

<span class="hljs-keyword">class</span> <span class="hljs-title class_">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title class_ inherited__">Component</span> &#123;
  state = &#123; <span class="hljs-comment">// 定义数据集</span>
    <span class="hljs-attr">counters</span>: [
      &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">value</span>: <span class="hljs-number">0</span> &#125;,
      &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">value</span>: <span class="hljs-number">0</span> &#125;,
      &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">value</span>: <span class="hljs-number">0</span> &#125;,
      &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">4</span>, <span class="hljs-attr">value</span>: <span class="hljs-number">0</span> &#125;,
    ],
  &#125;;

  handleIncrement = <span class="hljs-function">(<span class="hljs-params">counter</span>) =></span> &#123; <span class="hljs-comment">// 父组件定义方法 - 增加数量，用于向子组件传递！</span>
    <span class="hljs-keyword">const</span> counters = [...<span class="hljs-variable language_">this</span>.<span class="hljs-property">state</span>.<span class="hljs-property">counters</span>]; <span class="hljs-comment">// 数据备份,不能直接修改state中的内容！</span>
    <span class="hljs-keyword">const</span> index = counters.<span class="hljs-title function_">indexOf</span>(counter);
    <span class="hljs-comment">// counters[index] = &#123; ...counters[index] &#125;; // 这一步是？？？？</span>
    counters[index].<span class="hljs-property">value</span>++;
    <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">setState</span>(&#123; counters &#125;); <span class="hljs-comment">// 使用set函数，视图重新 render 渲染</span>
  &#125;;

  handleDecrement = <span class="hljs-function">(<span class="hljs-params">counter</span>) =></span> &#123;
  &#125;;

  handleReset = <span class="hljs-function">() =></span> &#123;
  &#125;;

  handleDelete = <span class="hljs-function">(<span class="hljs-params">counterId</span>) =></span> &#123;
  &#125;;

  handleRestart = <span class="hljs-function">() =></span> &#123;
  &#125;;

  <span class="hljs-title function_">render</span>(<span class="hljs-params"></span>) &#123; <span class="hljs-comment">// render函数！</span>
    <span class="hljs-keyword">return</span> ( <span class="hljs-comment">// 返回一个jsx！外层仅一个div</span>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"main__wrap"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">main</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"container"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"card__box"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">NavBar</span>
              <span class="hljs-attr">totalCounters</span>=<span class="hljs-string">&#123;</span>
                <span class="hljs-attr">this.state.counters.filter</span>((<span class="hljs-attr">c</span>) =></span> c.value > 0).length
              &#125;
            />
            <span class="hljs-tag"><<span class="hljs-name">Counters</span>
              <span class="hljs-attr">counters</span>=<span class="hljs-string">&#123;this.state.counters&#125;</span> // 这里的<span class="hljs-attr">this</span>指的是<span class="hljs-attr">App</span>，向子组件传递方法！
              <span class="hljs-attr">onReset</span>=<span class="hljs-string">&#123;this.handleReset&#125;</span>
              <span class="hljs-attr">onIncrement</span>=<span class="hljs-string">&#123;this.handleIncrement&#125;</span>
              <span class="hljs-attr">onDecrement</span>=<span class="hljs-string">&#123;this.handleDecrement&#125;</span>
              <span class="hljs-attr">onDelete</span>=<span class="hljs-string">&#123;this.handleDelete&#125;</span>
              <span class="hljs-attr">onRestart</span>=<span class="hljs-string">&#123;this.handleRestart&#125;</span>
            /></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">main</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title class_">App</span>; <span class="hljs-comment">// 导出App组件</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">counters.jsx</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Freactjs.org%2Fdocs%2Flists-and-keys.html" target="_blank" rel="nofollow noopener noreferrer" title="https://reactjs.org/docs/lists-and-keys.html" ref="nofollow noopener noreferrer">React官网 - Lists and Keys</a></p>
<ul>
<li>学习渲染组件的时候要加入key，vue的key要加冒号，react不用。。</li>
<li>使用map来循环渲染组件！</li>
<li>key可以帮助react决定那些是要改变的，添加的，删除的，</li>
<li><strong>key应该放在map函数里面</strong>，这样保证每个都是key都是唯一的。。（推荐不要用index做key）</li>
<li>兄弟节点直接key要唯一，这个key不用全局唯一</li>
<li>如果map函数内容很多很多，就该抽离成组件了！</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> <span class="hljs-title class_">React</span>, &#123; <span class="hljs-title class_">Component</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>; <span class="hljs-comment">// 必须要引入React</span>
<span class="hljs-keyword">import</span> <span class="hljs-title class_">Counter</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"./counter"</span>;

<span class="hljs-keyword">class</span> <span class="hljs-title class_">Counters</span> <span class="hljs-keyword">extends</span> <span class="hljs-title class_ inherited__">Component</span> &#123;
  <span class="hljs-title function_">render</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-comment">// 接收传入数据。</span>
    <span class="hljs-keyword">const</span> &#123; onReset, onIncrement, onDelete, onDecrement, counters, onRestart &#125; =
      <span class="hljs-variable language_">this</span>.<span class="hljs-property">props</span>;

    <span class="hljs-keyword">return</span> ( <span class="hljs-comment">// 返回JSX</span>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        &#123;/* 两个按钮 */&#125;
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"row"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">""</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span>
              <span class="hljs-attr">className</span>=<span class="hljs-string">"btn btn-success m-2"</span>
              <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;onReset&#125;</span> // 使用传入方法
              <span class="hljs-attr">disabled</span>=<span class="hljs-string">&#123;counters.length</span> === <span class="hljs-string">0</span> ? "<span class="hljs-attr">disabled</span>" <span class="hljs-attr">:</span> ""&#125;
            ></span>
              <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"fa fa-refresh"</span> <span class="hljs-attr">aria-hidden</span>=<span class="hljs-string">"true"</span> /></span> // bootstrap的icon
            <span class="hljs-tag"></<span class="hljs-name">button</span>></span>

            <span class="hljs-tag"><<span class="hljs-name">button</span>
              <span class="hljs-attr">className</span>=<span class="hljs-string">"btn btn-primary m-2"</span>
              <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;onRestart&#125;</span>
              <span class="hljs-attr">disabled</span>=<span class="hljs-string">&#123;counters.length</span> !== <span class="hljs-string">0</span> ? "<span class="hljs-attr">disabled</span>" <span class="hljs-attr">:</span> ""&#125;
            ></span>
              <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"fa fa-recycle"</span> <span class="hljs-attr">aria-hidden</span>=<span class="hljs-string">"true"</span> /></span>
            <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

        &#123;/* map遍历 */&#125;
        &#123;counters.map((counter) => (
          // 继续传递
          <span class="hljs-tag"><<span class="hljs-name">Counter</span>
            <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;counter.id&#125;</span> // 在<span class="hljs-attr">map</span>里，保证<span class="hljs-attr">key</span>的唯一
            <span class="hljs-attr">counter</span>=<span class="hljs-string">&#123;counter&#125;</span> // 继续向子组件传递
            <span class="hljs-attr">onIncrement</span>=<span class="hljs-string">&#123;onIncrement&#125;</span>
            <span class="hljs-attr">onDecrement</span>=<span class="hljs-string">&#123;onDecrement&#125;</span>
            <span class="hljs-attr">onDelete</span>=<span class="hljs-string">&#123;onDelete&#125;</span>
          /></span>
        ))&#125;
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title class_">Counters</span>;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">counter.jsx</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 为什么这里的React 不能去掉？？？</span>

<span class="hljs-comment">// 第一句代码引入了 React 库，这是为了将代码中的 JSX 语句转为React.createElement()，</span>
<span class="hljs-comment">// 所有的 React 模块都应该引入 React 模块，否则会抛错。</span>
<span class="hljs-keyword">import</span> <span class="hljs-title class_">React</span>, &#123; <span class="hljs-title class_">Component</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;

<span class="hljs-keyword">class</span> <span class="hljs-title class_">Counter</span> <span class="hljs-keyword">extends</span> <span class="hljs-title class_ inherited__">Component</span> &#123;
  <span class="hljs-title function_">render</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"row"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">""</span>></span>
            &#123;/* 颜色变换 + 数值变换 */&#125;
            <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">fontSize:</span> <span class="hljs-attr">24</span> &#125;&#125; <span class="hljs-attr">className</span>=<span class="hljs-string">&#123;this.getBadgeClasses()&#125;</span>></span>
              &#123;this.formatCount()&#125; // 通过方法的返回值来显示文字信息
            <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">""</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span>
              <span class="hljs-attr">className</span>=<span class="hljs-string">"btn btn-secondary"</span>
              // 使用传入的方法（增加函数），这里传入的参数，用于在<span class="hljs-attr">App.js</span>中判断。。。。
              <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> this.props.onIncrement(this.props.counter)&#125; 
            >
              <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"fa fa-plus-circle"</span> <span class="hljs-attr">aria-hidden</span>=<span class="hljs-string">"true"</span> /></span>
            <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span>
              <span class="hljs-attr">className</span>=<span class="hljs-string">"btn btn-info m-2"</span>
              <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> this.props.onDecrement(this.props.counter)&#125;
              disabled=&#123;this.props.counter.value === 0 ? "disabled" : ""&#125;
            >
              <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"fa fa-minus-circle"</span> <span class="hljs-attr">aria-hidden</span>=<span class="hljs-string">"true"</span> /></span>
            <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span>
              <span class="hljs-attr">className</span>=<span class="hljs-string">"btn btn-danger"</span>
              // 这里的删除，使用的是<span class="hljs-attr">filter</span>过虑，把这个传入的<span class="hljs-attr">id</span>，筛掉
              <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> this.props.onDelete(this.props.counter.id)&#125;
            >
              <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"fa fa-trash-o"</span> <span class="hljs-attr">aria-hidden</span>=<span class="hljs-string">"true"</span> /></span>
            <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
    
  <span class="hljs-comment">// 返回class内容。。</span>
  getBadgeClasses = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">let</span> classes = <span class="hljs-string">"badge m-2 badge-"</span>;
    classes += <span class="hljs-variable language_">this</span>.<span class="hljs-property">props</span>.<span class="hljs-property">counter</span>.<span class="hljs-property">value</span> === <span class="hljs-number">0</span> ? <span class="hljs-string">"warning"</span> : <span class="hljs-string">"primary"</span>;
    <span class="hljs-keyword">return</span> classes;
  &#125;;
   
  <span class="hljs-comment">// 返回文字信息</span>
  formatCount = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> &#123; value &#125; = <span class="hljs-variable language_">this</span>.<span class="hljs-property">props</span>.<span class="hljs-property">counter</span>;
    <span class="hljs-keyword">return</span> value === <span class="hljs-number">0</span> ? <span class="hljs-string">"Zero"</span> : value;
  &#125;;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title class_">Counter</span>;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">navbar.jsx</h3>
<p>发现还可以直接用函数接收变量。。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> <span class="hljs-title class_">React</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;

<span class="hljs-comment">// Stateless Functional Component</span>

<span class="hljs-comment">// 这里不用props，直接使用App.js传入的参数。。？？？？？</span>
<span class="hljs-keyword">const</span> <span class="hljs-title function_">NavBar</span> = (<span class="hljs-params">&#123; totalCounters &#125;</span>) => &#123;

<span class="hljs-comment">// 这里直接返回JSX就可以了。。不用render函数，如果基础component，必须要render函数</span>
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">nav</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"navbar navbar-light"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"navbar-brand"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"fa fa-shopping-cart fa-lg m-2"</span> <span class="hljs-attr">aria-hidden</span>=<span class="hljs-string">"true"</span> /></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>
          <span class="hljs-attr">className</span>=<span class="hljs-string">"badge badge-pill badge-info m-2"</span>
          <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">width:</span> <span class="hljs-attr">50</span>, <span class="hljs-attr">fontSize:</span> "<span class="hljs-attr">24px</span>" &#125;&#125;
        ></span>
          &#123;totalCounters&#125;
        <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        Items
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">nav</span>></span></span>
  );
&#125;;

--------

<span class="hljs-comment">// 第二种。。</span>
<span class="hljs-keyword">class</span> <span class="hljs-title class_">NavBar</span> <span class="hljs-keyword">extends</span> <span class="hljs-title class_ inherited__">Component</span> &#123;
  <span class="hljs-title function_">render</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">nav</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"navbar navbar-light"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"navbar-brand"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">i</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"fa fa-shopping-cart fa-lg m-2"</span> <span class="hljs-attr">aria-hidden</span>=<span class="hljs-string">"true"</span> /></span>
          <span class="hljs-tag"><<span class="hljs-name">span</span>
            <span class="hljs-attr">className</span>=<span class="hljs-string">"badge badge-pill badge-info m-2"</span>
            <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">width:</span> <span class="hljs-attr">50</span>, <span class="hljs-attr">fontSize:</span> "<span class="hljs-attr">24px</span>" &#125;&#125;
          ></span>
            &#123;this.props.totalCounters&#125; // 使用props
          <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
          Items
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">nav</span>></span></span>
    );
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title class_">NavBar</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">总结</h1>
<p>学习React的第一个案例</p>
<ul>
<li>react的组件划分也要靠视图来判断</li>
<li>App.js中，定义好了方法，直接往下传递即可</li>
<li>多个数据用map来渲染，在map中使用key</li>
<li>改变state，要用setState</li>
<li>每个react模块，都要引用react，import react！</li>
<li>&#123;&#125;里可以放数据，放方法，放任意Js表达式</li>
<li>组件的后缀是 jsx</li>
<li>继承component，一定要实现render方法。</li>
<li>React组件命名，使用大驼峰</li>
<li>组件要用export导出</li>
</ul>
<blockquote>
<p>好的决心必须以行动来贯彻,没有行动,好的决心没有任何意义。</p>
</blockquote></div>  
</div>
            