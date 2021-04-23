
---
title: 'Tailwindcss发布了2.1版本，是时候_入手_了'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=143'
author: 掘金
comments: false
date: Thu, 22 Apr 2021 17:28:21 GMT
thumbnail: 'https://picsum.photos/400/300?random=143'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>Tailwindcss v2.1发布，最大的更新就是把原来的<code>jit</code>插件以一种<code>mode</code>的方式合并到主题程序中了。也就是说Tailwindcss添加了一种编译模式。当然除了这个，还有其他有趣的功能和特性。下面一起看看。</p>
<h2 data-id="heading-1">just in time模式</h2>
<h3 data-id="heading-2">老版本思路</h3>
<p>Tailwindcss是通过读取配置文件，预生成所有的css类，提供给开发者使用，然后打包的时候，通过<code>postCss</code>的<code>pure</code>插件，来<code>tree-shaking</code>清除那些未使用的css类，从而大大简化最终生成的css文件。</p>
<p>听起来好像没什么问题，但是你真的使用过Tailwindcss的话，那就会发现，开发环境中，生成的类可能有3566K左右，当变更配置文件的时候，尤其是当你配置很多颜色或者变体<code>variant</code>的时候，重新生成可能很长时间，几秒到几十秒不等。</p>
<blockquote>
<p>Tailwind can take 3–8s to initially compile using our CLI, and upwards of 30–45s in webpack projects because webpack struggles with large CSS files.</p>
</blockquote>
<p>这显然是不能接受的。</p>
<h3 data-id="heading-3">jit思路</h3>
<p>新推出的<code>jit</code>模式，采用的思路是，不预先生成任何css类，你要用到什么，再生成什么，真正的按需生成，just in time。这个模式的编译时间超级快。</p>
<blockquote>
<p>This library can compile even the biggest projects in about 800ms (with incremental rebuilds as fast as 3ms), no matter what build tool you're using.</p>
</blockquote>
<h3 data-id="heading-4">使用</h3>
<p>使用起来非常简单，只需要在原来的配置文件添加一个配置项即可。然后就可以开始享受丝滑的编译速度了。</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// tailwind.config.js</span>
  <span class="hljs-built_in">module</span>.exports = &#123;
   <span class="hljs-attr">mode</span>: <span class="hljs-string">'jit'</span>,
    <span class="hljs-attr">purge</span>: [
      <span class="hljs-comment">// ...</span>
    ],
    <span class="hljs-attr">theme</span>: &#123;
      <span class="hljs-comment">// ...</span>
    &#125;
    <span class="hljs-comment">// ...</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意</strong>：由于<code>jit</code>模式需要扫描文件来按需生成CSS类，所以必须要通过<code>purge</code>配置项指定需要扫描的文件夹，否则就不会生成任何CSS类。</p>
<h2 data-id="heading-5">变体（variant）开箱即用</h2>
<p>很多变体如<code>focus-visible</code> <code>active</code> <code>disabled</code>等是没有默认开启的，因为变体会大大增加css文件体积，所以很多时候你需要手动去开启各种你需要用到的变体。由于是按需生产的，你可以很轻松的开箱即用任何变体，比如<code>sm:hover:active:disabled:opacity-75</code>，再也不用担心体积和速度问题。</p>
<h2 data-id="heading-6">所写即所得</h2>
<p>不用自定义CSS，就可以生成样式。在使用Tailwindcss的过程中，如果一些特殊的地方需要用到特殊的尺寸，比如<code>margin-top:-113px</code>，你不需要再去为他自定义一个CSS类，由于是按需生产的，你可以用方括号表示法来生成一个类，比如<code>top-[-113px]</code>，<code>md:top-[-113px]</code></p>
<h2 data-id="heading-7">没有环境差异</h2>
<p>由于是按需生成CSS类，所以你在开发环境生成的跟生产环境的是一样的，因为不需要清除未使用的样式,所以不用担心意外清除导致生产环境不一致的情况。</p>
<h2 data-id="heading-8">总结</h2>
<p>新版本很大程度提升了开发效率，这更加是时候“入手”Tailwindcss了。</p>
<p>我是一个Tailwindcss的粉丝，当我看到它的时候，我感觉打开了新世界的大门，看到了很多可玩性。如果你也是，那么欢迎一起讨论研究。</p>
<p>那些没有真正写过Tailwindcss的人，如果你们在徘徊犹豫，或者嗤之以鼻，就像作者说的，给它一个机会，去用一下。再多的文章，说再多的好处，都不及你真正上手把玩一下。</p>
<blockquote>
<p>I’ve written a few thousand words on why traditional “semantic class names” are the reason CSS is hard to maintain, but the truth is you’re never going to believe me until you actually try it. If you can suppress the urge to retch long enough to give it a chance, I really think you'll wonder how you ever worked with CSS any other way.</p>
</blockquote>
<p>在2.0+版本的时候，我尝试去翻译它的官方文档，进行到一半的时候，出了2.1版本。。。</p>
<p><a href="http://tailwindcss.cool/" target="_blank" rel="nofollow noopener noreferrer">翻译到一半的中文文档v2.0.2</a></p>
<p>如果能帮助到人，我会继续进行下去，并且同步2.1版本。Just let me know!</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            