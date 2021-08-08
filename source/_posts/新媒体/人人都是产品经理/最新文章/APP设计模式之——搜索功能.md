
---
title: 'APP设计模式之——搜索功能'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/soaKf1ome92140ybpDUM.jpg'
author: 人人都是产品经理
comments: false
date: Sun, 08 Aug 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/soaKf1ome92140ybpDUM.jpg'
---

<div>   
<blockquote><p>编辑导语：搜索功能是用户常使用功能之一，其中又包括条件输入、内容判定、搜索触发、结果展示等模块。那么，具体到各个模块，设计师又应当从哪些细节入手来提升用户的使用体验？本篇文章里，作者就搜索功能设计做了思考和总结，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5000803 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/soaKf1ome92140ybpDUM.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>可能在很多人看来，搜索是个不起眼的小功能，无需花太多时间赘述。但作为PM/UI/UX，我们没有理由轻视任何涉及用户体验的产品设计，个人来讲，是不怕用户批评和吐槽的，我最怕的是眼界狭隘，思路不开阔，因为这决定了我的成长空间和速度。</p>
<p>所以在这篇文章中，我尽可能地把自己遇到/思考到的，涉及搜索功能的设计模式，围绕着搜索流程，都一一列举出来，也希望大家在看到新颖的APP搜索模式时，贡献一下案例。</p>
<p>应第一篇专栏评论区@大大头披风朋友的建议，后面所有文章插图，我都会进行标注。</p>
<p>另外非常感谢大家的关注与赞赏，你们的认可是我更新的最大动力。</p>
<p>言归正传，先放一张搜索流程图：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/iq6AVW5qXRFy0IJZllv3.png" alt="APP设计模式之——搜索功能" width="757" height="193" referrerpolicy="no-referrer"></p>
<p>湖蓝色边框是最简洁/必要的搜索流程节点，考虑到各种各样的场景，整个搜索流程就变得“冗长”了，但是用户体验却上去了。下面我们就逐一介绍搜索流程中的各个动作和关键节点，以及典型实例。</p>
<h2 id="toc-1">一、输入搜索内容</h2>
<h3>1. 功能入口</h3>
<p>搜索功能入口即用户进入搜索流程的起点，这个起点通常都以静态形式展现在页面上，比如页面左上角或右上角的搜索图标，或页面上的搜索文本框（以圆角矩形为主）。如<b>格志</b>和<b>Reddit</b>：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/8W53VrNHl8F7KxwU131U.png" alt="APP设计模式之——搜索功能" width="757" referrerpolicy="no-referrer"></p>
<p>用户点击这个图标或者文本框后，才算触发了搜索流程的第一步：内容录入。</p>
<p>相对来说，搜索图标适合低频搜索应用，而搜索文本栏更适合高频搜索应用。查询类应用/场景显然非常适合搜索文本框，而且用户使用频度越高，搜索文本框自身面积就越大，所占页面位置也更加明显，比如<b>网易云音乐</b>和<b>金山词霸</b>：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/Us6pQAinm5B0jxtEppDY.png" alt="APP设计模式之——搜索功能" width="756" referrerpolicy="no-referrer"></p>
<p>个人来讲，不知为何，当我看到搜索文本框的时候，就有一种马上就要看到期待的内容的感觉，而单纯的搜索图标是没办法给这种感觉的。毕竟搜索图标和搜索结果中间，总会隔着一个搜索文本框。</p>
<h3>2. 条件输入</h3>
<p>可能有人会说了，输入搜索条件还有什么好说的？直接敲键盘不就完事儿了吗？</p>
<p>对于绝大部分用户来说，这确实没有问题，但是……俗话说得好，魔鬼都在细节里。越是这种不起眼的地方，我们越能做出一些能让小众用户觉得很好用/好玩的设计，在体现APP自身特色的同时，还能帮应用留住那些“长尾用户”。</p>
<p>条件输入环节，我们应该关注的设计要素：退出搜索页面、一键删除已输入内容、触发搜索动作执行的按钮、小键盘、小键盘增强设计。</p>
<p><b>退出搜索界面</b>：通常是“取消”二字，水平置于文本框右侧，也有些应用采取“＜”按钮设计，水平置于文本框左侧，比如<b>微信阅读</b>和<b>Quora</b>：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/iU7E3RP07ny07uWaqQuz.png" alt="APP设计模式之——搜索功能" width="756" referrerpolicy="no-referrer"></p>
<p><b>一键删除已输入内容</b>：通常是在搜索框右侧放置灰底白色“×”图标，也有些应用出于用户输入出错率高的情况，将这个元素放置到用户更容易“够得到”的位置，这个设计在大屏手机时代还是非常有必要的。</p>
<p>下面的<b>良仓</b>和<b>金山词霸</b>分别代表了这两种类型，且后者采用了“清空”文字’代替“×”图标，居于屏幕中央略靠下的位置，可以说非常醒目了：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/StGgun2r95F3Euvi9ZW5.png" alt="APP设计模式之——搜索功能" width="756" referrerpolicy="no-referrer"></p>
<p><b>触发搜索动作执行的按钮</b>：PC端产品很多还保留着有实际作用的“搜索”按钮，如百度首页的“百度一下”按钮：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/vQfwk7m4VPh4HI2xfLpN.png" alt="APP设计模式之——搜索功能" width="580" referrerpolicy="no-referrer"></p>
<p>谷歌的“Google搜索”：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/MHSqTZhMkZn9D4vTy8qN.png" alt="APP设计模式之——搜索功能" width="580" referrerpolicy="no-referrer"></p>
<p>以及相当多应用的搜索框内置的或者右侧的搜索图标，PC端的“搜索”触发是通过“Enter”回车键或鼠标单击完成，同理APP上的搜索触发，要么是通过点击页面上的“搜索”图标，要么是通过小键盘上的确认键来完成，而小键盘确认键往往有多种表现形式，如“搜索”、“确定”、“换行”等。</p>
<p><b>小键盘</b>：小键盘需要注意的就是根据输入框和表单的内容，来设置默认的小键盘样式，比如中文键盘、英文键盘、数字键盘等，为用户带来更顺畅的操作体验。</p>
<p><b>小键盘增强设计</b>：增强设计指的是在小键盘上方，再增加一行命令项，在视觉设计上表现为做到和小键盘融为一体，在功能上表现为根据用户使用场景，尤其是高频操作，来设计对应的功能。</p>
<p>比如<b>UC浏览器</b>的小键盘增强设计，除了给出常见的网址前缀后缀，还在中间放置了一个光标精准定位滚轴，极具匠心：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/9oBrIso5aftntuowJWd2.png" alt="APP设计模式之——搜索功能" width="758" referrerpolicy="no-referrer"></p>
<p>还有一些带有应用自身特色的小键盘增强设计，如<b>金山词霸</b>和<b>Quora</b>。</p>
<p>词霸有三个按钮：“返回”（退出搜索界面）、“清空”（一键清除已输入内容）、“翻译”（触发搜索动作），我相信只要用户几次词霸，便会对这个界面赞赏有加，高频操作按钮居中布局，非常方便用户单手操作，且搜索框显得非常简洁美观：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/ZdzCvsMn08YRJTFKwWSG.png" alt="APP设计模式之——搜索功能" width="759" referrerpolicy="no-referrer"></p>
<p>而Quora的增强设计更是独具匠心，将问答社区高频操作“搜索-提问-阅读-回答-”中的提问入口直接放到了小键盘上方，当用户在动态搜索结果中找不到自己想要的内容后，可以直接将想找的回答变为问题，惊不惊喜？意不意外？</p>
<p>而中国版Quora，即知乎，并没有建立起“搜索-提问”的关联，提问入口仍然是孤立的（文章发布后经@Tony Liao 和@大大头披风 的提醒，发现最新版知乎已经可以在搜索结果页的上划刷新的第四屏看到“没找到想要的内容？——去提问”的悬浮提示设计）：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/NBq7SLox5Hv0oMi7CPWe.png" alt="APP设计模式之——搜索功能" width="755" referrerpolicy="no-referrer"></p>
<p>思考时间：右侧输入框的设计有何优缺点？如何进行优化？</p>
<p>再放两个特殊增强设计，<b>Termius</b>（移动端主机管理工具）和<b>Navicat</b>（移动端数据库管理工具）。</p>
<p>前者整合了很多实体键盘按键，而后者为了不影响表结构的显示效果，干脆在增强设计行中做了个搜索框，所以没有一成不变的设计，还是要具体问题具体场景具体分析。当然这种产品的PM基本就必须要懂相关技术和操作了：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/MokMVNXW4GVhF4tn0HiP.png" alt="APP设计模式之——搜索功能" width="751" referrerpolicy="no-referrer"></p>
<h3>3. 辅助输入</h3>
<p>辅助输入，指的是在用户输入前，APP提供给用户一些内容或者选项，以便用户更快更省力地输入搜索条件。如<b>UC浏览器</b>和<b>知乎</b>就提供了历史搜索记录，来辅助：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/9yXiUscTQp9rdyn5USpV.png" alt="APP设计模式之——搜索功能" width="753" referrerpolicy="no-referrer"></p>
<p>UC是给出了历史搜索记录，而知乎则更进一步，对历史搜索记录进行了分类，使用“内容”和“用户”两个标签让用户进行切换，而且还增加了“最近浏览”入口，方便用户回溯自己近期的浏览列表，更胜一筹。</p>
<p>“尊重用户的劳动”是成功手机界面设计的最基本原则。“保存的搜索”和“最近搜索”使得搜索条件容易从以前的搜索历史中选择，而不用再次输入相同的关键词。</p>
<p>选项辅助输入，是指在用户输入搜索条件之前，提供一些基本的搜索范围（如内容分类等），让用户更快地获得期望的结果。参见<b>全民K歌</b>和<b>Pinterest：</b></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/SL6uTysRr3jpuzvxxhGv.png" alt="APP设计模式之——搜索功能" width="756" referrerpolicy="no-referrer"></p>
<p>这种搜索方式也可以称为“前置搜索类别”。这种搜索方式适用于分类较简单的内容，便于精确地定位搜索内容。</p>
<p>与“前置搜索类别”相对应的，是“<b>后置搜索类别</b>”，我们放到后面去讲。</p>
<p>此外还有包括基于地理位置搜索的辅助输入方式，这在基于LBS的APP中非常常见，如<b>猫眼电影</b>和<b>高德地图</b>：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/5miXdXFUhLIvVXfxG3kV.png" alt="APP设计模式之——搜索功能" width="751" referrerpolicy="no-referrer"></p>
<p>最佳实践：保存搜索需要额外的步骤去命名搜索参考值，尊重用户的劳动成果，让用户减少操作。</p>
<h2 id="toc-2">二、执行搜索命令</h2>
<p>在移动端，最广泛的搜索模式是：用户输入搜索内容后，APP自动执行搜索动作，同时将搜索结果以列表的形式展示在搜索文本框下方，用户继续输入搜索内容，搜索结果也会相应自动变化，当全部条件输入完毕时，点击搜索按钮，显示最终结果。</p>
<p>这种搜索模式，我称之为动态搜索，这也是目前最符合“懒设计”理念的搜索方式。同时，还有一种较为“古老”的搜索模式，即静态搜索，即用户输入完全部的搜索条件，再一键执行搜索命令。</p>
<h3>动态搜索</h3>
<p>动态搜索，指输入搜索条件时的实时搜索+实时展示。这种设计也被称为动态过滤，即输入文本数据，对应搜索结果将会动态过滤显示在屏幕上。同时，这也是一种特殊形式的辅助输入（见4.1.3）。我们以<b>豆瓣</b>为例：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/LITDsztwBxheqDqjdMVO.png" alt="APP设计模式之——搜索功能" width="752" referrerpolicy="no-referrer"></p>
<p>在输入“梦”和“梦的”两个搜索条件时，结果展现的完全不一样，这是因为动态搜索时，是根据已输入内容的词频热度进行搜索和排序的。这又涉及到搜索算法，对于这部分内容，我们放到后面去详细介绍。</p>
<p>目前使用静态搜索设计的APP已经越来越少，因此不做赘述。</p>
<h2 id="toc-3">三、搜索等待</h2>
<p>通常情况下，无论是动态搜索还是静态搜索，在搜索结果呈现之前，都会有进度条或者加载交互动作的指示器，用以告知用户：“正在搜索中，请耐心等待”。当搜索动作执行完毕后，再展示最终的搜索结果：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/MoY91BvTeXXV6xe6FV9i.png" alt="APP设计模式之——搜索功能" width="754" referrerpolicy="no-referrer"></p>
<p>在2G（第二代移动通信技术）时代，下载速度在几KB/S到10几KB/S之间，从录入搜索条件到显示搜索结果，通常需要1秒以上的响应时间，这时的系统反馈就非常必要，进度条或者加载动作能给用户以提示，表示正在搜索中。</p>
<p>到了3G/4G，甚至未来几年就能够在国内应用的5G时代，搜索结果几乎瞬时呈现，这时系统反馈动作是否必要呢？答案是肯定的，因为哪怕是在一线城市市中心，也会存在网络环境差的场景，应用仍需要给用户提供等待提示。</p>
<h2 id="toc-4">四、展示搜索结果</h2>
<h3>1. 展示方式</h3>
<p>搜索结果的展示，涉及到展示方式、展示层级等。</p>
<p>搜索完毕，结果会显示在原有页面下方，或在新页面中显示（相对较少）。展示方式也纷繁多样。比如最简单的文字列表视图（<b>墨墨单词</b>和<b>TripAdvisor</b>）：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/8QRpCVU7MwaghYL7YU6q.png" alt="APP设计模式之——搜索功能" width="755" referrerpolicy="no-referrer"></p>
<p>图文并茂式<b>列表视图</b>（<b>网易云课堂</b>和<b>在行</b>）：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/d2DDOUkEvHYKYwkkFBwL.png" alt="APP设计模式之——搜索功能" width="756" referrerpolicy="no-referrer"></p>
<p>还有一些简约化，内容设计感极强的列表（<b>Kickstarter</b>和<b>Town</b>）：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/LIZ6E4eOeIfIPQW3Yjfn.png" alt="APP设计模式之——搜索功能" width="760" referrerpolicy="no-referrer"></p>
<p>Kickstarter是横向左右滑动卡片式列表，每个卡片代表一个众筹项目；Town是纵向滑动大图列表，每个条目代表一处人文景观。</p>
<p>增强列表视图（<b>豆瓣</b>和<b>携程</b>）：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/gibjBYDTm5MxJzsPheFk.png" alt="APP设计模式之——搜索功能" width="754" referrerpolicy="no-referrer"></p>
<p>增强列表视图，是普通列表视图的变体，指在列表视图的基础上，糅合其他设计要素，而呈现出更加多样的视图方式。</p>
<p>比如豆瓣的多重列表视图就是增强列表视图的一种，它采用了基于搜索结果类别进行分列表展示的视图方式。简单来讲就是展示页面有多个列表，如“图书”列表、“电影/电视”列表等。</p>
<p>携程搜索展示页面是增强型列表视图的典型，在整体是列表视图的整体视觉效果上，有的列表项本身就是一项内容集合，如“张家界的旅游度假”；有的列表项本身是一个具体条目（张家界碧桂园凤凰酒店）；有的列表项增加了内容详情介绍（旅游产品介绍），不同列表项代表不同类别（飞机、酒店、旅游产品等），这种视图方式适合搜索结果门类及其复杂，不同结果展示权重不同的应用。</p>
<p><b>表格视图</b>（<b>小红书</b>和<b>ASOS</b>）：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/F4vc1nP2MfliqrxxTIUS.png" alt="APP设计模式之——搜索功能" width="755" referrerpolicy="no-referrer"></p>
<p>当搜索结果需要图文并茂地进行展示，且需要支持用户快速浏览较多条目的时候，表格视图再适合不过了，而上述两个前提，缺了任何一个，都会影响用户体验。这种视图方式经常应用在购物类的应用中，且最多两列排列，再多的话，信息就太过密集。</p>
<p>如果需要图文显示，且用户浏览速度更快，条目更多的时候，就由表格视图变为了图文并茂的列表视图，如淘宝和美团，只保留一列内容，是为了不打断用户的视觉流。设想一下从上到下，和从左到右+从上到下，哪种方案更好？</p>
<p><b>缩略图</b>（<b>Eventbrite</b>）：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/nXbzveTMGQqa1WKCsEBK.png" alt="APP设计模式之——搜索功能" width="753" referrerpolicy="no-referrer"></p>
<p>缩略图视图模式，指的是搜索结果的内容条目，是将详情页的图文内容进行选取、缩小或模糊处理后，以N个缩略图的方式，展示在搜索结果展示页，因此该模式通常和其他模式混合使用。</p>
<p>甚至<b>地图卫星图</b>（<b>摩拜</b>和<b>ofo</b>）：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/uhxxjggjXoheNvzFKgcv.png" alt="APP设计模式之——搜索功能" width="751" referrerpolicy="no-referrer"></p>
<p>地图/卫星图的视图方式，适合于提供基于LBS（基于地理位置信息服务）的应用，可以为用户提供空间和位置的宏观视角。当然，还有个默认前提就是：搜索结果信息类别单一，比如摩拜和ofo搜索结果都是标准化、同质化的单车，用户不需要关心这辆车有什么特质，只需要关心能不能用即可。</p>
<p>有时根据搜索结果的复杂程度和用户使用首选项的不同，也会使用多种视图显示，如<b>高德地图</b>和<b>Eventbrite</b>，就结合了地图和列表两种视图方式：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/hgi3gSdSe79NqXQ3ZBQo.png" alt="APP设计模式之——搜索功能" width="753" referrerpolicy="no-referrer"></p>
<p>高德地图搜索杨家火锅，火锅这种餐饮行业，即便同一品牌，不同门店提供的服务也可能相差极大，比如店铺环境、人气、价格（不同商圈价格会略有变化，会有一个价格系数）、经营状态、营业时间、评价等，所以除了位置信息，还需要把其他关键信息以列表形式呈现给用户。</p>
<p>而Eventbrite特征更加明显，我输入的搜索条件“基于纽约及周边地图的艺术类活动”显然囊括的内容更加纷繁多样，所以在展示结果时，除了使用地理位置视图，还将活动用列表的形式展现出来，配以主题、时间、地点和价格介绍等。</p>
<h3>2. 内容加载</h3>
<p>在搜索时，通常使用延迟加载技术，使部分结果可以被优先、快速地展示出来，而更多数据则会被延迟加载，这种设计有助于提高用户体验，如<b>Foursquare</b>：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/wKIg7uTv4T3KV1cSUWnf.png" alt="APP设计模式之——搜索功能" width="754" referrerpolicy="no-referrer"></p>
<p>许多应用通过““查看更多” 按钮，或拖动屏幕（上拉刷新）时自动加载更多结果。如<b>LOFTER</b>和<b>ABC News</b>：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/khdISYsJa5DfTXJSDxwn.png" alt="APP设计模式之——搜索功能" width="754" referrerpolicy="no-referrer"></p>
<p>也有应用把延迟加载做得更平滑，拖动屏幕（上拉刷新）时自动完成更新，如<b>开眼</b>，只有在关闭网络的情况下，我们才能看出它的加载交互，是由logo动效完成的：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/lnUkRLFXO6aaUKb5ZV96.png" alt="APP设计模式之——搜索功能" width="752" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、结果筛选</h2>
<p>结果筛选，指在搜索结果的基础上，通过筛选条件，对内容进行过滤，得到更加精确的搜索结果。通常分为前置筛选、后置筛选和全局筛选。</p>
<h3>1. 前置筛选</h3>
<p>前置筛选是在用户触发搜索动作之前进行的筛选，如<b>豆瓣</b>：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/v7HiGoDlEsStwo24vvyI.png" alt="APP设计模式之——搜索功能" width="754" referrerpolicy="no-referrer"></p>
<p>在动态搜索执行完，点击“全部”菜单，在下拉列表中选择“图书”，得到筛选后的结果，再次点击“搜索”按钮，进入展示搜索结果的全屏页：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/VLEbLtoZB1qWHQc4u0GJ.png" alt="APP设计模式之——搜索功能" width="757" referrerpolicy="no-referrer"></p>
<h3>2. 后置筛选</h3>
<p>后置筛选，也称结果筛选。指的是当搜索动作执行完毕后，基于搜索结果，所进行的二次筛选，通常是以“搜索表单”的方式呈现，特点是一个单独的表单输入多个条件和一个明显的搜索按钮。</p>
<p>这种搜索模式常用于内容分类较复杂的应用中，如<b>美团</b>和<b>淘宝</b>使用搜索表单来搜索服务和商品：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/KJHBvQNbEMeyLL1YkmoR.png" alt="APP设计模式之——搜索功能" width="753" referrerpolicy="no-referrer"></p>
<p>全部表单展开后，是这个样子的：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/SNrLm0azeMI89XA976Zu.png" alt="APP设计模式之——搜索功能" width="754" referrerpolicy="no-referrer"></p>
<p>最佳实践：</p>
<ol>
<li>用最少的内容输入，实现精准搜索。</li>
<li>遵循表单设计原则（对齐、标签、大小）。</li>
</ol>
<h3>3. 全局筛选</h3>
<p>有些应用的筛选逻辑只有一层，所有内容都在至少一个分类目录下被收录，各分类目录之间互斥，这样可以保证无论是在搜索动作执行的前面还是后面，都可以设定筛选条件，既可以前置，又可以后置。比如<b>知乎</b>：</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" title="APP设计模式之——搜索功能" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/fxdtGXDgK1MJQhAKRwl5.png" alt="APP设计模式之——搜索功能" width="754" referrerpolicy="no-referrer"></p>
<p>用户既可以在输入搜索条件前在“内容”和“用户”两个标签之间切换，也可以在得到搜索结果后再进行标签切换。</p>
<p> </p>
<p>作者：银发的芝加哥</p>
<p>原文链接：https://zhuanlan.zhihu.com/p/27476719</p>
<p>本文由@银发的芝加哥 授权发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
                      
</div>
            