
---
title: 'Linux彩蛋：gimme gimme gimme'
categories: 
 - 图片
 - 煎蛋
 - 首页
headimg: 'https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/01/ce1740cb2daa1eb128bf74c4355f65d9.jpg!custom'
author: 煎蛋
comments: false
date: Tue, 07 Sep 2021 04:10:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/01/ce1740cb2daa1eb128bf74c4355f65d9.jpg!custom'
---

<div>   
<blockquote><p>这是一个接近十年的彩蛋</p></blockquote><img src="https://cors.zfour.workers.dev/?http://img.jandan.net/news/2019/01/ce1740cb2daa1eb128bf74c4355f65d9.jpg!custom" referrerpolicy="no-referrer"><p>投稿：<strong>Uing</strong></p>
<p>如果你使用 Linux 系统，在大多数的发行版上，在<strong>半夜十二点半</strong>，打开终端 (Terminal)，输入<code>man</code>, 你会看到奇怪的东西：</p>
<blockquote><p>shell<br>
gimme gimme gimme </p></blockquote>
<p>这是一个接近十年的彩蛋，也是四年前才被一个开发者发现。</p>
<p>那这个彩蛋是什么意思呢？又是谁这么无聊大半夜一直输入<code>man</code> 去能发现这个彩蛋呢？</p>
<p>一切都从 StackExchange 的一个<a href="https://unix.stackexchange.com/questions/405783/why-does-man-print-gimme-gimme-gimme-at-0030">问题</a>说起。</p>
<p>捷克的开发者<a href="https://unix.stackexchange.com/users/173916/jaroslav-kucera">Jaroslav Kucera</a> 发现一个奇怪的现象，他的一个集成测试总是在半夜十二点半失败。这个测试一直在运行，而且不依赖外部网路，但总是在 12:30am 这个时间失败。追根溯源后他发现，是因为用了一个命令<code>man -w</code>去获取系统 <code>man</code> 文档的地址。<code>man</code> 是 POSIX 系统的文档帮助命令，是manual的缩写。(有些技术BBS论坛会看到RTFM这个缩写，表示 read the f**king manual，说明你的问题在文档清楚的写着，不要浪费大家的时间)</p>
<p>Jaroslav发现，在任何其他时间，<code>man -w</code>都给给出文档的目录地址，但在12:30am就会出现这个奇怪的信息：</p>
<blockquote><p>shell<br>
gimme gimme gimme </p>
<p>/usr/local/man:/usr/local/share/man:/usr/share/man</p></blockquote>
<p>而Jaroslav 的测试脚本默认用第一行作为目录去解析，而<code>ginme ginme ginme</code>显然不是目录，自然就失败了。</p>
<p>很自然地 Jaroslav在 StackExchange 问了这个<a href="https://unix.stackexchange.com/questions/405783/why-does-man-print-gimme-gimme-gimme-at-0030">问题</a>。当然，有问题自然有答案(？)，很快 <a href="https://unix.stackexchange.com/users/154641/marnanel-thurman">Marnanel</a> 就自首了：</p>
<blockquote><p>markdown<br>
Dear @colmmacuait, I think that if you type "man" at 0001 hours it should print "gimme gimme gimme". #abba  @marnanel - 3 November 2011</p></blockquote>
<p>呃，是我的错，我做出的建议。Sorry</p>
<p>基本上Commit的信息就是整个故事。man 的维护者是我的好基友，六年前的时候我开玩笑地建议他如果有人大半夜之后用了man的命令，应该打印出 "gimme gimme gimme" .....</p>
<p>没想到他真的干了，而只有少数人发现了这秘密，我们也快忘记这个事情了，直到今天。</p>
<p>那这个“gimme gimme gimme”到底什么意思呢？ Marnanel 回答说因为 <a href="https://en.wikipedia.org/wiki/ABBA">Abba</a> 乐队著名的 <a href="https://www.youtube.com/watch?v=XEjLoHdbVeE">《gimme gimme gimme! (a <strong>man</strong> after midnight)》(半夜后给我找一个男人)</a> </p>
<p>Marnanel 也没有想到这会导致任何问题，因为这真的只能是一个彩蛋(不影响关键功能的额外功能)，而不是一个bug。</p>
<p>当然，你永远不知道你的用户会怎么用你的产品，例如在另一个<a href="https://phabricator.wikimedia.org/T273741">事件</a>，Wikimedia发现从印度突然每天向某个<a href="https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/AsterNovi-belgii-flower-1mb.jpg/1280px-AsterNovi-belgii-flower-1mb.jpg">图片</a>发来9千万的下载需求，最后发现印度一个开发者在开发App过程中用了Wikimedia的图片链接，只是下载图片但不显示，而这个App 因为中国抖音在印度被封禁而作为替代品流行起来，最后导致Wikimedia遭受无妄之灾。</p>
<p>最后，对着问题的修复就是：<code>man -w</code>不会触发这个彩蛋，其他情况才会。</p>
<p><strong>如何触发这个彩蛋</strong></p>
<blockquote><p>shell<br>
man<br>
gimme gimme gimme </p></blockquote>
<p><strong>源代码</strong></p>
<blockquote><p>c<br>
src/man.c-1167- if (first_arg == argc) &#123;<br>
src/man.c-1168-   /* http://twitter.com/#!/marnanel/status/132280557190119424 */<br>
src/man.c-1169-   time_t now = time (NULL);<br>
src/man.c-1170-   struct tm *localnow = localtime (&now);<br>
src/man.c-1171-   if (localnow &&<br>
src/man.c-1172-       localnow->tm_hour == 0 && localnow->tm_min == 30)<br>
src/man.c:1173:     fprintf (stderr, "gimme gimme gimmen");
</p></blockquote>
<p><a target="_blank" rel="external" href="http://git.savannah.nongnu.org/cgit/man-db.git/commit/src/man.c?id=002a6339b1fe8f83f4808022a17e1aa379756d99">commit</a></p>  
</div>
            