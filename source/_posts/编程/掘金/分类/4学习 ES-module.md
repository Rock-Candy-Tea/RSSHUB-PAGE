
---
title: '4.学习 ES-module'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abee17649fd2401c848dbc9dd9e52396~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 06:11:23 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abee17649fd2401c848dbc9dd9e52396~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第4天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<blockquote>
<p>es module, ES Module的使用也很简单，相关语法也很少，核心是import和export</p>
</blockquote>
<blockquote>
<p>所有主流浏览器都将支持 ES 模块</p>
</blockquote>
<h2 data-id="heading-0">1.模块解决什么问题？</h2>
<blockquote>
<p>用 JavaScript 编码就是管理变量。这一切都是关于为变量赋值，或为变量添加数字，或将两个变量组合在一起并将它们放入另一个变量中</p>
</blockquote>
<pre><code class="copyable">let a = 1;
a += 2
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>由于作用域在 JavaScript 中的工作方式，函数无法访问在其他函数中定义的变量</p>
</blockquote>
<blockquote>
<p>如果您确实想在范围之外共享变量怎么办？处理这个问题的一种常见方法是将它放在您上方的范围内……例如，放在全局范围内,但它们会导致一些烦人的问题。</p>
</blockquote>
<p>首先，所有脚本标签都需要按正确的顺序排列。然后你必须小心确保没有人把这个顺序弄乱。</p>
<p>如果您确实弄乱了该顺序，那么在运行过程中，您的应用程序将抛出错误</p>
<blockquote>
<p>一旦您能够在模块之间导出和导入变量，就可以更轻松地将代码分解为可以相互独立工作的小块。然后你可以组合和重新组合这些块，有点像乐高积木，从同一组模块创建所有不同类型的应用程序。</p>
</blockquote>
<h2 data-id="heading-1">2.模块如何提供帮助？</h2>
<blockquote>
<p>模块提供了一种更好的方式来组织这些变量和函数。使用模块，可以将有意义的变量和函数组合在一起。</p>
</blockquote>
<blockquote>
<p>这将这些函数和变量放入模块范围。模块作用域可用于在模块中的函数之间共享变量</p>
</blockquote>
<h2 data-id="heading-2">Module Instances</h2>
<blockquote>
<p>当使用模块进行开发时，会构建一个依赖关系图。不同依赖项之间的连接来自使用的任何导入语句</p>
</blockquote>
<p>从入口文件开始，浏览器或者Node就沿着每一条"import"语句找到下面的代码。</p>
<pre><code class="copyable">main.js

import &#123; count &#125; from './counter.js';
import &#123; render &#125; from './dispaly.js';
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是，浏览器却使用不了这些文件。所有的文件都必须要转变为一系列被叫做“Module Records（模块记录）的数据结构，这样浏览器才能明白这些文件的内容。</p>
<p>在这之后，module record需要被转化为“module instance（模快实例）”。一个module instance包含2种东西：code和state。</p>
<p>code就是一系列的操作指令，就像菜单一样。但是，光有菜单，并不能作出菜，你还需要原材料。</p>
<p>而state就是原材料。State就是变量在每一个特地时间点的值。当然，这些变量只是内存里面一个个保存着值的小盒子的小名而已。</p>
<h2 data-id="heading-3">模块实例的产生步骤</h2>
<p>对于，ES Module来说，这需要经历三个步骤：</p>
<ul>
<li>1: 构建- 找到，下载所有的文件并且解析为module records。</li>
<li>2: Instantiation（实例化）- 在内存里找到所有的“盒子”，把所有导出的变量放进去（但是暂时还不求值）。然后，让导出和导入都指向内存里面的这些盒子。这叫做“linking(链接)”。</li>
<li>3: Evaluation（求值）- 执行代码，得到变量的值然后放到这些内存的“盒子”里。</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abee17649fd2401c848dbc9dd9e52396~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">构建</h2>
<p>对于每一个模块来说，构建阶段，每个模块都会发生三件事:</p>
<ul>
<li>1: 去哪里下载包含模块的文件（又叫“ module resolution（模块识别）”）</li>
<li>2: 获取文件（通过从一个URL下载或者从文件系统加载）</li>
<li>3: 把文件解析为module record（模块记录）</li>
</ul>
<h3 data-id="heading-5">1.查找文件并获取它</h3>
<blockquote>
<p>加载程序将负责查找文件并下载它。首先它需要找到入口点文件。在 HTML 中，您可以使用脚本标记告诉加载器在哪里找到它。</p>
</blockquote>
<pre><code class="copyable"><script src="main.js" type="module"></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">解析</h4>
<p>现在我们已经获取了这个文件，我们需要把它解析成一个模块记录。这有助于浏览器了解模块的不同部分是什么。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2F2r4s9p1yi1fa2jd7j43zph8r-wpengine.netdna-ssl.com%2Ffiles%2F2018%2F03%2F25_file_to_module_record.png" target="_blank" rel="nofollow noopener noreferrer" title="https://2r4s9p1yi1fa2jd7j43zph8r-wpengine.netdna-ssl.com/files/2018/03/25_file_to_module_record.png" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47bdb1a77333434aae7b0663146ab4fe~tplv-k3u1fbpfcp-watermark.image" alt="显示正在解析为模块记录的 main.js 文件的图表" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>创建模块记录后，将其放置在模块映射中。这意味着无论何时从现在开始请求它，加载器都可以从该地图中提取它。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2F2r4s9p1yi1fa2jd7j43zph8r-wpengine.netdna-ssl.com%2Ffiles%2F2018%2F03%2F25_module_map.png" target="_blank" rel="nofollow noopener noreferrer" title="https://2r4s9p1yi1fa2jd7j43zph8r-wpengine.netdna-ssl.com/files/2018/03/25_module_map.png" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce6b8ac2fd194fd39aa1e3a0fe79855f~tplv-k3u1fbpfcp-watermark.image" alt="用模块记录填充的模块映射图中的“获取”占位符" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>解析中有一个细节看似微不足道，但实际上却有很大的影响。所有模块都被解析，就好像它们<code>"use strict"</code>在顶部一样</p>
<h4 data-id="heading-7">实例化</h4>
<blockquote>
<p>实例结合了代码和状态。该状态存在于内存中，因此实例化步骤就是将事物连接到内存中。</p>
</blockquote>
<blockquote>
<p>首先，JS引擎创建一个模块环境记录。这管理模块记录的变量。然后它在内存中找到所有导出的框。模块环境记录将跟踪内存中的哪个框与每个导出相关联。</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9b362dc14124aab8756fb670f240918~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<blockquote>
<blockquote>
<p>仅供学习参考</p>
</blockquote>
</blockquote>
</blockquote>
<h2 data-id="heading-8">参考</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fhacks.mozilla.org%2F2018%2F03%2Fes-modules-a-cartoon-deep-dive%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://hacks.mozilla.org/2018/03/es-modules-a-cartoon-deep-dive/" ref="nofollow noopener noreferrer">es-modules-a-cartoon-deep-dive/</a></li>
</ul></div>  
</div>
            