
---
title: 'vue3+ts 开发组件库'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02c884396a584f5dad2af0109b74795e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 18:54:44 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02c884396a584f5dad2af0109b74795e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">架构参考element-ui</h1>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02c884396a584f5dad2af0109b74795e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">tsconfig.json</h1>
<ul>
<li>Typescript项目配置文件</li>
<li>命令行执行tsc后，会根据该配置文件将项目中的ts编译为js</li>
</ul>





























<table><thead><tr><th>选项</th><th>类型</th><th>默认值</th><th>描述</th></tr></thead><tbody><tr><td><code>--declaration</code> <code>-d</code></td><td><code>boolean</code></td><td><code>false</code></td><td>生成相应的 <code>.d.ts</code>文件。</td></tr><tr><td><code>--declarationDir</code></td><td><code>string</code></td><td></td><td>生成声明文件的输出路径。</td></tr><tr><td><code>--sourceMap</code></td><td><code>boolean</code></td><td><code>false</code></td><td>生成相应的 <code>.map</code>文件。</td></tr></tbody></table>
<h1 data-id="heading-2">vue.shim.d.ts</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
* vue.shim.d.ts的作用 
* 为了typescript做的适配定义文件，因为.vue文件不是一个常规的文件类型，*  ts是不能理解* vue文件是干嘛的，
* 加这一段是告诉ts，vue文件是这种类型。
* 可以把这一段删除，会发现import的所有vue类型的文件都会报错。
**/</span>
declare <span class="hljs-built_in">module</span> <span class="hljs-string">'*.vue'</span> &#123;
    <span class="hljs-keyword">import</span> &#123; App, defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
    <span class="hljs-keyword">const</span> component: ReturnType<<span class="hljs-keyword">typeof</span> defineComponent> & &#123;
        install(app: App) : <span class="hljs-keyword">void</span>
    &#125;
    <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> component
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">package.json配置vue</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"peerDependencies"</span>: &#123;
    <span class="hljs-string">"vue"</span>: <span class="hljs-string">"^3.0.9"</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>peerDependencies</code>的目的是提示宿主环境去安装满足插件peerDependencies所指定依赖的包，然后在插件import或者require所依赖的包的时候，永远都是引用宿主环境统一安装的npm包，最终解决插件与所依赖包不一致的问题。</li>
<li>白话：假如组件库工程安装了vue，业务项目工程中也安装了vue；代码运行时，组件库和业务项目各自调用的vue不是同一个，导致参数传递失败。</li>
</ul>
<h1 data-id="heading-4">webpack配置文件配置babel-loader，处理ts、es6</h1>
<pre><code class="hljs language-js copyable" lang="js">            &#123;
                    <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(ts|js)x?$/</span>,
                    exclude: <span class="hljs-regexp">/node_modules/</span>,
                    loader: <span class="hljs-string">'babel-loader'</span>,
                    <span class="hljs-attr">options</span>: &#123;
                        <span class="hljs-attr">presets</span>: [
                            <span class="hljs-string">'@babel/preset-env'</span>,[
                                <span class="hljs-string">'@babel/preset-typescript'</span>,
                                &#123;
                                    <span class="hljs-attr">allExtensions</span>: <span class="hljs-literal">true</span>
                                &#125;
                            ]
                        ]
                    &#125;
                &#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            