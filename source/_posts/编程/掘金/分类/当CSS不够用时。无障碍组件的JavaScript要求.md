
---
title: '当CSS不够用时。无障碍组件的JavaScript要求'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/78e1ac78-4eb5-47f7-92cc-813bb40c540e/1-css-js-requirements-accessible-components.png'
author: 掘金
comments: false
date: Fri, 18 Jun 2021 02:19:13 GMT
thumbnail: 'https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/78e1ac78-4eb5-47f7-92cc-813bb40c540e/1-css-js-requirements-accessible-components.png'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作为<a href="https://moderncss.dev/" target="_blank" rel="nofollow noopener noreferrer">ModernCSS.dev</a>的作者，我是一个CSS解决方案的忠实拥护者。而且，我喜欢看到人们用CSS来实现真正的开箱即用的设计和交互性的巧妙方法然而，我注意到一种趋势，即使用 "<a href="https://css-tricks.com/the-checkbox-hack/" target="_blank" rel="nofollow noopener noreferrer">复选框黑客</a>"等方法来推广 "纯CSS "组件。不幸的是，像这样的黑客行为使得大量的用户无法使用你的界面。</p>
<p>这篇文章涵盖了几个常见的组件，以及为什么CSS不足以涵盖无障碍性，详述了JavaScript的要求。这些要求是基于《<a href="https://www.w3.org/WAI/standards-guidelines/wcag/" target="_blank" rel="nofollow noopener noreferrer">网络内容可访问性指南》（WCAG）</a>和可访问性专家的额外研究。我不会规定JavaScript解决方案或演示CSS，而是研究在创建每个组件时需要考虑的问题。当然可以使用一个JavaScript框架，但为了增加所讨论的事件和功能，这不是必须的。</p>
<blockquote>
<p>所列的要求大体上不是可有可无的--它们对于帮助确保你的组件的可及性是必要的。</p>
</blockquote>
<p>如果你正在使用一个框架或组件库，你可以使用这篇文章来帮助评估所提供的组件是否<strong>符合无障碍要求</strong>。重要的是要知道，许多指出的项目不会被像aXe这样的自动可及性测试工具完全覆盖，因此需要一些人工测试。或者，你可以使用像<a href="https://www.cypress.io/" target="_blank" rel="nofollow noopener noreferrer">Cypress</a>这样的测试框架来创建所需功能的测试。</p>
<p>请记住，这篇文章主要是告知你每个界面组件的JavaScript注意事项。这并不是一个全面的资源，用于创建完全可访问的组件的所有实施细节，例如必要的咏叹调，甚至是标记。每种类型的资源都包括在内，以帮助你了解更多关于每种组件的广泛考虑。</p>
<h3 data-id="heading-0">确定只用CSS是否是一个合适的解决方案</h3>
<p>在你采用纯CSS的解决方案之前，有几个问题要问。我们将在这里介绍一些术语及其相关组件的更多背景。</p>
<ul>
<li>那么，<strong>你</strong>一定要全身心地投入到CSS中去，挑战极限，学习这门语言的功能。🎉</li>
<li><strong>该功能是否包括内容的显示和隐藏？</strong><br>
那么你至少需要用JS来切换ria，并在<code>Esc</code> 。对于某些类型的也会改变状态的组件，你可能还需要通过触发ARIA实时区域内的更新来传达变化。</li>
<li><strong>自然焦点顺序是最理想的吗？</strong><br>
如果自然顺序会使触发器和它所触发的元素之间的关系松散，或者键盘用户甚至不能通过自然标签顺序访问内容，那么你需要JS来协助焦点管理。</li>
<li><strong>风格化的控件是否提供了关于功能的正确信息？</strong><br>
像屏幕阅读器这样的辅助技术的用户会收到基于语义和ARIA的信息，帮助他们确定一个控件的作用。而且，语音识别的用户需要能够识别组件的标签或类型，以找出操作控件的短语。例如，如果你的组件的样式像标签，但使用单选按钮来像标签一样 "工作"，屏幕阅读器可能会听到 "单选按钮"，而语音用户可能会尝试使用 "标签 "这个词来操作它们。在这些情况下，你需要JS启用使用适当的控件和语义来实现预期的功能。</li>
<li><strong>效果是否依赖于悬停和/或聚焦？</strong><br>
，那么你可能需要JS来协助提供平等访问或持续访问内容的替代方案，特别是对于触摸屏用户和使用200%以上桌面缩放或放大软件的用户。</li>
</ul>
<p><strong>快速提示</strong>：<em>当你创建任何类型的自定义控件时，另一个参考资料是W3 "使用ARIA "指南中的《<a href="https://w3c.github.io/using-aria/#checklist" target="_blank" rel="nofollow noopener noreferrer">自定义控件可访问性开发检查表</a></em>》<em>。这里面提到了上面的几个要点，还有一些额外的设计和语义考虑。</em></p>
<h3 data-id="heading-1">工具提示</h3>
<p>缩小工具提示的定义是有点困难的，但在本节中，我们讨论的是在鼠标悬停在触发元素附近时出现的小文本标签。它们覆盖在其他内容上，不需要交互，并在用户取消悬停或焦点时消失。</p>
<p><img src="https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/78e1ac78-4eb5-47f7-92cc-813bb40c540e/1-css-js-requirements-accessible-components.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里的纯CSS解决方案可能看起来完全没问题，可以用类似的东西来完成。</p>
<pre><code class="copyable"><button class="tooltip-trigger">I have a tooltip</button>
<span class="tooltip">Tooltip</span>

.tooltip &#123;
display: none;
&#125;

.tooltip-trigger:hover + .tooltip,
.tooltip-trigger:focus + .tooltip &#123;
display: block;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然而，这忽略了相当多的可访问性问题，并排除了许多用户对工具提示内容的访问。</p>
<p>一大群被排除在外的用户是那些使用触摸屏的用户，因为在触摸屏上，<code>:hover</code> 事件与<code>:focus</code> 事件同步触发，所以<code>:hover</code> 可能不会被触发。这意味着任何与触发元素相关的动作--如按钮或链接--将与工具提示的显示同时启动。这意味着用户可能错过工具提示，或者没有时间阅读其内容。</p>
<p>如果工具提示被连接到一个没有事件的交互式元素上，工具提示可能会显示出来，但在另一个元素获得焦点之前不会被取消，而在此期间可能会阻止内容，妨碍用户完成任务。</p>
<p>此外，需要使用缩放或放大软件来导航的用户在使用工具提示时也会遇到相当大的障碍。由于工具提示是在悬停时显示的，如果这些用户需要通过平移屏幕来改变他们的视野来阅读工具提示，可能会导致它消失。工具提示也剥夺了用户的控制权，因为通常没有任何东西可以告诉用户工具提示会提前出现。<strong>叠加的内容</strong>可能会妨碍他们完成一项任务。在某些情况下，如与表单字段绑定的工具提示，手机或其他屏幕上的键盘可能会掩盖工具提示的内容。而且，如果他们没有适当地连接到触发元素，一些辅助技术用户甚至可能不知道工具提示已经出现。</p>
<p>对工具提示行为的指导来自<a href="https://www.w3.org/WAI/WCAG21/Understanding/content-on-hover-or-focus.html" target="_blank" rel="nofollow noopener noreferrer">WCAG成功标准1.4.13--悬停或聚焦的内容</a>。这个标准是为了帮助低视力用户和使用缩放软件的用户。工具提示（和其他在悬停和聚焦时出现的内容）的指导原则包括。</p>
<ul>
<li><strong>不允许</strong><br>
工具提示可以在不移动悬停或焦点的情况下被取消。</li>
<li><strong>可悬停</strong><br>
揭示的工具提示内容可以被悬停而不消失。</li>
<li><strong>持久性</strong><br>
附加内容不会基于超时而消失，而是等待用户移除悬停或焦点，或以其他方式取消它。</li>
</ul>
<p>要完全满足这些准则，需要一些JavaScript的帮助，特别是要让内容消失。</p>
<ul>
<li>辅助技术的用户会认为，解雇行为与Esc键有关，这需要一个JavaScript监听器。</li>
<li>根据Sarah Higley在下一节中描述的研究，在工具提示中添加一个可见的 "关闭 "按钮，也需要JavaScript来处理其关闭事件。</li>
<li>有可能需要用JavaScript来增强你的样式设计方案，以确保用户可以在工具提示内容上悬停，而不会在用户移动鼠标时被取消。</li>
</ul>
<h4 data-id="heading-2">工具提示的替代方案</h4>
<p>工具提示应该是最后的手段。Sarah Higley--一位特别热衷于劝阻使用工具提示的可及性专家--提供了这个简单的测试。</p>
<blockquote>
<p>"我为什么要在用户界面上添加这些文字？它还能放在哪里？"</p>
<p>- Sarah Higley来自演讲 "<a href="https://www.youtube.com/watch?v=lb0_v7D4kbs" target="_blank" rel="nofollow noopener noreferrer">Tooltips:</a>对<a href="https://www.youtube.com/watch?v=lb0_v7D4kbs" target="_blank" rel="nofollow noopener noreferrer">四个部分</a>的调查"</p>
</blockquote>
<p>根据Sarah在微软工作时参与的研究，另一个解决方案是专门的 "切换提示"。从本质上讲，这意味着提供一个额外的元素，允许用户有意触发<strong>额外内容的显示和隐藏</strong>。与工具提示不同，切换提示可以保留显示内容中的元素的语义。它们也把切换它们的控制权还给了用户，并保留了更多用户，特别是触摸屏用户的可发现性和可操作性。</p>
<p>如果你已经记住了<code>title</code> 属性的存在，只要知道它遭受了我们从我们的纯CSS解决方案中指出的所有相同问题。换句话说--不要在假设它是一个可接受的工具提示解决方案的情况下使用<code>title</code> 。</p>
<p>欲了解更多信息，请查看<a href="https://www.youtube.com/watch?v=lb0_v7D4kbs" target="_blank" rel="nofollow noopener noreferrer">Sarah在YouTube上的演讲</a>，以及她<a href="https://sarahmhigley.com/writing/tooltips-in-wcag-21/" target="_blank" rel="nofollow noopener noreferrer">关于工具提示的广泛文章</a>。要了解更多关于工具提示与切换提示的信息，以及关于为什么不使用<code>title</code> 的更多信息，请查阅Heydon Pickering在Inclusive Components的文章。工具<a href="https://inclusive-components.design/tooltips-toggletips/" target="_blank" rel="nofollow noopener noreferrer">提示和切换提示</a>。</p>
<h3 data-id="heading-3">模板</h3>
<p>模态--又称灯箱或对话框--是在触发动作后出现的页面内窗口。它们覆盖了其他的页面内容，可能包含结构化的信息，包括额外的操作，并且通常有一个半透明的背景来帮助区分模态窗口与页面的其他部分。</p>
<p><img src="https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/e2c1b6ac-6c84-4cbc-9a9f-882fb8be0708/2-css-js-requirements-accessible-components.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我见过一些纯CSS模态的变体（我也曾为我的作品集的一个旧版本做了一个模态）。他们可能使用 "复选框黑客"，利用<code>:target</code> 的行为，或者试图从<code>:focus</code> （这可能真的是一个变相的超大工具提示）中获得。</p>
<p>至于HTML<code>dialog</code> 元素，请注意它不被认为是全面无障碍的。因此，虽然我绝对鼓励人们在定制解决方案之前使用本地的HTML，但不幸的是，这个解决方案打破了这个想法。你可以了解更多关于<a href="https://www.scottohara.me/blog/2019/03/05/open-dialog.html" target="_blank" rel="nofollow noopener noreferrer">HTML<code>dialog</code> 不能被访问的原因</a>。</p>
<p>与工具提示不同，模态的目的是允许结构化的内容。这意味着可能有一个标题，一些段落内容，以及互动元素，如链接、按钮甚至是表单。为了让大多数用户能够访问这些内容，他们必须能够使用<strong>键盘事件</strong>，特别是标签。对于较长的模态内容，方向键也应该保留滚动的能力。就像工具提示一样，它们应该可以用Esc键来取消--而且只用CSS是没有办法做到的。</p>
<p>模态中的焦点管理需要JavaScript。模态应该_捕获_焦点，这意味着一旦焦点在模态中，用户就_不能_从模态中切换到后面的页面内容。但首先，焦点必须进入模态_内部_，这也需要JavaScript来实现一个完全可访问的模态解决方案。</p>
<p>下面是必须用JavaScript来管理的<strong>与模态相关的事件的顺序</strong>。</p>
<ol>
<li>在一个按钮上的事件监听器打开模态</li>
<li>焦点被放置在模态中；哪个元素根据模态内容而变化（见决策树）。</li>
<li>焦点被困在模态中，直到它被取消。</li>
<li>最好是，如果需要确认模态内容，除了专门的关闭按钮_或_诸如 "取消 "之类的破坏性按钮动作外，用户还能用Esc键关闭模态。
<ol>
<li>如果允许Esc，对模态背景的点击也应该解散该模态。</li>
</ol>
</li>
<li>解除后，如果没有发生导航，焦点将被放回触发的按钮元素上。</li>
</ol>
<h4 data-id="heading-4">模态焦点决策树</h4>
<p>基于<a href="https://www.w3.org/TR/wai-aria-practices-1.1/examples/dialog-modal/dialog.html" target="_blank" rel="nofollow noopener noreferrer">WAI-ARIA创作实践中的模态对话框示例</a>，这里有一个简化的决策树，用于在模态打开后将焦点放在哪里。上下文总是决定了这里的选择，而且理想情况下，焦点的管理不仅仅是 "第一个可关注的元素"。事实上，有时非焦点元素也需要被选择。</p>
<ul>
<li><strong>模态的主要主体是一个表单。</strong><br>
关注第一个表单字段。</li>
<li>模态<strong>内容的长度很大，并且把模态动作推到了视野之外。</strong><br>
如果有标题的话，聚焦一个标题，或者第一段。</li>
<li><strong>模态的目的是程序性的（例如：确认行动），有多个可用的行动。</strong><br>
根据上下文关注 "破坏性最小 "的行动（例如："OK"）。</li>
<li><strong>模态的目的是程序性的，有一个动作。</strong><br>
关注第一个可关注的元素。</li>
</ul>
<p><strong>快速提示</strong>：<em>在需要聚焦一个不可聚焦的元素的情况下，如标题或段落，添加<code>tabindex="-1"</code> ，这允许该元素以程序化的方式用JS聚焦，但不将其添加到DOM标签顺序中。</em></p>
<p>请参考<a href="https://www.w3.org/TR/wai-aria-practices-1.1/examples/dialog-modal/dialog.html" target="_blank" rel="nofollow noopener noreferrer">WAI-ARIA模式演示</a>，了解更多关于设置ARIA的其他要求，以及关于如何选择添加焦点的元素的更多细节。该演示还包括JavaScript，以示范如何进行焦点管理。</p>
<p>对于一个现成的解决方案，Kitty Giraudel已经创建了<a href="https://a11y-dialog.netlify.app/" target="_blank" rel="nofollow noopener noreferrer">a11y-dialog</a>，其中包括我们讨论的功能要求。Adrian Roselli也<a href="https://adrianroselli.com/2020/10/dialog-focus-in-screen-readers.html" target="_blank" rel="nofollow noopener noreferrer">研究了模态对话框的焦点管理</a>，并创建了一个演示，还汇编了关于不同的浏览器和屏幕阅读器组合将如何传达焦点元素的信息。</p>
<h3 data-id="heading-5">标签</h3>
<p>标签式界面涉及一系列的触发器，每次都会显示相应的内容面板。你可能会发现，这些CSS "黑科技 "涉及到使用风格化的单选按钮，或者<code>:target</code> ，这两种方式都允许一次只显示一个面板。</p>
<p><img src="https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/118262cd-04ee-4dfb-89dc-958995e5a0d6/3-css-js-requirements-accessible-components.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面是需要JavaScript的标签功能。</p>
<ol>
<li>对当前标签切换<code>aria-selected</code> 属性为真，对未选择的标签切换为假。</li>
<li>创建一个_漫游标签索引_来区分标签选择和焦点</li>
<li>通过响应方向键事件（以及可选的<code>Home</code> 和<code>End</code> ）在标签之间移动焦点</li>
</ol>
<p>你可以选择让标签选择跟随焦点--这意味着当一个标签被聚焦时，它也被选中并显示其相关的标签面板。WAI-ARIA创作实践为<a href="https://www.w3.org/TR/wai-aria-practices-1.1/#kbd_selection_follows_focus" target="_blank" rel="nofollow noopener noreferrer">选择是否跟随焦点</a>提供了这个<a href="https://www.w3.org/TR/wai-aria-practices-1.1/#kbd_selection_follows_focus" target="_blank" rel="nofollow noopener noreferrer">指南</a>。</p>
<p>无论您是否选择让选择跟随焦点，您也将使用JavaScript来监听箭头键事件，以便在标签元素之间移动焦点。这是一种允许<strong>标签选项导航的</strong>替代模式，因为漫游标签索引的使用（接下来描述）改变了自然的键盘标签焦点顺序。</p>
<h4 data-id="heading-6">关于游动<code>tabindex</code></h4>
<p>巡回<a href="https://www.w3.org/TR/wai-aria-practices/#kbd_roving_tabindex" target="_blank" rel="nofollow noopener noreferrer">标签索引</a>的概念是，<code>tabindex</code> 的值是通过程序控制来管理元素的焦点顺序的。关于标签，这意味着通过设置<code>tabindex="0"</code> ，只有被选中的标签是焦点顺序的一部分，而未被选中的标签被设置为<code>tabindex="-1"</code> ，这就把它们从自然键盘焦点顺序中移除。</p>
<p>这样做的原因是，当一个标签被选中时，下一个标签将把用户的焦点放在相关的标签面板内。你可以选择通过分配给标签面板的元素<code>tabindex="0"</code> ，使其成为可关注的元素，或者如果<strong>在标签面板内有</strong>一个<strong>可关注的元素</strong>的保证，这可能就没有必要了。如果你的标签面板内容将更加多变或复杂，你可以考虑根据我们为模态审查的决策树来管理焦点。</p>
<h3 data-id="heading-7">标签模式的例子</h3>
<p>这里有一些创建标签的参考模式。</p>
<ul>
<li><a href="https://dequeuniversity.com/library/aria/tabpanel" target="_blank" rel="nofollow noopener noreferrer">Deque大学的Tabpanel演示</a></li>
<li><a href="https://scottaohara.github.io/a11y_tab_widget/" target="_blank" rel="nofollow noopener noreferrer">Scott O'Hara的Tab widget测试</a>（测试几个功能模式</li>
<li>来自Heydon Pickering的_Inclusive Components_的<a href="https://inclusive-components.design/tabbed-interfaces/" target="_blank" rel="nofollow noopener noreferrer">Tabbed Interfaces</a>，它展示了Tab是如何逐步增强目录的。</li>
</ul>
<h3 data-id="heading-8">旋转木马</h3>
<p>旋转木马也被称为幻灯片或滑块，它涉及一系列旋转的内容面板（又称 "幻灯片"），其中包括控制机制。你会在许多配置中发现这些内容的广泛性。它们在某种程度上被认为是<a href="https://shouldiuseacarousel.com/" target="_blank" rel="nofollow noopener noreferrer">一种糟糕的设计模式</a>，是臭名昭著的。</p>
<p><img src="https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/994ef747-b95d-4b02-9a10-65da686d5e3a/4-css-js-requirements-accessible-components.jpg" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>只用CSS的旋转木马的棘手之处在于，它们可能不提供控制机制，或者它们可能使用意想不到的控制机制来操纵旋转木马的运动。例如，你可以再次使用 "复选框黑客 "来使旋转木马过渡，但<strong>复选框会</strong>给辅助技术的使用者<strong>带来错误的</strong>交互<strong>信息类型</strong>。此外，如果你把复选框的标签设计成视觉上的前进和后退的箭头，你很可能会给语音识别软件的用户带来错误的印象，让他们以为应该说什么来控制旋转木马。</p>
<p>最近，<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Scroll_Snap" target="_blank" rel="nofollow noopener noreferrer">对滚动快照的</a>原生<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Scroll_Snap" target="_blank" rel="nofollow noopener noreferrer">CSS支持</a>已经登陆。起初，这似乎是一个完美的纯CSS的解决方案。但是，即使是自动的可及性检查也会<strong>将这些标记为键盘用户无法浏览</strong>的，因为没有办法通过交互式元素进行导航。这个功能的默认行为还有其他可访问性和用户体验方面的问题，其中一些我已经包含在<a href="https://smolcss.dev/#smol-scroll-snap" target="_blank" rel="nofollow noopener noreferrer">我在SmolCSS上的滚动快照演示</a>中。</p>
<p>尽管旋转木马的外观有很大的差异，但还是有一些共同的特征。一种选择是<a href="https://dequeuniversity.com/library/aria/carousel" target="_blank" rel="nofollow noopener noreferrer">使用标签标记来创建一个旋转木马</a>，因为它实际上是相同的底层界面，只是视觉表现有所改变。与标签相比，旋转木马可以提供额外的上一页和下一页的控制，如果旋转木马是自动播放的，还可以暂停。</p>
<p>以下是根据你的旋转木马功能的JavaScript注意事项。</p>
<ul>
<li><strong>使用分页控件</strong><br>
在选择一个编号的项目时，以编程方式聚焦相关的旋转木马幻灯片。这将涉及到使用漫游标签索引来设置幻灯片容器，这样你就可以聚焦于当前的幻灯片，但要防止访问屏幕外的幻灯片。</li>
<li><strong>使用自动播放</strong><br>
包括一个暂停控制，还可以在幻灯片被悬停或其中的互动元素被聚焦时启用暂停。此外，你可以<a href="https://web.dev/prefers-reduced-motion/" target="_blank" rel="nofollow noopener noreferrer">在JavaScript中检查<code>prefers-reduced-motion</code></a> ，在暂停的状态下加载幻灯片，以尊重用户的喜好。</li>
<li><strong>使用上一页/下一页控件</strong><br>
包括一个标记为<code>aria-live="polite"</code> 的视觉隐藏元素，在这些控件被激活时，在实时区域中填充当前位置的指示，例如 "4号幻灯片的第2张"。</li>
</ul>
<h4 data-id="heading-9">构建无障碍旋转木马的资源</h4>
<ul>
<li><a href="https://www.w3.org/WAI/tutorials/carousels/" target="_blank" rel="nofollow noopener noreferrer">万维网联盟网络无障碍教程</a>中<a href="https://www.w3.org/WAI/tutorials/carousels/" target="_blank" rel="nofollow noopener noreferrer">关于旋转木马</a>的详尽实施细节和注意事项以及完整的代码示例</li>
<li>德克大学将<a href="https://dequeuniversity.com/library/aria/carousel" target="_blank" rel="nofollow noopener noreferrer">一个标签界面增强为一个旋转木马</a>的例子。</li>
<li>WAI-ARIA创作实践中的<a href="https://www.w3.org/TR/2019/NOTE-wai-aria-practices-1.1-20190814/examples/carousel/carousel-1.html" target="_blank" rel="nofollow noopener noreferrer">自动旋转图像旋转器</a>示例</li>
<li>Smashing的无障碍组件综述中<a href="https://www.smashingmagazine.com/2021/03/complete-guide-accessible-front-end-components/#accessible-carousels-and-content-sliders" target="_blank" rel="nofollow noopener noreferrer">精选的旋转木马资源</a></li>
</ul>
<h3 data-id="heading-10">下拉菜单</h3>
<p>这指的是一个按钮可以切换打开一个链接列表的组件，通常用于导航菜单。在<code>:hover</code> 或<code>:focus</code> ，止于显示菜单的CSS实现只会错过一些重要的细节。</p>
<p><img src="https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/365cc532-dc82-49a3-8326-4ed2692519f9/5-css-js-requirements-accessible-components.png" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我承认，我甚至认为通过使用较新的<code>:focus-within</code> 属性，我们可以安全地实现一个纯CSS的解决方案。你会看到<a href="https://moderncss.dev/css-only-accessible-dropdown-navigation-menu/" target="_blank" rel="nofollow noopener noreferrer">我那篇关于CSS下拉菜单的文章</a>被修改了，加入了关于必要的JavaScript的注释和资源（我保留了这个标题，以便寻求该解决方案的其他人也希望能完成JS的实现）。具体来说，只依靠CSS意味着违反<a href="https://www.w3.org/WAI/WCAG21/Understanding/content-on-hover-or-focus.html" target="_blank" rel="nofollow noopener noreferrer">WCAG成功标准1.4.13：悬停或聚焦时的内容</a>，我们在工具提示中了解到这一点。</p>
<p>我们需要为一些技术添加JavaScript，这些技术现在听起来应该很熟悉。</p>
<ul>
<li>通过监听<code>click</code> 事件，在<code>true</code> 和<code>false</code> 之间切换菜单按钮上的<code>aria-expanded</code> 。</li>
<li>在使用Esc键时关闭一个打开的菜单，并将焦点返回到菜单切换按钮上。</li>
<li>最好是在焦点移到菜单之外时关闭打开的菜单</li>
<li><em>可选的</em>：实现方向键以及<code>Home</code> 和<code>End</code> 键，以便在菜单切换按钮和下拉菜单中的链接之间进行键盘导航。</li>
</ul>
<p><strong>快速提示</strong>：<em>通过将菜单显示与<code>.dropdown-toggle[aria-expanded=` </code>"<code>true</code>"] 的选择器相关联，确保正确实现下拉菜单</em>。<em>+ .dropdown<code>rather than basing the menu display on the presence of an additional JS-added class like</code>active`。这也从你的JS解决方案中消除了一些复杂性!</em></p>
<p>这也被称为 "披露模式"，你可以在WAI-ARIA创作实践的<a href="https://w3c.github.io/aria-practices/examples/disclosure/disclosure-navigation.html" target="_blank" rel="nofollow noopener noreferrer">披露导航菜单示例</a>中找到更多细节。</p>
<h4 data-id="heading-11">关于创建无障碍组件的其他资源</h4>
<ul>
<li>Smashing的《<a href="https://www.smashingmagazine.com/2021/03/complete-guide-accessible-front-end-components/" target="_blank" rel="nofollow noopener noreferrer">可访问前端组件完整指南》</a>。</li>
<li>Carie Fisher的文章《<a href="https://www.smashingmagazine.com/2021/03/good-better-best-untangling-complex-world-accessible-patterns/" target="_blank" rel="nofollow noopener noreferrer">好、更好、最好：解开可访问模式的复杂世界</a>》。</li>
<li>关于常见设计模式和部件的演示和信息可从<a href="https://www.w3.org/TR/wai-aria-practices-1.2/" target="_blank" rel="nofollow noopener noreferrer">WAI-ARIA创作实践1.2</a>中获得。</li>
<li><a href="https://dequeuniversity.com/library/" target="_blank" rel="nofollow noopener noreferrer">德克大学的代码库</a></li>
<li><a href="https://github.com/scottaohara/accessible_components" target="_blank" rel="nofollow noopener noreferrer">Scott O'Hara的无障碍组件</a></li>
<li>Heydon Pickering的《<a href="https://inclusive-components.design/" target="_blank" rel="nofollow noopener noreferrer">包容性组件</a>》。</li>
</ul></div>  
</div>
            