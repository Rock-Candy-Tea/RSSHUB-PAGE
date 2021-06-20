
---
title: 'Tailwind CSS 2.2 发布，快速构建 UI 的 CSS 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4127'
author: 开源中国
comments: false
date: Sat, 19 Jun 2021 23:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4127'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Tailwind CSS 2.2 正式发布，该版本是有史以来功能最丰富的 Tailwind 版本之一，该版本更新内容如下：</p> 
<h3>全新改进的Tailwind CLI</h3> 
<p>我们以性能优先的思维方式从头开始重写了 Tailwind CLI 工具，同时还增加了对一堆新功能的支持：</p> 
<p><code>npx tailwindcss -o dist/tailwind.css --watch --jit --purge="./src/**/*.html"</code></p> 
<p>以下是一些亮点：</p> 
<ul> 
 <li>无需安装或配置——只需 npx tailwindcss -o output.css 就能从任何地方编译 Tailwind。甚至可以使用该 -jit 标志启用 JIT 模式并使用该 -purge 选项传入内容文件，而无需创建配置文件；</li> 
 <li>Watch 模式 —— 这样就可以在进行任何更改时自动重建 CSS；</li> 
 <li>JIT 性能优化 —— 由于我们的 CLI 是特定于 Tailwind 的，我们能够进行大量优化，使其成为在 JIT 模式下编译 CSS 的最快构建工具；</li> 
 <li>缩小支持 —— 现在可以使用 cssnano 通过添加 -minify 标志来缩小你的 CSS；</li> 
 <li>PostCSS 插件支持 —— 新的 CLI 将读取并尊重使用 postcss.config.js 文件配置的任何额外插件；</li> 
</ul> 
<p>它与以前的 CLI 完全兼容，因此如果您已经设置了任何脚本，您应该能够升级到 v2.2，而无需对脚本进行任何更改。</p> 
<h3><strong>伪元素变体前后</strong></h3> 
<p>此功能仅在 Just-in-Time 模式下可用；</p> 
<p>多年来很多用户一直想要这个功能，现在它终于来了！我们添加了对样式伪元素的第一方支持，例如<code>before</code>和<code>after</code>：</p> 
<p><code><div class="before:block before:bg-blue-500 after:flex after:bg-pink-300"></div></code></p> 
<p>我们会在用户使用 before 或 after 变体时自动设置 <code>content: ""</code> 以确保呈现元素，但用户可以使用 content 具有完全任意值支持的新实用程序覆盖它：</p> 
<p><code><div class="before:content-['hello'] before:block ..."></div></code></p> 
<p>用户甚至可以使用 CSS attr() 函数从属性中获取内容：</p> 
<p><code><div before="hello world" class="before:content-[attr(before)] before:block ..."></div></code></p> 
<p>当内容中有空格时，这会非常有用，因为在 CSS 类名称中不能使用空格。</p> 
<h3><strong>首字母/行变体</strong></h3> 
<p>此功能仅在 Just-in-Time 模式下可用；</p> 
<p>我们为<code>first-letter</code>和<code>first-line</code>伪元素添加了变体，因此您可以执行首字下沉之类的操作：</p> 
<pre><code><p class="first-letter:text-4xl first-letter:font-bold first-letter:float-left">
  The night was March 31, 1996, and it was finally time for Bret Hart to face off against Shawn
  Michaels in the long anticipated Iron Man match — a 60 minute war of endurance where the man who
  scored the most number of falls would walk away as the WWF World Heavyweight Champion.
</p>
</code></pre> 
<p>We've added a new <code>selection</code> variant that makes it super easy to style highlighted to match your design:</p> 
<h3><strong>选定的文本变体</strong></h3> 
<p>此功能仅在 Just-in-Time 模式下可用；</p> 
<p>我们添加了一个新的<code>selection</code>变体，使突出显示的样式变得非常容易以匹配设计：</p> 
<pre><code><p class="selection:bg-pink-200">
  After nearly a grueling hour of warfare with neither man scoring a fall, Hart locked in the
  Sharpshooter, his signature submission hold. As Michaels screamed in pain, the crowd were certain
  that Hart was about to walk away from WrestleMania XII as the still-World Heavyweight Champion.
</p>
</code></pre> 
<p>我们甚至以这样的方式构建了这个功能，它可以应用于父元素并向下级联，因此您可以通过将实用程序应用于正文来为整个站点设置高亮颜色：</p> 
<pre><code><body class="selection:bg-pink-200">
  <!-- ... -->
  <p>
    But Michaels didn't give up — he held on until the bell rang and the designated 60 minutes was
    up. Hart walked away content, thinking that without a clear winner, the title was his to hold.
    He was not prepared for what would happen next, when Gorilla Monsoon declared the match would
    continue under sudden death rules.
  </p>
</body>
</code></pre> 
<h3><strong>详尽的伪类支持</strong></h3> 
<p>此功能仅在 Just in Time 模式下可用；</p> 
<p>在这个版本中，我们基本上为每个我们能想到的缺失的伪类添加了变体：</p> 
<ul> 
 <li><code>only</code> <em>(only-child)</em></li> 
 <li><code>first-of-type</code></li> 
 <li><code>last-of-type</code></li> 
 <li><code>only-of-type</code></li> 
 <li><code>target</code></li> 
 <li><code>default</code></li> 
 <li><code>indeterminate</code></li> 
 <li><code>placeholder-shown</code></li> 
 <li><code>autofill</code></li> 
 <li><code>required</code></li> 
 <li><code>valid</code></li> 
 <li><code>invalid</code></li> 
 <li><code>in-range</code></li> 
 <li><code>out-of-range</code></li> 
</ul> 
<p>列表中个人最喜欢的是 <code>placeholder-shown</code> ——当与新的 siblings 选择器变体结合时，它可以做一些很酷的事情，比如浮动标签：</p> 
<pre><code><div class="relative">
  <input id="name" class="peer ...">
  <label for="name" class="peer-placeholder-shown:top-4 peer-focus:top-0 ...">
</div>
</code></pre> 
<hr> 
<h3><strong>修复和改进</strong></h3> 
<p>除了此版本引入的新功能外，我们还修复了一些可能困扰您的小问题。以下是自上次发布以来我们所做的修复和改进的列表：</p> 
<ul> 
 <li>JIT：支持应用重要的实用程序变体；</li> 
 <li>JIT：改进对 Svelte 类绑定的支持；</li> 
 <li>JIT：完善<code>calc</code>和 <code>var</code> 在任意值的支持</li> 
 <li>当转变不透明度时，转换<code>hsl</code> 颜色为<code>hsla</code> 而不是<code>rgba</code> ；</li> 
 <li>修复<code>backdropBlur</code>未生成；</li> 
 <li>改进 animation 值解析；</li> 
 <li>散列配置时忽略未知对象类型；</li> 
 <li>确保为具有 order-dependent 的实用程序的插件正确分组变体；</li> 
 <li>解决相对于<code>tailwind.config.js</code>而不是当前工作目录的清除路径；</li> 
 <li>JIT：当节点临时目录保存在与项目本身不同的驱动器上时修复临时文件存储；</li> 
 <li>支持 border-opacity 实用程序和默认<code>border</code>实用程序</li> 
 <li>JIT：修复扩展<code>@tailwind</code>指令的源映射</li> 
 <li>JIT：折叠相邻规则时忽略空格；</li> 
 <li>JIT：使用自定义分隔符时正确生成组父类；</li> 
 <li>JIT：修复多个<code>group</code>变体的错误堆叠；</li> 
 <li>JIT：修复由于保留未使用的上下文而导致的内存泄漏；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.tailwindcss.com%2Ftailwindcss-2-2" target="_blank">https://blog.tailwindcss.com/tailwindcss-2-2</a></p>
                                        </div>
                                      
</div>
            