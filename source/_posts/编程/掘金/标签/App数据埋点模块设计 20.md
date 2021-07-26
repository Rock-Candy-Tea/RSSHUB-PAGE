
---
title: 'App数据埋点模块设计 2.0'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b26e377fd004b47a18fd6aa322201b9~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 17:30:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b26e377fd004b47a18fd6aa322201b9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">概述</h2>
<p>在项目开发初期，我为产品设计了一套简易的埋点框架，主要解决了如何定义埋点，以及如何管理埋点的配置。随着项目能力不断的扩展，简易的AOP采集以及手工埋点方式在迭代速度上逐渐无法满足。以及依赖发版才能新增埋点数据，能支撑的业务模式太少，比如短期的线上活动分析就非常不友好，活动初期需要实时的用户使用数据，而活动结束后，这批数据又无需采集。</p>
<p>那么如何才能在不更新埋点规则的情况下，也能让产品同学能有可供分析的数据呢？我的答案是提供更细颗粒度的埋点数据。</p>
<h3 data-id="heading-1">方案1.0</h3>
<p><a href="https://juejin.cn/post/6932268614863028237" target="_blank" title="https://juejin.cn/post/6932268614863028237">App数据埋点模块设计</a></p>
<p>以我现在的IM项目为例，使用定制埋点代码的方式来上报埋点数据，比如1个小时内用户点击创建群组按钮10次。这类数据可以理解为结果数据，它直观的提供了一个无需分析的数据。</p>
<p>优点是服务端只需对数据进行合并分组，即可呈现到可视化后台，减少了服务端的开发成本，以及分析计算压力。缺点也很明显，由于客户端已经将数据进行了二次处理，造成了数据失真，通过结果无法反推原先用户的操作。比如用户是从首页创建的群组，还是从通讯录创建的群组，此时就需要再增加两个相关入口的埋点，或者修改“创建群组”埋点规则，增加关于来源的数据字段，并且需要等待下次发版后才能生效</p>
<h3 data-id="heading-2">方案2.0</h3>
<p>如果把上报数据从设计具体定制埋点，改变为统计用户的行为，则可以更灵活全面的为产品提供数据。比如从上报1小时内用户点击创建群组的次数，改为分别上报用户进入首页，用户点击创建群组按钮，用户创建了群组等多个埋点。此时产品再想分析用户创建群组的行为，可以让后端开发从埋点数据库中获取数据，再通过分析规则，1个小时内某个用户点击创建群组的次数，同时来源分布比例也可同时分析得出。</p>
<p>这个方案的优点如上述，即增加了数据的完整性，提供了灵活分析数据的可能。但也有些不足，如客户端需要在更短的时间周期内上报数据，势必对网络/系统资源的占用更多。分析埋点数据的计算从客户端集中到了服务端，相当于从分布式计算变成了单机计算，增加对服务端资源使用的压力。</p>
<p>所以目前我选择集合使用两种模式，对需要分析，但规则更新频率较低埋点，仍然采用客户端聚合计算后上传，比如页面停留时长的计算。</p>
<h2 data-id="heading-3">埋点与采集点</h2>
<p>为了更好的规范埋点的使用，先做几个抽象的定义。</p>
<p>埋点类型：</p>
<ol>
<li>事件类型埋点，表示某个事件的发生，也可以通过相同的事件ID来表示一个事件流程。比如用户发送了一张图片，用户从启动到IM登录的过程。</li>
<li>页面类型埋点，表示页面的生命周期。比如用户打开通讯录，用户进入聊天会话。</li>
<li>状态类型埋点，表示某些配置项的状态。比如用户是否开启推送通知，用户是否启用人脸识别。</li>
<li>日常类型埋点，表示在一个时间段内只上报一次的数据。比如用户当日登录。</li>
<li>计次类型埋点，由事件类型衍生而来，将时间段内的埋点聚合起来表示时间段内的发生次数。比如一小时内用户进入聊天会话的次数，一小时内用户发送图片消息的次数。</li>
</ol>
<p>采集点类型：</p>
<ol>
<li>通用型采集点，采集点可以产出多个同类型的埋点数据。比如页面跳转，按钮点击，App生命周期。</li>
<li>定制型采集点，采集点对应特定功能的逻辑。比如在创建群组成功后API的异步回调埋点，用户登录的完整流程埋点。</li>
</ol>
<h2 data-id="heading-4">用户行为统计</h2>
<h3 data-id="heading-5">设计目的</h3>
<p>为通用型采集点提供上下文环境，对用户的行为进行更细致的全量采集，同时采集点的设计尽可能不涉及原有逻辑代码的修改，即目前广泛应用的无埋点模式。</p>
<h3 data-id="heading-6">用户行为链</h3>
<p>每当用户行为触发时，创建用户行为模型加入用户行为链，最终可以形成一条记录用户行为的链表。</p>
<p>用户行为类型：</p>
<ol>
<li>页面跳转类型，比如页面初始化，页面展现，页面消失。</li>
<li>按键点击类型，比如功能按钮点击（发送表情），复用列表点击（从通讯录进入个人详情）。</li>
<li>系统事件类型，比如系统推送，系统截图，系统静音。</li>
</ol>
<h3 data-id="heading-7">采集用户行为</h3>
<p>以iOS为例，使用AOP去Hook页面的生命周期，手势的delegate，复用列表的Delegate，UIApplication的事件处理等，来完成采集点的初步搭建。</p>
<p>这里利用了Objc的Runtime特性，实现进行方法实现替换，如果语言不支持，使用基类继承的方式也能实现，只是成本会大很多。关于delegate的hook需要用到动态类创建，类似于系统框架实现KVO的机制，实现方案不太赘述，推荐<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F349878648" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/349878648" ref="nofollow noopener noreferrer">七步实现列表点击事件的采集</a></p>
<p>基于采集点，提供插件协议，将实现协议的插件注册到用户行为链管理器中，即可在事件触发式得到回调，再根据不同的筛选规则，生成不同的定制埋点。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b26e377fd004b47a18fd6aa322201b9~tplv-k3u1fbpfcp-zoom-1.image" alt="用户行为统计" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">事件标识</h3>
<p>为了通过用户行为链来分析当前用户的行为，需要保证每个事件都有标识符。通过标识符来预设规则，为触发规则的行为创建埋点数据。</p>
<h4 data-id="heading-9">页面跳转类型标识符</h4>
<p>以iOS的UIKit框架提供NavigationController，可以维护页面栈，可以得到从跟页面至当前页面的所有页面数据。</p>
<p>比如从首页（HomePage）先跳转会话详情界面（SessionPage），再跳转联系人详情界面（UserInfoPage），组成了导航路径HomePage -> SessionPage -> UserInfoPage。此时，即可将不同页面的Class作为单页面标识符组合成页面路径使用，如：“HomePage/SessionPage/UserInfoPage”。</p>
<p>如果当前系统框架并没提供类似功能，则需要自己设置一个标识符，或者将当前页面的Class名作为标识符，如"UserInfoPage"。</p>
<p>每当触发页面跳转时，创建一个用户行为模型加入到用户行为链中，如此只需要查询用户行为链即可知道用户的历史页面操作。</p>
<h4 data-id="heading-10">按键点击类型标识符</h4>
<p>按键类型分为两种，一种为单独使用按键，一种为复用列表按键。</p>
<p>单独使用按键可能存在UI控件被复用，按键的响应函数被复用的情况。可以组合按键的Class名、按键的响应函数名、按键所在的页面Class名来描述。</p>
<p>比如在会话详情（SessionPage）点击消息气泡的头像（ImageView），触发了联系人详情界面跳转动作（pushUserInfo）。根据标识符生成规则，可以组成“SessionPage/ImageView/pushUserInfo”的标识符。</p>
<p>复用列表按键用于动态列表中，会同时出现多个相同类型的按钮，在用户刷新或滚动的途中，相同按键的关联数据源可能发生改变，复用列表的响应函数几乎也都是同一个函数。此时在单独使用按键的标识符规则上，去除响应函数名，加入按键的位置信息来重新组成标识符。</p>
<p>比如在首页（HomePage）点击会话列表中第3个会话（SessionListCell），此时可以收集到的信息就只有按键的Class名称，按键所在页面的Class名以及按键的相对位置信息（第0个session，第3个row），可以组合成“HomePage/SessionListCell/0:3”。</p>
<p>如果发生数据源变化的情况，则还需要解析数据源模型，进行定制的埋点操作。</p>
<h4 data-id="heading-11">系统事件类型标识符</h4>
<p>这些事件是通过用户使用了系统功能后触发形成的，比如用户截屏，用户点击推送。可以直接设置默认字符串进行标识。</p>
<h3 data-id="heading-12">用户行为分析</h3>
<p>复杂的埋点规则，通常很难单凭一个用户行为数据做出单独的判断。</p>
<p>比如从首页（HomePage）使用全局搜索界面（GlobalSearchPage）搜索联系人，点击联系人跳转联系人详情界面（UserInfoPage），在联系人详情界面（UserInfoPage）中点击发送消息，进入会话详情界面（SessionPage）。需求是统计会话详情的来源是否为首页的全局搜索界面。</p>
<p>当采集点被触发时，我们需要进行一系列的判断</p>
<ol>
<li>判断距离当前用户行为是否为会话详情界面（SessionPage）的页面跳转。</li>
<li>判断距离当前最近的一次页面跳转事件是否全局搜索界面（GlobalSearchPage）。</li>
<li>判断全局搜索界面（GlobalSearchPage）之前是否来源为首页（HomePage）。</li>
</ol>
<p>注意，用户行为链会记录全量的用户行为，可能会存在重复的用户操作，以及已经被统计过的用户行为并不会从链中移除。</p>
<h5 data-id="heading-13">查询深度</h5>
<p>我们可以根据页面跳转行为作为分界线来给用户行为链分层，设计命中埋点时需要查询的最小深度来规避重复统计。</p>
<p>比如当前用户从首页（HomePage）跳转到全局搜索界面（GlobalSearchPage），又从全局搜索界面（GlobalSearchPage）退回到了首页（HomePage），接着用户去通讯录（ContactPage）等其他页面进行了十几个页面的跳转，最后通过联系人详情界面（UserInfoPage）的路径进入了会话详情界面（SessionPage）。</p>
<p>如果不设计查询深度，则此时仍然能查到链中存在跳转全局搜索界面（GlobalSearchPage）的用户行为记录。单纯判断是否全局搜索界面（GlobalSearchPage）的跳转记录会误判会话详情界面（SessionPage）的来源。如果将查询深度设置为2，则只查询会话详情界面（SessionPage）之前的两次页面跳转（用户详情与全局搜索界面），之前的用户行为记录则可以忽略。</p>
<h3 data-id="heading-14">埋点验证</h3>
<p>为了验证埋点数据的有效性，在开发模式下，每个埋点触发时，都应该打印相关信息到控制台和写入日志文件，再通过脚本验证日志的方式来确保每一步操作的埋点能正确记录。</p>
<h2 data-id="heading-15">参考文档</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Ftech.meituan.com%2F2017%2F03%2F02%2Fmt-mobile-analytics-practice.html" target="_blank" rel="nofollow noopener noreferrer" title="https://tech.meituan.com/2017/03/02/mt-mobile-analytics-practice.html" ref="nofollow noopener noreferrer">美团点评前端无痕埋点实践</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fneyoufan.github.io%2F2017%2F04%2F19%2Fios%2F%25E7%25BD%2591%25E6%2598%2593HubbleData%25E6%2597%25A0%25E5%259F%258B%25E7%2582%25B9SDK%25E5%259C%25A8iOS%25E7%25AB%25AF%25E7%259A%2584%25E8%25AE%25BE%25E8%25AE%25A1%25E4%25B8%258E%25E5%25AE%259E%25E7%258E%25B0%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://neyoufan.github.io/2017/04/19/ios/%E7%BD%91%E6%98%93HubbleData%E6%97%A0%E5%9F%8B%E7%82%B9SDK%E5%9C%A8iOS%E7%AB%AF%E7%9A%84%E8%AE%BE%E8%AE%A1%E4%B8%8E%E5%AE%9E%E7%8E%B0/" ref="nofollow noopener noreferrer">网易HubbleData无埋点SDK在iOS端的设计与实现</a></p></div>  
</div>
            