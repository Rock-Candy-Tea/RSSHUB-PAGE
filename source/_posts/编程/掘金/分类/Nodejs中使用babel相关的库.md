
---
title: 'Nodejs中使用babel相关的库'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/377fabb7a4bc4422bff9a60d44872354~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 17 Jul 2021 22:34:42 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/377fabb7a4bc4422bff9a60d44872354~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">需求</h1>
<p>有 js 文件的内容如下</p>
<pre><code class="copyable">(function getApis() &#123;
  return &#123;&#125;;
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>客户端发来的请求如下</p>
<pre><code class="copyable">"/api/page2"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时候 mock 程序要自动生成的内容如下</p>
<pre><code class="copyable">(function getApis() &#123;
  return &#123;
    "/api/page2": &#123;
      body: &#123;
        status: 200,
        data: &#123;&#125;,
      &#125;,
    &#125;,
  &#125;;
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>减少复制粘贴的成本</p>
<h1 data-id="heading-1">衡量</h1>
<p>首先要定位到<code>getApis</code>这个函数，然后找到其<code>return</code>语句的<code>&#123;</code>位置，再插入值，能够解析 js 文件才够精准，自然想到了 babel</p>
<h1 data-id="heading-2">实现</h1>
<p><strong>获得 ast 抽象树</strong>
<code>cnpm install --save-dev @babel/parser </code></p>
<pre><code class="copyable">const babelParser = require("@babel/parser");
const ast = babelParser.parse(`
(function getApis() &#123;
  return &#123;&#125;;
&#125;)();

`);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>找一个在线网站观看结构,这很重要,列如:<a href="https://link.juejin.cn/?target=https%3A%2F%2Fastexplorer.net%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://astexplorer.net/" ref="nofollow noopener noreferrer">astexplorer.net/</a></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/377fabb7a4bc4422bff9a60d44872354~tplv-k3u1fbpfcp-watermark.image" alt="a.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>遍历节点</strong>
<code>cnpm install --save-dev @babel/traverse </code></p>
<pre><code class="copyable">const &#123; default: babelTraverse &#125; = require("@babel/traverse");
let pos = null;
babelTraverse(ast, &#123;
  FunctionExpression(path) &#123;
    if (path.node.id.name === "getApis") &#123;
      pos = path.node.body.body[0].argument.start + 1;
      path.skip();
    &#125;
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>FunctionExpression</code>这个是怎么确定的呢，ast 在输出的时候已经给到了</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9aa475bfbfc54dbdb08011470cc5e429~tplv-k3u1fbpfcp-watermark.image" alt="b.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过<code>path.node.id.name === "getApis"</code>确认这个是我们要找的函数
<code>pos</code>就是其返回语句&#123;后面的位置了</p>
<p><strong>插入新的内容</strong>
用到<code>@babel/types</code>有些麻烦，因为是插入内容，就直接操作字符串了，通过<code>prettier</code>格式化下代码，然后写入</p>
<pre><code class="copyable">      let content =
        mockFileStr.slice(0, pos) +
        `
        "$&#123;params.url&#125;":$&#123;JSON.stringify(
          params.defaultConfig.autoCreateSettings.getDefaultValues(),
          null,
          2
        )&#125;,
        ` +
        mockFileStr.slice(pos);
      fs.writeFileSync(
        path.resolve(__dirname, moclFilepath),
        prettier.format(content)
      );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完整的例子:<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxiaodun%2Fsf-mock%2Fblob%2Fmain%2Futils%2FeditJsUtils.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xiaodun/sf-mock/blob/main/utils/editJsUtils.js" ref="nofollow noopener noreferrer">github.com/xiaodun/sf-…</a></p>
<h1 data-id="heading-3">感触</h1>
<p>记得有一次电话面试被问到<code>babel</code>相关的问题，我就说是做代码转译的
对面表示这样很敷衍，至少要说出<code>@babel/core</code>这些库的作用啥的
我则是感觉莫名其妙，我了解这些东西这么详细干嘛，平时也用不到
不知他是基于什么想去了解的</p></div>  
</div>
            