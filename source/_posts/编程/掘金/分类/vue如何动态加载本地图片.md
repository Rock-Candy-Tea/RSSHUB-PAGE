
---
title: 'vue如何动态加载本地图片'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: '...'
author: 掘金
comments: false
date: Wed, 21 Jul 2021 22:53:32 GMT
thumbnail: '...'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>大家好，我是前端队长Daotin，想要获取更多前端精彩内容，关注我(全网同名)，解锁前端成长新姿势。</p>
<p>以下正文：</p>
<br>
<p>今天遇到一个在vue文件中引入本地图片的问题，于是有了这篇文章。</p>
<p>通常，我们的一个img标签在html中是这么写的：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"../images/demo.png"</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种写法只能引用<strong>相对路径下的图片</strong>。不能使用绝对路径。使用绝对路径的话，这类资源将会直接被拷贝，而不会经过 webpack 的处理。</p>
<p>如果src是变量的话，我们一般会在data中定一个变量src进行动态绑定。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"src"</span>></span>

//data中定义变量src
data() &#123;
  return &#123;
    src: '../images/demo.png' 
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>然而这时候，会发现这个时候图片并没有被加载出来，图片没有显示出来，通过查看发现这张图片的地址显示 <code>../images/demo.png</code> ，也就是说通过v-bind形式绑定的相对路径不会被webpack的<code>file-loader</code>处理，只会做简单的文本替换。</p>
<p>那怎么办呢？</p>
<h2 data-id="heading-0">解决方法</h2>
<p><strong>1、将图片转</strong>**<code>base64</code>**<strong>格式</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"data:image/png;base64,iVBYKIGloxxxxxxxxxxxxxxxxxxx..."</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>一般图片比较小的可以这么做，比如图标icon等，大小一般在10KB以内的。</p>
<p><strong>2、使用</strong>**<code>import</code>**<strong>引入图片</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"src"</span>></span>

//使用import引入
import img from '../images/demo.png'

//data中定义变量src
data() &#123;
  return &#123;
    src: img 
  &#125;
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3、使用</strong>**<code>require</code>**<strong>动态加载</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"src"</span>></span>

//data中定义变量src
data() &#123;
  return &#123;
    src: require('../images/demo.png')
  &#125;
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>4、引入</strong>**<code>publicPath</code>**<strong>并且将其拼接在路径中，实现引入路径的动态变动</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">:src</span>=<span class="hljs-string">"publicPath + 'images/demo.jpg'"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span> // √
// 编译后:
<span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"/foo/images/demo.jpg"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>:&#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> &#123;
          <span class="hljs-attr">publicPath</span>: process.env.BASE_URL,
        &#125;
    &#125;,
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>vue.config.js</code>中配置<code>publicPath</code>路径：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//vue.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">publicPath</span>:<span class="hljs-string">'/foo/'</span>,
    ...
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">结论</h2>
<p><strong>静态资源</strong>可以通过两种方式进行处理：</p>
<ul>
<li>
<p>在 JavaScript <code>被导入</code>或在 template/CSS 中通过<code>相对路径</code>被引用。这类引用会被 webpack 处理。</p>
</li>
<li>
<p>放置在 <code>public</code> 目录下或通过<code>绝对路径</code>被引用。这类资源将会直接被拷贝，而不会经过 webpack 的处理。</p>
</li>
</ul>
<h2 data-id="heading-2">原理</h2>
<p><strong>从相对路径导入</strong></p>
<p>当你在 JavaScript、CSS 或 <code>*.vue</code> 文件中使用相对路径 (必须以 <code>.</code> 开头) 引用一个静态资源时，该资源将会被包含进入 webpack 的依赖图中。</p>
<p>在其编译过程中，所有诸如 <code><img src="..."></code>、<code>background: url(...)</code> 和 CSS <code>@import</code> 的资源 URL <strong>都会被解析为一个模块依赖</strong>。</p>
<p>用<strong>绝对路径引入</strong>时，路径读取的是<code>public</code>文件夹中的资源，任何放置在 <code>public</code> 文件夹的静态资源都会被简单的复制到编译后的目录中，而不经过 webpack特殊处理。</p>
<p>当你的应用被部署在一个域名的根路径上时，比如<code>http://www.abc.com/</code>，此时这种引入方式可以正常显示但是如果你的应用没有部署在域名的根部，那么你需要为你的 URL 配置 publicPath 前缀，<code>publicPath</code> 是部署应用包时的基本 URL，需要在 <code>vue.config.js</code> 中进行配置。</p>
<h2 data-id="heading-3">扩展</h2>
<h3 data-id="heading-4">关于vue file-loader vs url-loader</h3>
<blockquote>
<p>如果我们希望在页面引入图片（包括img的src和background的url）。当我们基于webpack进行开发时，引入图片会遇到一些问题。</p>
</blockquote>
<blockquote>
<p>其中一个就是引用路径的问题。拿background样式用url引入背景图来说，我们都知道，webpack最终会将各个模块打包成一个文件，因此我们样式中的url路径是相对入口html页面的，而不是相对于原始css文件所在的路径的。这就会导致图片引入失败。这个问题是用<code>file-loader</code>解决的，file-loader可以解析项目中的url引入（不仅限于css），根据我们的配置，将图片拷贝到相应的路径，再根据我们的配置，修改打包后文件引用路径，使之指向正确的文件。</p>
</blockquote>
<blockquote>
<p>另外，如果图片较多，会发很多http请求，会降低页面性能。这个问题可以通过url-loader解决。url-loader会将引入的图片编码，生成dataURl。相当于把图片数据翻译成一串字符。再把这串字符打包到文件中，最终只需要引入这个文件就能访问图片了。当然，如果图片较大，编码会消耗性能。因此url-loader提供了一个limit参数，小于limit字节的文件会被转为DataURl，大于limit的还会使用file-loader进行copy。</p>
</blockquote>
<blockquote>
<p>**url-loader和file-loader是什么关系呢？**简答地说，url-loader封装了file-loader。url-loader不依赖于file-loader，即使用url-loader时，只需要安装url-loader即可，不需要安装file-loader，因为url-loader内置了file-loader。通过上面的介绍，我们可以看到，url-loader工作分两种情况：1.文件大小小于limit参数，url-loader将会把文件转为DataURL；2.文件大小大于limit，url-loader会调用file-loader进行处理，参数也会直接传给file-loader。因此我们只需要安装url-loader即可。</p>
</blockquote>
<p>原文链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fweizaiyes%2Fp%2F7461967.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/weizaiyes/p/7461967.html" ref="nofollow noopener noreferrer">www.cnblogs.com/weizaiyes/p…</a></p>
<h3 data-id="heading-5">关于background url引入图片时</h3>
<p>按照上面理论，如果我采用相对路径的方式引入图片的话，webpack会对其require处理。</p>
<pre><code class="copyable">background: url('./iphonexs.png') 0 0 no-repeat;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际上确实如此，我看到页面的背景变成：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">background</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">/resources/dist/images/iphonexs.a25bee7.png</span>) <span class="hljs-number">0</span> <span class="hljs-number">0</span> no-repeat;


<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是根据url-loader的配置处理的结果。</p>
<p>或者采用<code>动态style</code>的方式：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> 
  <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123;'background': 'url(' + require('./iphonexs.png') + ') 0 0 no-repeat'&#125;"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">Reference</h2>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcli.vuejs.org%2Fzh%2Fguide%2Fhtml-and-static-assets.html%23%25E5%25A4%2584%25E7%2590%2586%25E9%259D%2599%25E6%2580%2581%25E8%25B5%2584%25E6%25BA%2590" target="_blank" rel="nofollow noopener noreferrer" title="https://cli.vuejs.org/zh/guide/html-and-static-assets.html#%E5%A4%84%E7%90%86%E9%9D%99%E6%80%81%E8%B5%84%E6%BA%90" ref="nofollow noopener noreferrer">cli.vuejs.org/zh/guide/ht…</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000019495695" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000019495695" ref="nofollow noopener noreferrer">segmentfault.com/a/119000001…</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-cli%2Fissues%2F48" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue-cli/issues/48" ref="nofollow noopener noreferrer">github.com/vuejs/vue-c…</a></p>
</li>
</ul>
<p>（完）</p>
<p>如果有问题可以帮我指出，感谢！</p>
<p>--- End ---</p>
<p>你好，我是前端队长Daotin，专注分享前端与认知。希望在这里，和你分享我的前端学习和工作经验，记录个人成长。</p>
<p>想要获取更多前端精彩内容，关注我(全网同名)，解锁前端成长新姿势。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5dfac7cd028e4ec3b7091f1f322f132d~tplv-k3u1fbpfcp-watermark.image" alt="captain-gzh-new.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            