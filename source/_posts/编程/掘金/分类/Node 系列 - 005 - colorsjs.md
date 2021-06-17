
---
title: 'Node 系列 - 005 - colors.js'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72758079c96547f1876bb5f4479438e0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 16 Jun 2021 16:05:24 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72758079c96547f1876bb5f4479438e0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>接入 <code>commander.js</code> 和 <code>Inquirer.js</code> 之后，本应该直接接上 <code>colors.js</code>，毕竟我们现在是控制台输出，控制台不搞得飘飘亮亮（花里胡哨的）。</p>
<p>但是上篇 <code>Inquires.js</code> 太给力了，直接上了 1.7w 字，所以相对而言，这篇就简短点呗。</p>
<blockquote>
<p>阅读提示：本篇文章略短，易读，下一篇再搞大的，不接受吐槽~</p>
</blockquote>

<h2 data-id="heading-0"><a name="user-content-chapter-one" id="user-content-chapter-one" href="https://juejin.cn/post/undefined"></a>一 目录</h2>
<p><strong>不折腾的前端，和咸鱼有什么区别</strong></p>


























<table><thead><tr><th>目录</th></tr></thead><tbody><tr><td><a href="https://juejin.cn/post/6974542964764704782#chapter-one">一 目录</a></td></tr><tr><td><a name="user-content-catalog-chapter-two" id="user-content-catalog-chapter-two" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6974542964764704782#chapter-two">二 前言</a></td></tr><tr><td><a name="user-content-catalog-chapter-three" id="user-content-catalog-chapter-three" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6974542964764704782#chapter-three">三 colors.js</a></td></tr><tr><td><a name="user-content-catalog-chapter-four" id="user-content-catalog-chapter-four" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6974542964764704782#chapter-four">四 重写 console.log</a></td></tr><tr><td><a name="user-content-catalog-chapter-five" id="user-content-catalog-chapter-five" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6974542964764704782#chapter-five">五 参考文献</a></td></tr><tr><td></td></tr></tbody></table>
<h2 data-id="heading-1"><a name="user-content-chapter-two" id="user-content-chapter-two" href="https://juejin.cn/post/undefined"></a>二 前言</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6974542964764704782#chapter-one">返回目录</a></p>
</blockquote>
<p><code>colors.js</code> 是 Marak 做的一个 4.1k star（2021-06-16）的仓库。</p>
<p>接入 <code>colors.js</code> 后可以让你的控制台更爆炸更有美感。</p>
<ul>
<li>安装：<code>npm i colors</code></li>
<li>输入代码：</li>
</ul>
<blockquote>
<p>src/index.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> program <span class="hljs-keyword">from</span> <span class="hljs-string">'commander'</span>;
<span class="hljs-keyword">import</span> common <span class="hljs-keyword">from</span> <span class="hljs-string">'./common'</span>;
<span class="hljs-keyword">import</span> colors <span class="hljs-keyword">from</span> <span class="hljs-string">'colors'</span>;

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
  .action(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> text = <span class="hljs-string">`
      _   _____   _       _       ___   __   _   _____  
     | | /  ___/ | |     | |     /   | |  \\ | | /  ___| 
     | | | |___  | |     | |    / /| | |   \\| | | |     
  _  | | \\___  \\ | |     | |   / /—| | | |\\   | | |  _  
 | |_| |  ___| | | |___  | |  / /  | | | | \\  | | |_| |
 \\_____/ /_____/ |_____| |_| /_/   |_| |_|  \\_| \\_____/
    `</span>;
    <span class="hljs-built_in">console</span>.log(colors.rainbow(text));
  &#125;);

program.parse(process.argv);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>package.json</p>
</blockquote>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"jsliang"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">"Fe-util, Node 工具库"</span>,
  <span class="hljs-attr">"main"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"jsliang"</span>: <span class="hljs-string">"ts-node ./src/index.ts jsliang"</span>,
    <span class="hljs-attr">"test"</span>: <span class="hljs-string">"ts-node ./src/index.ts test"</span>
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
    <span class="hljs-attr">"colors"</span>: <span class="hljs-string">"^1.4.0"</span>,
    <span class="hljs-attr">"commander"</span>: <span class="hljs-string">"^7.2.0"</span>,
    <span class="hljs-attr">"inquirer"</span>: <span class="hljs-string">"^8.1.0"</span>,
    <span class="hljs-attr">"rxjs"</span>: <span class="hljs-string">"^5.5.12"</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>执行 <code>npm run test</code></li>
</ul>
<p>发现控制台老漂亮了：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72758079c96547f1876bb5f4479438e0~tplv-k3u1fbpfcp-watermark.image" alt="colors-01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在上面代码中，添加了 <code>test</code> 相关指令（后续我们测试内容就塞到这里，可以不用加，但是 <strong>jsliang</strong> 会拿来做示例用）</p>
<p>至于这个好看的字体，就是通过 ASCII 艺术字转换器转换过来的。</p>
<ul>
<li><a href="https://tools.kalvinbg.cn/txt/ascii" target="_blank" rel="nofollow noopener noreferrer">Kalvin 在线工具</a></li>
<li><a href="https://www.wncx.cn/ascii/" target="_blank" rel="nofollow noopener noreferrer">ASCII 字形生成器</a></li>
</ul>
<p>这边随意推荐 2 个，更多的小伙伴可以自行挖掘。</p>
<h2 data-id="heading-2"><a name="user-content-chapter-three" id="user-content-chapter-three" href="https://juejin.cn/post/undefined"></a>三 colors.js</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6974542964764704782#chapter-one">返回目录</a></p>
</blockquote>
<p>工欲善其事，必先利其器。</p>
<p>在上面我们展示了 <code>colors.js</code> 中的一种彩虹色 <code>colors.rainbow</code>，那么肯定会有其他颜色。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> colors <span class="hljs-keyword">from</span> <span class="hljs-string">'colors'</span>;

<span class="hljs-built_in">console</span>.log(colors.rainbow(<span class="hljs-string">'rainbow'</span>));
<span class="hljs-built_in">console</span>.log(colors.black(<span class="hljs-string">'black'</span>));
<span class="hljs-built_in">console</span>.log(colors.red(<span class="hljs-string">'red'</span>));
<span class="hljs-built_in">console</span>.log(colors.green(<span class="hljs-string">'green'</span>));
<span class="hljs-built_in">console</span>.log(colors.yellow(<span class="hljs-string">'yellow'</span>));
<span class="hljs-built_in">console</span>.log(colors.blue(<span class="hljs-string">'blue'</span>));
<span class="hljs-built_in">console</span>.log(colors.magenta(<span class="hljs-string">'magenta'</span>));
<span class="hljs-built_in">console</span>.log(colors.cyan(<span class="hljs-string">'cyan'</span>));
<span class="hljs-built_in">console</span>.log(colors.white(<span class="hljs-string">'white'</span>));
<span class="hljs-built_in">console</span>.log(colors.gray(<span class="hljs-string">'gray'</span>));
<span class="hljs-built_in">console</span>.log(colors.grey(<span class="hljs-string">'grey'</span>));
<span class="hljs-built_in">console</span>.log(colors.bgBlack(<span class="hljs-string">'bgBlack'</span>));
<span class="hljs-built_in">console</span>.log(colors.bgRed(<span class="hljs-string">'bgRed'</span>));
<span class="hljs-built_in">console</span>.log(colors.bgGreen(<span class="hljs-string">'bgGreen'</span>));
<span class="hljs-built_in">console</span>.log(colors.bgYellow(<span class="hljs-string">'bgYellow'</span>));
<span class="hljs-built_in">console</span>.log(colors.bgBlue(<span class="hljs-string">'bgBlue'</span>));
<span class="hljs-built_in">console</span>.log(colors.bgMagenta(<span class="hljs-string">'bgMagenta'</span>));
<span class="hljs-built_in">console</span>.log(colors.bgCyan(<span class="hljs-string">'bgCyan'</span>));
<span class="hljs-built_in">console</span>.log(colors.bgWhite(<span class="hljs-string">'bgWhite'</span>));
<span class="hljs-built_in">console</span>.log(colors.bgGrey(<span class="hljs-string">'bgGrey'</span>));
<span class="hljs-built_in">console</span>.log(colors.reset(<span class="hljs-string">'reset'</span>));
<span class="hljs-built_in">console</span>.log(colors.bold(<span class="hljs-string">'bold'</span>));
<span class="hljs-built_in">console</span>.log(colors.dim(<span class="hljs-string">'dim'</span>));
<span class="hljs-built_in">console</span>.log(colors.italic(<span class="hljs-string">'italic'</span>));
<span class="hljs-built_in">console</span>.log(colors.underline(<span class="hljs-string">'underline'</span>));
<span class="hljs-built_in">console</span>.log(colors.inverse(<span class="hljs-string">'inverse'</span>));
<span class="hljs-built_in">console</span>.log(colors.hidden(<span class="hljs-string">'hidden'</span>));
<span class="hljs-built_in">console</span>.log(colors.strikethrough(<span class="hljs-string">'strikethrough'</span>));
<span class="hljs-built_in">console</span>.log(colors.rainbow(<span class="hljs-string">'rainbow'</span>));
<span class="hljs-built_in">console</span>.log(colors.zebra(<span class="hljs-string">'zebra'</span>));
<span class="hljs-built_in">console</span>.log(colors.america(<span class="hljs-string">'america'</span>));
<span class="hljs-built_in">console</span>.log(colors.trap(<span class="hljs-string">'trap'</span>));
<span class="hljs-built_in">console</span>.log(colors.random(<span class="hljs-string">'random'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将它们丢到 <code>test</code> 中，执行 <code>npm run test</code>，得到花里花哨的打印：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7a8fb78964348dcb8973e6f84452daa~tplv-k3u1fbpfcp-watermark.image" alt="colors-02.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3"><a name="user-content-chapter-four" id="user-content-chapter-four" href="https://juejin.cn/post/undefined"></a>四 重写 console.log</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6974542964764704782#chapter-one">返回目录</a></p>
</blockquote>
<p>OK，在上面我们已经华丽呼哨了，每次打印如果都要引用一遍 <code>colors</code> 那就有点说不过去啦。</p>
<p>所以咱们重写 <code>console.log</code>，这样只要有地方用到它了我们就有彩虹色了！</p>
<blockquote>
<p>base/getType.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@name <span class="hljs-variable">getType</span></span>
 * <span class="hljs-doctag">@description </span>获取类型
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string|object&#125;</span> </span>param 传入的变量
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> getType = (param: string): <span class="hljs-function"><span class="hljs-params">string</span> =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.prototype.toString.call(param).slice(<span class="hljs-number">8</span>, -<span class="hljs-number">1</span>);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>base/console.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> colors <span class="hljs-keyword">from</span> <span class="hljs-string">'colors'</span>;
<span class="hljs-keyword">import</span> &#123; getType &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./getType'</span>;

<span class="hljs-comment">// 打印索引</span>
<span class="hljs-keyword">let</span> consoleIndex = <span class="hljs-number">1</span>;

<span class="hljs-comment">// 重写 console.log</span>
<span class="hljs-keyword">const</span> log = <span class="hljs-built_in">console</span>.log;
<span class="hljs-built_in">console</span>.log = <span class="hljs-function">(<span class="hljs-params">...args: any</span>) =></span> &#123;
  log(<span class="hljs-string">`\n---<span class="hljs-subst">$&#123;consoleIndex++&#125;</span>---`</span>);
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < args.length; i++) &#123;
    <span class="hljs-keyword">const</span> arg = args[i];
    <span class="hljs-keyword">if</span> ([<span class="hljs-string">'String'</span>, <span class="hljs-string">'Number'</span>, <span class="hljs-string">'Boolean'</span>].includes(getType(arg))) &#123;
      log(colors.rainbow(<span class="hljs-built_in">String</span>(arg)));
    &#125; <span class="hljs-keyword">else</span> &#123;
      log(arg);
    &#125;
  &#125;
&#125;;

<span class="hljs-comment">// 重写 console.error</span>
<span class="hljs-keyword">const</span> error = <span class="hljs-built_in">console</span>.error;
<span class="hljs-built_in">console</span>.error = <span class="hljs-function">(<span class="hljs-params">...args: any</span>) =></span> &#123;
  log(<span class="hljs-string">`\n---<span class="hljs-subst">$&#123;consoleIndex++&#125;</span>---`</span>);
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < args.length; i++) &#123;
    <span class="hljs-keyword">const</span> arg = args[i];
    <span class="hljs-keyword">if</span> ([<span class="hljs-string">'String'</span>, <span class="hljs-string">'Number'</span>, <span class="hljs-string">'Boolean'</span>].includes(getType(arg))) &#123;
      error(colors.red(<span class="hljs-built_in">String</span>(arg)));
    &#125; <span class="hljs-keyword">else</span> &#123;
      error(arg);
    &#125;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 <code>src/index.ts</code> 中引用这个重写的 <code>console.ts</code>，这样全局就可以使用到了：</p>
<blockquote>
<p>src/index.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> program <span class="hljs-keyword">from</span> <span class="hljs-string">'commander'</span>;
<span class="hljs-keyword">import</span> common <span class="hljs-keyword">from</span> <span class="hljs-string">'./common'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'./base/console'</span>;

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
  .action(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'There is jsliang?'</span>, <span class="hljs-literal">true</span>);
    <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'随便报个错，表明它有问题'</span>);
  &#125;);

program.parse(process.argv);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时候运行 <code>npm run test</code> 打印效果为：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/200ac1e4d7ba4693b91731540357d060~tplv-k3u1fbpfcp-watermark.image" alt="colors-03.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>其实彩虹色看起来太花里胡哨了，但是暂时这边不更改吧，小伙伴们可以自行更换颜色</p>
</blockquote>
<p>那么，花里花哨的接入就完毕了，虽然都是 API 复制粘贴工程师，但是做下装饰搞好看一点还是可以有的~</p>
<p>下一篇见！</p>
<h2 data-id="heading-4"><a name="user-content-chapter-five" id="user-content-chapter-five" href="https://juejin.cn/post/undefined"></a>五 参考文献</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6974542964764704782#chapter-one">返回目录</a></p>
</blockquote>
<ul>
<li><a href="https://github.com/Marak/colors.js" target="_blank" rel="nofollow noopener noreferrer">GitHub：Marak/colors.js</a></li>
<li><a href="https://tools.kalvinbg.cn/txt/ascii" target="_blank" rel="nofollow noopener noreferrer">Kalvin 在线工具</a></li>
<li><a href="https://www.wncx.cn/ascii/" target="_blank" rel="nofollow noopener noreferrer">ASCII 字形生成器</a></li>
</ul>
<hr>
<p><strong>不折腾的前端，和咸鱼有什么区别！</strong></p>
<blockquote>
<p>jsliang 的文档库由 <a href="https://github.com/LiangJunrong" target="_blank" rel="nofollow noopener noreferrer">梁峻荣</a> 采用 <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="nofollow noopener noreferrer">知识共享 署名-非商业性使用-相同方式共享 4.0 国际 许可协议</a> 进行许可。<br>基于 <a href="https://github.com/LiangJunrong/document-library" target="_blank" rel="nofollow noopener noreferrer">github.com/LiangJunron…</a> 上的作品创作。<br>本许可协议授权之外的使用权限可以从 <a href="https://creativecommons.org/licenses/by-nc-sa/2.5/cn/" target="_blank" rel="nofollow noopener noreferrer">creativecommons.org/licenses/by…</a> 处获得。</p>
</blockquote></div>  
</div>
            