
---
title: '用Babel提效——从入门到业务实战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://img-1258692894.cos.ap-guangzhou.myqcloud.com/s4iqhn2pqz.png?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDylHWUBbleFZgX7PQBfsoUt0qQjlWzC9o%26q-sign-time%3D1663424259%3B1666016319%26q-key-time%3D1663424259%3B1666016319%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D0aaf72e9f9ff15a2b1212a473de96929379672a7&'
author: 掘金
comments: false
date: Sat, 17 Sep 2022 08:09:36 GMT
thumbnail: 'https://img-1258692894.cos.ap-guangzhou.myqcloud.com/s4iqhn2pqz.png?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDylHWUBbleFZgX7PQBfsoUt0qQjlWzC9o%26q-sign-time%3D1663424259%3B1666016319%26q-key-time%3D1663424259%3B1666016319%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D0aaf72e9f9ff15a2b1212a473de96929379672a7&'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>相信现在大多数的前端同学都有听过和用过 <code>Babel</code> ，它的官网如是介绍自己： <code>Babel 是一个 JavaScript 编译器</code> 。在开发中，我们最常用它来做 <code>ES6+</code> 语法向 <code>ES5</code> 的转换，也会用它配合打包工具来做压缩、混淆等工作。它的工作过程可能简单用三个步骤来概括：</p>
<ul>
<li>解析：将代码转换为抽象语法树（ <code>ast</code> ）</li>
<li>转换： <code>Babel</code> 或者相关插件对 <code>ast</code> 进行操作转换</li>
<li>生成：用新的抽象语法树重新生成代码</li>
</ul>
<p>由上面这三步可以看出，它是使用抽象语法树来贯穿全程的。而基于抽象语法树，我们很容易去做一些静态分析，本文举了三个我在实际工作中遇到的例子，并使用 <code>Babel</code> 去解决这三个实际问题。开始之前，还是有必要介绍一下 <code>Babel</code> 的相关概念以及 <code>API</code> 。</p>
<h1 data-id="heading-1">相关概念</h1>
<p>先来介绍一下会用到的几个包：</p>
<ul>
<li><code>@babel/cli</code> ： <code>Babel</code> 的命令行客户端，可通过命令行编译文件。</li>
<li><code>@babel/parser</code> ：将代码解析成 <code>ast</code></li>
<li><code>@babel/traverse</code> ：遍历 <code>ast</code></li>
<li><code>@babel/template</code> ：在转换 <code>ast</code> 的过程中，需要替换节点，这个库可以用静态声明的方式去替换，下文会提到</li>
<li><code>@babel/generator</code> ：将 <code>ast</code> 生成为代码</li>
<li><code>@babel/types</code> ：工具包，用来生成节点或者检查节点的类型</li>
</ul>
<p>介绍完会用到的包后，下面来介绍一些 <code>Babel</code> 插件的概念。插件返回的是一个函数，在这个函数里， <code>Babel</code> 帮我们去遍历 <code>ast</code> ，我们采用一个访问者模式去定义各个节点类型的处理函数。如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">visitor</span>: &#123;
      <span class="hljs-title class_">Identifier</span>: &#123;
        <span class="hljs-attr">enter</span>:(path) &#123;

        &#125;,
        <span class="hljs-attr">exit</span>:(path) &#123;

        &#125;
      &#125;,
    &#125;,
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Identifier</code> 是一种节点的类型，它可以是一个对象，具有 <code>enter</code> 属性和 <code>exit</code> 属性。 <code>ast</code> 是一个树状结构， <code>enter</code> 就是从根节点往子节点遍历方向时触发的回调函数， <code>exit</code> 就是子节点往根节点方向回溯时触发的回调函数。在开发好插件之后，可以项目根目录下的 <code>.babelrc</code> 文件处引用插件。</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"plugins"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-string">"./src/plugins/autoBindThis"</span><span class="hljs-punctuation">]</span>   
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上就是本文会用到的一些包以及一些概念的简要介绍，更多详细的文档内容可以移步下面这两个链接：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.babeljs.cn%2Fdocs%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.babeljs.cn/docs/" ref="nofollow noopener noreferrer">babel中文网</a>： <code>Babel</code> 的各种相关概念以及教程</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjamiebuilds%2Fbabel-handbook%2Fblob%2Fmaster%2Ftranslations%2Fzh-Hans%2Fplugin-handbook.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jamiebuilds/babel-handbook/blob/master/translations/zh-Hans/plugin-handbook.md" ref="nofollow noopener noreferrer">babel-plugin-handbook</a>：插件开发的相关教程与思路</p>
<p>那么话不多说，下面让我们进入实战环节。</p>
<h1 data-id="heading-2">autoBindThis</h1>
<p>做过 <code>React</code> 开发的同学应该知道，我们有时候会写出来这样的代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">class</span> <span class="hljs-title class_">Comp</span> &#123;
    <span class="hljs-title function_">constructor</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">func</span> = <span class="hljs-variable language_">this</span>.<span class="hljs-property">func</span>.<span class="hljs-title function_">bind</span>(<span class="hljs-variable language_">this</span>)
    &#125;
    <span class="hljs-title function_">func</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">setState</span>(&#123;
            <span class="hljs-comment">//xxx</span>
        &#125;)
    &#125;
    <span class="hljs-title function_">render</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">func</span>=<span class="hljs-string">&#123;this.func&#125;/</span>></span></span>
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为 <code>func</code> 函数是在子组件被调用的，如果 <code>func</code> 函数里面有 <code>this</code> 相关的操作，那么 <code>this</code> 最终的指向会不准，之前常见的写法是在构造函数里用 <code>bind</code> 显性绑定一次。那么在了解完 <code>Babel</code> 之后，就可以用 <code>Babel</code> 去解决这个问题。</p>
<p>思路也很清晰，找到所有的函数定义，剔除掉一些肯定不需要绑定的函数——比如 <code>constructor</code> 、组件的生命周期钩子等；然后在 <code>constructor</code> 函数里对每个函数进行 <code>this</code> 绑定。但是有一点需要注意的是，如果原来的代码里不存在 <code>constructor</code> 函数，那么这个插件得先把 <code>constructor</code> 函数给补上。在开发 <code>Babel</code> 相关的东西的时候，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fastexplorer.net%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://astexplorer.net/" ref="nofollow noopener noreferrer">astexplorer</a> 这个网站是必不可少的。</p>
<p><img src="https://img-1258692894.cos.ap-guangzhou.myqcloud.com/s4iqhn2pqz.png?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDylHWUBbleFZgX7PQBfsoUt0qQjlWzC9o%26q-sign-time%3D1663424259%3B1666016319%26q-key-time%3D1663424259%3B1666016319%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D0aaf72e9f9ff15a2b1212a473de96929379672a7&" alt="s4iqhn2pqz.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在这里我们可以看到代码解析成抽象语法树的数据结构，也可以很方便的看到各个对应的节点以及它们的属性。那么先来实现第一点需求：判断一下原先的代码存不存在 <code>constructor</code> 函数，如果不存在，需要给它补上。</p>
<p><img src="https://img-1258692894.cos.ap-guangzhou.myqcloud.com/e79e928dvc.png?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDylHWUBbleFZgX7PQBfsoUt0qQjlWzC9o%26q-sign-time%3D1663424429%3B1666016489%26q-key-time%3D1663424429%3B1666016489%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D6d10c644d59df73d2cdb5022cf48f71e1ec2e9fe&" alt="e79e928dvc.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里可以看到针对于 <code>classBody</code> 这个节点，它的 <code>body</code> 属性对应的就是这个类的所有方法，所以我们只要遍历这个数组，判断一下存不存在 <code>constructor</code> 函数，如果存在则忽略，如果不存在就给它补上。怎么补呢？刚开始接触的话可能有点无从下手，推荐在上面那个网站上写一个 <code>constructor</code> 函数，看看它的数据结构是怎样的。</p>
<p><img src="https://img-1258692894.cos.ap-guangzhou.myqcloud.com/qcx2h0hybd.png?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDylHWUBbleFZgX7PQBfsoUt0qQjlWzC9o%26q-sign-time%3D1663425185%3B1666017245%26q-key-time%3D1663425185%3B1666017245%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D5dd32241cb7e2d0cd9d8a580fa359412c73d956a&" alt="qcx2h0hybd.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由上图可以看到，它是一个 <code>classMethod</code> 类型，然后有 <code>kind</code> 、 <code>key</code> 等等属性，再配合我们的编辑器的提示：</p>
<p><img src="https://img-1258692894.cos.ap-guangzhou.myqcloud.com/zaq4n1wypm.png?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDylHWUBbleFZgX7PQBfsoUt0qQjlWzC9o%26q-sign-time%3D1663425267%3B1666017327%26q-key-time%3D1663425267%3B1666017327%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D7a3dc623773462a121c7856603493645dd1e91c6&" alt="zaq4n1wypm.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>就知道它的参数应该怎么传，这两个东西相互配合，然后去构造我们需要的 <code>ast node</code> 。具体的代码实现如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> =  <span class="hljs-keyword">function</span> (<span class="hljs-params">&#123; types: t &#125;</span>) &#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">visitor</span>: &#123;
            <span class="hljs-title class_">ClassBody</span>: &#123;
                <span class="hljs-title function_">enter</span>(<span class="hljs-params">path</span>) &#123;
                    <span class="hljs-keyword">const</span> allMethods = path.<span class="hljs-property">node</span>.<span class="hljs-property">body</span>
                    <span class="hljs-comment">// 判断constructor是否存在</span>
                    <span class="hljs-keyword">const</span> constructorExist = allMethods.<span class="hljs-title function_">find</span>(<span class="hljs-function"><span class="hljs-params">method</span> =></span> method.<span class="hljs-property">kind</span> === <span class="hljs-string">'constructor'</span>)
                    <span class="hljs-keyword">if</span> (!constructorExist) &#123;
                        <span class="hljs-comment">// 构造一个constructor塞入数组中</span>
                        path.<span class="hljs-property">node</span>.<span class="hljs-property">body</span>.<span class="hljs-title function_">unshift</span>(
                            t.<span class="hljs-title function_">classMethod</span>(
                                <span class="hljs-string">'constructor'</span>,
                                t.<span class="hljs-title function_">identifier</span>(<span class="hljs-string">'constructor'</span>),
                                [],
                                t.<span class="hljs-title function_">blockStatement</span>([])
                            )
                        )
                    &#125;
                &#125;
            &#125;
        &#125;
    &#125;;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那接下来剔除掉一些不需要绑定 <code>this</code> 的函数，将剩下的所有函数遍历，往 <code>constructor</code> 函数里面加上绑定的代码，也就是加上类似于 <code>this.fun = this.fun.bind(this)</code> 这样的语句。</p>
<p><img src="https://img-1258692894.cos.ap-guangzhou.myqcloud.com/m2yp3c1f21.png?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDylHWUBbleFZgX7PQBfsoUt0qQjlWzC9o%26q-sign-time%3D1663425625%3B1666017685%26q-key-time%3D1663425625%3B1666017685%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3Da3030fd7e2d8a2aa83404e6047a894ab43212f28&" alt="m2yp3c1f21.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>每一条语句都属于 <code>ExpressionStatement</code> 类型，存放在 <code>body</code> 属性中。所以我们需要把构造出来的 <code>ast node</code> 塞到 <code>body</code> 属性里。</p>
<p><img src="https://img-1258692894.cos.ap-guangzhou.myqcloud.com/40xjvun2jo.png?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDylHWUBbleFZgX7PQBfsoUt0qQjlWzC9o%26q-sign-time%3D1663425717%3B1666017777%26q-key-time%3D1663425717%3B1666017777%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D4919660d7dbd8f5ca1a214138748fe2f1afc6968&" alt="40xjvun2jo.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面这是一条绑定语句的抽象语法树的节点信息，看起来这只是一行代码，但是构造起来还挺麻烦的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> subAst = t.<span class="hljs-title function_">expressionStatement</span>(
    t.<span class="hljs-title function_">assignmentExpression</span>(
        <span class="hljs-string">'='</span>,
        t.<span class="hljs-title function_">memberExpression</span>(
            t.<span class="hljs-title function_">thisExpression</span>(), t.<span class="hljs-title function_">identifier</span>(path.<span class="hljs-property">node</span>.<span class="hljs-property">key</span>.<span class="hljs-property">name</span>)
        ),
        t.<span class="hljs-title function_">callExpression</span>(
            t.<span class="hljs-title function_">memberExpression</span>(
                t.<span class="hljs-title function_">memberExpression</span>(t.<span class="hljs-title function_">thisExpression</span>(), t.<span class="hljs-title function_">identifier</span>(path.<span class="hljs-property">node</span>.<span class="hljs-property">key</span>.<span class="hljs-property">name</span>)),
                t.<span class="hljs-title function_">identifier</span>(<span class="hljs-string">'bind'</span>)
            ),
            [t.<span class="hljs-title function_">thisExpression</span>()]
        )
    )
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候就可以利用上面提过的 <code>babel-template</code> 这个包，它只需要下面几行简单的代码就可以实现上面那一坨的功能：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> template = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@babel/template'</span>);
<span class="hljs-keyword">const</span> templateString = template.<span class="hljs-title function_">default</span>(<span class="hljs-string">`
    this.METHOD = this.METHOD.bind(this)
`</span>)
<span class="hljs-keyword">const</span> subAst = <span class="hljs-title function_">templateString</span>(&#123;
    <span class="hljs-attr">METHOD</span>: t.<span class="hljs-title function_">identifier</span>(path.<span class="hljs-property">node</span>.<span class="hljs-property">key</span>.<span class="hljs-property">name</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终可以一起来看一下这个插件实现的完整代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> disabled = [<span class="hljs-string">'constructor'</span>, <span class="hljs-string">'render'</span><span class="hljs-comment">/*其他生命周期函数...*/</span>]
<span class="hljs-keyword">const</span> template = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@babel/template'</span>);
<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = <span class="hljs-keyword">function</span> (<span class="hljs-params">&#123; types: t &#125;</span>) &#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">visitor</span>: &#123;
            <span class="hljs-title class_">ClassBody</span>: &#123;
                <span class="hljs-title function_">enter</span>(<span class="hljs-params">path</span>) &#123;
                    <span class="hljs-keyword">const</span> allMethods = path.<span class="hljs-property">node</span>.<span class="hljs-property">body</span>
                    <span class="hljs-keyword">const</span> constructorExist = [...allMethods].<span class="hljs-title function_">find</span>(<span class="hljs-function"><span class="hljs-params">method</span> =></span> method.<span class="hljs-property">kind</span> === <span class="hljs-string">'constructor'</span>)
                    <span class="hljs-keyword">if</span> (!constructorExist) &#123;
                        path.<span class="hljs-property">node</span>.<span class="hljs-property">body</span>.<span class="hljs-title function_">unshift</span>(
                            t.<span class="hljs-title function_">classMethod</span>(<span class="hljs-string">'constructor'</span>,
                                t.<span class="hljs-title function_">identifier</span>(<span class="hljs-string">'constructor'</span>),
                                [],
                                t.<span class="hljs-title function_">blockStatement</span>([])
                            )
                        )
                    &#125;
                &#125;,
            &#125;,
            <span class="hljs-title class_">ClassMethod</span>: &#123;
                <span class="hljs-title function_">enter</span>(<span class="hljs-params">path</span>) &#123;
                    <span class="hljs-keyword">if</span> (!disabled.<span class="hljs-title function_">includes</span>(path.<span class="hljs-property">node</span>.<span class="hljs-property">kind</span>) && !disabled.<span class="hljs-title function_">includes</span>(path.<span class="hljs-property">node</span>.<span class="hljs-property">key</span>.<span class="hljs-property">name</span>)) &#123;
                        <span class="hljs-keyword">const</span> constructor = path.<span class="hljs-property">container</span>.<span class="hljs-title function_">find</span>(<span class="hljs-function"><span class="hljs-params">method</span> =></span> method.<span class="hljs-property">kind</span> === <span class="hljs-string">'constructor'</span>);
                        <span class="hljs-keyword">if</span> (constructor) &#123;
                            <span class="hljs-keyword">const</span> templateString = template.<span class="hljs-title function_">default</span>(<span class="hljs-string">`
                              this.METHOD = this.METHOD.bind(this)
                            `</span>)
                            <span class="hljs-keyword">const</span> subAst = <span class="hljs-title function_">templateString</span>(&#123;
                                <span class="hljs-attr">METHOD</span>: t.<span class="hljs-title function_">identifier</span>(path.<span class="hljs-property">node</span>.<span class="hljs-property">key</span>.<span class="hljs-property">name</span>)
                            &#125;)
                            constructor.<span class="hljs-property">body</span>.<span class="hljs-property">body</span>.<span class="hljs-title function_">push</span>(
                                subAst
                            )
                        &#125;
                    &#125;
                &#125;
            &#125;,
        &#125;
    &#125;;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后可以通过 <code>babel-cli</code> 命令行工具去调用 <code>babel</code> 去编译对应的文件——类似于这样 <code>npx babel test.js --out-file ./out/test.js</code> ，别忘了在 <code>.babelrc</code> 文件中配置好这个插件。结果如下：</p>
<p><img src="https://img-1258692894.cos.ap-guangzhou.myqcloud.com/9ksudl9le1.png?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDylHWUBbleFZgX7PQBfsoUt0qQjlWzC9o%26q-sign-time%3D1663426346%3B1666018406%26q-key-time%3D1663426346%3B1666018406%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3Dbd8bfdf28ec00243545d56f5b3d470c0c6a2fc57&" alt="9ksudl9le1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在实践这个的过程中，个人觉得刚开始如何去构造节点是比较没有头绪的，希望能通过上面的展示，给予大家一些思路。</p>
<h1 data-id="heading-3">生成文档</h1>
<p>接下来我们来看一个生成文档的案例，这也是实际场景当中遇到的需求。无论是在开发前端组件、或者后端在写 <code>API</code> ，如果开发完成之后没有对应的文档的话，别人很难一下子看出来要如何使用。但是很多时候大家写完就算了，也没有去即使维护相对应的MD文档。所以这里就想做一个根据一些注释信息去生成文档的工具，让你在写注释的过程中就把文档给写了。那万一别人连这些注释也不想写怎么办？ <code>eslint+husky</code> 可以帮到你，之后我会写一篇关于 <code>eslint</code> 、 <code>stylelint</code> 插件的文章，但时候再在那里展开。其实 <code>husky</code> 这种也不是能把所有人拦住，总有人在自己的环境上没装。所以要彻底解决这个问题，个人的想法应该是禁止直接提交 <code>master</code> 分支（发布分支），只能通过 <code>feature</code> 分支合并到 <code>master</code> ，强制卡 <code>MR</code> 。扯的有点远了，下面来正式看看这个工具的具体实现。</p>
<p>假如我现在有这么一个服务端文件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>)
<span class="hljs-keyword">const</span> app = <span class="hljs-title function_">express</span>()
<span class="hljs-keyword">const</span> port = <span class="hljs-number">3000</span>

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@path</span> /login
 * <span class="hljs-doctag">@param</span> username 用户名 string Required
 * <span class="hljs-doctag">@param</span> password 密码 string Required
 */</span>
app.<span class="hljs-title function_">get</span>(<span class="hljs-string">'/login'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  res.<span class="hljs-title function_">send</span>(<span class="hljs-string">'Hello World!'</span>)
&#125;)

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@path</span> /user
 * <span class="hljs-doctag">@param</span> userId 用户id string Required
 * <span class="hljs-doctag">@param</span> fields 需要查询的字段 array|undefined
 */</span>
app.<span class="hljs-title function_">get</span>(<span class="hljs-string">'/user'</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  res.<span class="hljs-title function_">send</span>(<span class="hljs-string">'user info'</span>)
&#125;)

app.<span class="hljs-title function_">listen</span>(port, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">`Example app listening on port <span class="hljs-subst">$&#123;port&#125;</span>`</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我希望把 <code>login</code> 、 <code>user</code> 这两个接口前面的注释提取出来，生成接口文档，应该怎么办？老规矩，先在 <code>astexplorer</code> 看看它们长什么样。</p>
<p><img src="https://img-1258692894.cos.ap-guangzhou.myqcloud.com/b4d07sg6li.png?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDylHWUBbleFZgX7PQBfsoUt0qQjlWzC9o%26q-sign-time%3D1663426973%3B1666019033%26q-key-time%3D1663426973%3B1666019033%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D9041c1b9e22d6c35f0a50d09a5208fac63632d37&" alt="b4d07sg6li.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意到节点里有 <code>leadingComments</code> 和 <code>trailingComments</code> 这两个属性，分别表示节点前后的注释，我们规定相关的注释是写在节点的前面，所以去处理  <code>leadingComments</code> 就好了。整体的思路如下：</p>
<ul>
<li>读取所有要处理的文件，生成 <code>ast</code></li>
<li>对 <code>ExpressionStatement</code> 类型的节点进行处理，这个根据情况而定。</li>
<li>处理节点的 <code>leadingComments</code> ，根据约定的前缀还有字段顺序拼接字符串，输出到 <code>MD</code> 文件中</li>
</ul>
<p>整体代码我就直接贴出来了，行数也不多，感觉代码里都是一些“业务”的处理，我就只贴上一些注释，就不展开来讲</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; parse &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@babel/parser'</span>)
<span class="hljs-keyword">const</span> traverse = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@babel/traverse'</span>)
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-keyword">const</span> dir = path.<span class="hljs-title function_">resolve</span>(__dirname, <span class="hljs-string">'./server'</span>)
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)
<span class="hljs-comment">// 读取所有文件</span>
<span class="hljs-keyword">const</span> files = fs.<span class="hljs-title function_">readdirSync</span>(dir)
<span class="hljs-keyword">const</span> doc = &#123;&#125;
files.<span class="hljs-title function_">forEach</span>(<span class="hljs-function"><span class="hljs-params">filename</span> =></span> &#123;
    <span class="hljs-keyword">const</span> filepath = <span class="hljs-string">`<span class="hljs-subst">$&#123;dir&#125;</span>/<span class="hljs-subst">$&#123;filename&#125;</span>`</span>
    <span class="hljs-keyword">if</span> (!doc[filename]) doc[filename] = <span class="hljs-string">``</span>
    <span class="hljs-comment">// 读取文件内容</span>
    <span class="hljs-keyword">const</span> content = fs.<span class="hljs-title function_">readFileSync</span>(filepath, &#123; <span class="hljs-attr">encoding</span>: <span class="hljs-string">'utf8'</span> &#125;)
    <span class="hljs-comment">// 生成ast</span>
    <span class="hljs-keyword">const</span> ast = <span class="hljs-title function_">parse</span>(content)
    traverse.<span class="hljs-title function_">default</span>(ast, &#123;
        <span class="hljs-title class_">ExpressionStatement</span>: &#123;
            <span class="hljs-title function_">enter</span>(<span class="hljs-params">path</span>) &#123;
                <span class="hljs-keyword">if</span> (path.<span class="hljs-property">node</span>.<span class="hljs-property">leadingComments</span> && path.<span class="hljs-property">node</span>.<span class="hljs-property">leadingComments</span>.<span class="hljs-property">length</span> > <span class="hljs-number">0</span>) &#123;
                    <span class="hljs-keyword">let</span> comment = path.<span class="hljs-property">node</span>.<span class="hljs-property">leadingComments</span>[<span class="hljs-number">0</span>].<span class="hljs-property">value</span>
                    <span class="hljs-keyword">let</span> tableHead = <span class="hljs-literal">false</span>
                    comment = comment.<span class="hljs-title function_">split</span>(<span class="hljs-string">'\n'</span>).<span class="hljs-title function_">map</span>(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.<span class="hljs-title function_">replaceAll</span>(<span class="hljs-string">'*'</span>, <span class="hljs-string">''</span>).<span class="hljs-title function_">trim</span>()).<span class="hljs-title function_">filter</span>(<span class="hljs-function"><span class="hljs-params">v</span> =></span> !!v)
                    comment.<span class="hljs-title function_">forEach</span>(<span class="hljs-function"><span class="hljs-params">line</span> =></span> &#123;
                        <span class="hljs-keyword">const</span> result = line.<span class="hljs-title function_">split</span>(<span class="hljs-string">' '</span>).<span class="hljs-title function_">filter</span>(<span class="hljs-function"><span class="hljs-params">v</span> =></span> !!v)
                        <span class="hljs-keyword">const</span> commentName = result[<span class="hljs-number">0</span>]
                        <span class="hljs-comment">//  添加接口地址</span>
                        <span class="hljs-keyword">if</span> (commentName == <span class="hljs-string">'@path'</span>) &#123;
                            <span class="hljs-keyword">const</span> apiPath = result[<span class="hljs-number">1</span>]
                            doc[filename] += <span class="hljs-string">`
## <span class="hljs-subst">$&#123;apiPath&#125;</span>
`</span>
                        &#125;
                        <span class="hljs-keyword">if</span> (commentName == <span class="hljs-string">'@param'</span>) &#123;
                            <span class="hljs-comment">//  添加头部</span>
                            <span class="hljs-keyword">if</span> (!tableHead) &#123;
                                doc[filename] += <span class="hljs-string">`|参数名|参数描述|类型|是否必填|
|---|---|---|---|
`</span>
                                tableHead = <span class="hljs-literal">true</span>
                            &#125;
                            <span class="hljs-keyword">let</span> [_, fieldName, desc = <span class="hljs-literal">null</span>, type = <span class="hljs-literal">null</span>, required = <span class="hljs-string">'NoRequired'</span>] = result
                            doc[filename] += <span class="hljs-string">`|<span class="hljs-subst">$&#123;fieldName&#125;</span>|<span class="hljs-subst">$&#123;desc&#125;</span>|<span class="hljs-subst">$&#123;type.replaceAll(<span class="hljs-string">'|'</span>,<span class="hljs-string">'\\|'</span>)&#125;</span>|<span class="hljs-subst">$&#123;required === <span class="hljs-string">'Required'</span> ? <span class="hljs-literal">true</span> : <span class="hljs-literal">false</span>&#125;</span>|
`</span>
                        &#125;
                    &#125;)
                &#125;
            &#125;
        &#125;
    &#125;)
    <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">keys</span>(doc).<span class="hljs-title function_">forEach</span>(<span class="hljs-function"><span class="hljs-params">filename</span> =></span> &#123;
        <span class="hljs-comment">// 输出文档</span>
        fs.<span class="hljs-title function_">writeFileSync</span>(
            path.<span class="hljs-title function_">resolve</span>(__dirname, <span class="hljs-string">`./doc/<span class="hljs-subst">$&#123;filename.replace(<span class="hljs-string">'.js'</span>, <span class="hljs-string">'.md'</span>)&#125;</span>`</span>),
            doc[filename],
            &#123; <span class="hljs-attr">encoding</span>: <span class="hljs-string">'utf8'</span> &#125;
        )
    &#125;)
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后生成的接口文档就是下面这个样子的：</p>
<p><img src="https://img-1258692894.cos.ap-guangzhou.myqcloud.com/scdm7zp4fj.png?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDylHWUBbleFZgX7PQBfsoUt0qQjlWzC9o%26q-sign-time%3D1663427377%3B1666019437%26q-key-time%3D1663427377%3B1666019437%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D08b3b1e0eb034dd6a846a36a34deacac4d2f34b8&" alt="scdm7zp4fj.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实代码的实现并不难，但是这个生成文档的代码实现很难抽象出一个公共的方法，现在也有一些现成的库，比如 <code>jsdoc</code> 。但如果这些库不能满足你的特性化需求，你可以考虑使用上面的方式去实现自己的一套工具。上面是以接口文档作为例子，当然你也可以用来做组件的使用文档等等。</p>
<h1 data-id="heading-4">国际化</h1>
<p>国际化也是我们在业务中常常会遇见的需求，实现方式可能是用一些库或者自己实现一个 <code>translate</code> 函数，然后在代码里写各种文本的时候都需要用这个 <code>translate</code> 函数去套一下。其实这里也是可以利用 <code>Babel</code> 的静态分析特性，去自动的做这件事情，编码的时候还是照常写文本，经过 <code>Babel</code> 转换过后，生成的代码自动帮你套上 <code>translate</code> 函数。</p>
<p>我们这里主要处理两种节点：</p>
<ul>
<li>纯文本：对应 <code>StringLiteral</code> 类型</li>
<li>模版字符串：对应 <code>TemplateLiteral</code> 类型</li>
</ul>
<h2 data-id="heading-5">纯文本</h2>
<p>纯文本的处理还是比较简单的，假设我们的翻译函数是 <code>t</code> ，还是老套路，在上面的网站上看看<code> 文本</code> 跟 <code>t('文本')</code> 长得有什么区别，然后可以很快写出下面的代码：</p>
<pre><code class="hljs language-js copyable" lang="js">traverse.<span class="hljs-title function_">default</span>(ast, &#123;
    <span class="hljs-title class_">StringLiteral</span>: &#123;
        <span class="hljs-title function_">enter</span>(<span class="hljs-params">path</span>) &#123;
            <span class="hljs-keyword">const</span> &#123; value &#125; = path.<span class="hljs-property">node</span>
            <span class="hljs-keyword">if</span> (!(
                path.<span class="hljs-property">parent</span>.<span class="hljs-property">type</span> === <span class="hljs-string">'CallExpression'</span> && [<span class="hljs-string">'t'</span>, <span class="hljs-string">'require'</span>].<span class="hljs-title function_">includes</span>(path.<span class="hljs-property">parent</span>.<span class="hljs-property">callee</span>.<span class="hljs-property">name</span>)
            )
            ) &#123;
                <span class="hljs-keyword">const</span> astNode = t.<span class="hljs-title function_">callExpression</span>(
                    t.<span class="hljs-title function_">identifier</span>(<span class="hljs-string">'t'</span>),
                    [t.<span class="hljs-title function_">stringLiteral</span>(value)]
                )
                path.<span class="hljs-title function_">replaceWith</span>(astNode)
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要注意的是，有一些字符串是不需要再套用 <code>t</code> 函数的，比如本身就已经套用了 <code>t</code> 函数，或者是引用相关的路径。然后我们可以使用 <code>replaceWith</code> 这个方法来替换节点。</p>
<h2 data-id="heading-6">模版字符串</h2>
<p>下面再来看模版字符串的处理，如果转换前是这样的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> text3 = <span class="hljs-string">`<span class="hljs-subst">$&#123;num&#125;</span>：参数1：<span class="hljs-subst">$&#123;num1&#125;</span><span class="hljs-subst">$&#123;num1&#125;</span>，参数二：<span class="hljs-subst">$&#123;num2&#125;</span>`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那我希望转换后是这样的：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> text3 = <span class="hljs-title function_">t</span>(<span class="hljs-string">`#num#：参数1：#num1##num1#，参数二：#num2#`</span>, &#123;
  <span class="hljs-attr">num</span>: num,
  <span class="hljs-attr">num1</span>: num1,
  <span class="hljs-attr">num2</span>: num2
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么先来观察模版字符串的 <code>ast node</code> ：</p>
<p><img src="https://img-1258692894.cos.ap-guangzhou.myqcloud.com/gky8qhvmq2.png?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDylHWUBbleFZgX7PQBfsoUt0qQjlWzC9o%26q-sign-time%3D1663428996%3B1666021056%26q-key-time%3D1663428996%3B1666021056%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D692c438a0669ec3c97981a4720f81e984079c901&" alt="gky8qhvmq2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>里面有两个需要关注的属性：</p>
<ul>
<li><code>quasis</code> ：普通文本</li>
<li><code>expressions</code> ：表达式</li>
</ul>
<p>这两个属性之间有一个规律：一个表达式的两边一定是分别是一个普通文本，如果没有的话，那这个 <code>quasi</code> 里面的 <code>value</code> 属性就是空字符串。利用这个规律，我们就可以开始进行拼接与替换。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-title class_">TemplateLiteral</span>: &#123;
    <span class="hljs-title function_">enter</span>(<span class="hljs-params">path</span>) &#123;
        <span class="hljs-keyword">const</span> quasis = [...path.<span class="hljs-property">node</span>.<span class="hljs-property">quasis</span>]
        <span class="hljs-keyword">const</span> expressions = [...path.<span class="hljs-property">node</span>.<span class="hljs-property">expressions</span>]
        <span class="hljs-keyword">let</span> str = <span class="hljs-string">''</span>
        <span class="hljs-keyword">const</span> variables = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Set</span>()
        <span class="hljs-keyword">while</span> (quasis.<span class="hljs-property">length</span>) &#123;
            <span class="hljs-keyword">const</span> quasi = quasis.<span class="hljs-title function_">shift</span>()
            str += quasi.<span class="hljs-property">value</span>.<span class="hljs-property">raw</span>
            <span class="hljs-keyword">if</span> (expressions.<span class="hljs-property">length</span>) &#123;
                <span class="hljs-keyword">const</span> expression = expressions.<span class="hljs-title function_">shift</span>()
                str += <span class="hljs-string">`#<span class="hljs-subst">$&#123;expression.name&#125;</span>#`</span>
                <span class="hljs-comment">// 把变量收集起来</span>
                variables.<span class="hljs-title function_">add</span>(expression.<span class="hljs-property">name</span>)
            &#125;
        &#125;
        <span class="hljs-keyword">const</span> properties = []
        <span class="hljs-keyword">if</span> (variables.<span class="hljs-property">size</span> > <span class="hljs-number">0</span>) &#123;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> variable <span class="hljs-keyword">of</span> variables) &#123;
                <span class="hljs-keyword">const</span> property = t.<span class="hljs-title function_">objectProperty</span>(
                    t.<span class="hljs-title function_">identifier</span>(variable),
                    t.<span class="hljs-title function_">identifier</span>(variable)
                )
                properties.<span class="hljs-title function_">push</span>(property)
            &#125;
        &#125;
        <span class="hljs-keyword">const</span> args = [
            t.<span class="hljs-title function_">templateLiteral</span>(
                [
                    t.<span class="hljs-title function_">templateElement</span>(&#123;
                        <span class="hljs-attr">raw</span>: str,
                        <span class="hljs-attr">cooked</span>: str
                    &#125;)
                ],
                []
            ),
        ]
        <span class="hljs-keyword">if</span> (properties.<span class="hljs-property">length</span>) &#123;
            args.<span class="hljs-title function_">push</span>(
                t.<span class="hljs-title function_">objectExpression</span>(
                    properties
                )
            )
        &#125;
        <span class="hljs-comment">// 构建t函数抽象节点</span>
        <span class="hljs-keyword">const</span> astNode = t.<span class="hljs-title function_">callExpression</span>(
            t.<span class="hljs-title function_">identifier</span>(<span class="hljs-string">'t'</span>),
            args
        )
        <span class="hljs-comment">// 替换节点</span>
        path.<span class="hljs-title function_">replaceWith</span>(astNode)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为上面已经花了一些篇幅去讲如何构造节点，所以这里就不再详细的讲解了。替换前后的结果是这样的：</p>
<p><img src="https://img-1258692894.cos.ap-guangzhou.myqcloud.com/m550ps9q2k.png?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDylHWUBbleFZgX7PQBfsoUt0qQjlWzC9o%26q-sign-time%3D1663429370%3B1666021430%26q-key-time%3D1663429370%3B1666021430%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D6d04b6ffc0b0d70a1d93a5c72b77efd901dd23ba&" alt="m550ps9q2k.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">翻译函数</h2>
<p>最后一步，就是要实现一个全局的翻译函数。其实为什么要把模版字符串里面有变量的替换成那个样子呢？我们来看看中英文的一些表达，在中文里，我们说 <code>我手里有5个项目</code> ，对应英文其实可能是 <code>I have five projects</code> 。那么我们写在代码里就是 <code>我手里有$&#123;num&#125;个项目</code>，对应的英文词条是 <code>I have $&#123;num&#125; projects</code>，上述模版字符串的替换方式，可以看作一种中间状态，用一些占位符去标记，便于中英文转换时变量的插入。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = <span class="hljs-keyword">function</span> (<span class="hljs-params">string, params = &#123;&#125;</span>) &#123;
    <span class="hljs-keyword">const</span> en = &#123;
        <span class="hljs-string">'文本'</span>: <span class="hljs-string">'text'</span>,
        <span class="hljs-string">'#num#：参数1：#num1##num1#，参数二：#num2#'</span>: <span class="hljs-string">'#num#:param1:#num1##num1#,param2:#num2#'</span>,
        <span class="hljs-string">'字符串'</span>: <span class="hljs-string">'string'</span>
    &#125;
    <span class="hljs-keyword">let</span> result = en[string]
    <span class="hljs-keyword">if</span> (!result) <span class="hljs-keyword">return</span> string
    <span class="hljs-keyword">const</span> reg = <span class="hljs-regexp">/(#([^#][0-9a-zA-Z]+)#)/</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-title class_">Object</span>.<span class="hljs-title function_">keys</span>(params).<span class="hljs-property">length</span> === <span class="hljs-number">0</span>) &#123;
        <span class="hljs-keyword">return</span> result
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">let</span> regResult
        <span class="hljs-keyword">while</span> (regResult = reg.<span class="hljs-title function_">exec</span>(result)) &#123;
            <span class="hljs-keyword">const</span> origin = result[<span class="hljs-number">1</span>]
            <span class="hljs-keyword">const</span> variable = result[<span class="hljs-number">2</span>]
            result = result.<span class="hljs-title function_">replace</span>(origin, params[variable])
        &#125;
        <span class="hljs-keyword">return</span> result
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以上面转换过后的代码输出结果如下，整体是符合预期的：</p>
<p><img src="https://img-1258692894.cos.ap-guangzhou.myqcloud.com/o006c6urqh.png?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDylHWUBbleFZgX7PQBfsoUt0qQjlWzC9o%26q-sign-time%3D1663430083%3B1666022143%26q-key-time%3D1663430083%3B1666022143%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D16b42f7fc3dfef78bcff446d82afdcaf611a930b&" alt="o006c6urqh.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-8">最后</h1>
<p>本文举了三个实际应用中遇到的例子，并以 <code>Babel</code> 的方式去解决，属于是抛砖引玉。如果你平时在实际场景中还使用到 <code>Babel</code> 来做一些其他的事情的话，欢迎在评论区一起交流～如果你觉得这篇文章有用或者有趣的话，点点关注点点赞吧～</p></div>  
</div>
            