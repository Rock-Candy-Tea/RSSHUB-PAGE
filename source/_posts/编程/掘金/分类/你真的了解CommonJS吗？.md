
---
title: '你真的了解CommonJS吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad25d9e1801049ed88bc343f3767c98e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 24 May 2021 03:41:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad25d9e1801049ed88bc343f3767c98e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这篇文章主要从历史角度介绍一下Commonjs模块机制</p>
<h1 data-id="heading-0">1. Comminjs规范</h1>
<h2 data-id="heading-1">1.1 Comminjs出发点</h2>
<p>在js发展前期，它主要是在浏览器环境发光发热，由于ES规范规范化的时间比较早，所以涵盖的范畴比较小，但是在实际应用中，js的表现取决于宿主环境对ES规范的支持程度，随着web2.0的推进，HTML5崭露头角，它将web从网页时代带进了应用时代，并且在ES标准中出现了更多、更强大的api，在浏览器中也出现了更多、更强大的api供js调用，这需要感谢各大浏览器厂商对规范的大力支持，然而，浏览器的更新迭代和api的升级只出现在前端，后端的js规范却远远落后，对于js自身而言，它的规范依然是十分薄弱的，还存在一些严重的缺陷，比如：没有模块标准。</p>
<p>Commonjs规范的提出，主要是为了弥补当初js没有模块标准的缺点，以达到像其它语言（例如Java、Python）那样具备开发大型应用的基础能力，而不是停留在脚本程序的阶段。他们期望用commonjs规范写出的应用具备跨宿主环境（浏览器环境）执行的能力，这样不仅可以利用js编写web程序，而且也可以编写服务器、命令行工具、甚至桌面应用程序。</p>
<p>理论和实践总是相互影响和促进的，Node能以一种比较成熟的姿态出现，离不开Commonjs规范的影响，同样，在服务端，Commonjs能以一种寻常的姿态写进各个公司的项目中，也离不开Node优异的表现，下图是Node与W3C、还有浏览器，Commonjs组件、ES规范之间的关系：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad25d9e1801049ed88bc343f3767c98e~tplv-k3u1fbpfcp-watermark.image" alt="1234.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Node借鉴了Commonjs的模块化规范实现了一套非常易用的模块。</p>
<h2 data-id="heading-2">1.2 Comminjs模块规范</h2>
<p>commonjs对模块的定义十分简单，主要分为<code>模块引用</code>、<code>模块定义</code>、<code>模块标识</code>三个部分。</p>
<h3 data-id="heading-3">1.2.1 模块引用</h3>
<p>模块引用的示例代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在规范中，存在require()方法，这个方法接收<code>模块标识</code>，以此入一个模块的API到当前上下文中。</p>
<h3 data-id="heading-4">1.2.2 模块定义</h3>
<p>出了引入的功能之外，上下文还提供了exports对象，用于导出当前模块的方法或者变量，并且它是唯一导出的出口，在模块中，还存在一个module对象，代表模块自身，而exports是module的属性，在Node中，一个文件就是一个模块，将方法挂载在exports对象上作为属性即可定义导出的方式：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">exports</span>.add = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// ……</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在另一个文件中，我们通过require()方法引入模块后，就能调用方法或者属性了：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> math = <span class="hljs-built_in">require</span>(<span class="hljs-string">'math'</span>);
<span class="hljs-keyword">const</span> result = math.add(<span class="hljs-number">10</span>, <span class="hljs-number">20</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">1.2.3 模块标识</h3>
<p>模块标识其实就是传递给require()函数的参数，它必须是符合<code>小驼峰命名的字符串</code>，或者是
以 <code>.</code> 和 <code>..</code> 开头的相对路径或者绝对路径，它可以没有文件名后缀.js</p>
<p>模块的定义十分简单，接口也十分简洁，它的意义在于将累聚的方法或者变量限定在私有的作用域用，同时支持引入和导出功能以顺畅的衔接不同的模块（文件），每个模块具有独立的空间，它们互不干扰，在引用的时候也显得干净利落。</p>
<h1 data-id="heading-6">2. Node的模块实现</h1>
<p>尽管规范中exports、require֖和module听起来十分简单，但是Node在实现它的过程中究竟经历了什么，这个过程需要知晓：</p>
<p>在Node中引入模块，需要经历如下三个步骤：<code>路径分析</code>、<code>文件定位</code>、<code>编译执行</code></p>
<p>需要注意的是，在Node中，模块分为两类，一类是Node内置的模块，称为<code>核心模块</code>；另一类是用户编写的模块，称为<code>文件模块</code>。</p>
<ul>
<li>核心模块在Node源码的编译过程中，编译进了二进制文件，在进程启动时，部分核心模块就直接被加载进内存，这部分核心模块引入时，文件定位和编译执行这两个步骤可以省略掉，并且在路径分析的过程中优先判断，所以这部分的加载速度是最快的。</li>
<li>文件模块是在运行时动态加载，需要完整的路径分析、文件定位、编译执行过程，速度比核心模块慢。</li>
</ul>
<p>接下来，我们详细分析一下模块加载的过程：</p>
<h2 data-id="heading-7">2.1 优先从缓存加载</h2>
<p>在此之前，我们需要知晓的一点是，与浏览器会缓存静态文件从而提高性能一样，Node也会对引入过的模块进行缓存，以减少二次引入时的开销。不同的地方在于，浏览器只缓存文件，而Node缓存的是编译的对象。</p>
<p>不论是核心模块还是文件模块, require()方法对相同模块的二次加载都一律采用缓存优先的方式，这是第一优先级的。并且核心模块的缓存检查优先于文件模块的缓存检查。</p>
<h2 data-id="heading-8">2.2 路径分析和文件定位</h2>
<p>因为模块标识有几种形式，对于不同的标识符，模块查找和定位都有不同程度的差异。</p>
<h3 data-id="heading-9">2.2.1 模块标识符分析</h3>
<p>前面提到过，require()方法接收一个标识符作为参数，标识符在Node中主要分为以下几类：</p>
<ul>
<li>核心模块（内置模块），比如http、fs、path等</li>
<li>以 / 开头的绝对路径或者相对路径的文件模块</li>
<li>非路径形式的文件模块，如自定义的模块</li>
</ul>
<h4 data-id="heading-10">2.2.1.1 核心模块</h4>
<p>核心模块的优先级仅次于缓存加载，它在Node的源代码编译过程中编译为二进制代码，加载过程最快。</p>
<p>如果试图加载一个与核心模块标识符相同的自定义模块，那是不会成功的。如果自己编写了一个http用户模块，想要加载成功，必须选择一个不同的标识符或者换用路径的方式。</p>
<h4 data-id="heading-11">2.2.1.2 文件模块</h4>
<p>以 . 和 / 开头的标识符，都被当做文件模块来处理。在分析文件模块时，require()方法会将路径转为真实路径，并以真实路径作为索引，将编译执行后的结果存放到缓存中，以使二次加载时更快。</p>
<p>由于文件模块给Node指明了确切的文件位置,所以在查找过程中可以节约大量时间，其加载速度慢于核心模块。</p>
<h4 data-id="heading-12">2.2.1.3 自定义模块</h4>
<p>自定义模块指的是非核心模块，也不是路径形式的标识符。它是一种特殊的文件模块，可能是一个文件或者包的形式。这类模块的查找是最费时的，也是所有方式中最慢的一种。</p>
<p>在介绍自定义模块的查找方式之前，需要先介绍一下模块路径这个概念，关于这个路径的生成规则，我们可以手动尝试一番：在任意一个目录下创建一个js文件，然后打印出module.paths：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">module</span>.paths);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后执行代码，可以得到如下结果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a1dee7d5c434e578cb839c7437ecaeb~tplv-k3u1fbpfcp-watermark.image" alt="555.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，模块路径的内容具体表现为一个路径组成的数组，数组的生成规则如下：</p>
<ul>
<li>当前文件目录下的node_modules目录。</li>
<li>父目录下的node_modules目录。</li>
<li>父目录的父目录下的node_modules目录。</li>
<li>父目录的父目录的父目录下的node_modules目录。</li>
<li>沿路径向上逐级递归，直到根目录下的node_modules目录。</li>
</ul>
<p>它的生成方式与js的原型链或作用域链的查找方式十分类似。在加载的过程中，Node会逐个尝试模块路径中的路径，直到找到目标文件为止。可以看出，当前文件的路径越深，模块查找耗时会越多，这也是自定义模块的加载速度是最慢的原因。</p>
<h3 data-id="heading-13">2.2.2 文件定位</h3>
<p>从缓存加载的优化策略使得二次引人时不需要路径分析、文件定位和编译执行的过程，大大提高了再次加载模块时的效率。但在文件的定位过程中，还有一些细节需要注意，这主要包括文件扩展名的分析、目录的处理：</p>
<h4 data-id="heading-14">2.2.2.1 后缀分析：</h4>
<ul>
<li>
<p>require()在分析标识符的过程中，会出现标识符中不包含文件扩展名的情况。CommonJS模块规范也允许在标识符中不包含文件扩展名，这种情况下，Node会按.js、.json、.node的次序补足扩展名，依次尝试。</p>
</li>
<li>
<p>在尝试的过程中，需要调用fs模块同步阻塞式地判断文件是否存在。因为Node是单线程的，所以这里是一个会引起性能问题的地方。小诀窍是：如果是.node和.json文件，在传递给require()的标识符中带上文件后缀，会加快一点速度。另一个诀窍是：同步配合缓存，可以大幅度缓解Node单线程中阻塞式调用的缺陷。</p>
</li>
</ul>
<h4 data-id="heading-15">2.2.2.2 目录分析：</h4>
<ul>
<li>
<p>在分析标识符的过程中，require()通过分析文件扩展名之后，可能没有查找到对应文件，但却得到一个目录，这在引入自定义模块和逐个模块路径进行查找时经常会出现，此时Node会将目录当做一个包来处理。</p>
</li>
<li>
<p>在这个过程中，Node对CommonJS包规范进行了一定程度的支持。首先，Node在当前目录下查找package.json，通过JSON.parse()解析出包描述对象，从中取出main属性指定的文件名进行定位。如果文件名缺少扩展名，将会进行后缀分析的步骤。</p>
</li>
<li>
<p>如果main属性指定的文件名错误，或者压根没有package.json文件，Node会将index当做默认文件名，然后依次查找index.js、index.json、index.node。</p>
</li>
<li>
<p>如果在目录分析的过程中没有定位成功任何文件，则自定义模块进入下一个模块路径进行查找。如果模块路径数组都被遍历完毕，依然没有查找到目标文件，则会抛出查找失败的异常。</p>
</li>
</ul></div>  
</div>
            