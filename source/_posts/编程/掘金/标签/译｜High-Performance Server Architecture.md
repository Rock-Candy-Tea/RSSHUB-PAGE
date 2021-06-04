
---
title: '译｜High-Performance Server Architecture'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=1175'
author: 掘金
comments: false
date: Wed, 02 Jun 2021 20:06:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=1175'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">介绍</h3>
<p>本文的目的是分享我多年来关于如何开发某种应用程序的一些想法，对于这种应用程序，术语“服务”只是一个无力的近似称呼。更准确地说，将写的与一大类程序有关，这些程序旨每秒处理大量离散的消息或请求。网络服务通常最适合此定义，但从某种意义上讲，实际上并非所有的程序都是服务。但是，由于“高性能请求处理程序”是很糟糕的标题，为简单起见，倒不如叫“服务”万事大吉。</p>
<p>尽管单个程序中多任务处理现在很普遍，但我不会写此类“轻度并行”应用程序。您用来阅读本文的浏览器可能会并行执行某些操作，但是如此低的并行度真的不会带来多少有趣的挑战。当请求处理的基础结构本身是整体性能的瓶颈时，就会出现有趣的挑战，因此改进基础结构实际上会提高性能。对于运行在具有千兆位内存的千兆赫处理器上的浏览器，通过 DSL 线路同时进行六路下载，基础结构成为瓶颈并不常见。此文关注的重点不是用吸管抿水的应用程序，而是从消防水管喝水的应用程序。在硬件功能的边缘，如何做才是真正重要的。</p>
<p>有些人不可避免地会对我的一些意见和建议持怀疑态度，或者认为他们有更好的方法。挺好，我不是想成为上帝的代言人；我发现这些方法对我来说很有用，不仅是它们对性能的影响，而且它们对以后调试或扩展代码的难度也有影响。效果因人而异。如果还有其他方法对您更好，那太好了，但是请注意，我在这里建议的几乎所有方法都曾作为其他方法的替代品而存在，而我曾经尝试过，只是其结果让人厌恶或恐惧。你最喜欢的想法可能会在其中某个故事中占据显著位置，如果让我现在就讲述出来，无辜的读者可能会无聊至死。您不想伤害他们，对吗？</p>
<p>本文的其余部分将围绕我称之为“性能糟糕的四骑士”展开：</p>
<blockquote>
<p>译者注：天启四骑士，战争、瘟疫、饥荒和死亡。</p>
</blockquote>
<ol>
<li>数据拷贝</li>
<li>上下文切换</li>
<li>内存分配</li>
<li>锁竞争</li>
</ol>
<p>最后还将有一个总括的章节，但这些是最大的性能杀手。如果您能够处理大多数请求而无需数据拷贝，无需上下文切换，无需经过内存分配器并且无需竞争锁，那么即使有一些次要问题，您也会拥有一个性能良好的服务。</p>
<h3 data-id="heading-1"><a href="https://www.cyningsun.com/06-02-2021/high-performance-server-architecture-cn.html#%E6%95%B0%E6%8D%AE%E6%8B%B7%E8%B4%9D" title="数据拷贝" target="_blank" rel="nofollow noopener noreferrer"></a>数据拷贝</h3>
<p>这可能是一个很短的章节，原因很简单：大多数人已经吸取了这个教训。人人都知道数据拷贝不好。很明显，对吧？实际上，显而易见可能是您在计算机职业生涯的很早就知道，仅仅是因为有人在几十年前就开始使用这个词了。我知道我的情况就是如此，但我离题了。如今，每门学校课程和每个非正式的指南都涵盖了它。甚至营销人员也发现“零拷贝”是一个很好的热门词汇。</p>
<p>尽管事后看来副本很糟糕，但似乎仍然有些让人错过的细微差别。其中最重要的是，数据拷贝经常是隐藏和伪装起来的。您真的知道您调用的驱动程序或库中的代码是否会进行数据拷贝吗？可能超出您的想象。猜猜PC上的“编程 I/O”是指什么。哈希函数是伪装、非隐藏副本的一个示例，该函数具有副本的所有内存访问开销，并且还涉及更多的计算。一旦指出散列实际上是“拷贝升级版”，显然应该避免使用散列，但我知道至少有一群才华横溢的人，他们必须用艰难的方式来解决这个问题。如果您真的想摆脱数据拷贝，不管是因为它真的会影响性能，还是因为你想把“零拷贝操作”写入黑客会议幻灯片里，您将需要跟踪许多真正属于数据拷贝但并未广而告之的内容。</p>
<p>避免数据拷贝行之有效的方法是使用间接寻址，并传递缓冲区描述符（或缓冲区描述符链），而不是仅仅使用缓冲区指针。每个描述符通常由以下内容组成：</p>
<ul>
<li>整个缓冲区的指针和长度。</li>
<li>缓冲区的实际填充部分的指针和长度，或偏移量和长度。</li>
<li>指向列表中其他缓冲区描述符的前后指针。</li>
<li>引用计数。</li>
</ul>
<p>现在，代码只需将适当的缓冲区描述符的引用计数加一，而不用拷贝一段数据以确保它留在内存中。在某些情况下，这种做法可以非常好地工作，包括典型的网络协议栈的运行方式，但也可能成为一个真正令人头痛的问题。一般来说，很容易在链的开始或结尾添加缓冲区，添加对整个缓冲区的引用以及释放整个链。在中间添加，逐块释放或引用部分缓冲区愈加困难。尝试拆分或合并缓冲区简直让人发疯。</p>
<p>不过，我实际上并不建议所有情况都使用这种方法。为什么不？因为每次要查看头字段时都必须遍历描述符链，这将成为极大的痛苦。确实有比数据拷贝更糟糕的事情。我发现最好的方法是识别程序中的大对象，例如数据块，确保这些大对象按上述方法单独进行分配，这样就不必拷贝它们，也不必过多地操心其他事情。</p>
<p>这就引出了我关于数据拷贝的最后一点：不要过分规避。我已经看到太多的代码通过做更糟糕的事情来避免数据拷贝，例如强制执行上下文切换或中断大型 I/O 请求。数据拷贝代价很高，当您寻找避免冗余操作的地方时，它是您应首先考虑的问题之一，但是收益递减。对代码进行梳理，然后将其复杂度提高一倍，仅仅是为了去掉最后几份数据副本，通常是在浪费本可以更好利用在其他地方的时间。</p>
<h3 data-id="heading-2"><a href="https://www.cyningsun.com/06-02-2021/high-performance-server-architecture-cn.html#%E4%B8%8A%E4%B8%8B%E6%96%87%E5%88%87%E6%8D%A2" title="上下文切换" target="_blank" rel="nofollow noopener noreferrer"></a>上下文切换</h3>
<p>尽管每个人都认为数据拷贝很糟糕，但我却常常为这么多人完全忽略上下文切换对性能的影响而感到惊讶。根据我的经验，在高负载下，上下文切换实际上比数据副本要落后更多的“崩溃”。系统从一个线程到另一个线程所花费的时间，开始多于它在线程内实际执行有用工作所花费的时间。令人惊奇的是，在某种程度上，导致过度上下文切换的原因是显而易见的。上下文切换的第一大原因是活跃线程数多于处理器数。随着活跃线程与处理器的比率增加，上下文切换的数量也会增加——运气好的话会呈线性关系，但通常呈指数关系。这个非常简单的事实解释了为什么每个连接一个线程的多线程设计的伸缩性非常差。对于可伸缩系统来说，唯一可行的选择是限制活动线程的数量，使其（通常）小于或等于处理器的数量。这种方法的一种流行变体是永远只使用一个线程。尽管这种方法确实避免了上下文抖动，也避免了加锁，它也无法实现超过一个处理器的总吞吐量。因此，除非该程序无论如何都是非 CPU 密集型的（通常是网络I/O密集型的），否则它仍然不受重视。</p>
<p>“线程有度”的程序要做的第一件事就是弄清楚如何让一个线程同时处理多个连接。这通常意味着前端使用 select/poll、asynchronous I/O、信号或完成端口，后端是事件驱动的结构。哪种前端 API 最好，许多“宗教战争”已经打过，而且还在继续。Dan Kegel 的 <a href="http://www.kegel.com/c10k.html" target="_blank" rel="nofollow noopener noreferrer">C10K论文</a><br>
是该领域很好的资料。就个人而言，我认为所有 select/poll 和 signal 形式都是丑陋的，因此偏爱 AIO 或完成端口，但实际上并不重要。除了 select()，其他都可以很好地工作，处理程序前端最外层不需要做太多的工作。</p>
<p>多线程事件驱动服务最简单概念模型是在其中心处有一个队列。一个或多个 “listener” 线程读取请求并将其放入队列，一个或多个 “worker” 线程将其从中移除并处理。从概念上讲，这是一个很好的模型，但是人们通常经常以这种方式实现他们的代码。为什么这样做是错的呢？因为上下文切换的第二大原因是将工作从一个线程转移到另一个线程。有些人甚至要求由原始（译者注：listener）线程发送请求的响应，使错误更严重 —— 导致每个请求需要两次上下文切换而非一次。使用“对称的”方法非常重要，在这种方法中，给定线程可以在不更改上下文的情况下，从 “listener” 成为 “worker”，再成为 “listener”。</p>
<p>通常，即使将来的一瞬间，也不可能知道有多少个线程处于活跃状态。毕竟，请求可能随时出现在任何连接上，也可能专用于各种维护任务的“后台”线程在那一刻唤醒。如果您不知道有多少线程处于活跃状态，该如何限制有多少活跃线程？以我的经验，最有效也是最简单的方法之一：使用老式的计数信号量，每个线程在执行“实际工作”时都必须持有该信号量。如果已经达到线程限制，则每个 listen 模式线程可能会在唤醒时可能会产生一个额外的上下文切换，然后阻塞在信号量上，但是一旦所有 listen 模式线程都以这种方式阻塞，它们就不会继续争用资源，直到一个现有线程“退出”，因此系统影响可以忽略不计。更重要的是，这种方法处理维护线程比大多数替代方法更优雅（大部分时间处于睡眠状态，因此不计入活跃线程数）。</p>
<p>一旦将请求处理分为两个阶段（listener 和 worker），并使用多个线程为这些阶段提供服务，就很自然地将处理进一步分为两个以上的阶段。在最简单的形式下，处理一个请求就变成了在一个方向上依次调用各个阶段，然后又在另一个方向上进行调用（对于应答）的问题。但是，事情会变得更加复杂。一个阶段可能代表 “fork”出来两条处理路径的两个互不相同的阶段，或者本身可能会在不调用其他阶段的情况下生成应答（例如，缓存的值）。因此，每个阶段都必须能够指定请求“下一步应该做什么”。由阶段的派发函数的返回值表示，有三种可能：</p>
<ul>
<li>该请求需要传递到另一个阶段（返回值中报站指示阶段的ID或指针）。</li>
<li>请求已完成（特殊的“请求处理完毕”返回值）</li>
<li>请求被阻塞（特殊的“请求阻塞”返回值）。与前面的情况相同，只是请求没有被释放，稍后将由另一个线程继续执行。</li>
</ul>
<p>请注意，在本模型中，请求的排队是在阶段内，而非阶段之间。避免了将请求不断放在后继阶段的队列中，然后立即调用该后继阶段，再次使请求出队的常见愚蠢做法。我称之为没事找事的队列、锁定活动。</p>
<p>将一个复杂的任务分成多个较小的通信部分的想法似乎很熟悉，那是因为它实际上已经很久远了。我的方法源于 1978 年 C.A.R. Hoare 提出的“<a href="http://www.afm.sbu.ac.uk/csp/" target="_blank" rel="nofollow noopener noreferrer">Communicating Sequential Processes</a>”概念，该概念又基于 Per Brinch Hansen 和 Matthew Conway 的思想，这些思想可以追溯到 1963 年 —— 我出生之前！但是，当 Hoare 创造术语 CSP 时，他的意思是抽象数学意义上的“进程”，并且 CSP 进程不必与同名的操作系统实体相关。在我看来，通过单 OS 线程内部类线程的协程以实现 CSP 的常见方法给用户带来了并发的所有麻烦，却又没有任何可伸缩性。</p>
<p>同一时期，Matt Welsh 的 <a href="http://www.cs.berkeley.edu/~mdw/proj/seda/" target="_blank" rel="nofollow noopener noreferrer">SEDA</a> 是一个朝着更明智的方向发展的阶段执行理念的例子。实际上，SEDA 是“正确完成服务架构”的一个很好的例子，它的一些特定的特征值得评论（尤其是那些与我上面概述的特征不同的地方）。</p>
<ol>
<li>SEDA 的“批处理”倾向于强调一次处理多个请求，而我的方法倾向于强调一次处理单个请求的多个阶段。</li>
<li>在我看来，SEDA 的一个显著缺陷是，它为每个阶段分配了一个单独的线程池，只在后台重新分配各个阶段的线程以响应负载。因此，上面提到的引起上下文切换的“1”和“2”原因仍然存在。</li>
<li>在学术研究项目的背景下，用 Java 实现 SEDA 可能说得通。但是，在现实世界中，这种选择可谓不恰当的。</li>
</ol>
<h3 data-id="heading-3"><a href="https://www.cyningsun.com/06-02-2021/high-performance-server-architecture-cn.html#%E5%86%85%E5%AD%98%E5%88%86%E9%85%8D" title="内存分配" target="_blank" rel="nofollow noopener noreferrer"></a>内存分配</h3>
<p>分配和释放内存是许多应用程序中最常见的操作之一。因此，人们已经开发出许多巧妙的技巧来使通用存储器分配器更有效。然而，再聪明也弥补不了这样一个事实：在许多情况下，这种分配器的通用性不可避免地使它们的效率远远低于其他分配器。因此，关于如何完全避免使用系统内存分配器，我有三点建议。</p>
<p>建议一：简单的预分配。我们都知道，静态分配器如果导致程序功能受限，是非常不好的，但是还有许多其他形式的预分配可能会非常有益。通常，原因归结为这样一个事实：即使在此过程中“浪费”了一些内存，通过系统内存分配器的一次访问也要好于几次。因此，如果可以断言同时使用不超过N项，则在程序启动时进行预分配可能是一个有效的选择。即使不是这种情况，也可以在一开始就预先分配请求处理程序可能需要的所有内容，而不是根据需要分配每个内容。除了通过系统分配器在一次行程中连续分配多项的可能性之外，也通常大大简化了错误恢复代码。如果内存非常紧张，那么预分配可能不是一种选择，但在除最极端的情况外的所有情况下，结果通常都是净收益。</p>
<p>建议二：对经常分配和释放的对象使用 lookaside 列表。基本思想是将最近释放的对象放到列表中，而不是真正释放，希望如果很快再次使用，则只需将其从列表中移除，而不用从系统内存中分配。另一个好处是， lookaside 列表的存取转换的实现通常可以跳过复杂的对象初始化/终结。</p>
<p>通常不希望 lookaside 列表无限制地增长，即使程序处于空闲状态也从不释放任何内容。因此，通常有必要执行某种定期的 “sweeper” 任务以释放不活跃的对象，但是如果清理程序引入了不适当的加锁复杂性或竞争，则也不可取。因此，一个好的折衷方案是，lookaside 列表实际上由单独加锁的 “old” 列表和 “new” 列表组成的系统。优先从新列表开始分配，然后从旧列表开始分配，并且仅在万不得已的情况下才从系统中分配；对象总是被释放到新列表中。清理线程的操作如下：</p>
<ol>
<li>锁定两个列表。</li>
<li>保存旧列表的表头。</li>
<li>通过表头赋值，将（以前）新列表变为旧列表。</li>
<li>解锁。</li>
<li>在空闲时将保存的旧列表中的所有对象都释放掉。</li>
</ol>
<p>此类系统中的对象只有在至少一个但不超过两个完整的清除程序间隔不需要时才真正释放。最重要的是，清除程序在执行大部分工作时没有持有任何与常规线程竞争的锁。理论上，相同的方法可以推广到两级以上，但我还没有发现如此做有用。</p>
<p>使用 lookaside 列表的一个担心是列表指针可能会增加对象的大小。根据我的经验，使用 lookaside 列表的大多数对象都已经包含了列表指针，所以考虑此点没有实际意义。但是，即使指针只用于 lookaside 列表，但避免使用系统内存分配器（和对象初始化）方面所节省的开销，将远远弥补额外增加的内存。</p>
<p>建议三：实际上与尚未讨论到的加锁有关，但我仍然要加进来。即使使用 lookaside 列表，锁竞争通常也是分配内存的最大成本。一种解决方案是维护多个私有的 lookaside 列表，这样就绝对不可能争用任何一个列表。例如，每个线程可以有一个单独的 lookaside 列表。出于高速缓存 cache-warmth 的考虑，每个处理器一个列表更好，但是仅在线程无法被抢占的情况下才有效。如有必要，私有 lookaside 列表甚至可以与共享列表相结合，以创建具有极低分配开销的系统。</p>
<h3 data-id="heading-4"><a href="https://www.cyningsun.com/06-02-2021/high-performance-server-architecture-cn.html#%E9%94%81%E7%AB%9E%E4%BA%89" title="锁竞争" target="_blank" rel="nofollow noopener noreferrer"></a>锁竞争</h3>
<p>众所周知，高效的加锁方案很难设计，因此我称之为 “Scylla” 和 “Charybdis”，取自《奥德赛》中的怪物。Scylla 是过于简单和/或粗粒度的锁，是可以或应该并行的串行化的活动，这些活动可以或应该并行进行，从而牺牲了性能和可伸缩性。Charybdis 是过于复杂或细粒度的锁，加锁的空间和加锁的操作时间会再次降低性能。靠近 Scylla 的陷阱是代表死锁和活锁的状态。靠近 Charybdis 的陷阱是代表竞态条件。两者之间，有一个狭窄的渠道代表既高效又正确的加锁……或者在哪？由于锁定往往与程序逻辑紧密相关，因此，如果不从根本上改变程序的工作方式，通常就不可能设计出良好的锁定方案。这就是为什么人们讨厌锁，并试图将不可伸缩的单线程实现合理化的原因。</p>
<p>几乎每个加锁方案都是从“围绕所有事物的一个大锁”开始，并且茫然地希望性能不会太糟。当希望破灭时（几乎总是这样），大锁被分解成小锁，然后继续祈祷，然后重复整个过程，大概直到性能足够为止。但是，通常每次迭代都会增加 20-50％ 的复杂性和锁开销，以减少 5-10％ 的锁竞争。幸运的是，最终结果性能仍然会有些许提高，但实际下降的情况也并不少见。设计师只能挠头了，“我把锁力度做得更细，就像教科书上说的那样”，他想，“那为什么性能会变得更差呢？”</p>
<p>我认为情况变得更糟，因为上述方法从根本上讲是错误的。把“解决方案空间”想象成一座山脉，高点代表好的解决方案，低点代表差的解决方案。问题是，“大锁”的起点几乎总是被各种山谷，马鞍山，小山峰、死胡同与高峰隔开。这是一个经典的爬山问题。想从一个起点爬到更高的山峰，只迈出一小步，从不走下坡路，几乎是行不通的。我们需要的是一种完全不同的接近顶峰的方式。</p>
<p>您要做的第一件事是形成程序加锁的脑中地图。该地图有两个轴：</p>
<ul>
<li>纵轴表示代码。如果您使用的是非分支阶段的阶段体系结构，则可能已经有了一个显示划分的图表，就像每个人都在使用的 OSI 模型网络协议栈那样。</li>
<li>横轴表示数据。在每个阶段中，应将每个请求分配给一个数据集，该数据集使用的资源应该独立于其他任何资源。</li>
</ul>
<p>现在有了一个网格，其中每个单元格表示特定处理阶段中的特定数据集。最重要的是以下规则：两个请求不应处于争用状态，除非它们位于相同的数据集和相同的处理阶段。如果你能做到这一点，你已经成功了一半。</p>
<p>一旦定义了网格，就可以绘制程序的每种加锁类型，下一个目标是确保所得的点尽可能沿两个轴均匀分布。不幸的是，这部分是非常特定于应用的。你必须像钻石切割师一样思考，利用你对程序执行的知识来寻找阶段和数据集之间的自然“解理纹”。它们有时从一开始就很明显，有时很难找到，但回想起来似乎更明显。将代码分为多个阶段是一个复杂的程序设计问题，因此我能提供的内容不多，但以下是一些关于如何定义数据集的建议：</p>
<ul>
<li>如果有某种与请求相关联的块号或哈希或事务ID，那么最好将该值除以数据集的数量。</li>
<li>有时，最好动态地将请求分配给数据集，根据哪个数据集拥有最多的可用资源，而不是请求的某些内在属性。把它想象成现代CPU中的多个整数单元；它们对离散请求流经系统略知一二。</li>
<li>确保每个阶段的数据集分配不同通常是有用的，这样可以保证在一个阶段竞争的请求在另一阶段不会再次竞争。</li>
</ul>
<p>如果您已经将“加锁域”进行了垂直和水平划分，并确保加锁活动均匀地分布在生成的单元格中，则可以确定加锁状态良好。不过，还有一步。您还记得我几段内容之前嘲笑的“小步走”方法吗？它仍然有它的作用，因为现在你处于一个好的起点而不是一个糟糕的起点。用比喻的话来说，你可能已经爬上了这座山脉最高峰之一的斜坡，但你可能还没有到达山顶。现在是时候收集竞争的统计信息了，看看您需要做些什么来改进，以不同的方式拆分阶段和数据集，然后收集更多的统计信息，直到满意为止。如果你做了这些，你一定能从山顶看到美丽的景色。</p>
<h3 data-id="heading-5"><a href="https://www.cyningsun.com/06-02-2021/high-performance-server-architecture-cn.html#%E5%85%B6%E4%BB%96%E5%86%85%E5%AE%B9" title="其他内容" target="_blank" rel="nofollow noopener noreferrer"></a>其他内容</h3>
<p>正如我所承诺的，我已经讨论了服务设计中四个最大的性能问题。不过，特定的服务仍然有其他重要的问题需要解决。主要是要了解平台/环境：</p>
<ul>
<li>存储子系统如何处理较大和较小的请求？顺序还是随机？read-ahead 和 write-behind 的能力如何？</li>
<li>使用的网络协议的效率如何？是否可以设置参数或标志以获得更好的性能？是否有诸如TCP_CORK，MSG_PUSH 或 Nagle-toggling 技巧之类的工具可用于避免发送微小消息？</li>
<li>系统是否支持分散/集中 I/O（例如readv / writev）？使用这些可以提高性能，也可以减轻使用缓冲链的痛苦。</li>
<li>页大小是多少？缓存行大小是多少？在边界上内容对齐是否值得？相对于其他操作，系统调用或上下文切换的成本多高？</li>
<li>reader/writer 加锁原语是否处于饥饿？因何饥饿？事件有“惊群效应”的问题吗？睡眠/唤醒是否有一种恶劣的（但非常常见的）行为，即当 X 唤醒 Y 时，即使 X 还有事情要做，上下文也会立即切换到 Y？</li>
</ul>
<p>我相信我能想出更多这样的问题。相信你也可以。在任何特定情况下，针对任何一个问题做点什么都不值得，但通常至少值得考虑一下。如果您不知道答案 — 其中许多答案在系统文档中找不到 — 请找出答案。编写一个测试程序或微观基准，从经验上寻找答案；无论如何，编写这样的代码本身就是一种有用的技能。如果您要编写在多个平台上运行的代码，那么其中许多问题都与您应该将功能抽象到每个平台库中的点相关，这样您就可以在支持特定功能的平台上实现性能提升。</p>
<p>“知道答案”理论也适用于你自己的代码。找出代码中重要的高级操作是什么，并在不同的条件下对它们进行计时。这与传统的概要性能剖析不太一样；这是衡量 <em>设计</em> 元素，而不是实际的实现。低级优化通常是搞砸设计的人最后的选择。</p>
<p><em>原文：</em> <a href="https://pl.atyp.us/content/tech/servers.html" target="_blank" rel="nofollow noopener noreferrer">High-Performance Server Architecture</a></p>
<p><strong>本文作者</strong>：cyningsun<br>
<strong>本文地址</strong>： <a href="https://www.cyningsun.com/06-02-2021/high-performance-server-architecture-cn.html" target="_blank" rel="nofollow noopener noreferrer">www.cyningsun.com/06-02-2021/…</a><br>
<strong>版权声明</strong>：本博客所有文章除特别声明外，均采用 <a href="http://creativecommons.org/licenses/by-nc-nd/3.0/cn/" target="_blank" rel="nofollow noopener noreferrer">CC BY-NC-ND 3.0 CN</a> 许可协议。转载请注明出处！</p></div>  
</div>
            