
---
title: '写了个 babel-plugin，我收获了不止一点'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d2a70c5d83b433289759a4d5ff2a8a2~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 11 May 2021 23:19:29 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d2a70c5d83b433289759a4d5ff2a8a2~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d2a70c5d83b433289759a4d5ff2a8a2~tplv-k3u1fbpfcp-zoom-1.image" alt="图片 babel" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">一、问题引出</h2>
<p>我们知道 <code>react</code> 中一切皆组件，公共组件一般都会在 src 目录下新建 components 目录来存放。那么问题来了：如果组件拆分得细而多，那么文件数量自然而然就多了起来，我们在使用时可能会看见如下场景：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/044b3481c99a46dea4357b131ed2a6b4~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一大堆的文件是不是看着头就大！试想我们可不可以像 <code>antd</code> 组件一样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;
    ReimburseDetail,
    ContactUs,
    HoverTips,
    CustomModal,
    ReimburseStatus
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'src-components'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这么使用呢？哎，还真有办法！</p>
<h2 data-id="heading-1">二、解决问题</h2>
<h3 data-id="heading-2">方案一</h3>
<ol>
<li>在 <code>components</code> 目录下新建一个 <code>index.js</code> ，引入目录下所有文件，然后导出。
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
* './module' 要读取的目录
* true 是否读取子目录
* /\.js$/ 匹配后缀为'.js'的文件
*/</span>
<span class="hljs-keyword">const</span> files = <span class="hljs-built_in">require</span>.context(<span class="hljs-string">'./module'</span>, <span class="hljs-literal">true</span>, <span class="hljs-regexp">/\.js$/</span>)
<span class="hljs-keyword">const</span> modules = files.keys().reduce(<span class="hljs-function">(<span class="hljs-params">modules, path</span>) =></span> &#123;
    <span class="hljs-comment">// './app.js' => 'app'</span>
    <span class="hljs-keyword">const</span> name = path.replace(<span class="hljs-regexp">/^\.\/|.js$/g</span>, <span class="hljs-string">''</span>)
    modules[name] = files(path).default
    <span class="hljs-keyword">return</span> modules
&#125;, &#123;&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> modules
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>试试效果：可以满足要求，但打包体积会变大，未使用的组件也参与了打包。</li>
</ol>
<h3 data-id="heading-3">方案二</h3>
<ol>
<li>
<p>我们试试手动实现一个 <code>babel-plugin</code> 。</p>
</li>
<li>
<p>思路：我们知道引入单一文件时不存在所谓的按需加载，当一个文件暴露的出口文件多时，那么这个文件就不是单一文件了，一旦文件被引用，该文件暴露的文件就全部会引入并参与打包，这显然不是我们需要的。那么我们是不是可以做点什么呢？假如我引入一个不存在的包，然后导出想要的组件：</p>
<ul>
<li>显然不可能会导入所有的包</li>
<li>显然不可能会生效，编译会报错</li>
</ul>
<p>基于这个思路，我们可以手动修改它默认的编译规则，以达到我们想要的目的。我们需要拦截所有使用了我们自定义的包名文件，对传入的组件名提取出来，修改编译规则，让其单独引入传入的包名的组件参与单独引入打包，就可以达到我们想要的目的。</p>
</li>
<li>
<p>来吧，上手干。参照 <a href="https://segmentfault.com/a/1190000016459270" target="_blank" rel="nofollow noopener noreferrer">链接这篇文章</a> 查看 <code>babel-plugin</code> <code>api</code> 就开搞：</p>
<pre><code class="hljs language-json copyable" lang="json">    <span class="hljs-comment">// .babelrc</span>
    &#123;
        <span class="hljs-attr">"plugins"</span>: [
            [
                <span class="hljs-string">"./src/utils/my-plugin-import"</span>, &#123;
                    <span class="hljs-attr">"libraryName"</span>: <span class="hljs-string">"src-components"</span>,
                    <span class="hljs-attr">"alias"</span>: <span class="hljs-string">"@/components"</span>
                &#125;
            ],
            ...
        ]
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> toLine = <span class="hljs-function"><span class="hljs-params">name</span> =></span> &#123;
    <span class="hljs-keyword">const</span> str = name.replace(<span class="hljs-regexp">/([A-Z])/g</span>, <span class="hljs-string">"-$1"</span>).toLowerCase()
    <span class="hljs-keyword">return</span> str.split(<span class="hljs-string">'-'</span>)[<span class="hljs-number">0</span>] ? str : str.slice(<span class="hljs-number">1</span>)
&#125;

<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">&#123; types: t &#125;</span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">visitor</span>: &#123;
            <span class="hljs-function"><span class="hljs-title">ImportDeclaration</span>(<span class="hljs-params">path, source</span>)</span> &#123;
                <span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">opts</span>: &#123; libraryName, alias &#125; &#125; = source
                <span class="hljs-keyword">if</span> (!t.isStringLiteral(path.node.source, &#123; <span class="hljs-attr">value</span>: libraryName &#125;)) &#123;
                    <span class="hljs-keyword">return</span>
                &#125;
                <span class="hljs-keyword">const</span> newImports = path.node.specifiers.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
                    <span class="hljs-keyword">const</span> str = toLine(item.local.name)

                    <span class="hljs-keyword">return</span> t.importDeclaration(
                        [t.importDefaultSpecifier(item.local)],
                        t.stringLiteral(<span class="hljs-string">`<span class="hljs-subst">$&#123;alias&#125;</span>/<span class="hljs-subst">$&#123;str&#125;</span>`</span>)
                    )
                &#125;)

                path.replaceWithMultiple(newImports)
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>.babelrc</code> 使用上我们的插件，<code>babel-loader</code> 会在编译的时候执行我们的自定义 <code>js</code></li>
<li>配置我们的自定义包名 <code>src-components</code>（引用的时候使用）</li>
<li>配置我们需要加载的组件的路径 <code>alias</code></li>
<li>映射规则转换：大写驼峰 - 中划线命名方式</li>
<li>最终路径就是：<code>alias + name</code></li>
<li>恭喜你，到这里就完成了</li>
</ul>
</li>
</ol>
<h2 data-id="heading-4">三、上手体验</h2>
<p>修改组件引入方式，保存 ，编译正常，无任何毛病；爽歪歪，再 <code>build</code> 构建试试，无完全没问题。</p>
<h2 data-id="heading-5">四、回顾与思考</h2>
<p>这种方式确实给我们带来了极大便利，优化了大量代码，简洁易读。这样看来，我们的代码是不是都可以和 <code>antd</code> 写法相媲美了，美滋滋。</p>
<p>等等 <code>antd</code> 是怎么实现按需引入的呢？噢噢，原来使用了 <code>babel-plugin-import</code>，让我们看看 <code>.babelrc</code> ：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// .babelrc</span>
[
    <span class="hljs-string">"import"</span>,
    &#123;
        <span class="hljs-attr">"libraryName"</span>: <span class="hljs-string">"antd"</span>,
        <span class="hljs-attr">"libraryDirectory"</span>: <span class="hljs-string">"es"</span>,
        <span class="hljs-attr">"style"</span>: <span class="hljs-literal">true</span>
    &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>哇咔咔，这是不是惊奇的相似？只不过别人还做了额外的功能就是导包的时候，再引入对应的css罢了。</p>
<p>至此，就到文末了。我们从发现问题到解决问题，从写插件再到发觉按需引入原理，收获还真不止一点点哦！</p></div>  
</div>
            