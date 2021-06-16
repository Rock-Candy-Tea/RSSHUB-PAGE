
---
title: 'Node 系列 - 004 - Inquirer.js'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ff26d26890f4c3ea260c97d70746894~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 15:57:08 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ff26d26890f4c3ea260c97d70746894~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>——————————☆☆☆——————————</p>
<p>Node 系列相应地址：</p>
<ul>
<li>代码仓库：<a href="https://github.com/LiangJunrong/all-for-one" target="_blank" rel="nofollow noopener noreferrer">github.com/LiangJunron…</a></li>
<li>文章仓库：<a href="https://github.com/LiangJunrong/document-library/tree/master/%E7%B3%BB%E5%88%97-%E5%89%8D%E7%AB%AF%E8%B5%84%E6%96%99/Node" target="_blank" rel="nofollow noopener noreferrer">github.com/LiangJunron…</a></li>
</ul>
<p>——————————☆☆☆——————————</p>

<h2 data-id="heading-0"><a name="user-content-chapter-one" id="user-content-chapter-one" href="https://juejin.cn/post/undefined"></a>一 目录</h2>
<p><strong>不折腾的前端，和咸鱼有什么区别</strong></p>












































<table><thead><tr><th>目录</th></tr></thead><tbody><tr><td><a href="https://juejin.cn/post/6974171023025389576#chapter-one">一 目录</a></td></tr><tr><td><a name="user-content-catalog-chapter-two" id="user-content-catalog-chapter-two" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6974171023025389576#chapter-two">二 前言</a></td></tr><tr><td><a name="user-content-catalog-chapter-three" id="user-content-catalog-chapter-three" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6974171023025389576#chapter-three">三 集成 Inquirer.js</a></td></tr><tr><td><a name="user-content-catalog-chapter-four" id="user-content-catalog-chapter-four" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6974171023025389576#chapter-four">四 Inquirer.js 使用技巧</a></td></tr><tr><td> <a href="https://juejin.cn/post/6974171023025389576#chapter-four-one">4.1 输入框</a></td></tr><tr><td> <a href="https://juejin.cn/post/6974171023025389576#chapter-four-two">4.2 单选项</a></td></tr><tr><td> <a href="https://juejin.cn/post/6974171023025389576#chapter-four-three">4.3 多选项</a></td></tr><tr><td> <a href="https://juejin.cn/post/6974171023025389576#chapter-four-four">4.4 确认框</a></td></tr><tr><td> <a href="https://juejin.cn/post/6974171023025389576#chapter-four-five">4.5 校验输入</a></td></tr><tr><td><a name="user-content-catalog-chapter-five" id="user-content-catalog-chapter-five" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6974171023025389576#chapter-five">五 动态提问</a></td></tr><tr><td><a name="user-content-catalog-chapter-six" id="user-content-catalog-chapter-six" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6974171023025389576#chapter-six">六 参考文献</a></td></tr><tr><td></td></tr></tbody></table>
<h2 data-id="heading-1"><a name="user-content-chapter-two" id="user-content-chapter-two" href="https://juejin.cn/post/undefined"></a>二 前言</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6974171023025389576#chapter-one">返回目录</a></p>
</blockquote>
<p>经过前面 TypeScript 环境的搭建和 <code>commander.js</code> 的配合，我们现在可以在 <code>.ts</code> 文件中编写对应指令，然后通过 <code>npm run xxx</code> 来运行项目了，但是这种方式有个 Bug：</p>
<ul>
<li>当指令过多的时候，我们压根记不住那么多的指令！</li>
</ul>
<p>所以，就需要一个智能提示，将指令简化并可视化。</p>
<h2 data-id="heading-2"><a name="user-content-chapter-three" id="user-content-chapter-three" href="https://juejin.cn/post/undefined"></a>三 集成 Inquirer.js</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6974171023025389576#chapter-one">返回目录</a></p>
</blockquote>
<p>这边 <strong>jsliang</strong> 想的一个法子就是通过终端那种问答形式的来解决这个问题（后续可能安排页面或者 Chrome 插件等）</p>
<p>那么，废话少说，Here we go~</p>
<p><strong>首先</strong>，安装必须的包：</p>
<ul>
<li>安装 <code>Inquirer.js</code>：<code>npm i inquirer</code></li>
<li>安装 <code>@types/inquirer</code>（可选，TS 必装）：<code>npm i @types/inquirer -D</code></li>
</ul>
<p><strong>然后</strong>。我们就可以开始耍起来了，接入前面的 TypeScript 和 <code>commander.js</code>，拿起 <code>index.ts</code> 和 <code>package.json</code> 就是一顿修改：</p>
<blockquote>
<p>src/index.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> program <span class="hljs-keyword">from</span> <span class="hljs-string">'commander'</span>;
<span class="hljs-keyword">import</span> inquirer <span class="hljs-keyword">from</span> <span class="hljs-string">'inquirer'</span>;
<span class="hljs-keyword">import</span> &#123; sortCatalog &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./sortCatalog'</span>;

program
  .version(<span class="hljs-string">'0.0.1'</span>)
  .description(<span class="hljs-string">'工具库'</span>)

program
  .command(<span class="hljs-string">'jsliang'</span>)
  .description(<span class="hljs-string">'jsliang 帮助指令'</span>)
  .action(<span class="hljs-function">() =></span> &#123;
    inquirer
    .prompt([
      &#123; 
        <span class="hljs-attr">type</span>: <span class="hljs-string">'rawlist'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'question1'</span>,
        <span class="hljs-attr">message</span>: <span class="hljs-string">'请问需要什么服务？'</span>,
        <span class="hljs-attr">choices</span>: [<span class="hljs-string">'公共服务'</span>, <span class="hljs-string">'其他'</span>]
      &#125;,
    ])
    .then(<span class="hljs-function">(<span class="hljs-params">answers</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (answers.question1 === <span class="hljs-string">'公共服务'</span>) &#123;
        inquirer.prompt([
          &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">'rawlist'</span>,
            <span class="hljs-attr">name</span>: <span class="hljs-string">'question'</span>,
            <span class="hljs-attr">message</span>: <span class="hljs-string">'当前公共服务有：'</span>,
            <span class="hljs-attr">choices</span>: [<span class="hljs-string">'文件排序'</span>]
          &#125;
        ]).then(<span class="hljs-function">(<span class="hljs-params">answers</span>) =></span> &#123;
          <span class="hljs-keyword">if</span> (answers.question === <span class="hljs-string">'文件排序'</span>) &#123;
            inquirer.prompt([
              &#123;
                <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
                <span class="hljs-attr">name</span>: <span class="hljs-string">'question'</span>,
                <span class="hljs-attr">message</span>: <span class="hljs-string">'需要排序的文件夹为？（绝对路径）'</span>,
                <span class="hljs-attr">default</span>: <span class="hljs-string">'D:/xx'</span>,
              &#125;
            ]).then(<span class="hljs-keyword">async</span> (answers) => &#123;
              <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> sortCatalog(answers.question);
              <span class="hljs-keyword">if</span> (result) &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'排序成功！'</span>);
              &#125;
            &#125;).catch(<span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
              <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'出错啦！'</span>, error);
            &#125;);
          &#125;
        &#125;).catch(<span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
          <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'出错啦！'</span>, error);
        &#125;);
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (answers === <span class="hljs-string">'其他'</span>) &#123;
        <span class="hljs-comment">// 做其他事情</span>
      &#125;
    &#125;).catch(<span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'出错啦！'</span>, error);
    &#125;);
  &#125;);

program.parse(process.argv);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意这里 <code>sort</code> 改成 <code>jsliang</code> 了（人不要脸天下无敌）。</p>
<blockquote>
<p>package.json</p>
</blockquote>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"jsliang"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">"Fe-util, Node 工具库"</span>,
  <span class="hljs-attr">"main"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"jsliang"</span>: <span class="hljs-string">"ts-node ./src/index.ts jsliang"</span>
  &#125;,
  <span class="hljs-attr">"keywords"</span>: [
    <span class="hljs-string">"jsliang"</span>,
    <span class="hljs-string">"Node 工具库"</span>,
    <span class="hljs-string">"Node"</span>
  ],
  <span class="hljs-attr">"author"</span>: <span class="hljs-string">"jsliang"</span>,
  <span class="hljs-attr">"license"</span>: <span class="hljs-string">"ISC"</span>,
  <span class="hljs-attr">"devDependencies"</span>: &#123;
    <span class="hljs-attr">"@types/inquirer"</span>: <span class="hljs-string">"^7.3.1"</span>,
    <span class="hljs-attr">"@types/node"</span>: <span class="hljs-string">"^15.12.2"</span>,
    <span class="hljs-attr">"@typescript-eslint/eslint-plugin"</span>: <span class="hljs-string">"^4.26.1"</span>,
    <span class="hljs-attr">"@typescript-eslint/parser"</span>: <span class="hljs-string">"^4.26.1"</span>,
    <span class="hljs-attr">"eslint"</span>: <span class="hljs-string">"^7.28.0"</span>,
    <span class="hljs-attr">"ts-node"</span>: <span class="hljs-string">"^10.0.0"</span>,
    <span class="hljs-attr">"typescript"</span>: <span class="hljs-string">"^4.3.2"</span>
  &#125;,
  <span class="hljs-attr">"dependencies"</span>: &#123;
    <span class="hljs-attr">"commander"</span>: <span class="hljs-string">"^7.2.0"</span>,
    <span class="hljs-attr">"inquirer"</span>: <span class="hljs-string">"^8.1.0"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>于是就有了效果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ff26d26890f4c3ea260c97d70746894~tplv-k3u1fbpfcp-watermark.image" alt="Inquirer-01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一样的丝滑好用，还可以控制文件夹路径了~</p>
<p>但是！小伙伴们看到上面代码，是不是有种想吐的感觉。</p>
<ul>
<li>问题 1：呀，这是啥，这些代码你写了什么功能？</li>
<li>问题 2：太恶心了吧，居然不支持 <code>async/await</code>？</li>
</ul>
<p>OK，一一解决问题，咱们先讲解下 <code>Inquirer.js</code> 里面的一些操作。</p>
<h2 data-id="heading-3"><a name="user-content-chapter-four" id="user-content-chapter-four" href="https://juejin.cn/post/undefined"></a>四 Inquirer.js 使用技巧</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6974171023025389576#chapter-one">返回目录</a></p>
</blockquote>
<p>在上面的代码中，通过 <code>.prompt(Array<Object>)</code> 可以传递多个问题信息，然后通过回调获取答案，举例一个输入框：</p>
<pre><code class="hljs language-js copyable" lang="js">inquirer.prompt([
  &#123; 
    <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'question'</span>,
    <span class="hljs-attr">message</span>: <span class="hljs-string">'请问需要什么服务？'</span>,
  &#125;
]).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'成功！'</span>, res);
&#125;).catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'报错！'</span>, err);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中 <code>Object</code> 里面可以塞：</p>
<ul>
<li><code>type</code>：【String】提示的类型，默认 <code>input</code>，包含 <code>input</code>、<code>number</code>、<code>confirm</code>、<code>list</code>、<code>rawlist</code>、<code>expand</code>、<code>checkbox</code>、<code>password</code>、<code>editor</code></li>
<li><code>name</code>：【String】存储当前问题回答的变量</li>
<li><code>message</code>：【String|Function】提问的问题内容</li>
<li><code>default</code>：【String|Number|Boolean|Array|Function】默认值</li>
<li><code>choices</code>：【Array|Function】列表选项</li>
<li><code>validate</code>：【Function】验证方法，校验输入值是否可行，有效返回 <code>true</code>，否则返回字符串表示错误信息（返回 <code>false</code> 则为默认的错误信息）</li>
<li><code>filter</code>：【Function】对答案进行过滤处理，返回处理后的值</li>
<li><code>transformer</code>：【Function】操作答案的显示效果</li>
<li><code>when</code>：【Function|Boolean】接受答案，根据前面的内容判断是否需要展示该问题</li>
<li><code>pageSize</code>：【Number】在 <code>list</code>、<code>rawlist</code>、<code>expand</code>、<code>checkbox</code> 这种多选项中，进行分页拆分</li>
<li><code>prefix</code>：【String】修改默认前缀</li>
<li><code>suffix</code>：【String】修改默认后缀</li>
<li><code>askAnswered</code>：【Boolean】已有答案是否强制提问</li>
<li><code>loop</code>：【Boolean】<code>list</code> 是否能循环滚动选择，默认 <code>true</code></li>
</ul>
<p>相信你也看不懂，咱们将一些可能用到的写一写用例吧。</p>
<blockquote>
<p>后续代码为简写，全写大概为下面代码所示，后面就不哆嗦了</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> program <span class="hljs-keyword">from</span> <span class="hljs-string">'commander'</span>;
<span class="hljs-keyword">import</span> inquirer <span class="hljs-keyword">from</span> <span class="hljs-string">'inquirer'</span>;

program
  .version(<span class="hljs-string">'0.0.1'</span>)
  .description(<span class="hljs-string">'工具库'</span>)

program
  .command(<span class="hljs-string">'jsliang'</span>)
  .description(<span class="hljs-string">'jsliang 帮助指令'</span>)
  .action(<span class="hljs-function">() =></span> &#123;
    inquirer
    .prompt([
      &#123; 
        <span class="hljs-attr">type</span>: <span class="hljs-string">'rawlist'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'question'</span>,
        <span class="hljs-attr">message</span>: <span class="hljs-string">'请问需要什么服务？'</span>,
        <span class="hljs-attr">choices</span>: [<span class="hljs-string">'公共服务'</span>, <span class="hljs-string">'其他'</span>]
      &#125;,
    ])
    .then(<span class="hljs-function">(<span class="hljs-params">answers</span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'答案：'</span>, answers);
    &#125;).catch(<span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'出错啦！'</span>, error);
    &#125;);
  &#125;);

program.parse(process.argv);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：<br>
① 下面这些举例，你也可以在 <code>Inquires.js</code> 中找到，但是 <strong>jsliang</strong> 希望搬运到自己这篇文章中方便后续检索。<br>
② 如果有评论没看到这个注释就吐槽 <strong>jsliang</strong> 抄写人家 README，那 <strong>jsliang</strong> 也无话可说，只是被吐槽了几次，稍微写点注释</p>
</blockquote>
<h3 data-id="heading-4"><a name="user-content-chapter-four-one" id="user-content-chapter-four-one" href="https://juejin.cn/post/undefined"></a>4.1 输入框</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6974171023025389576#chapter-one">返回目录</a></p>
</blockquote>
<p><strong>输入文本</strong>：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b872cfb6ce534263ae78d2189fd14819~tplv-k3u1fbpfcp-watermark.image" alt="Inquirer-02.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可配合参数：<code>type, name, message[, default, filter, validate, transformer]</code></p>
<pre><code class="hljs language-js copyable" lang="js">inquirer.prompt([
  &#123; 
    <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'question'</span>,
    <span class="hljs-attr">message</span>: <span class="hljs-string">'问题？'</span>,
    <span class="hljs-attr">default</span>: <span class="hljs-string">'liangjunrong'</span>,
  &#125;
]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>输入数字</strong>：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/362845dbc0194ca3852a569949fc49c4~tplv-k3u1fbpfcp-watermark.image" alt="Inquirer-03.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可配合参数：<code>type, name, message[, default, filter, validate, transformer]</code></p>
<pre><code class="hljs language-js copyable" lang="js">inquirer.prompt([
  &#123; 
    <span class="hljs-attr">type</span>: <span class="hljs-string">'number'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'question'</span>,
    <span class="hljs-attr">message</span>: <span class="hljs-string">'问题？'</span>,
    <span class="hljs-attr">default</span>: <span class="hljs-string">'1'</span>,
  &#125;
]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>输入密码</strong>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31c282450c7d478795a2d7ed306528a5~tplv-k3u1fbpfcp-watermark.image" alt="Inquirer-04.png" loading="lazy" referrerpolicy="no-referrer">
可配合参数：<code>type, name, message, mask,[, default, filter, validate]</code></p>
<pre><code class="hljs language-js copyable" lang="js">inquirer.prompt([
  &#123; 
    <span class="hljs-attr">type</span>: <span class="hljs-string">'password'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'question'</span>,
    <span class="hljs-attr">message</span>: <span class="hljs-string">'问题？'</span>,
  &#125;
]);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5"><a name="user-content-chapter-four-two" id="user-content-chapter-four-two" href="https://juejin.cn/post/undefined"></a>4.2 单选项</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6974171023025389576#chapter-one">返回目录</a></p>
</blockquote>
<p><strong>没下标的单选项</strong>：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/897f13b60a514bcfa848b9d0618b7fc8~tplv-k3u1fbpfcp-watermark.image" alt="Inquirer-05.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可配合参数：<code>type, name, message, choices[, default, filter, loop]</code></p>
<pre><code class="hljs language-js copyable" lang="js">inquirer.prompt([
  &#123; 
    <span class="hljs-attr">type</span>: <span class="hljs-string">'list'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'question'</span>,
    <span class="hljs-attr">message</span>: <span class="hljs-string">'问题？'</span>,
    <span class="hljs-attr">default</span>: <span class="hljs-string">'jsliang'</span>,
    <span class="hljs-attr">choices</span>: [<span class="hljs-string">'liangjunrong'</span>, <span class="hljs-string">'jsliang'</span>]
  &#125;
]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>添加分隔符</strong>：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5b25edd27bf4281b7fb751099cea5ec~tplv-k3u1fbpfcp-watermark.image" alt="Inquirer-06.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">inquirer.prompt([
  &#123; 
    <span class="hljs-attr">type</span>: <span class="hljs-string">'list'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'question'</span>,
    <span class="hljs-attr">message</span>: <span class="hljs-string">'问题？'</span>,
    <span class="hljs-attr">default</span>: <span class="hljs-string">'jsliang'</span>,
    <span class="hljs-attr">choices</span>: [
      <span class="hljs-string">'liangjunrong'</span>,
      <span class="hljs-keyword">new</span> inquirer.Separator(), <span class="hljs-comment">// 添加分隔符</span>
      <span class="hljs-string">'jsliang'</span>,
    ]
  &#125;
]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>有下标的单选项</strong>：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/539e8ca95c5b482cb1319c50731e7fba~tplv-k3u1fbpfcp-watermark.image" alt="Inquirer-07.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可配合参数：<code>type, name, message, choices[, default, filter, loop]</code></p>
<pre><code class="hljs language-js copyable" lang="js">inquirer.prompt([
  &#123; 
    <span class="hljs-attr">type</span>: <span class="hljs-string">'rawlist'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'question'</span>,
    <span class="hljs-attr">message</span>: <span class="hljs-string">'问题？'</span>,
    <span class="hljs-attr">default</span>: <span class="hljs-string">'jsliang'</span>,
    <span class="hljs-attr">choices</span>: [<span class="hljs-string">'liangjunrong'</span>, <span class="hljs-string">'jsliang'</span>]
  &#125;
]);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6"><a name="user-content-chapter-four-three" id="user-content-chapter-four-three" href="https://juejin.cn/post/undefined"></a>4.3 多选项</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6974171023025389576#chapter-one">返回目录</a></p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d81a0839c33e4e52b764e15677608558~tplv-k3u1fbpfcp-watermark.image" alt="Inquirer-08.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可配合参数：<code>type, name, message, choices[, filter, validate, default, loop]</code></p>
<pre><code class="hljs language-js copyable" lang="js">inquirer.prompt([
  &#123; 
    <span class="hljs-attr">type</span>: <span class="hljs-string">'checkbox'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'question'</span>,
    <span class="hljs-attr">message</span>: <span class="hljs-string">'问题？'</span>,
    <span class="hljs-attr">choices</span>: [<span class="hljs-string">'liangjunrong'</span>, <span class="hljs-string">'jsliang'</span>]
  &#125;
]);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7"><a name="user-content-chapter-four-four" id="user-content-chapter-four-four" href="https://juejin.cn/post/undefined"></a>4.4 确认框</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6974171023025389576#chapter-one">返回目录</a></p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b0b04f41cc842c1834e428e1db4c7fc~tplv-k3u1fbpfcp-watermark.image" alt="Inquirer-09.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可配合参数：<code>type, name, message, [default]</code></p>
<pre><code class="hljs language-js copyable" lang="js">inquirer.prompt([
  &#123; 
    <span class="hljs-attr">type</span>: <span class="hljs-string">'confirm'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'question'</span>,
    <span class="hljs-attr">message</span>: <span class="hljs-string">'问题?'</span>,
  &#125;
]);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8"><a name="user-content-chapter-four-five" id="user-content-chapter-four-five" href="https://juejin.cn/post/undefined"></a>4.5 校验输入</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6974171023025389576#chapter-one">返回目录</a></p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebfc94a5e9094ec68cbdd3360b65e110~tplv-k3u1fbpfcp-watermark.image" alt="Inquirer-10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">inquirer.prompt([
  &#123; 
    <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'phone'</span>,
    <span class="hljs-attr">message</span>: <span class="hljs-string">'请输入手机号'</span>,
    <span class="hljs-attr">validate</span>: <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (val.match(<span class="hljs-regexp">/\d&#123;11&#125;/g</span>)) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
      &#125;
      <span class="hljs-keyword">return</span> <span class="hljs-string">'请输入 11 位数字'</span>;
    &#125;,
  &#125;
]);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9"><a name="user-content-chapter-five" id="user-content-chapter-five" href="https://juejin.cn/post/undefined"></a>五 动态提问</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6974171023025389576#chapter-one">返回目录</a></p>
</blockquote>
<p>上面我们说了 2 个问题：</p>
<ul>
<li>问题 1：呀，这是啥，这些代码你写了什么功能？</li>
<li>问题 2：太恶心了吧，居然不支持 <code>async/await</code>？</li>
</ul>
<p>刚才已经将问题 1 解决了（就是这个 <code>Inquires.js</code> 功能支持），下面我们看看问题 2 怎么操作。</p>
<p>其实为了解决这个问题，我们需要按照 <code>Inquires.js</code> 中的推荐安装 <code>Rx.js</code>，<code>Rx.js</code> 参考文献：</p>
<ul>
<li><a href="https://github.com/ReactiveX/rxjs" target="_blank" rel="nofollow noopener noreferrer">GitHub：rxjs</a></li>
<li><a href="https://cn.rx.js.org/manual/overview.html" target="_blank" rel="nofollow noopener noreferrer">RxJS 中文文档</a></li>
</ul>
<p>开始安装：</p>
<ul>
<li>安装 <code>rxjs</code>：<code>npm i rxjs@5</code></li>
</ul>
<blockquote>
<p>当前版本为 <code>v7.1.0</code>，但是看了下 <code>Inquirer.js</code> 举例的是 <code>v5.x</code> 版本，找了一会找不到新版本的用法，只能出此下举</p>
</blockquote>
<blockquote>
<p>其次 <strong>jsliang</strong> 是真的懒，不想了解 <code>Rx.js</code> 做啥子的，我只希望项目能按照 <code>async/await</code> 方式跑起来</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> program <span class="hljs-keyword">from</span> <span class="hljs-string">'commander'</span>;
<span class="hljs-keyword">import</span> Rx <span class="hljs-keyword">from</span> <span class="hljs-string">'rxjs/Rx'</span>;
<span class="hljs-keyword">import</span> inquirer <span class="hljs-keyword">from</span> <span class="hljs-string">'inquirer'</span>;

<span class="hljs-keyword">const</span> prompts = <span class="hljs-keyword">new</span> Rx.Subject();

<span class="hljs-comment">// 无情的信息处理器</span>
inquirer.prompt(prompts).ui.process.subscribe(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'成功：'</span>, result);
&#125;, <span class="hljs-function">(<span class="hljs-params">error: unknown</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'失败'</span>, error);
&#125;, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'完成'</span>);
&#125;);

program
  .version(<span class="hljs-string">'0.0.1'</span>)
  .description(<span class="hljs-string">'工具库'</span>)

program
  .command(<span class="hljs-string">'jsliang'</span>)
  .description(<span class="hljs-string">'jsliang 帮助指令'</span>)
  .action(<span class="hljs-function">() =></span> &#123;
    prompts.next(&#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'confirm'</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">'question'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'问题?'</span>,
    &#125;);
    prompts.complete();
  &#125;);

program.parse(process.argv);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就完成了封装，更方便处理信息了。（可以想象后面会有一堆 <code>switch...case...</code> 判断）</p>
<p>但是，预想不到的是，在多个模块接入 <code>Inquire.js</code> 后，出问题了。</p>
<blockquote>
<p>多个模块示例</p>
</blockquote>
<pre><code class="copyable">+ src
  - index.ts
  + base
    - config.ts
  + common
    - inquirer.ts
  + jsliang
    - inquirer.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>暂不需要按照这个目录更改接口，以下一个目录为准</p>
</blockquote>
<blockquote>
<p>个人怀疑 <code>Rx.js</code> 是单实例缘故</p>
</blockquote>
<p>运行时报错提示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7384b23adbec42b2ba73da073c41ccb2~tplv-k3u1fbpfcp-watermark.image" alt="Inquirer-11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">npm ERR! code ELIFECYCLE
npm ERR! errno 1
npm ERR! jsliang@1.0.0 test: `ts-node ./src/index.ts test`
npm ERR! Exit status 1
npm ERR!
npm ERR! Failed at the jsliang@1.0.0 test script.
npm ERR! This is probably not a problem with npm. There is likely additional logging output above.

npm ERR! A complete log of this run can be found in:
npm ERR!     C:\Users\wps\AppData\Roaming\npm-cache\_logs\2021-06-08T11_46_58_005Z-debug.log
<span class="copy-code-btn">复制代码</span></code></pre>
<p>排查了老久，应该跟我不熟悉 RX.js 有关，所以就想着能不能更新一波：</p>
<blockquote>
<p>【准】按照这个目录更改文件夹/文件</p>
</blockquote>
<pre><code class="copyable">+ src —————————————————————— src 文件夹
  - index.ts ——————————————— 主入口
  + base ——————————————————— 基础文件夹，例如 config/math 等
    - config.ts ———————————— 常用配置项
    - inquirer.ts —————————— inquirer 总处理口，统一封装 async/await
    - interface.ts ————————— 暂时将所有通用的 interface.ts 放到这里
  + common ————————————————— 通用功能
    - index.ts ————————————— common 处理问题的入口
    - sortCatalog.ts —————— inquirer 调用具体的功能文件
  + jsliang ———————————————— 业务功能
    - xx.ts ———————————————— 业务功能文件
<span class="copy-code-btn">复制代码</span></code></pre>
<p>顺带给个目录图吧：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/216cdf558ee948f397c638e500f41a92~tplv-k3u1fbpfcp-watermark.image" alt="Inquirer-12.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>src/base/inquirer.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> myInquirer <span class="hljs-keyword">from</span> <span class="hljs-string">'inquirer'</span>;
<span class="hljs-keyword">import</span> Rx <span class="hljs-keyword">from</span> <span class="hljs-string">'rxjs/Rx'</span>;
<span class="hljs-keyword">import</span> &#123; Question &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./interface'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> inquirer = (questions: Question[], <span class="hljs-attr">answers</span>: any): <span class="hljs-function"><span class="hljs-params">void</span> =></span> &#123;
  <span class="hljs-keyword">const</span> prompts = <span class="hljs-keyword">new</span> Rx.Subject();

  <span class="hljs-comment">// 长度判断</span>
  <span class="hljs-keyword">if</span> (questions.length !== answers.length) &#123;
    <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'问题和答案长度不一致！'</span>);
  &#125;

  <span class="hljs-comment">// 问题列表</span>
  <span class="hljs-keyword">const</span> questionList = questions.map(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      prompts.next(<span class="hljs-built_in">Object</span>.assign(&#123;&#125;, item, &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-built_in">String</span>(index),
      &#125;));
    &#125;;
  &#125;);

  <span class="hljs-comment">// 问题处理器</span>
  myInquirer.prompt(prompts).ui.process.subscribe(<span class="hljs-keyword">async</span> (res) => &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'执行成功，输入信息为：'</span>, res);
    <span class="hljs-keyword">const</span> index = <span class="hljs-built_in">Number</span>(res.name);
    
    <span class="hljs-comment">// 回调函数：结果、问题列表、prompts（控制是否需要停止）</span>
    answers[index](res, questionList, prompts);

    <span class="hljs-comment">// 默认最后一个问题就自动终止</span>
    <span class="hljs-keyword">if</span> (index === answers.length - <span class="hljs-number">1</span>) &#123;
      prompts.complete(); <span class="hljs-comment">// 回调函数可以手动控制终止询问时机</span>
    &#125;
  &#125;, <span class="hljs-function">(<span class="hljs-params">error: unknown</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'执行失败，报错信息为：'</span>, error);
  &#125;, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// console.log('完成'); // 必定会执行的代码</span>
  &#125;);

  <span class="hljs-comment">// 执行第一个问题</span>
  questionList[<span class="hljs-number">0</span>]();
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>src/base/interface.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> interface Question &#123;
  <span class="hljs-attr">type</span>: string,
  name?: string,
  <span class="hljs-attr">message</span>: string,
  <span class="hljs-keyword">default</span>?: string,
  choices?: string[],
  validate?(): boolean,
&#125;

<span class="hljs-keyword">export</span> interface Result &#123;
  <span class="hljs-attr">name</span>: string,
  <span class="hljs-attr">answer</span>: string,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按照这样子设置后，就可以在其他地方愉快玩耍了：</p>
<blockquote>
<p>src/common/index.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; inquirer &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../base/inquirer'</span>;
<span class="hljs-keyword">import</span> &#123; Result &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../base/interface'</span>;
<span class="hljs-keyword">import</span> &#123; sortCatalog &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./sortCatalog'</span>;

<span class="hljs-keyword">const</span> common = (): <span class="hljs-function"><span class="hljs-params">void</span> =></span> &#123;
  <span class="hljs-comment">// 测试新特性</span>
  <span class="hljs-keyword">const</span> questionList = [
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'list'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'请问需要什么服务？'</span>,
      <span class="hljs-attr">choices</span>: [<span class="hljs-string">'公共服务'</span>, <span class="hljs-string">'其他'</span>]
    &#125;,
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'list'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'当前公共服务有：'</span>,
      <span class="hljs-attr">choices</span>: [<span class="hljs-string">'文件排序'</span>]
    &#125;,
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'需要排序的文件夹为？（绝对路径）'</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">'D:/xx'</span>,
    &#125;,
  ];

  <span class="hljs-keyword">const</span> answerList = [
    <span class="hljs-keyword">async</span> (result: Result, <span class="hljs-attr">questions</span>: any) => &#123;
      <span class="hljs-keyword">if</span> (result.answer === <span class="hljs-string">'公共服务'</span>) &#123;
        questions[<span class="hljs-number">1</span>]();
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (result.answer === <span class="hljs-string">'其他'</span>) &#123;
        <span class="hljs-comment">// 做其他事情</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'暂未开通该服务'</span>);
      &#125;
    &#125;,
    <span class="hljs-keyword">async</span> (result: Result, <span class="hljs-attr">questions</span>: any) => &#123;
      <span class="hljs-built_in">console</span>.log(result);
      <span class="hljs-keyword">if</span> (result.answer === <span class="hljs-string">'文件排序'</span>) &#123;
        questions[<span class="hljs-number">2</span>]();
      &#125;
    &#125;,
    <span class="hljs-keyword">async</span> (result: Result) => &#123;
      <span class="hljs-keyword">const</span> sortResult = <span class="hljs-keyword">await</span> sortCatalog(result.answer);
      <span class="hljs-keyword">if</span> (sortResult) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'排序成功！'</span>);
      &#125;
    &#125;,
  ];

  inquirer(questionList, answerList);
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> common;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>传递问题数组，然后回调函数处理内容，满足我当前的需求，咱就不再改造了。</p>
<p>其他详细文件内容如下：</p>
<blockquote>
<p>src/index.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> program <span class="hljs-keyword">from</span> <span class="hljs-string">'commander'</span>;
<span class="hljs-keyword">import</span> common <span class="hljs-keyword">from</span> <span class="hljs-string">'./common'</span>;

program
  .version(<span class="hljs-string">'0.0.1'</span>)
  .description(<span class="hljs-string">'工具库'</span>)

program
  .command(<span class="hljs-string">'jsliang'</span>)
  .description(<span class="hljs-string">'jsliang 帮助指令'</span>)
  .action(<span class="hljs-function">() =></span> &#123;
    common();
  &#125;);

program.parse(process.argv);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>src/base/config.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@name </span>默认的全局配置
 * <span class="hljs-doctag">@time </span>2021-05-22 16:12:21
 */</span>
<span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;

<span class="hljs-comment">// 基础目录</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> BASE_PATH = path.join(__dirname, <span class="hljs-string">'./docs'</span>);

<span class="hljs-comment">// 忽略目录</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> IGNORE_PATH = [
  <span class="hljs-string">'.vscode'</span>,
  <span class="hljs-string">'node_modules'</span>,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>src/common/sortCatalog.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@name </span>文件排序功能
 * <span class="hljs-doctag">@time </span>2021-05-22 16:08:06
 * <span class="hljs-doctag">@description </span>规则
   1. 系统顺序 1/10/2/21/3，希望排序 1/2/3/10/21
   2. 插入文件 1/2/1-1，希望排序 1/2/3（将 1-1 变成 2，2 变成 3）
*/</span>
<span class="hljs-keyword">import</span> fs <span class="hljs-keyword">from</span> <span class="hljs-string">'fs'</span>;
<span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;
<span class="hljs-keyword">import</span> &#123; IGNORE_PATH &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../base/config'</span>;

<span class="hljs-keyword">const</span> recursion = <span class="hljs-function">(<span class="hljs-params">filePath: string, level = <span class="hljs-number">0</span></span>) =></span> &#123;
  <span class="hljs-keyword">const</span> files = fs.readdirSync(filePath);

  files
    .filter((<span class="hljs-function"><span class="hljs-params">item</span> =></span> !IGNORE_PATH.includes(item))) <span class="hljs-comment">// 过滤忽略文件/文件夹</span>
    .sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span>
      <span class="hljs-built_in">Number</span>((a.split(<span class="hljs-string">'.'</span>)[<span class="hljs-number">0</span>]).replace(<span class="hljs-string">'-'</span>, <span class="hljs-string">'.'</span>))
      - <span class="hljs-built_in">Number</span>((b.split(<span class="hljs-string">'.'</span>)[<span class="hljs-number">0</span>]).replace(<span class="hljs-string">'-'</span>, <span class="hljs-string">'.'</span>))
    ) <span class="hljs-comment">// 排序文件夹</span>
    .forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123; <span class="hljs-comment">// 遍历文件夹</span>
      <span class="hljs-comment">// 设置旧文件名称和新文件名称</span>
      <span class="hljs-keyword">const</span> oldFileName = item;
      <span class="hljs-keyword">const</span> newFileName = <span class="hljs-string">`<span class="hljs-subst">$&#123;index + <span class="hljs-number">1</span>&#125;</span>.<span class="hljs-subst">$&#123;oldFileName.slice(oldFileName.indexOf(<span class="hljs-string">'.'</span>) + <span class="hljs-number">1</span>)&#125;</span>`</span>;

      <span class="hljs-comment">// 设置旧文件路径和新文件路径</span>
      <span class="hljs-keyword">const</span> oldPath = <span class="hljs-string">`<span class="hljs-subst">$&#123;filePath&#125;</span>/<span class="hljs-subst">$&#123;oldFileName&#125;</span>`</span>;
      <span class="hljs-keyword">const</span> newPath = <span class="hljs-string">`<span class="hljs-subst">$&#123;filePath&#125;</span>/<span class="hljs-subst">$&#123;newFileName&#125;</span>`</span>;

      <span class="hljs-comment">// 判断文件格式</span>
      <span class="hljs-keyword">const</span> stat = fs.statSync(oldPath);

      <span class="hljs-comment">// 判断是文件夹还是文件</span>
      <span class="hljs-keyword">if</span> (stat.isFile()) &#123;
        fs.renameSync(oldPath, newPath); <span class="hljs-comment">// 重命名文件</span>
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (stat.isDirectory()) &#123;
        fs.renameSync(oldPath, newPath); <span class="hljs-comment">// 重命名文件夹</span>
        recursion(newPath, level + <span class="hljs-number">1</span>); <span class="hljs-comment">// 递归文件夹</span>
      &#125;
    &#125;);
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> sortCatalog = (filePath: string): <span class="hljs-function"><span class="hljs-params">boolean</span> =></span> &#123;
  <span class="hljs-comment">// 绝对路径</span>
  <span class="hljs-keyword">if</span> (path.isAbsolute(filePath)) &#123;
    recursion(filePath);
  &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 相对路径</span>
    recursion(path.join(__dirname, filePath));
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么，<code>Inquirer.js</code> 接入就搞定了，试试我们的 <code>npm run jsliang</code>，可以正常使用！</p>
<p>后面可以愉快写功能啦~</p>
<h2 data-id="heading-10"><a name="user-content-chapter-six" id="user-content-chapter-six" href="https://juejin.cn/post/undefined"></a>六 参考文献</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6974171023025389576#chapter-one">返回目录</a></p>
</blockquote>
<ul>
<li><a href="https://github.com/SBoudrias/Inquirer.js/" target="_blank" rel="nofollow noopener noreferrer">GitHub：SBoudrias/Inquirer.js</a></li>
<li><a href="https://github.com/ReactiveX/rxjs" target="_blank" rel="nofollow noopener noreferrer">GitHub：rxjs</a></li>
<li><a href="https://cn.rx.js.org/manual/overview.html" target="_blank" rel="nofollow noopener noreferrer">RxJS 中文文档</a></li>
<li><a href="https://blog.csdn.net/qq_26733915/article/details/80461257" target="_blank" rel="nofollow noopener noreferrer">CSDN：inquirer.js —— 一个用户与命令行交互的工具</a></li>
</ul>
<hr>
<blockquote>
<p>jsliang 的文档库由 <a href="https://github.com/LiangJunrong" target="_blank" rel="nofollow noopener noreferrer">梁峻荣</a> 采用 <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="nofollow noopener noreferrer">知识共享 署名-非商业性使用-相同方式共享 4.0 国际 许可协议</a> 进行许可。<br>基于 <a href="https://github.com/LiangJunrong/document-library" target="_blank" rel="nofollow noopener noreferrer">github.com/LiangJunron…</a> 上的作品创作。<br>本许可协议授权之外的使用权限可以从 <a href="https://creativecommons.org/licenses/by-nc-sa/2.5/cn/" target="_blank" rel="nofollow noopener noreferrer">creativecommons.org/licenses/by…</a> 处获得。</p>
</blockquote></div>  
</div>
            