
---
title: 'EasySync协同技术指南(中文翻译)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8313'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 02:12:32 GMT
thumbnail: 'https://picsum.photos/400/300?random=8313'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文章由 @快手Docs团队 翻译，转载请注明来处</p>
<h2 data-id="heading-0">1 文档</h2>
<ul>
<li>
<p>一个文档（document）是一个字符（char）列表或一个字符串（string）</p>
</li>
<li>
<p>一个文档也可以被表示为一个变更集（changeset）列表</p>
</li>
</ul>
<h2 data-id="heading-1">2 变更集</h2>
<ul>
<li>
<p>一个变更集表示对文档的一个更改</p>
</li>
<li>
<p>一个变更集可以被应用于一个文档以产生一个新的文档</p>
</li>
<li>
<p>当一个文档被表示为一个变更集列表时，我们认为第一个变更集应用于空文档 []。</p>
</li>
</ul>
<h2 data-id="heading-2">3 变更集表示</h2>
<p>(l→l′)[c1, c2, c3, ...]</p>
<p>l代表文档更改前的长度，</p>
<p>l′代表文档更改后的长度，</p>
<p>[c1, c2, c3,...]是描述更改后文档的一个字符数组（长为l′）。</p>
<p>满足0 ≤ i ≤ l′ 的任意ci 是一个数字整型（int）或一个字符</p>
<ul>
<li>
<p>数字表示在原始文档中保留的字符</p>
</li>
<li>
<p>字符表示插入</p>
</li>
</ul>
<h2 data-id="heading-3">4 变更集约束</h2>
<ul>
<li>
<p>变更集是遵循一定规范的，因而具有可比较性。在计算机内存中, 我们总是对相同的变更集有着同样的表示。如果两个变更集的内存表示有区别，它们一定是不同的变更集。</p>
</li>
<li>
<p>变更集是简洁的。因此，如果在计算机内存中有两种方式表示一个变更集，我们总是使用占用最少字节的那一种。</p>
</li>
</ul>
<p>稍后我们会讨论对变更集表示的优化（采用“strips”和其他类似的技术）。任何变更集表示都必须满足这两个约束条件。</p>
<h2 data-id="heading-4">5 符号表示</h2>
<ul>
<li>
<p>我们用代数乘法符号来表示变更集的应用</p>
</li>
<li>
<p>当变更集被定义为对文档的操作时，文档本身被表示为一个变更集列表，初始化于一个空文档</p>
</li>
</ul>
<p>举例 A = (0→5)[“hello”] B = (5→11)[0−4,“world”]</p>
<p>我们可以把文档 “hello world” 写作A·B或者AB. 注意初始文档可以被表示为变更集 (0→N)[“<文档内容>”]。</p>
<p>当A和B是变更集时，我们也可以把 (AB) 称为A和B的组合，变更集在组合后是封闭的。</p>
<h2 data-id="heading-5">6 变更集组合</h2>
<p>对于任意两个变更集，类似</p>
<p>A = (n1→n2)[···]</p>
<p>B = (n2→n3)[···]</p>
<p>很明显存在第三个变更集C = (n1→n3)[···] 应用于文档X能与先应用A后应用B得到同样的结果。在这种情况下 ，我们写作AB=C。</p>
<p>有了第三节中的表示方法， 很容易计算出两个变更集的组合。</p>
<h2 data-id="heading-6">7 变更集合并</h2>
<p>现在让我们来到文档编辑的真实场景。假定两个不同的用户在同一时间对同一文档做了两个不同的改动，它们不可能直接组合。举例来说, 如果我们有一个文档X，长度是n，我们可能有变更集A = (n→na)[...na characters]，B = (n→nb)[...nb characters] ，且n≠na≠nb。</p>
<p>不可能直接计算 (XA)B，因为B只能被应用于长度为n的文档，而 (XA) 有着na的长度。类似的，A也不能应用于 (XB) 因为(XB) 的长度是nb。</p>
<p>这就是引入合并的原因。合并基于两个应用于同一初始文档的变更集（不能被组合），计算出一个新的变更集，同时保留两者的改动。A和B的合并被写作m(A, B)， 为了让系统工作，我们需要 m(A, B) =m(B, A)</p>
<p>为了建立一个可行的系统，除了到目前为止我们所说的合并机制，还有许多不同的实现。对于遵循以下约束的文本，我们已经给出一个实现。</p>
<h2 data-id="heading-7">8 追赶（follow）</h2>
<p>当用户A和B在他们的屏幕前有着同一文档X时，他们开始分别进行变更A和B，计算m(A, B)是没有用的，因为m(A, B)应用于文档X，但是用户已经在看文档XA和XB了。我们真正想要的是计算B'和A'，使得XAB'=XBA'=Xm(A, B)。</p>
<p>“追赶”计算出变更集B'和A'，它的函数定义f为，当我们计算f(A, B)时，使得Af(A, B) =Bf(B, A) =m(A, B) =m(B, A)</p>
<ul>
<li>
<p>A中的插入变为f(A, B)的保留字符</p>
</li>
<li>
<p>B中的插入变为f(A, B)的插入</p>
</li>
<li>
<p>保留同时在A和B中保留的任何字符</p>
</li>
</ul>
<p>举例 假定我们有一个初始文档X=(0→8)[“baseball”] ，用户A把它修改成了 “basil”，用户B把它修改成了“below”，我们有</p>
<p>X = (0→8)[“baseball”]</p>
<p>A = (8→5)[0−1,“si”,7]</p>
<p>B = (8→5)[0,“e”,6,“ow”]</p>
<p>首先我们根据约束条件计算合并 m(A, B) =m(B, A)</p>
<p>m(A, B) = (8→6)[0,”e”,”si”,”ow”] = (8→6)[0,“esiow”] (注: besiow)</p>
<p>然后我们需要计算follow B' = f(A, B) 和A' = f(B, A).</p>
<p>B′= f(A, B) = (5→6)[0,“e”,2,3,“ow”]</p>
<p>注意数字 0, 2 和 3 是A中的索引 A = (8→5)[0,1,“si”,7]</p>
<p>0 1 2 3 4</p>
<p>0 1 s i 7</p>
<p>A′=f(B, A) = (5→6)[0,1,”si”,3,4]</p>
<p>我们现在可以检查AB′=BA′=m(A, B) = (8→6)[0,“esiow”]</p>
<p>现在我们已经把上述的数学含义彻底弄清楚了，我们可以建立一个客户端/服务端系统来支持多个用户的实时编辑。</p>
<h2 data-id="heading-8">9 系统概述</h2>
<p>有一个服务端保存文档的当前状态。客户端（用户）可以从他们的web浏览器连接到服务端。客户断和服务端保存着状态并且可以实时地互相发送消息。但是由于我们处在一个web浏览器的场景中，客户端之间不能直接发送消息，必须一直通过服务端（这可能与前面的技术有所区别？）</p>
<p>该系统的另一个关键设计特性是客户端必须始终能够编辑文档的本地副本，这样用户就不会因为等待发送或接收数据而被阻止输入。</p>
<h2 data-id="heading-9">10 客户端状态</h2>
<p>在任何时候，客户端都以3个变更集的形式保持着其状态。客户端文档看起来像A·X·Y。</p>
<p>其中A是最新的服务端版本，是来自这个和其他客户端的所有已经提交给服务端的变更集的组合，且服务端已经通知了相关的客户端。初始化为 A =(0→N)[<文档初始内容>].</p>
<p>X是客户端已提交到服务端但尚未得到确认的所有变更集的组合。初始化为 X =(N→N)[0,1,2,...N−1]。表示不变的变更集identity,，我们后面记为IN，</p>
<p>Y是客户端已完成但尚未向服务端提交的所有变更集的组合。初始化为 Y =(N→N)[0,1,2,...N−1]。</p>
<h2 data-id="heading-10">11 客户端操作</h2>
<p>客户端做5件事.</p>
<p>1. 将新的键入合并到本地状态</p>
<p>2. 提交变更集到服务端</p>
<p>3. 监听对已提交变更集的确认</p>
<p>4. 从服务端监听来自于其他客户端的变更集</p>
<p>5. 连接到服务端并且请求初始化文档</p>
<p>当这5个事件发生时，客户端根据下面的关系更新其A·X·Y的表示。随着时间的推移，更改“向左移动”：用户键入时变为Y，将变更集提交到服务端时变为X，服务端确认变更集时变为A</p>
<h3 data-id="heading-11">11.1 新的本地键入</h3>
<p>当一个用户对文档做了一个编辑操作E时，客户端计算(Y·E)的组合并且更新其本地状态，也就是Y←Y·E。也就是如果Y是保存本地未提交的更改的变量，将被赋为新值(Y·E)</p>
<h3 data-id="heading-12">11.2 提交变更集到服务端</h3>
<p>当客户端将其本地更改提交到服务端时，它将传输一个Y的副本，然后把Y赋值给X，IN赋值给Y。就是说：</p>
<ol>
<li>
<p>发送Y到服务端</p>
</li>
<li>
<p>X←Y</p>
</li>
<li>
<p>Y←IN</p>
</li>
</ol>
<p>只要收到确认消息，这种情况每隔500毫秒发生一次。在再次提交前必须收到确认。注意，在第二步发生之前，X总是等于IN，因此不会有任何信息丢失。</p>
<h3 data-id="heading-13">11.3 监听服务端的 ACK 消息</h3>
<p>当客户端收到来自于服务端的ACK消息时</p>
<p>A←A·X</p>
<p>X←IN</p>
<h3 data-id="heading-14">11.4 监听其他客户端的变更集</h3>
<p>当一个客户端监听到另一个客户端的变更集B时，会计算出一个新的A，X和Y，我们分别叫做A'，X'和Y'。它也会计算出一个变更集D，应用于客户端当前的文本视图V。因为AXY必须和当前的视图相等，所以在客户端监听到B之前AXY =V，计算执行后A'X'Y' =VD。</p>
<p>步骤如下</p>
<ol>
<li>
<p>计算 A' = AB</p>
</li>
<li>
<p>计算 X' = f(B, X)</p>
</li>
<li>
<p>计算 Y' = f(f(X, B), Y)</p>
</li>
<li>
<p>计算 D = f(Y, f(X, B))</p>
</li>
<li>
<p>赋值 A←A',X←X',Y←Y'</p>
</li>
<li>
<p>应用D于用户屏幕上显示的当前视图。</p>
</li>
</ol>
<p>在第2、3、4步中的f为追赶操作在第8节中有描述</p>
<p>证明 AXY = V ⇒ A'X'Y' = VD，等价于 A'X'Y' = (AB)(f(B, X))(f(f(X, B), Y))，我们上面提过合并是可以交换的，所以对于任意两个变更集P和Q，</p>
<p>m(P, Q) =m(Q, P) =Qf(Q, P) =Pf(P, Q)</p>
<p>应用于上面的关系，我们得到</p>
<p>A'X'Y' = ABf(B, X)f(f(X, B), Y) // 译注：Bf(B, X) = Xf(X, B)</p>
<p>= AXf(X, B)f(f(X, B), Y) // f(X, B)f(f(X, B), Y) = Yf(Y,f(X,B))</p>
<p>= AXYf(Y, f(X, B)) // D = f(Y, f(X, B))</p>
<p>= AXYD</p>
<p>= VD</p>
<p>正如我们所说的那样</p>
<h3 data-id="heading-15">11.5 连接到服务端</h3>
<p>当客户端第一次连接到服务端时，它首先生成一个随机的唯一ID并将其发送到服务端。客户端记住此ID并且在发送每个变更集到服务端时都携带上。</p>
<p>客户端从服务端接收文档的最新版本，称为HEADTEXT。然后客户端设置：</p>
<p>A←HEADTEXT</p>
<p>X←IN</p>
<p>Y←IN</p>
<p>最后客户端在屏幕上显示HEADTEXT。</p>
<h2 data-id="heading-16">12 服务端概览</h2>
<p>像客户端一样, 服务端也有状态并且执行操作。操作只有在回复来自客户端的消息时才会执行。</p>
<h2 data-id="heading-17">13 服务端状态</h2>
<p>服务端将文档作为一个有序的版本记录列表进行维护。一个版本记录是一个包含一个变更集和作者信息的数据结构</p>
<p>RevisionRecord = &#123;</p>
<p>ChangeSet, // 变更集</p>
<p>Source (unique ID), // 来源（唯一ID）</p>
<p>Revision Number // 版本号，连续顺序，从0开始</p>
<p>&#125;</p>
<p>为了提高效率，服务端还可以存储一个名为HEADTEXT的变量，它是版本记录列表中所有变更集的组合。这是一种优化，因为很明显它可以从一组版本记录中计算出来。</p>
<h2 data-id="heading-18">14 服务端操作概览</h2>
<p>除了维护代表已连接客户端集合的状态以及记住各个客户端中的最新版本号外，服务端还做了两件事：</p>
<ol>
<li>
<p>响应请求初始文档的客户端连接。</p>
</li>
<li>
<p>响应客户端提交的新变更集。</p>
</li>
</ol>
<h3 data-id="heading-19">14.1 响应客户端连接</h3>
<p>当服务端接收到来自客户端的一个连接请求时，它将接收到客户端的唯一ID，并将其存储在服务端的一组已连接的客户端中。然后它向客户端发送HEADTEXT的内容和对应的版本号。最后服务端表明该客户端的版本号是最新的。</p>
<h3 data-id="heading-20">14.2 响应客户端变更集</h3>
<p>当服务端从一个客户端接收到有关客户端变更集C的信息时，它将做5件事：</p>
<p>1. 表明该改动适用于版本号rC（客户端的最新版本)。</p>
<p>2. 创建一个相对于服务端最近版本号（我们称之为rH，H 代表 HEAD）的新变更集C′，C′可以用追赶（第8节）计算出来。请记住，服务端有一系列的变更集</p>
<p>S0→S1→. . . Src→Src+1→. . .→SrH</p>
<p>C′是相对于Src的，但是我们需要计算相对于SrH的。我们可以通过计算f(Src+1，C)来计算出相对于Src+1的新的C（译注：Src+1C′ =m(C,Src+1)= Src+1f(Src+1，C) ）同样，我们可以重复计算Src+2，以此类推，直到C′代表相对SrH为止。</p>
<p>3. 发送C′到所有其他客户端</p>
<p>4. 发送ACK到原始客户端</p>
<p>5. 基于C′和客户端ID创建一个新的版本号记录，并添加到服务端的版本号记录列表中。</p>
<h2 data-id="heading-21">额外话题</h2>
<p>(a) 优化 （strips, 更多缓存等）</p>
<p>(b) 组合、合并和追赶的伪代码</p>
<p>(c) 如何使用作者信息基于谁键入了什么内容对文档进行彩色标记</p>
<p>(d) 如何在客户端和服务端之间保持持久连接</p></div>  
</div>
            