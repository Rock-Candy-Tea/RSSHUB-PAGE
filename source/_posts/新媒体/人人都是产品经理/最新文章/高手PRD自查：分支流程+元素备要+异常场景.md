
---
title: '高手PRD自查：分支流程+元素备要+异常场景'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/03/Pk5xnziJb5UAKVVzZrBL.png'
author: 人人都是产品经理
comments: false
date: Tue, 15 Mar 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/03/Pk5xnziJb5UAKVVzZrBL.png'
---

<div>   
<blockquote><p>编辑导语：经常会有这样的情况，当你自信满满地把PRD给开发，自以为十分完美了，然而事与愿违，不一会儿就发现有满满的漏洞等着补。要走出这个困境，应该注意分支流程穷尽+元素备要+异常情况穷尽，一起来看看吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-769606 aligncenter" src="https://image.yunyingpai.com/wp/2022/03/Pk5xnziJb5UAKVVzZrBL.png" alt referrerpolicy="no-referrer"></p>
<p>问：把大象放进冰箱需要几步？把长颈鹿放进冰箱需要几步？</p>
<p>答：把大象放进冰箱共需要3步，把长颈鹿放进冰箱共需要4步。</p>
<p>把大象放进冰箱，第一步：打开冰箱门；第二步：把大象装进去；第三步：关好冰箱门。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="高手PRD自查：分支流程+元素备要+异常场景" src="https://image.yunyingpai.com/wp/2022/03/FYdDUt08WD7tllWKtsxK.png" alt="高手PRD自查：分支流程+元素备要+异常场景" referrerpolicy="no-referrer"></p>
<p>把长颈鹿放进冰箱，第一步：打开冰箱门；第二步：把大象取出来；第三步：把长颈鹿装进去；第四步：关好冰箱门。</p>
<p>把这个顺序交给人去干，一般没问题。然而，把这个步骤直接描述给程序，一定出问题。</p>
<p>因为问题并没有想象的那么简单：</p>
<ul>
<li>大象不肯进去怎么办？</li>
<li>冰箱太小装不下怎么办？</li>
<li>好不容易塞进去，冰箱门关不上怎么办……</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="高手PRD自查：分支流程+元素备要+异常场景" src="https://image.yunyingpai.com/wp/2022/03/x6uIdNlbsUwm3aUfhS8a.jpeg" alt="高手PRD自查：分支流程+元素备要+异常场景" referrerpolicy="no-referrer"></p>
<p>于是交付给程序的实际流程图需要如下：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="高手PRD自查：分支流程+元素备要+异常场景" src="https://image.yunyingpai.com/wp/2022/03/U3dCskpMHA4mF27NvpJ2.jpeg" alt="高手PRD自查：分支流程+元素备要+异常场景" referrerpolicy="no-referrer"></p>
<p><strong>这就是在产品设计中常常会遇到的问题。</strong></p>
<p>自信满满把PRD给到开发同学的时候，刚出去玩一会回头就发现满满的漏洞等着补。</p>
<p>只有手忙脚乱地，开始各种填坑……</p>
<p>这本质是马克思所说的事物矛盾的普遍性导致的。解决办法就是辩证看待，对立统一。</p>
<p>落地一点说，主要得兜住三个方面：分支流程穷尽+元素备要+异常情况穷尽。</p>
<h2 id="toc-1">一、分支流程</h2>
<p>当然我们做设计的时候，主要精力肯定是应该集中在主要任务和流程上，分支流程虽说是小概率事件，但是也要有所考虑，不然方案就会不完整。</p>
<p>解决这个问题，<strong>根本上是场景的穷尽。</strong></p>
<p>需要注意：现实业务的场景枚举，与设计方案的枚举没有绝对对应性。也就是穷举场景可能是四个，但是实际上只需要三个方案就能覆盖。</p>
<p>但是场景枚举之间和分支方案之间存在MECE的属性。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="高手PRD自查：分支流程+元素备要+异常场景" src="https://image.yunyingpai.com/wp/2022/03/qIkSbbd39tfmCtFfDibJ.png" alt="高手PRD自查：分支流程+元素备要+异常场景" referrerpolicy="no-referrer"></p>
<p>案例：</p>
<p>OMS系统与亚马逊店铺对接的前提是：亚马逊店铺可用、对OMS系统已授权、OMS系统开启对接。</p>
<p>成功对接后，来自亚马逊的某些操作，会导致对接异常。此时通过接口返回错误提示，可以展示在OMS系统的店铺上，提醒商户处理。</p>
<p>那么这里有多少分支场景呢？</p>
<p>场景一：店铺被亚马逊封了，接口返回店铺异常信息。需用户在亚马逊处理。</p>
<p>场景二：店铺被用户在亚马逊关闭了。接口返回店铺异常信息。 需用户在平台处理。</p>
<p>场景三：店铺被用户在亚马逊自行注销了。接口返回店铺异常信息。需用户在平台处理。</p>
<p>场景四：OMS系统授权失败或者亚马逊变更了授权信息。接口返回店铺异常信息。需在OMS系统以正确的信息重新授权。<br>
这个是第一性的，此后才能判断功能是否覆盖到上述场景。</p>
<p>针对场景到功能设计，本质是一种映射：</p>
<p style="text-align: center;"><strong>y=f（X）</strong></p>
<p>映射是分层的。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="高手PRD自查：分支流程+元素备要+异常场景" src="https://image.yunyingpai.com/wp/2022/03/MX55apcQQamBPsIbctWo.png" alt="高手PRD自查：分支流程+元素备要+异常场景" width="705" height="525" referrerpolicy="no-referrer"></p>
<p><strong>功能，</strong>是将业务进行功能层面的映射；</p>
<p><strong>产品，</strong>是对若干业务段在产品层面的映射；</p>
<p><strong>数据层面</strong>，设计一个数据表，是对实体属性的描述，E-R图 (Entity Relationship Diagram，实体-联系图)就是实体到数据层面映射的示意图；</p>
<p><strong>而字段层面，</strong>字段与属性之间也建立映射关系；</p>
<p><strong>数智层面，</strong>数字孪生、VR、AR都是对事物的图像化映射和展示；</p>
<p><strong>云计算层面，</strong>云服务是对实体物理技术设备生产力的虚拟化映射。</p>
<p>一些细致末梢的流程可能会采用放弃，或者粗鲁的<strong>兜底方案</strong>。但这不代表放弃。而是每个流程在方案层面都有所交代。</p>
<h2 id="toc-2">二、元素备要</h2>
<p>如何一网打尽才是重要的。大多数是把每个流程都是按前、中、后进行要素的齐备。</p>
<h3>1. 设计前</h3>
<p>主要检查点：用户类型、帐号体系。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="高手PRD自查：分支流程+元素备要+异常场景" src="https://image.yunyingpai.com/wp/2022/03/0UcT3LYHDuZyt7shRfij.jpeg" alt="高手PRD自查：分支流程+元素备要+异常场景" width="789" height="150" referrerpolicy="no-referrer"></p>
<p>未登录：登录和未登录按钮权限差别，需要登录后才可操作的功能是否备注。</p>
<p>用户权限：需要读取权限吗？如何描述读取内容让用户读？不同权限管理。</p>
<h3>2. 设计中</h3>
<p><strong>1）框架阶段</strong></p>
<p>主要检查点：层级关系、信息区分、扩展性。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="高手PRD自查：分支流程+元素备要+异常场景" src="https://image.yunyingpai.com/wp/2022/03/6qDyvoCsNSEF5535w7wE.jpeg" alt="高手PRD自查：分支流程+元素备要+异常场景" width="758" height="155" referrerpolicy="no-referrer"></p>
<p><strong>2）流程阶段</strong></p>
<p>主要检查点：角色，入口，目的，操作，离开、中断。</p>
<p>「我是谁？从哪里来？要到哪里去？怎么去？还有谁？」。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="高手PRD自查：分支流程+元素备要+异常场景" src="https://image.yunyingpai.com/wp/2022/03/HhyQWBcocUEPwSTFpPDS.jpeg" alt="高手PRD自查：分支流程+元素备要+异常场景" width="817" height="137" referrerpolicy="no-referrer"></p>
<p>要看流程有没有短路，如果过程中有中断，中断后要怎么提示，如果有不同的权限和角色，还得检查相互之间有没有相通和关联的地方，共同的关键节点。以及逆向操作。不同角色不同场景的任务流程一定要单独梳理。</p>
<p><strong>3）内容显示</strong></p>
<p>主要检查点：数据显示、缓存、内容、状态（特别是为空、初始）、显示（各种极限情况）。「为空、初始、极限情况」。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="高手PRD自查：分支流程+元素备要+异常场景" src="https://image.yunyingpai.com/wp/2022/03/ltxZbxdwtqZKpBeuw12B.jpeg" alt="高手PRD自查：分支流程+元素备要+异常场景" referrerpolicy="no-referrer"></p>
<p><strong>4）反馈通知</strong></p>
<p>主要检查点：通知，提醒，界面反馈，用户反馈入口。</p>
<p>「操作的任何阶段（前、中、后被中断）都要防止用户发呆」。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="高手PRD自查：分支流程+元素备要+异常场景" src="https://image.yunyingpai.com/wp/2022/03/MAo8r7qtUjDT08TSRDQC.jpeg" alt="高手PRD自查：分支流程+元素备要+异常场景" width="807" height="242" referrerpolicy="no-referrer"></p>
<p><strong>5）文本控件</strong></p>
<p>主要检查点：表意清晰、使用一致。「结合流程检查要符合操作的前后情景，符合用户的常规认知和习惯」。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="高手PRD自查：分支流程+元素备要+异常场景" src="https://image.yunyingpai.com/wp/2022/03/PHvVUiVjFOghD2X13oMq.jpeg" alt="高手PRD自查：分支流程+元素备要+异常场景" width="787" height="232" referrerpolicy="no-referrer"></p>
<p><strong>文本内容：</strong></p>
<ul>
<li>文本长度：是否有限制？</li>
<li>文案内容：是否完整、通俗易懂、有趣</li>
<li>超过负载时如何显示？</li>
<li>核心词汇是否统一（如各种用户角色名称）</li>
<li>重要、复杂的操作内容是否有清晰的解释说明？</li>
<li>浏览到内容底部的情感化表达</li>
</ul>
<p><strong>控件：</strong></p>
<ul>
<li>按钮类型：主按钮、次按钮、幽灵按钮、虚线按钮是否按需区分使用（一般一个界面或视窗中只有一个主按钮）</li>
<li>按钮状态：默认、经过、点击、置灰、选中、加载中（提交按钮）；其中不同状态下按钮的置灰，是否有说明为什么不可用？以及按钮激活条件是什么？</li>
<li>链接：点击后颜色是否有变化</li>
<li>选择组件：单选、多选、tab选，是否有默认选中项</li>
<li>输入框：输入及时校验，有错误时定位；有特殊输入条件限制的输入框是否有明确说明</li>
</ul>
<p><strong>表格：</strong></p>
<ul>
<li>基础表格：内容项过多时，考虑将次要身份鉴别类信息隐藏，鼠标浮动到对应字段后浮窗显示</li>
<li>表格排序：默认排序和切换排序，核心字段的默认宽度</li>
<li>表格操作：考虑在当前表格内完成（页内编辑）；批量操作时对于互斥的选项处理</li>
<li>对齐：一般文字左对齐，数字右对齐</li>
<li>折叠、展开：主要内容在列内显示，更多内容点击展开显示</li>
<li>分页：表格内容翻页展示还是无限加载？若分页每页显示多少条内容？</li>
</ul>
<h3>3. 设计后</h3>
<p>检查点：设备、中断情况、网络情况、特殊状态、刷新方式、异常操作。「多页面通用内容放在一页一起搞定」。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="高手PRD自查：分支流程+元素备要+异常场景" src="https://image.yunyingpai.com/wp/2022/03/CvsvWVfacGTpyboYWNaT.png" alt="高手PRD自查：分支流程+元素备要+异常场景" width="768" height="598" referrerpolicy="no-referrer"></p>
<p>从A状态到B状态：</p>
<ul>
<li>触发源：操作按钮在当前界面中是否明确？</li>
<li>触发区域：操作按钮是否易操作易触达？</li>
<li>未释放状态：考虑内容过多或展示过快时支持长按停留内容；是否可以取消，例如发送语音消息，此时是否允许用户取消发送？</li>
</ul>
<h2 id="toc-3">三、异常情况</h2>
<h3>1. 异常流程</h3>
<p>退出、撤销、重置、返回、不通过、过期失效</p>
<ul>
<li>返回：从哪里来是否可以回到那里去</li>
<li>保存：复杂任务流是否支持保存或自动保存；意外退出前保存提示</li>
<li>复杂状态之间的变化关系：子流程梳理辅助说明</li>
</ul>
<h3>2. 刷新和加载</h3>
<ul>
<li>刷新：自动还是手动刷新？每次刷新加载多少条内容？刷新失败如何提示？</li>
<li>无线刷新：顶部下拉、底部上拉，安卓有刷新按钮</li>
<li>加载：复杂页面是否有副列表加载？预览、保存、提交的完成时间若超过3S是否有加载的过渡状态？新加载内容是否有高亮底纹显示？</li>
</ul>
<h3>3. 网络异常</h3>
<ul>
<li>没有网络（无网）</li>
<li>网络超时（断网）</li>
<li>网络太慢（弱网）</li>
<li>网络环境变化：从WiFi到数据流量环境时是否需要切换视图</li>
<li>加载失败：是否自动重新加载？</li>
</ul>
<h3>4. 操作异常</h3>
<ul>
<li>连续多次点击给予反馈、统一设备登录多个账号验证码、统一IP；连续破坏性操作n项内容时是否需要身份验证。</li>
<li>数据相关：进入页面后服务器获取不到数据；搜索无结果状态；数据加载时间较长时预设默认图片、状态、内容框架；</li>
<li>错误提示页：404页面、即将上线、页面失效、服务下线、系统繁忙，考虑出错页面内容情感化表达以减弱用户的受挫感。</li>
</ul>
<h2 id="toc-4">四、PRD自查</h2>
<h3>1. 按功能插件自查</h3>
<p><strong>1）输入框</strong></p>
<p>需限定输入的范围，做输入校验。</p>
<p>示例：最多输入10个数值，输入不合规则的内容，则在输入框下方红色字体提示，比如：“请不要输人汉字！”。</p>
<p><strong>2）下拉框</strong></p>
<p>下拉的同时是否支持输入搜索，是否支持多选。</p>
<p><strong>3）导入文档</strong></p>
<p>表头校验、自校验、与系统校验、写入逻辑（全部不予导入或部分导入)、下载结果文档；</p>
<p><strong>4）已有功能的逻辑规则变更</strong></p>
<p>则要考虑旧数据兼容或初始化。</p>
<p><strong>5）基础数据删除</strong></p>
<p>则要考虑基础数据被调用的地方，删除和编辑怎么处理。</p>
<p>比如：商品分类中维护的“商品类型”被删除，那么再编辑和删除该分类下的历史数据的时候就可能报错，所以基础数据维护时候要校验调用情况。</p>
<p><strong>6）设置规则</strong></p>
<p>考虑规则去重、规则优先级。一般情况下，没有优先级的话，规则的去重和命中次序校验起来比较麻烦。（在<后端产品经理宝典>一书中有专门介绍）。</p>
<p><strong>7）列表的数据的排序</strong></p>
<p>一般按照修改时间的倒叙排列，也可以用数据库id代替序号。用数据库id的好处是，方便用户和技术协作追溯数据。</p>
<p><strong>8）异常机制</strong></p>
<p>每时每刻都要有逆向思维，告诉开发人员什么算异常？异常了怎么标示出来。</p>
<p>比如：表1字段A，匹配表2字段B，将匹配成功的数据写入表3。就要考虑表1中字段A为空的情况该怎么办。</p>
<p><strong>9）页面长期不登录</strong></p>
<p>则给自动退出。主要考虑到后端系统的保密性。</p>
<p><strong>10）凡是带操作的</strong></p>
<p>一般都要设置页面权限。最简单的方式是所有系统的权限都分三个等级：不能查看、只能查看、可以编辑。</p>
<p><strong>11）功能修订</strong></p>
<p>比如规则变更，需要考虑旧数据是否要按照新规则进行初始化。</p>
<h3>2. 按需求类型自查</h3>
<p><strong>1）功能需求</strong></p>
<p>需要穷尽功能覆盖的使用场景，穷尽本功能相关联的各个系统模块，穷尽本功能的用户角色、权限。</p>
<p><strong>2）性能需求</strong></p>
<ul>
<li>数据量较大时的系统压力、反应速度；</li>
<li>批量上传、下载要考虑数量上限，考虑是否异步处理；</li>
<li>考虑浏览器兼容性；</li>
<li>考虑调用接口超时的备用策略等。</li>
</ul>
<p><strong>3）安全需求</strong></p>
<p>敏感词屏蔽（同步过滤和异步召回）、防刷单机制、数据补推机制、风险预警等。</p>
<h3>3. 关键词提醒自查</h3>
<p>笔者不完全罗列了几个关键词，可以作为自查的维度。</p>
<p><strong>1）完整</strong></p>
<p>流程是否存在断头路。</p>
<p><strong>2）逆向</strong></p>
<p>功能流程是否可逆，如果逆向操作，是否考虑对应的机制：比如退款、退货操作。</p>
<p><strong>3）异常</strong></p>
<p>即异常机制。各个步骤都可能出现预期外的情况。</p>
<p><strong>4）歧义</strong></p>
<p>需求文档的语法、功能文案、名词是否易懂，是否存在歧义。</p>
<p><strong>5）兼容</strong></p>
<p>是否存在兼容问题：不同业务人员对功能都能接受吗？各个系统之间兼容吗？新旧功能的兼容吗（比如历史数据要不要初始化）？</p>
<p><strong>6）备用</strong></p>
<p>是否有备用方案，次级选项。比如当正常流程无法传输的时候，是否可以用导入的机制救急。业务高峰的系统，是否有降级处理逻辑。</p>
<p><strong>7）穷尽</strong></p>
<p>业务场景和可能原因是否穷举完毕。</p>
<p>默认：是否给予了默认值。</p>
<p>比如设置规则功能业务未设置怎么办？</p>
<p><strong>8）脱敏</strong></p>
<p>是否存在敏感信息，是否有脱敏机制。</p>
<h3>4. 其他</h3>
<p>自查的方式还有很多，比如也可以按照“增、查、改、删、显、传、算”自查等。</p>
<h3>#专栏作家#</h3>
<p>唧唧歪歪PM，公众号：唧唧歪歪PM（ID：jjyypm），人人都是产品经理专栏作家，2019年年度作者。《后端产品经理宝典》作者，药学硕士转行互联网产品多年；熟悉跨境电商业务，医药领域；擅长大型后台体系，社交APP。</p>
<p>本文原创发布于人人都是产品经理，未经作者许可，禁止转载</p>
<p>题图来自pixabay，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5354610" data-author="195416" data-avatar="http://image.woshipm.com/wp-files/2020/03/Gk8VXhA3hfl6JZiywk2K.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            