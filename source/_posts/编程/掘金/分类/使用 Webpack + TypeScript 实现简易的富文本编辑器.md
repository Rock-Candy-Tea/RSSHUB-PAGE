
---
title: '使用 Webpack + TypeScript 实现简易的富文本编辑器'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d79681362cb47b0ac02b15f5d484e9b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 03 Apr 2021 21:19:58 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d79681362cb47b0ac02b15f5d484e9b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt="artem-sapegin-DErxVSSQNdM-unsplash.jpg" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d79681362cb47b0ac02b15f5d484e9b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>图片来源 <a href="https://unsplash.com/photos/b18TRXc8UPQ" target="_blank" rel="nofollow noopener noreferrer">unsplash.com/photos/b18T…</a></p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>写这篇文章的目的是为了记录自己第一次实现一个非常简易的富文本编辑器的过程，项目使用到了 Webpack 和 TypeScript。</p>
<h2 data-id="heading-1">项目介绍</h2>
<h3 data-id="heading-2">项目目录文件</h3>
<pre><code class="copyable">  |-- 富文本编辑器,
      |-- README.md,
      |-- index.html,
      |-- package-lock.json,
      |-- package.json,
      |-- tsconfig.json,
      |-- webpack.build.config.js,
      |-- webpack.config.js,
      |-- dist,// 打包生成的文件
      |   |-- yangEditor.js,
      |-- lib,
      |   |-- index.css,
      |   |-- index.js,
      |   |-- yangEditor.ts,
      |-- src,
          |-- index.js,
  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>项目安装的依赖</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"clean-webpack-plugin"</span>: <span class="hljs-string">"^3.0.0"</span>,
<span class="hljs-string">"css-loader"</span>: <span class="hljs-string">"^5.2.0"</span>,
<span class="hljs-string">"html-webpack-plugin"</span>: <span class="hljs-string">"^5.3.1"</span>,
<span class="hljs-string">"style-loader"</span>: <span class="hljs-string">"^2.0.0"</span>,
<span class="hljs-string">"ts-loader"</span>: <span class="hljs-string">"^8.1.0"</span>,
<span class="hljs-string">"typescript"</span>: <span class="hljs-string">"^4.2.3"</span>,
<span class="hljs-string">"webpack"</span>: <span class="hljs-string">"^5.30.0"</span>,
<span class="hljs-string">"webpack-cli"</span>: <span class="hljs-string">"^4.6.0"</span>,
<span class="hljs-string">"webpack-dev-server"</span>: <span class="hljs-string">"^3.11.2"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3"><code>webpack.config.js</code> 开发环境的 <code>Webpack</code> 配置</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>)
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"html-webpack-plugin"</span>)

<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">"development"</span>,
    <span class="hljs-attr">entry</span>: <span class="hljs-string">"./src/index.js"</span>,
    <span class="hljs-attr">devServer</span>: &#123;
        <span class="hljs-attr">port</span>: <span class="hljs-number">8089</span>, <span class="hljs-comment">// 设置端口号</span>
    &#125;,

    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.ts$/</span>,
                use: <span class="hljs-string">"ts-loader"</span>,
                <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span>
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
                use: [<span class="hljs-string">"style-loader"</span>, <span class="hljs-string">"css-loader"</span>]
            &#125;
        ]
    &#125;,

    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
            <span class="hljs-attr">template</span>: <span class="hljs-string">"./index.html"</span>
        &#125;)
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4"><code>webpack.build.config.js</code> 生产环境的 <code>Webpack</code> 配置</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>)

<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">"production"</span>,
    <span class="hljs-attr">entry</span>: <span class="hljs-string">"./lib/index.js"</span>,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">"yangEditor.js"</span>,
        <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">"./dist"</span>),
        <span class="hljs-attr">libraryTarget</span>: <span class="hljs-string">'umd'</span>
    &#125;,
    
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.ts$/</span>,
                use: <span class="hljs-string">"ts-loader"</span>,
                <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span>
            &#125;,
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
                use: [<span class="hljs-string">"style-loader"</span>, <span class="hljs-string">"css-loader"</span>]
            &#125;
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">项目运行命令</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"scripts"</span>: &#123;
<span class="hljs-string">"dev"</span>: <span class="hljs-string">"webpack serve --open Chrome.exe"</span>,
<span class="hljs-string">"build"</span>: <span class="hljs-string">"webpack --config webpack.build.config.js"</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">document.execCommand</h2>
<blockquote>
<p>document.execCommand 已废弃</p>
</blockquote>
<p>当一个HTML文档切换到设计模式时，<code>document</code>暴露 <a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Document/execCommand" target="_blank" rel="nofollow noopener noreferrer">execCommand</a> 方法，该方法允许运行命令来操纵可编辑内容区域的元素,本次项目实现富文本编辑器就是使用该它。</p>
<h3 data-id="heading-7">语法</h3>
<ul>
<li><code>bool = document.execCommand(aCommandName, aShowDefaultUI, aValueArgument)</code>，返回值是一个 <code>Boolean</code> ，如果是 <code>false</code> 则表示<code>操作不被支持</code>或<code>未被启用</code>。</li>
</ul>
<h3 data-id="heading-8">参数</h3>
<ul>
<li><code>aCommandName</code>:一个 DOMString ，命令的名称。</li>
<li><code>aShowDefaultUI</code>:是否展示用户界面，一般为 false。</li>
<li><code>aValueArgument</code>:一些命令（例如insertImage）需要额外的参数（insertImage需要提供插入image的url），默认为null。</li>
</ul>
<h2 data-id="heading-9">简易富文本具体实现</h2>
<h3 data-id="heading-10">yangEditor.ts</h3>
<blockquote>
<p>该文件在lib/yangEditor.ts</p>
</blockquote>
<p>首先我们创建一个类，传入一个<code>DOM</code>节点字符串，获取<code>DOM</code>节点。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">YangEditor</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">dom: string</span>)</span> &#123;
<span class="hljs-keyword">if</span> (!dom) &#123;
<span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'请传入DOM节点！！！'</span>);
&#125;
<span class="hljs-keyword">let</span> editWrapper: HTMLElement = <span class="hljs-built_in">document</span>.getElementById(dom);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">Command 指令</h3>
<blockquote>
<p>指令有设置标题，设置字体颜色，设置字体加粗。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 指令数组</span>
<span class="hljs-keyword">const</span> actions = [
&#123;
<span class="hljs-attr">command</span>: <span class="hljs-string">'formatblock'</span>,
<span class="hljs-attr">values</span>: [
&#123; <span class="hljs-attr">text</span>: <span class="hljs-string">'- 设置标题大小 -'</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">'selected'</span> &#125;,
&#123; <span class="hljs-attr">text</span>: <span class="hljs-string">'H1标题'</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">'h1'</span> &#125;,
&#123; <span class="hljs-attr">text</span>: <span class="hljs-string">'H2标题'</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">'h2'</span> &#125;,
&#123; <span class="hljs-attr">text</span>: <span class="hljs-string">'H3标题'</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">'h3'</span> &#125;,
&#123; <span class="hljs-attr">text</span>: <span class="hljs-string">'H4标题'</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">'h4'</span> &#125;,
&#123; <span class="hljs-attr">text</span>: <span class="hljs-string">'H5标题'</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">'h5'</span> &#125;,
],
&#125;,
&#123;
<span class="hljs-attr">command</span>: <span class="hljs-string">'forecolor'</span>,
<span class="hljs-attr">values</span>: [
&#123; <span class="hljs-attr">text</span>: <span class="hljs-string">'- 设置字体颜色 -'</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">'selected'</span> &#125;,
&#123; <span class="hljs-attr">text</span>: <span class="hljs-string">'红色'</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">'red'</span> &#125;,
&#123; <span class="hljs-attr">text</span>: <span class="hljs-string">'蓝色'</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">'blue'</span> &#125;,
&#123; <span class="hljs-attr">text</span>: <span class="hljs-string">'绿色'</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">'green'</span> &#125;,
&#123; <span class="hljs-attr">text</span>: <span class="hljs-string">'黑色'</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">'black'</span> &#125;,
],
&#125;,
&#123;
<span class="hljs-attr">command</span>: <span class="hljs-string">'bold'</span>,
<span class="hljs-attr">values</span>: [
&#123; <span class="hljs-attr">text</span>: <span class="hljs-string">'- 设置字体粗体 -'</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">'selected'</span> &#125;,
&#123; <span class="hljs-attr">text</span>: <span class="hljs-string">'粗体'</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">''</span> &#125;,
],
&#125;,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">创建<code>DOM</code>节点</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 创建DOM节点</span>
private createDOM(type: string, className?: string): HTMLElement &#123;
<span class="hljs-keyword">let</span> dom = <span class="hljs-built_in">document</span>.createElement(type);
dom.className = className || <span class="hljs-string">''</span>;
<span class="hljs-keyword">return</span> dom;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">动态创建 <code>select</code> 标签</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 创建select节点</span>
private createSelectDOM(commandItem: ActionsItem): HTMLSelectElement &#123;
<span class="hljs-keyword">let</span> select = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'select'</span>);
commandItem.values.forEach(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
select.add(<span class="hljs-keyword">new</span> Option(item.text, item.value));
select.id = <span class="hljs-string">`<span class="hljs-subst">$&#123;commandItem.command&#125;</span>`</span>;
&#125;);

select.onchange = <span class="hljs-function">() =></span> &#123;
                       <span class="hljs-comment">// select标签onchange事件，调用execCommand方法</span>
<span class="hljs-built_in">this</span>.execCommand(commandItem.command, select.options[select.selectedIndex].value);
&#125;;
<span class="hljs-keyword">return</span> select;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">使用 <code>document.execCommand</code> 方法</h3>
<blockquote>
<p>在select标签调佣onchange事件，调用execCommand方法。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">private execCommand(cmd: string, <span class="hljs-attr">value</span>: string): <span class="hljs-keyword">void</span> &#123;
<span class="hljs-comment">//execCommand bool = document.execCommand(aCommandName, aShowDefaultUI, aValueArgument)</span>
<span class="hljs-comment">// aCommandName 一个 DOMString ，命令的名称。</span>
<span class="hljs-comment">//aShowDefaultUI 一个 Boolean， 是否展示用户界面，一般为 false</span>
<span class="hljs-comment">//aValueArgument 一些命令（例如insertImage）需要额外的参数（insertImage需要提供插入image的url），默认为null。</span>
<span class="hljs-built_in">document</span>.execCommand(cmd, <span class="hljs-literal">false</span>, value);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">使用方法</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; YangEditor &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../lib/index"</span>
<span class="hljs-keyword">new</span> YangEditor(<span class="hljs-string">"yangEdit"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">实现效果</h2>
<p><img alt="tutieshi_640x320_15s.gif" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34a391612cf94b0c839f60a21b97c5c9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-17">项目源码</h2>
<p><a href="https://github.com/yanglvyou/yangEditor" target="_blank" rel="nofollow noopener noreferrer">编辑器源码地址</a></p>
<h2 data-id="heading-18">参考资料</h2>
<p><a href="https://developer.mozilla.org/zh-CN/docs/Web/API/Document/execCommand" target="_blank" rel="nofollow noopener noreferrer">MDN execCommand</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            