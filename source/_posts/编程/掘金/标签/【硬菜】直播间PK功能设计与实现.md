
---
title: '【硬菜】直播间PK功能设计与实现'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=6812'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 18:51:34 GMT
thumbnail: 'https://picsum.photos/400/300?random=6812'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>最近刚上线了一个新的直播间PK功能，由于之前旧的PK功能做得有点烂，所以目前的PK功能对公司营收没什么增长，这不我就出手了，进行重构与优化，下面将分享一下我在需求开发过程中的开发思路以及遇到的一些问题。</p>
<h1 data-id="heading-1">PK功能介绍</h1>
<p><strong>1. PK算是一种游戏类功能，中途各种游戏状态不算多，整体也不会很复杂</strong></p>
<p><strong>2. 发起PK的两种方式：</strong></p>
<ul>
<li>随机匹配房间PK</li>
<li>邀请指定房间PK</li>
</ul>
<p><strong>3. PK随机匹配匹配池规则：</strong></p>
<ul>
<li>
<p>由于不同的房间整体金主、打赏实力相差较大，避免让一个千万大哥去打一个小主播的情况，按不同的直播间经济实力分不同的匹配池</p>
</li>
<li>
<p>优先匹配实力相当的房间，如高级别匹配池达到一定等待时间阙值，则进入下一轮较低级的匹配池，以此类推，直至达到匹配超时时间。</p>
</li>
<li>
<p>一定时间内PK匹配过的房间尽量不要继续匹配到，尽量保证每次随机匹配的都是新房间</p>
</li>
<li>
<p>匹配池实时更新，可根据PK小时榜、日榜、周榜、连胜局数更新</p>
</li>
</ul>
<p><strong>4.邀请指定房间PK规则:</strong></p>
<ul>
<li>
<p>不可邀请未开播、不在直播间、未打开接受邀请开关、在玩着其他游戏/其他状态/正在PK的房间...</p>
</li>
<li>
<p>输入房间ID查询房间，默认显示推荐的房间(PK过、查询过、实力相当的)</p>
</li>
<li>
<p>被邀请方可接受、拒绝邀请, 拒绝邀请N次后单位时间内邀请方不可邀请该房间，接受邀请后准备开始PK</p>
</li>
<li>
<p>邀请后出现邀请倒计时，倒计时结束后自动取消，中途也可手动取消邀请</p>
</li>
</ul>
<p><strong>5.PK计分/结算/奖励方式:</strong></p>
<ul>
<li>
<p>PK开始后唤醒指定PK礼物面板，用户在PK房间内送礼增加积分，送特定礼物有积分加成</p>
</li>
<li>
<p>PK结束后进行PK结算，进行相应榜单类统计，直播间公屏等...</p>
</li>
<li>
<p>发放对应PK排行榜单奖励，包括小时榜、日榜、周榜等</p>
</li>
</ul>
<h1 data-id="heading-2">PK需求分析与实现方式</h1>
<p><strong>1. 随机PK匹配池</strong></p>
<ul>
<li>[需求分析]</li>
</ul>
<p>房间有几百万个，撑死活跃且玩PK的不会超过五十万，将匹配池分成5个，低层级匹配池明显人数会比高层级多很多，所以要注意低层级匹配池的容量问题以及高层级的随机性。</p>
<ul>
<li>[实现方式]</li>
</ul>
<p>随机队列，客户端通过长连接请求匹配时，先入队，记录开始匹配时间，服务端开一个常驻线程去随机从相同队列中取两个房间出来，其过程中注意下并发问题，如匹配不成功或同一队列中没有可匹配的对手重新塞入队列等待，等待时间超过一定阙值时，出队，进入下一级队列。</p>
<p><strong>2. 指定PK邀请</strong></p>
<ul>
<li>[需求分析]</li>
</ul>
<p>邀请指定房间PK时，点击邀请后判断房间当前状态是否能邀请、对方房间是否需要邀请，这些都是需要服务端去兜底，邀请过期后点击接受提示已过期，点击拒绝记录5分钟拒绝次数，超过三次出现reject all弹窗，点击自动关闭邀请开关，弹窗引导打开开关提示，邀请中可取消邀请，未取消邀请前只能邀请一人，邀请、匹配中不可接受他人邀请。</p>
<ul>
<li>[实现方式]</li>
</ul>
<p>邀请后下发一个广播给对方房间，此时要注意要注意邀请过期，以及重复邀请的问题，邀请倒计时，开多几个常驻线程，因为这个倒计时的状态切换和轮询会比较频繁，邀请操作使用分布式锁锁住被邀请房间，因为一但邀请后被邀请房间无法再被其他房间邀请，同时自己点击邀请的时候也得锁住自己房间，过期、取消、对方拒绝时解锁，锁的过期时间设置成和邀请倒计时一样的时间即可，这样一但发生异常也不至于一直死锁。</p>
<p><strong>3. PK开始前</strong></p>
<ul>
<li>[需求分析]</li>
</ul>
<p>PK匹配/接受PK邀请后双方准备进入PK状态，此时客户端有个PK开始前倒计时动画要播放，同时需要拉取双方房间最近的战绩、信息显示在对方的房间内，要注意客户端播放PK倒计时动画有可能会卡顿，造成一定延迟，播放动画时间为5S左右，此时服务端需要在5S内做好PK就绪工作。</p>
<ul>
<li>[实现方式]</li>
</ul>
<p>进入PK后不能马上切换为游戏中状态，如果切换成游戏中状态此时送礼统计也会计分，加多一个PK开始前准备就绪的状态，先预准备双方房间信息，再开两个延迟线程，5S后切换成游戏中状态，并广播同步给双方房间，防止客户端卡顿在5S后未自动进入。</p>
<p><strong>4. PK中</strong></p>
<ul>
<li>[需求分析]</li>
</ul>
<p>PK期间可能会有人陆续进房/离开，所以房间内的PK信息得定时同步，不能完全依赖客户端维持状态，PK期间房主不可关闭退出PK按钮，但是是不能阻止房主退出房间的，一但房主退出房间，那等于整个直播间都关了，PK得自动终止。</p>
<ul>
<li>[实现方式]</li>
</ul>
<p>进入PK后不能马上切换为游戏中状态，如果切换成游戏中状态此时送礼统计也会计分，加多一个PK开始前准备就绪的状态，先预准备双方房间信息，再开两个延迟线程，5S后切换成游戏中状态，并广播同步给双方房间，防止客户端卡顿在5S后未自动进入。</p>
<p><strong>5. PK期间送礼</strong></p>
<ul>
<li>[需求分析]</li>
</ul>
<p>PK开始时，可对房间进行送礼，送礼后双方进度条都要有变化，要注意的是送礼时间点的把握，因为送礼事件是异步处理，有大量并发时会有延迟，所以统计时得根据送出礼物的时间去统计，
别根据执行时间去统计，这里又有个问题，当你送礼事件执行的时候可能PK已经结束了，所以不能根据PK状态去判断，得根据时间+房间ID去判断是否是PK过程中送的礼物。</p>
<ul>
<li>[实现方式]</li>
</ul>
<p>PK中时先预设置PK开始、结束时间，送礼的时候根据礼物送出时间是否在开始、结束范围内，并且没有中途取消/异常中断操作的时候进行统计即可。进度条在PK分数改变后广播通知一下双方房间即可，同时也需要采用轮询的方式去同步进度条，防止中途出什么幺蛾子。</p>
<p><strong>6. PK结束后</strong></p>
<ul>
<li>[需求分析]</li>
</ul>
<p>PK结束后需要播报PK结果公屏、同时重置PK游戏状态，统计PK结果，记录PK相关埋点、消耗数据等。</p>
<ul>
<li>[实现方式]</li>
</ul>
<p>PK结束操作在准备PK开始预准备数据时，这个时候我们已经设了一个预期的结束时间，我们这时再增加一个延迟队列，就是到这个预期结束时间开始执行PK结束的操作，当然执行前得判断是否已经被异常结束，
结束后将PK整场的数据、消耗该加埋点的加、该入库的入库，毕竟这个运营同学还是比较关心这PK的消耗数据。</p>
<h1 data-id="heading-3">总结与复盘</h1>
<ul>
<li>
<p>[问题1] - PK功能整体依赖Redis比较多，整体QPS很高</p>
</li>
<li>
<p>[ 解决方案] - 考虑增加一层JVM缓存，降低Redis整体的性能开销</p>
</li>
</ul>
<br>
<ul>
<li>
<p>[问题2] - PK出现异常的情况下，自动恢复速度较慢，有时界面会卡住不动</p>
</li>
<li>
<p>[解决方案] - 目前是采用轮询检测的方式恢复，整体轮询数据量大，降低轮询时间也不是好选择，可考虑与客户端共同检测降低服务端轮询开销，优化检测算法。</p>
</li>
<li>
<p>[问题3] - PK匹配池问题</p>
</li>
<li>
<p>[解决方案] - 目前只有5个匹配池，整体匹配规则比较单调，后续会根据兴趣爱好、类目、胜率等推荐算法匹配更加合适、公平的PK对手</p>
</li>
</ul></div>  
</div>
            