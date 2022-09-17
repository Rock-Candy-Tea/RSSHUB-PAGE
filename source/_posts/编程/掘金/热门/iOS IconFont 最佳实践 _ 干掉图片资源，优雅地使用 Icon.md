
---
title: 'iOS IconFont 最佳实践 _ 干掉图片资源，优雅地使用 Icon'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5012168ac5f94f6cb52efe83f810b848~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
author: 掘金
comments: false
date: Sun, 04 Sep 2022 09:20:44 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5012168ac5f94f6cb52efe83f810b848~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第2篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" target="_blank" title="https://s.juejin.cn/ds/jooSN7t">点击查看活动详情</a></p>
<h2 data-id="heading-0">前言</h2>
<p>作为大前端开发者一定经常使用很多小图标，使用小图标不可避免的要导入图片资源，图片资源又要考虑倍率、尺寸和颜色，总之体验不佳。为了解决这个问题 Iconfont 应运而生，不过原生使用体验还是不够好，本文目的就是优化开发体验。</p>
<h2 data-id="heading-1">什么是 IconFont</h2>
<blockquote>
<p><strong>官方：</strong> 阿里妈妈 MUX 倾力打造的矢量图标管理、交流平台。 设计师将图标上传到 iconfont 平台，用户可以自定义下载多种格式的icon，平台也可将图标转换为字体，便于前端工程师自由调整与调用。</p>
</blockquote>
<p>可喜的是 Iconfont 是<strong>免费</strong>的，且<strong>支持单色和多色</strong>。设计师可以开发自己的单色和多色图库，并以私有方式管理，供公司内部使用。</p>
<p><strong>单色示例：</strong> <img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5012168ac5f94f6cb52efe83f810b848~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<strong>多色示例：</strong> <img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca7b96ae5c544d8788dedd2cce12ea1e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">为什么要使用 IconFont</h2>
<p><strong>使用图片资源的痛点：</strong></p>
<ul>
<li>在不同设备上图片倍率不同，需要导入 2 倍和 3 倍图</li>
<li>图片资源比较大，不利于包大小控制</li>
<li>同一图标不同颜色需要多张图</li>
<li>图片资源管理起来容易显得混乱</li>
</ul>
<p><strong>IconFont 特点：</strong></p>
<ul>
<li>Icon 以自定义字体的形式定义在字体文件里</li>
<li>字体是矢量的，这意味着无论 Icon 的 size 是 <code>20 * 20</code> 还是 <code>2000 * 2000</code> 都不会失真</li>
<li>像使用任何系统提供的字体一样，字体可以设置任意颜色</li>
<li>文件体积很小</li>
</ul>
<p><strong>通过以上分析很容易得出结论：使用 IconFont 利益极大，不使用 IconFont 危害极大</strong></p>
<h2 data-id="heading-3">Iconfont 使用方式</h2>
<p><strong>iOS 端官方推荐使用方式：</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e11bcc63b0b34d74970bd28ec0049e32~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<strong>我的第一感觉是有些怪怪的，可也确实合理，这么用又心有不甘。</strong></p>
<p><strong>痛点梳理：</strong></p>
<ul>
<li>导入字体需要把字体相关文件导入工程，还要修改工程 info.plist 文件，这对多模块共享字体极不友好。更无法接受的是这基本无法对字体进行版本管理</li>
<li>创建 Font 时需要硬编码字体名称，对我来说不太能接受</li>
<li>label.text 赋值时是 unicode 码，可读性极低，完全不能接受</li>
<li>更多时候我们需要的是一张图片，使用 UILabel 显示一张图片不符合我们的常识和习惯</li>
</ul>
<h2 data-id="heading-4">Iconfont 最佳实践</h2>
<p>本着 IconFont 是个好东西，不能因为它当前存在的缺点而放弃它，应该尽量让它变得更加完美的宗旨，对使用方式进行了一些优化。</p>
<p>以上所有痛点都有办法解决：</p>
<ul>
<li>导入字体一定要把字体文件导入主工程并修改 info.plist 文件吗？<strong>并不是</strong></li>
<li>创建 Font 时需要硬编码字体名称吗？<strong>并不是</strong></li>
<li>label.text 赋值时一定要是 unicode 码吗？是的，不过我们可以<strong>给它起个有意义的名字</strong>。</li>
<li>更多时候我们需要的是一张图片，可以<strong>把 Icon 转换为一张图片</strong></li>
</ul>
<p>问题分析透彻了，那就开始寻找条件是否满足。</p>
<ol>
<li>字体是可以动态加载的，可以通过以下代码实现字体动态加载</li>
<li>字体名称硬编码显然可以轻松解决</li>
<li>观察 <code>iconfont.json</code> 文件，证明 label.text 赋值时可以给 unicode 码起个有意义的名称<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69a5c8f82eb840189a7d248d34880965~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>可以把 Icon 转换为一张图片</li>
</ol>
<p><strong>至此，以上所有痛点均已完美解决，下面是完整方案：</strong></p>
<ol>
<li>新建 CocoaPods 模块，用于多模块共享字体，<strong>命令</strong>：<code>pod lib create BBIconFont</code></li>
<li>新建 json2swift.py 脚本文件，内容如下：<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28efe6f9a41c4b37a7915c04873da2be~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>把下载来的 <code>iconfont</code> 文件夹拖入 <code>Assets</code> 目录 <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/232dd844ca274fbf81470707bb831296~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>新增文件 <code>UIFont+BBIconFont.swift</code>，内容如下：<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b40619bd3a64696aee548ae33e7e9a5~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>新增文件 <code>UIImage+BBIconFont.swift</code>，内容如下：<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d5f1ece41e84e73807c59076f823f28~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>执行脚本 <code>python json2swift.py</code></li>
<li>脚本成功执行后会生成文件 <code>BBIconNames.swift</code>，内容如下：<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3245d54f527c41d58e242a32a45ca58b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></li>
</ol>
<p><strong>业务代码中使用方式如下：</strong></p>
<pre><code class="hljs language-swift copyable" lang="swift"><span class="hljs-comment">// 导入 BBIconFont 模块</span>
<span class="hljs-keyword">import</span> BBIconFont
​
<span class="hljs-comment">// 获取 UIImage 对象，可以用于任意合适的地方</span>
<span class="hljs-keyword">let</span> image <span class="hljs-operator">=</span> <span class="hljs-type">UIImage</span>.if_image(<span class="hljs-type">BBIconNames</span>.add <span class="hljs-keyword">as</span> <span class="hljs-type">NSString</span>)
<span class="hljs-comment">// 获取 UIImage 对象同时指定大小、颜色，可以用于任意合适的地方</span>
<span class="hljs-keyword">let</span> image <span class="hljs-operator">=</span> <span class="hljs-type">UIImage</span>.if_image(<span class="hljs-type">BBIconNames</span>.add <span class="hljs-keyword">as</span> <span class="hljs-type">NSString</span>, size: <span class="hljs-number">16</span>, color: .yellow)
​
<span class="hljs-comment">// 字体方式使用</span>
<span class="hljs-keyword">let</span> lable <span class="hljs-operator">=</span> <span class="hljs-type">UILabel</span>()
lable.font <span class="hljs-operator">=</span> <span class="hljs-type">UIFont</span>.if_iconFont(<span class="hljs-number">16</span>)
<span class="hljs-comment">// 纯 Icon</span>
lable.text <span class="hljs-operator">=</span> <span class="hljs-string">"后面是个 Iconfont 字符: <span class="hljs-subst">\(BBIconNames.add)</span>"</span>
lable.textColor <span class="hljs-operator">=</span> .yellow
​
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">小结</h2>
<p>通过我们的变通，最终可以像使用原生字体一样使用 IconFont，并能很好的对字体进行版本管理和共享。</p>
<p>最后给大家分享个观点：不要因为一个技术方案（大方向必须对，出发点是效能提升）当下的某些不完美而急于否定，而是应该首先思考能否让它变得更加完美。</p></div>  
</div>
            