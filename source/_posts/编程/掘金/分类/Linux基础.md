
---
title: 'Linux基础'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09311d83a941431f9b043d911e03e692~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 22:26:19 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09311d83a941431f9b043d911e03e692~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、Linux常见命令</h1>
<h2 data-id="heading-1">1.1常见的Linux指令（持续更新）</h2>





















































<table><thead><tr><th align="center">序号</th><th align="center">命令</th><th align="center">描述</th><th align="center">功能</th></tr></thead><tbody><tr><td align="center">01</td><td align="center">ls</td><td align="center">list</td><td align="center">查看当前文件夹下的内容</td></tr><tr><td align="center">02</td><td align="center">pwd</td><td align="center">print wrok directory</td><td align="center">查看当前所在文件夹</td></tr><tr><td align="center">03</td><td align="center">cd [目录]</td><td align="center">change directory</td><td align="center">切换文件夹/路径</td></tr><tr><td align="center">04</td><td align="center">touch [文件名]</td><td align="center">touch</td><td align="center">创建一个空文件夹（主要功能）</td></tr><tr><td align="center">05</td><td align="center">mkdr [目录名]</td><td align="center">make directory</td><td align="center">创建目录</td></tr><tr><td align="center">06</td><td align="center">rm[文件名]</td><td align="center">remove</td><td align="center">删除指定的文件名</td></tr><tr><td align="center">07</td><td align="center">clear</td><td align="center">clear</td><td align="center">清屏</td></tr></tbody></table>
<blockquote>
<p>rm -r 文件名/文件夹名   这个命令可以删除文件或者一个文件夹（删除文件夹里面的文件也就删除了哦），其中的-r是代表<code>递归-recursive</code>，递归删除。让rm不再局限于删除文件。</p>
</blockquote>
<h2 data-id="heading-2">1.2终端命令格式</h2>
<blockquote>
<p>command [-options] [parameter]</p>
</blockquote>
<p>说明：</p>
<ul>
<li>
<p><code>command</code>：命令名</p>
</li>
<li>
<p><code>[-options]</code>:选项，可用来对命令进行控制</p>
</li>
<li>
<p><code>[parameter]</code>：传给命令的参数，可以是0个，一个或多个</p>
<blockquote>
<p>命令说明中，带有<code>[]</code>的说明可选</p>
</blockquote>
</li>
</ul>
<h3 data-id="heading-3">1.3查阅命令帮助信息（了解）</h3>
<h3 data-id="heading-4">1.3.1 --help</h3>
<blockquote>
<p>command --help</p>
</blockquote>
<ul>
<li>显示<code>command</code>命令的帮助信息</li>
</ul>
<h3 data-id="heading-5">1.3.2 man</h3>
<blockquote>
<p>man command</p>
</blockquote>
<ul>
<li>
<p>查阅<code>command</code>命令的使用手册</p>
<blockquote>
<p>man是<code>manual</code>的缩写</p>
</blockquote>

































<table><thead><tr><th align="center">操作键</th><th align="center">功能</th></tr></thead><tbody><tr><td align="center">space</td><td align="center">显示手册页的下一屏</td></tr><tr><td align="center">enter</td><td align="center">一次滚动手册页的一行</td></tr><tr><td align="center">b</td><td align="center">回滚一页</td></tr><tr><td align="center">f</td><td align="center">前滚一屏</td></tr><tr><td align="center">q</td><td align="center">退出</td></tr><tr><td align="center">/word</td><td align="center">搜索word字符串</td></tr></tbody></table>
</li>
</ul>
<h1 data-id="heading-6">二、文件和目录常用命令</h1>
<h2 data-id="heading-7">2.1 终端使用技巧</h2>
<h3 data-id="heading-8">2.1.1 自动补全</h3>
<ul>
<li>在敲出<code>文件</code>/<code>目录</code>/<code>命令</code>的前几个字母之，按下<code>tab</code>键。
<ul>
<li>如果输入的没有歧义，就会自动补全。</li>
<li>如果存在歧义（即有多个文件与输入的字母相匹配）,再次按下<code>tab</code>将会显示所有可匹配到的命令，再次输入相应的搜索字段，可逐层筛选，直到你找到自己想输入的命令为止。</li>
</ul>
</li>
</ul>
<h3 data-id="heading-9">2.1.2选择曾经使用过的命令</h3>
<ul>
<li>使用键盘:arrow_up:和:arrow_down:按钮，就可以调节你曾经是用过的上一个命令或者下一个命令。</li>
<li>如果想退出选择，输入新的命令按<code>ctrl+c</code>，即可退出选择</li>
</ul>
<h2 data-id="heading-10">2.2 ls 命令</h2>
<h3 data-id="heading-11">2.2.1 ls 的基本使用</h3>
<ul>
<li><code>ls</code>是<code>list</code>的意思，查看当前目录下的文件</li>
</ul>
<h3 data-id="heading-12">2.2.2 隐藏文件和隐藏文件的查看</h3>
<ul>
<li>Linux<strong>文件</strong>或者目<strong>名称</strong>最长可以<strong>256</strong>个字符</li>
<li>在linux中，文件名以<code>.</code>开头的文件，均视为隐藏文件</li>
<li>在linux中查看隐藏文件需要使用<code>ls -a </code>命令</li>
</ul>
<h3 data-id="heading-13">2.2.3 ls命令的常用选项</h3>





















<table><thead><tr><th align="center">选项</th><th align="center">含义</th></tr></thead><tbody><tr><td align="center">-a</td><td align="center">显示指定目录下所有子目录与文件，包括隐藏文件</td></tr><tr><td align="center">-l</td><td align="center">以列表方式显示文件的详细信息</td></tr><tr><td align="center">-h</td><td align="center">配合-l以人性化的方式显示文件的大小</td></tr></tbody></table>
<blockquote>
<p>在Linux里，选项命令是可以分开写的，也是可以合并写的，如<code>ls -l -h</code>的效果与<code>ls -lh</code>的效果是一样的。</p>
</blockquote>
<ul>
<li>
<p>在使用选项<code>-l</code>后会以列表方式展示文件夹，开头是**<code>d</code>的为文件夹<strong>开头</strong>是<code>-</code>的为文件**.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09311d83a941431f9b043d911e03e692~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-14">扩展（没啥用的知识又增加了）</h3>























































<table><thead><tr><th align="center">单位</th><th align="center">英文</th><th align="center">含义</th></tr></thead><tbody><tr><td align="center">字节</td><td align="center">b(byte)</td><td align="center">计算机中作为一个单元，8位二进制一字节</td></tr><tr><td align="center">千</td><td align="center">k(kibibyte)</td><td align="center">1kb=1024b，千字节（1020=2^10）</td></tr><tr><td align="center">兆</td><td align="center">M(Mebibyte)</td><td align="center">1MB=1024KB 百万字节</td></tr><tr><td align="center">千兆</td><td align="center">G(Gigabyte)</td><td align="center">1GB=1024MB，</td></tr><tr><td align="center">太</td><td align="center">T(Terabyte)</td><td align="center">1TB = 1024GB</td></tr><tr><td align="center">拍</td><td align="center">P(petabyte)</td><td align="center">1P=1024T</td></tr><tr><td align="center">艾</td><td align="center">E(Exabyte)</td><td align="center">1EB =1024PB</td></tr><tr><td align="center">泽</td><td align="center">Z(Zettabyte)</td><td align="center">1ZB=1024EB</td></tr><tr><td align="center">尧</td><td align="center">Y(Yottabyte)</td><td align="center">1YB=1024ZB</td></tr></tbody></table>
<h3 data-id="heading-15">2.2.4 ls与通配符的搭配使用</h3>





























<table><thead><tr><th align="center">通配符</th><th align="center">含义</th></tr></thead><tbody><tr><td align="center">*</td><td align="center">代表任意个数个字符</td></tr><tr><td align="center">？</td><td align="center">代表人已一个字符，至少一个</td></tr><tr><td align="center">[]</td><td align="center">代表可以匹配字符组中的任意一个</td></tr><tr><td align="center">[abc]</td><td align="center">匹配a、b、c的任意一个</td></tr><tr><td align="center">[a-c]</td><td align="center">匹配a到c的任意一个</td></tr></tbody></table>
<ul>
<li>
<p>效果简单的演示</p>
<ol>
<li>
<p><code>ls *3.txt</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8690776140e844509ab47a31b3862908~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>说明：匹配以3结尾的txt文件</p>
</blockquote>
</li>
<li>
<p><code>ls 3*.txt</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc8f4b47a3894583ad87fc2f5babcc28~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>说明：匹配以3开头的txt文件</p>
</blockquote>
</li>
<li>
<p><code>ls *3*</code>/<code>ls *3*.txt</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71a67694e7654212adeddd82c77a9702~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb85e81e008c4131a7d66e5d90dd493f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>说明：无论是<code>ls *3*</code>还是<code>ls *3*.txt</code>,匹配中间为3的文件，因为后缀也算文件名的一部分，所以搜索结果是上述结果。</p>
</blockquote>
</li>
<li>
<p><code>ls ?est.txt</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5465ec7fc6e44d378a370b243f135783~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>说明：? 只能任意匹配一个字符</p>
</blockquote>
</li>
<li>
<p><code>ls ???.txt</code></p>
<blockquote>
<p>说明：匹配三个字符的txt文件</p>
</blockquote>
</li>
<li>
<p><code>ls [13]23.txt</code>与<code>ls [1-3]23.txt</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7f87fcffe7847aa926913a07352d535~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ol>
</li>
</ul>
<h2 data-id="heading-16">2.3<code> cd</code>命令</h2>
<h3 data-id="heading-17">2.3.1 <code>cd</code></h3>
<ul>
<li>
<p><code>cd</code>命令是change directory的简写，功能是更改用户当前的工作目录（切换目录）</p>





























<table><thead><tr><th>命令</th><th>含义</th></tr></thead><tbody><tr><td><code>cd</code></td><td>切换到当前目录的用户主目录（/home/用户目录）</td></tr><tr><td><code>cd ~</code></td><td>切换到当前目录的用户主目录（/home/用户目录）</td></tr><tr><td><code>cd .</code></td><td>切换到当前目录</td></tr><tr><td><code>cd ..</code></td><td>切换到上级目录</td></tr><tr><td><code>cd -</code></td><td>切换最近一次的工作目录（可以在最近两次工作目录之前来回切换）</td></tr></tbody></table>
</li>
</ul>
<h2 data-id="heading-18">2.4 <code>touch</code>命令</h2>
<ul>
<li>创建文件或者修改文件时间
<ul>
<li>如果文件<strong>存在</strong>，可以修改文件的末次修改日期</li>
<li>如果文件<strong>不存在</strong>，可以创建一个空白文件</li>
</ul>
</li>
</ul>
<h2 data-id="heading-19">2.5 <code>mkdir</code>命令</h2>
<ul>
<li>
<p>创建一个新的目录</p>













<table><thead><tr><th>选项</th><th>含义</th></tr></thead><tbody><tr><td>-p</td><td>可以递归创建目录</td></tr></tbody></table>
<blockquote>
<p>新建目录的名称<strong>不能与当前目录中已有的目录或文件同名</strong>（后缀包含在文件名中）</p>
</blockquote>
</li>
</ul>
<h2 data-id="heading-20">2.6 rm命令</h2>
<blockquote>
<p>Linux中删除文件将<strong>不能恢复</strong>，所以<code>rm</code>命令要<strong>慎重使用</strong></p>
</blockquote>

















<table><thead><tr><th>参数</th><th>含义</th></tr></thead><tbody><tr><td>-f</td><td>强制删除，忽略不存在的文件，不会提示</td></tr><tr><td>-r</td><td>递归的删除目录下的内容，删除文件夹时必须添加此参数</td></tr></tbody></table>
<h2 data-id="heading-21">2.6 拷贝和移动文件</h2>





























<table><thead><tr><th>命令</th><th>英文</th><th>作用</th><th>例子</th></tr></thead><tbody><tr><td><code>tree</code> [目录名]</td><td>tree</td><td>以树状图列出文件目录结构</td><td><code>tree  Desktop</code></td></tr><tr><td><code>cp</code> 源文件 目标文件</td><td>copy</td><td>复制文件或目录</td><td><code>cp 01.txt Desktop/新建/01.txt</code></td></tr><tr><td><code>mv</code> 源文件 目标文件</td><td>move</td><td>移动文件或目录</td><td><code>mv 01.txt ./新建文件夹/01.txt</code></td></tr></tbody></table>
<h3 data-id="heading-22">2.6.1 tree命令</h3>













<table><thead><tr><th>命令</th><th>作用</th></tr></thead><tbody><tr><td>-d</td><td>只显示文件夹的树状图结构</td></tr></tbody></table>
<h3 data-id="heading-23">2.6.2cp命令</h3>





















<table><thead><tr><th>选项</th><th>含义</th></tr></thead><tbody><tr><td>-f</td><td>已经存在的木匾文件直接覆盖，不会提示</td></tr><tr><td>-i</td><td>覆盖文件前提示</td></tr><tr><td>-r</td><td>若给出的源文件是目录文件，则<code>cp</code>将递归复制该目录下所有子目录和文件，目标文件必须为一个目录名</td></tr></tbody></table>
<blockquote>
<p><strong><code>cp</code>命令默认是-f的，也就是说不加选项的情况下，同名文件或文件夹会默认覆盖掉。</strong></p>
</blockquote>
<h3 data-id="heading-24">2.6.3 mv命令</h3>













<table><thead><tr><th>选项</th><th>含义</th></tr></thead><tbody><tr><td>-i</td><td>覆盖文件前提示</td></tr></tbody></table>
<blockquote>
<p><code>mv</code>命令可以用来移动文件或目录，也可以给文件或目录<strong>重命名</strong></p>
<ul>
<li>操作方式为<code>cp 01.txt 02.txt</code>-><code>mv 01.txt  02.txt</code>,就将01改名为02，但因为mv命令也是覆盖的，所以建议在<strong>使用时添加一个<code>-i</code></strong>.</li>
</ul>
</blockquote>
<h2 data-id="heading-25">2.7 查看文件内容</h2>

























<table><thead><tr><th>命令</th><th>英文</th><th>功能</th></tr></thead><tbody><tr><td><code>cat 文件名</code></td><td>concatenate</td><td>查看文件内容，创建文件、文件合并、追加文件内容等功能</td></tr><tr><td><code>more 文件名</code></td><td>more</td><td>分屏显示文件内容</td></tr><tr><td><code>grep 搜索文本文件名</code></td><td>grep</td><td>搜索文本文件内容</td></tr></tbody></table>
<h3 data-id="heading-26">2.7.1 cat命令</h3>
<ul>
<li>
<p><code>cat</code>命令可以用来<strong>查看文件内容、创建文件、文件合并、追加文件内容</strong>等功能</p>
</li>
<li>
<p><code>cat</code>会一次显示所有内容，适合查看<strong>内容较少</strong>的文本文件</p>
<ul>
<li>

















<table><thead><tr><th>选项</th><th>含义</th></tr></thead><tbody><tr><td>-b</td><td>对非空输出行编号</td></tr><tr><td>-n</td><td>对输出的所有行编号</td></tr></tbody></table>
<blockquote>
<p>命令演示：<code>cat [选项] 被查看的文件名</code> eg:<code>cat -b 01.txt</code></p>
<p>Linux中海油一个<code>nl</code>的命令和<code>cat -b</code>的效果等价</p>
</blockquote>
</li>
</ul>
</li>
</ul>
<h3 data-id="heading-27">2.7.2 more命令</h3>
<ul>
<li>
<p><code>more</code>命令可以用于分屏显示文件内容，每次只显示一页内容</p>
</li>
<li>
<p>适用于<strong>查看内容比较多</strong>的文本文件</p>
</li>
<li>
<p>使用more的操作键</p>





























<table><thead><tr><th align="center">操作键</th><th align="center">功能</th></tr></thead><tbody><tr><td align="center">space</td><td align="center">显示手册页的下一屏</td></tr><tr><td align="center">enter</td><td align="center">一次滚动手册页的一行</td></tr><tr><td align="center">b</td><td align="center">回滚一页</td></tr><tr><td align="center">f</td><td align="center">前滚一屏</td></tr><tr><td align="center">q</td><td align="center">退出</td></tr></tbody></table>
<blockquote>
<p>命令演示：<code>more 被查看的文件名</code> eg:<code>more 01.txt</code></p>
</blockquote>
</li>
</ul>
<h3 data-id="heading-28">2.7.3 <code>grep</code>命令</h3>
<ul>
<li>
<p><code>grep</code>是一个非常强大的文本搜索工具</p>
</li>
<li>
<p><code>grep</code>允许对文本文件进行模式查找（所谓的模式查找也叫正则表达式）</p>





















<table><thead><tr><th align="center">选项</th><th align="center">含义</th></tr></thead><tbody><tr><td align="center">-n</td><td align="center">显示匹配及行号</td></tr><tr><td align="center">-v</td><td align="center">显示不包含匹配文本的所有航（相当于求反）</td></tr><tr><td align="center">-i</td><td align="center">忽略大小写</td></tr></tbody></table>
<blockquote>
<p>命令演示: <code>grep 搜索内容 被搜索文件</code> eg: <code>grep abc 01.txt</code>/<code>grep abc ./新建文件夹/01.txt</code></p>
</blockquote>
</li>
<li>
<p>常用的模式查找</p>

















<table><thead><tr><th>参数</th><th>含义</th></tr></thead><tbody><tr><td>^a</td><td>行首，搜索以a开头的行</td></tr><tr><td>ke$</td><td>行尾，搜索以ke结束的行</td></tr></tbody></table>
</li>
</ul>
<h2 data-id="heading-29">2.8 其他</h2>
<h3 data-id="heading-30">2.8.1 echo文字内容</h3>
<ul>
<li><code>echo</code>会在终端中显示参数指定的文字，通常会和<strong>重定向</strong>联合使用</li>
</ul>
<p>2.8.2 重定向 >和>></p>
<ul>
<li>
<p>Linux允许将一个命令执行结果<strong>重定向</strong>到一个<strong>文件</strong></p>
</li>
<li>
<p>将本应显示在<strong>终端上的内容</strong> <strong>输出/追加</strong>到指定文件中</p>
</li>
<li>
<p><code>></code>表示输出，会覆盖原件原有的内容</p>
</li>
<li>
<p><code>>></code>表示追加，会将内容追加到已有文件的末尾</p>
<blockquote>
<p>命令演示：</p>
<ul>
<li><code>echo hello world! > 01.txt</code>,将hello world重定向到<code>01.txt</code>文档中，并覆盖原本的内容。如果目标目录中没有重定向的文件，那么Linux会自动创建一个该文件。（就是如果没有01.txt，就会自动生成一个01.txt并把内容重定向进去）。</li>
<li><code>tree >> 01.txt</code> 将tree查询的结果追加到<code>01.txt</code>内容后面。</li>
</ul>
</blockquote>
</li>
</ul>
<h3 data-id="heading-31">2.8.3 管道<code>|</code></h3>
<ul>
<li>Linux允许将一个<strong>命令的输出</strong>通过<strong>管道</strong>作为<strong>另一个命令的入口</strong>.</li>
</ul>
<p>管道常用的命令有：</p>
<ul>
<li>
<p><code>more</code>：分屏显示内容。</p>
</li>
<li>
<p><code>grep</code>:在命令执行结果的基础上查询指定的文本</p>
<blockquote>
<p>命令演示：<code>ls -lha ~ | more</code> 会将home目录下的所有目录（包含隐藏目录/文件）分屏显示</p>
</blockquote>
</li>
</ul>
<h1 data-id="heading-32">三、系统配置及基础操作</h1>
<h2 data-id="heading-33">3.1关机/重启</h2>















<table><thead><tr><th align="center">命令</th><th align="center">英文</th><th align="center">功能</th></tr></thead><tbody><tr><td align="center">shutdown</td><td align="center">shutdown</td><td align="center">关机/重启</td></tr></tbody></table>
<h3 data-id="heading-34">3.1.1 shutdown</h3>

















<table><thead><tr><th align="center">选项</th><th align="center">含义</th></tr></thead><tbody><tr><td align="center">-r</td><td align="center">重启</td></tr><tr><td align="center">-c</td><td align="center">取消关机/重启</td></tr></tbody></table>
<ul>
<li>
<p>不指定选项的话，默认一分钟之后关闭系统。</p>
</li>
<li>
<p>远程登录服务器时，最好不要关闭系统，所以一定要加选项<code>-r</code>。</p>
</li>
<li>
<p>常用命令：</p>
<pre><code class="hljs language-basic copyable" lang="basic">#重新启动操作系统，now表示现在
$ shutdown -r now
#立即关机
$ shutdown now

#系统在今天的<span class="hljs-number">13</span>：<span class="hljs-number">06</span> 关机/重启
$ shutdown -r <span class="hljs-number">13</span>:<span class="hljs-number">06</span>
$ shutdown <span class="hljs-number">13</span>:<span class="hljs-number">06</span>

#系统将在十分钟后关机/重启
$ shutdown <span class="hljs-number">10</span>
$ shutdown -r <span class="hljs-number">10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-35">3.2 网卡和<code>IP</code>地址</h2>




















<table><thead><tr><th>命令</th><th>英文</th><th>功能</th></tr></thead><tbody><tr><td><code>ifconfig</code></td><td>configure a network interface</td><td>查看/配置计算机当前的网卡配置信息</td></tr><tr><td><code>ping ip</code></td><td>ping</td><td>检测目标<code>ip</code>是否连接正常</td></tr></tbody></table>
<h3 data-id="heading-36">3.2.1网卡</h3>
<ul>
<li>（概念懒得写了，想了解详见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.baidu.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.baidu.com/" ref="nofollow noopener noreferrer">什么是网卡和IP地址</a>）</li>
</ul>
<h3 data-id="heading-37">3.2.2 <code>ifconfig</code>命令</h3>
<ul>
<li>
<p><code>ifconfig</code>命令是用来查看和配置网卡信息的。</p>
</li>
<li>
<p>如果系统内找不到<code>ifconfig</code>命令，报错截图如下;</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea6be3c1cc024f289bc034b0c64a412e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>输入截图中提示的命令之后安装完成后即可使用<code>ifconfig</code>命令。</p>
</li>
<li>
<p>常用的<code>ifconfig</code>命令</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 查看网卡配置信息</span>
$ ifconfig 

<span class="hljs-comment">#查看网卡对应的IP地址</span>
$ ifconfig | grep inet
<span class="hljs-comment">#上面这个命令是在查询结果中搜索inet的值，也就是ip地址了</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-38">3.2.3 <code>ping</code>命令</h3>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment">#查看系统与目标IP地址连接是否正常</span>
$ ping IP
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<ul>
<li>如果要暂停ping命令，按下ctrl+c即可</li>
</ul>
</blockquote>
<h1 data-id="heading-39">四、远程操作</h1>
<h2 data-id="heading-40">4.1 ssh基础</h2>
<p>SSH是一种使用<code>Secure Shell</code>协议来连接远程计算机的软件程序</p>
<ul>
<li>
<p>SSH是目前比较可靠，专门为远程登陆会话和其他网络服务提供安全性的协议</p>
<ul>
<li>利用<code>SSH协议</code>可以有效防止远程管理过程中的信息泄露</li>
<li>利用<code>SSH协议</code>可以对所有传输的数据进行贾母，也可以防止DNS欺骗和IP欺骗</li>
</ul>
</li>
<li>
<p>通过SSH传输的数据是经过压缩的，可以提高传输速度</p>
<blockquote>
<p><del>开放22号端口命令（下面的命令是我在使用的时候百度尝试的，有用，但是我现在还看不懂，没法把解释放在博客上，但后面我明白了之后会补上:smile:）;</del></p>
</blockquote>
</li>
</ul>
<h3 data-id="heading-41">4.1.1 域名&端口号</h3>
<p>具体概念详见：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.baidu.com" target="_blank" rel="nofollow noopener noreferrer" title="https://www.baidu.com" ref="nofollow noopener noreferrer">什么是域名&端口号</a>。这里我只简单描述一下。</p>
<ol>
<li>
<p>域名就相当于<code>IP</code>地址的<strong>别名</strong>。</p>
</li>
<li>
<p>我们知道<code>IP</code>可以确定一台电脑，端口号是用来确定一台电脑的<strong>某个应用程序</strong>的。</p>
<ul>
<li>SSH服务器的默认端口号是22，如果是默认端口号，在连接的时候可以省略。</li>
</ul>
</li>
<li>
<p>常见的服务端口号列表</p>

























<table><thead><tr><th>服务</th><th>端口号</th></tr></thead><tbody><tr><td>SSH服务器</td><td>22</td></tr><tr><td>Web服务器</td><td>80</td></tr><tr><td>HTTPS</td><td>443</td></tr><tr><td>FTP服务器</td><td>21</td></tr></tbody></table>
</li>
</ol>
<h3 data-id="heading-42">4.1.2 SSH命令的使用</h3>
<pre><code class="hljs language-basic copyable" lang="basic">$ ssh [-p port] user@<span class="hljs-comment">remote</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p><code>user</code>是在远程机器上的用户名，如果不指定的话默认为当前用户</p>
</li>
<li>
<p><code>remote</code>是远程机器的地址，可以是<strong>IP/域名/别名</strong>。</p>
</li>
<li>
<p><code>port</code>是SSH Server监听的端口，如果不指定，就默认22</p>
<blockquote>
<p>提示：</p>
<ul>
<li>使用<code>exit</code>退出当前用户的登陆</li>
<li>在工作中，可能SSH服务器的端口号不是22，那就需要使用<code>-p</code>选项，指定正确的端口号，否则无法正常连接。</li>
</ul>
</blockquote>
</li>
</ul>
<h2 data-id="heading-43">4.2 scp命令</h2>
<ul>
<li>
<p><strong>scp并不能在windows系统下使用，Mac的终端可以正常使用</strong></p>
</li>
<li>
<p>scp就是<code>secure copy</code>，是一个在Linux下用来进行<strong>远程拷贝文件的命令</strong>。</p>
</li>
<li>
<p>它的地址格式与SSH相同，但是指定端口的时候<code>-P</code>命令是<strong>大写</strong>的。</p>
<pre><code class="hljs language-basic copyable" lang="basic">#把本地当前目录下的文件复制到远程 home目录下的某文件夹内
#如果 : 后面不是绝对路径则以用户 home目录为参照路径
$ scp -P port <span class="hljs-number">01</span>.txt user@<span class="hljs-comment">remote:Desktop/01.py</span>

#把远程 home 目录下的Desktop/<span class="hljs-number">01</span>.txt复制到本地当前目录下
$ scp -P port user@<span class="hljs-comment">remote:Desktop/01.txt 01.txt</span>

#加上 -r 选项可以传送文件夹
#把当前目录下的dome文件夹复制到哦远程 home 目录下的desktop
$ scp -r demo user@<span class="hljs-comment">remote:Desktop</span>

#把远程 home 目录下的Desktop复制到当前目录下的demo文件夹
$ scp -r user@<span class="hljs-comment">remote:Desktop demo</span>
<span class="copy-code-btn">复制代码</span></code></pre>













<table><thead><tr><th>选项</th><th>功能</th></tr></thead><tbody><tr><td>-r</td><td>若给出的源文件是目录文件，则scp将递归复制该文件下的所有子目录和文件，<strong>目标文件必须为一个目录名</strong></td></tr></tbody></table>
</li>
<li>
<p>Windows中需要通过软件<code>xshell</code>等，通过ftp进行传输文件。</p>
</li>
</ul>
<h1 data-id="heading-44">五、用户权限相关命令</h1>
<h2 data-id="heading-45">5.1用户和权限的基本概念</h2>
<h3 data-id="heading-46">5.1.1基本概念</h3>
<ul>
<li>
<p>用户管理包括<strong>用户</strong>与<strong>组</strong>管理。</p>
</li>
<li>
<p>Linux中，不论是本机还是远程登录，都要有一个账号，并且<strong>对不同的系统资源有不同的使用权限</strong>。</p>
</li>
<li>
<p>对文件/目录的权限包括：</p>



































<table><thead><tr><th>权限</th><th>英文</th><th>缩写</th><th>数字代号</th></tr></thead><tbody><tr><td>读</td><td>read</td><td>r</td><td>4</td></tr><tr><td>写</td><td>write</td><td>w</td><td>2</td></tr><tr><td>执行</td><td>excute</td><td>x</td><td>1</td></tr><tr><td>无权限</td><td></td><td>-</td><td>0</td></tr></tbody></table>
</li>
<li>
<p>在Linux中，客户以制定每个用户针对不同文件或目录的不同权限</p>
</li>
</ul>
<p>5.1.2 组的概念</p>
<ul>
<li>在实际应用中，我们可以预先针对<strong>组</strong>设置好权限，然后将不同的用户天降到对应的组中，从而不用一次为每个用户设置权限。</li>
</ul>
<h2 data-id="heading-47">5.2 从<code>ls -l</code>了解权限</h2>
<table>
    <tbody><tr>
        <td></td> 
        <td>目录</td> 
        <td colspan="3">拥有者权限</td> 
        <td colspan="3">组权限</td>
        <td colspan="3">其他用户权限</td> 
   </tr>
    <tr>
        <td>文件权限示例</td>    
        <td>-</td>    
        <td>r</td>    
        <td>w</td>     
        <td>x</td>    
        <td>r</td>    
        <td>w</td> 
        <td>-</td>    
        <td>r</td>    
        <td>-</td> 
        <td>-</td> 
    </tr>
    <tr>
        <td>文件夹权限示例</td>
        <td>d</td>    
        <td>r</td>    
        <td>w</td>     
        <td>x</td>    
        <td>r</td>    
        <td>w</td> 
        <td>x</td>    
        <td>r</td>    
        <td>-</td> 
        <td>x</td>  
    </tr>
</tbody></table>
<p>具体说明截图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9618c7f1e2e840889c50e464e5f4ec6d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>硬链接数：就是有多少种方式可以访问到当前文件/文件夹</p>
<blockquote>
<p>硬连接数我不知道有什么作用，所以感兴趣的自己百度一下，我就不多废话了。</p>
</blockquote>
</li>
</ul>
<h2 data-id="heading-48">5.3 chmod 简单使用</h2>
<ul>
<li>
<p><code>chmod</code>可以修改<strong>用户/组</strong>对<strong>文件/目录</strong>的权限。</p>
</li>
<li>
<p>命令格式：</p>
<pre><code class="hljs language-basic copyable" lang="basic">$chmod +/-rewx 文件名|目录名
#在chmod后面跟+或者-代表添加权限或者减少权限，符号后面跟（rwx）权限。后面加要修改的目录/文件名
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>命令演示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62d2dc642a654da1b8ad05c05406f29a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
</li>
</ul>
<h3 data-id="heading-49">5.3.1 执行文件</h3>
<ul>
<li>
<p><strong>重点</strong>，我们来看一下Linux中如何<strong>执行一个文件</strong>。</p>
<ol>
<li>先来创建一个文件（为了方便查看结果，我写了点可执行代码）我是提前在ubuntu中安装了python环境。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3283ffccfbdf41aea99a5af4958e538e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>
<p>然后默认是不可执行的，我们通过chmod命令来更改权限。图片与执行的截图放在一起了。</p>
</li>
<li>
<p>执行文件</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61c7549b9fd6451e90a41db3c0b02cd4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ol>
</li>
</ul>
<h3 data-id="heading-50">5.3.2执行目录</h3>
<ul>
<li>
<p><strong>没有x权限</strong>：其实cd 到某个目录就是在执行目录，从上面的图片中也可以看出，默认当前用户是拥有目录的执行权限的，如果没有x的执行权限，目录将不能cd进去。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a4375f1af0b46a6b8aa76346fb5f713~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p><strong>没有r权限</strong>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b603c1128e464b15aa35222b94cbaaac~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>但是非常闲的我，发现一个问题，当你进去02文件夹后，依然可以创建文件，只是不能查看，并且可以打开创建的文件或者你已知的在02文件夹内的文件。<strong>为了做演示，我提前在02文件夹里创建了01.txt</strong>。这是因为w权限还在！！！！</p>
</blockquote>
</li>
<li>
<p>没有w权限</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce040ac2d14a4fb18b8105cd2aedbc34~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h2 data-id="heading-51">5.4 超级用户</h2>
<ul>
<li>Linux中的<code>root</code>账号通常用于<strong>系统的维护和管理</strong>，对于操作系统的<strong>所有资源具有所有访问权限</strong></li>
<li>在大多数的Linux系统中，都不推荐直接使用root账号登陆系统</li>
<li>在Linux安装的过程中，系统会自动创建一个用户账号，而这个默认的用户就称为“标准用户”</li>
</ul>
<p>5.4.1  sudo命令</p>
<ul>
<li>
<p><code>sudo</code>是<code>substitute user</code>的缩写，表示使用另一个用户的身份</p>
</li>
<li>
<p><code>sudo</code>命令用来以其他身份执行命令，预设的身份为<code>root</code>。</p>
</li>
<li>
<p>用户使用<code>sudo</code>时，必须先输入密码，此次输入密码<strong>有5分钟的有效期</strong>，超过时间则重新输入密码.</p>
<blockquote>
<p>若其未经授权的用户其企图使用sudo,则会发出警告邮件给管理员</p>
</blockquote>
</li>
</ul>
<h2 data-id="heading-52">5.5 组管理</h2>
<blockquote>
<p><strong>创建/删除组的命令都需要<code>sudo</code>执行。</strong></p>
</blockquote>

























<table><thead><tr><th>命令</th><th>作用</th></tr></thead><tbody><tr><td>groupadd 组名</td><td>添加组</td></tr><tr><td>groupdel 组名</td><td>删除组</td></tr><tr><td>cat  /etc/group</td><td>确认组信息</td></tr><tr><td>chgrp -R  组名 文件/目录名</td><td>递归修改文件/目录的所属组</td></tr></tbody></table>
<blockquote>
<p><code>cat  /etc/group</code></p>
<ul>
<li>族信息保存在<code>/etc/group</code>文件中。</li>
<li><code>/etc</code>目录是专门用来保存系统配置信息的目录</li>
</ul>
</blockquote>
<p>实际应用中，我们都是预先针对组设置好权限，<strong>然后将不同的用户添加到对应的组</strong>，<strong>从不用一次为每个用户设置权限</strong>。</p>
<h2 data-id="heading-53">5.6 创建用户/设置密码/删除用户</h2>






























<table><thead><tr><th>命令</th><th>作用</th><th>说明</th></tr></thead><tbody><tr><td>useradd -m -g 组 新建用户名</td><td>添加新用户</td><td>-m自动创建用户家目录；-g制定用户所在度组，否则会建立与当前用户同名的组</td></tr><tr><td>passwd 用户名</td><td>设置用户密码</td><td>如果是普通用户，直接用passwd客户以修改自己的账户密码。</td></tr><tr><td>userdel -r 用户名</td><td>删除用户</td><td>-r 选项会自动删除用户家目录</td></tr><tr><td>cat  /etc/passwd| grep       用户名</td><td>确认用户信息</td><td>新建用户后，用户信息会存在/etc/passwd或/etc/grep中</td></tr></tbody></table>
<blockquote>
<p><code>cat  /etc/passwd| grep 用户名</code>的命令是通过管道配合<code>grep</code>命令，直接查看到用户的的信息。</p>
</blockquote>
<blockquote>
<ul>
<li>创建用户时，如果忘记添加<code>-m</code>制定新用户的家目录，最好<strong>删掉重新创建</strong>。</li>
<li>用户信息保存在<code>etc/passwd</code>中</li>
</ul>
</blockquote>
<h2 data-id="heading-54">5.7 查看用户信息</h2>
<h3 data-id="heading-55">5.7.1 命令</h3>





















<table><thead><tr><th>命令</th><th>功能</th></tr></thead><tbody><tr><td>id [用户名]</td><td>查看用户UID（用户id）和GID(组id)</td></tr><tr><td>who</td><td>查看当前所有登陆的用户列表</td></tr><tr><td>whoami</td><td>查看单签登陆用户的账户名</td></tr></tbody></table>
<h3 data-id="heading-56">5.7.2 passwd文件</h3>
<blockquote>
<p><code>etc/passwd</code>文件中存放的是用户的信息，分别有七组信息分别用<code>：</code>隔开：</p>
<ol>
<li>用户名</li>
<li>密码（如果设置密码会显示x，表示加密）</li>
<li>UID（用户标识）</li>
<li>GID（组标识）</li>
<li>用户签名或者本地账号（当未指定创建账号的组时，就会创建一个用户名相同的组）</li>
<li>家目录</li>
<li>登陆使用的Shell,就是登陆之后，使用的重担命令，<code>ubuntu</code>默认的是<code>dash</code>。</li>
</ol>
<p>截图对比如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bd6f63bf5054492a0ab44599529b78c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<h3 data-id="heading-57">5.7.3 usermod命令</h3>
<ul>
<li>
<p><code>usermod</code>可以用来设置用户的<strong>主组</strong>/附加组合登陆shell,命令格式如下：</p>
</li>
<li>
<p>**主组：**通常在新建用户时制定，在<code>etc/passwd</code>的第四项GID对应</p>
</li>
<li>
<p><strong>附加组：<strong>在<code>etc/group</code>中最后一列标识该组的用户列表，用于</strong>指定用户的附加权限</strong>.</p>
<blockquote>
<p>设置了用户的附加组之后，需要重新登陆才能生效</p>
</blockquote>
</li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment">#修改用户的主组（passwd中的GID）</span>
$ usermod -g 组 用户名
<span class="hljs-comment">#修改用户的附加组</span>
$ usermod -G 组 用户名
<span class="hljs-comment">#修改用户登陆 Shell</span>
$ usermod -s /bin/bash
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>学习的时候，描述的是登陆使用的shell默认是dash，但是，dash在win终端上无法使用上下左右按键且文件和文件夹显示没有颜色和高亮区分，所以我们要将shell登陆模式更改为bash。（因为我尝试了一万种方法，也没把我的ubuntu的shell模式改为dash，所以就没做演示也截图了，谅解，看不懂的就百度一下吧）</p>
</blockquote>
<blockquote>
<p>默认使用<code>useradd</code>添加的用户是没有权限使用<code>sudo</code>以<code>root</code>身份执行命令的，需要下面的命令将用户添加到<code>sudo</code>组中。</p>
</blockquote>
<pre><code class="hljs language-bash copyable" lang="bash">$ usermod -G sudo 用户名
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查看自己当前登陆的shell：</p>
<p>命令</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment">#1. 第一种方法 （必须大写）</span>
$ <span class="hljs-built_in">echo</span> <span class="hljs-variable">$SHELL</span>
<span class="hljs-comment"># 2. 第二种方法</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36f91e43553744aaad7264bf618a9761~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-58">5.8 which命令</h2>
<ul>
<li>which命令可以查看执行命令所在位置</li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash">$ <span class="hljs-built_in">which</span> ls
<span class="hljs-comment">#输出/bin/ls</span>
$ <span class="hljs-built_in">which</span> useradd
<span class="hljs-comment">#输出 /usr/sbin/useradd</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>bin</code>和<code>sbin</code></p>
<ul>
<li>
<p>在<code>Linux</code>中，绝大多数可执行文件都是保存在<code>/bin</code>、<code>/sbin</code>、<code>/usr/bin</code>、<code>/usr/sbin</code>下</p>
</li>
<li>
<p><code>/bin</code>（binary）是二进制执行文件目录，主要用于具体应用</p>
</li>
<li>
<p><code>/sbin</code>(system binary)是系统管理员专用的二进制代码存放目录，用于系统管理</p>
</li>
<li>
<p><code>/usr/bin</code>（user commands for applications）后期安装的一些软件</p>
</li>
<li>
<p><code>/usr/sbin</code>（super user commands for applications）超级用户的一些管理程序</p>
<blockquote>
<p>cd这个命令是内置在系统内核中的，没有独立的文件，因此用<code>which</code>无法找到<code>cdm</code>命令的位置</p>
</blockquote>
</li>
</ul>
<h2 data-id="heading-59">5.9 切换用户</h2>




















<table><thead><tr><th>命令</th><th>功能</th><th>说明</th></tr></thead><tbody><tr><td>su-用户名</td><td>切换用户并且切换目录</td><td>加<code>-</code>可以切换到用户家目录，否则保持位置不变</td></tr><tr><td>exit</td><td>退出 当前登陆账户</td><td></td></tr></tbody></table>
<blockquote>
<p><code>su</code>命令后面加上<code>-</code>就会切换到用户的家目录，不加就不会切换目录</p>
</blockquote>
<ul>
<li>
<p><code>su</code>不接用户名可以切换到<code>root</code>,但是不推荐使用</p>
</li>
<li>
<p>exit退出只是退出当前登陆账户，会退回到上一次上一个账户，图示如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d61fe9e3de7741ef9b67f7767eed3afe~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h1 data-id="heading-60">六、操作文件及文件夹</h1>
<h2 data-id="heading-61">6.1 修改拥有者/组/权限</h2>





















<table><thead><tr><th>命令</th><th>功能</th></tr></thead><tbody><tr><td>chown</td><td>修改拥有者</td></tr><tr><td>chgrp</td><td>修改组</td></tr><tr><td>chmod</td><td>修改权限</td></tr></tbody></table>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 修改文件/目录的拥有者</span>
$ chown 用户名 文件名/目录名

<span class="hljs-comment">#递归修改文件/目录的组</span>
$ chgrp -R 组名 文件名

<span class="hljs-comment"># 递归修改文件权限</span>
$ chmod -R 755 文件名/目录名
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><code>chmod</code>在设置权限时，可以简单的使用三个数字分别对应 <strong>拥有者/组/其他用户</strong> 的权限。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 直接修改文件/目录 的 读/写/执行 权限，但是不能精确到拥有者/组/其他用户</span>
$ chmod +/-rwx 文件名/目录名
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<table>
    <tbody><tr>
    <td colspan="3">拥有者</td>
    <td colspan="3">组</td>
    <td colspan="3">其他用户</td>
    </tr>
    <tr>
    <td>r</td>
    <td>w</td>
    <td>x</td>
    <td>r</td>
    <td>w</td>
    <td>x</td>
    <td>r</td>
    <td>w</td>
    <td>x</td>
    </tr>
    <tr>
    <td>4</td>
    <td>2</td>
    <td>1</td>
    <td>4</td>
    <td>2</td>
    <td>1</td>
    <td>4</td>
    <td>2</td>
    <td>1</td></tr>
</tbody></table>
<p>三个对应的值的计算方式分别是上述表格中对应的数字相加，例如 拥有者对该文件/目录有r、w两个权限，就是对应的数组相加（4+2+0 = 6），那么拥有者这一项对应的数字就是6，组权限和其他用户权限以此类推。具体图例如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e6f3bc2e58f4f65bf99dacae85d650c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-62">七、系统信息相关命令</h1>
<h2 data-id="heading-63">7.1 查看时间和日期</h2>

















<table><thead><tr><th>命令</th><th>作用</th></tr></thead><tbody><tr><td>date</td><td>查看系统时间</td></tr><tr><td>cal</td><td>calendar 查看日历。添加选项<code>-y</code>可以查看一年的日历</td></tr></tbody></table>
<h2 data-id="heading-64">7.2 磁盘信息</h2>

















<table><thead><tr><th>命令</th><th>作用</th></tr></thead><tbody><tr><td>df -h</td><td>disk free 显示磁盘剩余空间</td></tr><tr><td>du -h</td><td>disk usage 显示目录下的文件大小</td></tr></tbody></table>
<ul>
<li><code>-h</code>选项：如果不加将以字节为单位显示，加了则以 <code>k</code>、<code>M</code>、<code>G</code>等为单位显示</li>
</ul>
<h2 data-id="heading-65">7.3 进程信息</h2>
<ul>
<li>进程，通俗的说<strong>就是当前正在执行的一个程序</strong>。</li>
</ul>
<h3 data-id="heading-66">7.3.1 ps命令</h3>

























<table><thead><tr><th>命令</th><th>功能</th></tr></thead><tbody><tr><td>ps</td><td>显示当前正在进行的进程</td></tr><tr><td>ps aux</td><td>process status 查看进程的详细情况</td></tr><tr><td>top</td><td>动态显示运行中的进程并排序</td></tr><tr><td>kill [-9] 进程代号</td><td>种植指定代号的进程，<code>-9</code>表示强行终止</td></tr></tbody></table>
<blockquote>
<p><code>ps</code>默认只会显示当前用户通过终端启动的应用程序</p>
</blockquote>
<ul>
<li>
<p><code>ps</code>选项说明</p>





















<table><thead><tr><th>选项</th><th>含义</th></tr></thead><tbody><tr><td>a</td><td>显示终端上所有进程，包括其他用户的进程</td></tr><tr><td>u</td><td>显示进程的详细状态</td></tr><tr><td>x</td><td>显示没有控制终端的进程</td></tr></tbody></table>
<blockquote>
<p>使用<code>kill</code>命令时，最好只终止当前用户开启的进程，（特别是不要关闭root身份开启的进程，否则可能会导致系统崩溃）</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f46e7f1686eb4f3e82a53b883bc8edd9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>STAT（状态）说明</p>





















































<table><thead><tr><th>代码</th><th>说明</th></tr></thead><tbody><tr><td>R</td><td>runing 运行状态</td></tr><tr><td>S</td><td>可中断睡眠态</td></tr><tr><td>D</td><td>不可终端睡眠态</td></tr><tr><td>T</td><td>停止态</td></tr><tr><td>Z</td><td>僵尸态</td></tr><tr><td>s</td><td>表示这个进程是领导者进程</td></tr><tr><td>+</td><td>该进程为前台进程</td></tr><tr><td>l</td><td>该进程是多线程进程</td></tr><tr><td>N</td><td>低优先级进程</td></tr><tr><td><</td><td>高优先级进程</td></tr><tr><td>[]</td><td>表示是一个内核进程</td></tr></tbody></table>
</li>
</ul>
<h1 data-id="heading-67">八、 其他命令</h1>
<h2 data-id="heading-68">8.1 查找文件</h2>
<ul>
<li>
<p><code>find</code>命令通常用来在特定的<strong>目录下搜索</strong>符合条件的文件。</p>













<table><thead><tr><th>命令</th><th>作用</th></tr></thead><tbody><tr><td>find [路径] [查找规则]</td><td>查找指定目录下的文件</td></tr></tbody></table>
<blockquote>
<p>命令演示：</p>
<ul>
<li>
<p><code>find ./02/ -name "*.txt"</code></p>
</li>
<li>
<p>查询当前目录下的02目录下以<code>.txt</code>结尾的文件</p>
</li>
</ul>
</blockquote>





























<table><thead><tr><th>选项</th><th>功能</th></tr></thead><tbody><tr><td>-name</td><td>按名称查找</td></tr><tr><td>-iname</td><td>忽略大小写</td></tr><tr><td>-size</td><td>按大小查找</td></tr><tr><td>-user</td><td>按属性查找</td></tr><tr><td>-type</td><td>按类型查找</td></tr></tbody></table>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 搜索 /etc下大于1M的文件</span>
$ find /etc -size +1M
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-69">8.2 软连接</h2>













<table><thead><tr><th>命令</th><th>功能</th></tr></thead><tbody><tr><td>ln -s    源文件    链接文件</td><td>建立文件的软链接，相当于win下的<strong>快捷方式</strong></td></tr></tbody></table>
<blockquote>
<ul>
<li>没有<code>-s</code>选项的话创建的是一个<strong>硬链接文件</strong>。</li>
<li>两个文件占用相同大小的硬盘空间，工作中几乎不会简历文件的硬链接</li>
<li>源文件要使用绝对路径，不能使用相对路径，这样可以方便移动链接文件后，仍可正常使用</li>
</ul>
</blockquote>
<h2 data-id="heading-70">8.3 打包压缩</h2>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 打包文件</span>
$ tar -cvf 打包文件.tar 被打包的文件/路径

<span class="hljs-comment">#解包</span>
$ tar -xvf 打包文件.tar
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>tar</code>选项</li>
</ul>

























<table><thead><tr><th>选项</th><th>含义</th></tr></thead><tbody><tr><td>c</td><td>生成档案文件，创建打包文件</td></tr><tr><td>x</td><td>解开档案文件</td></tr><tr><td>v</td><td>列出归档解档得详细过程，显示进度</td></tr><tr><td>f</td><td>指定档案文件名称，f后面一定是<code>.tar</code>文件，所以必须放到选项的最后面</td></tr></tbody></table>
<blockquote>
<ul>
<li>当你打包多个文件的时候，如果是将多个文件打包成一个包，文件用空格隔开，如:<code>tar -cvf test.tar 01.txt 02.txt 03.txt</code>.</li>
</ul>
</blockquote>
<h2 data-id="heading-71">8.4 压缩/解压缩</h2>
<h3 data-id="heading-72">8.4.1 gzip</h3>
<ul>
<li><code>tar</code>与<code>gzip</code>命令结合可以使用实现文件打包和压缩
<ul>
<li>`tar只负责打包文件但不压缩</li>
<li>用<code>gzip</code>压缩<code>tar</code>打包后的文件，其扩展名一般用<code>XXX.tar.gz</code>.</li>
</ul>
</li>
<li>在<code>tar</code>命令中有一个选项<code>-z</code>,可以调用<code>gzip</code>以方便的实现压缩/解压缩</li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment">#压缩文件</span>
$ tar -zcvf 打包文件.tar.gz 被压缩文件/路径

<span class="hljs-comment">#解压缩</span>
$ tar -zxvf 打包文件.tar.gz

<span class="hljs-comment">#解压缩到指定路径</span>
$ tar -zxvf 打包文件.tar.gz -C 目标文件
<span class="copy-code-btn">复制代码</span></code></pre>













<table><thead><tr><th>选项</th><th>含义</th></tr></thead><tbody><tr><td>-C</td><td>解压缩到指定目录（要解压缩的目录必须存在）</td></tr></tbody></table>
<h2 data-id="heading-73">8.5 软件安装</h2>
<ul>
<li><code>apt</code>是<code>AdVanced Packaging Tool</code>是Linux下的一个安装包管理工具</li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装软件</span>
$ sudo apt install 软件包

<span class="hljs-comment">#卸载软件</span>
$ duso apt remove 软件名

<span class="hljs-comment">#更新已安装的包</span>
$ sudo apt upgrade
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-74">九、软件安装源</h2>
<blockquote>
<p>算是个使用提示吧：在设置-》软件更新里将软件源更改为国内的会提高软件下载安装速度。</p>
</blockquote>
<h3 data-id="heading-75">那么基础就算是结束了，剩下的就看我啥时候有时间继续往深学习，再继续更新咯~~~:stuck_out_tongue_closed_eyes:</h3>
<h3 data-id="heading-76">未完待续~</h3>
<blockquote>
<h3 data-id="heading-77">如果有哪些知识点写的有问题滴滴我，我会尽快修改，互利共进！！！</h3>
</blockquote></div>  
</div>
            