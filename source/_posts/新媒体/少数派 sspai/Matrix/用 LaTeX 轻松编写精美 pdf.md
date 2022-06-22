
---
title: '用 LaTeX 轻松编写精美 pdf'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://cdn.sspai.com/2022/06/17/article/c9c83497c2d820f21e65ddfc0745aeae?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
author: 少数派 sspai
comments: false
date: Fri, 17 Jun 2022 13:07:41 GMT
thumbnail: 'https://cdn.sspai.com/2022/06/17/article/c9c83497c2d820f21e65ddfc0745aeae?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
---

<div>   
<div class="articleWidth-content" data-v-557a067a><div class="update-wrap" data-v-557a067a></div><div class="content wangEditor-txt minHeight" data-v-557a067a><h2>LaTeX 不只是写数学公式</h2><p>你可能了解过 LaTeX 是一种编写数学公式的语言，它是内嵌在 Markdown 中的，但即使你平时没有写数学公式的需求，也可以用它来编写 pdf，我大学里社会实践的策划书都是使用 LaTeX 编译制作的。</p><h2>LaTeX 相比 Word 的好处</h2><p>LaTeX 相比 Word 就好比 Markdown 之于富文本，只要用语句声明这里有一个什么样的样式，就能编译出应该有的样式，让你能够专注于内容。</p><p>其中感受最明显的一点是大纲的制作，在 LaTeX 中，标注了层级后，就能用一句命令制作出点击可跳转的目录。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/06/17/article/c9c83497c2d820f21e65ddfc0745aeae?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="hyperref" data-original="https://cdn.sspai.com/2022/06/17/article/c9c83497c2d820f21e65ddfc0745aeae" referrerpolicy="no-referrer"></figure><p>这样的效果在 Word 里实现是非常麻烦的，并且由于这大纲是自动生成的，非常<strong>利于修改</strong>。</p><h2>LaTeX 编译 pdf 快速上手</h2><h3>文件格式</h3><p>纯文本文件的格式是 <code>.txt</code></p><p>Markdown 文件的格式是 <code>.md</code></p><p>LaTeX 文件的格式是 <code>.tex</code></p><p>其实它们都是纯文本，都能用文本编辑器打开，后缀名只是决定了打开它们的方式，在 Markdown 编辑器比如 Obsidian 中可以编译 <code>.md</code>，同样，要通过 <code>.tex</code> 生成 pdf，需要 LaTeX 的编译器。</p><p>接下来让我们来看一下怎么写 <code>tex</code> 文件吧。</p><h3>基本结构</h3><p>要想编译出 pdf，至少需要这么一个结构。</p><pre class="language-tex"><code>\documentclass&#123;ctexart&#125;
% 导言区
\begin&#123;document&#125;
% pdf 呈现的内容
\end&#123;document&#125;</code></pre><p>LaTeX 中的命令都用 <code>\</code> 作为开头。</p><p><code>\begin&#123;&#125;</code> 和 <code>\end&#123;&#125;</code> 创建了一个环境，在这里，这个环境叫做 <code>document</code>，意味着你写在这里面的内容会被编译到 pdf 中。</p><p>而在 <code>\begin&#123;document&#125;</code> 环境之前的内容，不会被编译到 pdf 中，但用于写对 pdf 整体进行设置的语句。</p><p><code>\documentclass&#123;&#125;</code> 是设置文档的类型，只要在你的 pdf 中需要用到中文，就把文档类型设置成 <code>ctexart</code> 就好了。</p><h3>基本信息</h3><p>了解了基本结构以后，我们来对文档进行一些基本的设置。</p><ul><li><code>\author&#123;&#125;</code>：作者</li><li><code>\title&#123;&#125;</code>：标题</li><li><code>\date&#123;&#125;</code>：日期</li></ul><p>有了这些基本的信息以后，我们就可以为 pdf 创建内容了。</p><p>在内容区域写下 <code>\maketitle</code></p><pre class="language-tex"><code>\documentclass&#123;ctexart&#125;

\author&#123;唐夕洲&#125;
\title&#123;用 $\LaTeX$ 轻松编写精美 pdf&#125;
\date&#123;&#125;

\begin&#123;document&#125;

\maketitle

\end&#123;document&#125;</code></pre><p>pdf 已经出现内容啦！</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/06/17/article/1cc3f452b2bd7509f6aeb4c7f12c2101?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="出现内容" data-original="https://cdn.sspai.com/2022/06/17/article/1cc3f452b2bd7509f6aeb4c7f12c2101" referrerpolicy="no-referrer"></figure><h3>大纲结构</h3><p>在 Markdown 中，我们用 <code>#</code> 的个数来声明这是一个几级标题。</p><pre class="language-md"><code># 一级标题
## 二级标题
### 三级标题</code></pre><p>在 LaTeX 中是这样写的</p><pre class="language-tex"><code>%...
\begin&#123;document&#125;

\section&#123;一级标题&#125;
    %一些内容
    \subsection&#123;二级标题&#125;
        \subsubsection&#123;三级标题&#125;
            %一些内容

\end&#123;document&#125;</code></pre><p>缩进并不是必须的，但这是一个良好的习惯。</p><p>声明了各个层级的标题后，我们就可以制作大纲了。</p><p>在 <code>\maketitle</code> 下方写上 <code>\tableofcontents</code></p><pre class="language-tex"><code>%...
\begin&#123;document&#125;

\maketitle
\tableofcontents

\section&#123;一级标题&#125;
    %一些内容
    \subsection&#123;二级标题&#125;
        \subsubsection&#123;三级标题&#125;
            %一些内容

\end&#123;document&#125;</code></pre><p>就会得到这样的效果</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/06/17/article/5609e45ee8c1f31fef6b616c06c4bb6a?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="目录" data-original="https://cdn.sspai.com/2022/06/17/article/5609e45ee8c1f31fef6b616c06c4bb6a" referrerpolicy="no-referrer"></figure><p>但你会发现目录周围并没有红色边框，也就是说不能点击跳转。</p><p>这时候只要在导言区写上 <code>\usepackage&#123;hyperref&#125;</code> 就可以了。</p><pre class="language-tex"><code>\documentclass&#123;ctexart&#125;

\usepackage&#123;hyperref&#125;

\begin&#123;document&#125;

\tableofcontents

%...

\end&#123;document&#125;</code></pre><h3>引入包</h3><p>LaTeX 自带的功能是有限的，如果想要扩展功能，就要通过 <code>\usepackage&#123;&#125;</code> 来引入相应的包。</p><p>你也可以理解为使用插件，但不需要安装什么东西，只需要写出对应的包的名字就好了。</p><p>到此为止，你已经可以做出有模有样的 pdf 了，并且实现这一切并不需要不停移动鼠标调整样式，只需要写下几句命令就可以了！</p><h2>结语</h2><p>虽然 LaTeX 包罗万象，但整体看来，无非就是一些命令而已，当想要做出什么效果时，在搜索引擎里搜索一下就能得到答案了。</p><p>其实我写的远不止这些，但最终决定将很多内容删去，只留下最基础的部分，我不希望自己只是将其他人已经写过的内容再写一遍，我希望能让这篇文章看起来没有任何技术成分，为你打开 LaTeX 大门。</p></div><div class="update-details-wrap" data-v-557a067a></div><!----></div><div style="border:1px solid transparent;" data-v-557a067a></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-557a067a><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>3</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>5</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-3409" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90%E7%94%A8%20LaTeX%20%E8%BD%BB%E6%9D%BE%E7%BC%96%E5%86%99%E7%B2%BE%E7%BE%8E%20pdf%E3%80%91LaTeX%E4%B8%8D%E5%8F%AA%E6%98%AF%E5%86%99%E6%95%B0%E5%AD%A6%E5%85%AC%E5%BC%8F%E4%BD%A0%E5%8F%AF%E8%83%BD%E4%BA%86%E8%A7%A3%E8%BF%87LaTeX%E6%98%AF%E4%B8%80%E7%A7%8D%E7%BC%96%E5%86%99%E6%95%B0%E5%AD%A6%E5%85%AC%E5%BC%8F%E7%9A%84%E8%AF%AD%E8%A8%80%EF%BC%8C%E5%AE%83%E6%98%AF%E5%86%85%E5%B5%8C%E5%9C%A8Markdown%E4%B8%AD%E7%9A%84%EF%BC%8C%E4%BD%86%E5%8D%B3%E4%BD%BF%E4%BD%A0%E5%B9%B3%E6%97%B6%E6%B2%A1%E6%9C%89%E5%86%99%E6%95%B0%E5%AD%A6%E5%85%AC%E5%BC%8F%E7%9A%84%E9%9C%80%E6%B1%82%EF%BC%8C%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=https%3A%2F%2Fcdn.sspai.com%2F2022%2F06%2F17%2Ffd92e5d1d2b9969d2de112a7a3f99175.png%3FimageMogr2%2Fauto-orient%2Fquality%2F95%2Fthumbnail%2F!1420x708r%2Fgravity%2FCenter%2Fcrop%2F1420x708%2Finterlace%2F1&appkey=3196502474#" target="_blank"><i class="iconfont iconfont-weibo-simple right-16"></i></a><span><div role="tooltip" id="el-popover-868" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><span class="el-popover__reference-wrapper"><i class="iconfont iconfont-wechat-simple right-16"></i></span></span><a href="https://twitter.com/share?text=%E3%80%90%E7%94%A8%20LaTeX%20%E8%BD%BB%E6%9D%BE%E7%BC%96%E5%86%99%E7%B2%BE%E7%BE%8E%20pdf%E3%80%91LaTeX%E4%B8%8D%E5%8F%AA%E6%98%AF%E5%86%99%E6%95%B0%E5%AD%A6%E5%85%AC%E5%BC%8F%E4%BD%A0%E5%8F%AF%E8%83%BD%E4%BA%86%E8%A7%A3%E8%BF%87LaTeX%E6%98%AF%E4%B8%80%E7%A7%8D%E7%BC%96%E5%86%99%E6%95%B0%E5%AD%A6%E5%85%AC%E5%BC%8F%E7%9A%84%E8%AF%AD%E8%A8%80%EF%BC%8C%E5%AE%83%E6%98%AF%E5%86%85%E5%B5%8C%E5%9C%A8Markdown%E4%B8%AD%E7%9A%84%EF%BC%8C%E4%BD%86%E5%8D%B3%E4%BD%BF%E4%BD%A0%E5%B9%B3%E6%97%B6%E6%B2%A1%E6%9C%89%E5%86%99%E6%95%B0%E5%AD%A6%E5%85%AC%E5%BC%8F%E7%9A%84%E9%9C%80%E6%B1%82%EF%BC%8C%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="iconfont iconfont-twitter-simple right-16"></i></a></div></div><span class="el-popover__reference-wrapper"><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            