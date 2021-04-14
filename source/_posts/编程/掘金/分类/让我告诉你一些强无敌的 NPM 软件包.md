
---
title: '让我告诉你一些强无敌的 NPM 软件包'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b6a2d8506304a62afeb575afed3c5ea~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 13 Apr 2021 02:16:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b6a2d8506304a62afeb575afed3c5ea~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>面对繁忙的日程安排与紧迫的工期限制，选择能够切实提升生产率的工具无疑至关重要。</p>
<p>在这里，我整理出一份个人最喜欢的 NPM 软件包清单。为了便于浏览，我还对它们进行了分类，希望呈现出更加清晰的结构。</p>
<p>当然，大家不必全数安装与学习。在大多数情况下，每个类别选择一款就足以解决生产需求。我只是想多提供一点替代方案，帮助每位读者朋友找到最适合自己的选项。闲言少叙，咱们马上开始！</p>
<h2 data-id="heading-0">🧰 实用工具</h2>
<h3 data-id="heading-1">Lodash</h3>
<p><a href="https://www.lodashjs.com/docs/latest" target="_blank" rel="nofollow noopener noreferrer">lodash</a>是一套现代 JavaScript 实用程序库，提供模块化、性能与多种附加功能。可提供关于 JavaScript 数组、对象及其他数据结构的多种实用功能。</p>
<p><img alt="lodash-logo" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b6a2d8506304a62afeb575afed3c5ea~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">安装及示例</h4>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add lodash
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>不要滥用，尽量使用 ES 自带方法</strong> 。 我常用的一些方法如下</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// -----------------------------深度比较两个对象的值是否全相等</span>
<span class="hljs-keyword">import</span> &#123; isEqual, cloneDeep, uniqBy, sortBy &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"lodash"</span>;

<span class="hljs-keyword">const</span> <span class="hljs-built_in">object</span> = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span> &#125;;
<span class="hljs-keyword">const</span> other = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span> &#125;;

isEqual(<span class="hljs-built_in">object</span>, other);
<span class="hljs-comment">// => true</span>

<span class="hljs-built_in">object</span> === other;
<span class="hljs-comment">// => false</span>

<span class="hljs-comment">// -----------------------------深拷贝</span>
<span class="hljs-keyword">const</span> objects = [&#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span> &#125;, &#123; <span class="hljs-attr">b</span>: <span class="hljs-number">2</span> &#125;];

<span class="hljs-keyword">const</span> deep = cloneDeep(objects);
<span class="hljs-built_in">console</span>.log(deep[<span class="hljs-number">0</span>] === objects[<span class="hljs-number">0</span>]);
<span class="hljs-comment">// => false</span>

<span class="hljs-comment">// -----------------------------数组去重</span>
uniqBy([&#123; <span class="hljs-attr">x</span>: <span class="hljs-number">1</span> &#125;, &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">2</span> &#125;, &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">1</span> &#125;], <span class="hljs-string">"x"</span>);
<span class="hljs-comment">// => [&#123; 'x': 1 &#125;, &#123; 'x': 2 &#125;]</span>

<span class="hljs-comment">// -----------------------------数组排序</span>
<span class="hljs-keyword">const</span> users = [
  &#123; <span class="hljs-attr">user</span>: <span class="hljs-string">"fred"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">48</span> &#125;,
  &#123; <span class="hljs-attr">user</span>: <span class="hljs-string">"barney"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">36</span> &#125;,
  &#123; <span class="hljs-attr">user</span>: <span class="hljs-string">"fred"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">40</span> &#125;,
  &#123; <span class="hljs-attr">user</span>: <span class="hljs-string">"barney"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">34</span> &#125;,
];
sortBy(users, <span class="hljs-string">"age"</span>);
<span class="hljs-comment">/*
[
  &#123; 'user': 'barney', 'age': 34 &#125;,
  &#123; 'user': 'barney', 'age': 36 &#125;,
  &#123; 'user': 'fred', 'age': 40 &#125;,
  &#123; 'user': 'fred', 'age': 48 &#125;,
];
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">qs</h3>
<p><a href="https://www.npmjs.com/package/qs" target="_blank" rel="nofollow noopener noreferrer"><code>qs</code></a> 处理 URL 查询字符串,支持内嵌对象和数组。简而言之，就是将对象和 URL 地址的参数互相转换</p>
<p><img alt="qs-github" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6599b1196e84ee6ab1f0d0ce4a274d1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-4">安装及示例</h5>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add qs
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; parse, stringify &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"qs"</span>;

<span class="hljs-comment">// 用途一</span>
<span class="hljs-comment">// 将 浏览器上 URL地址参数转换为对象（字符串转对象）</span>
<span class="hljs-keyword">const</span> urlParams = parse(<span class="hljs-built_in">window</span>.location.href.split(<span class="hljs-string">"?"</span>)[<span class="hljs-number">1</span>]);

<span class="hljs-comment">// 用途二</span>
<span class="hljs-comment">// 将对象参数 传递给到后端接口--GET 请求  （对象转字符串）</span>
<span class="hljs-keyword">const</span> params = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"wang"</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-string">"18"</span>,
  <span class="hljs-attr">sex</span>: <span class="hljs-string">"女"</span>,
&#125;;

<span class="hljs-comment">// =>  /api/user?name=wang&age=18&sex=%E5%A5%B3</span>
<span class="hljs-keyword">const</span> apiUrl = <span class="hljs-string">`/api/user?<span class="hljs-subst">$&#123;stringify(params)&#125;</span>`</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">classnames</h3>
<p><a href="https://www.npmjs.com/package/classnames" target="_blank" rel="nofollow noopener noreferrer">classnames</a>有条件地将类名组合在一起</p>
<h4 data-id="heading-6">安装及示例</h4>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add classnames
<span class="copy-code-btn">复制代码</span></code></pre>
<p>错误 ❎ 代码示例: React 原生动态添加多个样式类名会报错：</p>
<pre><code class="hljs language-tsx copyable" lang="tsx">import styles from "./index.less";

const Index=()=><div className=&#123;style.class1 style.class2&#125;</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改为如下代码即可解决</p>
<pre><code class="hljs language-tsx copyable" lang="tsx">import React from "react"
import classnames from 'classnames'

import styles from "./index.less";

const Index=()=>(<div
          className=classnames(&#123;
              style.class1,
              style.class2
          &#125;)>
</div>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">numeral</h3>
<p><a href="http://numeraljs.com/#format" target="_blank" rel="nofollow noopener noreferrer">numeral</a>是一个专门用来格式化数字的 NPM 库，同时 numeral 还能解析各种格式的数字。</p>
<p><img alt="numeral-github" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f995483fc3174302900f69b0fa00d3de~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">安装及示例</h4>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add numeral
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> numeral <span class="hljs-keyword">from</span> <span class="hljs-string">"numeral"</span>;

<span class="hljs-comment">// 解析数字</span>
numeral(<span class="hljs-string">"10,000.12"</span>); <span class="hljs-comment">// 10000.12</span>
numeral(<span class="hljs-string">"$10,000.00"</span>); <span class="hljs-comment">// 10000</span>
numeral(<span class="hljs-string">"3.467TB"</span>); <span class="hljs-comment">// 3467000000000</span>
numeral(<span class="hljs-string">"-76%"</span>); <span class="hljs-comment">// -0.76</span>

<span class="hljs-comment">// 格式化</span>

numeral(<span class="hljs-number">10000.23</span>).format(<span class="hljs-string">"0,0"</span>); <span class="hljs-comment">// '10,000'</span>
numeral(<span class="hljs-number">1000.234</span>).format(<span class="hljs-string">"$0,0.00"</span>); <span class="hljs-comment">// '$1,000.23'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">cross-env</h3>
<p><a href="https://www.npmjs.com/package/cross-env" target="_blank" rel="nofollow noopener noreferrer">cross-env</a>是一个运行<strong>跨平台</strong>设置和使用环境变量的脚本</p>
<h5 data-id="heading-10">安装及示例</h5>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add cross-env --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"start"</span>: <span class="hljs-string">"cross-env REACT_APP_ENV=development webpack"</span>,
    <span class="hljs-string">"build"</span>: <span class="hljs-string">"cross-env REACT_APP_ENV=production webpack"</span>,
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">path-to-regexp</h3>
<p><a href="https://www.npmjs.com/package/path-to-regexp" target="_blank" rel="nofollow noopener noreferrer">path-to-regexp</a>用来处理 url 中地址与参数，能够很方便得到我们想要的数据。</p>
<p>js 中有 <code>RegExp</code> 方法做正则表达式校验，而 <code>path-to-regexp</code> 可以看成是 url 字符串的正则表达式。</p>
<h4 data-id="heading-12">安装及示例</h4>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add path-to-regexp
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>pathToRegexp</code>方法可以类比于 js 中 <code>new RegExp('xxx')</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> pathToRegexp <span class="hljs-keyword">from</span> <span class="hljs-string">"path-to-regexp"</span>;

<span class="hljs-keyword">const</span> re = pathToRegexp(<span class="hljs-string">"/foo/:bar"</span>);
<span class="hljs-built_in">console</span>.log(re); <span class="hljs-comment">// /^\/foo\/((?:[^\/]+?))(?:\/(?=$))?$/i</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>compile</code>用于填充 url 字符串的参数值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> pathToRegexp = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path-to-regexp"</span>);

<span class="hljs-keyword">var</span> url = <span class="hljs-string">"/user/:id/:name"</span>;
<span class="hljs-keyword">var</span> data = &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">10001</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">"bob"</span> &#125;;

<span class="hljs-comment">// /user/10001/bob</span>
<span class="hljs-built_in">console</span>.log(pathToRegexp.compile(url)(data));
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h2 data-id="heading-13">📅 日期格式</h2>
<h3 data-id="heading-14">Day.js</h3>
<p><a href="https://dayjs.gitee.io/docs/zh-CN/display/format" target="_blank" rel="nofollow noopener noreferrer">Day.js</a> 是一款快速且轻量化的 <a href="http://momentjs.cn/" target="_blank" rel="nofollow noopener noreferrer">Moment.js</a>(自 2020 年 9 月起进入纯维护模式,不再开发新版本) 替代方案。二者拥有类似的 API，只要你接触过 <code>Moment.js</code>，就能够快速上手 <code>Day.js</code>。</p>
<p><img alt="dayJS-office" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54dadaf204fd4efeb3860ffe53e58647~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-15">安装</h4>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add dayjs
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">示例</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> dayjs <span class="hljs-keyword">from</span> <span class="hljs-string">"dayjs"</span>;

<span class="hljs-keyword">const</span> myformat = <span class="hljs-string">"YYYY-MM-DD HH:mm:ss"</span>;

<span class="hljs-comment">// -------------------------以字符串形式返回 当前时间</span>
<span class="hljs-keyword">const</span> data = dayjs().format(myformat);
<span class="hljs-comment">// =>  2020-11-25 12:25:56</span>

<span class="hljs-comment">// -------------------------日期格式化</span>
<span class="hljs-keyword">const</span> data1 = dayjs(<span class="hljs-string">"2020-11-25 12:25:56"</span>).format(<span class="hljs-string">"YYYY/MM/DD HH/mm/ss"</span>);
<span class="hljs-comment">// => 2020/11/25 12/25/56</span>

<span class="hljs-comment">// -------------------------多久之前</span>
<span class="hljs-keyword">var</span> relativeTime = <span class="hljs-built_in">require</span>(<span class="hljs-string">"dayjs/plugin/relativeTime"</span>);
dayjs.extend(relativeTime);
<span class="hljs-keyword">const</span> data1 = dayjs(<span class="hljs-string">"2020-11-25 11:40:41"</span>).fromNow();

<span class="hljs-comment">// =></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h2 data-id="heading-17">🌷 Linters 与格式化工具</h2>
<h3 data-id="heading-18">ESLint</h3>
<p><a href="https://eslint.bootcss.com/docs/user-guide/getting-started" target="_blank" rel="nofollow noopener noreferrer">ESLint</a> 是一个很好用的工具，可用来避免代码错误并强制开发团队使用编码标准。ESLint 是用于识别和报告 ECMAScript/JavaScript 代码中模式的工具。ESLint 具备全面的可插入特性，每项规则对应一款插件，供你在运行时添加更多内容。</p>
<p><img alt="eslint-offcial" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ca7c4c0ffad4f84ba906623bb19f583~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-19">安装和使用</h5>
<pre><code class="hljs language-powershell copyable" lang="powershell"><span class="hljs-variable">$</span> yarn add eslint -<span class="hljs-literal">-dev</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，你应该设置一个配置文件：</p>
<pre><code class="hljs language-powershell copyable" lang="powershell"><span class="hljs-variable">$</span> ./node_modules/.bin/eslint -<span class="hljs-literal">-init</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后，你可以在任何文件或目录上运行 ESLint，如下所示：</p>
<pre><code class="hljs language-powershell copyable" lang="powershell"><span class="hljs-variable">$</span> ./node_modules/.bin/eslint yourfile.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有关更多说明，请参阅<a href="https://eslint.org/" target="_blank" rel="nofollow noopener noreferrer">官方文档</a>，其中有许多入门和配置示例。</p>
<h3 data-id="heading-20">Prettier</h3>
<p><a href="https://prettier.bootcss.com/docs/index.html" target="_blank" rel="nofollow noopener noreferrer">Prettier</a> 是一款风格鲜明的代码格式化程序。它通过解析代码并使用自己的规则（限定最大行长）对代码进行重新输出，借此实现统一的样式；</p>
<p><img alt="prettier-office" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1541af36a2e549b2b38b10588385d48e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-21">安装</h4>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add --dev --exact prettier
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">示例</h4>
<p>创建 <code>.prettierrc.js</code> 加入自定义格式化规则</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">trailingComma</span>: <span class="hljs-string">"es5"</span>,
  <span class="hljs-attr">tabWidth</span>: <span class="hljs-number">4</span>,
  <span class="hljs-attr">semi</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">singleQuote</span>: <span class="hljs-literal">true</span>,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建 <code>.prettierignore</code> 加入需要忽略的文件或目录</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> Ignore artifacts:</span>
build
coverage
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行格式化命令</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> 格式化src目录下的所有js文件</span>

prettier --write "src/**/*.js"
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">stylelint</h3>
<p><a href="https://stylelint.io/user-guide/get-started" target="_blank" rel="nofollow noopener noreferrer">stylelint</a> 一个强大的样式规则，可以让你强制执行样式规范，避免书写错误的样式代码</p>
<h4 data-id="heading-24">安装</h4>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add stylelint stylelint-config-standard --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">示例</h4>
<p>创建<code>.stylelintrc.js</code>并加入配置</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">extends</span>: <span class="hljs-string">"stylelint-config-standard"</span>,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 lint 命令</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> 检查 src目录下所有css文件是否符合规范</span>
npx stylelint "src/**/*.css"
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">Husky </h3>
<p><a href="https://www.npmjs.com/package/husky" target="_blank" rel="nofollow noopener noreferrer">Husky</a> 可以帮助我们简单直接地实现 git hooks。你们团队正在协作开发，并希望在整个团队中推行一套编码标准？没问题！有了 Husky，你就可以要求所有人在提交或推送到存储库之前自动完成 lint 并测试其代码。</p>
<p><img alt="HUSKY-GITHUB" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec7412d2675c430f9d134c2ae3b63529~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-27">安装及示例</h5>
<pre><code class="hljs language-powershell copyable" lang="powershell">yarn add husky -<span class="hljs-literal">-dev</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是一个实现 husky hooks 的示例：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// package.json</span>
&#123;
  <span class="hljs-attr">"husky"</span>: &#123;
    <span class="hljs-attr">"hooks"</span>: &#123;
      <span class="hljs-attr">"pre-commit"</span>: <span class="hljs-string">"npm lint"</span>,
      <span class="hljs-attr">"pre-push"</span>: <span class="hljs-string">"npm test"</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里 <code>pre-commit</code> 的 <code>hooks</code> 会在你提交到存储库之前运行。在将代码推送到存储库之前，将运行 <code>pre-push hook</code>。</p>
<hr>
<h2 data-id="heading-28">🧙‍♂️ 数据生成器</h2>
<h3 data-id="heading-29">Uuid</h3>
<p><a href="https://www.npmjs.com/package/uuid" target="_blank" rel="nofollow noopener noreferrer">uuid</a>是一个便捷的微型软件包，能够快速生成更为复杂的通用唯一标识符（UUID）。</p>
<h4 data-id="heading-30">安装及示例</h4>
<pre><code class="copyable">npm install uuid
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; v4 <span class="hljs-keyword">as</span> uuidv4 &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"uuid"</span>;
uuidv4(); <span class="hljs-comment">// ⇨ '9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31">faker.js</h3>
<p><a href="https://www.npmjs.com/package/faker" target="_blank" rel="nofollow noopener noreferrer">faker.js</a>非常实用的工具包，用于在浏览器及 Node.js 中生成大量假数据。</p>
<p><img alt="faker-github" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f0ab7a99ade4a11b3435944aae2c55c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-32">安装及示例</h4>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add faker
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> faker <span class="hljs-keyword">from</span> <span class="hljs-string">"faker"</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">generateCustomers</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> customers = []

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> id = <span class="hljs-number">0</span>; id < <span class="hljs-number">50</span>; id++) &#123;
    <span class="hljs-keyword">const</span> firstName = faker.name.firstName()
    <span class="hljs-keyword">const</span> lastName = faker.name.firstName()
    <span class="hljs-keyword">const</span> phoneNumber = faker.phone.phoneNumberFormat()
    <span class="hljs-keyword">const</span> zipCode = faker.address.zipCode()
    <span class="hljs-keyword">const</span> date = faker.date.recent()

    customers.push(&#123;
      id,
      firstName,
      lastName ,
      phoneNumber ,
      zipCode,
      date
    &#125;)
  &#125;

  <span class="hljs-keyword">return</span> &#123; customers &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-33">Mock.js</h3>
<p><a href="http://mockjs.com/examples.html" target="_blank" rel="nofollow noopener noreferrer">Mock.js</a> 是一个模拟数据生成器，可帮助前端开发和原型与后端进度分开，并减少某些单调性，尤其是在编写自动化测试时。</p>
<p><img alt="moackjs-github" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc52cc9447ba4e43b8f86235a1ebdcca~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-34">安装及示例</h5>
<pre><code class="copyable">npm install mockjs
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> Mock <span class="hljs-keyword">from</span> <span class="hljs-string">"mockjs"</span>;

<span class="hljs-keyword">const</span> Random = Mock.Random

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">generateCustomers</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> customers = []

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> id = <span class="hljs-number">0</span>; id < <span class="hljs-number">50</span>; id++) &#123;
    <span class="hljs-keyword">const</span> firstName = Random.first()
    <span class="hljs-keyword">const</span> lastName = Random.last()
    <span class="hljs-keyword">const</span> province = Random.province()
    <span class="hljs-keyword">const</span> date = Random.date()

    customers.push(&#123;
      id,
      firstName,
      lastName ,
      province,
      date
    &#125;)
  &#125;

  <span class="hljs-keyword">return</span> &#123; customers &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h2 data-id="heading-35">🧪 测试工具</h2>
<h3 data-id="heading-36">Jest</h3>
<p><a href="https://www.jestjs.cn/docs/getting-started" target="_blank" rel="nofollow noopener noreferrer">Jest</a> 是一款便捷好用的 JavaScript 测试框架，以简单为核心诉求。您可以通过易于上手且功能丰富的 API 编写测试，从而快速获取结果。</p>
<p><img alt="jest-office" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45618dec2d38426ab86713324d26d179~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-37">安装及示例</h4>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add --dev jest
<span class="copy-code-btn">复制代码</span></code></pre>
<p>测试<code>sum</code>函数，这个函数的功能是两数相加。首先创建 <code>sum.js</code> 文件：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b;
&#125;
<span class="hljs-built_in">module</span>.exports = sum;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，创建名为 <code>sum.test.js</code> 的文件。这个文件包含了实际测试内容：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> sum = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./sum"</span>);

test(<span class="hljs-string">"adds 1 + 2 to equal 3"</span>, <span class="hljs-function">() =></span> &#123;
  expect(sum(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>)).toBe(<span class="hljs-number">3</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将如下代码添加到 <code>package.json</code> 中：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"script"</span>: &#123;
    <span class="hljs-attr">"test"</span>: <span class="hljs-string">"jest"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，运行 <code>yarn test</code> ，Jest 将输出如下信息：</p>
<pre><code class="hljs language-shell copyable" lang="shell">PASS  ./sum.test.js
✓ adds 1 + 2 to equal 3 (5ms)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-38">Mocha</h3>
<p><a href="https://mochajs.cn/" target="_blank" rel="nofollow noopener noreferrer">Mocha</a> 是一个功能丰富的 javascript 测试框架，运行在 node.js 和浏览器中，使异步测试变得简单有趣。Mocha 测试连续运行，允许灵活和准确的报告，同时将未捕获的异常映射到正确的测试用例。</p>
<h3 data-id="heading-39">安装及示例</h3>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add mocha --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，创建名为 <code>test.js</code> 的文件。这个文件包含了实际测试内容：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">var</span> assert = <span class="hljs-built_in">require</span>(<span class="hljs-string">"assert"</span>);

describe(<span class="hljs-string">"Array"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  describe(<span class="hljs-string">"#indexOf()"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    it(<span class="hljs-string">"should return -1 when the value is not present"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      assert.equal([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>].indexOf(<span class="hljs-number">4</span>), -<span class="hljs-number">1</span>);
    &#125;);
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将如下代码添加到 <code>package.json</code> 中：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"script"</span>: &#123;
    <span class="hljs-attr">"test"</span>: <span class="hljs-string">"mocha"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，运行 <code>yarn test</code> ，Mocha 将输出如下信息：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> ./node_modules/mocha/bin/mocha</span>

  Array
    #indexOf()
      ✓ should return -1 when the value is not present


  1 passing (9ms)
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h2 data-id="heading-40">👨‍💻 进程管理器与运行器</h2>
<h3 data-id="heading-41">Nodemon</h3>
<p><a href="https://www.npmjs.com/package/nodemon" target="_blank" rel="nofollow noopener noreferrer">nodemon</a>用来监视 node.js 应用程序中的任何更改并自动重启服务,非常适合用在开发环境中。</p>
<p>nodemon 将监视启动目录中的文件，如果有任何文件更改，nodemon 将自动重新启动 node 应用程序。</p>
<h4 data-id="heading-42">安装及示例</h4>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add  nodemon global
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>server.js</code>表示一个 Node.js 入口文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"start"</span>: <span class="hljs-string">"nodemon server.js"</span>,
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-43">PM2</h3>
<p><a href="https://www.npmjs.com/package/pm2" target="_blank" rel="nofollow noopener noreferrer">PM2</a> 是一个具有内置负载均衡器的 Node.js 应用程序的生产流程管理器。有了它，你就可以让应用程序永远保持活跃，可以在不停机的前提下重新加载它们，并简化常见的系统管理任务。</p>
<p><img alt="p2-github" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac4eefa000cb4664b0a208b92d335efa~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-44">安装及示例</h5>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> yarn add global pm2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可以像下面一样启动任何应用程序（Node.js、Python、Ruby、$PATH 中的二进制文件……）</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> pm2 start app.js</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，你的应用将被守护、监控并永远保持活跃。有关流程管理的更多信息<a href="https://pm2.keymetrics.io/docs/usage/quick-start/" target="_blank" rel="nofollow noopener noreferrer">见此</a>：</p>
<p>应用程序启动后，你就可以轻松管理它们。可以通过以下方法列出所有正在运行的应用程序：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> pm2 ls</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07e62e1a02c640aa88a33e986b4f437d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>查阅<a href="https://pm2.io/" target="_blank" rel="nofollow noopener noreferrer">官方文档</a>，以获取 PM2 功能给的完整列表。</p>
<h3 data-id="heading-45">Concurrently</h3>
<p><a href="https://www.npmjs.com/package/concurrently" target="_blank" rel="nofollow noopener noreferrer">Concurrently</a>简单而直接——可同时运行多条命令的实用工具。</p>
<p><img alt="Concurrently-github" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/912f956311fb4c589936e6dd03a0a113~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-46">安装及示例</h5>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add concurrently global
<span class="copy-code-btn">复制代码</span></code></pre>
<p>时启动前端 webpack 项目和 后端 node 项目</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// package.json   同</span>
<span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-attr">"start"</span>: <span class="hljs-string">"concurrently \"webpack-dev-server\" \"nodemon server.js\""</span>,
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h2 data-id="heading-47">Web sockets</h2>
<h3 data-id="heading-48">Socket.io</h3>
<p><a href="https://socketio.bootcss.com/" target="_blank" rel="nofollow noopener noreferrer">Socket.IO</a> 支持实时、双向、基于事件的通信功能。它能够运行在各类平台、浏览器及设备之上，且拥有良好的可靠性与速度表现。</p>
<p><img alt="Socket.io-office" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67c0f960a6234559ba907592559c04b7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-49">安装及示例</h4>
<p><a href="https://socketio.bootcss.com/get-started/chat/" target="_blank" rel="nofollow noopener noreferrer">官方教程</a></p>
<h3 data-id="heading-50">WS</h3>
<p><a href="https://www.npmjs.com/package/ws" target="_blank" rel="nofollow noopener noreferrer">WS</a>易于使用、快速且经过全面测试的 WebSocket 客户端与服务器实现。同时也是一套强大、抽象度更低且几乎能够与 Socket.io 相媲美的替代方案。</p>
<p><a href="https://www.npmjs.com/package/ws" target="_blank" rel="nofollow noopener noreferrer">官方教程</a></p>
<hr>
<h2 data-id="heading-51">最后</h2>
<p>在日常工作中你还使用哪些 <strong>NPM 工具库</strong>呢？欢迎在评论区留下的你的见解！</p>
<p>觉得有收获的朋友欢迎<strong>点赞</strong>，<strong>关注</strong>一波!</p>
<h2 data-id="heading-52">往期文章</h2>
<p>react 构建系列</p>
<ol>
<li><a href="https://juejin.cn/post/6947872709208457253" target="_blank">企业级前端开发规范如何搭建 🛠</a></li>
<li><a href="https://juejin.cn/post/6947874258324946952" target="_blank">「React Build」之集成 Webpack5/React17</a></li>
<li><a href="https://juejin.cn/post/6947875008840466463" target="_blank">「React Build」之集成 CSS/Less/Sass/Antd</a></li>
<li><a href="https://juejin.cn/post/6947875454783062024" target="_blank">「React Build」之集成图片/字体</a></li>
<li><a href="https://juejin.cn/post/6948233242981957640" target="_blank">「React Build」之集成 Redux/Typescript</a></li>
<li><a href="https://juejin.cn/post/6948959158783705124" target="_blank">「React Build」之使用 Redux-thunk 实现 Redux 异步操作</a></li>
<li><a href="https://juejin.cn/post/6950162473106276360" target="_blank">「React Build」之集成 React-Router/Antd Menu 实现路由权限</a></li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            