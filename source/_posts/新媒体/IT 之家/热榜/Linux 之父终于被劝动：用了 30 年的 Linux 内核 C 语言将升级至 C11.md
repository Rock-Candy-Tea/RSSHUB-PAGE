
---
title: 'Linux 之父终于被劝动：用了 30 年的 Linux 内核 C 语言将升级至 C11'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2022/2/c6069040-f8f5-4f78-862e-49ef8364b674.png'
author: IT 之家
comments: false
date: Fri, 25 Feb 2022 06:00:46 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/2/c6069040-f8f5-4f78-862e-49ef8364b674.png'
---

<div>   
<p data-vmark="7afb">还在使用 89 年版 C 语言的 Linux 内核，现在终于要做出改变了。今天，Linux 开源社区宣布，<span class="accentTextColor">未来会把内核 C 语言版本升级到 C11</span>，<span class="accentTextColor">预计 5.18 版之后生效</span>，也就是今年 5 月。</p><p data-vmark="f162" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/2/c6069040-f8f5-4f78-862e-49ef8364b674.png" w="620" h="250" alt="Linux" title="Linux 之父终于被劝动：用了 30 年的 Linux 内核 C 语言将升级至 C11" width="620" height="250" referrerpolicy="no-referrer"></p><p data-vmark="3c79">这个决定很突然，从发起问题到官方声明，不过才一个星期，要知道说服固执的 Linux 之父 Linus Torvalds 可不是件容易的事。事情的原因，说起来还有那么一点偶然的因素。</p><h2 data-vmark="f571">一个 bug 的连锁反应</h2><p data-vmark="354c">问题的起源是来自上周的一次 Linux 社区讨论。</p><p data-vmark="9a60">一位名叫 Jakob Koschel 的博士生，在研究阻止与内核链表 primitive 相关的预测执行漏洞时，发现了这样一个问题。</p><p data-vmark="4049"><span class="accentTextColor">Linux 内核广泛使用由 struct list_head 定义的双向链表</span>：</p><pre>struct list_head &#123;
    struct list_head *next, *prev;
    &#125;;</pre><p data-vmark="11d1">这种结构通常嵌入到其他结构中。通过这种方式，可以使用任何相关的结构类型制作链表。</p><p data-vmark="c92a">除此之外，内核还提供大量可用于遍历和操作链表的函数和宏。list_for_each_entry () 就是其中之一，这是伪装成一种控制结构的宏。问题就出在这个宏上。假设内核包含如下结构：</p><pre>struct foo &#123;
        int fooness;
    struct list_head list;
    &#125;;</pre><p data-vmark="4f78">list 中的元素可用于创建 foo 结构的双向链表。假设有一个叫做 foo_list 的结构声明作为此类链表的头，使用以下代码可以遍历此链表：</p><pre>struct foo *iterator;

    list_for_each_entry(iterator, &foo_list, list) &#123;
        do_something_with(iterator);
    &#125;
    /* Should not use iterator here */</pre><p data-vmark="0367">list 参数告诉宏在 foo 结构中 list_head 结构的名称。这个循环将为列表中的每个元素执行一次，迭代器指向该元素。由此导致了 USB 子系统中的一个 bug：传递给该宏的迭代器在退出宏后还能被使用。</p><p data-vmark="26cd">这是一件危险的事情，所以 Koschel 提交了一个修复补丁，在循环后停止使用迭代器搞定了 bug。</p><p data-vmark="6eed" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/2/883fe114-cef5-4f83-bfd7-f5ef6797fadd.png" w="552" h="414" alt title="Linux 之父终于被劝动：用了 30 年的 Linux 内核 C 语言将升级至 C11" width="552" height="414" referrerpolicy="no-referrer"></p><h2 data-vmark="4e62">说服 Linus</h2><p data-vmark="aefc">但是 Linus Torvalds 本人并不太喜欢这个补丁，也没有看到它与预测执行漏洞的关系。在 Koschel 详细解释后，Linus 承认这只是一个普通的 bug。</p><p data-vmark="e32f">然而事情并没有那么简单，Linus 不久后意识到了真正的根源：传递给链表遍历宏的迭代器，必须在循环本身之外的范围内声明。这种非预测性 bug 发生的原因是，C89 中没有“在循环中声明变量”。</p><p data-vmark="898a">像 list_for_each_entry () 这样的宏，从根本上总是将最后一个 HEAD 入口泄漏到循环之外，仅仅是因为我们不能在循环本身中声明迭代器变量。</p><p data-vmark="07c8">如果可以编写一个可以声明自己的迭代器列表遍历宏，那么迭代器在循环之外将不可见，并且不会出现此类问题。但是，由于内核停留在 C89 标准上，因此无法在循环中声明变量。</p><p data-vmark="cff5">Linus 决定，那咱们还是升级吧，也许是时候转向 C99 标准了。虽然它也有 20 多年的历史，但至少比 C89 新，可以在循环中声明变量。</p><p data-vmark="03e4">既然 C89 如此陈旧，这么多年还没做出改变呢？Linus 说，那是因为我们在一些古老的 gcc 编译器版本中遇到了一些奇怪的问题，不能随便升级。</p><p data-vmark="a4a0" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/2/f722fcce-e23a-4e9c-87de-00b73bdc78a8.png" w="781" h="499" alt title="Linux 之父终于被劝动：用了 30 年的 Linux 内核 C 语言将升级至 C11" width="781" height="499" referrerpolicy="no-referrer"></p><p data-vmark="2984">但是，现在 Linux 内核已将 gcc 的最低要求提升至 5.1 版，因此过去那些奇怪的 bug 应该不会有了。</p><p data-vmark="c3d7">而另一位核心开发者 Arnd Bergmann 认为，咱们完全可以升级到 C11 甚至更高版本。但如果升级到 C17 或 C2x，会破坏对 gcc-5/6/7 的支持，因此升级到 C11 更容易实现。</p><p data-vmark="18ee">最终，Torvalds 赞成这个想法：“好的，请提醒我，让我们在 5.18 合并窗口的早期尝试一下。”接下来迁移到 C11 可能会导致一些意想不到的 bug，但如果一切顺利，下一个 Linux 内核版本将正式转向 C11。</p><p data-vmark="84a7">参考链接：</p><p data-vmark="dba7">[1]<span class="link-text-start-with-http">https://lwn.net/SubscriberLink/885941/01fdc39df2ecc25f/</span></p><p data-vmark="214e">[2]<span class="link-text-start-with-http">https://news.ycombinator.com/item?id=30459634</span></p>
          
</div>
            