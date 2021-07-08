
---
title: 'TS在React项目中的应用实践（附项目源码）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0dfc3c409856446bad444a23d80c6241~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 02:30:44 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0dfc3c409856446bad444a23d80c6241~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>前置阅读：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.tslang.cn%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.tslang.cn/index.html" ref="nofollow noopener noreferrer">TypeScript 中文网</a></p>
</blockquote>
<h1 data-id="heading-0">目录</h1>
<ul>
<li><strong>React项目集成TS</strong>
<ul>
<li>集成流程概览</li>
<li>安装依赖</li>
<li>为什么不使用ts-loader</li>
<li>bebel.config.json修改</li>
<li>webpack修改</li>
<li>.eslintrc修改</li>
<li>package.json配置</li>
<li>声明文件的作用</li>
</ul>
</li>
<li><strong>TS在项目中应该怎么去写？</strong>
<ul>
<li>应用到哪些地方？</li>
<li>怎么应用 ？（附todoList项目源码）</li>
</ul>
</li>
</ul>
<h2 data-id="heading-1">React项目集成TS</h2>
<h3 data-id="heading-2">集成流程概览</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0dfc3c409856446bad444a23d80c6241~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210705172133448.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">安装依赖</h3>
<p>@babel/preset-typescript 是babel转义ts</p>
<p>@types/react @types/react-dom 是react依赖的类型库</p>
<p>@types/webpack-env 是webpack的全局属性类型库</p>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add typescript @babel/preset-typescript @types/react @types/react-dom @types/webpack-env -D 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">为什么不使用ts-loader</h3>
<ul>
<li>只管理一个编译器更轻松</li>
<li>babel更快，原因具体可见 <a href="https://juejin.cn/post/6968636129239105549" target="_blank" title="https://juejin.cn/post/6968636129239105549">为什么说用 babel 编译 typescript 是更好的选择</a></li>
<li>babel加了 polyfills  做了低版本的兼容处理，而tsloader没有</li>
</ul>
<p>当然是有缺点的，但是缺点可以避免，总收益是大的所以就用babel</p>
<ul>
<li>无法实时完成项目的类型检查，检查提示错误是IDE的提示，这个优化方法 就是每次开发完成后 执行一下类型检查 <code>tsc -noEmit</code></li>
</ul>
<h3 data-id="heading-5">bebel.config.json修改</h3>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"presets"</span>: [<span class="hljs-string">"@babel/env"</span>, <span class="hljs-string">"@babel/preset-react"</span>, <span class="hljs-string">"@babel/preset-typescript"</span>], <span class="hljs-comment">// 新增</span>
  <span class="hljs-attr">"plugins"</span>: [<span class="hljs-string">"react-hot-loader/babel"</span>]
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">webpack修改</h3>
<blockquote>
<p>全部react文件更名为TSX格式 原因是tsx语义更强</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function">(<span class="hljs-params">env, args</span>) =></span> &#123;
<span class="hljs-comment">// prd 模式</span>
  <span class="hljs-keyword">const</span> cssTypePrd = args.env.css === <span class="hljs-string">'prd'</span>

  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./app.tsx'</span>, <span class="hljs-comment">// 入口文件</span>
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [ <span class="hljs-comment">// 配置加载器</span>
        &#123;
          <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(jsx|tsx|js|ts)?$/</span>,<span class="hljs-comment">// 处理es6语法以及jsx语法</span>
          loader: <span class="hljs-string">'babel-loader'</span>,
          <span class="hljs-attr">include</span>: [
            path.resolve(__dirname, <span class="hljs-string">'src'</span>), <span class="hljs-comment">// 使用目录</span>
            path.resolve(__dirname, <span class="hljs-string">'app.tsx'</span>), <span class="hljs-comment">// 使用文件</span>
          ],
        &#125;,
        ]
    &#125;,
    <span class="hljs-attr">resolve</span>: &#123; <span class="hljs-comment">// 新增因为现在的文件变为了 tsx 和ts后缀名所以需要增加两个后缀名 tsx和ts</span>
      <span class="hljs-attr">extensions</span>: [<span class="hljs-string">'.tsx'</span>, <span class="hljs-string">'.ts'</span>, <span class="hljs-string">'.json'</span>, <span class="hljs-string">'.js'</span>], <span class="hljs-comment">// 尝试按顺序解析这些后缀名。如果有多个文件有相同的名字，但后缀名不同，webpack 会解析列在数组首位的后缀的文件 并跳过其余的后缀。</span>
    &#125;,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">.eslintrc修改</h3>
<pre><code class="hljs language-yaml copyable" lang="yaml">&#123;
    <span class="hljs-attr">"extends":</span> [
        <span class="hljs-string">"eslint-config-ali"</span>,
        <span class="hljs-string">"eslint-config-ali/react"</span>,
        <span class="hljs-string">"eslint-config-ali/typescript"</span>, <span class="hljs-string">//</span> <span class="hljs-string">修改项</span>
        <span class="hljs-string">"eslint-config-ali/typescript/react"</span> <span class="hljs-string">//</span> <span class="hljs-string">修改项</span>
    ],
    <span class="hljs-attr">"rules":</span> &#123;
        <span class="hljs-attr">"semi":</span> [<span class="hljs-number">2</span>, <span class="hljs-string">"never"</span>],
        <span class="hljs-attr">"no-console":</span> <span class="hljs-string">"off"</span>,
        <span class="hljs-attr">"react/no-array-index-key":</span> <span class="hljs-string">"off"</span>,
        <span class="hljs-string">"react/prop-types"</span><span class="hljs-string">:"off"</span>
    &#125;,
    <span class="hljs-attr">"globals":</span> &#123; <span class="hljs-string">//</span> <span class="hljs-string">修改项</span>
        <span class="hljs-attr">"GLOBAL_ENV":</span> <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-attr">"ignorePatterns":</span> [ <span class="hljs-string">//</span> <span class="hljs-string">忽略文件夹</span>
        <span class="hljs-string">"dist"</span>,
        <span class="hljs-string">"node_modules"</span>,
        <span class="hljs-string">"*.d.ts"</span>
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">ts-config.json 文件</h3>
<blockquote>
<p>虽然不需要ts-loader来进行转译，但是需要ts-config的配置和IDE协作</p>
</blockquote>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"compilerOptions"</span>: &#123; <span class="hljs-comment">// 编译配置</span>
        <span class="hljs-attr">"jsx"</span>: <span class="hljs-string">"react"</span>,
        <span class="hljs-attr">"types"</span>: [<span class="hljs-string">"node"</span>, <span class="hljs-string">"react"</span>, <span class="hljs-string">"react-dom"</span>, <span class="hljs-string">"webpack-env"</span>], <span class="hljs-comment">// 获取node_modules下的@types下的ts依赖，不写就算add type也没用</span>
        <span class="hljs-attr">"allowSyntheticDefaultImports"</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 允许从没有设置默认导出的模块中默认导入。这并不影响代码的输出，仅为了类型检查</span>
        <span class="hljs-attr">"noEmit"</span>: <span class="hljs-literal">true</span>,  <span class="hljs-comment">// 不生成文件，只做类型检查  </span>
    &#125;,
&#125;
<span class="hljs-comment">// 参考链接 https://segmentfault.com/a/1190000021421461 </span>
<span class="hljs-comment">// https://juejin.cn/post/6844904052094926855#heading-17</span>
<span class="hljs-comment">// 这里没用ts-loader所以tsconfig的作用只有给IDE提示</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">package.json配置</h3>
<pre><code class="hljs language-json copyable" lang="json">    <span class="hljs-string">"typeCheck"</span>: <span class="hljs-string">"tsc --noEmit"</span> <span class="hljs-comment">// 新增 ts类型检查命令 不生产输出文件</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">声明文件的作用</h3>
<blockquote>
<p>在完成这些后会发现less 还有 img文件的import会标红，因为这些文件都需要类型声明 还有全局变量</p>
</blockquote>
<p>新建一个 externals.d.ts</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">declare</span> <span class="hljs-built_in">module</span> <span class="hljs-string">'*.less'</span> &#123; <span class="hljs-comment">// less报错</span>

    <span class="hljs-keyword">const</span> classes: &#123; [className: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">string</span> &#125;;
  
    <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> classes;
  
   &#125;

<span class="hljs-comment">// 文件报错声明</span>
<span class="hljs-keyword">declare</span> <span class="hljs-built_in">module</span> <span class="hljs-string">'*.svg'</span>

<span class="hljs-keyword">declare</span> <span class="hljs-built_in">module</span> <span class="hljs-string">'*.png'</span>

<span class="hljs-keyword">declare</span> <span class="hljs-built_in">module</span> <span class="hljs-string">'*.jpg'</span>

<span class="hljs-keyword">declare</span> <span class="hljs-built_in">module</span> <span class="hljs-string">'*.jpeg'</span>

<span class="hljs-keyword">declare</span> <span class="hljs-built_in">module</span> <span class="hljs-string">'*.gif'</span>

<span class="hljs-keyword">declare</span> <span class="hljs-built_in">module</span> <span class="hljs-string">'*.bmp'</span>

<span class="hljs-keyword">declare</span> <span class="hljs-built_in">module</span> <span class="hljs-string">'*.tiff'</span>

<span class="hljs-comment">// 全局变量</span>
<span class="hljs-keyword">declare</span> <span class="hljs-keyword">var</span> GLOBAL_ENV: <span class="hljs-built_in">string</span>;


<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">TS在项目中应该怎么去写？</h2>
<blockquote>
<p>TS的目的是为了更安全高效的类型提示和检查</p>
</blockquote>
<h3 data-id="heading-12">应用到哪些地方？</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c0f24861fe24b9d90c293c262309ccc~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210705172224295.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">基础知识是哪些？</h3>
<h4 data-id="heading-14">函数类型接口以及类型别名</h4>
<ul>
<li>
<p>两者区别</p>
<ul>
<li>具体可以看这个文章 [<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FSunshowerC%2Fblog%2Fissues%2F7%23" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/SunshowerC/blog/issues/7#" ref="nofollow noopener noreferrer">typescript 中的 interface 和 type 到底有什么区别？</a>](<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FSunshowerC%2Fblog%2Fissues%2F7" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/SunshowerC/blog/issues/7" ref="nofollow noopener noreferrer">github.com/SunshowerC/…</a>)</li>
</ul>




















<table><thead><tr><th>名称</th><th>不同点</th><th>相同点</th></tr></thead><tbody><tr><td>interface</td><td>没有联合类型 以及 元组</td><td>都可以描述对象和函数，都允许扩展</td></tr><tr><td>type</td><td>无法声明合并</td><td>都可以描述对象和函数，都允许扩展</td></tr></tbody></table>
</li>
</ul>
<h4 data-id="heading-15">泛型</h4>
<ul>
<li>
<p>函数泛型</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span><<span class="hljs-title">T</span>>(<span class="hljs-params">name:T</span>) => </span>&#123;
<span class="hljs-built_in">console</span>.log(name)
&#125;

test<<span class="hljs-built_in">string</span>>(<span class="hljs-string">'小明'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>class泛型</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Test</span><<span class="hljs-title">T</span>></span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">params:T</span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(params)
    &#125;
&#125;

<span class="hljs-keyword">new</span> Test<<span class="hljs-built_in">Number</span>>(<span class="hljs-number">1</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>interface泛型</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">interface</span> Test<T> &#123;
<span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>,
    <span class="hljs-attr">info</span>: T
&#125;

<span class="hljs-keyword">const</span> test:Test<<span class="hljs-built_in">string</span>> = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'小米'</span>,
    <span class="hljs-attr">age</span>:<span class="hljs-number">11</span>,
    <span class="hljs-attr">info</span>: <span class="hljs-string">'我是一个学生'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-16">枚举</h4>
<ul>
<li>
<p>维护常量</p>
<ul>
<li>建议写法</li>
</ul>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-built_in">enum</span> Test &#123;
    NAME = <span class="hljs-string">'name'</span>,
    AGE = <span class="hljs-string">'age'</span>,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-17">typeof 与 keyof 的用法</h4>
<ul>
<li>
<p>typeof</p>
<ul>
<li>
<p>给枚举以及 定义类型的值用</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">const</span> a: <span class="hljs-built_in">number</span> = <span class="hljs-number">3</span>

<span class="hljs-comment">// 相当于: const b: number = 4</span>
<span class="hljs-keyword">const</span> b: <span class="hljs-keyword">typeof</span> a = <span class="hljs-number">4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p>keyof</p>
<ul>
<li>
<p>只能给类型用</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">interface</span> Point &#123;
    <span class="hljs-attr">x</span>: <span class="hljs-built_in">number</span>;
    y: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-comment">// type keys = "x" | "y"</span>
<span class="hljs-keyword">type</span> keys = keyof Point;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
</ul>
<h3 data-id="heading-18">怎么应用 ？</h3>
<h4 data-id="heading-19">写一个简单的todoList</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fyu648813710%2Fmy-react-cli-template%2Ftree%2Ftodo-list-ts" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/yu648813710/my-react-cli-template/tree/todo-list-ts" ref="nofollow noopener noreferrer">项目地址</a></p>
<ul>
<li>函数组件定义</li>
<li>函数组件的props定义</li>
<li>hooks的定义</li>
<li>自己方法的定义</li>
</ul>
<h3 data-id="heading-20">注意的坑有？</h3>
<ul>
<li>class组件的defaultprops 无法和props的类型相关联，但是函数组件可以 ，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2FWayou%2Fp%2Freact_typescript_default_props.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/Wayou/p/react_typescript_default_props.html" ref="nofollow noopener noreferrer">参考链接</a>， （可以看一下当前的 react的定义类型文件。）</li>
<li>chilren的定义 需要 写 React.ReactNode ,其他 ReactNodeArray 与 ReactChild 无法容错</li>
<li>函数组件如果使用<code>React.FC</code>类型无法直接返回 Arr.map 结构，因为Arr.map有可能返回为<code>[]</code></li>
</ul>
<h3 data-id="heading-21">扩展阅读</h3>
<h4 data-id="heading-22">TS的内置函数</h4>
<p>TS的lib 声明文件 有一些内置的工具函数可以用</p>
<ul>
<li>
<p>Partial</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// 让对象属性的所有属性都是可选的</span>
<span class="hljs-keyword">interface</span> User &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>
&#125;

<span class="hljs-comment">/*
* &#123;
 name?: string,
 age?:string
&#125;
*/</span>
<span class="hljs-keyword">type</span> Test = Partial<User>

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>Required</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// 全部属性转为必需属性</span>
<span class="hljs-keyword">interface</span> User &#123;
    name?: <span class="hljs-built_in">string</span>,
    age?: <span class="hljs-built_in">number</span>
&#125;

<span class="hljs-comment">/*
* &#123;
 name: string,
 age:string
&#125;
*/</span>
<span class="hljs-keyword">type</span> Test = Required<User>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>Readonly</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// 全部属性转为只读属性</span>
<span class="hljs-keyword">interface</span> User &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>
&#125;

<span class="hljs-comment">/*
* &#123;
 readonly name: string,
 readonly age:string
&#125;
*/</span>
<span class="hljs-keyword">type</span> Test = Readonly<User>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>Pick</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 获取全部对象类型某个属性</span>
interface User &#123;
    <span class="hljs-attr">name</span>: string,
    <span class="hljs-attr">age</span>: number
&#125;

<span class="hljs-comment">/*
* &#123;
 name: string,
 &#125;
*/</span>
type Test = Pick<User, <span class="hljs-string">'name'</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>Record</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// 对象类型中赋给某个新的对象类型</span>
<span class="hljs-keyword">interface</span> User &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>
&#125;

<span class="hljs-comment">/*
* &#123;
 test: User,
 &#125;
*/</span>
<span class="hljs-keyword">type</span> Test = Record<<span class="hljs-string">'test'</span>, User>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>Omit</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// 对象类型排除某个属性</span>
<span class="hljs-comment">// 对象类型中赋给某个新的对象类型</span>
<span class="hljs-keyword">interface</span> User &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>
&#125;

<span class="hljs-comment">/*
* &#123;
    name: string,
 &#125;
*/</span>
<span class="hljs-keyword">type</span> Test = Omit<User, <span class="hljs-string">'age'</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-23">TS的<code>?</code>和<code>！</code>操作符用法</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fe2tox%2Fblog%2Fissues%2F9" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/e2tox/blog/issues/9" ref="nofollow noopener noreferrer">TypeScript中的问号 ? 与感叹号 ! 是什么意思？</a></p>
<h2 data-id="heading-24">参考链接</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fe2tox%2Fblog%2Fissues%2F9" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/e2tox/blog/issues/9" ref="nofollow noopener noreferrer">TypeScript中的问号 ? 与感叹号 ! 是什么意思？</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2FWayou%2Fp%2Freact_typescript_default_props.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/Wayou/p/react_typescript_default_props.html" ref="nofollow noopener noreferrer">React + TypeScript 默认 Props 的处理</a></li>
<li><a href="https://juejin.cn/post/6968636129239105549" target="_blank" title="https://juejin.cn/post/6968636129239105549">为什么说用 babel 编译 typescript 是更好的选择</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FSunshowerC%2Fblog%2Fissues%2F7%23" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/SunshowerC/blog/issues/7#" ref="nofollow noopener noreferrer">typescript 中的 interface 和 type 到底有什么区别？</a></li>
</ul></div>  
</div>
            