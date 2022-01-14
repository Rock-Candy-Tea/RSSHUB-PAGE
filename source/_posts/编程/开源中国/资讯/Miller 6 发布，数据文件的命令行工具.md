
---
title: 'Miller 6 发布，数据文件的命令行工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1956'
author: 开源中国
comments: false
date: Fri, 14 Jan 2022 07:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1956'
---

<div>   
<div class="content">
                                                                                            <p>Miller 是一个命令行工具，用于查询、调整和重新格式化各种格式的数据文件，包括 CSV、TSV、JSON 和 JSON Lines。</p> 
<h3>用户体验</h3> 
<p>Miller 6 的功能主要由 2021 年 Miller 用户调查结果和 GitHub Issues 中的大量反馈来推动。</p> 
<h3>性能</h3> 
<p>在简单处理方面，性能与 Miller 5 相当，在复杂处理链方面，Miller 6 由于改进了多核利用率，因此性能远远优于 Miller 5，除此之外，CSV I/O 也有明显改善。</p> 
<h3>文档改进</h3> 
<p>文档和在线帮助（<code>mlr --help</code>）已经被完全重写。</p> 
<h3>改进 Windows 体验</h3> 
<p>Miller 最初是为类 Unix 操作系统开发的，包括 Linux 和 macOS。Miller 5.2.0 成为了第一个支持 Windows 的版本。从 6.0.0 版本开始，Miller 直接在 Windows 上构建。</p> 
<p>现在，Windows 上的体验与 Linux，NetBSD / FreeBSD和 macOS 上的体验几乎相同，MSYS2 不再是必需的 。</p> 
<h3>输出着色</h3> 
<p>每当输出到终端时，Miller 都会对键和值使用单独的可自定义颜色。</p> 
<h3>改进的命令行解析</h3> 
<p>Miller 6 具有 getoptish 命令行解析：</p> 
<ul> 
 <li><code>xyz</code>自动扩展为<code>x -y -z</code>，例如<code>mlr cut -of shape,flag</code>与<code>mlr cut -o -f shape,flag</code>相同</li> 
 <li><code>-foo=bar</code>会自动扩展为<code>-foo bar</code>，因此（例如<code>mlr --ifs=comma</code>与<code>mlr --ifs comma</code>相同.</li> 
</ul> 
<h3>改进了 DSL 解析的错误消息</h3> 
<p>对于<code>mlr put</code>和<code>mlr filter</code>，解析错误消息现在包含位置信息：</p> 
<pre>mlr: cannot parse DSL expression.
Parse error on token ">" at line 63 columnn 7.
</pre> 
<h3>脚本</h3> 
<p>脚本现在更容易支持带有<code>sh</code>的<code>#!</code>，以及现在支持带有<code>mlr -s</code>的<code>#!</code>。对于 Windows，也可以使用<code>mlr -s</code>。这些变化有助于减少反斜杠引起的混乱，让用户在少打字的同时做更多的事情。</p> 
<h3>改进的国际化支持</h3> 
<p>现在可以用 UTF-8 编写字段名称、局部变量等，例如<code>mlr --c2p filter '$σχήμα == "κύκλος"' παράδειγμα.csv</code>。</p> 
<h3>改进的日期时间/时区支持</h3> 
<p>包括支持通过函数参数指定时区，作为<code>TZ</code>环境变量的替代方法。</p> 
<h3>对压缩输入的进程内支持</h3> 
<p>除了<code>--prepipe gunzip</code>之外，在 Miller 6 中现在还可以使用<code>--gzin</code>标志。如果你的文件以<code>.gz</code>结尾，那你甚至无需这样操作，Miller 将通过文件扩展名自动检测并自动解压缩<code>mlr --csv cat foo.csv.gz.z</code></p> 
<h3>支持读取网络网址</h3> 
<p>可以读取带有<code>https://</code>和<code>http://</code> 和<code>file://</code> 前缀的输入:</p> 
<pre>mlr --csv sort -f shape \\  <https://raw.githubusercontent.com/johnkerl/miller/main/docs/src/gz-example.csv.gz>
</pre> 
<h3>改进 JSON / JSON Lines 支持和数组</h3> 
<p>数组现在在 Miller 的<code>put</code>/<code>filter</code>编程语言中受支持，此外<code>array</code>现在是一个关键字，因此它不再可用作局部变量或 UDF 名称。</p> 
<h3>改进数值转换</h3> 
<p>Miller 6 最核心的部分是深度重构如何从文件内容解析数据值、如何推断类型以及如何将它们转换回文本到输出文件。</p> 
<p>在 Miller 5 及更低版本中，所有值都存储为字符串，然后仅根据需要转换为 int/float。</p> 
<p>在 Miller 6 中，可解析为 int/float 的东西从读取输入数据的那一刻起就被视为 int/float，并且它们通过动词链传递。</p> 
<h3>重复字段名称的重复数据删除</h3> 
<p>默认情况下，除 JSON / JSON Lines 之外的所有文件格式的字段名称都会被重复数据删除。</p> 
<h3>对 IFS 和 IPS 正则表达式支持</h3> 
<p><code>IFS</code>和<code>IPS</code>可以是正则表达式：分别使用<code>--ifs-regex</code>或<code>--ips-regex</code>代替<code>--ifs</code>或<code>--ips</code>。还可以使用<code>--ifs space --repifs</code>或<code>--ifs-regex '()+'</code>。</p> 
<h3>大小写折叠排序选项</h3> 
<p>sort 现在接受<code>-c</code>和<code>-cr</code>选项，用于大小写折叠的升序/降序排序。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmiller.readthedocs.io%2Fen%2Flatest%2Fnew-in-miller-6%2F" target="_blank">https://miller.readthedocs.io/en/latest/new-in-miller-6/</a></p>
                                        </div>
                                      
</div>
            