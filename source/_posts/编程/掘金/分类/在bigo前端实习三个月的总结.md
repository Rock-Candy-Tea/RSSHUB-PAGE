
---
title: '在bigo前端实习三个月的总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0234702e819c4f1c94fce6869e0d88c6~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 27 Mar 2021 00:20:52 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0234702e819c4f1c94fce6869e0d88c6~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt="file" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0234702e819c4f1c94fce6869e0d88c6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>本文首发于：<a href="https://github.com/bigo-frontend/blog/" target="_blank" rel="nofollow noopener noreferrer">github.com/bigo-fronte…</a> 欢迎关注、转载。</p>
<h2 data-id="heading-0">一、整体认知</h2>
<h3 data-id="heading-1">1. 团队协作</h3>
<p>在家或者在学校的时候，一直都是自己独立地开发项目，前后端都是自己一个人梭哈，怎么写，任凭自己主宰，在这种独自一人开发的模式中，对于团队协作模式可谓是一无所知。
后来，实习期间，经过几次版本的迭代之后，对于团队协作开发模式已经有了整体上的认知。例如一个项目的需求周期是怎样的：</p>
<ol>
<li><strong>需求评审</strong></li>
<li><strong>需求进入排期表</strong></li>
<li><strong>进入开发</strong></li>
<li><strong>前后端自测联调</strong></li>
<li><strong>自测无误后发起提测</strong></li>
<li><strong>测试提bug（最好没有bug）</strong></li>
<li><strong>要是有bug就修复</strong></li>
<li><strong>发布上线</strong></li>
</ol>
<p>在这些过程中，前端主要发挥什么作用，也有了大致上的了解。</p>
<h3 data-id="heading-2">2. 工程化的理解</h3>
<p>在实习之前，我对于工程化的概念比较模糊，更多的是局限于 <strong>组件化</strong>，<strong>模块化</strong> 等。虽然之前平时逛有一些技术博客网站的时候，会看到一些类似 《<strong>xx走进工程化xx</strong>》《<strong>xx自动化xx</strong>》，我也迫不及待地点进去了，但对于我来说，确实只是玄学，于是我会马上关闭，然后深呼吸，接着，选择《js的基本类型》《css 选择器的顺序》等文章 津津有味地读起来。</p>
<p>实习期间，进过几次发版之后，了解到，原来上线，是不需要手动把资源上传到服务器的。用名为<strong>jenkins</strong> 的持续集成／持续发布的工具实现起来要方便许多。</p>
<p>慢慢的刷新了我对工程化的认知，<strong>工程化远不止组件与模块</strong>，原来它还包括 <strong>规范化、 持续集成、自动化构建、自动化部署、自动化测试</strong>等等。</p>
<p>工程化是一个很大的话题，希望随着实践经验的积累，能够慢慢地掌握精髓，后面也需要找些书来看看。</p>
<h3 data-id="heading-3">3. Git操作</h3>
<p>除了写代码，我想我最大的一个难题就是git操作了</p>
<p>在实习前，我会的git命令是这样的</p>
<ul>
<li><code>git pull</code></li>
<li><code>git add</code></li>
<li><code>git commit</code></li>
<li><code>git push</code></li>
</ul>
<p>我的分支是这样的</p>
<ul>
<li><code>master</code></li>
</ul>
<p>在创建分支的过程中，踩了不少次坑，我终于摸出了一条正确的道路，比如 在分支的管理上，我的经历是这样的：</p>
<ul>
<li>
<p><strong>刚开始</strong>：<strong>一个项目对应一个文件一个分支</strong>(所有需求都在一个分支里完成)</p>
</li>
<li>
<p><strong>后来</strong>：<strong>一个需求对应一个文件一个分支</strong>（导致分支间的关系不明确）</p>
</li>
<li>
<p><strong>最后</strong>：<strong>同个文件夹，一个分支对应一个需求</strong>（目前来说，还没发现什么问题♪(^∇^*)）</p>
</li>
</ul>
<p><strong>除此之外</strong>，由于有时是另一个需求还没开发完，就要开发其他需求，所以是好几个分支在同时开发的，这时难就发生了意想不到的事情，例如下面我所遇到的：</p>
<h4 data-id="heading-4">更改已经被 push ，但是不是需要的</h4>
<p>在分支上开发的过程中，添加了一些错误的文件，或者错误的修改之后，把本地的修改给add,commit,并且push上去了，但是这些修改是不需要的。怎么回退呢？</p>
<ol>
<li>git本地回退到指定版本后，按以往的提交顺序进行提交时会报错</li>
<li>这是因为gitlab已经在你提交历史前面了，你无法把push过的再次push进行覆盖，这个时候加个参数–force就行</li>
<li>加完参数后发现gitlab不允许强行push到保护的分支上，解决方法是让项目的管理员暂时在gitlab上把你要提交的分支设置为不受保护的分支即可</li>
</ol>
<p>除此之外也了解到有<code>git revert</code>这个方法</p>
<h4 data-id="heading-5">正在发开当前分支，但需要切到其他分支</h4>
<p>开开心心地在新的分支上开发新的功能，这时候，产品经理说 其他分支有bug或者修改需求，需要赶紧处理下，这样的话，就需要切到目标分支了，那在当前的分支上所作的修改该怎么办呢？</p>
<p>我想到的是commit，但其实还有更好的方法</p>
<ol>
<li>使用<code>git stash push –m”message”</code> 保存当前的修改</li>
<li>切到目标分支修改bug，修改提交后切回原分支</li>
<li>使用<code>git stash pop</code> 还原</li>
</ol>
<p>这里需要注意的就是保存当前修改的时候，最好是添加上message，而不是简单的git stash，因为git stash 一旦多了之后，就会记不清是做了什么修改</p>
<h4 data-id="heading-6">在错误的分支开发了新功能，新功能还没有在本地进行commit（提交）</h4>
<ol>
<li>
<p>使用<code>git stash push –m”message”</code>保存当前的修改</p>
</li>
<li>
<p>切换到需要开发的分支</p>
</li>
<li>
<p>使用<code>git stash apply</code> 应用修改</p>
</li>
</ol>
<h4 data-id="heading-7">在错误的分支开发了新功能，新功能已经在本地提交了，但是还没有push到远程仓库</h4>
<ol>
<li><code>git log --oneline </code> 先获取本次commit的hash</li>
<li><code>git cherry-pick <commit hash></code> 切到目标分支后将本次commit的修改merge到目标分支</li>
<li><code>git reset <commit hash>  </code> 切回错误分支，回退到之前版本</li>
<li><code>git checkout -- </code>. 清空修改</li>
</ol>
<h2 data-id="heading-8">二、调试技巧</h2>
<h3 data-id="heading-9">1. console.table展示数据</h3>
<p>在以往打印某个变量，基本都是使用console.log,但是其实还有更好的方法。</p>
<p>在控制台上展示数组或对象，使用console.table比console.log更加直观明了。</p>
<pre><code class="copyable">console.table([
  &#123;name:"Sunny",age:18,country:'China',job:'engineer'&#125;,
  &#123;name:"Luffy",age:16,country:'Japan',job:'Pirate'&#125;,
  &#123;name:"Kin",age:36,country:'Italy',job:'doctor'&#125;,
])
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c047c72f596249519996625e4439caf8~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>当然，有时候，你可能不想输出那么多列，比如，你只想输出name和job,那么你只需要在后面加个依赖数组，表明要输出哪些字段</p>
<pre><code class="copyable">console.table([
  &#123;name:"Sunny",age:18,country:'China',job:'engineer'&#125;,
  &#123;name:"Luffy",age:16,country:'Japan',job:'Pirate'&#125;,
  &#123;name:"Kin",age:36,country:'Italy',job:'doctor'&#125;,
],['name','job'])
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ce023fd7d514044891f5af27c224c00~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>实际上，除了console.table。还有其他的方法：</p>
<ul>
<li><strong>console.info</strong> ：与console.log 的作用是几乎完全一样的，也是在控制台中打印信息，只不过打印时的样式可能与 console.log 略有区别</li>
<li><strong>console.error</strong>：同样和console.log的作用几乎一样，不过会将打印的内容通过显目的红色标注出来并前面带一个 ×</li>
<li><strong>console.warn</strong>：道理同上，会通过黄色感叹号来高亮打印信息。</li>
<li><strong>console.time 和 console.timeEnd</strong>：两个方法是结合在一起使用的，他们接受一个相同的参数，输出两句表达式中间的代码的执行时间。</li>
<li><strong>console.count</strong>：会打印当前的打印内容，并在后面跟上该内容的打印次数。</li>
</ul>
<p>说了这么多，除了table，其实更多还是使用debugger！</p>
<h3 data-id="heading-10">2. copy复制数据</h3>
<p>使用copy方法 可以复制控制台 输出的值 到粘贴板，比手动复制要方便一些
需要注意的是，只能在谷歌浏览器上哦</p>
<h3 data-id="heading-11">3. 滚动元素到视图</h3>
<p>在调试DOM元素的时候，我们已经聚焦到相关的DOM结构上了，但是对应的元素并没有在可视窗口上展示，那么我们可以将其快速滚动到可视窗口。</p>
<p><strong>控制面板 => Elements => 右击选中的DOM节点 => Scroll into view</strong></p>
<h3 data-id="heading-12">4. 捕获快照</h3>
<p>有时候，需要把实现好的页面交付给产品看一下，这时需要截图，但是如果网页太长，就很不方便了，难道要截很多张吗？当然，可以下载长截图的工具，可以这样，但是没必要，其实有一个长截图的命令：</p>
<p><strong>控制面板 => 审查元素 => command + shift + p => capture full size screenshot</strong></p>
<p>这时你就能看到一张长截图啦</p>
<h3 data-id="heading-13">5. 捕获局部快照</h3>
<p>当然，有时候，并不想截取那么长，只想截取某个部分，其实也是有对应的命令的</p>
<p><strong>控制面板 => 审查元素 => command + shift + p => capture node screens</strong></p>
<h2 data-id="heading-14">三、代码风格</h2>
<p>由于实习过程中，是在一个现在的项目上进行迭代，添加新的功能，所以可以从前辈们的代码中学习到一些比较好的代码风格，以下就列出来一些印象比较深刻的。</p>
<h3 data-id="heading-15">1. 注重命名</h3>
<p>命名一个事件，总是有些困难，因为它很重要，我们希望可以直截了当地从方法名就看出方法的作用。比如将两个数组合并成一个新的数组，并且返回的数组不存在重复的值。</p>
<p>我们会怎样命名，才能体现出它的功能呢？</p>
<p>也许可以这样：</p>
<pre><code class="copyable">mergeListsIntoUniqueList(arr1,arr2)&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是，实际上，一个方法只做一件事是最好的，这样耦合性会低一些，方法的复用性也就好一点</p>
<p>我们把这两个方法拆成两个方法，一个负责合并，一个负责去重</p>
<pre><code class="copyable">mergeList(arr1,arr2)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">unique(arr)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">2. IF语句简化</h3>
<p>看一下下面的代码：</p>
<pre><code class="hljs language-js copyable" lang="js">多个<span class="hljs-keyword">if</span>嵌套

<span class="hljs-keyword">if</span>(name === <span class="hljs-string">"sunny"</span> || name === <span class="hljs-string">"Luffy"</span> || === <span class="hljs-string">"Kin"</span>)&#123;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有个比较优美的写法，就是把这些值写进一个数组来，然后判断name是否在数组里即可</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> nameArr = [<span class="hljs-string">"sunny"</span>,<span class="hljs-string">"Luffy"</span>,<span class="hljs-string">"Kin"</span>]
<span class="hljs-keyword">if</span>(nameArr.includes(name))&#123;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">3. && 代替 if</h3>
<p>看一下下面的代码：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hello</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"hi"</span>)
  &#125;
  <span class="hljs-keyword">let</span> enableSpeak = <span class="hljs-literal">false</span>
  <span class="hljs-keyword">if</span>( enableSpeak)&#123;
    hello()
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实有个更加优美的写法</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hello</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"hi"</span>)
  &#125;
  <span class="hljs-keyword">let</span> enableSpeak = <span class="hljs-literal">false</span>
 
  enableSpeak && hello()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">4. 多个if嵌套</h3>
<p>当我们在接收后端返回来的数据的时候，接受到的是一个多层嵌套的对象，而我们要拿到深层处的一个对象属性的值，为了防止报错，我们可能需要利用多层if嵌套，如下代码所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span>(result.data)&#123;
  <span class="hljs-keyword">if</span>(result.data.obj)&#123;
    <span class="hljs-keyword">if</span>(result.list.obj.name)&#123;
      <span class="hljs-keyword">if</span>(result.list.obj.name.firstname)&#123;

      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样写起来，始终是有些麻烦的。</p>
<p>有个可选链操作符( ?. )，它允许读取位于连接对象链深处的属性的值，而不必明确验证链中的每个引用是否有效</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span>(result.data.obj.name.firstname)&#123;
 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">5. 尽早返回</h3>
<p>有下面的代碼：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleEvent</span>(<span class="hljs-params">event</span>)</span>&#123;
  <span class="hljs-keyword">if</span>(event)&#123;
    <span class="hljs-comment">//...</span>
    <span class="hljs-keyword">if</span>(event.target)&#123;
      <span class="hljs-comment">// do some thing real</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>尽早返回使得我们的代码更加易读</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleEvent</span>(<span class="hljs-params">event</span>)</span>&#123;
  <span class="hljs-keyword">if</span>(!event || !event.target)&#123;
   <span class="hljs-keyword">return</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">6. 对象参数</h3>
<p>有下面所示代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createObj</span>(<span class="hljs-params">name,sex,age,hobby,job,address</span>)</span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当函数的参数比较多时，我们可以将同一类的参数使用对象进行合并，然后将合并后的对象作为参数传入，这样在调用该函数时能够很清楚地理解每个参数的含义,也不用去记住每个参数的位置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createObj</span>(<span class="hljs-params">&#123;name,sex,age,hobby,job,address&#125;</span>)</span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">四、新技术</h2>
<p>在实习前，由于专攻vue，对于react属于零基础，由于组里的项目是react，所以就开始走上react的踩坑之路</p>
<p>在写react的时候，会出现一个报错，因此就会引发一些思考</p>
<h3 data-id="heading-22">1. 为什么要引入React</h3>
<p>在写 React 的时候，你可能会写类似这样的代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">A</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>前端sunny<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要是不写</p>
<pre><code class="copyable">import React from 'react'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就会报错，很奇怪，下面代码中明明没有使用到react的方法或属性，为什么一定要引入react呢？</p>
<p>后来查资料原来是 babel 会把jsx代码转化成</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">A</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">return</span> React.createElement(<span class="hljs-string">'h1'</span>,<span class="hljs-literal">null</span>,<span class="hljs-string">"前端sunny"</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">2. 为什么要引入super(),能不能不调用？</h3>
<p>JavaScript 对this使用的限制，是有原因的。假设有如下的继承：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.name = name;
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Geek</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.sayHello;
    <span class="hljs-built_in">super</span>(name);
  &#125;
  <span class="hljs-function"><span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>)</span> &#123;
    alert(<span class="hljs-string">'Good morning xdm!'</span>);
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果 JavaScript 允许在调用super之前使用 this,一个月之后，我们需要修改sayHello方法,方法中使用了 name 属性：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>)</span> &#123;
    alert(<span class="hljs-string">'Good morning xdm! I am '</span>+ <span class="hljs-built_in">this</span>.name);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就会出现 name 为 undefined的情况了，是不是细思极恐！</p>
<h3 data-id="heading-24">3. 为什么调用方法要 bind this</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Geek</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Person</span> </span>&#123;
 
  <span class="hljs-function"><span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>)</span> &#123;
    alert(<span class="hljs-string">'Good morning xdm!'</span>);
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.handleClick&#125;</span>></span>Click<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>会发现 this是 undefined，第一次遇到这个问题，始终会觉得奇怪，因为在以前写vue的时候，是没啥问题的</p>
<p><strong>vue代码:</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><button @click=<span class="hljs-string">"handleClick"</span>>Click</button>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者</p>
<pre><code class="hljs language-js copyable" lang="js"><button @click=<span class="hljs-string">"this.handleClick"</span>>Click</button>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之所以react和vue事件的使用方式有所差别，原因还是内部的实现机制的不同</p>
<p>react将事件通过addEventListener统一注册到 document上，然后会有一个事件池存储了所有的事件，当事件触发的时候，通过dispatchEvent进行事件分发，可以简单的理解为，最终this.handleClick会做为一个回调函数调用</p>
<p>作为回调函数调用通常会出现this丢失的情况，就像下面的代码，最常见不过：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">delaySayHello</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">let</span> _this = <span class="hljs-built_in">this</span>;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">// 使用_this</span>
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那有哪些方法来处理这个this呢？</p>
<h4 data-id="heading-25">1. 直接bind this</h4>
<p>写起来顺手，一气呵成。性能不太好，每次 render 都会进行 bind，而且如果有两个元素的事件处理函数式同一个，也还是要进行 bind。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Geek</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Person</span> </span>&#123;
 
  <span class="hljs-function"><span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>)</span> &#123;
    alert(<span class="hljs-string">'Good morning xdm!'</span>);
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.sayHello.bind(this)&#125;</span>></span>Click<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-26">2.constructor里手动bind</h4>
<p>因为构造函数只执行一次，那么只会 bind 一次，如果有多个元素都需要调用这个函数，也不需要重复 bind。</p>
<p>没有明显缺点，可能就是代码多了？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Geek</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span>&#123;
    <span class="hljs-built_in">super</span>(props)
    <span class="hljs-built_in">this</span>.sayHello = <span class="hljs-built_in">this</span>.sayHello.bind(<span class="hljs-built_in">this</span>)
  &#125;
  <span class="hljs-function"><span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>)</span> &#123;
    alert(<span class="hljs-string">'Good morning xdm!'</span>);
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.sayHello.bind(this)&#125;</span>></span>Click<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-27">3.使用箭头函数</h4>
<p>顺手，好看。每次 render 都会重复创建函数，性能会差一点。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Geek</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">sayHello</span>(<span class="hljs-params"></span>)</span> &#123;
    alert(<span class="hljs-string">'Good morning xdm!'</span>);
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;(e)</span>=></span>this.sayHello(e)&#125;>Click<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-28">4.public class field</h4>
<p>顺手，好看。处于试验阶段，如果不愿冒险，最好是在构造函数中绑定 this</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Geek</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Person</span> </span>&#123;
  sayHello = <span class="hljs-function">() =></span> &#123;
    alert(<span class="hljs-string">'Good morning xdm!'</span>);
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;&#125;</span>></span>Click<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">4. 手写简单的react</h3>
<p>为了更好地熟悉react的实现原理，看一些教学视频和资料，自己尝试着写了一个简单的react</p>
<p><a href="https://juejin.cn/post/6898292945867571207" target="_blank">手写简单的react核心原理</a> :<a href="https://juejin.cn/post/6898292945867571207" target="_blank">juejin.cn/post/689829…</a></p>
<h3 data-id="heading-30">5. React Hook 的学习</h3>
<p>由于在项目的迭代中，新增的组件尽量是需要使用hooks来实现的，所以， 对react hook的学习也是必不可少的。</p>
<p>其中，学到了例如<code>useMemo</code>，<code>useCallback</code>等性能优化方法。同样，为了更好地使用，也通过看了些视频和资料，自己尝试着写了hooks中 常用的 hook的实现原理。</p>
<p><a href="https://juejin.cn/post/6890349061019271182" target="_blank">手写React Hook核心原理</a></p>
<h2 data-id="heading-31">结尾</h2>
<p>学无止境，发现还有很多东西需要去学习，例如react fiber，react-saga，next.js,react 360等，在接下来的日子里，也需要努力学习啊！</p>
<p>欢迎大家留言讨论，祝工作顺利、生活愉快！</p>
<p>我是bigo前端，下期见。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            