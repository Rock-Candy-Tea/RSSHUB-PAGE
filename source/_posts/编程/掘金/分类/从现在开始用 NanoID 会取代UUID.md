
---
title: '从现在开始用 NanoID 会取代UUID'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39964584ef5b426bac1a7e7c60d8ea77~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 22:15:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39964584ef5b426bac1a7e7c60d8ea77~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>如果你的项目有生成唯一 <code>key</code> 或者使用 <code>uuid</code> 的场合，那么从现在开始，请使用 NanoID。之前在文章《<a href="https://juejin.cn/post/6972916469969453070#heading-2" target="_blank">分享8个可以提高开发效率的JavaScript库</a>》介绍过 <a href="https://github.com/ai/nanoid/" target="_blank" rel="nofollow noopener noreferrer">NanoID</a> 。NanoID 是一个创建唯一 <code>key</code> 的轻量级的脚本库，在过去有类似需求首先想到的是 uuid ，与其相比 <a href="https://www.npmjs.com/package/nanoid" target="_blank" rel="nofollow noopener noreferrer">NanoID</a> 要小得多。</p>
<pre><code class="copyable">const &#123; nanoid &#125; = require("nanoid");

const key = nanoid();
console.log(key); // U6XRwZsfcDuexQ7m55qdy
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从 npmjs.com 信息来看，NanoID 一周的下载量达到<strong>上千万</strong>，此外，NanoID 比 UUID 小了将近 7 岁，而且它的 GitHub 星数已经超过 UUID 了。下图是两个脚本库的趋势数据图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39964584ef5b426bac1a7e7c60d8ea77~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>查看网站数据可以点击这里：<a href="https://www.npmtrends.com/nanoid-vs-uuid" target="_blank" rel="nofollow noopener noreferrer">www.npmtrends.com/nanoid-vs-u…</a>。</p>
<p>从上面的数据已经足以说明问题了，下面介绍一下 NanoID 的特点。</p>
<h3 data-id="heading-0">体积小</h3>
<p>和 UUID 相比，NanoID 的大小要小大概 <strong>4.5</strong> 倍，压缩大小只有 <strong>108</strong> 字节，并且没有任何依赖关系。</p>
<h3 data-id="heading-1">更安全</h3>
<p>在大部分随机生成器使用的是不安全的随机数 <code>Math.random()</code>。而 <code>NanoID</code> 使用 <a href="https://nodejs.org/api/crypto.html" target="_blank" rel="nofollow noopener noreferrer">crypto module</a> 。</p>
<p>此外，NanoID 在 ID 生成器的实现过程中使用了自己的称为统一算法的算法，而不是使用随机的字母表。</p>
<h3 data-id="heading-2">更高效</h3>
<p>NanoID 比 UUID 快 60%，UUID 的字符表使用 36 个不同字符，而 NanoID 只使用了 21 个字符。</p>
<p>此外，NanoID 还支持 14 种不同的编程语言，它们分别是：</p>
<blockquote>
<p>C#、C++、Clojure 和 ClojureScript、Crystal、Dart & Flutter、Deno、Go、Elixir、Haskell、Janet、Java、Nim、Perl、PHP、带字典的 Python、Ruby、Rust、Swift</p>
</blockquote>
<h3 data-id="heading-3">兼容性</h3>
<p>NanoID 还支持 PouchDB、CouchDB WebWorkers、Rollup 以及 React 和 Reach-Native 等库。</p>
<h3 data-id="heading-4">灵活性</h3>
<p>NanoID 的另一个特点是灵活性，它允许开发人员使用自定义字母表。可以更改文字或 id 的大小，如下所示：</p>
<pre><code class="copyable">const &#123; customAlphabet &#125; = require("nanoid");
const nanoid = customAlphabet("devpointDEV123456789", 6);
const nid = nanoid();
console.log(nid); // 4it6tp
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">局限性</h3>
<p>根据 StackOverflow 中的许多专家意见，使用 NanoID 没有明显的缺点或限制。</p>
<p>可读性方面（不便于记忆）应该算是 NanoID 的主要缺点，另外，NanoID 不是连续的，因此不能作为数据库表的主键。</p>
<h3 data-id="heading-6">总结</h3>
<p>NanoID正逐渐成为Javascript中最流行的唯一id生成器，大多数开发人员更愿意选择它而不是 UUID 。在考虑到它的体积小、URL 友好性、安全性和高效，因此建议从现在开始在项目中使用 NanoID 取代UUID 。</p></div>  
</div>
            