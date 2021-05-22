
---
title: '新进webpack打包系列一'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2437'
author: 掘金
comments: false
date: Fri, 21 May 2021 19:55:06 GMT
thumbnail: 'https://picsum.photos/400/300?random=2437'
---

<div>   
<div class="markdown-body"><style>.markdown-body .octicon&#123;display:inline-block;fill:currentColor;vertical-align:text-bottom&#125;.markdown-body .anchor&#123;float:left;line-height:1;margin-left:-20px;padding-right:4px&#125;.markdown-body .anchor:focus&#123;outline:none&#125;.markdown-body h1 .octicon-link,.markdown-body h2 .octicon-link,.markdown-body h3 .octicon-link,.markdown-body h4 .octicon-link,.markdown-body h5 .octicon-link,.markdown-body h6 .octicon-link&#123;color:#1b1f23;vertical-align:middle;visibility:hidden&#125;.markdown-body h1:hover .anchor,.markdown-body h2:hover .anchor,.markdown-body h3:hover .anchor,.markdown-body h4:hover .anchor,.markdown-body h5:hover .anchor,.markdown-body h6:hover .anchor&#123;text-decoration:none&#125;.markdown-body h1:hover .anchor .octicon-link,.markdown-body h2:hover .anchor .octicon-link,.markdown-body h3:hover .anchor .octicon-link,.markdown-body h4:hover .anchor .octicon-link,.markdown-body h5:hover .anchor .octicon-link,.markdown-body h6:hover .anchor .octicon-link&#123;visibility:visible&#125;.markdown-body h1:hover .anchor .octicon-link:before,.markdown-body h2:hover .anchor .octicon-link:before,.markdown-body h3:hover .anchor .octicon-link:before,.markdown-body h4:hover .anchor .octicon-link:before,.markdown-body h5:hover .anchor .octicon-link:before,.markdown-body h6:hover .anchor .octicon-link:before&#123;width:16px;height:16px;content:" ";display:inline-block;background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' aria-hidden='true'%3E%3Cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z'/%3E%3C/svg%3E")&#125;.markdown-body&#123;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:#24292e;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji;font-size:16px;line-height:1.5;word-wrap:break-word&#125;.markdown-body details&#123;display:block&#125;.markdown-body summary&#123;display:list-item&#125;.markdown-body a&#123;background-color:initial&#125;.markdown-body a:active,.markdown-body a:hover&#123;outline-width:0&#125;.markdown-body strong&#123;font-weight:inherit;font-weight:bolder&#125;.markdown-body h1&#123;margin:.67em 0&#125;.markdown-body img&#123;border-style:none&#125;.markdown-body code,.markdown-body kbd,.markdown-body pre&#123;font-family:monospace,monospace;font-size:1em&#125;.markdown-body hr&#123;box-sizing:initial;overflow:visible&#125;.markdown-body input&#123;font:inherit;margin:0;overflow:visible&#125;.markdown-body [type=checkbox]&#123;box-sizing:border-box;padding:0&#125;.markdown-body *&#123;box-sizing:border-box&#125;.markdown-body input&#123;font-family:inherit;font-size:inherit;line-height:inherit&#125;.markdown-body a&#123;color:#0366d6;text-decoration:none&#125;.markdown-body a:hover&#123;text-decoration:underline&#125;.markdown-body strong&#123;font-weight:600&#125;.markdown-body hr&#123;height:0;margin:15px 0;overflow:hidden;background:transparent;border-bottom:1px solid #dfe2e5&#125;.markdown-body hr:after,.markdown-body hr:before&#123;display:table;content:""&#125;.markdown-body hr:after&#123;clear:both&#125;.markdown-body table&#123;border-spacing:0;border-collapse:collapse&#125;.markdown-body td,.markdown-body th&#123;padding:0&#125;.markdown-body details summary&#123;cursor:pointer&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:0;margin-bottom:0&#125;.markdown-body h1&#123;font-size:32px&#125;.markdown-body h1,.markdown-body h2&#123;font-weight:600&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:20px&#125;.markdown-body h3,.markdown-body h4&#123;font-weight:600&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5,.markdown-body h6&#123;font-weight:600&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body p&#123;margin-top:0;margin-bottom:10px&#125;.markdown-body blockquote&#123;margin:0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:0;margin-top:0;margin-bottom:0&#125;.markdown-body ol ol,.markdown-body ul ol&#123;list-style-type:lower-roman&#125;.markdown-body ol ol ol,.markdown-body ol ul ol,.markdown-body ul ol ol,.markdown-body ul ul ol&#123;list-style-type:lower-alpha&#125;.markdown-body dd&#123;margin-left:0&#125;.markdown-body code,.markdown-body pre&#123;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px&#125;.markdown-body pre&#123;margin-top:0;margin-bottom:0&#125;.markdown-body input::-webkit-inner-spin-button,.markdown-body input::-webkit-outer-spin-button&#123;margin:0;-webkit-appearance:none;appearance:none&#125;.markdown-body :checked+.radio-label&#123;position:relative;z-index:1;border-color:#0366d6&#125;.markdown-body .border&#123;border:1px solid #e1e4e8!important&#125;.markdown-body .border-0&#123;border:0!important&#125;.markdown-body .border-bottom&#123;border-bottom:1px solid #e1e4e8!important&#125;.markdown-body .rounded-1&#123;border-radius:3px!important&#125;.markdown-body .bg-white&#123;background-color:#fff!important&#125;.markdown-body .bg-gray-light&#123;background-color:#fafbfc!important&#125;.markdown-body .text-gray-light&#123;color:#6a737d!important&#125;.markdown-body .pl-3,.markdown-body .px-3&#123;padding-left:16px!important&#125;.markdown-body .px-3&#123;padding-right:16px!important&#125;.markdown-body .f6&#123;font-size:12px!important&#125;.markdown-body .lh-condensed&#123;line-height:1.25!important&#125;.markdown-body .text-bold&#123;font-weight:600!important&#125;.markdown-body .pl-c&#123;color:#6a737d&#125;.markdown-body .pl-c1,.markdown-body .pl-s .pl-v&#123;color:#005cc5&#125;.markdown-body .pl-e,.markdown-body .pl-en&#123;color:#6f42c1&#125;.markdown-body .pl-s .pl-s1,.markdown-body .pl-smi&#123;color:#24292e&#125;.markdown-body .pl-ent&#123;color:#22863a&#125;.markdown-body .pl-k&#123;color:#d73a49&#125;.markdown-body .pl-pds,.markdown-body .pl-s,.markdown-body .pl-s .pl-pse .pl-s1,.markdown-body .pl-sr,.markdown-body .pl-sr .pl-cce,.markdown-body .pl-sr .pl-sra,.markdown-body .pl-sr .pl-sre&#123;color:#032f62&#125;.markdown-body .pl-smw,.markdown-body .pl-v&#123;color:#e36209&#125;.markdown-body .pl-bu&#123;color:#b31d28&#125;.markdown-body .pl-ii&#123;color:#fafbfc;background-color:#b31d28&#125;.markdown-body .pl-c2&#123;color:#fafbfc;background-color:#d73a49&#125;.markdown-body .pl-c2:before&#123;content:"^M"&#125;.markdown-body .pl-sr .pl-cce&#123;font-weight:700;color:#22863a&#125;.markdown-body .pl-ml&#123;color:#735c0f&#125;.markdown-body .pl-mh,.markdown-body .pl-mh .pl-en,.markdown-body .pl-ms&#123;font-weight:700;color:#005cc5&#125;.markdown-body .pl-mi&#123;font-style:italic;color:#24292e&#125;.markdown-body .pl-mb&#123;font-weight:700;color:#24292e&#125;.markdown-body .pl-md&#123;color:#b31d28;background-color:#ffeef0&#125;.markdown-body .pl-mi1&#123;color:#22863a;background-color:#f0fff4&#125;.markdown-body .pl-mc&#123;color:#e36209;background-color:#ffebda&#125;.markdown-body .pl-mi2&#123;color:#f6f8fa;background-color:#005cc5&#125;.markdown-body .pl-mdr&#123;font-weight:700;color:#6f42c1&#125;.markdown-body .pl-ba&#123;color:#586069&#125;.markdown-body .pl-sg&#123;color:#959da5&#125;.markdown-body .pl-corl&#123;text-decoration:underline;color:#032f62&#125;.markdown-body .mb-0&#123;margin-bottom:0!important&#125;.markdown-body .my-2&#123;margin-bottom:8px!important;margin-top:8px!important&#125;.markdown-body .pl-0&#123;padding-left:0!important&#125;.markdown-body .py-0&#123;padding-top:0!important;padding-bottom:0!important&#125;.markdown-body .pl-1&#123;padding-left:4px!important&#125;.markdown-body .pl-2&#123;padding-left:8px!important&#125;.markdown-body .py-2&#123;padding-top:8px!important;padding-bottom:8px!important&#125;.markdown-body .pl-3&#123;padding-left:16px!important&#125;.markdown-body .pl-4&#123;padding-left:24px!important&#125;.markdown-body .pl-5&#123;padding-left:32px!important&#125;.markdown-body .pl-6&#123;padding-left:40px!important&#125;.markdown-body .pl-7&#123;padding-left:48px!important&#125;.markdown-body .pl-8&#123;padding-left:64px!important&#125;.markdown-body .pl-9&#123;padding-left:80px!important&#125;.markdown-body .pl-10&#123;padding-left:96px!important&#125;.markdown-body .pl-11&#123;padding-left:112px!important&#125;.markdown-body .pl-12&#123;padding-left:128px!important&#125;.markdown-body hr&#123;border-bottom-color:#eee&#125;.markdown-body kbd&#123;display:inline-block;padding:3px 5px;font:11px SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;line-height:10px;color:#444d56;vertical-align:middle;background-color:#fafbfc;border:1px solid #d1d5da;border-radius:3px;box-shadow:inset 0 -1px 0 #d1d5da&#125;.markdown-body:after,.markdown-body:before&#123;display:table;content:""&#125;.markdown-body:after&#123;clear:both&#125;.markdown-body>:first-child&#123;margin-top:0!important&#125;.markdown-body>:last-child&#123;margin-bottom:0!important&#125;.markdown-body a:not([href])&#123;color:inherit;text-decoration:none&#125;.markdown-body blockquote,.markdown-body details,.markdown-body dl,.markdown-body ol,.markdown-body p,.markdown-body pre,.markdown-body table,.markdown-body ul&#123;margin-top:0;margin-bottom:16px&#125;.markdown-body hr&#123;height:.25em;padding:0;margin:24px 0;background-color:#e1e4e8;border:0&#125;.markdown-body blockquote&#123;padding:0 1em;color:#6a737d;border-left:.25em solid #dfe2e5&#125;.markdown-body blockquote>:first-child&#123;margin-top:0&#125;.markdown-body blockquote>:last-child&#123;margin-bottom:0&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:24px;margin-bottom:16px;font-weight:600;line-height:1.25&#125;.markdown-body h1&#123;font-size:2em&#125;.markdown-body h1,.markdown-body h2&#123;padding-bottom:.3em;border-bottom:1px solid #eaecef&#125;.markdown-body h2&#123;font-size:1.5em&#125;.markdown-body h3&#123;font-size:1.25em&#125;.markdown-body h4&#123;font-size:1em&#125;.markdown-body h5&#123;font-size:.875em&#125;.markdown-body h6&#123;font-size:.85em;color:#6a737d&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:0;margin-bottom:0&#125;.markdown-body li&#123;word-wrap:break-all&#125;.markdown-body li>p&#123;margin-top:16px&#125;.markdown-body li+li&#123;margin-top:.25em&#125;.markdown-body dl&#123;padding:0&#125;.markdown-body dl dt&#123;padding:0;margin-top:16px;font-size:1em;font-style:italic;font-weight:600&#125;.markdown-body dl dd&#123;padding:0 16px;margin-bottom:16px&#125;.markdown-body table&#123;display:block;width:100%;overflow:auto&#125;.markdown-body table th&#123;font-weight:600&#125;.markdown-body table td,.markdown-body table th&#123;padding:6px 13px;border:1px solid #dfe2e5&#125;.markdown-body table tr&#123;background-color:#fff;border-top:1px solid #c6cbd1&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;.markdown-body img&#123;max-width:100%;box-sizing:initial;background-color:#fff&#125;.markdown-body img[align=right]&#123;padding-left:20px&#125;.markdown-body img[align=left]&#123;padding-right:20px&#125;.markdown-body code&#123;padding:.2em .4em;margin:0;font-size:85%;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body pre&#123;word-wrap:normal&#125;.markdown-body pre>code&#123;padding:0;margin:0;font-size:100%;word-break:normal;white-space:pre;background:transparent;border:0&#125;.markdown-body .highlight&#123;margin-bottom:16px&#125;.markdown-body .highlight pre&#123;margin-bottom:0;word-break:normal&#125;.markdown-body .highlight pre,.markdown-body pre&#123;padding:16px;overflow:auto;font-size:85%;line-height:1.45;background-color:#f6f8fa;border-radius:3px&#125;.markdown-body pre code&#123;display:inline;max-width:auto;padding:0;margin:0;overflow:visible;line-height:inherit;word-wrap:normal;background-color:initial;border:0&#125;.markdown-body .commit-tease-sha&#123;display:inline-block;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:90%;color:#444d56&#125;.markdown-body .full-commit .btn-outline:not(:disabled):hover&#123;color:#005cc5;border-color:#005cc5&#125;.markdown-body .blob-wrapper&#123;overflow-x:auto;overflow-y:hidden&#125;.markdown-body .blob-wrapper-embedded&#123;max-height:240px;overflow-y:auto&#125;.markdown-body .blob-num&#123;width:1%;min-width:50px;padding-right:10px;padding-left:10px;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;line-height:20px;color:rgba(27,31,35,.3);text-align:right;white-space:nowrap;vertical-align:top;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none&#125;.markdown-body .blob-num:hover&#123;color:rgba(27,31,35,.6)&#125;.markdown-body .blob-num:before&#123;content:attr(data-line-number)&#125;.markdown-body .blob-code&#123;position:relative;padding-right:10px;padding-left:10px;line-height:20px;vertical-align:top&#125;.markdown-body .blob-code-inner&#123;overflow:visible;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;color:#24292e;word-wrap:normal;white-space:pre&#125;.markdown-body .pl-token.active,.markdown-body .pl-token:hover&#123;cursor:pointer;background:#ffea7f&#125;.markdown-body .tab-size[data-tab-size="1"]&#123;-moz-tab-size:1;tab-size:1&#125;.markdown-body .tab-size[data-tab-size="2"]&#123;-moz-tab-size:2;tab-size:2&#125;.markdown-body .tab-size[data-tab-size="3"]&#123;-moz-tab-size:3;tab-size:3&#125;.markdown-body .tab-size[data-tab-size="4"]&#123;-moz-tab-size:4;tab-size:4&#125;.markdown-body .tab-size[data-tab-size="5"]&#123;-moz-tab-size:5;tab-size:5&#125;.markdown-body .tab-size[data-tab-size="6"]&#123;-moz-tab-size:6;tab-size:6&#125;.markdown-body .tab-size[data-tab-size="7"]&#123;-moz-tab-size:7;tab-size:7&#125;.markdown-body .tab-size[data-tab-size="8"]&#123;-moz-tab-size:8;tab-size:8&#125;.markdown-body .tab-size[data-tab-size="9"]&#123;-moz-tab-size:9;tab-size:9&#125;.markdown-body .tab-size[data-tab-size="10"]&#123;-moz-tab-size:10;tab-size:10&#125;.markdown-body .tab-size[data-tab-size="11"]&#123;-moz-tab-size:11;tab-size:11&#125;.markdown-body .tab-size[data-tab-size="12"]&#123;-moz-tab-size:12;tab-size:12&#125;.markdown-body .task-list-item&#123;list-style-type:none&#125;.markdown-body .task-list-item+.task-list-item&#123;margin-top:3px&#125;.markdown-body .task-list-item input&#123;margin:0 .2em .25em -1.6em;vertical-align:middle&#125;</style><blockquote>
<p>文章内容输出来源：拉勾大前端高薪训练营</p>
</blockquote>
<h1 data-id="heading-0">模块打包工具</h1>
<ul>
<li>
<p>由来</p>
<ul>
<li>
<p>ES Modules存在环境兼容问题</p>
</li>
<li>
<p>模块文件过多，网络请求频繁</p>
</li>
<li>
<p>所有的前端资源都需要模块化</p>
</li>
<li>
<p>美好设想</p>
<ul>
<li>
<p>编译</p>
<ul>
<li>开发阶段尽情使用新特性</li>
<li>生产阶段最大程度兼容所有浏览器</li>
</ul>
</li>
<li>
<p>打包</p>
<ul>
<li>将散落的文件打包为一个文件</li>
<li>解决模块过多频繁发出资源请求的问题</li>
<li>支持不同种类的前端资源类型</li>
</ul>
</li>
</ul>
</li>
<li>
<p>总结</p>
<ul>
<li>
<p>新特性代码编译</p>
<ul>
<li>通过构建系统和一些编译工具来实现</li>
</ul>
</li>
<li>
<p>模块化JS打包</p>
<ul>
<li>通过构建系统和一些编译工具来实现</li>
</ul>
</li>
<li>
<p>支持不同类型的资源模块</p>
<ul>
<li>需要前端模块打包工具</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li>
<p>概要</p>
<ul>
<li>
<p>Webpack</p>
<ul>
<li>
<p>核心特性满足了以上所述需求</p>
</li>
<li>
<p>一款模块打包器(Module bundler)</p>
</li>
<li>
<p>对于有环境兼容性的特性，可以使用 模块加载器(Loader) 对其进行编译转换</p>
</li>
<li>
<p>代码拆分(Code Splitting)</p>
<ul>
<li>
<p>能够将应用中所有的代码都按照我们的需要去打包</p>
<ul>
<li>不用担心把所有的文件打包到一起产生笨重大文件的问题。</li>
</ul>
</li>
<li>
<p>我们可以把应用加载过程当中初次运行的时候所必须的那些模块打包到一起。对于其他的模块可以单独存放，等实际需要时再异步加载该模块。这种加载称为增量加载或渐进式加载。</p>
</li>
</ul>
</li>
<li>
<p>对于前端模块类型的问题，Webpack支持我们在JS中以模块化的方式去载入任意类型的资源文件，即资源模块(Asset Module)</p>
</li>
</ul>
</li>
<li>
<p>Rollup</p>
</li>
<li>
<p>Parcel</p>
</li>
</ul>
</li>
<li>
<p>作用</p>
<ul>
<li>打包工具解决的是前端整体的模块化，并不单指JS模块化</li>
<li>可以让我们在开发阶段更好的享受模块化所带来的优势，同时呢不必担心模块化给生产环境所产生的一些影响。</li>
</ul>
</li>
</ul>
<h1 data-id="heading-1">Webpack</h1>
<h2 data-id="heading-2">- 快速上手</h2>
<pre><code class="copyable">- Webpack作为目前最主流的前端模块打包器，提供了一整套的前端项目模块化方案，而非仅仅局限于只对JS的模块化。通过Webpack提供的前端模块化方案，我们可以轻松的对我们前端项目中涉及到的所有资源进行模块化。
- Webpack想法先进，早期使用过程比较繁琐，官方文档也比较晦涩难懂，所以最开始的时候，显得对我们开发者不是十分友好。但是随着版本迭代，官方文档也在不断更新，目前Webpack已经非常受欢迎了，基本上可以说是覆盖了绝大多数现代web项目应用开发过程。
- 案例

- src

- heading.js

- export default () ⥤ &#123;
const element = document.createElement('h2')

element.textContent='hello world'
element.addEventListener('click', () ⥤ &#123;
   alert('Hello webpack')
&#125;)

return element
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<pre><code class="copyable">- index.js

- import createHeading from './heading.js'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const heading= createHeading()</p>
<p>document.body.append(heading)</p>
<pre><code class="copyable">- index.html

- <!DOCTYPE html>
<span class="copy-code-btn">复制代码</span></code></pre>


    
    
    
    Webpack - 快速上手


    


<pre><code class="copyable">- 安装serve

- yarn global add serve

- 运行

- serve  .

- 引入Webpack处理JS模块

- 由于Webpack是npm的一个工具模块，所以先初始化一个package.json文件

- yarn init --yes

- 安装Webpack及其cli插件

- yarn add webpack webpack-cli --dev
- yarn webpack --version

- Ok~

- 执行打包操作

- yarn webpack

- OK~

- 将webpack命令包装在package.json中的scripts属性中

- "scripts": &#123;
"build": "webpack"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;
- 运行: yarn build</p>
<pre><code class="copyable">- OK~
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">- 配置文件</h2>
<pre><code class="copyable">- Webpack4以后的版本支持零配置直接启动打包

- 整个打包过程会将src/index.js作为打包入口，并在dist目录下生成main.js文件

- 添加配置文件webpack.config.js

- 此文件是运行在Node环境中的js文件，所以需要以CommonJS方式来编写代码
- 内容

- const path = require ('path')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>module.exports = &#123;
// 指定webpack打包的入口路径，指定相对路径时，'./'不能省略
entry: './src/main.js',
// 设置输出文件的位置
output: &#123;
// 设置输出文件名称
filename: 'bundle.js',
// 指定输出文件所在目录，不可使用相对路径
path: path.join(__dirname,'output')
&#125;
&#125;
- 打包: yarn build</p>
<pre><code class="copyable">- OK~
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">- 工作模式</h2>
<pre><code class="copyable">- webpack4新增了一个工作模式的用法

- 此用法大大简化了webpack配置的复杂程度

- 可以理解为针对不同环境预设的几组配置

- yarn build

- 警告: 大概意思是未指定mode属性，将以生产环境方式进行打包

- 打包代码进行过优化，很难阅读

- yarn webpack --mode development

- 无警告

- 打包代码可读性强

- mode

- development

- 此工作模式下webpack会优化打包速度
- 增加调试过程中需要的辅助到我们打包代码中

- production

- 此工作模式会优化代码

- none

- webpack运行最原始状态的打包，不会去做任何额外的处理

- 除了在运行参数中设置工作模式也可以在配置文件webpack.config.js中指定

- const path = require ('path')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>module.exports = &#123;
mode: 'development',
// 指定webpack打包的入口路径，指定相对路径时，'./'不能省略
entry: './src/main.js',
// 设置输出文件的位置
output: &#123;
// 设置输出文件名称
filename: 'bundle.js',
// 指定输出文件所在目录，不可使用相对路径
path: path.join(__dirname,'output')
&#125;
&#125;
- 运行: yarn build</p>
<h2 data-id="heading-5">- 打包结果运行原理</h2>
<pre><code class="copyable">- 为了可以更好的理解打包过后的代码

- 将mode设置为none

- const path = require ('path')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>module.exports = &#123;
mode: 'none',
// 指定webpack打包的入口路径，指定相对路径时，'./'不能省略
entry: './src/main.js',
// 设置输出文件的位置
output: &#123;
// 设置输出文件名称
filename: 'bundle.js',
// 指定输出文件所在目录，不可使用相对路径
path: path.join(__dirname,'output')
&#125;
&#125;</p>
<pre><code class="copyable">- 打包: yarn webpack

- dist目录下成功生成了bundle.js文件
- 分析bundle.js文件

- Ctrl+K,Ctrl+0

- 折叠所有代码

- 整体生成代码是一个立即执行函数即IIFE

- 该函数是webpack工作入口

- 形参参数为modules
- 实参为一个数组，数组中每一个元素都是参数列表相同的函数

- 每个函数对应的就是我们源代码中的模块
- 也就是说我们每个模块都会被包裹到这样一个函数当中，从而去实现模块的私有作用域

- 展开webpack工作入口函数，分析函数体内部

- 1，定义1个对象，用于缓存已经加载的模块对象
- 2，定义了一个require函数，用于加载模块
- 3，在require函数上挂载了一些属性或工具函数

- m属性

- 用于缓存参数modules

- c属性

- 用于缓存已经加载过的模块s

- d函数

- 用于给指定对象定义getter函数

- r函数

- 给指定对象定义__esModule标志

- t函数

- 创建一个伪命名空间对象

- n函数

- 用于处理兼容性

- o函数

- 用于判断指定对象是否拥有给定属性

- p属性

- 公共路径前缀

- 函数最后调用了自定义的require函数，传入了一个0开始加载我们的模块

- 总结

- webpack打包过后的代码并不会特别的复杂。
- 只是帮我们把所有的模块放到同一个文件当中
- 除了放到同一个文件当中，webpack还提供了一些基础代码，让我们的这些模块与模块之间相互依赖关系还可以保持原有的那个状态。
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            