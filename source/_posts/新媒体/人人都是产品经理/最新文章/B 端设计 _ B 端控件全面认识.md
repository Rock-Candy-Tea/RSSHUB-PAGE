
---
title: 'B 端设计 _ B 端控件全面认识'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/AsBTAQGIM3MizbgNm1yi.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 03 Aug 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/AsBTAQGIM3MizbgNm1yi.jpg'
---

<div>   
<blockquote><p>编辑导语：对于B端控件设计，你的了解程度是多少呢？控件可以让用户自然、有效地完成系统功能的使用本文作者介绍了常规的B端控件设计，希望对你设计B端控件有所帮助，我们一起来看下吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4984958 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/AsBTAQGIM3MizbgNm1yi.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、B端基础控件的认识</h2>
<p>控件一词，直译的话可以翻译成 “用来控制的元件”，是我们对 B 端系统进行信息录入、更改、操作的元素。让用户可以自然、有效地完成系统功能的使用，正确使用控件元素是必要的基础。</p>
<p>控件包含的类型、细节、规范非常多，我们先来解释一下，常见的主流控件都有哪些。</p>
<p>第一，按钮类控件，在 UI 界面中应用最多的控件类型，也是理解成本最低的元素。</p>
<p>但是，按钮并不是只有一个矩形框中间放文字而已，还有多种细节的变体。包括但不局限于圆形、前置图标、呈现加载进程等，标签控件本质上也是按钮的一种。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/Tgm1fX5HOJADgNUMIo8I.png" alt width="806" height="328" referrerpolicy="no-referrer"></p>
<p>第二，表单类控件，表单是用来采集信息的控件。比如我们去银行办理业务，就会让你填写一张相应的表单，里面会收集各种不同的信息。</p>
<p>表单类的控件，就是都要根据我们想要采集的数据，以对应的样式、交互呈现给用户。比如文本输入框、单选、复选、下拉菜单、级联选择、滑动条等等。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/ZB4Bs93ak9ADymFsqJIY.png" alt width="765" height="475" referrerpolicy="no-referrer"></p>
<p>第三，时间选择器，即选择某一点或某一段时间的控件。严格来说，它也是表单控件中的一种，之所以单独拿出来讲，是因为它是所有表单控件中最复杂的一类。</p>
<p>时间选择期可以选择日期、时、分、秒，也可以选择一段时间，包含大量的条件和状态判断。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/KMfwW6j0kABmQGV1IPgH.png" alt width="857" height="181" referrerpolicy="no-referrer"></p>
<p>第四，面包屑控件，可以理解成是步骤或层级的表现控件，直观的反应当前页面的位置，可以进行快速的切换和返回。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/p0hU15OUapjUdVswhzUK.png" alt width="787" height="229" referrerpolicy="no-referrer"></p>
<p>第五，页码控件，在通过列表呈现数据项目的时候，往往一页是展示不完的，所以我们会将它切割成若干不同的页面，于是就会使用分页控件帮助用户进行页面的跳转。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/59av20wA47sN4UVXw74c.png" alt width="832" height="276" referrerpolicy="no-referrer"></p>
<p>第六，导航栏，即 B 端内容模块的导航控件，通过导航栏快速切换到不同的模块。主流的B端项目，都会使用侧边导航的形式，也有少部分项目会使用传统项目的顶部导航设计。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/rNgEZLCC6jKG1HxeDqfz.png" alt width="653" height="1146" referrerpolicy="no-referrer"></p>
<p>第七，开关，即对某判断事件进行是或否的控制元素，和手机中我们使用的开关功能一致。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/JEuNLdILq7icaWtalTfO.png" alt referrerpolicy="no-referrer"></p>
<p>第八，分页选择控件，英文是 Tabs，在我的用法里从来不把 Tab 直接翻译成 “标签” 和英文 Tag 冲突。它的功能即切换对应内容区域的控件，和手机分页器一样。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/X3Ak5sHqYorGvMDiYmlV.png" alt width="783" height="352" referrerpolicy="no-referrer"></p>
<p>第九，提醒类控件，用来提示、警示用户的一系列控件类型。包含类似警告弹窗、强提示、气泡、侧边提示栏等等。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/npES8kD08WrGnJPbaLcs.png" alt referrerpolicy="no-referrer"></p>
<p>以上就是我们在设计 B 端中常见的控件类型，有一个基本的认识，那么下面就分别讲解它们设计的要点，以及常用的参数特征。</p>
<h2 id="toc-2">二、按钮的设计要点</h2>
<h3>1. 按钮的尺寸</h3>
<p>按钮是整个 UI 中最基础的控件，学习任何一种 UI 类型的控件，都从按钮展开。在移动端中，有官方建议的合理触控区域 44pt 作为参照，来划分大、小按钮，但在网页项目中，并没有那么明确的官方建议。</p>
<p>所以，我们根据过往的经验，依旧先将按钮划分成大、中、小三个等级，然后再讲解它们对应的长宽数值区间。</p>
<p>首先从小按钮开始说起，前面我们讲过，中文最小字号在 11px，那么最小的按钮尺寸就必然大于这个数值。所以，对于比较次要的按钮、标签，建议使用 16-28px 高的按钮。</p>
<p>中按钮，一般应用在一些表单确认、取消、上传等基础功能的使用上，可以使用 28-44px 高的按钮。</p>
<p>大按钮，就比较特殊，只有在登陆或者是意义非常重大的场景下（比如删除重要数据提示）才会使用，它的高通常在 44-64px，大于 64px 的按钮在 B 端项目中基本不会存在，除非有特殊的业务要求。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/utfitXEoje0nZVsUbTX6.png" alt width="588" height="419" referrerpolicy="no-referrer"></p>
<p>前面讲的都是按钮的高，那么按钮的宽怎么来的呢？按钮的宽度设置有两种，一种是定宽，一种是自适应宽度。</p>
<p>定宽按钮没有非常明确的数值标准或比例标准，基本要求就是大于等于宽。常见的定宽按钮宽高比为 1:1、2:3、2:1、3:1 。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/lsfnZRpbTmzCChZTvSHn.png" alt referrerpolicy="no-referrer"></p>
<p>虽然宽度没有设限，但在网页和手机客户端不同，不会做出远远大于高，甚至撑满屏幕的按钮，这在巨大的电脑画布中不仅不协调，而且会看起来非常不像按钮。</p>
<p>自适应按钮则是根据宽度进行伸缩的按钮类型，通过定义左右内边距的数值，来计算按钮实际的宽度。无论里面只有文字还是图标文字混合，使用自适应按钮都可以完美匹配。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/H1R3VfSrFkack9H0cSHb.png" alt referrerpolicy="no-referrer"></p>
<h3>2. 按钮的状态</h3>
<p>除了长宽尺寸外，还要额外关注按钮的状态。按钮并不是一个 “死” 的静态视觉元素，它本身包含了若干种不同的状态，需要通过视觉样式进行传达。</p>
<p>比如最常见的，就是默认、悬浮、点击、不可点状态。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/gqoFcnTmn9M7W7RLf8qp.png" alt width="762" height="220" referrerpolicy="no-referrer"></p>
<p>除此以外，当按钮本身加入更多的功能、内涵以后，我们都需要根据它的使用场景来考虑对应的状态，如下载按钮，有些平台点击下载需要一个比较长的加载过程，于是这个Loding的动画就可以在按钮中进行呈现，表示下载请求正在处理，而不是让用户以为这是一个无效的按钮。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/tX7eS7rQM3B8F0FYjxBQ.png" alt width="766" height="313" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、表单控件的设计</h2>
<p>表单是一个大类，包含的控件非常多。如果我们把每个细分选项都单独挑出来讲，那可以写一本 B 端字典了。</p>
<p>所以，我们可以从输入框这个控件入手，优先确认输入框的尺寸基础，然后再根据它拓展出其它的相关控件元素出来。</p>
<h3>1. 输入框的尺寸定义</h3>
<p>输入框虽然不如按钮出现频率高，包含的尺寸规格极多，但同样也有大小之分。</p>
<p>常规输入框的高度在24-48之间，根据实际场景的需要，尽量以4的倍数来定义输入框的高度。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/xGse2gupSlj7uosn3vDp.png" alt referrerpolicy="no-referrer"></p>
<p>单行输入框宽度通常是固定的，不像按钮会向右延伸，所以输入框的宽度需要根据对应的场景，输入内容的长度来判断，没有统一的标准，尽量不要制定远低于实际内容长度的数值即可。</p>
<p>虽然我们定制的输入框看上去好像就是给一个矩形背景，把字体丢进去居中对齐就好。但是，开发中一个输入框实际的尺寸，是通过内部元素尺寸+内边距实现的。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/dSJ7isOqyQ8trnxKiKpt.png" alt referrerpolicy="no-referrer"></p>
<p>所以，输入框出现多行的时候，并不是简单把原来的尺寸x2，而是先确定内部元素的行高，一个支持多行显示，默认高 36px 的输入框，行高20，那么当出现两行的时候高 56，三行高 76，以此类推。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/51XeiEprSwX75wEbP5nb.png" alt width="750" height="1045" referrerpolicy="no-referrer"></p>
<h3>2. 下拉菜单</h3>
<p>输入框完成以后，那么之后的下拉菜单，在默认状态下和输入框就几乎使用了一样的样式，只是增加了可以下拉的示意或图标。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/QHjjMufSK4ZHAglUjA0f.png" alt width="751" height="466" referrerpolicy="no-referrer"></p>
<p>在下拉菜单中，如果包含了列表选项，那么每个列表的高度，也可以使用相同的尺寸，而不用给出一个新的数值。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/fCpJNpOclB4vgGZ5otzo.png" alt width="774" height="740" referrerpolicy="no-referrer"></p>
<h3>3. 单选和复选控件</h3>
<p>接着，就是单选和复选框的设计了，如果只看视觉效果，单选复选的实际大小好像都不大，不需要和输入框有瓜葛。</p>
<p>这么想就不对了，实际上这类控件中，都有包含对应的选区，它的实际大小并不是我们视觉上的边缘。而我们使用的实际背景选区尺寸，同样使用输入框的大小来制定，并对内容进行居中。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/xhr22lePZe1Cru3NGoKx.png" alt width="802" height="466" referrerpolicy="no-referrer"></p>
<p>比较值得新手注意的是，在设计这类控件时，单选和复选框的尺寸，要控制在12-20px，超过20像素的选框会明显偏大，缺失细节感。</p>
<h3>4. 滑动条控件</h3>
<p>之后，就是滑动条控件的设计了。滑动条控件的样式看起来并不复杂，一般由一个圆形滑块（也有方形）和一个进度条组成。</p>
<p>在这类控件中，进度条的粗细虽然可以自由定义，但尽可能不要使用 1px，因为实在太细了，做的浅了看不清楚，做得深了又有很强的割裂感。</p>
<p>关键点在于对滑块本身尺寸的控制上，前面我们讲过单选和复选框的尺寸，实际上这个滑块是可以继承单选或复选框尺寸的。当它们使用相同大小的时候，往往在并列、并排的时候，会让整个表单系统看起来更和谐、统一。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/7pJxQWFsatUWI0O5rBQH.png" alt width="654" height="197" referrerpolicy="no-referrer"></p>
<p>表单的设计，就是从输入框和基础的表单类型入手，然后再根据这些元素的尺寸拓展出后续其它表单控件的尺寸。</p>
<p>所以，掌握这种思路，就不需要对大量的表单控件死记硬背，可以灵活应对不同的表单设计需求。</p>
<h2 id="toc-4">四、时间选择器控件</h2>
<h3>1. 时间选择器的组成</h3>
<p>时间选择器，是一个非常复杂的控件，通常它由一个下拉菜单和时间面板组合而成。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/QfLSdmduexEk42OHG3t4.png" alt width="572" height="763" referrerpolicy="no-referrer"></p>
<p>下拉菜单作为一个表单控件，设计的方式前面已经说过了。时间的选择包含两种类型，单点选择和范围选择，单点是具体到某天某日某时，比如闹钟提醒，而范围是从某个时间点到另一个时间点之间的值，例如酒店预定时长。</p>
<p>不管使用哪种选择类型，我们优先要注意时间的层级格式，要显示年/月/日，还是精细到时/秒/分，以及链接层级的符号。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/hLFXvRAJcoQ5NmMLSKWB.png" alt width="626" height="312" referrerpolicy="no-referrer"></p>
<p>单点选择模式的表单相对容易，就仅仅是显示格式上的差异。但是，在范围选择中，表单的设计就有比较大的差异，要包含起始和结束两个时间点。</p>
<p>我们可以在一个表单方框中将前后两个时间点都囊括进来，也可以将开始和结束拆分成两个表单，两种模式都有各自的交互逻辑和使用方式。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/SvJ1hhfJ1w3cD8tISrnB.png" alt width="816" height="150" referrerpolicy="no-referrer"></p>
<p>而点击表单后，就是弹出的时间选择面板。一个最完整的时间面板，会包含年份选择、月份选择、星期标识、日期选择、分时秒选择。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/iyZT5yppUEFQWnhUKsaZ.png" alt width="844" height="199" referrerpolicy="no-referrer"></p>
<h3>2. 时间选择面板的定义</h3>
<p>下拉菜单部分的设计，和前面的表单输入框基本一致，我就不在这里继续讨论了，主要来分享关于时间选择面板的设计尺寸。设计该面板的时候，也是先从模块入手：</p>
<ul>
<li>年/月份选择</li>
<li>日期选择</li>
<li>分时选择</li>
</ul>
<p>每个模块都有高度的设置规则，年/月和分时选择栏，都可以采取定高的模式设计，可以使用 28-36px 的高度。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/o2FqRDAavY81qRy8W48R.png" alt width="640" height="658" referrerpolicy="no-referrer"></p>
<p>而对于日期选择模块，高度的设计则有比较特殊，模块的总高度不需要提前制定，而是根据内容行数决定。包含星期标识行、日期行数。</p>
<p>每个日期的数字，都由一个完整的矩形 View 包裹，整个日期展示区域，就是由这些矩形拼装而成，每个矩形可以是正方形也可以是纵向长方形。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/tJXPSdgXlikIWyVxmxtA.png" alt width="616" height="621" referrerpolicy="no-referrer"></p>
<p>在这个模式下，如果要增加选中模式，可以直接通过填充背景 View 的色彩来完成。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/B280TgKwpbfZoYYtPxCC.png" alt width="659" height="397" referrerpolicy="no-referrer"></p>
<p>日期数值的显示也有状态的区分，包含 “不可选” 和 “今天” 两个。不可选的日期置灰即可，而标识今天的日期数字，可以使用特殊的色彩或添加特定的符号标识。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/GM9FeeiMPwSBhjJYCbBk.png" alt width="712" height="579" referrerpolicy="no-referrer"></p>
<p>最后，就是包含具体分时选择的设置了，如果这个时间选择器中即包含了从日期到秒的选择，那么在面板中，就建议使用手动输入的方式来完时、分、秒的设置。</p>
<h2 id="toc-5">五、面包屑控件</h2>
<p>面包屑控件，用来表示用户当前所处页面的层级，由页面链接和分隔元素组成，是一个比较容易设计的样式。页面链接主要由文字展示，比较少会在这个部分玩花样，最多关注当前页面和上级页面的色彩差异。</p>
<p>在设计它们的时候，最简单的做法，就是使用文本框直接键入，如：电话亭首页 > 课程 > B端入门电话亭首页 / 课程 / B端入门如果要严谨一点，可以将手动键入的大于号换成箭头图标。</p>
<p>这种基础的形式占据了 95% 以上的项目场景，只有在高度复杂，层级众多的项目中，我们会额外在该控件中增加页面下拉菜单，以及使用的筛选标签元素。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/Mugerz40hSKMF9FQ10dz.png" alt referrerpolicy="no-referrer"></p>
<h2 id="toc-6">六、页码控件</h2>
<h3>1. 页码控件的组成</h3>
<p>页码控件是用来控制列表翻页的工具，当列表条目数量超出单页显示数量以后就会均分成若干数量的页面，以页码控件进行翻页和跳转。</p>
<p>在这个应用场景中，包含许多需要考虑的因素，核心问题来自页面数量过多和有限的展示区间的矛盾。对于数据量较大的列表，展示的数据往往会超过4位数，这就需要我们提供多种交互元素来辅助用户进行页面跳转。在最完整的页码控件中，会包含下面这些元素：</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/utzAJyaq6T0ByNM7iI6w.png" alt width="871" height="134" referrerpolicy="no-referrer"></p>
<p>不同的系统或者页面，对所需的交互元素要求是不一致的，需要我们根据页面的目标来判断应该放哪些内容。</p>
<h3>2. 页码控件的尺寸</h3>
<p>该控件的设计，样式上主要的差异是是否包含矩形边框，不过不管这个边框是否可见，我们也依旧会以创建 View 视图的方法来设计它。页面控件的设计首先从页码数字开始，优先制定高度，再根据数字数来制定宽度。通常，这类标签按钮的高度在 28-36px 之间。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/KKnr68ifcuChqmqshWa5.png" alt width="862" height="238" referrerpolicy="no-referrer"></p>
<p>宽度非固定的设计模式是一个必须注意的问题，因为 1 位数和 4 位数所需空间是有非常大差异的。只要确认好左右间距的数值，那么设计后面的前/后翻页、输入框、页数等内容，就会变得非常清晰了。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/WF5nAxEoVQ7kpeEall1q.png" alt width="870" height="297" referrerpolicy="no-referrer"></p>
<p>页码设计中，不要遗漏的就是省略号了，它代表还有大量的页码没有被展示出来，通常这个省略号只出现在最后一页或者最开头一页中。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/yQPFdpxFGln8acIshQlu.png" alt width="827" height="357" referrerpolicy="no-referrer"></p>
<p>切记不要把省略号安置到序列的中部，变成类似下方这种状态：1·2·3·4·5 …… 996·997·998·999</p>
<h2 id="toc-7">七、导航栏控件</h2>
<h3>1. 导航栏的组成</h3>
<p>在今天，99% B端项目导航栏都坐在左侧，内容在右侧，通过选择左侧导航的链接快速打开和跳转到不同的模块中去。</p>
<p>导航栏的设计相对一般组件来说，对页面的视觉效果影响更大，因为导航栏有较大的占比，而且通常为了和内容做区分，都会采用和右侧相反的色彩进行凸显，或使用品牌色。</p>
<p>常规的导航栏中，仅包含的内容有后台 LOGO、导航选项。复杂的情况下可能还包含头像、提醒、定制模块，暂时不用考虑。导航选项是导航栏的关键所在，最简单的B端项目往往只有一级，但业务越多的项目导航选项的层级也就越多，会以树桩的形式展开和收起。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/xSsaL7CufLkgxe1sucOt.png" alt width="586" height="713" referrerpolicy="no-referrer"></p>
<p>对于一些适配支持比较好的项目，导航栏还会有缩略模式，即缩减宽度后只显示图标或更改文字排列方向的状态。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/WN8aV4NImTpeWMEw6DeV.png" alt width="310" height="1575" referrerpolicy="no-referrer"></p>
<h3>2. 导航栏的数值</h3>
<p>在导航栏设计中，一般LOGO放在顶部，使用 28-64 之间的高度，然后下方才放导航选项。只要项目不太复杂，那么就建议为导航提供统一的高度，从32-48px 之间选择。</p>
<p>即使是二级标题，也可以使用相同的高度而不用特地缩小，通过变更文字的色彩、缩进的方式来表现层级的区别，这样在交互中更具整体性。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/yjDsAcvIRixh6woSCIoH.png" alt width="503" height="917" referrerpolicy="no-referrer"></p>
<p>如果使用缩略型导航，则宽度控制在 32-64 即可。</p>
<h2 id="toc-8">八、开关控件</h2>
<p>开关控件作为用来控制功能启停的元素，包含开启、关闭、禁用三个基本状态。B端开关设计受到移动端系统的影响，所以和我们手机上使用的开关控件样式几乎一致。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/4wb5lIoAkjY4WIo4JjIt.png" alt width="665" height="358" referrerpolicy="no-referrer"></p>
<p>但是，并不是所有启停场景下都适用这种开关，如果启用和关闭的逻辑比较复杂，那么就可以使用表单的两个单选项控件并添加文字提示，或者使用勾选完成开启关闭。</p>
<h2 id="toc-9">九、分页选择控件</h2>
<p>在B端的分页器中，设计的规格和移动端是不同的，移动端应为屏幕窄，经常将 2、3 个分页标签进行均分来实现布局。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/aysjyIgMaPXEUo1HxAWw.png" alt width="734" height="168" referrerpolicy="no-referrer"></p>
<p>而在 B 端分页控件，也优先确定设计的高度，小分页控件在 24-36 之间，大的在 36-64 之间。如果文字字数不太多，就使用等宽的设计，如果文字数量比较捉摸不定，就采取等内边距自适应设计。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/YIGwbAHgfI5UqwEgar7D.png" alt width="725" height="337" referrerpolicy="no-referrer"></p>
<h2 id="toc-10">十、提醒类控件</h2>
<p>最后，就是提醒类控件的设计了。提醒类控件一般包含两个类型，弱提醒和强提醒。弱提醒是直接悬浮在画面中，不会对遮挡以外区域有太大影响，并会自己消失的提示，也可以称为 Toast 气泡框。这个框的设计，是确定四周内边距的宽，然后再根据文字内容来展示。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/LhbUUytVYz382UQxcgLW.png" alt width="665" height="360" referrerpolicy="no-referrer"></p>
<p>而强提示弹窗，则是一个正常的弹窗。我们会在这个弹窗中置入标题、文本、按钮三种要素。并且，为了体现 “强”，会对窗口下方的界面使用黑色遮罩，让用户注意力集中到窗口中！这类黑色遮罩通常使用透明度为 40-60% 的黑色，太浅和太深都不好。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/L8aKQrXDS5idugJUkJNd.png" alt width="783" height="431" referrerpolicy="no-referrer"></p>
<h2 id="toc-11">十一、结语</h2>
<p>今天的分享就到这边，对于控件组件的说明，我会在后面单开更全更更细节的干货分享出来。</p>
<p>掌握这两篇内容中设计的逻辑，就可以拓展到其它类似组件和元素中去。主要掌握的是设计的方式，而不要硬背具体的数值。</p>
<p> </p>
<p>本文由 @酸梅干超人 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4977700" data-author="840505" data-avatar="http://image.woshipm.com/wp-files/2021/07/JCf8Fx1LZhUm0zOfxAw4.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            