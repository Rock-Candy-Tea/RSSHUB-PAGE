
---
title: '浏览器界的_千禧虫_：Google已着手测试Chrome 100解决方案'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1227/a718b967112f3d6.webp'
author: cnBeta
comments: false
date: Mon, 27 Dec 2021 03:16:34 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1227/a718b967112f3d6.webp'
---

<div>   
Google Chrome 版本号即将突破 100，从前期测试结果来看该版本可能会导致部分网站无法正常工作。<strong>目前，Google已经着手调查和测试解决方案</strong>。根据 Chromium Bug Tracker，已知受影响的网站主要是那些用 Duda（一个网页设计工具包）开发的网站。<br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/1227/a718b967112f3d6.webp" alt="nqd83i9h.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">这些网站都使用相同的代码来检查你使用的是什么版本的 Chrome。<br style="text-align: left;"></p><p style="text-align: left;">一般来说，如果一个网站需要知道你使用的是什么浏览器以及它的最新版本，它将检查所谓的“用户代理字符串”（User Agent string）。这是一段文字，你的浏览器将其附加到它的每个网络连接上，让网站了解自己。如果你分析一下“用户代理字符串”的实际内容，你会发现有大量的废话，其中大部分是为了保持与 20 世纪 90 年代和 21 世纪初的网站的兼容性。</p><p style="text-align: left;">但是，在这种情况下，这并不是最重要的。让我们看一下 Chrome 浏览器的用户代理字符串的例子。</p><blockquote style="text-align: left;"><p style="text-align: left;">Mozilla/5.0 (<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36</p></blockquote><p style="text-align: left;">在最后，你可以看到我们要找的部分是"Chrome/96.0.4664.45"，它给了我们浏览器的精确版本号。然而，大多数网络开发者可能只关心主要的版本号，在我们的例子中是"96"。</p><p style="text-align: left;">由于用户代理字符串是简单的文本，开发人员需要设计一种方法来解释这些信息以满足他们的需要。在Duda的例子中，开发者选择只读取“Chrome/”之后的前两位数字。这意味着“Chrome/99”将是99，但另一方面，“Chrome/100”将被视为 10 版本。</p><p style="text-align: left;">下一个问题是，Duda 会自动阻止任何低于 40 版本的 Chrome 浏览器--这是 2015 年发布的，如果这能提供一些观点的话。随即，Chrome 99 之后的每个版本的浏览器都会被认为是 10 版本，因此被屏蔽。</p><p style="text-align: left;">那么，如果我们不能抛弃这些网站，可以做些什么呢？</p><p style="text-align: left;">第一个建议就是是改变开发者应该检查 Chrome 浏览器版本的地方。为了老网站的利益，Chrome 将把用户代理字符串的第一个版本号锁定为 99。如果网站开发人员想要检查超过这个版本的具体版本，他们需要查看第二组数字。</p><p style="text-align: left;">例如，Chrome 100.0.1234.56 的浏览器版本在用户代理字符串中会以“Chrome/99.100.1234.56”这样的方式展示。为此，在 chrome://flags 中增加了一个新的标志，让 Googlers 和网络开发人员测试各种网站是否会受到 Chrome 主要版本号位置的这种变化的影响。</p><p style="text-align: left;">将 User-Agent 字符串中的 Chrome 主要版本锁定为 99，并强制将主要版本号放到次要版本位置。这个标志是对 Chrome 100 意外中断的一个备份计划。</p><blockquote style="text-align: left;"><p style="text-align: left;">#force-major-to-minor</p></blockquote><p style="text-align: left;">然而，正如你可能注意到的，在该标志的描述中，这个解决方案被认为是一个"备份计划"。目前的解决方案是由Google与个别开发者联系，了解Chrome 100即将出现的问题。</p><p style="text-align: left;">到目前为止，该公司在这方面的努力实际上有一些运气，因为Duda不是唯一出现问题的网络工具包。直到几天前，所有通过英国的Yell Business创建的网站也被设定为与Chrome 100中断。在个别Googlers的宣传下，Yell Business 为其整个网络修复了这个问题。</p><p style="text-align: left;">目前的希望是，Google能够明确地找到全网所有在Chrome 100发布时出现故障的网站，并就这个问题与它们的开发者联系。如果这些问题能在3月底Chrome 100发布前有足够的时间得到解决，那么对网络开发者来说就根本不需要改变。</p>   
</div>
            