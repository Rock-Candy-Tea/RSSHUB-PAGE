
---
title: '有点不一样！亚马逊 AWS 云产品交互设计细节分析'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/04/ORi5sBOXqnIvpM2bKoaw.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 11 Apr 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/04/ORi5sBOXqnIvpM2bKoaw.jpg'
---

<div>   
<blockquote><p>编辑导语：亚马逊的AWS云产品连续 11 年被 Gartner 评为“全球云计算领导者”，作者在使用了这个产品之后，发现了一些设计特点，本文通过6个方面来进行介绍，让我们一起来看看吧！</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-784446 aligncenter" src="https://image.yunyingpai.com/wp/2022/04/ORi5sBOXqnIvpM2bKoaw.jpg" alt referrerpolicy="no-referrer"></p>
<p>最近体验了亚马逊的AWS 云产品，发现了一些设计特点分享给大家。由于云产品业务比较复杂，我无法从业务角度做出分析，只能做一些交互方面的评判。大家也可以了解下国外产品与国内产品在交互上的差异。</p>
<p>本文内容主要有以下几个方面：</p>
<ol>
<li>弹窗的应用</li>
<li>面包屑导航</li>
<li>表格设计</li>
<li>分屏展示</li>
<li>版本切换</li>
<li>悬停交互</li>
</ol>
<p>PS：因为 AWS 云科技是一个大平台，我只是做了部分产品的体验，难免有些遗漏或者以偏概全，感兴趣的同学可以自己去体验一下。或许有不一样的发现。</p>
<h2 id="toc-1">一、弹窗替代</h2>
<p>弹窗是B端产品中重要的组件，可以承载业务内容、给出用户反馈等等，使用频率比较高。不过在亚马逊云产品中，弹窗主要用在一些设置项和内容选择的场景中例如下图，存储桶名称采用了文本框输入形式，用户也可以点击按钮打开弹窗选择内容。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/PYAhnQpW03gUaPjaTqJF.png" alt width="389" height="301" referrerpolicy="no-referrer"></p>
<p>不过有没有更好的操作方式呢？输入框改为下拉选择控件是不是更简单呢？</p>
<p>是因为选择项很多，下拉选择不方便？或者用户要查看存储桶的详细信息才能确定选择目标？这个点我没想明白。</p>
<p>总的来说，弹窗用的比较少，而是采用其他形式做了替代。</p>
<h3>1. 错误信息内嵌</h3>
<p>在亚马逊中，错误信息直接展示在页面底部，从而减少了弹窗的应用，也减弱了阻断感。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/xsPXhhVTR1r4pANvuSR8.png" alt width="389" height="301" referrerpolicy="no-referrer"></p>
<h3>2. 高成本行为减少误操作</h3>
<p>删除或者禁用内容时，为了避免用户误操作，我们经常会使用二次确认弹窗。</p>
<p>在亚马逊中则是采用了输入固定信息的方式，避免用户误操作，也可以省略弹窗提示。不过用户的交互成本是不是太高了呢？</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/zpHqnFDVosrlJv4T9YJF.png" alt width="389" height="301" referrerpolicy="no-referrer"></p>
<h3>3. 隐形弹窗</h3>
<p>在亚马逊上传文件时，上传的过程及完成后的结果采用的是弱弹窗样式。并非传统意义上增加了遮罩的弹出层。主要是由于内容很多，干脆将弹窗铺满了整个内容区，给人感觉像是普通页面，只是需要通过右上角按钮关闭窗口。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/vpOyQPOQRDTKfKiaY8hS.png" alt width="389" height="301" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、面包屑导航</h2>
<p>在亚马逊中，面包屑是一种非常重要的导航方式。用户进入到操作页面时，左侧导航菜单会自动收起，给内容区更大的展示空间。另外功能的配置大都采用页面跳转方式完成，导致功能路径比较深。所以面包屑菜单成为了唯一的导航方式。</p>
<p>而在国内云产品中，腾讯云、华为云都将页面层级尽量扁平化，一般不超过3级，所以取消了面包屑导航。阿里云虽然保留了面包屑菜单，但是在二级页面中都增加了“返回”按钮，面包屑的作用也被弱化了。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/9i9peOuhaNOpZvYVot8v.png" alt width="389" height="301" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、表格设计</h2>
<p>在B端产品中，表格是非常重要的组件。亚马逊中表格设计有比较明显的特点。</p>
<h3>1. 右上角的翻页器</h3>
<p>亚马逊将翻页器放置在了表格的右上角，个人认为不太符合用户的视觉动线。国内翻页器都是放在表格下方，毕竟用户浏览到表格底部就可以翻页了。放在右上角可能的原因有2点（个人猜测）：</p>
<p>节约空间。单独的页码条会占据一行页面空间；为了节约空间，表格每页显示的行数，被放在了首选项设置，表格项总量则被在了表格标题后面（见上图）；</p>
<p>亚马逊通过调研或者数据了解到用户翻页行为比较少。主要是通过搜索定位内容，并能够在首页就可以找到目标；</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/OLrFx0vuhlKUaFCK4CSE.png" alt width="389" height="301" referrerpolicy="no-referrer"></p>
<h3>2. 自动换行</h3>
<p>我们在表格中经常会遇到内容显示不下的场景。通常我们会选择截断方式，鼠标悬停触发气泡显示全部信息。</p>
<p>在亚马逊产品中，则引入了excel 表格自动换行的方式，在首选项中勾选自动换行后，表格就可以完整字段信息，便于用户更方便的浏览完整信息。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/E7jt4g8WWQLTAfZX7SNQ.png" alt width="389" height="301" referrerpolicy="no-referrer"></p>
<h3>3. 右键功能</h3>
<p>亚马逊表格中没有单独的操作列，只能选定表格项后，激活功能按钮进行操作。而国内表格大都支持批量和单个操作两种方式。</p>
<p>不过为了弥补操作列的缺失，亚马逊表格中增加了右键功能，用户可以在表格首选项中开启右键菜单功能，可以替代浏览器的右键菜单。另外右键的优势就是可以承载更多的菜单项。不过对于用户来说，可能需要重新适应这种交互方式。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/Bt2QbmD3T6hx5651KNGH.png" alt width="389" height="301" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、分屏显示</h2>
<p>Web系统中详细信息主要是采用弹窗、抽屉、页面跳转等方式呈现给用户。在亚马逊产品中设计了分屏模式。用户选择表格项后，下方会展示表格项的详情内容，并且分屏空间可以拖动或者设定三个显示尺寸。从而减少用户的跳转，操作更加高效。不过这种方式在大屏显示器上应用效果会更好。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/IfgKQPTVbmU3fc2sHdIy.png" alt width="389" height="301" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、版本切换</h2>
<p>如果采用A/B test，我们更希望用户体验新版本，从而获得更多的反馈信息。所以旧版本入口大都会弱化展示。而亚马逊则采用了开关方式切换版本，放置在醒目的标题菜单的位置。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/TnlIFXHph1X70BrBDN2K.png" alt width="389" height="301" referrerpolicy="no-referrer"></p>
<h2 id="toc-6">六、点击VS悬停</h2>
<p>在亚马逊中很少使用悬停交互，更多采用点击方式。例如表格中的访问权限的解释信息，是通过点击操作完成的，想要去关闭浮窗信息，要点击空白处或者关闭按钮。</p>
<p>而我们为了减少用户操作，通常会优先选择鼠标悬停的方式触发内容展示，随用随走，交互上更加轻量。</p>
<p>另外为了减少页面信息量，我们会根据信息重要性，将解释说明内容隐藏在图标里，通过悬停方式触发。在亚马逊产品中，我没见过这种交互方式。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/YHU4zyfRlCpUwNovoRuU.png" alt width="389" height="301" referrerpolicy="no-referrer"></p>
<h2 id="toc-7">七、总结</h2>
<p>我不是AWS 云产品的重度用户，体验也不深入。总的来说，感觉 AWS 与国内的产品有较大的差异。AWS更加朴实，程序化风格比较重。国内的云产品则更多的融入了互联网的风格。以上就是我对AWS 云产品的体验总结。</p>
<h3>#专栏作家#</h3>
<p>子牧先生，微信公众号：HelloDesign，产品体验设计师</p>
<p>本文原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5386802" data-author="200991" data-avatar="http://image.woshipm.com/wp-files/2020/10/KjOwksgBxtYVlDsqUgAh.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            