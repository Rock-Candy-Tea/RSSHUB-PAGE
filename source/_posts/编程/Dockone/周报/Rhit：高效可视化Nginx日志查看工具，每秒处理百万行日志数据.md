
---
title: 'Rhit：高效可视化Nginx日志查看工具，每秒处理百万行日志数据'
categories: 
 - 编程
 - Dockone
 - — 周报
headimg: 'http://dockone.io/uploads/article/20210320/7a0b1c6eb35e019b87fb36687014eb7e.png'
author: Dockone
comments: false
date: 2021-03-23 12:52:19
thumbnail: 'http://dockone.io/uploads/article/20210320/7a0b1c6eb35e019b87fb36687014eb7e.png'
---

<div>   
<br>【编者的话】Rhit是一个格式化Nginx日志，可快速阅读、查看Nginx日志的工具。<br>
<h3>简介</h3>Rhit可以从标准文件夹中读取Nginx的日志文件（gzipped的压缩文件也可以），并进行分析统计，在控制台中以可视化的表格形式展示，并且不会产生任何多余的临时文件或数据。<br>
<br>可以按照日期、响应值、请求来源等进行过滤匹配，并进行分析，Rhit具有很高的效率，每秒可以处理百万行日志数据。<br>
<br>以下是在一月份的日志中查找状态码为 1xx、2xx 的结果：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210320/7a0b1c6eb35e019b87fb36687014eb7e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210320/7a0b1c6eb35e019b87fb36687014eb7e.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
项目地址是：<a href="https://github.com/Canop/rhit" rel="nofollow" target="_blank">https://github.com/Canop/rhit</a><br>
<h3>安装</h3>直接下载使用编译好的二进制文件，但是需要确保shell能够找到rhit二进制文件，一个比较容易的处理方式就是把它放到/usr/local/bin目录下，并且为它添加可执行权限。<br>
<pre class="prettyprint">chmod +x rhit<br>
// 下载地址<br>
https://dystroy.org/rhit/download<br>
</pre><br>
从crates.io安装，依赖Rust环境，使用以下命令安装：<br>
<pre class="prettyprint">cargo install rhit<br>
</pre><br>
源码安装，依赖Rust环境，将github源码clone之后，进入到rhit文件夹，运行以下命令：<br>
<pre class="prettyprint">cargo install --path .<br>
</pre><br>
<h3>显示字段</h3>Rhit可以自动打开默认目录下的nginx日志文件，也可以在命令行参数中指定日志路径：<br>
<pre class="prettyprint">rhit my/archived/logs<br>
</pre><br>
Nginx常见的日志行是这样的：<br>
<pre class="prettyprint">178.133.125.122 - - [21/Jan/2021:05:49:52 +0000] "HEAD /broot/download/x86_64-pc-windows-gnu/broot.exe HTTP/1.1" 200 0 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"<br>
</pre><br>
它由几个字段组成：日期、远程IP地址、路径、发送的字节等。rhit可以执行对表格进行排序的字段列表，如果未指定，默认按照日期、状态码、来源和路径来显示，如果要制定多个字段，使用逗号进行分割，如-f date,status；显示所有字段，使用-f all。<br>
<br>基于日期。使用--field date，或者缩写为-f date。默认情况下，条形图的长度基于命中数量进行统计，也可以修改排序键以基于发送字节数进行统计。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210320/36ade9738489850db026473692182a38.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210320/36ade9738489850db026473692182a38.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
基于IP。默认情况下不显示远程IP，可以使用rhit -f ip进行显示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210320/e8a4e143782c870441e742d2b5bd13ff.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210320/e8a4e143782c870441e742d2b5bd13ff.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
基于请求方法。默认不显示HTTP请求方法，可以使用rhit -f method进行显示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210320/7ea6dad183731621f23557aaba8f8342.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210320/7ea6dad183731621f23557aaba8f8342.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
基于路径。命令为rhit -f path<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210320/e765d917df6e6bc32b40928cb092b284.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210320/e765d917df6e6bc32b40928cb092b284.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
基于Referer。命令为rhit -f ref<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210320/17335c5fa9e92a63df83bc09686a5218.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210320/17335c5fa9e92a63df83bc09686a5218.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
基于状态码。命令为rhit -f status<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210320/3e7f4dd8df67838dd5cd86c2c6472421.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210320/3e7f4dd8df67838dd5cd86c2c6472421.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>筛选</h3>Rhit提供了一些过滤器，用于筛选结果列表，展示自己想看到或者不想看到的一些数据。<br>
<br>按日期筛选。精确到天，日期格式是年/月/日，如筛选2021/2/15到2021/2/20的数据，也可以筛选大于某个时间、小于某个时间或不包含某个时间（使用'>'，'<'，'!'符号）：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210320/fdfbc6c306a358b6596ae2309a56d630.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210320/fdfbc6c306a358b6596ae2309a56d630.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
按远程IP筛选。参数为-i，筛选特定的IP，或者排除某个特定的IP（使用'!'符号）。<br>
<br>按请求方法筛选。参数为-m，筛选特定方法，或者排除特定的方法。<br>
<br>按请求路径筛选，参数为-p，可以精确匹配，也可以使用正则表达式（例如所有路径均以"download"开头且以"exe"：结尾，参数为 -p 'download.*exe$'）：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210320/6df5ef9dea0d787cad1515c2b778cecd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210320/6df5ef9dea0d787cad1515c2b778cecd.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
按Referer筛选。参数为-r，与按路径筛选的语法一致：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210320/ebd26b58551645f220294c36affe577f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210320/ebd26b58551645f220294c36affe577f.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
按状态码筛选。参数为-s，筛选特定状态码，或者排除特定的状态码。<br>
<br>组合筛选。以上方式可以任意组合。<br>
<h3>排序键</h3>默认情况下，所有表都按照hits进行排序，这就是排序键，排序键的所有值都以粉红色显示，包括直方图。如果对发送字节数更感兴趣，可以将排序键修改为bytes，使用-k b进行更改：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210320/ce2786523fdf24b97e0ffe385e83e92b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210320/ce2786523fdf24b97e0ffe385e83e92b.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
原文链接：<a href="https://mp.weixin.qq.com/s/w7x4YrQCG0a2NUXeqxO4hg" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/w7x4YrQCG0a2NUXeqxO4hg</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            