
---
title: 'deno + Vite 会碰撞出什么样的火花呢？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1be8201f3b29417395390a7b3ab47359~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 04 Apr 2021 19:15:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1be8201f3b29417395390a7b3ab47359~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1be8201f3b29417395390a7b3ab47359~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>欢迎关注公众号「<strong>程序员自习室</strong>」，获取更多精彩文章，同时可加入微信学习群与更多精英前端一起交流学习！</p>
</blockquote>
<p>进入2021年后，前端最火的是啥呢？我觉得就是尤大开发的<a href="https://cn.vitejs.dev/" target="_blank" rel="nofollow noopener noreferrer">Vite</a> ，这是它官网的 <code>slogan</code> ,号称：<strong>“下一代前端开发与构建工具”</strong> ，够狂！ <code>webpack</code> 肯定瑟瑟发抖了！</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3eefd25871d544b68acc1a478d3cdaab~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>对于不了解 <a href="https://cn.vitejs.dev/" target="_blank" rel="nofollow noopener noreferrer">Vite</a> 的读者，我们先大概简单介绍一下, <strong>同时建议你去看看文档，学习了解一下</strong>！</p>
<p><code>Vite</code> (法语意为 "快速的"，发音 <code>/vit/</code>) 是一种新型前端构建工具，能够显著提升前端开发体验。 特点就是<strong>快，超级快！</strong> 它具有一个高度依赖 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules" target="_blank" rel="nofollow noopener noreferrer">原生 ES 模块</a>的开发服务器，以提供速度惊人的 <a href="https://cn.vitejs.dev/guide/features.html#hot-module-replacement" target="_blank" rel="nofollow noopener noreferrer">模块热更新（HMR）</a>。使其如此快速的原因之一是，它一次只能按需处理一个文件，而不是构建整个项目。</p>
<p>默认情况下，它可以处理 <code>TypeScript</code>，<code>JSX</code> 和 <code>CSS</code> 模块，所以你可以开箱即用。如果您想要构建用于生产的应用程序，它也可以轻松搞定，不做过多介绍了。</p>
<p>关于本文标题提到的 <a href="https://doc.deno.land/" target="_blank" rel="nofollow noopener noreferrer">deno</a> ，我们也做一个简单的介绍。</p>
<p>了解 <code>deno</code> 的读者（不了解的同学别慌，推荐大家阅读<a href="https://deno-tutorial.js.org/" target="_blank" rel="nofollow noopener noreferrer">Deno 钻研之术</a>）知道， <code>deno</code> 是 <code>JavaScript</code> 和 <code>TypeScript</code> 的安全运行时。换句话说，它可以在没有浏览器的情况下执行 <code>JavaScript</code> 和 <code>TypeScript</code>。它之所以说是安全的，是因为执行的代码运行在一个对系统的访问受到限制的环境中。如果要使用某些功能，则需要为其提供显式访问。你把理解成一个浏览器环境也ok!</p>
<p>好了，关于<code>deno</code>和<code>Vite</code>,我相信大家有个简单的认识了，想要进一步学习的可以访问官网学习，本文不做赘述了！</p>
<h2 data-id="heading-0">deno 和 Vite 为何会有碰撞呢？</h2>
<p>deno是一个js运行时，Vite 是一个前端构建工具，那么他们有啥联系呢？容我慢慢道来！</p>
<p>众所周知，<code>deno</code> 在诞生之日起，就不喜欢<code>npm</code>，处理第三方依赖项采用的是原生支持的方式。</p>
<p>在 <code>deno</code> 中，当你想要使用一个 <code>package</code> 包时候，必须使用与ES浏览器相同的方式，通过 <code>import</code> 一个 <code>URL</code> 来实现。差不多是这样:</p>
<pre><code class="copyable">import * as R from 'https://cdn.skypack.dev/ramda@0.27.1';
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然这是没啥问题的，对于单个文件脚本来说是完美的。</p>
<p>对于更复杂的项目，我们可以约定将所有内容放入<code>deps.ts</code> 文件中，这不是最好的办法，但是也可以。</p>
<p>还有一个实验功能，称为 <a href="https://deno.land/manual@v1.7.5/linking_to_external_code/import_maps#import-maps" target="_blank" rel="nofollow noopener noreferrer">import-maps</a> ，看起来效果会更好些。</p>
<blockquote>
<p>从1.8.0版本开始，deno中的 import-maps 才是稳定的。</p>
</blockquote>
<p>反正不管怎么样，我现在就想要下面这种方式，写惯了 <code>React</code>项目，这样才最爽！</p>
<pre><code class="copyable">import * as R from 'ramda';
<span class="copy-code-btn">复制代码</span></code></pre>
<p>想要使用 <code>npm</code>包管理器来获取 <code>ramda</code>。但是在 deno 中这就是一种罪过。这个时候试试尤大的<code>Vite</code>是不是可以帮到我呢？</p>
<h2 data-id="heading-1">Vite 助力 deno</h2>
<p>假设我们要使用 <code>ramda</code>。 同样，我们要使用 <code>npm</code> 来获取源代码，因此我们执行下面操作。</p>
<pre><code class="copyable">npm install ramda@0.27.1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在让我们创建脚本。 我们将其称为 <code>main.js</code>。</p>
<pre><code class="copyable">import * as R from 'ramda';​const increment = R.map(x => x + 1);​console.log(increment([1, 2, 3]));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们来安装 <code>vite</code>。</p>
<pre><code class="copyable">npm install -D vite@2.1.5
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再创建一个文件 <code>index.html</code>, 用来测试效果。</p>
<pre><code class="copyable"><!DOCTYPE html><html lang="en"><head>  <meta charset="UTF-8">  <title>test</title></head><body>  <script type="module" src="/main.js"></script></body></html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在使用vite。</p>
<pre><code class="copyable">npx vite
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果一切顺利，则应该在屏幕上显示此内容。</p>
<pre><code class="copyable">  vite v2.1.5 dev server running at:​  > Local:    http://localhost:3000/  > Network:  http://172.20.10.11:3000/  > Network:  http://192.168.138.17:3000/​  ready in 3724ms.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>访问 <a href="http://localhost:3000/" target="_blank" rel="nofollow noopener noreferrer">http://localhost:3000/</a> ，打开浏览器的 console, 你应该会得到这样子：</p>
<p><img alt="image-20210404183312799" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8fe2a28d358483f955d34d3a4c56245~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">[ 2, 3, 4 ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很好。现在我们怎么样在 <code>deno</code> 中得到这个结果呢？</p>
<p>我说过，<code>deno</code> 可以理解为一个浏览器。我们知道浏览器是从URL中拉取资源。在你开始使用 <code>deno</code>之前，如果你不想 "污染 "系统中的全局缓存，我建议设置 <code>DENO_DIR</code> 环境变量。在 mac 中，你可以这样做:</p>
<pre><code class="copyable">export DENO_DIR="$PWD/.cache"
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>windows用户，对不起啦，我也不会，你们自己百度吧~</p>
</blockquote>
<p>接下来，我们首先直接运行<code>main.js</code></p>
<pre><code class="copyable">deno run main.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果报错：</p>
<pre><code class="copyable">error: relative import path "ramda" not prefixed with / or ./ or ../ Imported from "file:///Users/wangweidong/V2021/denoAndVite/main.js"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>直接在文件系统中运行 <code>main.js</code>，而是运行 <code>Vite</code> 为我们起的本地服务的 <code>main.js</code>。</p>
<pre><code class="copyable">deno run "http://localhost:3000/main.js"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果，没有报错，我们成功了！</p>
<pre><code class="copyable">Download http://localhost:3000/main.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们已经成功地在<code>deno</code>环境中使用了<code>npm</code>包。但不要高兴太早，我们再运行一次。没有 <code>"Download http://..."</code>。</p>
<p>现在在 <code>main.js</code>中改变一些内容，再次执行 <code>main.js</code> 。</p>
<pre><code class="copyable">import * as R from 'ramda';​const increment = R.map(x => x + 1);-- console.log(increment([1, 2, 3]));+ console.log('hello');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是没有收到 hello 呢？现在你想知道为什么吗?</p>
<p>因为 <code>deno</code> 是从服务器(localhost)上抓取 <code>main.js</code>，所以它将源码保存在缓存文件夹(DENO_DIR)中，除非<code>url</code>改变，否则它不会再尝试下载。</p>
<p>我们该如何解决这个问题呢？有以下两个办法：</p>
<p>1、使用了一个<code>querystring t</code> 来附加一个随机数到 <code>url</code>上，这样每次执行命令时都会创建一个 "新" <code>url</code>。</p>
<pre><code class="copyable">deno run "http://localhost:3000/main.js?t=$RANDOM"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、使用参数 <code>--reload</code></p>
<pre><code class="copyable">deno run --reload "http://localhost:3000/main.js"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到现在，你已经拥有了一个带有 <code>Vite</code> 和 <code>deno</code> 的开发环境。</p>
<p>以防万一，有必要说一下。即使我们可以从 <code>npm</code> 下载任何我们想要的东西，也不意味着它能在 deno 上工作。有时候某个包就是不兼容，也没办法！</p>
<h2 data-id="heading-2">总结</h2>
<p>这个探索性的实验虽然是有效的，但是我不鼓励大家使用这个组合来开生产应用，如果是个人实验性的学习项目完全可以的！</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            