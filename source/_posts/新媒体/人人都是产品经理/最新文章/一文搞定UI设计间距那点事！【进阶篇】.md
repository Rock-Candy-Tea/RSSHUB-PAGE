
---
title: '一文搞定UI设计间距那点事！【进阶篇】'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.woshipm.com/wp-files/2022/07/0vzyoXaeKKYw7gQZIn1T.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 18 Jul 2022 00:00:00 GMT
thumbnail: 'https://image.woshipm.com/wp-files/2022/07/0vzyoXaeKKYw7gQZIn1T.jpg'
---

<div>   
<blockquote><p>导读：UI设计由三大元素组成，即色彩、图形、文字，其中图形与文字的排版方式是建立视觉层级的重要元素。两者结合的媒介就是间距，合理的间距能给用户带来具有美感且舒适的视觉体验，本期我们就聊一聊UI设计中间距那点事。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5529639 aligncenter" src="https://image.woshipm.com/wp-files/2022/07/0vzyoXaeKKYw7gQZIn1T.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、文字与间距</h2>
<p>文字是UI设计中最重要的信息传递元素，文字的排版看似容易其实并不简单，因为文字的属性众多，比如字号、字间距、行高、段落等等。</p>
<p>很多设计师对文字属性很了解，也能够合理运用，但总会卡在开发环节，花费很长时间验收，最终还是得不到理想效果。</p>
<p>下面我们从根上去认识文字，对文字中能够影响排版间距的属性，一一解析，并且了解开发逻辑，正确与他们对接。</p>
<h3>1. 文字-行高</h3>
<p>字体设计师，为了能满足文字行间距的合理展示，通常会给字体设定一定的行高。</p>
<p>行高就是在设计软件中选中文字后，上下外边框高度，字体的行高没有标准，不同的字体一般默认行高也不一样。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/XZ9tdLIbvmbrv85ShTnS.png" referrerpolicy="no-referrer"></p>
<p>也就是因为字体的行高，让UI设计师对文字与其他元素的间距设定，有不同的见解。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/lelHSLKXhBfMqmvKqD8Z.png" referrerpolicy="no-referrer"></p>
<p>上图都是30px的间距，但因为字体行高不同，A、B两个方案的实际视觉间距不同。</p>
<p>认同A方案合理的设计师，理由是文字最好设置一定的行高，不然折行时视觉上没有行间距，很拥挤，不得不再设置行高，最终30px的间距还是有间隙。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/AhvX0ojytRApIcxG4nOo.png" referrerpolicy="no-referrer"></p>
<p>认同B方案的设计师，理由是UI设计本身对几个像素的差距就很敏感，视觉上做不到统一，就是不合理。</p>
<p>两者的表述都对，但也确实都有一定的弊端，下面给大家介绍两个解决方案。</p>
<p>可以确定的是，为了满足文字折行后的阅读性体验，最好带有一定的行高，这样也会利于与开发对接。</p>
<p><strong>第一种：</strong></p>
<p>首先说一下UI设计中，间距设定的一个理念，间距设定一般要设定一个最小栅格基数，如4、5、6、8为间距设定的起始数值。</p>
<p>然后页面中，接下来所有的间距设定，都得是这个数值的倍数。（这点后面会详细讲解）</p>
<p>‍在一个带有文字的设计组件中，若设计思路上要呈现视觉统一的间距，那可以算出字号与行高的间隙，然后减去相对应的栅格数值，使其视觉上接近统一的间距。</p>
<p>下图所示，设计思路上想呈现一个30px的统一间距，那就可以减去一个最小栅格数值。</p>
<p>若最小栅格数值是6px，最终给出的间距就是24px，视觉距离呈现的就是接近30px的距离。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/IE2emrwBAOJrxclRuG8v.png" referrerpolicy="no-referrer"></p>
<p>这种方式也是我一直以来用的方法，好处就是没有打破间距设定的原则。</p>
<p>设计的间距与开发看到的间距，都是有规律的栅格系统间距。</p>
<p>唯一有点不完美的地方就是，实际距离有时还会有一点小误差，但其实在视觉上也完全可以忽略掉了。</p>
<p><strong>第二种：</strong></p>
<p><strong>第二种方式就是精益求精，不考虑间距的栅格系统原则，算出字号与行高的间隙，间距上准确减去，保证没有一丁点的误差。</strong></p>
<p>我找了一下这样的产品，发现iOS端的滴滴APP中，有个模块是这样的设计理念。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/AvMSPDgBfomoU7OCBzxU.png" referrerpolicy="no-referrer"></p>
<p>上图案例中，字号36px，行高44px，文字上下的间隙就是4px。</p>
<p>所以设置距离26px，加上行高间隙正好是30px，得到统一的间距效果。</p>
<p>这种方式有一个小小的弊端，就是开发感受不到间距的规则，最终设计验收时可能会耗费更多的时间。</p>
<p><strong>特殊情况：</strong></p>
<p>另外有一种情况，就不能刻意去追求文字的视觉对齐，除非是平面设计，因为开发的逻辑也不会去支持这样做。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/96Aegcv6KSd7TZ7SfHjg.png" referrerpolicy="no-referrer"></p>
<p><strong>上图中错误的方式是因为，开发写这个卡片，会写成一个容积俗称盒子，内容都会放在盒子里面，就算内容过多，也是向下进行扩展适配。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/9YtWCwyFIY4DuRWdjOY6.png" referrerpolicy="no-referrer"></p>
<h3>2. 开发对接-关于行高（重点内容）</h3>
<p>字体行高的间隙有了解决方法，接下来是与开发的对接，这也是最关键的一个环节，设计的再好，最终不能很好的落地，也是白搭。</p>
<p>UI设计师在设计验收iOS端时，可能会遇到这样的问题，设计与开发都用了同样的间距参数，但最终呈现的间距还是不一样。</p>
<p>原因就是，同样的苹方字体，iOS端开发的默认字体行高，与设计软件中的字体默认行高不一样。</p>
<p>比如在Sketch软件中42号字的苹方字体默认行高是59，但是iOS开发软件中默认是52。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/WxIpBofSUl3cR2aupuK6.png" referrerpolicy="no-referrer"></p>
<p>如果开发不手动调整字的行高，就会出现与设计的偏差。</p>
<p>根据我的调研，iOS开发工程师，若不是特殊情况，基本不会去改默认行高参数。</p>
<p>下面我们列举一下，设计常用苹方字号的默认行高，与iOS开发默认行高的数值对比，从中找一下规律。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/u3tkrMEO1fpnCjakkYBX.png" referrerpolicy="no-referrer"></p>
<p>上图中可以得出，字号越大，设计默认行高与iOS开发默认行高差距越大。</p>
<p>所以设计上最好把默认行高改成与开发一样的默认行高，这样才能保障，开发不手动调整行高下，是一致的。</p>
<p>iOS开发字号默认行高有一定的规律，随着字号的增加，行高会在字号基础上+4、+6、+8、+10以偶数递增。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/sKWJ1OC4BbpGXt3oBiaO.png" referrerpolicy="no-referrer"></p>
<p>虽有规律但也不容易形成记忆，推荐一个公式。</p>
<p>用字号除10后乘以2，再加上字号，就是iOS开发的默认行高，公式如下：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/jAfSe1x4QgAnpYQiSijY.png" referrerpolicy="no-referrer"></p>
<p>有公式可能还不够便捷，再给大家推荐一款Sketch行高修复插件，Auto Fix iOS Text Line Height for Mac 。</p>
<p>这款插件是专门针对iOS字体行高修复，使其与开发默认行高保持一致。</p>
<p><strong>关于安卓：</strong></p>
<p>安卓系统 Material Design 使用的字体，中文是思源黑体，英文是Roboto。</p>
<p>因为安卓系统开源，不同的安卓手机厂商大多会更换字体。</p>
<p>比如小米手机MIUI系统中英文都使用Misans字体，所以安卓文字行高没有一个标准。</p>
<p>安卓开发与iOS开发还有个不同点是，安卓开发使用什么字体，行高就是字体本身的默认行高。</p>
<p>思源黑体行高默认和字号大小一样，Roboto行高接近苹方字体行高。</p>
<p>如果设计稿按安卓规范设计，那思源黑体最好设置成与苹方字体一样的行高，然后安卓工程师手动去调整，iOS开发工程师所见即所得。</p>
<p><strong>字体修复后使用经验：</strong></p>
<p>关于修复后字体的使用方式，分享一些经验，UI设计中使用文字的频率很高，有标题、副标题、正文、辅助文字等，字号都有所不同。</p>
<p>当在设计中，确定这些文字字号后，做一次行高的修复，然后把这些文字创建成字符样式，每次用时从字符样式库里面选择即可。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/YRBcS99o6STpi2Ctxq0k.png" referrerpolicy="no-referrer"></p>
<p>最后说一下，特殊情况结合自身产品风格，去定义文字行高是完全没有问题的，开发可以根据设计的定义的行高进行调整。</p>
<h3>3. 文字-段落</h3>
<p>在有段落的文案中，很多设计师为了方便，直接给一个回车键的段落间距，这样是万万不可取的。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/t1MEBYZIPcTI8QB10BYP.png" referrerpolicy="no-referrer"></p>
<p>一个回车键的间距，就是一行字的行高，通常这个间距都比较大，就算设计风格需要这么大的间距，那一定也要手动去设置段落。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/QxvKnmGRCBsVFsKiRmJp.png" referrerpolicy="no-referrer"></p>
<p>段落数值的设定，一般情况要大于文字行高的一半，比如文字行高为42，那段落最好大于21，这样段落间距加上文字行高，整体就是≥1.5倍。</p>
<p>为什么是≥1.5倍？原因是文字的行间距，一般大于1.5倍视觉上是比较舒适，例如字号是30，那行高设置为45，形成1.5倍的间距。</p>
<h3>4. 文字-字间距</h3>
<p>字间距是字与字之间的间距，默认一般为0不做设定，特殊设计风格以外。</p>
<p>有一种情况，当一段左对齐文字中存在标点或数字英文字母时，那末尾可能不够一个字符的空间，就会出现末尾留白的情况。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/DLtoMbsedyZLQw5QxHfy.png" referrerpolicy="no-referrer"></p>
<p>出现这种参差不齐的情况，确实不那么美观，但在UI设计中实属正常。</p>
<p>不用刻意去设置成左右水平对齐，这样虽整齐，但因为不同的字间距会影响阅读体验。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/UGgL3pRIuB8NvbYpmGCW.png" referrerpolicy="no-referrer"></p>
<h3>5. 文字-字号</h3>
<p>不同字号间距设定有一个原则，<strong>当字号越大时，字与其他元素间距也就需要相对越大。</strong></p>
<p>字号越大说明级别越高，级别越高从信息层级上来讲，就需要较大的间距来呈现。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/QzuG0VlKLc56m8xJUHf7.png" referrerpolicy="no-referrer"></p>
<p>这是客观上的一个原则，文字越大，就需要更多的留白去承托，就像文字的行高，字号越大文字的行高增加的倍数也就越大。</p>
<h2 id="toc-2">二、如何定义间距？</h2>
<p>间距是UI设计中建立信息层级、提升阅读体验、表达元素之间的关系、表现重要信息的重要方式。</p>
<p>定义合理的间距其实非常有学问，打开京东、淘宝你会发现元素之间的间距非常紧凑，打开爱彼迎、蔚来又会发现元素之间较为宽松，这是为什么？</p>
<p>其实就是他们的设计语言不同，致使展示出的形态也就各异，而间距就是表现设计语言的其中一种方式。</p>
<p>在UI设计中，间距的设定一般会选择一个最小栅格基数，如4、5、6、8等数值，之后页面中，所有的间距都要以，最小栅格基数的倍数呈现。</p>
<p>谷歌推出的设计语言 Material Design 推荐栅格系统的最小基数是8dp，一切间距、尺寸都应该是8dp的倍数。</p>
<p>淘宝的设计，据我所知用的是5的基数，爱彼迎用的是8的基数，从这点来看，基本可以得出一个结论，使用越小的数值基数，设计呈现通常就会越紧凑。</p>
<p>一个最小栅格基数的倍数值有很多，但其实通常有6个左右常用间距，就能满足绝大多数的场景。</p>
<p>我目前负责的产品最小栅格基数是6，设计上常用间距大概有6个，完全能够满足大多数设计场景所需。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/5NvQeY63LbEtAcj2SPSZ.png" referrerpolicy="no-referrer"></p>
<p>这些间距其实并不用刻意去选择，当你使用最小栅格倍数值时间长了，就能自然得出几个常用的间距，字号的选择使用基本也适用这个逻辑。</p>
<p>另外，一个产品中模块众多，难免会出现一些特殊情况，所以肯定不能限定死只可以用那几个间距。</p>
<p>除了上图中列举的常用间距之外，12、36、90、120等一些间距数值也会用到，只是用的频率不会很高。</p>
<p><strong>案例解析：</strong></p>
<p>接下来，根据最小栅格基数为6的设计规范，通过一个商品卡片案例，分析一下间距设定的几个原则。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/2JXllZChy7tOEsTYPEpO.png" referrerpolicy="no-referrer"></p>
<p>上图中，首先要给各个元素分类，比如主标题和副标题是一类内容；标签是一类内容；价格是一类内容；“找相似”按钮又是一类内容。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/MOxRvCYQ6Em0BK1GOw3x.png" referrerpolicy="no-referrer"></p>
<p>根据亲密关系原则，同类内容的间距应该更近，这样有利于建立信息层级关系，提升用户的可读性。</p>
<p>具体多近呢？可以根据商品卡片在页面中的外边距，来进行分析定义。</p>
<p>看一个产品的外边距基本能判断，是宽松型排版，还是紧凑型排版。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/0RTkCAcK2L9I6Chq31iZ.png" referrerpolicy="no-referrer"></p>
<p>产品的外边距是根据设计语言，产品定位，产品内容多少等来定义，常见的边距有20、24、30、36、48、60等。（大概就是这个范围内）</p>
<p>使用较大外边距，内容区域的间距要小于外边距，小到可以直观分辨即可，这样可以体现出页面中，内容的亲密关系。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/qavjKlkJIwDNqdhwhwK2.png" referrerpolicy="no-referrer"></p>
<p>使用常规外边距，比如我们的案例中，使用30px就是常规外边距，内容区域要适当小于或等于外边距，这样视觉上体现的是统一性。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/qujWX0jIDeOJh6YN0D7K.png" referrerpolicy="no-referrer"></p>
<p>主标题与副标题属于同类项，它们之间的间距一定要小于，卡片的内边距，这样整体看上去才能体现信息层级。</p>
<p>间距小到多少，还是那个理念，可以直观感受到比内边距小即可为止，不能过小。</p>
<p>一般来说，视觉上的间距大概是内边距（同模块中的大间距）的一半，就会表现的不错。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/f2ISdqpA6lFBRpNOcMZN.png" referrerpolicy="no-referrer"></p>
<p>案例中设置的是一个栅格单位6px，再加上文字的行间隙，视觉上大概就是15px的间距，就是内边距的一半。</p>
<p>接下来，给案例加标签，标签与文字不是同类信息，所以要适当与主副标题拉开间距。</p>
<p>通常第一选择就是，视觉距离与内边距30px，保证统一。</p>
<p>案例中设置的是24px，再加上文字的行间距，就非常接近30px。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/8UzHEoTy47Mh5iAG4mVq.png" referrerpolicy="no-referrer"></p>
<p>接下来是价格，对于一个商品卡片设计，价格是需要着重突出体现的。</p>
<p>一般设计上要突出一个元素，大概3种方式：一是改变颜色；二是放大；三是加大留白；也就是加大间距。</p>
<p>案例的商品卡片，设计风格价格颜色规范是黑色，所以颜色不能改变。</p>
<p>只能放大或加大留白，放大和留白得在合理的范围内，不然就会破坏卡片的整体结构性。</p>
<p>间距上与标签设置30px的间距，加上文字的行高，视觉上的间距，会成为卡片中最大的间距留白，从而起到突出的作用。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://image.woshipm.com/wp-files/2022/07/T25f1QCNvR59Q3dBtkoR.png" referrerpolicy="no-referrer"></p>
<p>这种设计方法，在一个设计组件中，最好只出现一个，不然整体结构就会有一定程度上的破坏。</p>
<p>另外强调一下，统一性固然重要，但设计的核心是为需求目标服务，所以，这时候统一性的优先级是次于需求目标的。</p>
<p>就像淘宝首页的瓷片区，间距非常紧凑，失去了一定的美感，但这样做确实展示了更多的内容，满足了需求目标。</p>
<h2 id="toc-3">三、最后</h2>
<p>最后做个总结：</p>
<ol>
<li>关于文字的间距，要考虑文字的行高，尽可能保持视觉统一性；</li>
<li>iOS设计稿，设计软件中默认的文字行高，与开发软件中的默认行高不一致，最好修复行高，与开发保持一致；</li>
<li>文字段落不要用回车键去定义，要用段落参数，段落间距通常要大于文字行高1.5倍；</li>
<li>多行文字出现这种参差不齐的情况，不要设置为左右水平对齐；</li>
<li>一般字号越大，字与其他元素间距也需要越大；</li>
<li>UI设计要结合产品定位等，制定最小栅格基数，然后任何间距要以最小栅格基数的倍数呈现；</li>
<li>一个产品中，通常设置6个左右的间距数值，能满足大多数设计的场景；</li>
<li>善于使用亲密关系、留白理念、统一性等设计原则，设计前理解需求目标。</li>
</ol>
<h3>#专栏作家#</h3>
<p>吴星辰，微信公众号：互联网设计帮，人人都是产品经理专栏作家。</p>
<p>本文原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5529480" data-author="882855" data-avatar="https://static.woshipm.com/WX_U_201905_20190514184830_8086.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            