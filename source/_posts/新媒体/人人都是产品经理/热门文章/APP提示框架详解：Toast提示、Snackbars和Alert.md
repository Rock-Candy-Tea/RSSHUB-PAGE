
---
title: 'APP提示框架详解：Toast提示、Snackbars和Alert'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/img/102.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 11 Mar 2016 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/img/102.jpg'
---

<div>   
<img data-action="zoom" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/img/102.jpg" referrerpolicy="no-referrer"><blockquote><p>某日和iOS开发聊天，说到iOS规范里没有安卓中的Toast形式的提示。我有点惊讶，仔细回忆iOS的交互规范，似乎是有。后来找来书确认了下，竟然是没有。遂把这个框架整理了下，在文中同时也强调下Android的交互规范的差异。在对比这两个差异的同时也能更好的了解这个框架的设计思想。</p></blockquote>
<p>
</p><p><strong>描述</strong></p>
<p>用户操作后，在APP执行操作前以模态方式让用户确认操作，或在操作告知操作结果。（ps.非模态形式反馈暂不在讨论范围）</p>
<h2 id="toc-1">一、构成元素</h2>
<ul>
<li>标题</li>
<li>文字</li>
<li>按钮</li>
</ul>
<h2 id="toc-2">二、使用前提</h2>
<ul>
<li>case1：会造成严重破坏</li>
<li>case2：存在误操作可能性，并且会造成严重后果或不便</li>
<li>case3：会造成严重破坏，并且可撤销</li>
<li>case4：进一步对所做的操作进行确定和执行</li>
</ul>
<h2 id="toc-3">三、表现形式</h2>
<h3>1.Toast</h3>
<p><a href="http://image.woshipm.com/wp-files/2016/03/183.png"><img data-action="zoom" class=" size-full wp-image-296681 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2016/03/183.png" alt="1" width="197" height="136" referrerpolicy="no-referrer"></a></p>
<p style="text-align: center;">Toast.jpg</p>
<p>Android中的Toast是一种简易的消息提示框。</p>
<p>告知用户任务状态，操作结果，例如：发送成功，加载中，删除成功。</p>
<p>Toast会在屏幕所有层的最上方。</p>
<p>显示时间有限，1s+左右消失</p>
<p>考虑到显示的时间，容易被用户忽略，不适合承载过多的文字和重要信息。</p>
<p>这么一来，其实这个功能似乎有点鸡肋，怪不得在iOS中建议，设计一种引人注目但又和你的 app 的样式相协调的方式去展示信息。很多APP中也是这么做的，脉脉的刷新成功，花瓣的上传成功。</p>
<p><img data-action="zoom" class=" size-full wp-image-296682 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2016/03/242.png" alt="2" width="592" height="358" srcset="http://www.woshipm.com/wp-content/uploads/2016/03/242.png 592w, http://www.woshipm.com/wp-content/uploads/2016/03/242-404x244.png 404w" sizes="(max-width: 592px) 100vw, 592px" referrerpolicy="no-referrer"></p>
<p>也有的如支付宝使用的方框形式。</p>
<p><img data-action="zoom" class=" size-full wp-image-296683 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2016/03/331.png" alt="3" width="211" height="362" srcset="http://www.woshipm.com/wp-content/uploads/2016/03/331.png 211w, http://www.woshipm.com/wp-content/uploads/2016/03/331-175x300.png 175w" sizes="(max-width: 211px) 100vw, 211px" referrerpolicy="no-referrer"></p>
<p>但要注意，Toast的出现与用户的操作行为紧密相关，所以其出现的位置与用户的操作最好能联系在一起，如上图中今日头条下拉刷新后的提示，支付宝转账成功的位置。</p>
<p>Toast一般有简短文字或者简单易懂的图标，如删除成功字样或者简单易懂的图标</p>
<p><a href="http://image.woshipm.com/wp-files/2016/03/420.png"><img data-action="zoom" class=" size-full wp-image-296684 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2016/03/420.png" alt="4" width="196" height="155" referrerpolicy="no-referrer"></a></p>
<p>Android 对Toast的作用介绍是，主要用于提示系统消息，但实际运用不仅限于此。</p>
<p>可以看到，是否把Toast融合于界面之中，其实影响的提示框架的一个特点，显示层级最高，打断用户的其他操作，让用户专心于提示框架显示的信息。而Toast的信息刚好踩在了这个临界点上，不太重要的信息是否需要打断用户的操作。这个就要看各个产品对这个信息传达的重要性的判断了。</p>
<h3>2.Snackbars</h3>
<p>在Android出的Material Design中又提出了一个与Toast类似的Snackbars。</p>
<p>Snackbar 是一种针对操作的轻量级反馈机制，通常出现在手机屏幕或者桌面端左下方，以浮动弹出框的形式存在。</p>
<p>与Toast相同，Snackbar也会出现屏幕所有层的最上方，包括浮动操作按钮；短暂出现后，会主动消失。</p>
<p>但Snackbar带有一定的交互性，用户触摸屏幕其他地方后自动消失，也可以在屏幕上滑动关闭。</p>
<p>而且Snackbar有时候可以带有一个操作，如撤销。对于一些可能会有不好后果的操作，并且可撤销，可以以Snackbars 的形式告知并提供撤销按钮。</p>
<p><a href="http://image.woshipm.com/wp-files/2016/03/518.png"><img data-action="zoom" class=" size-full wp-image-296685 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2016/03/518.png" alt="5" width="331" height="134" referrerpolicy="no-referrer"></a></p>
<p style="text-align: center;">clipboar.png</p>
<h3>3.Alert</h3>
<p>在用户进行操作后，APP执行操作前，如果用户的操作的结果会带来比较严重的后果，如不可撤销的数据删除，金钱交易，退出登录等。出现模态的提示框，包括说明性的标题、文字和进一步确定按钮（1-N）。</p>
<p><a href="http://image.woshipm.com/wp-files/2016/03/619.png"><img data-action="zoom" class=" size-full wp-image-296686 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2016/03/619.png" alt="6" width="301" height="135" referrerpolicy="no-referrer"></a></p>
<p style="text-align: center;">Alert</p>
<p>使用Alert时必须传达出清楚且可操作的信息。和其他的模态提示一样，Alert会打断用户的操作，要求用户集中精力来处理其传达的信息，并需要一次点击才能结束，因此要让用户明确知道警告框出现的合理性和必要性。并且Alert的出现必须非常克制，这样用户才不会因为频繁的点击确定而导致不必要的损失。所以其中每个元素的设计都要经过细致的考虑，如下文。</p>
<p><strong>3.1标题</strong></p>
<p>iOS要求标题的文字必须简洁易懂，快速传达当前的情境和对应的解决方案。</p>
<p>最好使用短句，偏于理解。</p>
<p>恰当的使用标点，是一个短句或一个简单但又不是问句的句子，句末不需要句号。如果是一个问句，句末使用问话。</p>
<p>android中提示框的标题是可选的，用于说明提示的类型。可以是与之相关的程序名，或者是选择后会影响到的内容。例如：设置，音量等。</p>
<p><strong>3.2文字</strong></p>
<p>在iOS中推荐使用标题，只有在标题无法简短清晰的传递意思才再补充文字说明。</p>
<p>对正文的要求与标题类似，一个简短、完整的句子。同时尽量让文字足够简短以便能在一两行之间显示。不要让警告框出现滚动条，这绝对不是好的体验。如果必须出现，则需要有足够的视觉线索。</p>
<p>不需要在文字中说明每个按钮的意思和结果，让按钮本身的文本来显示其对应的操作和结果。</p>
<p>不要用长句</p>
<p>不要用倒装</p>
<p>不要用否定</p>
<p>不要有歧义</p>
<p>要提供给用户足够决策的信息</p>
<p><strong>3.3按钮</strong></p>
<p>在iOS中推荐使用两个按钮的警告框，如果更多可以考虑使用下文的操作栏。“两个按钮的Alert通常是最有用的，因为对人们来说在两个按钮之间做选择最容易。单个按钮的Alert就不那么有用，因为它通常只是提示用户，并没有赋予用户任何对当前状况的控制能力。包含三个或三个以上按钮的Alert明显比双按钮Alert复杂，应该尽可能避免使用。”</p>
<p>在android中倒没这个要求，android的Alert同时起到了iOS里Alert和操作栏的警告，通知和选择作用。如果各自遵守交互规范倒是没有太多的好坏之分。</p>
<p>在各个APP中最常见的也是2个按钮的Alert，所以前段时间也看见知乎上一个帖子在讨论确定和取消按钮的左右问题。</p>
<p>这里的“确定”代表的是确定执行操作按钮，按钮名称可以删除，继续，退出等等。而“取消”代表的是放弃这个操作，比如不保存，取消退出等。</p>
<p>在iOS中，明确这两个之后再考虑一个前提，确定操作如果误点不会带来比较严重的后果，而且是用户比较有可能的操作，那应该放在右边，同时可以柔和的颜色提示按钮的安全性；取消按钮则放在左侧。</p>
<ul>
<li>如果确定按钮误点会带来比较严重的后果，且是用户比较有可能的操作，那比较适合放在左侧，并且可以用醒目的颜色（红）作为警示。</li>
<li>如果取消按钮误点会带来比较严重的后果，且不是用户比较有可能的操作，那适合放在左侧。</li>
<li>如果没有按钮误点会带来比较严重的后果，那。。。就不要用Alert~</li>
</ul>
<p>另外，Alert中的按钮要与其上的文本对应，不要用烂大街的确定，取消，要用明确告知操作后果的文字，如保存，删除，转账等。用户已经养成了看见确定就点确定的习惯，所以要用明确的动作来提示。</p>
<p>在android中比较简单，确定类事件都放在右侧，取消类事件就放在左侧。个人比较喜欢iOS的设计规范，更人性化一点，产品人员考虑的更多一点，用户就可以少考虑一点。</p>
<p>在android中Alert还起到选择的作用，所以多个选择的情况刚常见，这时候起到的有点类似iOS的操作栏，进一步确定和选择所要的操作。</p>
<h3>4.操作栏</h3>
<p>在iOS中，用户操作后，需要进行确认和操作的按钮大于3个，会推荐使用操作栏的形式。</p>
<p>不带标题，可能有文字介绍，具体要求与Alert文字类似。</p>
<p>显示两个或两个以上的按钮。</p>
<p>使用红色和靠近操作列表顶部来提醒用户注意那些执行潜在破坏性操作的按钮。</p>
<p>取消按钮放在最下的位置并与其他按钮做一定的区分。</p>
<p><a href="http://image.woshipm.com/wp-files/2016/03/715.png"><img data-action="zoom" class=" size-full wp-image-296687 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2016/03/715.png" alt="7" width="326" height="203" referrerpolicy="no-referrer"></a></p>
<p style="text-align: center;">操作栏</p>
<p>如果选择按钮太多，可以参考下图的形式组织按钮和滚动显示，但要留有足够的视觉线索。</p>
<p><a href="http://image.woshipm.com/wp-files/2016/03/817.png"><img data-action="zoom" class=" size-full wp-image-296688 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2016/03/817.png" alt="8" width="205" height="322" srcset="http://www.woshipm.com/wp-content/uploads/2016/03/817.png 205w, http://www.woshipm.com/wp-content/uploads/2016/03/817-191x300.png 191w" sizes="(max-width: 205px) 100vw, 205px" referrerpolicy="no-referrer"></a></p>
<p style="text-align: center;">微信</p>
<h2 id="toc-4">四、位置</h2>
<p>可以发现，操作栏的位置一般是从页面底部跳出，然后停留在页面底部的地方；而Alert一般是出现页面的中间；</p>
<p>Toast则比较多变，和用户前置操作的位置，信息的重要性，Toast的形态相关。</p>
<p>主要有顶部；内容区上方，导航下方（如下拉刷新）；页面中间（整体性，比较重要的信息提示）；页面下方，菜单栏上方（最常见）；页面底部；与操作按钮融合等。这么一算，就没不能放的地方。除了一个点，不要在模态的界面上再出现一个模态框架，这样会导致层级的复杂化和提示框任务的简单明确。</p>
<h2 id="toc-5">五、注意</h2>
<p>要注意随时提供一个明显而安全的退出模态框架的方式，这种方式一般是等同于点击“取消”，如点击空白区域，安卓的虚拟键等。<br>
提示框架如非必要不要出现，尤其Alert形式，出现得少会有助于用户对其认真对待。</p>
<p>回想下自己在pc端删除东西时点击确认的毫不犹豫，就要相信用户在警告框出现的时候的点击“确认”更多的是下意识的，所以注意不要完全寄希望与提示框架。要靠比用户想的更多更完善来避免提示框架的出现。</p>
<p> </p>
<p>作者@<a class="author-name blue-link" href="http://www.jianshu.com/users/74e9207acd73" target="_blank">静默之思</a></p>
<p>来源@简书</p>
<p>本文由 @<a class="author-name blue-link" href="http://www.jianshu.com/users/74e9207acd73" target="_blank">静默之思</a> 授权发布于人人都是产品经理 ，未经许可，禁止转载。</p>
                      
</div>
            