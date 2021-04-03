
---
title: '从零开始，编写一个 HomeBrew 缓存清理脚本'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://cdn.sspai.com/editor/u_xfzh5jgk/16172757734620.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
author: 少数派 sspai
comments: false
date: Thu, 01 Apr 2021 12:29:38 GMT
thumbnail: 'https://cdn.sspai.com/editor/u_xfzh5jgk/16172757734620.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
---

<div>   
<div class="articleWidth-content" data-v-e1f0100a><div class="content wangEditor-txt minHeight" data-v-e1f0100a><p>如果你正在使用 HomeBrew，并且没有使用过垃圾清理软件对其缓存进行过清理，不如通过 <code>open ~/Library/Caches/Homebrew</code> 命令打开 HomeBrew 缓存目录来看看。HomeBrew 虽然提供了 <code>brew cleanup</code> 工具来回收空间，但它只能清理历史版本备份，而不能清理下载缓存。经年累月的各种软件包可能堆积在这个目录中，一点一点蚕食宝贵的硬盘空间。</p><p>在过去，我一直使用 Setapp 中提供的 CleanMyMac X 来清理这些缓存。CleanMyMac X 作为 macOS 垃圾清理软件中的老牌劲旅，可以较好地识别并清理 HomeBrew 留下的垃圾。在退订 Setapp 后，我选择了 Lemon（腾讯柠檬清理）作为 CleanMyMac X 的替代品。Lemon 对国内（尤其是腾讯自家）app 的缓存识别以及清新的 UI 都让我十分满意，但它可以清理的缓存并不及 CleanMyMac X 来得丰富，而其中的一条「漏网之鱼」便是 HomeBrew。</p><p> </p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/editor/u_xfzh5jgk/16172757734620.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="Lemon 无法检测并清理 HomeBrew 缓存" data-original="https://cdn.sspai.com/editor/u_xfzh5jgk/16172757734620.png" referrerpolicy="no-referrer"><figcaption>Lemon 无法检测并清理 HomeBrew 缓存</figcaption></figure><p> </p><p>即使是 CleanMyMac X，在清理 HomeBrew 缓存时也稍显不足。垃圾清理软件的工作原理一般是扫描可能的缓存路径，并且对其中可以清理的目录进行移除。然而，HomeBrew 的缓存目录中除了占据较大空间的软件包之外，还有指令表等其他索引。虽然这些索引可以随时重建，但如果能够精准定位并移除要清理的文件，就能将重建缓存和目录结构的时间节约下来。接下来，我们将编写一个简单的 shell 脚本来完成这个任务。</p><h2>设计逻辑</h2><p>我们首先来观察 HomeBrew 缓存目录的结构。HomeBrew 缓存目录下存放了数个索引文件，以及指向所有 HomeBrew Formulae 软件包的符号链接（软链接）；<code>Cask</code> 目录则存放了指向所有 HomeBrew Cask 软件包的软链接。在 <code>downloads</code> 目录中，我们可以看到被指向的这些软件包。</p><p> </p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/editor/u_xfzh5jgk/16172800482896.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt="HomeBrew 缓存目录结构" data-original="https://cdn.sspai.com/editor/u_xfzh5jgk/16172800482896.png" referrerpolicy="no-referrer"><figcaption>HomeBrew 缓存目录结构</figcaption></figure><p> </p><p>软链接，或者叫符号链接，是文件系统中指向其他位置的一种特殊文件。不同于 macOS 中的「替身」和 Windows 中的「快捷方式」，对软链接的访问将直接指向原始文件或目录，因此可以通过软链接访问原始目录内的文件。值得一提的是「访达」会将软链接显示为「替身」，不过二者实际上有很大的不同。</p><p>我们发现这个目录下存放了指向两种类型、全部软件包的软链接。除了软链接和软件包之外，其他文件均不属于需要清理的垃圾。因此，我们只需找出所有的软链接，将它们所指的软件包和本身均删除，就能达到精确清理的目的。这样的清理不会影响未完成的下载，因为它们不会被创建软链接。我们将在后面介绍如何清理这类文件。</p><h2>编写代码</h2><p>通常，我们建议在 shell 脚本的第一行标明脚本所使用的 shell。macOS Big Sur 的默认 shell 为 zsh，而在这篇文章中我选择了使用更广泛的 bash。二者之间有些许语法差异，但本示例中的脚本不会涉及这些差异。</p><pre class="language-shell"><code>#!/bin/bash
</code></pre><p><code>#</code> 在 shell 脚本中用作单行注释的提示符，系统通过读取位于脚本开头的注释就可以识别脚本所使用的 shell。我们在脚本中可以用 <code>#</code> 来添加一些注释，有时也会被用来隐藏一些无用的代码。</p><p>接下来，我们需要找出所有的软链接。我们可以使用系统内置的 <code>find</code> 工具，向它传入 <code>-type l</code> 即可搜索指定目录下的软链接。HomeBrew 缓存目录中的软链接可以用以下命令导出：</p><pre class="language-shell"><code>find ~/Library/Caches/Homebrew -type l
</code></pre><p>在 bash 中，我们可以用 <code>$()</code> 来将指令的输出转换为变量。获取到所有软链接后，我们需要对其进行遍历并分别进行处理。bash 提供了 <code>for</code> 语句来进行遍历，在本例中用法如下：</p><pre class="language-shell"><code>for link in $(find ~/Library/Caches/Homebrew -type l)
do
    # 清理语句
done
</code></pre><p>在循环体中，符号链接的路径将被保存到局部变量 <code>$link</code>。我们可以用 <code>realpath</code> 工具来直接获取其指向的文件，而不需要自行编写相关的代码。这个工具可以用以下命令安装：</p><pre class="language-shell"><code>brew install realpath
</code></pre><p>不少垃圾清理软件都提供了直接删除和移动到废纸篓的选项。在 macOS 操作系统中提供了 <code>rm</code> 这一很多人都有所耳闻的命令，可以用来直接删除。而如果需要将文件移到废纸篓，我们可以用以下命令安装 <code>trash-cli</code> 工具：</p><pre class="language-shell"><code>brew install trash-cli
</code></pre><p>在本例中，所要删除的均是单个文件，而且不存在权限问题，因此调用方式非常简单。</p><pre class="language-shell"><code>rm <file>       # 直接删除
trash <file>    # 移到废纸篓
</code></pre><p>结合上述知识点，我们就能实现循环体了。我个人比较推荐将软链接文件直接删除，将软件包移到废纸篓，大家可以根据自己的需要进行选择。对于移到废纸篓的软件包，我们如果需要再次使用可以将其放回 <code>~/Library/Caches/Homebrew/downloads</code> 目录，HomeBrew 会自动识别并重新建立软链接。完整的脚本文件如下：</p><pre class="language-shell"><code>#!/bin/bash

for link in $(find ~/Library/Caches/Homebrew -type l)
do
    trash $(realpath $link)
    rm $link
done
</code></pre><p>其中尤其需要注意的是删除的顺序，必须先处理原始文件、再处理软链接，软链接被删除后将无法定位到原始文件。</p><h2>保存脚本</h2><p>我们可以将脚本保存为形如 <code>brew-clean.sh</code> 的脚本文件，这样就可以用 <code>bash brew-clean.sh</code> 来执行它。为了调用更方便，我们可以将其赋予可执行权限，这样就能直接地调用它。我们不妨将其命名为 <code>brew-clean</code>，我们的目标则是通过 <code>brew-clean</code> 这样的命令直接调用这个脚本。</p><p>首先，我们可以使用 <code>chmod</code> 命令为 <code>brew-clean</code> 赋予可执行权限。参数 <code>+x</code> 就表示「增加可执行权限」。</p><pre class="language-shell"><code>chmod +x brew-clean
</code></pre><p>现在，我们已经可以用 <code>./brew-clean</code> 的方式来调用它了。为了在任意目录下都可以调用，我们可以将其保存到 <code>/usr/local/bin</code>。这是专门存放用户自行安装的程序的目录。</p><pre class="language-shell"><code>mv brew-clean /usr/local/bin
</code></pre><p>以上命令将 <code>brew-clean</code> 文件移动到了 <code>/usr/local/bin</code>。如果你希望复制而非移动，可以将 <code>mv</code>（即 move）替换为 <code>cp</code>（即 copy）。</p><p>让我们来试试运行效果：</p><p> </p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/editor/u_xfzh5jgk/16172762642690.gif" alt="简单 HomeBrew 缓存清理 demo" data-original="https://cdn.sspai.com/editor/u_xfzh5jgk/16172762642690.gif" referrerpolicy="no-referrer"><figcaption>简单 HomeBrew 缓存清理 demo</figcaption></figure><p> </p><p>Awesome！</p><h2>功能拓展</h2><p>在前两节，我们用短短七行代码就实现了 HomeBrew 缓存清理功能。我将在这一板块抛砖引玉，提出一些可以扩展此脚本的想法和实现方式，大家也可以在评论区里提出自己的 idea。</p><h3>在脚本中加入 <code>brew cleanup</code></h3><p>我们在上文中已经提到，HomeBrew 内置的 <code>brew cleanup</code> 工具可以用来移除历史版本备份，从而释放磁盘空间。如果确有需要，可以在 for 循环前或循环后加入一行 <code>brew cleanup</code> 来调用它。</p><p>之所以不推荐在脚本中加入，是因为 <code>brew cleanup</code> 执行十分缓慢（在我的 Mac 上可能长达数分钟），而这个脚本在大多数情况下只需要数秒就能完成下载缓存的清理，直接在脚本中调用 <code>brew cleanup</code> 会使原本轻快的脚本变得笨重。此外，在默认设置下 HomeBrew 每三十天将自动进行一次 cleanup（一般在完成 upgrade 或 install 之后），手动调用比较费时，意义不大。</p><h3>在运行结束后展示清理结果</h3><p>在 <code>brew cleanup</code> 完成后，它会输出清理的文件总数。我们也可以在脚本中实现这一功能，大致的实现如下：</p><pre class="language-shell"><code>count=0
for link in $(find ~/Library/Caches/Homebrew -type l)
do
    let count++
    # 清理语句
done

echo "Pruned $count symbolic links and $count files from $(realpath ~/Library/Caches/Homebrew)"
</code></pre><p>在上面这段代码中，我使用了变量 <code>$count</code> 进行计数。shell 默认将变量视为字符串，因此进行数学运算需要使用其他工具或特殊语法，这里使用的是兼容性比较好且较为直观的 <code>let</code>。</p><h3>对 Cask 和 Formulae 进行针对性处理</h3><p>HomeBrew Cask 软件包一般是 DMG 或是 PKG 格式的安装包。不同于经过特殊封装的 Formulae，Cask 软件包大都是由软件开发商官方发布的，并且可以在任何兼容的机器上很方便地进行安装。我们当然可以单独处理 HomeBrew Cask 软件包，例如将其保留或者移至回收站，而对 Formulae 采取直接删除处理。要达到以上效果，我们可以将以下代码加入到脚本开头：</p><pre class="language-shell"><code>for link in $(find ~/Library/Caches/Homebrew/Cask -type l)
do
    trash $(realpath $link) # 删除此行以保留 Cask 软件包
    rm $link
done
</code></pre><p>以上这段代码从利用了 HomeBrew Cask 软链接存放在单独目录的特性，先对其进行处理。这样在执行原有逻辑时，指向 Cask 软件包的链接已经不复存在，所以可以用于单独处理 Formulae 软件包。</p><h3>清理未完成的下载</h3><p>在 HomeBrew 中，未完成的下载统一使用了 <code>.incomplete</code> 作为扩展名。它们不会被建立符号连接，因此不能用上文的方式进行处理。对于这类缓存，我们可以直接在下载目录中进行定位并删除。所需命令大致如下：</p><pre class="language-shell"><code>rm ~/Library/Caches/Homebrew/downloads/*.incomplete
</code></pre><p>其中，<code>*</code> 是通配符，<code>*.incomplete</code> 即表示该目录下所有名称以 <code>.incomplete</code> 结尾的文件。<code>rm</code> 和 <code>trash</code> 均支持使用 <code>*</code> 通配符批量删除文件。</p><h2>总结与延伸</h2><p>接下来我会将以上提到的所有功能进行整合，晒出一份完整的脚本。大家可以自取所需，以此为基础定制自己的清理脚本：</p><pre class="language-shell"><code>#!/bin/bash

# 文件计数
file_count=0
link_count=0
incomplete_count=0

# 清理 HomeBrew Cask 下载缓存
for cask_link in $(find ~/Library/Caches/Homebrew/Cask -type l)
do
    # 将 Cask 软件包移至废纸篓
    # let file_count++
    # trash $(realpath $cask_link)
    let link_count++
    rm $link
done

# 清理 HomeBrew 下载缓存
for link in $(find ~/Library/Caches/Homebrew -type l)
do
    let file_count++
    trash $(realpath $link)
    let link_count++
    rm $link
done

# 获取 *.incomplete 文件数量
let incomplete_count=$(ls -l ~/Library/Caches/Homebrew/downloads/*.incomplete | wc -l)
# 清理未完成的下载
rm ~/Library/Caches/Homebrew/downloads/*.incomplete

# 复数输出函数
plural() &#123;
    if [ $1 -gt 1 ]
    then
        echo "$1 $2s"
    else
        echo "$1 $2"
    fi
&#125;

# 输出消息提示
echo "Pruned $(plural $link_count "symbolic link"), $(plural $file_count "file") and $(plural $incomplete_count "incomplete download") from $(realpath ~/Library/Caches/Homebrew)"

# 调用 `brew cleanup`
# echo 'Running `brew cleanup`'
# brew cleanup
</code></pre><p>在以上的示例中，我使用了一些之前未提到的技巧，例如管道、<code>if</code> 条件分支、自定义函数，以及 <code>ls</code> 和 <code>wc</code> 工具。感兴趣的读者可以自行阅读相关的开放教程，例如 <a href="https://101.ustclug.org/">鄙社 Linux 101 教程</a> 中的 <a href="https://101.ustclug.org/Ch06/#shell-scripts">Shell 脚本</a> 部分。此外，由人民邮电出版社引进的<a href="https://www.epubit.com/bookDetails?id=N28189">《UNIX/Linux/OS X中的Shell编程（第4版）》</a>是 Shell 编程领域不可多得的佳作，适合各知识水平的读者参考和学习。</p></div><!----></div><div style="border:1px solid transparent;" data-v-e1f0100a></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-e1f0100a><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>2</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>0</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-6808" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90%E4%BB%8E%E9%9B%B6%E5%BC%80%E5%A7%8B%EF%BC%8C%E7%BC%96%E5%86%99%E4%B8%80%E4%B8%AA%20HomeBrew%20%E7%BC%93%E5%AD%98%E6%B8%85%E7%90%86%E8%84%9A%E6%9C%AC%E3%80%91%E5%A6%82%E6%9E%9C%E4%BD%A0%E6%AD%A3%E5%9C%A8%E4%BD%BF%E7%94%A8HomeBrew%EF%BC%8C%E5%B9%B6%E4%B8%94%E6%B2%A1%E6%9C%89%E4%BD%BF%E7%94%A8%E8%BF%87%E5%9E%83%E5%9C%BE%E6%B8%85%E7%90%86%E8%BD%AF%E4%BB%B6%E5%AF%B9%E5%85%B6%E7%BC%93%E5%AD%98%E8%BF%9B%E8%A1%8C%E8%BF%87%E6%B8%85%E7%90%86%EF%BC%8C%E4%B8%8D%E5%A6%82%E9%80%9A%E8%BF%87open~%2FLibrary%2FCache%2FHomebre%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=https%3A%2F%2Fcdn.sspai.com%2Feditor%2Fu_xfzh5jgk%2F16172791725082.jpg%3FimageMogr2%2Fauto-orient%2Fquality%2F95%2Fthumbnail%2F!1420x708r%2Fgravity%2FCenter%2Fcrop%2F1420x708%2Finterlace%2F1&appkey=3196502474#" target="_blank"><i class="icon icon-article_weibo right-16"></i></a><span><div role="tooltip" id="el-popover-2360" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><i class="icon icon-article_weixin right-16"></i></span><a href="https://twitter.com/share?text=%E3%80%90%E4%BB%8E%E9%9B%B6%E5%BC%80%E5%A7%8B%EF%BC%8C%E7%BC%96%E5%86%99%E4%B8%80%E4%B8%AA%20HomeBrew%20%E7%BC%93%E5%AD%98%E6%B8%85%E7%90%86%E8%84%9A%E6%9C%AC%E3%80%91%E5%A6%82%E6%9E%9C%E4%BD%A0%E6%AD%A3%E5%9C%A8%E4%BD%BF%E7%94%A8HomeBrew%EF%BC%8C%E5%B9%B6%E4%B8%94%E6%B2%A1%E6%9C%89%E4%BD%BF%E7%94%A8%E8%BF%87%E5%9E%83%E5%9C%BE%E6%B8%85%E7%90%86%E8%BD%AF%E4%BB%B6%E5%AF%B9%E5%85%B6%E7%BC%93%E5%AD%98%E8%BF%9B%E8%A1%8C%E8%BF%87%E6%B8%85%E7%90%86%EF%BC%8C%E4%B8%8D%E5%A6%82%E9%80%9A%E8%BF%87open~%2FLibrary%2FCache%2FHomebre%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="icon icon-article_twitter right-16"></i></a></div></div><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            