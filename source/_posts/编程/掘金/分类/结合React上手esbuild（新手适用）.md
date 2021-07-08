
---
title: '结合React上手esbuild（新手适用）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77de6c503c474a079d940de2771715d5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 01:44:44 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77de6c503c474a079d940de2771715d5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我们都知道react有一个官方的脚手架create-react-app，一条命令就可以让你使用react编写代码，但是在这个脚手架中react代码的打包过程对我们是完全隐藏的。</p>
<p>对于一个新手来说，比如我刚接触到这个工具的时候是充满了疑惑的，为什么我不能<code>npm install react react-dom</code>然后直接使用<code>script</code>标签引入呢？为什么这些代码要打包才可以使用？打包很复杂吗？怎么进行打包呢？</p>
<p>上面这些问题我们暂且不做回答，下面直接使用esbuild这个打包工具，带大家从零开始制作一个简单的react页面。</p>
<p>esbuild是一个比较新的打包工具，这里是它的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fesbuild.github.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://esbuild.github.io/" ref="nofollow noopener noreferrer">官方文档</a>，相较于create-react-app使用的webpack而言，它的优点是快，缺点是不支持css module等特性。当然了，如果你一定要使用css module的话，那么很抱歉这篇文章不能帮助到你</p>
<h3 data-id="heading-0">开始动手</h3>
<h4 data-id="heading-1">1. 初始化</h4>
<p>确定你已经安装好了<a href="https://link.juejin.cn/?target=http%3A%2F%2Fnodejs.cn%2Fdownload%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://nodejs.cn/download/" ref="nofollow noopener noreferrer">node</a>和<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/" ref="nofollow noopener noreferrer">npm</a>，然后打开电脑的命令行，新建一个文件夹，并运行<code>npm init -y</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77de6c503c474a079d940de2771715d5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">2. 安装依赖</h4>
<p>安装需要用到的依赖，我们会用到<code>react</code> <code>react-dom</code> <code>esbuild</code>这三个包</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbc45fdceb834fcca4c1325f76f162b5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">3. 新建文件</h4>
<p>打开你的 vs code或者其他编辑器，新建一个html文件，以及一个src文件夹（包含一个css文件和一个jsx文件）</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12352d3360fd40e7a4a7fc353ee95a3a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">4. 写代码</h4>
<p>在你的jsx和css中随便写点什么</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'./style.css'</span>;

<span class="hljs-keyword">const</span> root = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>);
root.className = <span class="hljs-string">'root'</span>;
<span class="hljs-built_in">document</span>.body.appendChild(root);

<span class="hljs-keyword">const</span> App = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'esbuild'</span>></span>Hello, Esbuild!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">className</span>=<span class="hljs-string">'react'</span>></span>Hello, React!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
&#125;;

ReactDOM.render(
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>,
    root,
);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.esbuild</span> &#123;
    <span class="hljs-attribute">color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">247</span>, <span class="hljs-number">209</span>, <span class="hljs-number">71</span>);
&#125;

<span class="hljs-selector-class">.react</span> &#123;
    <span class="hljs-attribute">color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">97</span>, <span class="hljs-number">218</span>, <span class="hljs-number">251</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">5. 进行打包</h4>
<p>在你的package.json文件的script标签中加入<code>"build": "esbuild src/app.jsx --outfile=build/index.js --bundle"</code>，这代表以src文件夹中的app.jsx为入口，build文件夹的index.js为输出进行打包。
然后在终端中输入<code>npm run build</code>命令</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a10cba379dc44ccbaa99865cdfa70a5c~tplv-k3u1fbpfcp-watermark.image" alt="Xnip2021-07-07_17-03-19.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在你的目录下面多出了一个build文件夹和两个文件</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7aa8c464f0244246bcc382ce48ff6443~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">6. 查看效果</h4>
<p>这时我们打开之前新建的html文件，将其初始化然后将build文件夹中的两个文件链接上去</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"./build/index.css"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Esbuild and React<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./build/index.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后可以使用vs code中的live server打开或者直接通过浏览器打开，页面就可以正常显示了</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d0983d4915b4631a55916985c759b52~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">7. 完善功能</h4>
<p>仅有这些的话，对于开发而言还远远不够，如何达到原生js开发时的实时更改的效果呢，我们可以在package.json中之前build命令后面加一个<code>--watch</code>或者增加一个watch命令<code>    "watch": "esbuild src/app.jsx --outfile=build/index.js --bundle --watch"</code>然后借助vs code的live server插件就可以实现实时的效果了。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f8ca3b5dc93484c9705812645ba420c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">总结</h3>
<p>本文结合react对esbuid这个打包工具进行了简单使用，最后一步实现方法并不是唯一的，还可以使用esbuild的serve功能实现，大家可以阅读<a href="https://link.juejin.cn/?target=https%3A%2F%2Fesbuild.github.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://esbuild.github.io/" ref="nofollow noopener noreferrer">官方文档</a>探索。</p>
<p>本文写作的初衷是为初学者推荐一款合适的打包工具，在我看来，webpack这个工具非常的臃肿，尽管它功能非常丰富，但是初学之时并不是很友好，esbuild除了打包速度飞快，对于ts文件的处理也是非常友好，不需要设置各种loader，配置简单，是一个非常“轻”的选择。
除此之外，vite也是一个不错的选择。</p></div>  
</div>
            