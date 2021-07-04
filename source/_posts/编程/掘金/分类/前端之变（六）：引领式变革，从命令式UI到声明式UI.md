
---
title: '前端之变（六）：引领式变革，从命令式UI到声明式UI'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7913'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 06:11:20 GMT
thumbnail: 'https://picsum.photos/400/300?random=7913'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>当我在2020年使用前端的技术栈去编写一个跨平台桌面App时，发现前端在UI方面其模式与我在移动端接触到的有很大的差异，那时候我意识到原来在前端，其UI使用的是另一种模式，后面我才知道它的名字：<strong>声明式UI</strong></p>
<p>事实上，前端本身也经历了变革，至少在JQuery时代，它与移动端一致，其UI模式仍然属于传统的命令式UI，但到了React及Vue的时代，它变成了声明式UI。从我有限的知识来看，至少在大前端的其它两个方向：移动端与桌面开发，并未优先引领式的出现这种变革。</p>
<p>因此，我把前端的这种变革，称之为：<strong>引领式变革</strong>。</p>
<p>它改变的不仅仅是自己。而且正在改变移动端，无论是Android官方自己主推的Jetpack，还是iOS官方新的UI框架SwiftUI，与之前也完全不同，都从命令式UI变为声明式UI。很难说这种变革，没有受到前端的影响或借鉴。</p>
<p>这说明前端技术变革不仅改变了自身，甚至在一些方面走在了更前面。</p>
<p>本周，继续就前端之变阐述自己的思考与分析。这是第六篇。前面几篇分别是：</p>
<ol>
<li><a href="https://taoofcode.cc/blogs/2021-05-16/the_change_of_front_1" target="_blank" rel="nofollow noopener noreferrer">前端之变（一）：技术的变与不变</a></li>
<li><a href="https://taoofcode.cc/blogs/2021-05-23/the_change_of_front_2" target="_blank" rel="nofollow noopener noreferrer">前端之变（二）: "不变"的前端</a></li>
<li><a href="https://taoofcode.cc/blogs/2021-05-30/the_change_of_front_3" target="_blank" rel="nofollow noopener noreferrer">前端之变（三）：变革与突破</a></li>
<li><a href="https://taoofcode.cc/blogs/2021-06-05/the_change_of_front_4" target="_blank" rel="nofollow noopener noreferrer">前端之变（四）：进击的前端</a></li>
<li><a href="https://taoofcode.cc/blogs/2021-06-20/the_change_of_front_5" target="_blank" rel="nofollow noopener noreferrer">前端之变（五）：王者归来</a></li>
</ol>
<h2 data-id="heading-0">命令式与声明式</h2>
<p>首先，要明确一个前提，UI这个事情，只在<strong>大前端</strong>才有。所以，无论是命令式UI还是声明式UI，在后端编码是不存在这个概念的。</p>
<p>当然，若干年前，后端兼顾前端页面的开发，但那个时代已经过去了。现在主流的模式应该是前后端分离，由后端人员同时来开发前端，比如用JSP或FreeMarker模板技术的做法，在现在应该不多见了，不能算主流了。</p>
<p>UI这个事情并非只在Web前端才有，事实上，在技术的几个方向，除了后端以外，包括前端，移动端及桌面端都存在UI。</p>
<p>因此，无论是命令式UI，还是声明式UI，其概念是同时适应于前端，移动端以及桌面端的。</p>
<p>在这个前提之下，我们就可以来仔细分析下，在前端发生变革以前，事实上无论是在前端，移动端还是桌面端，其UI的编码模式都属于<strong>命令式UI</strong></p>
<blockquote>
<p>什么是命令式UI</p>
</blockquote>
<p><em><strong>UI的更新是由程序员使用代码主动刷新，UI与数据并无必然的映射关系，这种我们称之为命令式UI</strong></em></p>
<blockquote>
<p>什么是声明式UI</p>
</blockquote>
<p><em><strong>UI的更新并非由程序员使用代码来主动刷新，而是由后面隐藏机制来负责维护UI的刷新，UI与数据有映射关系，这种我们就称之为声明式UI</strong></em></p>
<p>上面这种定义是我的定义，根据上述定义，区分是命令式UI还是声明式UI的两个核心点是：</p>
<ol>
<li>程序员是否要显式的去调用代码刷新UI</li>
<li>UI与数据是否存在映射关系</li>
</ol>
<h2 data-id="heading-1">传统UI模式：命令式UI</h2>
<p>我们回到过往的时光，在那个还是JQuery主导前端开发的时代，我们设想一个最简单的需求：<strong>记住上一次的登录用户名</strong></p>
<p>我在这里用前端与移动端的代码来示例，展现命令式UI的做法:</p>
<blockquote>
<p>前端</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//基于JQuery的实现</span>
<span class="hljs-keyword">const</span> lastLoginUsername = localstorage.getItem(<span class="hljs-string">"lastLoginUsername"</span>)
$(<span class="hljs-string">"#username"</span>).val(lastLoginUsername);<span class="hljs-comment">//主动刷新UI</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>移动端</p>
</blockquote>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">//Android + Java</span>
String lastLoginUsername = preferences.getString(<span class="hljs-string">"lastLoginUsername"</span>, <span class="hljs-string">""</span>);
usernameInput.setText(lastLoginUsername);<span class="hljs-comment">//主动刷新UI</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述的这些实现，就是典型的命令式UI，它都具备几个特点：</p>
<ul>
<li>在程序中，你可以显式的引用或拿到UI组件</li>
<li>UI组件的内容是怎么样，什么时候改变内容，都是由程序员在合适的时候进行处理。UI本身与数据并无直接的映射关联，都是由程序员将数据显式的注入到UI中。</li>
</ul>
<p>无论是传统的前端开发，还是我前些年开发原生iOS与Android，都统一属于这种模式。它们都毫不例外的属于命令式UI。</p>
<p>这种命令式UI的模式，是存在一些问题的，表现在：</p>
<p><strong>UI维护工作较重</strong></p>
<p>从上面我的描述可以看出，整体UI行为，怎么样，什么时候怎么改变，要全部由程序员使用代码来处理。可想而知，这个过程显然是非常繁重的。事实上，可以说，无论是过往的前端，还是现在的移动端，可能有相当一部分工作都是在处理UI的各种刷新上面。</p>
<p><strong>易于出错</strong></p>
<p>很显然，需要刷新UI的时机很多，比如下拉刷新，通知数据变更，网络不好数据加载错误，其它模块变更引发的联动UI变更等等，很多情况下需要你处理UI的刷新工作。</p>
<p>需要处理的事情一旦多起来，出错的概率就再所难免了。</p>
<p><strong>性能不佳</strong></p>
<p>通过一个UI包含很多内容与组件，但需要刷新时，你是怎么处理刷新的？</p>
<p>是不管三七二十一，将所有UI内容全部设置一下，还是先对比下，有改变的再刷新，没改变的不再刷新？</p>
<p>可能有相当一部分比例，是属于全部设置一下的做法。这种的性能肯定不会太好，产生了许多不必要刷新。</p>
<p>当然，如果你比对然后只尽量做必要性的刷新，那这个事也有相当的复杂度的，而且可能易于出错。</p>
<p><strong>UI与数据易出现不一致</strong></p>
<p>想像一下吧，你的代码中有一份数据，这份数据决定了UI的展现，但事实上程序员是分开处理这两个部分的，由一些代码来调用刷新数据，再由一些方法现刷新UI，无论你做的多么周到，出现数据变更 ，UI却忘记刷新的可能性仍然是非常高的。</p>
<p>因此，UI与数据出现不一致的可能性极高。</p>
<p>所幸，声明式UI出现了，它极大的改善了这些问题。</p>
<h2 data-id="heading-2">变革之道：声明式UI</h2>
<p>声明式UI与命令式UI的最核心的区别在于：</p>
<ol>
<li>UI是数据的映射与描述，甚至一些框架中，程序员是无法持有UI组件的。更谈不上去调用这个组件的方法刷新UI了。</li>
<li>程序员关心的只是数据，只需要在合适的时机刷新数据就行了。UI则根据映射，由技术背后的机制帮你去刷新处理。</li>
</ol>
<p>很显然，这是对<strong>命令式UI</strong>做了根本性的改变。</p>
<p>我在这举一个简单的例子，仍然以<strong>记住上一次登录用户</strong>这个需求为例。</p>
<pre><code class="hljs language-react copyable" lang="react">//代码做了删减，只保留了有关的部分
export const LoginView = observer(() => &#123;

  const [username, setUsername] = useState(localStorage.getItem('login_username'));

  return (
    <Input className="input_username" value=&#123;username&#125; onChange=&#123;e => setUsername(e.target.value)&#125; />
  );
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是一个React代码，你可以看到，input_username这个输入框的值是&#123;username&#125;这个变量，而要修改这个输入框的值的方式，也不是调用UI的方法去设置值，而是通过改变username这个变量来实现。</p>
<p>所以，修改这个UI的内容的方法是</p>
<pre><code class="hljs language-react copyable" lang="react">onChange=&#123;e => setUsername(e.target.value)&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一旦你改变了username的值，input_username的内容自动的刷新改变了，并不需要程序员去介入UI的刷新工作。</p>
<p>这就是<strong>声明式UI</strong></p>
<p><strong>声明式UI</strong>如果要论述，可以说的很多，我这篇文章的目的不在于此。就不详细去解释它了。</p>
<p>当然，很明显，与命令式UI相比，上述的几个缺点都有所改善：</p>
<p><strong>程序员没有复杂的UI操作</strong></p>
<p>在声明式UI中，程序员要做的就是定义数据与UI的映射关系而已，一旦定义好后，后面只需要关心数据的维护，不需要再关心UI的刷新了，这极大的减轻了程序员的在UI上的工作。</p>
<p>事实上，以我个人编写移动端与前端的经历来看，前端的UI编写的确更快，更有效率</p>
<p><strong>难以出错</strong></p>
<p>显而易见的是吧，UI刷新是由框架或技术背后实现的，你只需要刷新数据就可以了，框架或技术的可靠性保证了不太可能出现数据刷新了，UI却没刷新或刷新出错的情况。</p>
<p><strong>极高的性能</strong></p>
<p>由于对数据的映射与刷新是框架在背后处理的，通过大部分框架都不会数据一变就全量刷新，这就太low了。</p>
<p>比如，React就有一个diff算法，这个算法保证了只进行必要的刷新，这是非常高效的做法。</p>
<p><strong>UI与数据的一致性</strong></p>
<p>你只需要关心数据，变更数据。并不需要担心数据与UI出现不一致的情况。</p>
<p>在框架质量有所保证的前提下，这种可能几乎为小的可以忽略不计。(框架也可能有BUG，不能期望它为0)</p>
<h2 data-id="heading-3">趋势，大前端UI的未来</h2>
<p>当然，『后』前端阶段，无论是React或Vue，都已经是这种声明式UI的做法了，它已经是前端的事实与主流了。</p>
<p>而在移动端，Android现在本身主推的是Jetpack，而iOS主推的是SwiftUI，这些也都是声明式UI了。但在移动端，它们仍然只是趋势，移动端现在绝大部分主流可能仍然是过往的命令式UI。</p>
<p>但可想而知，就算移动端，未来也必然会转向声明式UI。</p>
<p>至于移动端非原生的技术，类似Flutter,React Native等就不用说了，这些已经是声明式UI的实现了。</p>
<p>至于桌面端，由于我只有基于Electron开发桌面软件的经验，这是个前端技术，当然也是声明式UI，至于原生Window或Linux桌面开发，我并未有相关经验，但我相信借鉴声明式UI也绝对是正确的趋势。</p>
<p>所以，做为一个大前端的程序员，无论你是前端或是移动端，还是桌面端，你都要做好迎接声明式UI的未来的准备。</p>
<h2 data-id="heading-4">前端之困</h2>
<p>前端发生了巨大的变革，如我所言，这种变化是革命性的，颠覆性的。</p>
<p>但从我在前端的经验来看，无论是前端语言的生态，还是质量，与后端仍存在一些差距，这就非常值得我的思考，如果理念与技术并没有问题，那问题究竟在哪？</p>
<p>下一篇，前端之变（七）：前端之困，继续就前端阐述我的思考与分析。</p></div>  
</div>
            