
---
title: '复盘：B端后台导入功能'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.woshipm.com/wp-files/2022/07/MjIJTjHIc301qXMCqivu.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 29 Jul 2022 00:00:00 GMT
thumbnail: 'https://image.woshipm.com/wp-files/2022/07/MjIJTjHIc301qXMCqivu.jpg'
---

<div>   
<blockquote><p>编辑导读：导入功能是个小功能，通常需要产品设计好一个设计模板，需要规则清晰，提示明确，方便用户进行操作。本文作者根据自身工作经验，对B端后台导入功能进行了复盘分析，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5544370 aligncenter" src="https://image.woshipm.com/wp-files/2022/07/MjIJTjHIc301qXMCqivu.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>做为B端产品人，常常碰到导入功能，虽然是一个小功能，但是在规划的时候，也遇到很多坑，此处用于复盘一个导入功能。</p>
<h2 id="toc-1">一、导入功能分析</h2>
<p>一个完整的导入功能，通常会有几个关键要素：导入模板、导入报错信息、导入过程中相关交互提示，图1为完整的导入功能流程图。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/Hy2qoidzZjnRYhCSdAhs.png" alt width="1066" height="188" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图1 导入功能流程图</p>
<p>在设计一个导入功能的时候，主要围绕关键要素进行展开：</p>
<p><strong>1、导入模板：</strong>支持用户导入模板下载；</p>
<p><strong>2、导入报错信息：</strong>导入数据错误后，支持用户查看导入报错信息；</p>
<p><strong>3、导入过程中相关交互提示</strong>：导入过程中的相应加载样式，以及完成导入或失败导入的对应提示。</p>
<h2 id="toc-2">二、导入模板下载</h2>
<p>通常，产品要提前设计好一个导入模板，规则清晰，提示明确，方便用户进行操作。</p>
<p>前期产品经理针对用户需求，提炼所需要导入的字段，所需要的导入字段有了之后，在设计导入模板时，常常有如下设计要点：</p>
<p><strong>1、模板标题；</strong></p>
<p><strong>2、填写须知描述；</strong></p>
<p><strong>3、导入示例，提示用户按此示例仿照填写；</strong></p>
<p><strong>4、必填、选填字段区分；</strong></p>
<p><strong>5、时间格式规范，如常见的时间格式有2022-07-27、2022/07/27等等；</strong></p>
<p><strong>6、特殊符号限制，比如中英文括号等；</strong></p>
<p><strong>7、固定选项，设计下拉框的格式，不让用户手输；</strong></p>
<p><strong>8、涉及金额等数值的栏位，要标注清楚单位；</strong></p>
<p><strong>9、限制输入格式及文件大小，防止文件过载，导入失败，可在特殊规则描述中指明。</strong></p>
<p>具体模板范例类似如图2，填写须知处可根据实际业务场景说明。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/rZQQYvzKElNHl3ZgNOYe.png" alt width="2570" height="612" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图2 导入模版示例图</p>
<p>备注：</p>
<p>此处模版填写须知中涉及的的单个文件导入不超过5000行，应根据实际开发情况而定，一些设定也可能是通过判断文件大小，而非文件行数。</p>
<h3>2.1 导入模板错误处理</h3>
<p>模版导入过程中，一旦出现导入报错，要针对不同的错误类型，给予不同错误提示。让用户明确应该怎么修改，图3是一些常见的报错信息。</p>
<p style="text-align: center;"><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/ReJ8qxOV41Dn5n7e2qDL.jpeg" alt width="2560" height="1036" referrerpolicy="no-referrer">图3 导入常见报错</p>
<p><strong>1）数据报错提示优先级</strong></p>
<p>一个导入数据，可能同时存在多个错误信息，规定好每个<strong>错误信息的优先判定条件</strong>，报错提示时，通常根据错误信息的优先级，每次提示一条错误原因。用户重新修改后，如果还有其他错误原因，则根据新的错误原因，重新修改重新提交。</p>
<p>此处虽然也可以一次性显示该数据的所有错误原因，但这种提示方式，一旦数据较多，对开发而言，关联校验较为复杂。</p>
<p><strong>2）处理数据重复问题</strong></p>
<p>数据重复问题，可以通过<strong>覆盖、跳过或上传失败</strong>进行处理。根据不同的使用场景，选择不同的方式：</p>
<ul>
<li>若没有提供错误信息，显示上传失败，避免用户修改时，修改了正确数据，反而错误数据没有修改到；</li>
<li>若覆盖后不造成影响，可以直接覆盖导入；</li>
<li>若数据存在唯一编号，不允许重复的情况，可在导入过程，系统直接跳过，在相应的报错提示中，提示清楚错误编号及错误原因。</li>
</ul>
<p><strong>3）特殊字符注意事项</strong></p>
<p>导入过程中，除了上面提到的常见报错类型，还需要考虑是否需要过滤空格，或者excel可能出现的特殊符号，如’符号（用户有时通过导入模板处理数据时，模版编号栏位中有时会带有该符号，如下图4）。</p>
<p>之所以过滤空格和某些excel常见的特殊符号，主要是防止导入内容进行筛选时，精准搜索匹配不到。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/B0ezMpuac4vjMO58mUXa.png" alt width="350" height="356" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图4 excel特殊符号</p>
<p><strong>4）部分导入成功问题</strong></p>
<p>导入过程中的数据报错，通常是部分数据报错，提示错误数据的方式有多种：</p>
<p>方式一：</p>
<p>导入成功的数据，<strong>错误信息直接展示，不支持在线修改</strong>，这种方式开发实现较为简单，但实际用户需要一个个去比对导入模板中的哪条数据错误，体验不太好，如图5。</p>
<p style="text-align: center;"><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/OJSHJSb42dYj5ZOoawUf.jpeg" alt width="1997" height="1440" referrerpolicy="no-referrer">图5 导入报错提示</p>
<p>方式二：</p>
<p>导入成功的数据，<strong>错误信息直接展示，并支持直接修改</strong>，但这种方式通常<strong>适用数据量较小</strong>的情况，如图6，可以直接在弹窗列表中修改信息，修改后提交。</p>
<p style="text-align: center;"><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/wnsL8RJL1MBXwHedAdHk.jpeg" alt width="2021" height="1440" referrerpolicy="no-referrer">图6 导入报错修改</p>
<p>通常导入提示支持直接修改的方式，上述情况只是其中一种，还有许多其他方式，如：</p>
<p>1、导入上传失败后，<strong>提示失败内容，跳转新页面处理，通过【修改】按钮弹窗修改</strong>，这种方式对于报错数据需要分页的比较友好。</p>
<p>2、也有些数据量较少的导入，会在导入上传的时候，支持用户查看即将导入的信息，确定无误后再导入等…</p>
<p>方式三：</p>
<p>导入成功的数据，<strong>错误信息采用文档下载的方式，重新修改错误信息后，再行导入</strong>，这种方式<strong>适合一些数据量较大</strong>的文件，如图7。</p>
<p style="text-align: center;"><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/6LZC6h4PbRsNFk0nuNqx.jpeg" alt width="2069" height="1440" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图7 错误文件下载</p>
<p>有些报错提示，也会在下载错误报告后，加上对应的错误原因展示或者直接在线修改，但如果数据量较大，直接错误文件下载就足够了，不建议加上另外2个。</p>
<p><strong>5）导入后的数据修改</strong></p>
<p>导入后的数据修改方式，有如下2种：</p>
<p><strong>1、列表处直接修改。这种方式适合小数据量修改。</strong></p>
<p><strong>2、导入修改。直接使用导入修改，要根据实际情况判定：</strong></p>
<p>（1）覆盖原有数据；</p>
<p>（2）有重复标识，不支持导入覆盖的，须提供删除功能进行数据删除后，才能重新导入。</p>
<h3>2.1 导入过程中相关交互提示</h3>
<p>导入过程中的加载和相关提示语，可以说是通用规则，作为提升用户体验的方式，必不可少。</p>
<p>1、若数据庞大，导入耗时，可以通过进度条显示，或者类似百度网盘类的下载，显示预计时间，避免用户等待焦虑。</p>
<p style="text-align: center;"><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/1FuzqllTZFXkgMqMfjf0.jpeg" alt width="2560" height="503" referrerpolicy="no-referrer">图8 导入进度条</p>
<p>2、若数据轻量，可以直接通过加载图案，显示导入中。</p>
<p style="text-align: center;"><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/HfW3EPva64tPIucn5fDv.jpeg" alt width="141" height="182" referrerpolicy="no-referrer">图9 导入加载样式</p>
<p>除了加载过程中的交互样式，还有导入失败和导入成功的相应的提示文案也必不可少，毕竟要让一个功能的起始结束，都要让用户有参与感。</p>
<h2 id="toc-3">三、总结</h2>
<p>以上是对近期B端导入功能遇到的一些问题总结，导入功能看着常见，但其实真正设计时，有很多小细节需要思考，此处也仍有很多细节未考虑齐全，未来一边踩坑一边完善自己的相关认知。</p>
<p> </p>
<p>本文由 @小熊不是尼不昵 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5543901" data-author="890081" data-avatar="https://static.qidianla.com/woshipm_def_head_2.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            