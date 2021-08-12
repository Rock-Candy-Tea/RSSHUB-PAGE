
---
title: '利用lerna管理多框架日历组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95987c4030c244bda407ea1076d1182a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 22:59:57 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95987c4030c244bda407ea1076d1182a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>最近在开发公司内部使用的小程序框架，第一次接触到了多包管理工具 -- <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flerna%2Flerna%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/lerna/lerna/" ref="nofollow noopener noreferrer">lerna</a></p>
</blockquote>
<p>本篇将会以个人开发的<a href="https://juejin.cn/post/6946154756721115166" target="_blank" title="https://juejin.cn/post/6946154756721115166">日历组件</a>为例，简述使用lerna管理项目的历程。</p>
<p>也许大家会问了，你这日历组件不是vue写的🐴要lerna管理个啥。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95987c4030c244bda407ea1076d1182a~tplv-k3u1fbpfcp-watermark.image" alt="时代变了" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在构思组件开发时就想着能够为多框架的用户提供支持，所以就有了<strong>react/vue/小程序</strong>版本。</p>
<h2 data-id="heading-0">初探lerna</h2>
<p>回到正题，我们先看一看项目的目录结构。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c517857c5fc447369f340b13ccc00f17~tplv-k3u1fbpfcp-watermark.image" alt="WX20210618-205140@2x.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>按照lerna项目默认的项目结构，我们会将需要管理的包都放进<code>packages</code>文件夹内，并在根目录的<code>lerna.json</code>中编写lerna相关的配置。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79a9c5b6d86643c88328b64b205ec6e8~tplv-k3u1fbpfcp-watermark.image" alt="WX20210618-205226@2x.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>packages</code>文件夹内的结构如上图，代表我使用lerna同时在管理4个包，分别基于vue/react/原生微信小程序开发而成的日历组件，以及负责处理日历核心逻辑的<code>core</code>包。</p>
<p><a href="https://juejin.cn/post/6946154756721115166" target="_blank" title="https://juejin.cn/post/6946154756721115166">日历组件</a>文中有提及，笔者对一个上古时期的日历组件做了一次优化，优化的重点是<strong>抽离</strong>及<strong>易读</strong>。</p>
<p>在抽离的过程中发现，其实<strong>生成日历数据</strong>这件事，不论这个组件是vue开发的还是react开发甚至是小程序组件，都需要这段逻辑。所以我们可以将其进行更彻底的抽离，直接将这类逻辑收束成依赖包，供所有类型的日历组件进行调用。</p>
<p>核心逻辑具体实现就不再赘述了，基本和前一篇文章阐述的一致。关于日历视图层react以及小程序的实现，基本就是将Vue中的实现“翻译”成框架对应的写法。如果大家有兴趣的话可以点击下方的传送门↓↓</p>
<h3 data-id="heading-1">React组件实现<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmykurisu%2Fcalendar%2Ftree%2Fmaster-next%2Fpackages%2Freact" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/mykurisu/calendar/tree/master-next/packages/react" ref="nofollow noopener noreferrer">(Github传送门)</a></h3>
<p>在React实践中，比较特别的有两个地方：</p>
<ul>
<li>用useMemo替代vue实现中的computed</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> isFirstMonth = useMemo(<span class="hljs-function">() =></span> selectedMonth === <span class="hljs-number">0</span>);

<span class="hljs-keyword">const</span> isLastMonth = useMemo(<span class="hljs-function">() =></span> selectedMonth === <span class="hljs-number">11</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>用useLayoutEffect替代vue实现中的nextTick</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">
useLayoutEffect(<span class="hljs-function">() =></span> &#123;

    setBlockHeight(<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.__main__block-head'</span>).offsetWidth + <span class="hljs-string">"px"</span>);

&#125;, [calendarData]);

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">微信小程序组件实现<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmykurisu%2Fcalendar%2Ftree%2Fmaster-next%2Fpackages%2Fminiapp" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/mykurisu/calendar/tree/master-next/packages/miniapp" ref="nofollow noopener noreferrer">(Github传送门)</a></h3>
<p>小程序本身的开发模式就和vue谜之相似，基本上可以说是无痛移植，就是在获取日历方块宽度的时候没法用<code>querySelector</code>，必须得使用小程序自己的API<code>createSelectorQuery</code>。</p>
<p>但是在样式这块就不太一样，微信小程序只认与wxml同名的wxss文件，不支持样式的导入，所以在进行核心逻辑打包的时候同时执行一个<code>miniapp-script.js</code>，将css文件复制到miniapp目录中并更改其后缀名。</p>
<h2 data-id="heading-3">lerna实践</h2>
<p>结合上面的描述，我们只能认为lerna是一种包管理的思维，将原来的单项目对单依赖包的模式变成了单项目对多依赖包，并看不出它有什么其他实质性的帮助。</p>
<p>但是当我准备将写好的4个依赖包发布到npm时，遇到了比较棘手的问题，这4个依赖的打包方式完全不同，发布的时候岂不是得cd到每个包里进行install、build、version等机械式的操作。（其实并不用）</p>
<p>首先，先看看创建lerna项目的第一步，<code>lerna.json</code>的配置。</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;

    <span class="hljs-attr">"version"</span>: <span class="hljs-string">"independent"</span>,

    <span class="hljs-attr">"packages"</span>: [

        <span class="hljs-string">"packages/*"</span>

    ],

    <span class="hljs-attr">"npmClient"</span>: <span class="hljs-string">"yarn"</span>,

    <span class="hljs-attr">"useWorkspaces"</span>: <span class="hljs-literal">true</span>,

    <span class="hljs-attr">"command"</span>: &#123;

        <span class="hljs-attr">"publish"</span>: &#123;

            <span class="hljs-attr">"allowBranch"</span>: <span class="hljs-string">"master-next"</span>

        &#125;

    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>version</code>字段是用来定义lerna项目的版本号，如果此字段声明了版本号，则内部的所有子项目都会按此版本号进行发布。但是可以选择通过不填版本号，如上述配置一样填写<code>independent</code>，来进行另一种发布模式，在这种发布模式下每个子项目维护自己的版本号。</p>
<p><code>packages</code>字段则是用于声明作用目录，只有在数组内的子项目才会被lerna检索到。</p>
<p><code>npmClient</code>字段用于声明lerna执行指令时使用的包管理工具，默认是<code>npm</code>。配置里声明的是<code>yarn</code>，所以可以开启<code>workspaces</code>模式。workspaces是yarn的一大特色，使用了workspaces之后绝大多数的依赖包都被提升到了根目录下的node_modules之内，各个子项目的node_modules里面不会重复存在依赖。</p>
<p><code>command</code>字段则是对lerna指令内置的参数进行改动。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flerna%2Flerna%23lernajson" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/lerna/lerna#lernajson" ref="nofollow noopener noreferrer">具体用法</a></p>
<p>接下来，笔者通过一次日历组件的打包发布全流程，给大家直观的展示接入lerna之后的玩法。</p>
<blockquote>
<p>lerna ls</p>
<p>获取本地项目内子项目列表</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8a48605c1674f8283ba1b1678368b5f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>lerna bootstrap</p>
<p>安装作用目录下全项目的依赖</p>
</blockquote>
<blockquote>
<p>lerna changed or lerna diff</p>
<p>用于确认本次修改涉及到的范围，lerna会将有改动的子项目都列出来，方便我们及时回顾改动</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2989ac4b9f2043998eb715180f3107a8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>lerna run (any script)</p>
<p>在所有子项目依次执行某条指令，图中展示的是build指令，等同于在每个子项目中进行了yarn build</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f9fcf109835416c9c6bb3de86f52db6~tplv-k3u1fbpfcp-watermark.image" alt="WX20210811-112000@2x.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>lerna publish</p>
<p>将本次改动的子项目批量进行npm发布，如下图所示，在输入指令之后可以为每个项目指定想要发布的版本</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c70ec8b5413848e3b7cd80684370fb08~tplv-k3u1fbpfcp-watermark.image" alt="WX20210811-112236@2x.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2d8c7a5dedb42cda40bb65537ab2b5d~tplv-k3u1fbpfcp-watermark.image" alt="WX20210811-112254@2x.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2be216f970b847f2829690c4cf682e2b~tplv-k3u1fbpfcp-watermark.image" alt="WX20210811-112329@2x.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>lerna clean</p>
<p>后续迭代时如果想重新安装各项目依赖，可以先执行clean指令，它会将项目底下所有node_modules都清理干净</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c631a8a26ee44979a89865bec56053c3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">闲聊</h2>
<p>断断续续搞了2年的日历组件，总算有了大概雏形，每个框架都有开箱即用的npm包：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2F%40mykurisu%2Fcalendar-component-vue" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/@mykurisu/calendar-component-vue" ref="nofollow noopener noreferrer">@mykurisu/calendar-component-vue</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2F%40mykurisu%2Fcalendar-component-miniapp" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/@mykurisu/calendar-component-miniapp" ref="nofollow noopener noreferrer">@mykurisu/calendar-component-miniapp</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2F%40mykurisu%2Fcalendar-component-react" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/@mykurisu/calendar-component-react" ref="nofollow noopener noreferrer">@mykurisu/calendar-component-react</a></p>
<p>如果大家有需要的话可以直接install，有任何问题都可以到<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmykurisu%2Fcalendar" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/mykurisu/calendar" ref="nofollow noopener noreferrer">@mykurisu/calendar</a>中进行反馈。</p>
<p>如果是关于样式上的问题，我建议fork一下项目，直接修改core中的样式，修改完之后改一下package.json里面的配置，甚至可以发布成自己的私有包。另外，如果有时间的话我也会更新多个日历皮肤，争取做到真正的开箱即用。</p>
<p>最后，如果本项目对大家有帮助麻烦帮忙点点<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmykurisu%2Fcalendar" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/mykurisu/calendar" ref="nofollow noopener noreferrer">@mykurisu/calendar</a>的star，后续的更新也会及时推送给大家。</p></div>  
</div>
            