
---
title: '媒体渠道的_广告投放转化_数据回传API，对接需求怎么写？'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/06/FMZwperET1kXWrAtwRAq.png'
author: 人人都是产品经理
comments: false
date: Thu, 20 Jun 2019 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/06/FMZwperET1kXWrAtwRAq.png'
---

<div>   
<blockquote><p>本文将以某款金融产品对接快手广告平台为例，介绍广告主商业产品经理的入门级需求策划任务——对接广告平台的标准接口，把转化数据准确上报。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-2487084 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/06/FMZwperET1kXWrAtwRAq.png" alt width="800" height="450" referrerpolicy="no-referrer"></p>
<p>一款有强变现能力的产品（比如金融、游戏、电商），免不了在各种媒体渠道投放广告（比如快手、头条、抖音）。而从用户点击广告到下载、注册、登录、付费等一系列关键行为转化的数据统计，一方面关系到广告结费，另一方面也可以分析广告投放效果、及时调整策略缩减成本提升转化率。</p>
<p>但是，媒体方只有用户点击广告的数据，投放广告的广告主也只有自身产品相关的转化数据，要做到整体漏斗的统计分析，就需要整合双方数据，许多广告平台应运而生（比如凤巢、广点通、多彩互动）。广告主商业产品经理的入门级需求策划任务，就是要对接广告平台的标准接口，把转化数据准确上报。</p>
<p>需要注意的是，媒体方和广告主不会共用一套账户体系，如何把一个用户在两端产生的数据匹配到一起就大有文章：</p>
<ol>
<li>首先，手机号是最为准确的匹配字段，如果媒体方和广告主的账号绑定的是同一个手机号，就可以认定这是同一个用户，数据可统一归集。</li>
<li>然而，不是所有的媒体渠道都需要用户注册登录，一些游客也会点击广告带来转化。这时，安卓的IMEI设备号、苹果的IDFA设备号就有了用武之地，即时你没有注册账号，但你手机的设备号总不会变，如果媒体方和广告主采集的行为数据对应的设备号是一致的，那也可匹配上两端的数据。</li>
<li>可是这样也不能100%解决问题，有些用户并不会授权给客户端获取它的设备号，那就压根拿不到他的IMEI和IDFA。不过，我们还有手机的MAC网卡地址、Android下的AndroidID、IP地址等可以用来匹配用户身份的字段。总体来说，IMEI和IDFA的采集率最高，其它匹配方式可作为备选或补充。（其实，IMEI和IDFA之外的字段媒体方也不一定会采集、广告平台接口也不一定会提供）</li>
</ol>
<p>（以某款金融产品对接快手广告平台为例）</p>
<h2 id="toc-1">一、业务概述</h2>
<h3>1.1 背景</h3>
<p>****、***在快手信息流投放缺少转化数据统计分析，转化量及成本有优化空间。</p>
<p>如下表所示，从历史数据来看对接转化数据回传API，收益明显。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/06/uHSuhByba5fZBxpaKdbI.png" alt width="556" height="236" referrerpolicy="no-referrer"></p>
<p>另外，需求实施的前置条件是达标的设备号获取率，经调研已满足要求：</p>
<ol>
<li>快手的IMEI和IDFA获取率95%左右；</li>
<li>APP客户端优化于5月7日上线：V*.*.*版本（****）的IMEI获取率为91.53%，V*.*.*版本（***）的IMEI获取率为91.21%，达到预期要求；</li>
<li>****和***的IDFA抓取率在98%以上。</li>
</ol>
<h3>1.2 目标</h3>
<p>如下表所示，通过本次对接转化数据回传API，实现****、***在快手信息流投放的量级增长、成本降低。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/06/XiSo7XeuCINlqbtxI5oC.png" alt width="559" height="113" referrerpolicy="no-referrer"></p>
<h3><strong>1.3 业务主流程示意图</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/06/dihjh5mz6IfSFemkvMfm.png" alt width="833" height="413" referrerpolicy="no-referrer"></p>
<ol>
<li>快手用户点击快手客户端展示的广告。</li>
<li>快手客户端请求广告平台中设置的监测链接（广告主自行开发或者托管第三方监测平台），通过宏替换的方式把点击数据详细信息实时同步给广告主或者第三方监测平台（具体见接口一）。</li>
<li>广告主或者第三方监测平台接收到快手接口一上报的点击请求后，记录请求参数中的用户信息（例如用户的IDFA-MD5、IMEI-MD5等）和callback信息，后续从产生相关转化的用户中，匹配出由快手推广渠道带来的用户及其转化数据。</li>
<li>广告主或者第三方监测平台将匹配出的转化数据，通过请求相应的callback通知快手效果统计服务器（具体见接口二）。</li>
<li>快手效果统计服务器将接收到的转化信息和广告点击数据匹配，在投放平台报表中披露出对应广告计划-广告组-广告创意的转化数据。</li>
</ol>
<h3><strong>1.4 名词解释</strong></h3>
<p><strong>1.4.1 广告主</strong></p>
<p>本次对接快手API，****、***两款产品流程、需求一致，统称为在快手媒体渠道投放信息流广告的“广告主”。</p>
<p><strong>1.4.2 新增注册</strong></p>
<p>用户手机号本次注册是首次注册，对于同一个手机号****和***是独立分开的，即同一个手机号可以在****和***各新增注册一次。</p>
<p><strong>1.4.3 广告点击</strong></p>
<p>当快手用户点击广告可互动区域时，触发点击事件，该事件被认为是一次有效的广告点击。进入指定落地页后点击内部相关链接等行为，不算作点击。</p>
<p><strong>1.4.4 转化数</strong></p>
<p>快手后台报表中展现的转化数据，时间上以快手服务器收到回调请求的时间为准，量级上以客户实际上报请求数为准。</p>
<h2 id="toc-2">二、API对接流程</h2>
<h3><strong>2.1 流程图</strong></h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/06/5SHQ1ePreyfEkGk2Xo1Q.jpg" alt width="792" height="1208" referrerpolicy="no-referrer"></p>
<p>作为广告主，****、***对接快手API的流程分为<b>记录点击用户的设备号相关信息</b>、<b>新增注册用户判断</b>、<b>获取注册用户的设备号相关信息</b>、<b>设备号匹配</b>、<b>发送注册用户的设备号相关信息</b>5个环节。</p>
<p>需要注意的是，记录点击用户的设备号相关信息对其它4个环节来说是异步的、前置的。</p>
<h3><strong>2.2 流程说明</strong></h3>
<p><strong>2.2.1 记录点击用户的设备号相关信息</strong></p>
<p>1. 快手客户端请求点击监测URL（广告主预先在快手广告平台设置），把用户点击数据详细信息实时通过接口一同步给广告主服务端；</p>
<p>2. 广告主服务端接收到快手接口一上报的点击请求后，记录请求参数中的用户信息，其中包括用户的IDFA-MD5或IMEI-MD5、用户点击广告的AID、CID、DID和DNAME、用户点击广告的时间TS和callback信息；（参数说明如下表）</p>
<p><img data-action="zoom" class="aligncenter" style="color: #666666;" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/06/UVSfI8Wwx5jWiehWUqxh.png" alt width="732" height="328" referrerpolicy="no-referrer"></p>
<p>需要额外说明的是，用户每一次点击行为都会上报，都需要完整记录参数信息；</p>
<p>3. <a href="https://www.example.com/?channel=kuaishou&aid=__AID__&cid=__CID__&did=__DID__&dname=__DNAME__&ts=__TS__&idfaMD5=__IDFA2__&callback=__CALLBACK__">点击监测URL的iOS格式</a></p>
<p><a href="https://www.example.com/?channel=kuaishou&aid=__AID__&cid=__CID__&did=__DID__&dname=__DNAME__&ts=__TS__&imeiMD5=__IMEI2__&callback=__CALLBACK__">点击监测URL的Android格式</a></p>
<p>其中：</p>
<ul>
<li>www.example.com是广告主接收点击上报数据的地址，需服务端给出</li>
<li>channel=kuaishou是广告主自定义用来区分渠道的参数信息，快手上报时原样返回，不做任何修改</li>
<li>channel/aid/cid/did/dname/ts/idfaMD5/imeiMD5/callback这几个参数名称仅作为参考，最终使用的参数名称可由服务端自行设定</li>
<li>__CALLBACK__为必填参数，快手客户端在上报的时候会替换成http形式的地址（已编码一次），广告主在接收到上报数据后，需要保存该地址，当用户在应用内完成注册时，请求该地址来上报转化数据（需要拼接相应参数）。</li>
</ul>
<p>4. 响应要求：响应方式为JSON数据格式，HTTP标准状态码，响应内容不做要求。</p>
<p><strong>2.2.2 新增注册用户判断</strong></p>
<ol>
<li>用户首次登录APP，广告主服务端判断用户是否为新增注册的用户，若用户不是新增注册则流程结束；</li>
<li>若用户本次是新增注册，则广告主服务端获取该用户安装来源的注册渠道号，若获取的注册渠道号不是快手渠道号（****、***的快手渠道号详见附件《快手&**渠道号》），则流程结束；</li>
<li>若获取的注册渠道号是快手渠道号，则流程进入下一环节2.2.3.。</li>
</ol>
<p><strong>2.2.3 获取注册用户的设备号相关信息</strong></p>
<p>经过广告主服务端判断，通过快手信息流渠道下载APP且为新增注册的用户通过筛选。</p>
<p>针对这一部分用户，获取他们的MD5加密后的设备ID、用户注册时间两个字段信息，若获取失败则流程结束，若获取成功则流程进入下一环节2.2.4。</p>
<p>其中：</p>
<ul>
<li>安卓imei双卡手机可能有两个，取默认的一个</li>
<li>iOS下的idfa计算MD5，规则为32位十六进制数字+4位连接符“-”的原文（比如：32ED3EE5-9968-4F25-A015-DE3CFF569568），再计算MD5，再转大写</li>
<li>用户注册时间需为13位毫秒级时间戳</li>
</ul>
<p><strong>2.2.4 设备号匹配</strong></p>
<p>将获取到的注册用户MD5加密设备号与2.2.1.记录的点击用户的MD5加密设备号进行匹配，具体匹配规则为：注册用户的MD5加密设备号存在于点击用户的MD5加密设备号名单中，且最近一次的点击行为发生在注册前7天之内（天数可配置）视为匹配成功，否则为不成功。</p>
<p>若匹配不成功则流程结束，若匹配成功则进入下一环节2.2.5。</p>
<p><strong>2.2.5 发送注册用户的设备号相关信息</strong></p>
<p>1. 发送地址：广告主通过接口一接收的注册前7天内最近一次点击行为的__CALLBACK__替换后的http地址（需要拼接相应参数）；</p>
<p>2. 需要拼接的参数：</p>
<ul>
<li>event_type，事件类型，参数值回传2，含义是转化事件为注册</li>
<li>event_time，事件时间，13位毫秒级时间戳（若请求中携带event_type参数，则必须同时携带event_time参数，否则报错）</li>
<li>callback，接口一接收的__CALLBACK__替换后的http地址中的callback参数（参考下方示例中标红处）</li>
</ul>
<p>3. 回调的请求URL（接口一中__CALLBACK__的对应值，链接地址Decode后再拼接相关参数）<a href="http://ad.partner.gifshow.com/track/activate?event_type=2&event_time=1536045380000&callback=DHAJASALKFyk1uCKBYCyXp-iIDS-uHDd_a5SJ9Dbwkqv46dahahd87TW7hhkJkd">点击查看示例</a>（“callback=”后字段的字符每次都会不同）</p>
<p>4. 响应内容：回调后response里的result=1代表回调请求上报成功。</p>
<h3>2.3 时序说明</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2019/06/lR3xXhr2Jer03q38DFSJ.jpg" alt width="470" height="493" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、其他说明</h2>
<h3>3.1 异常处理</h3>
<p>若接口二响应异常，广告主最多上报3次同一条应用内转化数据；如果发送仍失败，则放弃本次发送，并记录异常日志。</p>
<h3>3.2 异常报警</h3>
<p>广告主上报应用内转化数据到快手广告平台，采用即时策略，如果连续3次同一条应用内转化数据发送失败，就短信或邮件报警提醒到相应人员，每天最多发送一次报警，具体发送名单如下：</p>
<blockquote><p>姓名***，手机号**********，邮箱**********</p></blockquote>
<h3>3.3 数据需求</h3>
<p>需要记录注册转化用户设备号相关信息的发送、响应数据，具体需求字段如下：</p>
<p>Ø channel：渠道</p>
<p>Ø aid：广告组id<br>
Ø cid：广告创意ID</p>
<p>Ø did：广告计划Id</p>
<p>Ø dname：广告计划名称</p>
<p>Ø dt：广告点击事件发生的UTC时间戳</p>
<p>Ø idfaMD5：iOS下的idfa计算MD5</p>
<p>Ø imeiMD5：对15位数字的IMEI进行MD5</p>
<p>Ø event_type：转化事件类型</p>
<p>Ø event_time：转化事件时间</p>
<p>Ø sendNumber：第几次发送（1~3）</p>
<p>Ø sendTime：发送时间</p>
<p>Ø returnCode：返回码</p>
<p>Ø returnTime：返回时间</p>
<h3>3.4 信息资料</h3>
<p><strong>3.4.1 <a href="https://yiqixie.com/d/home/fcAA20a3_jN265xtjzJPmNg4r">快手广告平台转化数据API文档v1.4</a></strong><br>
<strong>3.4.2 快手&**渠道号 </strong></p>
<p> </p>
<p>本文由 @鱼缸外的鱼 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自 Unsplash ，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="2484140" data-author="116368" data-avatar="http://image.woshipm.com/wp-files/2019/06/TGkZeYGrjfOBeAFgg8Ii.png"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            