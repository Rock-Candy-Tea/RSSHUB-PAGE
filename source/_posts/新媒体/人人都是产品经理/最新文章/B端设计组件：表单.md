
---
title: 'B端设计组件：表单'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/rkOBiCdkPEejmbA17SW4.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 22 Jul 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/rkOBiCdkPEejmbA17SW4.jpg'
---

<div>   
<blockquote><p>编辑导语：表单的存在可以让用户更加清晰地获取反馈结果，进而推动系统与用户之间的信息与数据传递。那么，一个完整且合理的表单由哪些部分构成？本篇文章里，作者对B端设计组件之一——表单进行了总结，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4916445 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/rkOBiCdkPEejmbA17SW4.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>在B端产品中，表单是用户向系统传递和修改数据信息的主要方式，同时也是系统获取用户数据、响应反馈结果的主要方式，可以说表单是人机交互中重要的数据媒介。</p>
<h2 id="toc-1">一、表单构成</h2>
<p>一个完整的表单通常包括标题、必填提示、标签、提示信息、占位符、输入区、操作按钮等几部分。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/qgIGz2OcIZiYtyYO4sDR.png" alt width="765" height="613" referrerpolicy="no-referrer"></p>
<ul>
<li><b>标题：</b>一个表单模块的主题，起到说明表单模块是什么的作用。尤其是在分组表单中的作用更为明显。</li>
<li><b>必填提示：</b>区分多个表单内容项的必填和非选填，一般常用红色的“*”表示。</li>
<li><b>标签：</b>表单内容项的名称，说明对应表单含义以及向用户说明应该录入信息的类型。</li>
<li><b>提示：</b>辅助用户理解操作表单，有引导信息 (说明提示) 和反馈信息用户操作提示两种。</li>
<li><b>占位符：</b>一种辅助用户的录入线索，位于输入区。</li>
<li><b>输入区：</b>表单结构中的核心区域，是用户交互最集中、向系统传递信息的最前线，样式和类型也最为丰富。</li>
<li><b>操作按钮：</b>“完结”表单操作流程的触发器，用于向服务器提交数据或者放弃操作。较复杂表单结构中的按钮也更为复杂。</li>
</ul>
<h2 id="toc-2">二、表单形式</h2>
<h3>1. 标题</h3>
<p>概括表单模块的主题，让用户快速了解接下来的要交互信息内容。相对简单、容易被用户理解的表单可以没有标题，但表单相对复杂或者表单内容项多需要分类组织的时候，标题的重要性就突显出来了。</p>
<h3>2. 标签</h3>
<p>根据标签与输入区的位置来区分，可以分为左对齐、右对齐、顶对齐、内联式、浮动式几种。</p>
<p><b>1）左对齐</b></p>
<p>标签位于输入域左侧，字段左对齐。</p>
<p>“I”字型的视觉动线更加符合现代人们的阅读习惯，阅读效率高的同时也利于用户对标签的整体浏览。但由于表单字段长短不一，造成部分标签和输入区之间的距离较大，从而降低了这些表单标签和与其对应输入区的亲密性，用户的录入的效率也会随之降低，横向排列对页面横向空间有一定要求。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/DPplWQnUQbpm2QagIzMt.png" alt width="768" height="427" referrerpolicy="no-referrer"></p>
<ul>
<li>优点：视觉动线符合人们阅读习惯，在一定程度上节约纵向空间。</li>
<li>缺点：标签与相对应的输入区间距大小不一，录入效率降低，标签、输入区宽度度弹性小。</li>
</ul>
<p>任何事物都是具有两面性的，标签与对应的输入区距离过大会造成视觉断点，影响阅读的连续性，但有些场景需求就是需要引起人们注意，需要严肃、谨慎对待的时候，此时应用这种设计策略会达到较理想的效果。</p>
<p><b>2）右对齐</b></p>
<p>也叫冒号对齐，标签位于输入区左侧，字段右对齐。</p>
<p>右对齐表单的标签和输入区之间的距离是固定的，标签和输入区之间有明确的视觉关联，两者之间的亲密性较高。相对标签简短的表单，用户阅读、填写的效率较高，但对于标签长短不一的多个内容项，左侧的参差不齐又会使得标签不易于完整阅读。横向排列结构对页面的横向空间有一定的要求。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/DpL81zt1903gNAVb0xHi.png" alt width="763" height="424" referrerpolicy="no-referrer"></p>
<ul>
<li>优点：标签与输入区有明确的视觉关联，阅读、录入效率较高，也在一定程度上节约纵向空间。</li>
<li>缺点：表单左侧排列参差不齐，整体阅读性差，标签、输入区宽度弹性小。</li>
</ul>
<p><b>3）顶对齐</b></p>
<p>标签位于输入区上方，字段与输入区左对齐。标签和输入区的亲密性强，“I”字型的视觉动线使得用户阅读、填写效果较高。对于标签字符长度大，尤其是外文标签，顶对齐表单的适应性更强。上下排列结构对页面的纵向空间有一定要求。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/cyy6u5hJaZ7zv3GugYtp.png" alt width="765" height="538" referrerpolicy="no-referrer"></p>
<ul>
<li>优点：对齐方式符合视觉动线，阅读、录入效率高，标签、输入区的横向弹性大。</li>
<li>缺点：一定程度上占用纵向空间。</li>
</ul>
<p>扩展：“I”字型视觉动线从上到下，“Z”字型视觉动线从左到右再从上到下。现实生活中，人们对于左右的反应要弱于对上下，很多人对于分辨左右方向需要一定的反应时间，但对于上下几乎是不假思索的。</p>
<p><b>4）内联式</b></p>
<p>标签在输入区内，类似于输入区的占位符。在用户输入过程中文字标签隐藏，可能会引起用户的迷茫，用户填写完成时不易复核，使用体验一般。另外扩展性也较差，对输入框较友好，而其他类型的表单 (平铺单选、开关) 则会受到限制。</p>
<p>另一变种形式——图标内联式，虽在一定程度上缓解了用户迷茫和怀疑心理，但一些语义性不强的图标也会可能造成用户的认知负担，加大用户学习成本。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/aVJxoJ1BbdywVSM7jg98.png" alt width="769" height="427" referrerpolicy="no-referrer"></p>
<ul>
<li>优点：横向空间要求相对低，表单横向弹性大。</li>
<li>缺点：可能会造成用户迷茫，加大用户认知负担和学习成本。</li>
</ul>
<p><b>5）浮动式</b></p>
<p>标签在输入前位于输入区类似占位符，输入中 (后)，标签向上移动并变小，节约了空间的同时，标签依然存在。</p>
<p>变小后的标签虽一定程度上降低了可视性，但也保障了用户录入信息的准确性和可复核性。与其他几种表单相比，开发实现的难度也相对应的增加了一些。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/nV9fvZpmvN1U0YIyfrOq.png" alt width="769" height="427" referrerpolicy="no-referrer"></p>
<ul>
<li>优点：表单横向弹性大，对纵向空间的要求也不高。</li>
<li>缺点：需要一定的开发难度。</li>
</ul>
<h3>3. 输入区录入方式</h3>
<p>输入区是用户交互最多也是最能影响使用体验的区域，不同类型数据选择与之相应的录入方式，对提高表单操作效率和用户体验大有裨益。依据录入方式的不同可以分为：文本录入、选择录入、上传录入三种方式。</p>
<p><b>1）文本录入</b></p>
<p>文本录入是以文本形式提交信息的交互方式，操作成本较高且过程中又充满不确定性，极易引起用户情绪的波动。在处理这类表单的时候要着重考虑用户录入效率和使用体验。</p>
<p><b>① 文本框（Input）：</b>输入字符总数较少单行录入形式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/ZR8xHSmyE1SMZ2i8O2VT.png" alt width="763" height="424" referrerpolicy="no-referrer"></p>
<p><b>② 文本域（Textarea）：</b>输入字符总数较大且单一文本数据的录入形式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/oJOFJS3278a7CZ9PrZSo.png" alt width="762" height="477" referrerpolicy="no-referrer"></p>
<p><b>③ 搜索（Search）：</b>输入关键字符快速从数据池中匹配与之对应的数据，帮助用户缩小选择范围，快速获取目标数据。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/Yi9Jb9KqEl8d15l2PdtJ.png" alt width="765" height="439" referrerpolicy="no-referrer"></p>
<p><b>2）选择录入</b></p>
<p>选择录入是在已有的备选数据中做选择，相较于文本录入步骤更少、无输入错误风险，录入效率也更高。</p>
<p><b>① 单选框 (Radio)：</b>允许用户在一组默认选项中选择一个，每个选项互斥，有选中和未选中两种状态。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/VmGcOzd1BzxlD51s6GCo.png" alt width="767" height="426" referrerpolicy="no-referrer"></p>
<p><b>② 复选框 (Checkbox)：</b>用户在一组默认选项中选择多个，单个选项间相互独立，常配合全选复选框使用，有全选、半选、未选三种状态。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/xspbA8A9y4HMJkbDOHHX.png" alt width="765" height="428" referrerpolicy="no-referrer"></p>
<p><b>③ 开关（Switch）：</b>用于切换单个选项的状态，适用于两种相对立的状态，如：开和关、显示和隐藏、禁用和启用等。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/jras98jnkyZkxQ28yRn0.png" alt width="765" height="425" referrerpolicy="no-referrer"></p>
<p><b>④ 下拉菜单（Dropdown）：</b>允许用户从已有备选项中选择一个选项或多个选项，相对于单选和复选，下拉菜单可以容纳更多的选项数量，选项数量过于大时常与搜索框结合使用。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/8UTn1gPdLq1cyidh2IME.png" alt width="765" height="439" referrerpolicy="no-referrer"></p>
<p><b>⑤ 滑块选择（Slider）：</b>用户可以在一个连续或非连续的区间内，通过滑动锚点来选择一个合适的数值或范围。</p>
<p>需求精度要求不高的场景下使用「连续滑块」可得到更灵活便捷的操作；需求精度要求高的场景下可配合「数字输入」使用。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/08h5fV21OBebvONxaSlq.png" alt width="767" height="516" referrerpolicy="no-referrer"></p>
<p><b>⑥ 日期选择器（DatePicker）：</b>帮助用户浏览和选择日期，常见有日期选择、时间选择、日期时间选择和相对应的范围选择。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/A3yzzaZJJDOefyTcSCW2.png" alt width="767" height="910" referrerpolicy="no-referrer"></p>
<p>选择录入数据的方式多种多样，还有穿梭框、评分等日常使用频率不高的形式。</p>
<p><b>3）文件上传</b></p>
<p>文件上传是上传信息到服务器的一种数据录入方式，常见有点击上传、缩略图上传、拖拽上传。</p>
<p><b>① 点击上传：</b>通过点击上传按钮唤起的文件管理器来选择需要上传的文件，常用于单个文件上传且不需要预览的场景。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/JWvWY07Mn86zPQ6F3tti.png" alt width="767" height="426" referrerpolicy="no-referrer"></p>
<p><b>② 缩略图上传：</b>也是通过文件管理器来选择需要上传的文件，常用于图片上传，上传的图片在页面中呈缩略图显示，一般还可以直接在缩略图片上赋予其他的交互 (查看、删除等)。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/oDcHrN8S25sxucYKZGWC.png" alt width="767" height="548" referrerpolicy="no-referrer"></p>
<p><b>③ 拖拽上传：</b>用户拖拽文件到指定区域即可完成上传，也支持点击上传。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/TL1bGyeHXgiPY5JqqfqV.png" alt width="766" height="587" referrerpolicy="no-referrer"></p>
<h3>4. 提示</h3>
<p>提示信息的存在是为了辅助用户更好地理解表单、提高录入效率、顺利完成操作任务的。主要有输入前的引导信息和输入中、输入后的反馈信息。</p>
<p><b>1）引导信息</b></p>
<p>对表单填写内容进行解释说明的提示信息，给用户提供录入引导和暗示。有全局引导和内容项引导两种。</p>
<p><b>① 全局引导：</b>对整个表单的解释说明，对于一些包含敏感信息表单，全局提示还包括信息的用途、安全性、保密性等，以此消除用户不信任。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/GmqKIKxWAHJhB0VDJay9.png" alt width="766" height="512" referrerpolicy="no-referrer"></p>
<p><b>② 内容项引导：</b>针对单个的内容进行精确引导提示，提示的形式也多种多样，示例型占位符提示、说明文字提示、图标和气泡组合提示、输入框聚焦提示等，其中图标和气泡的组合提示最为常用，对新手用户、熟练用户都很友好。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/KVi6WIdGuyh7wnKbM0an.png" alt width="765" height="473" referrerpolicy="no-referrer"></p>
<p><b>2）反馈信息</b></p>
<p>包括实时 (操作中) 校验用户录入数据的合规性，和告知用户操作后的结果状态两种。前者主要是前端校验，用来判断数据格式正确与否；后者主要是后端校验，与数据库进行交互匹配。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/bajBLNYQU34a70K0vCTd.png" alt width="765" height="813" referrerpolicy="no-referrer"></p>
<p><b>反馈信息要精准</b></p>
<p>表单录入过程中需要留意反馈信息的时候，大概率是用户录入数据错误的时候（正确的话进行下面的操作了），此时输入错误的反馈信息要足够精确的描述错误原因，帮助用户快速定位错误，辅助用户合规录入。</p>
<p>比如密码录入错误，不要仅仅提示“密码输入错误”，要尽可能提示能帮助用户正确输入密码的话术如“密码是区分字母大小写和数字的组合，如：AAbb123”。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/PDA8zXGZ5SPEbc2GzvO4.png" alt width="765" height="813" referrerpolicy="no-referrer"></p>
<h3>5. 操作按钮</h3>
<p>这里的操作按钮常规意义上指的是“完结”表达操作的按钮，常见在一些较简单的表单场景。在复杂些的表单中，分别会在header区、body区、footer区放置影响全局属性、仅影响跟随对象、有“完结流程”属性的按钮。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/wgJwGKjvsrMum4PDzcVr.png" alt width="768" height="556" referrerpolicy="no-referrer"></p>
<p>按钮本就是B端设计中的一个重大模块，更多详见<a href="http://www.woshipm.com/pd/4824922.html">“B端设计组件：按钮”。</a></p>
<h3>6. 必填提示</h3>
<p>必填提示是在一个表单模块中，用来区分哪些内容项是必填写的，哪些是非必填的。通常用一个红色的“*”表示，过多“*”会造成页面视觉噪点的增多，给本就枯燥的表单页面增加视觉压力；有些情况下，红色作为一种有特殊含义的颜色，会引起用户误解。</p>
<p>为避免过多的视觉噪点，我们可以利用标签或者占位符来提示用户哪些内容项是必填的，哪些是非必填的。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/95544vuQ9KPQ1XpmfGoq.png" alt width="764" height="436" referrerpolicy="no-referrer"></p>
<h3>7. 占位符</h3>
<p>位于输入区内起引导用户录入作用，用户录入数据时就会消失，有示例型占位符和通用型占位符两种。也可以算是一种轻量化的提示信息，与其他提示信息相比，视觉负担较小，占用空间更小，与输入内容的关联性更强。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/2XcF3Z11s6b6bQXy3nKT.png" alt width="765" height="774" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、表单应用</h2>
<p>B端业务场景复杂多样，面对各种各样的表单需求，怎么在满足业务需求的前提下，兼顾页面展示效率，保证用户操作效率和使用体验呢？根据表单任务复杂度的不同，将表单分为下面几种形式去探讨。</p>
<h3>1. 基础表单<b> (直铺)</b></h3>
<p>适合于内容项较少，内容项无明显相关性的表单。</p>
<p><b>1）单列布局</b></p>
<p>在表单页面横向方向上放置一列表单，比较符合人们的阅读习惯，“I”字型的视觉动线引导用户从上到下浏览、填写表单，内容项不多的前提下，是表单操作效率最高的布局方式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/Y5SqPRVmatTFZF9hhCrn.png" alt width="765" height="445" referrerpolicy="no-referrer"></p>
<p><b>2）多列布局</b></p>
<p>在表单页面横向方向上放置两列或多列表单，这样的布局会让页面的利用率得到提升，但“Z”字型的视觉动线引导用户从左到右，再从上到下的阅读，会使操作效率和用户体验在一定程度上打折扣。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/CJmA2TOwIL42gGaswrvV.png" alt width="766" height="633" referrerpolicy="no-referrer"></p>
<h3>2. 分组表单（卡片分组）</h3>
<p>适合于内容项较多，且不同内容之中存在明显相关性分类归纳的表单。</p>
<p>化繁为简是人处理复杂事物常用的方法，通过分组的方式，我们可以将一个较大的的任务分解为几个较小任务，化解表单在用户视觉上的重量，相邻小任务之间的间隔也相当于给用户设置心理休息点，降低用户面对大量录入时的心理压力。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/A34n4UEE6kxjjM9nM9CV.png" alt width="767" height="641" referrerpolicy="no-referrer"></p>
<h3>3. 分步表单</h3>
<p>适用于内容项复杂、有明确先后顺序的的表单内容，将其按照一定的逻辑关系组织成线性流程，利用步骤条告知用户完整流程和进度，当前流程只展示此流程下的表单内容，数据校验也在此流程结束时完成。也是将复杂表单任务切割，提高录入效率，提升用户体验的常用方式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/wJyxHBKkrA8pbjszPyxd.png" alt width="765" height="482" referrerpolicy="no-referrer"></p>
<h3>4. tab页签表单</h3>
<p>适用于内容项复杂，且不同内容可以通过一定的逻辑进行分类归纳的表单内容，不同类别之间相互独立，用户可以切换不同类别浏览填写所有表单数据，表单footer区放置具有“完结”流程属性的操作按钮。也属于一种将复杂表单简单化的方案。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/sNDOEnrqWQAudJ1kV3Tf.png" alt width="766" height="440" referrerpolicy="no-referrer"></p>
<h3>5. 动态可编辑表单</h3>
<p>动态可编辑是指表单内容项是不固定的，用户可以按照实际业务需求对某些内容项进行动态增减。适用于内容项复杂，多任务嵌套使用的场景，常见有动态表单、动态表格、折叠面板、弹窗/抽屉编辑等。</p>
<p><b>1）动态表单</b></p>
<p>用户通过动态增减表单数目来满足业务需求，常见形式有一个固定的表单，通过增减按钮可以设置表单数目，一般动态表单数目≤3。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/q31eXUjSrcp1iHc2M9a8.png" alt width="767" height="480" referrerpolicy="no-referrer"></p>
<p><b>2）动态表格</b></p>
<p>和动态表单的交互逻辑基本一致，外观上是以表格形式展示，增减的动态数据数目建议3~6个。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/835GarG8pBTfAMEusK1H.png" alt width="765" height="516" referrerpolicy="no-referrer"></p>
<p><b>3）折叠面板</b></p>
<p>适用于表单中明显嵌套子任务的模式，收起状态下只读子任务设置，展开状态则可以对子任务的设置进行编辑修改。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/XXY2NzZzElTclmh1cg9v.png" alt width="766" height="864" referrerpolicy="no-referrer"></p>
<p><b>4）弹窗/抽屉编辑</b></p>
<p>常见的处理包含子任务流程、内容项复杂的表单模式，相较于折叠面板扩展性更强，承载的信息更多，一般而言，抽屉的信息承载能力大于弹窗。模态的弹窗/抽屉会打断用户的当前主流程，任务的切割感强。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/4mOoznMUy0JetLxSlrq4.png" alt width="764" height="714" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/OD2s6Lh7PVtzIF8r5bsA.png" alt width="765" height="715" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、实际应用中的一些思考</h2>
<h3>1. 表单输入区的宽度要不要整齐划一？</h3>
<p>很多设计师在拿到表单需求的时候，都会潜意识地追求视觉上整齐划一，强行将表单的宽度定为统一宽度。这种处理方式没有深入思考表单应用规范和用户填写感受。事实上有秩序的“不一致”也不一定要比“整齐”的视觉感受差。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/IA9sMKD86XZM8n8RYSXf.png" alt width="766" height="918" referrerpolicy="no-referrer"></p>
<p>每一类型的表单的输入区都会因其录入需求存在合理的宽度，输入区的宽度应该匹配和暗示其填写的内容。合理的输入区宽度，不仅能够给用户的输入量提供心理预判，还提升整个表单操作过程中的掌控感。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/G3V8KwracpGVPJb39W5b.png" alt width="768" height="438" referrerpolicy="no-referrer"></p>
<p>表单在B端项目的应用场景十分丰富且复杂，针对每一种场景去定制也是不现实的。怎么去兼顾美观和用户的使用体验呢？</p>
<p>结合Ant_Design的解决方案，我们可以定义一个基准输入区宽度和几个不同尺寸的输入区，其宽度按照一定的内在逻辑去生长扩展。例如：基准输入宽度XS = 128px，以其倍数 (n) 加上 (n-1) 倍的间距 (8px) 为规则，分为5种不同尺寸 (XS、S、M、L、XL)。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/2oSX59Ohwh3IByyI8IsJ.png" alt width="766" height="667" referrerpolicy="no-referrer"></p>
<p>表单的外观视觉虽呈现错落有致，但在内在逻辑的约束下做到了“有秩序的不一致”。不仅解决了暗示用户输入量多少的问题，更是避免了设计师在面对表单时不必要的主观和感性，同时开发人员也更容易地做到对设计稿的精准还原。</p>
<h3>2. 表单中的隐藏交互</h3>
<p><b>1）行内编辑</b></p>
<p>一种隐藏较深的富交互模式，一般应用于表格中的较短字段。</p>
<p>用户鼠标滑过字段热区通常会给予明显的视觉反馈，向用户提出交互邀请，点击后原来的只读状态变成可编辑状态，用户修改后点击页面空白地方即可完成操作，被编辑字段除了的字段本身变化外，背景色也可以高亮一会来反馈用户刚刚发生的编辑动作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/zKbUa4YxxGa6cy15Lfrj.png" alt width="765" height="1016" referrerpolicy="no-referrer"></p>
<p><b>2）气泡卡片</b></p>
<p>也是一种隐藏较深的一种富交互模式，用户鼠标滑过字段热区通常会给予明显的视觉反馈，点击后原来的只读状态变成可编辑状态，并弹出气泡编辑面板，用户修改后点击操作按钮完成编辑，气泡面板随之消失，被编辑字段的背景高亮 (3秒)，反馈用户的编辑动作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/f7F4Az1Am6m8j4Twwilu.png" alt width="763" height="1074" referrerpolicy="no-referrer"></p>
<p>可给予用户更大的操作自由度来防止用户犯错，在提示用户操作成功的的全局提示框内，添加“撤销”按钮，给予用户一定的“后悔药”。一定时间 (5s) 后，全局提示消失，“撤销”按钮也随之消失，用户编辑的内容也就不能撤回。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/mnOnzsx8qGsxmD1dAXQd.png" alt width="766" height="491" referrerpolicy="no-referrer"></p>
<h3>3. 按钮没有满足触发条件时要不要禁用？</h3>
<p>表单内容项没有填写完成的时候，操作区的主按钮要不要禁用，处于一种置灰不可点击的状态，只有当满足操作条件时才会高亮并有交互事件?</p>
<p>当表单的内容项非常少 (≤3) 时可以使用主按钮禁用，用户输入内容按钮高亮，这种反馈很容易被捕捉到，也易于用户理解。当表单内容项多有必填和非必填同时存在的时候，此时主按钮禁用会使得用户产生疑问，过长的表单也使用户也不易捕捉到按钮反馈，此时可采用提交校验来对表单信息是否完整进行提示，不建议使用主按钮禁用。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/JKof8TgLBNc2rJA2vz1a.png" alt width="766" height="723" referrerpolicy="no-referrer"></p>
<h3>4. 修改输入区的内容，要不要快速清除按钮？</h3>
<p>修改表单输入区已填写内容时，有的会存在快速清除按钮 (如：密码输入框)，有的则没有，这是为什么呢？</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/PIJ0WbONtdJiL627DoZy.png" alt width="765" height="462" referrerpolicy="no-referrer"></p>
<p>这里的关注点其实还是个效率的问题，这里的效率不只是一个个清除和一键清除的对比，还要考虑到重新录入的效率。</p>
<p>面对一个需要修改的表单我们大概率会在清除后再次录入的，这时候就要考虑录入成本的高低。密码输入错误一键清除后，再次录入也会很快地完成，此时应该为了提高效率应该使用一键清除；而表单中若是我们精心编写的一段话，润色也花费了不少时间，清除后重新录入的的成本就会高很多，此时就应该谨慎提供一键清除。</p>
<p>判断是否需要一键清空按钮，首先需要判断修改成本的高低，低输入成本可以使用一键清空按钮，输入成本较高时，慎用一键清空按钮。</p>
<h3>5. 表单设计小技巧</h3>
<p><strong>1) 优先考虑选择录入</strong></p>
<p>表单样式能用选择的就不要用文本录入，尽量让用户做选择，而不是填空 （填空的不确定性、成本高），除非想要降低操作效率。选择录入不仅仅交互步骤少，更能避免用户对表单的一头雾水以及输入错误的情况。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/6m2n7PMrkglXVLh75M1t.png" alt width="766" height="471" referrerpolicy="no-referrer"></p>
<p><b>2) </b>有限制输入时，给予用户明确的提示，增加用户感知，减少出错率。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/msaps7pOMD5gvDLr7wBM.png" alt width="769" height="427" referrerpolicy="no-referrer"></p>
<p><b>3) 内容排列有逻辑</b></p>
<p>下拉菜单选项按照一定的逻辑排序，例如：根据重要程度。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/hHi4eIURrAZCnp1pqjHq.png" alt width="766" height="491" referrerpolicy="no-referrer"></p>
<p><b>4) 联系上下自动补全</b></p>
<p>在实际的应用场景中，有些表单的信息是可以根据已填写数据联想得到的，此时就应该让这些表单关联已填写的内容自动填写，从而提升整个表单的录入效率和使用体验。</p>
<p>例如：在填写一些与个人信息相关的表单时，输入身份证号后，像省份、出生年月、性别、户籍地址等可以从身份证号中关联到的信息就应该自动填写显示出来，让用户检查关联出的信息正确与否以及修改错误信息即可。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/1gzMg19iWaFNirOuyFwg.png" alt width="767" height="531" referrerpolicy="no-referrer"></p>
<p>更多表单设计小技巧 详见第一篇文章<a href="http://www.woshipm.com/pd/4811937.html" target="_blank" rel="noopener noreferrer">《提升表单设计效果的18个技巧》</a></p>
<p>以上是作者在学习和实际工作中关于表单的一些思考和总结，欢迎大家指正交流。</p>
<p> </p>
<p>本文由@小梗果 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4910764" data-author="1267161" data-avatar="http://image.woshipm.com/wp-files/2021/07/2SCGqUTk8KWcIGQoqCYa.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">1人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602183139_2302.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            