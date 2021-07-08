
---
title: '通过 Quill API 实现对编辑器内容的完全控制（附有查找替换功能的实现）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74049dabc1c4a07bf4f0ece127f9ef8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 15:39:39 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74049dabc1c4a07bf4f0ece127f9ef8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevui.design%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://devui.design/" ref="nofollow noopener noreferrer">DevUI</a> 是一款面向企业中后台产品的开源前端解决方案，它倡导<code>沉浸</code>、<code>灵活</code>、<code>至简</code>的设计价值观，提倡设计者为真实的需求服务，为多数人的设计，拒绝哗众取宠、取悦眼球的设计。如果你正在开发 <code>ToB</code> 的<code>工具类产品</code>，DevUI 将是一个很不错的选择！</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74049dabc1c4a07bf4f0ece127f9ef8~tplv-k3u1fbpfcp-watermark.image" alt="Kagol.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以下文章和本文相关，也许你也会喜欢：</p>
<p><a href="https://juejin.cn/post/6844904073620094990" target="_blank" title="https://juejin.cn/post/6844904073620094990">《现代富文本编辑器Quill的模块化机制》</a></p>
<p><a href="https://juejin.cn/post/6966993945973194765" target="_blank" title="https://juejin.cn/post/6966993945973194765">《Quill富文本编辑器的实践》</a></p>
<p><a href="https://juejin.cn/post/6968104416784171039" target="_blank" title="https://juejin.cn/post/6968104416784171039">《如何将龙插入到编辑器中？》</a></p>
<p><a href="https://juejin.cn/post/6968616701709516836" target="_blank" title="https://juejin.cn/post/6968616701709516836">《今天是儿童节，整个贪吃蛇到编辑器里玩儿吧》</a></p>
<p><a href="https://juejin.cn/post/6844904145145741326" target="_blank" title="https://juejin.cn/post/6844904145145741326">《现代富文本编辑器Quill的内容渲染机制》</a></p>
<p><a href="https://juejin.cn/post/6976023288753586184" target="_blank" title="https://juejin.cn/post/6976023288753586184">《Quill基本使用和配置》</a></p>
<h1 data-id="heading-0">引言</h1>
<p>这是深入浅出 Quill 系列的第2篇。</p>
<p><a href="https://juejin.cn/post/6976023288753586184" target="_blank" title="https://juejin.cn/post/6976023288753586184">上一篇</a>我们介绍了 Quill 的基本使用和配置，相信大家能够使用 Quill 搭建一个简单的富文本编辑器啦。</p>
<p>不过实际的业务场景可能更复杂，有更多定制的需求，Quill 能否满足呢？</p>
<p>Quill 是一款 API 驱动的富文本编辑器，它的内容可以通过API实现完全的掌控，我们一起来看看吧。</p>
<h1 data-id="heading-1">1 对内容的控制</h1>
<p>富文本编辑器最基本的操作就是对内容的<code>增</code>/<code>删</code>/<code>改</code>/<code>查</code>，比如：</p>
<ul>
<li>在编辑器某处增加一些文本</li>
<li>选中编辑器中的一部分内容，将其删除</li>
<li>选中一部分文本，给它添加某种格式</li>
<li>获取其中一部分内容，对其进行转换</li>
</ul>
<p>以上操作直接通过键盘和鼠标很容易操作，但是通过 API 如何实现呢？</p>
<h2 data-id="heading-2">1.1 删</h2>
<p>先看<code>删</code>的部分，通过<code>deleteText()</code>方法实现，该方法主要有两个入参：</p>
<ul>
<li>index 从哪儿删除</li>
<li>length 删除多少内容</li>
</ul>
<p>比如我想把下面的<code>Hello </code>删除：</p>
<pre><code class="copyable">this.quill.deleteText(0, 6);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8acfa089096476c98cb94897de5c00d~tplv-k3u1fbpfcp-watermark.image" alt="删除内容.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>又比如我想删除编辑器里的所有内容，但我们不知道里面一共有多少内容，是不是需要一个一个数一下呢？</p>
<p>其实是不需要的，Quill 提供了一个查询编辑器总字符数的方法<code>getLength()</code>（后面介绍<code>查</code>的部分也会讲到）。</p>
<p>所以删除所有内容也很简单：</p>
<pre><code class="copyable">this.quill.deleteText(0, this.quill.getLength());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有一种常见的情况，就是我们想删除编辑器中选中的内容，这要如何实现呢？</p>
<p>Quill 提供了一个获取编辑器选区的方法<code>getSelection()</code>（后面介绍<code>对选区的控制</code>时会讲到）可以轻松实现：</p>
<pre><code class="copyable">// 获取选区内容所在的index和length
const &#123; index, length &#125; = this.quill.getSelection();

this.quill.deleteText(index, length);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/312b4fdaaca64b9d862557708807d479~tplv-k3u1fbpfcp-watermark.image" alt="删除选中内容.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>是不是非常方便呢？</p>
<h2 data-id="heading-3">1.2 查</h2>
<p>再来看<code>查</code>的部分，Quill 托管了编辑器里所有的内容，因此它对里面的内容了如指掌，Quill 知道：</p>
<ul>
<li>指定位置有什么内容</li>
<li>有多少内容</li>
<li>它的格式是什么</li>
</ul>
<p>可以使用<code>getText()</code>方法获取纯文本内容，它的使用方式和前面介绍过的<code>deleteText()</code>类似：</p>
<pre><code class="copyable">// 获取指定位置的文本
this.quill.getText(0, 6);

// 不传入任何参数，可以获取全部文本
this.quill.getText();

// 获取选中文本
const &#123; index, length &#125; = this.quill.getSelection();
this.quill.getText(index, length);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>都知道有什么内容了，拿到内容的长度就很简单了：</p>
<pre><code class="copyable">const length = this.quill.getText().length;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Quill 提供了一个简便的方法<code>getLength()</code>，可以直接拿到全部文本的长度：</p>
<pre><code class="copyable">const length = this.quill.getLength();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要获取选中文本的长度，可以使用之前介绍过的<code>getSelection()</code>方法：</p>
<pre><code class="copyable">const length = this.quill.getSelection().length;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">1.3 增</h2>
<h3 data-id="heading-5">1.3.1 插入文本</h3>
<p>往编辑器里增加格式化的内容是最常见的需求，Quill 针对该场景提供了非常丰富的 API，最基础的就是<code>insertText()</code>方法。</p>
<p>该方法既可以增加纯文本，又可以增加带格式的文本。</p>
<p>插入纯文本需要传入两个参数：</p>
<ul>
<li>index 从哪个位置插入文本</li>
<li>text 插入什么文本</li>
</ul>
<pre><code class="copyable">this.quill.insertText(0, 'DevUI 是一款面向企业中后台产品的开源前端解决方案');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>插入带格式的文本需要额外传入两个参数：</p>
<ul>
<li>format 格式的名字</li>
<li>value 格式的值</li>
</ul>
<p>比如我想在当前光标后面插入一个带超链接的<code>DevUI</code>：</p>
<pre><code class="copyable">const range = this.quill.getSelection();
if (range) &#123;
  this.quill.insertText(range.index, 'DevUI', 'link', 'https://devui.design/');
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11990f6f23ea4329870b25abb5160b0b~tplv-k3u1fbpfcp-watermark.image" alt="插入带格式的文本.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">1.3.2 插入嵌入内容</h3>
<p>插入嵌入内容的方法<code>insertEmbed()</code>，相信大家都很熟悉了，我在之前的</p>
<ul>
<li><a href="https://juejin.cn/post/6966993945973194765" target="_blank" title="https://juejin.cn/post/6966993945973194765">《Quill富文本编辑器的实践》</a></li>
<li><a href="https://juejin.cn/post/6968104416784171039" target="_blank" title="https://juejin.cn/post/6968104416784171039">《如何将龙插入到编辑器中？》</a></li>
<li><a href="https://juejin.cn/post/6968616701709516836" target="_blank" title="https://juejin.cn/post/6968616701709516836">《今天是儿童节，整个贪吃蛇到编辑器里玩儿吧》</a></li>
</ul>
<p>三篇文章中多次使用过这个API。</p>
<p>这个方法和<code>insertText()</code>的区别在于没有第二个参数，因为它不需要插入文本。</p>
<p>比如插入B站风格的分割线：</p>
<pre><code class="copyable">const index = this.quill.getSelection().index;
this.quill.insertEmbed(index, 'divider', &#123;
  url: 'assets/images/divider.png',
  width: '660px',
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/512f46d819d64d1b9f696067a56b1b83~tplv-k3u1fbpfcp-watermark.image" alt="B站风格的分割线.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>比如插入龙：</p>
<pre><code class="copyable">const index = this.quill.getSelection().index;
this.quill.insertEmbed(index, 'dragon', &#123;
  id: 'canvas-dragon',
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77522d808a1a4e1fbdf7014052c68e0a~tplv-k3u1fbpfcp-watermark.image" alt="插入龙.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>比如插入贪吃蛇小游戏：</p>
<pre><code class="copyable">const index = this.quill.getSelection().index;
this.quill.insertEmbed(index, 'snake', &#123;
  id: 'canvas-snake',
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/258ba882baa644e4b2cc799da233152d~tplv-k3u1fbpfcp-watermark.image" alt="插入贪吃蛇小游戏.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">1.3.3 用纯文本替换现有内容</h3>
<p>这两个方法都是在现有内容的基础上新增文本。</p>
<p>如果要直接用新的内容替换现有文本，要怎么做呢？</p>
<p>使用以下两个<code>set</code>方法即可：</p>
<ul>
<li>setText 设置纯文本</li>
<li>setContents 设置带格式的文本</li>
</ul>
<p><code>setText()</code>方法只有一个参数：</p>
<ul>
<li>text 需要插入的纯文本</li>
</ul>
<pre><code class="copyable">this.quill.setText('Hello DevUI!');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果<code>text</code>参数传入空字符串，则会清空编辑器内容：</p>
<pre><code class="copyable">this.quill.setText('');
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">1.3.4 用 delta 数据替换现有内容</h3>
<p><code>setContents()</code>方法非常强大，可以使用指定的 delta 数据来渲染编辑器的内容。</p>
<p>比如我们想要将当前富文本的内容变成一个贪吃蛇游戏：</p>
<pre><code class="copyable">this.quill.setContents([
  &#123; insert: &#123; snake: &#123; id: 'snake' &#125; &#125; &#125;
]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般 delta 数据会存储在数据库中，使用 delta 来初始化编辑器内容时，可以使用该方法。</p>
<h2 data-id="heading-9">1.4 改</h2>
<p><code>setContents()</code>方法还有一个兄弟叫<code>updateContents()</code>，这俩兄弟本领都非常强。</p>
<p><code>updateContents()</code>方法可以使用 delta 更新编辑器中的指定内容。</p>
<p>比如我想把选中的<code>Quill</code>内容变成<code>DevUI</code>，并加上超链接，不使用<code>updateContents()</code>方法的情况下，我们需要调用多个方法：</p>
<pre><code class="copyable">const &#123; index, length &#125; = this.quill.getSelection();
this.quill.deleteText(index, length);
this.quill.insertText(index, 'DevUI', 'link', 'https://devui.design/');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们再来看看使用<code>updateContents()</code>方法如何实现：</p>
<pre><code class="copyable">this.quill.updateContents([
  &#123; retain: index &#125;,
  &#123; delete: length &#125;,
  &#123; insert: 'DevUI', attributes: &#123; link: 'https://devui.design/' &#125; &#125;
]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两种方法的效果一样，但是后者只需要调用一个方法。</p>
<blockquote>
<p><code>updateContents()</code>方法可以赋予我们通过操作 delta 这个 JSON 数据来操作编辑器内容，而不用手动调用 API 去改变内容，在某些场景下这将是一个极大的便利。</p>
</blockquote>
<h1 data-id="heading-10">2 对格式的控制</h1>
<h2 data-id="heading-11">2.1 删</h2>
<p>除了可以删除编辑器内容外，我们可能还需要清除某部分内容的格式，清除格式可以使用<code>removeFormat()</code>方法，该方法的使用方式和<code>deleteText()</code>几乎是一样的，不再赘述。</p>
<pre><code class="copyable">// 清除指定位置和长度的文本的格式
this.quill.removeFormat(0, 6);

// 清除全部文本的格式
this.quill.removeFormat(0, this.quill.getLength());

// 清除选中文本的格式
const &#123; index, length &#125; = this.quill.getSelection();
this.quill.removeFormat(index, length);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">2.2 查</h2>
<h3 data-id="heading-13">获取单一格式</h3>
<p><code>getText()</code>方法只能拿到纯文本，并不知道里面有什么格式，要想获取指定文本的格式，可以使用<code>getFormat()</code>方法，使用方式都一样。</p>
<pre><code class="copyable">// 获取选中文本的格式
const &#123; index, length &#125; = this.quill.getSelection();
const format = this.quill.getFormat(index, length);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比如粗体的格式：</p>
<pre><code class="copyable">&#123; bold: true &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>超链接的格式：</p>
<pre><code class="copyable">&#123; link: "https://juejin.cn/post/6976023288753586184" &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15e4eebd9269482e9d323bffc89c258a~tplv-k3u1fbpfcp-watermark.image" alt="获取格式.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">获取 Delta 格式</h3>
<p>不过<code>getFormat()</code>方法只能拿到单一的格式，如果想知道指定内容的全部格式信息，需要使用一个更加强大的API：<code>getContents()</code>，这个方法能获取内容的 delta 形式，而 delta 格式不仅描述了有什么内容，还描述了这些内容的格式是什么。</p>
<p>比如以下选中的内容，我们看看它的内容和格式是什么。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d883a95524ce4189bc9f200fb94ae854~tplv-k3u1fbpfcp-watermark.image" alt="delta格式.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>调用<code>getContents()</code>方法：</p>
<pre><code class="copyable">const &#123; index, length &#125; = this.quill.getSelection();
const contents = this.quill.getContents(index, length);
console.log('contents:', contents);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打印了以下信息：</p>
<pre><code class="copyable">&#123;
  ops: [
    &#123; insert: '删除内容' &#125;,
    &#123; attributes: &#123; header: 2 &#125;, insert: '\n' &#125;, // 标题二格式
    &#123; insert: '先看' &#125;,
    &#123; attributes: &#123; code: true &#125;, insert: '删' &#125;, // 行内代码格式
    &#123; insert: '的部分，通过' &#125;,
    &#123; attributes: &#123; code: true &#125;, insert: 'deleteText()' &#125;, // 行内代码格式
    &#123; insert: '方法实现，该方法主要有两个入参：\nindex 从哪儿删除' &#125;,
    &#123; attributes: &#123; list: 'bullet' &#125;, insert: '\n' &#125;, // 无序列表格式
    &#123; insert: 'length 删除多少内容' &#125;,
    &#123; attributes: &#123; list: 'bullet' &#125;, insert: '\n' &#125;, // 无序列表格式
    &#123; insert: '比如我想把下面的' &#125;,
    &#123; attributes: &#123; code: true &#125;, insert: 'Hello ' &#125;, // 行内代码格式
    &#123; insert: '删除：\nthis.quill.deleteText(0, 6);' &#125;,
    &#123; attributes: &#123; 'code-block': true &#125;, insert: '\n' &#125;, // 代码块格式
    &#123; insert: '\n' &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从以上 delta 结构我们很容易得出编辑器内容的格式信息：</p>
<ul>
<li><code>删除内容</code>是标题二格式</li>
<li><code>删</code>/<code>deleteText()</code>/<code>Hello </code>是行内代码格式</li>
<li><code>index 从哪儿删除</code>和<code>length 删除多少内容</code>是无序列表格式</li>
<li><code>this.quill.deleteText(0, 6);</code>是代码块格式</li>
<li>其他内容都是纯文本格式</li>
</ul>
<p>是不是一目了然呢？</p>
<h2 data-id="heading-15">2.3 增</h2>
<p>除了删除和查找格式之外，还可以设置格式，Quill提供了3个设置格式的方法：</p>
<ul>
<li>format(format, value) 设置选中文本的格式</li>
<li>formatLine(index, length, format, value) 设置行（块级）格式</li>
<li>formatText(index, length, format, value) 设置指定位置的文本格式</li>
</ul>
<pre><code class="copyable">// 设置选中文本为粉色
this.quill.format('color', 'pink');

// 设置第10-20个字符为粉色
this.quill.formatText(10, 10, 'color', 'pink');

// 设置第一行为有序列表
this.quill.formatLine(0, 1, 'list', 'ordered');
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-16">3 对选区的控制</h1>
<h2 data-id="heading-17">3.1 查</h2>
<h3 data-id="heading-18">3.1.1 查询选区信息</h3>
<p>获取当前选区或光标的方法<code>getSelection()</code>，我们在前面已经使用过多次，说明这个方法是一个非常实用的高频方法。</p>
<p>该方法不需要传入参数，返回当前选区信息：</p>
<ul>
<li>index 选区开始位置</li>
<li>length 选区长度</li>
</ul>
<pre><code class="copyable">&#123;
  index: 0,
  length: 3
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果只有光标，没有选择任何内容，则返回的<code>length</code>为<code>0</code>。</p>
<p>如果编辑器没有光标，则返回<code>null</code>。</p>
<h3 data-id="heading-19">3.1.2 查询文本相对定位位置</h3>
<p>除了查询选区位置和长度，还可以使用<code>getBounds()</code>方法查询指定位置的文本在编辑器容器中的相对定位位置，该方法有两个入参：</p>
<ul>
<li>index 选区开始位置</li>
<li>length 选区长度</li>
</ul>
<p>比如我想看下编辑器开头的三个字符的位置：</p>
<pre><code class="copyable">const bounds = this.quill.getBounds(0, 3);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>返回结果：</p>
<pre><code class="copyable">&#123;
  bottom: 49.100006103515625
  height: 22.5
  left: 18
  right: 66
  top: 26.600006103515625
  width: 48
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">3.2 增</h2>
<p>除了查看当前选区信息，我们还可以使用<code>setSelection()</code>方法手动设置选区和光标位置，该方法有两个参数：</p>
<ul>
<li>index 选区开始位置</li>
<li>length 选区长度</li>
</ul>
<p>如果只设置第一个参数，将只设置光标位置，不选中文本：</p>
<pre><code class="copyable">// 将光标定位到第10个字符后面
this.quill.setSelection(10);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两个参数同时设置将选中文本：</p>
<pre><code class="copyable">// 选中第1到10个字符
this.quill.setSelection(0, 10);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>选区和光标是后续操作的基础，所以该方法和<code>getSelection()</code>方法一样，是一个非常常用的方法。</p>
<h1 data-id="heading-21">4 小结</h1>
<p>我们做一个简单的小结：</p>
<ul>
<li>对内容的控制
<ul>
<li>删除内容 deleteText(index, length)</li>
<li>查找内容 getText(index, length)</li>
<li>获取编辑器内容长度 getLength()</li>
<li>插入文本内容 insertText(index, text, format, value)</li>
<li>插入嵌入内容 insertEmbed(index, format, value)</li>
<li>使用纯文本替换内容 setText(text)</li>
<li>用 delta 数据替换现有内容 setContents(delta)</li>
<li>用 delta 更新内容 updateContents(delta)</li>
</ul>
</li>
<li>对格式的控制
<ul>
<li>删除格式 removeFormat(index, length)</li>
<li>查找单一格式 getFormat(index, length)</li>
<li>获取 Delta 格式 getContents(index, length)</li>
<li>设置选中文本的格式 format(format, value)</li>
<li>设置行格式 formatLine(index, length, format, value)</li>
<li>设置文本格式 formatText(index, length, format, value)</li>
</ul>
</li>
<li>对选区的控制
<ul>
<li>获取选区/光标信息 getSelection()</li>
<li>获取指定文本的相对定位 getBounds(index, range)</li>
<li>设置选区/光标  setSelection(index, range)</li>
</ul>
</li>
</ul>
<h1 data-id="heading-22">5 案例：查找替换功能</h1>
<p>最后我们用一个查找替换的案例来温故下之前介绍过的 API。</p>
<pre><code class="copyable">// 待查找文本
const str = 'Quill';
const length = str.length;

// 匹配目标文本的正则
const reg = new RegExp(str, 'g');

let match;
while ((match = reg.exec(this.quill.getText())) !== null) &#123;
  // 目标文本在文档中的位置
  const index = match.index;
  
  // 匹配到目标文本之后，我们可以对该文本做高亮或替换的处理
  
  // 高亮
  this.quill.formatText(index, length, 'background', '#ef0fff');
  
  // 替换
  this.quill.deleteText(index, length);
  this.quill.insertText(index, 'DevUI', 'link', 'https://devui.design/');
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>查找替换</code>动画演示效果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7443a9a2594a4f5fa44b5f076d990705~tplv-k3u1fbpfcp-watermark.image" alt="查找替换.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-23">小结</h1>
<p>本文主要介绍了 Quill 的常用API，以及每个API的使用场景。</p>
<p>后续将介绍更多关于 Quill 的实践，关注 DevUI 不迷路🦌。</p>
<p>欢迎加DevUI小助手微信：devui-official，一起讨论Angular技术和前端技术。</p>
<p>欢迎关注我们<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevui.design%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://devui.design/" ref="nofollow noopener noreferrer">DevUI</a>组件库，点亮我们的小星星🌟：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdevcloudfe%2Fng-devui" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/devcloudfe/ng-devui" ref="nofollow noopener noreferrer">github.com/devcloudfe/…</a></p>
<p>也欢迎使用DevUI新发布的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevui.design%2Fadmin%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://devui.design/admin/" ref="nofollow noopener noreferrer">DevUI Admin</a>系统，开箱即用，10分钟搭建一个美观大气的后台管理系统！</p>
<h1 data-id="heading-24">加入我们</h1>
<p>我们是DevUI团队，欢迎来这里和我们一起打造优雅高效的人机设计/研发体系。招聘邮箱：<a href="https://link.juejin.cn/?target=mailto%3Amuyang2%40huawei.com" target="_blank" title="mailto:muyang2@huawei.com" ref="nofollow noopener noreferrer">muyang2@huawei.com</a>。</p>
<p>文/DevUI Kagol</p>
<p>往期文章推荐</p>
<p><a href="https://juejin.cn/post/6976023288753586184" target="_blank" title="https://juejin.cn/post/6976023288753586184">《Quill基本使用和配置》</a></p>
<p><a href="https://juejin.cn/post/6844904073620094990" target="_blank" title="https://juejin.cn/post/6844904073620094990">《现代富文本编辑器Quill的模块化机制》</a></p>
<p><a href="https://juejin.cn/post/6966993945973194765" target="_blank" title="https://juejin.cn/post/6966993945973194765">《Quill富文本编辑器的实践》</a></p>
<p><a href="https://juejin.cn/post/6968104416784171039" target="_blank" title="https://juejin.cn/post/6968104416784171039">《如何将龙插入到编辑器中？》</a></p>
<p><a href="https://juejin.cn/post/6968616701709516836" target="_blank" title="https://juejin.cn/post/6968616701709516836">《今天是儿童节，整个贪吃蛇到编辑器里玩儿吧》</a></p></div>  
</div>
            