
---
title: 'Node 系列 - 007 - node-xlsx'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abecbc54bcb24e68995f977feb7a78ef~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 08:05:30 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abecbc54bcb24e68995f977feb7a78ef~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>——————————☆☆☆——————————</p>
<p>Node 系列相应地址：</p>
<ul>
<li>代码仓库：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FLiangJunrong%2Fall-for-one" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/LiangJunrong/all-for-one" ref="nofollow noopener noreferrer">github.com/LiangJunron…</a></li>
<li>文章仓库：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FLiangJunrong%2Fdocument-library%2Ftree%2Fmaster%2F%25E7%25B3%25BB%25E5%2588%2597-%25E5%2589%258D%25E7%25AB%25AF%25E8%25B5%2584%25E6%2596%2599%2FNode" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/LiangJunrong/document-library/tree/master/%E7%B3%BB%E5%88%97-%E5%89%8D%E7%AB%AF%E8%B5%84%E6%96%99/Node" ref="nofollow noopener noreferrer">github.com/LiangJunron…</a></li>
</ul>
<p>——————————☆☆☆——————————</p>
<p>在通过 Puppeteer 操作浏览器下载到 Excel 之后，我们终于可以将预备将多语言的操作玩出花来了。</p>
<p>本篇我们将通过 <code>node-xlsx</code>，对 Excel 进行多语言导入导出的操作。</p>

<h2 data-id="heading-0"><a name="user-content-chapter-one" id="user-content-chapter-one" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a>一 目录</h2>
<p><strong>不折腾的前端，和咸鱼有什么区别</strong></p>












































<table><thead><tr><th>目录</th></tr></thead><tbody><tr><td><a href="https://juejin.cn/post/6984070264615075847#chapter-one" target="_blank" title="#chapter-one">一 目录</a></td></tr><tr><td><a name="user-content-catalog-chapter-two" id="user-content-catalog-chapter-two" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a><a href="https://juejin.cn/post/6984070264615075847#chapter-two" target="_blank" title="#chapter-two">二 前言</a></td></tr><tr><td><a name="user-content-catalog-chapter-three" id="user-content-catalog-chapter-three" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a><a href="https://juejin.cn/post/6984070264615075847#chapter-three" target="_blank" title="#chapter-three">三 快速开始</a></td></tr><tr><td> <a href="https://juejin.cn/post/6984070264615075847#chapter-three-one" target="_blank" title="#chapter-three-one">3.1 测试导入</a></td></tr><tr><td> <a href="https://juejin.cn/post/6984070264615075847#chapter-three-two" target="_blank" title="#chapter-three-two">3.2 测试导出</a></td></tr><tr><td> <a href="https://juejin.cn/post/6984070264615075847#chapter-three-three" target="_blank" title="#chapter-three-three">3.3 测试定制宽度</a></td></tr><tr><td><a name="user-content-catalog-chapter-four" id="user-content-catalog-chapter-four" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a><a href="https://juejin.cn/post/6984070264615075847#chapter-four" target="_blank" title="#chapter-four">四 多语言操作</a></td></tr><tr><td> <a href="https://juejin.cn/post/6984070264615075847#chapter-four-one" target="_blank" title="#chapter-four-one">4.1 导入</a></td></tr><tr><td> <a href="https://juejin.cn/post/6984070264615075847#chapter-four-two" target="_blank" title="#chapter-four-two">4.2 导出</a></td></tr><tr><td><a name="user-content-catalog-chapter-five" id="user-content-catalog-chapter-five" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a><a href="https://juejin.cn/post/6984070264615075847#chapter-five" target="_blank" title="#chapter-five">五 后续</a></td></tr><tr><td><a name="user-content-catalog-chapter-six" id="user-content-catalog-chapter-six" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a><a href="https://juejin.cn/post/6984070264615075847#chapter-six" target="_blank" title="#chapter-six">六 参考文献</a></td></tr><tr><td></td></tr></tbody></table>
<h2 data-id="heading-1"><a name="user-content-chapter-two" id="user-content-chapter-two" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a>二 前言</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6984070264615075847#chapter-one" target="_blank" title="#chapter-one">返回目录</a></p>
</blockquote>
<p>在服务端的工作中，生成报表并送给运营、产品进行分析应该是一门简单手艺。</p>
<p>但是在前端中，能这样耍的机会并不多，所以多语言操作是个好玩的点（没接触过的会觉得比较新鲜）。</p>
<p>当然，既然服务端可以，对 Node.js 来说，提供这种功能也无可厚非。</p>
<p><strong>jsliang</strong> 非常懒，所以直奔主题打开 GitHub：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abecbc54bcb24e68995f977feb7a78ef~tplv-k3u1fbpfcp-watermark.image" alt="Excel-01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那就第 1 个了，不要搞什么调研不调研的，对于非生产数据来说，我就是玩~</p>
<p>看第一行简介：<code>Excel file parser/builder that relies on js-xlsx.</code></p>
<p><code>js-xlsx</code>？这个我知道啊，在 <code>2021.06.03</code> 这一刻有 <code>25.7k</code> Star 的仓库地址：<code>https://github.com/SheetJS/sheetjs</code></p>
<blockquote>
<p>其实一开始试了下它关于 Node 的，enm...一时半会没入门！</p>
</blockquote>
<p>但是，我还是用我的 <code>node-xlsx</code> 吧，毕竟例子都在它仓库的 README.md 贴出来了！</p>
<h2 data-id="heading-2"><a name="user-content-chapter-three" id="user-content-chapter-three" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a>三 快速开始</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6984070264615075847#chapter-one" target="_blank" title="#chapter-one">返回目录</a></p>
</blockquote>
<ul>
<li>安装包：<code>npm i node-xlsx -S</code></li>
<li>安装 TypeScript：<code>npm i @types/node-xlsx -D</code></li>
</ul>
<h3 data-id="heading-3"><a name="user-content-chapter-three-one" id="user-content-chapter-three-one" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a>3.1 测试导入</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6984070264615075847#chapter-one" target="_blank" title="#chapter-one">返回目录</a></p>
</blockquote>
<blockquote>
<p>src/index.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> program <span class="hljs-keyword">from</span> <span class="hljs-string">'commander'</span>;
<span class="hljs-keyword">import</span> common <span class="hljs-keyword">from</span> <span class="hljs-string">'./common'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'./base/console'</span>;
<span class="hljs-keyword">import</span> xlsx <span class="hljs-keyword">from</span> <span class="hljs-string">'node-xlsx'</span>;
<span class="hljs-keyword">import</span> fs <span class="hljs-keyword">from</span> <span class="hljs-string">'fs'</span>;

program
  .version(<span class="hljs-string">'0.0.1'</span>)
  .description(<span class="hljs-string">'工具库'</span>)

program
  .command(<span class="hljs-string">'jsliang'</span>)
  .description(<span class="hljs-string">'jsliang 帮助指令'</span>)
  .action(<span class="hljs-function">() =></span> &#123;
    common();
  &#125;);

program
  .command(<span class="hljs-string">'test'</span>)
  .description(<span class="hljs-string">'测试频道'</span>)
  .action(<span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-comment">// 测试新功能的时候使用</span>
    
    <span class="hljs-comment">// 以 buffer 形式导入</span>
    <span class="hljs-keyword">const</span> workSheetsFromBuffer = xlsx.parse(fs.readFileSync(<span class="hljs-string">`<span class="hljs-subst">$&#123;__dirname&#125;</span>/common/dist/Excel 试用文件.xlsx`</span>));
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">JSON</span>.stringify(workSheetsFromBuffer, <span class="hljs-literal">null</span>, <span class="hljs-number">2</span>));

    <span class="hljs-comment">// 以文件形式导入</span>
    <span class="hljs-keyword">const</span> workSheetsFromFile = xlsx.parse(<span class="hljs-string">`<span class="hljs-subst">$&#123;__dirname&#125;</span>/common/dist/Excel 试用文件.xlsx`</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">JSON</span>.stringify(workSheetsFromFile, <span class="hljs-literal">null</span>, <span class="hljs-number">2</span>));
  &#125;);

program.parse(process.argv);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 <code>npm run test</code>，控制台打印如下：</p>
<pre><code class="hljs language-js copyable" lang="js">---<span class="hljs-number">1</span>---
[
  &#123;
    <span class="hljs-string">"name"</span>: <span class="hljs-string">"Sheet1"</span>,
    <span class="hljs-string">"data"</span>: [
      [
        <span class="hljs-string">"key"</span>,
        <span class="hljs-string">"zh-CN"</span>,
        <span class="hljs-string">"en-US"</span>,
        <span class="hljs-string">"zh-TW"</span>,
        <span class="hljs-string">"zh-GZ"</span>
      ],
      [
        <span class="hljs-string">"noMoney"</span>,
        <span class="hljs-string">"我没钱啦！"</span>,
        <span class="hljs-string">"I have no money"</span>,
        <span class="hljs-string">"我沒錢啦！"</span>,
        <span class="hljs-string">"我冇钱啦！"</span>
      ]
    ]
  &#125;
]

---<span class="hljs-number">2</span>---
[
  &#123;
    <span class="hljs-string">"name"</span>: <span class="hljs-string">"Sheet1"</span>,
    <span class="hljs-string">"data"</span>: [
      [
        <span class="hljs-string">"key"</span>,
        <span class="hljs-string">"zh-CN"</span>,
        <span class="hljs-string">"en-US"</span>,
        <span class="hljs-string">"zh-TW"</span>,
        <span class="hljs-string">"zh-GZ"</span>
      ],
      [
        <span class="hljs-string">"noMoney"</span>,
        <span class="hljs-string">"我没钱啦！"</span>,
        <span class="hljs-string">"I have no money"</span>,
        <span class="hljs-string">"我沒錢啦！"</span>,
        <span class="hljs-string">"我冇钱啦！"</span>
      ]
    ]
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>OK，都能正常导入~</p>
<h3 data-id="heading-4"><a name="user-content-chapter-three-two" id="user-content-chapter-three-two" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a>3.2 测试导出</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6984070264615075847#chapter-one" target="_blank" title="#chapter-one">返回目录</a></p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> program <span class="hljs-keyword">from</span> <span class="hljs-string">'commander'</span>;
<span class="hljs-keyword">import</span> common <span class="hljs-keyword">from</span> <span class="hljs-string">'./common'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'./base/console'</span>;
<span class="hljs-keyword">import</span> xlsx <span class="hljs-keyword">from</span> <span class="hljs-string">'node-xlsx'</span>;
<span class="hljs-keyword">import</span> fs <span class="hljs-keyword">from</span> <span class="hljs-string">'fs'</span>;

program
  .version(<span class="hljs-string">'0.0.1'</span>)
  .description(<span class="hljs-string">'工具库'</span>)

program
  .command(<span class="hljs-string">'jsliang'</span>)
  .description(<span class="hljs-string">'jsliang 帮助指令'</span>)
  .action(<span class="hljs-function">() =></span> &#123;
    common();
  &#125;);

program
  .command(<span class="hljs-string">'test'</span>)
  .description(<span class="hljs-string">'测试频道'</span>)
  .action(<span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-comment">// 测试新功能的时候使用</span>
    
    <span class="hljs-comment">// 导出数据</span>
    <span class="hljs-keyword">const</span> data = [
      [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>],
      [<span class="hljs-literal">true</span>, <span class="hljs-literal">false</span>, <span class="hljs-literal">null</span>, <span class="hljs-string">'sheetjs'</span>],
      [<span class="hljs-string">'foo'</span>, <span class="hljs-string">'bar'</span>, <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-string">'2014-02-19T14:30Z'</span>), <span class="hljs-string">'0.3'</span>],
      [<span class="hljs-string">'baz'</span>, <span class="hljs-literal">null</span>, <span class="hljs-string">'qux'</span>],
    ];
    <span class="hljs-keyword">const</span> buffer = xlsx.build([&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"jsliang"</span>, <span class="hljs-attr">data</span>: data &#125;]); <span class="hljs-comment">// 拿到文件 buffer</span>

    <span class="hljs-comment">// 写入文件</span>
    fs.writeFileSync(<span class="hljs-string">`<span class="hljs-subst">$&#123;__dirname&#125;</span>/common/dist/test-sheet.xlsx`</span>, Buffer.from(buffer));
  &#125;);

program.parse(process.argv);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 <code>npm run test</code> 后，目录变成：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6f2c16a9f1144f5bac8e0a9e8926b78~tplv-k3u1fbpfcp-watermark.image" alt="Excel-02.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>打开这个 Excel 文件，可以看到：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86c308b70b4944a58032f4ef62213c44~tplv-k3u1fbpfcp-watermark.image" alt="Excel-03.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>好的，导出也 OK 了~</p>
<h3 data-id="heading-5"><a name="user-content-chapter-three-three" id="user-content-chapter-three-three" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a>3.3 测试定制宽度</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6984070264615075847#chapter-one" target="_blank" title="#chapter-one">返回目录</a></p>
</blockquote>
<p>当然，有时候产品非常懒，需要我们将表格宽度给做好成每一列都能宽一点，那就要定制下页面宽度：</p>
<blockquote>
<p>index.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> program <span class="hljs-keyword">from</span> <span class="hljs-string">'commander'</span>;
<span class="hljs-keyword">import</span> common <span class="hljs-keyword">from</span> <span class="hljs-string">'./common'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'./base/console'</span>;
<span class="hljs-keyword">import</span> xlsx <span class="hljs-keyword">from</span> <span class="hljs-string">'node-xlsx'</span>;
<span class="hljs-keyword">import</span> fs <span class="hljs-keyword">from</span> <span class="hljs-string">'fs'</span>;

program
  .version(<span class="hljs-string">'0.0.1'</span>)
  .description(<span class="hljs-string">'工具库'</span>)

program
  .command(<span class="hljs-string">'jsliang'</span>)
  .description(<span class="hljs-string">'jsliang 帮助指令'</span>)
  .action(<span class="hljs-function">() =></span> &#123;
    common();
  &#125;);

program
  .command(<span class="hljs-string">'test'</span>)
  .description(<span class="hljs-string">'测试频道'</span>)
  .action(<span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-comment">// 测试新功能的时候使用</span>
    
    <span class="hljs-comment">// 导出数据</span>
    <span class="hljs-keyword">const</span> data = [
      [<span class="hljs-string">'key'</span>, <span class="hljs-string">'zh-CN'</span>, <span class="hljs-string">'en-US'</span>, <span class="hljs-string">'zh-TW'</span>, <span class="hljs-string">'zh-GZ'</span>],
      [<span class="hljs-string">'noMoney'</span>, <span class="hljs-string">'我没钱啦！'</span>, <span class="hljs-string">'I have no money'</span>, <span class="hljs-string">'我沒錢啦！'</span>, <span class="hljs-string">'我冇钱啦！'</span>],
    ];
    <span class="hljs-comment">// 列宽设置</span>
    <span class="hljs-keyword">const</span> options = &#123;
      <span class="hljs-string">'!cols'</span>: [
        &#123; <span class="hljs-attr">wch</span>: <span class="hljs-number">10</span> &#125;,
        &#123; <span class="hljs-attr">wch</span>: <span class="hljs-number">15</span> &#125;,
        &#123; <span class="hljs-attr">wch</span>: <span class="hljs-number">15</span> &#125;,
        &#123; <span class="hljs-attr">wch</span>: <span class="hljs-number">15</span> &#125;,
        &#123; <span class="hljs-attr">wch</span>: <span class="hljs-number">15</span> &#125;,
      ]
    &#125;
    <span class="hljs-comment">// 生成 buffer</span>
    <span class="hljs-keyword">const</span> buffer = xlsx.build([&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"jsliang"</span>, <span class="hljs-attr">data</span>: data &#125;], options); <span class="hljs-comment">// 拿到文件 buffer</span>

    <span class="hljs-comment">// 写入文件</span>
    fs.writeFileSync(<span class="hljs-string">`<span class="hljs-subst">$&#123;__dirname&#125;</span>/common/dist/Excel 导出文件.xlsx`</span>, Buffer.from(buffer));
  &#125;);

program.parse(process.argv);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 <code>npm run test</code>，看到 <code>dist</code> 目录生成：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0eaa2033b4494f14ae53d04b639de983~tplv-k3u1fbpfcp-watermark.image" alt="Excel-04.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后点开「Excel 导出文件.xlsx」，里面内容为：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/426ea31aa48244f3b8b3557e6d2c3130~tplv-k3u1fbpfcp-watermark.image" alt="Excel-05.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>安逸，满屏飘满 no money~</p>
<h2 data-id="heading-6"><a name="user-content-chapter-four" id="user-content-chapter-four" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a>四 多语言操作</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6984070264615075847#chapter-one" target="_blank" title="#chapter-one">返回目录</a></p>
</blockquote>
<p>在我们简单了解 <code>node-xlsx</code> 之后，我们就可以通过它完成多语言的导入导出，以及下一章会讲解如何获取需要的资源。</p>
<h3 data-id="heading-7"><a name="user-content-chapter-four-one" id="user-content-chapter-four-one" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a>4.1 导入</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6984070264615075847#chapter-one" target="_blank" title="#chapter-one">返回目录</a></p>
</blockquote>
<p>接「006 - Puppeteer」，我们在上一篇文章已经完成了资源的下载，实际上我们应该一条龙服务，从下载到导入统统给安排了。</p>
<p>那么，我们当前的目录需要改造一番：</p>
<pre><code class="copyable">- src
  + base
  - common
    - language
      + dist
      - download.ts
      - export.ts
      - import.ts
      - source.json
    - index.ts
    - questionList.ts
    - sortCatalog.ts
  - index.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<p>文字目录好像没那么清晰，还是贴个图吧：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0a08eacae1c4d65a82ecfaa9a421f59~tplv-k3u1fbpfcp-watermark.image" alt="Excel-06.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么，开始写代码：</p>
<blockquote>
<p>questionList.ts - 先明确自己的提问路线</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// common 板块的问题咨询路线</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> questionList = &#123;
  <span class="hljs-string">'公共服务'</span>: &#123; <span class="hljs-comment">// q0</span>
    <span class="hljs-string">'文件排序'</span>: &#123; <span class="hljs-comment">// q1</span>
      <span class="hljs-string">'需要排序的文件夹'</span>: <span class="hljs-string">'Work 工作'</span>, <span class="hljs-comment">// q2</span>
    &#125;,
  &#125;,
  <span class="hljs-string">'多语言'</span>: &#123; <span class="hljs-comment">// q0</span>
    <span class="hljs-string">'下载多语言资源'</span>: &#123; <span class="hljs-comment">// q3</span>
      <span class="hljs-string">'下载地址'</span>: <span class="hljs-string">'Work 工作'</span>, <span class="hljs-comment">// q4</span>
    &#125;,
    <span class="hljs-string">'导入多语言资源'</span>: &#123; <span class="hljs-comment">// q3</span>
      <span class="hljs-string">'下载地址'</span>: <span class="hljs-string">'Work 工作'</span>, <span class="hljs-comment">// q4</span>
    &#125;,
    <span class="hljs-string">'导出多语言资源'</span>: &#123; <span class="hljs-comment">// q3</span>
      <span class="hljs-string">'导出全量资源'</span>: <span class="hljs-string">'Work 工作'</span>,
      <span class="hljs-string">'导出单门资源'</span>: <span class="hljs-string">'Work 工作'</span>,
    &#125;
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>index.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; inquirer &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../base/inquirer'</span>;
<span class="hljs-keyword">import</span> &#123; Result &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../base/interface'</span>;
<span class="hljs-keyword">import</span> &#123; sortCatalog &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./sortCatalog'</span>;
<span class="hljs-keyword">import</span> &#123; downLoadExcel &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./language/download'</span>;
<span class="hljs-keyword">import</span> &#123; importLanguage &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./language/import'</span>;
<span class="hljs-keyword">import</span> &#123; exportLanguage &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./language/export'</span>;

<span class="hljs-comment">// 问题记录器</span>
<span class="hljs-keyword">const</span> answers = &#123;
  <span class="hljs-attr">q0</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">q1</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">q2</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">q3</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">q4</span>: <span class="hljs-string">''</span>,
&#125;;

<span class="hljs-keyword">const</span> common = (): <span class="hljs-function"><span class="hljs-params">void</span> =></span> &#123;
  <span class="hljs-comment">// 问题路线：看 questionList.ts</span>
  <span class="hljs-keyword">const</span> questionList = [
    <span class="hljs-comment">// q0</span>
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'list'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'请问需要什么服务？'</span>,
      <span class="hljs-attr">choices</span>: [<span class="hljs-string">'公共服务'</span>, <span class="hljs-string">'多语言'</span>]
    &#125;,
    <span class="hljs-comment">// q1</span>
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'list'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'当前公共服务有：'</span>,
      <span class="hljs-attr">choices</span>: [<span class="hljs-string">'文件排序'</span>]
    &#125;,
    <span class="hljs-comment">// q2</span>
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'需要排序的文件夹为？（绝对路径）'</span>,
    &#125;,
    <span class="hljs-comment">// q3</span>
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'list'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'请问多语言需要什么支持？'</span>,
      <span class="hljs-attr">choices</span>: [
        <span class="hljs-string">'下载多语言资源'</span>,
        <span class="hljs-string">'导入多语言资源'</span>,
        <span class="hljs-string">'导出多语言资源'</span>,
      ],
    &#125;,
    <span class="hljs-comment">// q4</span>
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'资源下载地址（HTTP）？'</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">'https://www.kdocs.cn/l/sdwvJUKBzkK2'</span>,
    &#125;
  ];

  <span class="hljs-keyword">const</span> answerList = [
    <span class="hljs-comment">// q0 - 请问需要什么服务？</span>
    <span class="hljs-keyword">async</span> (result: Result, <span class="hljs-attr">questions</span>: any) => &#123;
      answers.q0 = result.answer;
      <span class="hljs-keyword">switch</span> (result.answer) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'公共服务'</span>:
          questions[<span class="hljs-number">1</span>]();
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'多语言'</span>:
          questions[<span class="hljs-number">3</span>]();
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">default</span>: <span class="hljs-keyword">break</span>;
      &#125;
    &#125;,
    <span class="hljs-comment">// q1 - 当前公共服务有：</span>
    <span class="hljs-keyword">async</span> (result: Result, <span class="hljs-attr">questions</span>: any) => &#123;
      answers.q1 = result.answer;
      <span class="hljs-keyword">if</span> (result.answer === <span class="hljs-string">'文件排序'</span>) &#123;
        questions[<span class="hljs-number">2</span>]();
      &#125;
    &#125;,
    <span class="hljs-comment">// q2 - 需要排序的文件夹为？（绝对路径）</span>
    <span class="hljs-keyword">async</span> (result: Result, <span class="hljs-attr">_questions</span>: any, <span class="hljs-attr">prompts</span>: any) => &#123;
      answers.q2 = result.answer;
      <span class="hljs-keyword">const</span> sortResult = <span class="hljs-keyword">await</span> sortCatalog(result.answer);
      <span class="hljs-keyword">if</span> (sortResult) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'排序成功！'</span>);
        prompts.complete();
      &#125;
    &#125;,
    <span class="hljs-comment">// q3 - 请问多语言需要什么支持？</span>
    <span class="hljs-keyword">async</span> (result: Result, <span class="hljs-attr">questions</span>: any, <span class="hljs-attr">prompts</span>: any) => &#123;
      answers.q3 = result.answer;
      <span class="hljs-keyword">switch</span> (result.answer) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'下载多语言资源'</span>:
        <span class="hljs-keyword">case</span> <span class="hljs-string">'导入多语言资源'</span>:
          questions[<span class="hljs-number">4</span>]();
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'导出多语言资源'</span>:
          <span class="hljs-keyword">const</span> exportResult = <span class="hljs-keyword">await</span> exportLanguage();
          <span class="hljs-keyword">if</span> (exportResult) &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'导出成功！'</span>);
            prompts.complete();
          &#125;
        <span class="hljs-attr">default</span>: <span class="hljs-keyword">break</span>;
      &#125;
    &#125;,
    <span class="hljs-comment">// q4 - 资源下载地址（HTTP）？</span>
    <span class="hljs-keyword">async</span> (result: Result) => &#123;
      answers.q4 = result.answer;
      <span class="hljs-keyword">const</span> download = <span class="hljs-keyword">async</span> (): <span class="hljs-built_in">Promise</span><any> => &#123;
        <span class="hljs-keyword">const</span> downloadResult = <span class="hljs-keyword">await</span> downLoadExcel(result.answer);
        <span class="hljs-keyword">if</span> (downloadResult) &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'下载成功！'</span>);
          <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
        &#125;
      &#125;;
      <span class="hljs-keyword">switch</span> (answers.q3) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'下载多语言资源'</span>:
          <span class="hljs-keyword">await</span> download();
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'导入多语言资源'</span>:
          <span class="hljs-keyword">await</span> download();
          <span class="hljs-keyword">const</span> importResult = <span class="hljs-keyword">await</span> importLanguage();
          <span class="hljs-keyword">if</span> (importResult) &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'导入完毕！'</span>);
          &#125;
        <span class="hljs-attr">default</span>:
          <span class="hljs-keyword">break</span>;
      &#125;
    &#125;,
  ];

  inquirer(questionList, answerList);
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> common;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，我们如果要导入的话，肯定有个对应的资源文件，这边就用 <code>source.json</code> 演示：</p>
<blockquote>
<p>source.json</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"zh-CN"</span>: &#123;

  &#125;,
  <span class="hljs-string">"en-US"</span>: &#123;

  &#125;,
  <span class="hljs-string">"zh-TW"</span>: &#123;

  &#125;,
  <span class="hljs-string">"zh-GZ"</span>: &#123;

  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简版内容如下，通过 <code>import.ts</code> 导入资源并填充里面内容：</p>
<blockquote>
<p>import.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> xlsx <span class="hljs-keyword">from</span> <span class="hljs-string">'node-xlsx'</span>;
<span class="hljs-keyword">import</span> fs <span class="hljs-keyword">from</span> <span class="hljs-string">'fs'</span>;
<span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> importLanguage = <span class="hljs-keyword">async</span> (): <span class="hljs-built_in">Promise</span><boolean> => &#123;
  <span class="hljs-keyword">const</span> language = <span class="hljs-built_in">JSON</span>.parse(fs.readFileSync(path.join(__dirname, <span class="hljs-string">'./source.json'</span>), <span class="hljs-string">'utf8'</span>));

  <span class="hljs-keyword">const</span> workSheetsFromBuffer = xlsx.parse(
    fs.readFileSync(
      path.join(__dirname, <span class="hljs-string">'/dist/Excel 试用文件.xlsx'</span>),
    ),
  );

  <span class="hljs-keyword">const</span> sheet1Data = workSheetsFromBuffer[<span class="hljs-number">0</span>].data.map(<span class="hljs-function"><span class="hljs-params">i</span> =></span> i.map(<span class="hljs-function"><span class="hljs-params">j</span> =></span> <span class="hljs-built_in">String</span>(j)));

  <span class="hljs-comment">// 获取头部数据</span>
  <span class="hljs-keyword">const</span> header = sheet1Data[<span class="hljs-number">0</span>];
  
  <span class="hljs-comment">// 查找 key 对应列</span>
  <span class="hljs-keyword">let</span> keyIndex = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < header.length; i++) &#123;
    <span class="hljs-keyword">if</span> (header[i] === <span class="hljs-string">'key'</span>) &#123;
      keyIndex = i;
      <span class="hljs-keyword">break</span>;
    &#125;
  &#125;
  <span class="hljs-keyword">if</span> (keyIndex < <span class="hljs-number">0</span>) &#123;
    <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'未找到 key 对应列！'</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  &#125;

  <span class="hljs-comment">// 设置资源内容</span>
  <span class="hljs-keyword">const</span> fullLanguage: any[] = [...Object.keys(language), ...header.filter(<span class="hljs-function">(<span class="hljs-params">item: any</span>) =></span> item !== <span class="hljs-string">'key'</span>)];
  <span class="hljs-keyword">const</span> filterFullLanguage = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < fullLanguage.length; i++) &#123;
    <span class="hljs-keyword">if</span> (!filterFullLanguage.has(fullLanguage[i])) &#123;
      filterFullLanguage.add(fullLanguage[i]);
      <span class="hljs-comment">// 如果没有该种语言，则新增</span>
      <span class="hljs-keyword">if</span> (!language[fullLanguage[i]]) &#123;
        language[fullLanguage[i]] = &#123;&#125;;
      &#125;
    &#125;
  &#125;

  <span class="hljs-comment">// 获取内容数据</span>
  <span class="hljs-keyword">const</span> body = sheet1Data.slice(<span class="hljs-number">1</span>);
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < body.length; i++) &#123;

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < body[i].length; j++) &#123;
      <span class="hljs-keyword">if</span> (j !== keyIndex) &#123;
        <span class="hljs-keyword">const</span> nowLanguage = language[header[j]]; <span class="hljs-comment">// 一个损耗性能的操作，每次都会读取新列表，但是我不想优化</span>
        <span class="hljs-keyword">const</span> nowKey = body[i][keyIndex]; <span class="hljs-comment">// 获取这一行的 key</span>
        nowLanguage[nowKey] = body[i][j]; <span class="hljs-comment">// 替换 key</span>
      &#125;
    &#125;
  &#125;

  fs.writeFileSync(path.join(__dirname, <span class="hljs-string">'./source.json'</span>), <span class="hljs-built_in">JSON</span>.stringify(language, <span class="hljs-literal">null</span>, <span class="hljs-number">2</span>), <span class="hljs-string">'utf8'</span>);

  <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>export.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> exportLanguage = <span class="hljs-keyword">async</span> (): <span class="hljs-built_in">Promise</span><boolean> => &#123;
  <span class="hljs-comment">// 详细内容待补充</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">await</span> <span class="hljs-literal">true</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编写完毕，执行 <code>npm run jsliang</code>，按照提问逐个回车：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/322639db414f42468dd0fd92cd862807~tplv-k3u1fbpfcp-watermark.image" alt="Excel-07.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后代码跑起来（姿势很帅），成功导入：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2da07b7201846fcbfca935388a43e45~tplv-k3u1fbpfcp-watermark.image" alt="Excel-08.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc9a6c3121ff47ba87e9247dd2af4e0c~tplv-k3u1fbpfcp-watermark.image" alt="Excel-09.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样导入流程就完毕了。</p>
<blockquote>
<p>当然，导入的过程中，还需要修复对齐 key（即某中文 key 情况下，其他资源未翻译；或者删除 key 资源），这些就不哆嗦列举了，需要的时候补充写一写，也不难~</p>
</blockquote>
<h3 data-id="heading-8"><a name="user-content-chapter-four-two" id="user-content-chapter-four-two" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a>4.2 导出</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6984070264615075847#chapter-one" target="_blank" title="#chapter-one">返回目录</a></p>
</blockquote>
<p>导入尚且如此，导出就更轻松了：</p>
<blockquote>
<p>export.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> xlsx <span class="hljs-keyword">from</span> <span class="hljs-string">'node-xlsx'</span>;
<span class="hljs-keyword">import</span> fs <span class="hljs-keyword">from</span> <span class="hljs-string">'fs'</span>;
<span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> exportLanguage = <span class="hljs-keyword">async</span> (): <span class="hljs-built_in">Promise</span><boolean> => &#123;
  <span class="hljs-keyword">const</span> languageData = <span class="hljs-built_in">JSON</span>.parse(fs.readFileSync(path.join(__dirname, <span class="hljs-string">'./source.json'</span>), <span class="hljs-string">'utf8'</span>));

  <span class="hljs-comment">// 组装头部数据</span>
  <span class="hljs-keyword">const</span> header = <span class="hljs-built_in">Object</span>.keys(languageData);

  <span class="hljs-comment">// 组装内容数据</span>
  <span class="hljs-keyword">const</span> chineseKeyList = <span class="hljs-built_in">Object</span>.keys(languageData[<span class="hljs-string">'zh-CN'</span>]);
  <span class="hljs-keyword">const</span> body: any[] = [];
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < chineseKeyList.length; i++) &#123;
    <span class="hljs-keyword">const</span> nowKey = chineseKeyList[i];
    <span class="hljs-keyword">const</span> nowFloor = [nowKey];
    <span class="hljs-built_in">console</span>.log(nowFloor, nowKey);
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < header.length; j++) &#123;
      <span class="hljs-keyword">const</span> nowLanguage = header[j];
      nowFloor.push(languageData[nowLanguage][nowKey]);
    &#125;
    body.push(nowFloor);
  &#125;

  <span class="hljs-comment">// 导出数据</span>
  <span class="hljs-keyword">const</span> data = [
    [<span class="hljs-string">'keys'</span>, ...header],
    ...body,
  ];
  <span class="hljs-keyword">const</span> buffer = xlsx.build([&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"jsliang"</span>, <span class="hljs-attr">data</span>: data &#125;]); <span class="hljs-comment">// 拿到文件 buffer</span>

  <span class="hljs-comment">// 写入文件</span>
  fs.writeFileSync(path.join(__dirname, <span class="hljs-string">'./dist/Excel 导出文件.xlsx'</span>), Buffer.from(buffer));

  <span class="hljs-keyword">return</span> <span class="hljs-keyword">await</span> <span class="hljs-literal">true</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 <code>npm run jsliang</code>，按流程点点：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/946baa1f8c0e4ff7bb458f4fc3fe77a6~tplv-k3u1fbpfcp-watermark.image" alt="Excel-10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后就看下 <code>dist</code> 目录有没有对应的文件：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90ea768cff8f4bf1a632229e9bbff3d5~tplv-k3u1fbpfcp-watermark.image" alt="Excel-11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在打开文件看看：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0076ab34455b4636b8e724bf6b2a5d80~tplv-k3u1fbpfcp-watermark.image" alt="Excel-12.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>OK，搞定，收工~</p>
<h2 data-id="heading-9"><a name="user-content-chapter-five" id="user-content-chapter-five" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a>五 后续</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6984070264615075847#chapter-one" target="_blank" title="#chapter-one">返回目录</a></p>
</blockquote>
<p>那么，Excel 的操作流程我们就安排得明明白白了。</p>
<p>再往下一章，<strong>jsliang</strong> 可能开启 Node 服务，完成简单网站的搭建，不过 <strong>jsliang</strong> 于 2018 年写过一篇 Node 从 0 基础到企业官网的文章了，所以咱们尝试搞个小游戏吧，嘿嘿~</p>
<blockquote>
<p>当前阶段算上 Node 初篇完毕，主要也没啥内容，后续会补充开启服务，WebSocket 等内容，冲鸭~</p>
</blockquote>
<h2 data-id="heading-10"><a name="user-content-chapter-six" id="user-content-chapter-six" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a>六 参考文献</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6984070264615075847#chapter-one" target="_blank" title="#chapter-one">返回目录</a></p>
</blockquote>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcloud.tencent.com%2Fdeveloper%2Farticle%2F1653844" target="_blank" rel="nofollow noopener noreferrer" title="https://cloud.tencent.com/developer/article/1653844" ref="nofollow noopener noreferrer">nodejs 实现导出 excel 报表</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FSheetJS%2Fsheetjs" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/SheetJS/sheetjs" ref="nofollow noopener noreferrer">GitHub：SheetJS</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmgcrea%2Fnode-xlsx" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/mgcrea/node-xlsx" ref="nofollow noopener noreferrer">GitHub：node-xlsx</a></li>
</ul>
<hr>
<blockquote>
<p>jsliang 的文档库由 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FLiangJunrong" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/LiangJunrong" ref="nofollow noopener noreferrer">梁峻荣</a> 采用 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fcreativecommons.org%2Flicenses%2Fby-nc-sa%2F4.0%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://creativecommons.org/licenses/by-nc-sa/4.0/" ref="nofollow noopener noreferrer">知识共享 署名-非商业性使用-相同方式共享 4.0 国际 许可协议</a> 进行许可。<br>基于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FLiangJunrong%2Fdocument-library" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/LiangJunrong/document-library" ref="nofollow noopener noreferrer">github.com/LiangJunron…</a> 上的作品创作。<br>本许可协议授权之外的使用权限可以从 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcreativecommons.org%2Flicenses%2Fby-nc-sa%2F2.5%2Fcn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://creativecommons.org/licenses/by-nc-sa/2.5/cn/" ref="nofollow noopener noreferrer">creativecommons.org/licenses/by…</a> 处获得。</p>
</blockquote></div>  
</div>
            