
---
title: 'B 端设计总结（一）：设计体系&模态对话框'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.woshipm.com/wp-files/2022/09/S7RQtFHmXSNdzRmtABDY.png'
author: 人人都是产品经理
comments: false
date: Mon, 19 Sep 2022 00:00:00 GMT
thumbnail: 'https://image.woshipm.com/wp-files/2022/09/S7RQtFHmXSNdzRmtABDY.png'
---

<div>   
<blockquote><p>作为一名产品经理，可能会遇到没有资源给你做交互，也没有资源给你画UI的情况，这种时候便需要学会自给自足。这个系列是作者在两年中“自给自足”做设计的一些发现，本文分析了设计体系和模态对话框，一起来看一下吧。</p>
</blockquote><p><img data-action="zoom" class="aligncenter size-full wp-image-5610073" src="https://image.woshipm.com/wp-files/2022/09/S7RQtFHmXSNdzRmtABDY.png" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>众所周知（大雾，黑帕云这样的产品几乎使用了所有类型 B 端的组件。</p>
<p>由于我司设计资源有限，所以在拥有了组件库、设计师定好了设计规范之后，作为产品经理就直接可以手撸设计稿了。</p>
<p>作为一个长大了的产品经理，有时候没有资源给你做交互没有资源给你画 UI 的，你要自己学会自给自足。</p>
<p>这个系列就是作为产品经理的我，在这两年中“自给自足”做设计的一些总结与发现。</p>
<p>自给自足的前提是，前面说的组件库和设计规范，即拥有一个设计体系（Design System）。</p>
<h2 id="toc-1">01 什么是设计体系？</h2>
<p>关于设计体系的定义和内容各家都不同，我找出来了以下案例供参考。</p>
<h3>1. 《设计体系：数字产品设计的系统化方法》</h3>
<p>Tilio（一个写作和笔记应用）联合创始人，有十年 UX 设计经验的阿拉·霍尔马托娃在《设计体系：数字产品设计的系统化方法》一书中这么定义：</p>
<p>设计体系是为了实现数字产品的目的而组织起来的一套相互关联的模式和共享实践。模式指的是界面中那些重复的要素：用户流程、交互方式、按钮、文本框、图标、配色、排版、文案，等等。实践则是我们如何创建、捕获、共享和使用这些模式，尤其是在团队协作时做这些事情的方法。</p>
<p>书中将设计体系分成以下几个部分：设计目的、设计原则、组件库、样式指南，以及用于提高设计师和开发人员沟通效率的工作流程和实用工具。</p>
<p>整理之后，可以参考下图：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端设计总结·前言：设计体系" src="https://image.woshipm.com/wp-files/2022/09/iGFUvY9m6QEJ83Bt1IPQ.png" alt="B 端设计总结·前言：设计体系" width="1014" referrerpolicy="no-referrer"></p>
<h3>2. Salesforce：Lightning Design System</h3>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端设计总结·前言：设计体系" src="https://image.woshipm.com/wp-files/2022/09/Cr0D1kw1nOtaYxwhXTLh.png" alt="B 端设计总结·前言：设计体系" width="1014" referrerpolicy="no-referrer"></p>
<h3>3. Material Design</h3>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端设计总结·前言：设计体系" src="https://image.woshipm.com/wp-files/2022/09/JCDUWyqNN7BZYBHm6f9V.png" alt="B 端设计总结·前言：设计体系" width="1014" referrerpolicy="no-referrer"></p>
<p>可以发现，以上设计体系无论如何定义概念，都是由<strong>设计原则+设计指南+一些基础的元素（比如 Design Token、Material Foundation、Icons）+组件库+其他资源工具</strong>构成。</p>
<p>形成这些内容的目的都是为了给自己产品建立一套保证设计质量、提升设计决策、提升沟通效率的“工具包”，从而让产品形成自己的符合设计原则的风格。</p>
<p>所以设计体系是什么不重要，<strong>重要的是如何在遵循设计原则下，能够高效做出高质量的设计。</strong></p>
<h2 id="toc-2">02 设计原则（Design Principes）</h2>
<p>一个开源设计原则和方法的网站 Design Principle这样定义设计原则：Design Principles are a set of considerations that form the basis of any good product.</p>
<p>译为“设计原则是构成任何好产品的一套基础考虑因素。”</p>
<p>比如 Salesforce 的设计原则是：清晰、高效、一致、美观。并且优先级由前到后。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端设计总结·前言：设计体系" src="https://image.woshipm.com/wp-files/2022/09/eSAXSTvxcVA8V3kf1xII.png" alt="B 端设计总结·前言：设计体系" width="586" height="658" referrerpolicy="no-referrer"></p>
<p>可以理解为 Salesforce 会追求清晰大于高效、一致、美观，比如在产品设计中，让用户清楚的看到、理解、自信地去操作要比任何事情都要重要。</p>
<p>这个准则很容易理解，可以推论出 Salesforce 在度量体验时，将“易用性”放在了第一位，即作为一个 SaaS 产品，不能有任何让用户产生疑惑的地方。如果在设计上的美观而要牺牲清晰，这就是不可取的。</p>
<h2 id="toc-3">03 组件库</h2>
<p>有了设计原则之后，下一步是需要一个组件库。这里说的组件库囊括了无论是原子化的颜色、字体、阴影、Icon 这些基本的元素，还包括了已经封装好的组件，如 Button、Alert、Toast、Text Input。</p>
<p>关于为什么要组件化，也不多说了，之前看过一篇阅文体验设计 YUX 的《组件化思维—— 适应并推动业务及产品变革的设计案例》写得非常清楚。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端设计总结·前言：设计体系" src="https://image.woshipm.com/wp-files/2022/09/PpCQN9pUraIZOLrcyei2.png" alt="B 端设计总结·前言：设计体系" width="901" height="487" referrerpolicy="no-referrer"></p>
<p>接下来我通过 Minecraft 这个游戏来总结了组件库。</p>
<p>玩过生存模拟类游戏大家都知道，在游戏中会有一些可以靠双手劳动得来的基础材料，比如砍树砍来的木头、地上捡的石头、挖矿挖的燧石。这些基础材料可以合成一些简单处理过的材料，比如把木头合成为木板。然后可以再把半成品进一步加工，比如木棍。</p>
<p>在 Minecraft 这个游戏中，如果玩家要制造一个弓箭，需要一个弓和一个箭。弓和箭的合成又需要一些半成品和成品或者原材料来加工制作，如下图：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端设计总结·前言：设计体系" src="https://image.woshipm.com/wp-files/2022/09/WqBYVirGdqR4KzQeaZLW.png" alt="B 端设计总结·前言：设计体系" width="1016" referrerpolicy="no-referrer"></p>
<p>对应在设计组件库中可以对照查看，一个完整的页面是可以通过一些元素、控件、组件、大组件组成：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端设计总结·前言：设计体系" src="https://image.woshipm.com/wp-files/2022/09/WojLgmze787DNEO6cvhN.png" alt="B 端设计总结·前言：设计体系" width="1497" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">04 适用人群</h2>
<p>关于 「B 端设计总结」这一系列，主要是我个人在已有了我们的设计规范和组件库后，“自给自足”的情况下探索出来的一些组件使用规则，更偏向<strong>产品经理</strong>或者<strong>交互设计师</strong>来参考。</p>
<p>所以系列中不会写设计规范，比如说字号、颜色、间距等等这些属于设计规范中内容。<strong>而是基于已有的规范，总结之前我们功能中涉及到的该使用哪些组件，也可以称之为狭义上的设计指南（Design Guidelines）或者设计模式（Design Patterns）</strong>。</p>
<h2 id="toc-5">05 设计原则 Design Principes</h2>
<p>正式开始之前，想整理一个合格的设计应该有哪些方面的考量因素，这样能够帮助我们在做设计时，尽大可能地保证设计的质量。</p>
<p>在前言中提到设计原则，使用了 Salesforce 作为案例介绍了他们的设计原则是：清晰、高效、一致、美观。</p>
<p>但这更像是宏观层面的品牌原则，不仅是设计，而是覆盖在方方面面传递给用户的感知。</p>
<p>而国内的设计团队，会把设计原则落实在细节。这也更通用、更加能指导设计执行。</p>
<p>比如腾讯云的 Element UI 的设计原则是：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端设计总结2：模态对话框" src="https://image.woshipm.com/wp-files/2022/09/XcNn7hrofBJRXZxW9Q3A.png" alt="B 端设计总结2：模态对话框" width="844" referrerpolicy="no-referrer"></p>
<p>京东的 LEGAO Design 的设计原则是：一致性、可控性、秩序性、提高效率、及时反馈、简洁美观、宽容性。</p>
<p>这两个设计团队给出的设计原则都包含了一致、反馈、效率、可控，LEGAO Design 在基础上增加了秩序性、简洁美观和宽容性。</p>
<p>在 LEGAO Design 的设计原则中有非常详尽的举例和说明，在此就不搬运了，建议像我一样没有设计基础的产品经理同学仔细学习。</p>
<p>说点儿不同的。</p>
<p>其中 Element Design 和 LEGAO Design 的“可控”稍有不同，Element Design 的可控包含两个方面：</p>
<ol>
<li>用户的决策是可控的，要根据场景给予操作建议或安全提示，但不能代替用户决策。</li>
<li>结果要求是可控的，用户可以自由决策，包括撤销、回退和终止当前操作。</li>
</ol>
<p>LEGAO Design 在此基础上将“用户决策”和“结果可控”结合在一起，认为在危险操作或者破坏性操作需要提前告知用户，并且应该要提供撤销、回退和终止等操作。</p>
<p>另外还对“可控”增加了“进度可控”：清晰地告知用户当前处在系统的什么位置，从哪里来，可以到哪里去。比如提供清晰便捷的导航方式，非必要条件下导航各个标签权重保持一致，不要因为差异化对用户产生选择性干扰。</p>
<p>此外， LEGAO Design 在可控的基础上，格外增加了“宽容性”，声明应当允许用户犯错：</p>
<p>设计应该是帮助用户避免犯错，当危险发生时能保护用户免受伤害。宽容性设计是通过约束和良好的功能可见性来防止错误的发生，能提示潜在的危险，当某一选择能带来伤害时会要求先确认后执行。<strong>宽容性设计允许错误发生时的动作可逆性操作。</strong></p>
<p>在《交互设计精髓中》也单独列了一章来讲“防止错误，通知决定”。</p>
<p>没有人能够保证所有的设计都是“清晰”（Salesforce 的 Design Principe）的，即便是设计是清晰的，也会有意外的情况。所以好的设计应该是清晰，并且允许用户犯错的。</p>
<p>容错处理能够在心理上暗示<strong>鼓励用户安心地多去探索你的产品</strong>。</p>
<p>而在一些情况上，容错处理有较大的成本，还来不及进入开发，这时应该换一种思路：<strong>我们需要尽可能地拦截错误的发生</strong>（这一部分见文末的小节「危险提示 Danger Alert」）。</p>
<p>设计原则说的差不多了，下面开始这个系列的正文。</p>
<h2 id="toc-6">06 模态框 Modal</h2>
<p>在写什么是模态对话框（Modal Dialog）之前，先来写写模态框（Modal）和对话框（Dialog）。</p>
<p>模态框一词最早是从技术同事那听来的，因为我那会儿一直管这些叫弹框，事实也确实是如此。</p>
<p>在维基百科中这么定义：</p>
<p>In user interface design for computer applications, a modal window is a graphical control element subordinate to an application’s main window.</p>
<p>A modal window creates amodethat disables the main window but keeps it visible, with the modal window as achild windowin front of it. Users must interact with the modal window before they can return to theparentapplication. This avoids interrupting theworkflowon the main window. Modal windows are sometimes calledheavy windowsormodal dialogsbecause they often display adialog box.</p>
<p>不专业地翻译一下：</p>
<p>在应用程序的交互设计中，模态窗口是一个从属于主窗口的图形控制元素。</p>
<p>一个模态窗口创建后，主窗口就失效了，但仍然保持可见。模态窗口能够作为一个子窗口在主窗口的前面。此时用户必须先与模态窗口进行交互，才能返回到父窗口。这避免了中断主窗口的工作流程，模态窗口有时候也被称为重窗口（？）或者模态对话框，因为他们经常以对话框形式展示。</p>
<p>在一个 React UI框架 Material-UI中这么描述模态框：</p>
<p>“模态框”（Modal）这个词有时也被用来指代“对话框”，但是这种用法属于误用。模态框的窗口描述了 UI 的一部分。如果一个元素阻挡了用户与应用的其它部分的互动，这个元素就是模态的。</p>
<p>简单总结就是：<strong>当这个模态框被打开后，当前的所有进程都被阻断了，直到这个模态框关闭。</strong></p>
<p>基于上述的定义，归纳模态框常见的类型可以有以下几种：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端设计总结2：模态对话框" src="https://image.woshipm.com/wp-files/2022/09/mVjHQBWdGsprdCZX8bTx.png" alt="B 端设计总结2：模态对话框" width="1014" referrerpolicy="no-referrer"></p>
<p><strong>注意</strong>：这些类型不代表只属于模态，也可以以非模态形式存在。</p>
<h2 id="toc-7">07 对话框 Dialog</h2>
<p>第一次接触“Dialog”这个词还是在《交互设计精髓》中，书中给了很明确的概念：<strong>对话框以对话的方式让使用者参与进来，在对话框中它给出消息或要求输入。</strong></p>
<p>对话框又可以分为模态（Modal）和非模态（Modeless）两种类型。</p>
<p>模态框在前面已经描述过了，与之相反的就是非模态：当非模态对话框被打开后，用户可以运行其他事情。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端设计总结2：模态对话框" src="https://image.woshipm.com/wp-files/2022/09/wyq392xvVda3LBW9rPUW.png" alt="B 端设计总结2：模态对话框" width="1014" referrerpolicy="no-referrer"></p>
<p>关于为什么要使用模态对话框这种类型，简单快速地可以使用这样的决策原则：<strong>有重要的信息需要来阻断当前的进程，希望用户必须完成操作之后才能继续往下进行。</strong></p>
<h2 id="toc-8">08 模态对话框 Modal Dialog</h2>
<p>这篇文章主要写我们常用的模态对话框。</p>
<p>在《交互设计精髓》中，将模态对话框按照“目的导向”分为五种类型：</p>
<ol>
<li>属性（Property）</li>
<li>功能（Function）</li>
<li>进度（Process）</li>
<li>通知（Notification）</li>
<li>公告（Bulletin）</li>
</ol>
<p>因为书中也没有具体举例，所以我接下来会按照这五种类型列举在黑帕云中的对话框示例。</p>
<h3>1. 属性对话框 Property Dialog</h3>
<p>属性对话框常见在一些设置、详情中，比如电脑的系统设置、黑帕云的小组件配置。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端设计总结2：模态对话框" src="https://image.woshipm.com/wp-files/2022/09/lbdKOUm7rG9GWDwpGbIb.png" alt="B 端设计总结2：模态对话框" width="1014" referrerpolicy="no-referrer"></p>
<p>这个对话框通常由一些复杂的设置项构成。这种对话框适用于一些不太频繁的操作。</p>
<h3>2. 功能对话框 Function Dialog</h3>
<p>功能对话框通常在菜单或者某个具体的按钮打开，对话框中有一些对接下来这个功能事件的设置，这种对话框通常都会有一个[下一步]或者[确定]的主按钮（Primary Boutton）用来确认设置、关闭对话框并且执行功能。</p>
<p>另外成对出现的还会有[取消]按钮。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端设计总结2：模态对话框" src="https://image.woshipm.com/wp-files/2022/09/yWa6IGIVEOlseg8gwlVY.png" alt="B 端设计总结2：模态对话框" width="1014" referrerpolicy="no-referrer"></p>
<h3>3. 进度对话框 Process Dialog</h3>
<p>这种对话框向用户表明正在忙于某些内部的功能，其他处理能力可能会降低。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端设计总结2：模态对话框" src="https://image.woshipm.com/wp-files/2022/09/YO6Ah3AVIsYHT5zlsntO.png" alt="B 端设计总结2：模态对话框" width="1014" referrerpolicy="no-referrer"></p>
<p>在一些耗时较长的进度对话框中，还应该有以下信息：</p>
<ul>
<li>什么事情在进行中</li>
<li>现在一切正常</li>
<li>最好能展示出现在还需要多久完成</li>
<li>现在进度是多少，可以用“完成百分比”或者“已完成数/总需要完成数”表示</li>
<li>取消进程的按钮入口</li>
</ul>
<p>上图的例子中，macOS 软件更新中的取消进程是在 hover 进度条时出现了“×”，代表可以取消下载。</p>
<p>黑帕云中批量编辑由于耗时较短（通常情况下小于 10 秒），在用户等待感知的范围内，只需告知操作正在进行中，一切正常即可，无需提供详尽的进度信息。</p>
<h3>4. 通知对话框 Notification Dialog</h3>
<p>通知对话框是将一些重要的信息汇报给用户，来源可以是一些触发的事件，也可以是其他用户的通知。</p>
<p>常见的有通知中心对话框，处理完成某个操作的告知等等。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端设计总结2：模态对话框" src="https://image.woshipm.com/wp-files/2022/09/QiTFs6WyzpXe6tX44gIj.png" alt="B 端设计总结2：模态对话框" width="1075" referrerpolicy="no-referrer"></p>
<h3>5. 公告对话框 Bulleting Dialog</h3>
<p>公告对话框也是由程序自动启动的。包含三种类型：错误、警告、确认。</p>
<p>这种对话框通常不会要求用户填写什么，只会询问你“真的要进行吗？”或者告诉你一件事情。</p>
<p>所以在这种对话框上，一般只会有只有[取消]和[确认]，或者[OK]。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端设计总结2：模态对话框" src="https://image.woshipm.com/wp-files/2022/09/rTxLtFVfe5aPi4fqdK7Q.png" alt="B 端设计总结2：模态对话框" width="1014" referrerpolicy="no-referrer"></p>
<p>这种对话框比较特殊，因为没有一般对话框的 Header 和关闭按钮。<br>
的框架，他们把这种类型的对话框直接做成一种组件，命名为警告对话框（Alert）。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端设计总结2：模态对话框" src="https://image.woshipm.com/wp-files/2022/09/jAax853aIKFgyspkyCDO.png" alt="B 端设计总结2：模态对话框" width="1200" referrerpolicy="no-referrer"></p>
<p>我之前犯的错误就是用这种对话框承载了一个功能性的操作对话框。</p>
<p>当时是在做“复制应用”这个功能，需要一个对话框来承载复制的应用时是否复制应用中的数据。可以理解为，复制一个文档时，只复制这个文档的目录结构作为模板，还是连同文档内容一起复制。</p>
<p>当时不了解功能对话框和公告对话框的区别，所以直接用 Alert 组件这样画图：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端设计总结2：模态对话框" src="https://image.woshipm.com/wp-files/2022/09/XRfmPtEaz4IMdbjVgqi7.png" alt="B 端设计总结2：模态对话框" width="1019" referrerpolicy="no-referrer"></p>
<h2 id="toc-9">09 危险提示 Danger Alert</h2>
<p>前面在设计原则中提到了“容错处理”，在这一小节也详细写一写曾经被教育过的经历。</p>
<p>在很多破坏性的操作都会<strong>二次进行提醒</strong>，让用户确认操作，比如说删除操作。在删除之前都会询问用户“你真的要删除吗？”</p>
<p>想一想……你在看到这些提示的时候，是不是眼疾手快地按下那个[确认]按钮？</p>
<p>在《交互设计精髓》中有一节把这样的行为叫“大喊‘狼来了’的对话框”。</p>
<p>所以这种对话框在没有容错处理时，非常容易被我们这种无脑按[确认]的用户酿成大错。比如我手贱只是试试这个删除，然后就把某个表几千条辛苦写了一个月的数据删掉了。</p>
<p>所以，如果没有撤回或者回收站之类的功能的话，我会非常崩溃……然后联系产品的客服人员找某个倒霉的运维大哥帮我在数据库恢复数据。</p>
<p>你看容错处理多重要，有效帮助运维大哥延年益寿。</p>
<p>如果产品本身已经具备了容错能力，听起来喊“狼来了”的危险提示似乎不是必要的？</p>
<p>是的。我们在 macOS 中删除文件时，没有任何提示，直接被删掉。在邮箱删除邮件时，一样没有任何提示。</p>
<p>因为你知道可以在用 CMD+Z 进行撤回，也可以在回收站找到它们。</p>
<p>但是，如果产品还来不及做回收站或者撤回时，你不得不想点别的办法让删除确认变得不那么“狼来了”。</p>
<p>一个傻瓜但是有作用的办法是让删除确认增加一点成本：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端设计总结2：模态对话框" src="https://image.woshipm.com/wp-files/2022/09/sS3SHA0Y3khk6spsv60N.png" alt="B 端设计总结2：模态对话框" width="1014" referrerpolicy="no-referrer"></p>
<p>自从我们研发老哥哥花了 5 分钟做了这个输入验证的功能之后，误删应用、误删业务表的用户来找我们的次数直接断崖式下降到了 0。</p>
<h2 id="toc-10">10 写在最后</h2>
<p>这个系列会写的比较随意，大概会按照我觉得哪些容易写就会先写。</p>
<p>在完结之后，再根据常见的结构再进行梳理。</p>
<p>下一篇不出意外的话会写输入和选择控件（Entry&Selection Control），包含常见的文字输入（Text Input）、选择输入（Select Input）、日期输入（Date Input）、单选输入（Radio Input）、多选输入（CheckBox Input）、开关输入（Switch Input）。</p>
<div class="article--copyright"><p>作者：高拉，微信公众号：高拉</p>
<p>本文由 @高拉 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<p>该文观点仅代表作者本人，人人都是产品经理平台仅提供信息存储空间服务。</p>
</div><div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5609966" data-author="872276" data-avatar="https://image.woshipm.com/wp-files/2021/11/et9Uq8iw5K57MPLU2AHf.png"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            