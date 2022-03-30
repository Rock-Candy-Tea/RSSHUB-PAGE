
---
title: 'PRD：腾讯会议产品需求文档'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/ozHmlYzbbdugCCbPKZo6.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 23 Feb 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/ozHmlYzbbdugCCbPKZo6.jpg'
---

<div>   
<blockquote><p>编辑导语：如今随着科技的不断发展，人们工作的模式也有了创新，比如腾讯会议就能实现远程开会沟通满足大多会议需求，并且去年疫情也有不少学校使用腾讯会议开启网课模式；本文作者分享了关于腾讯会议的产品需求文档，我们一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-4385147" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/ozHmlYzbbdugCCbPKZo6.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>腾讯会议是在疫情之后崛起的一款云会议协作app，给人们带来了极大的便利。</p>
<p>本人是一名大三在校生，对产品知识颇感兴趣，并且日后想从事有关产品方面的工作；借此机会研究了这款app，并借鉴各位前辈的经验输出了这份腾讯会议的PRD文档，第一次写，还请各位大佬多多指正~</p>
<h2 id="toc-1">一、文档概述</h2>
<h3>1. 版本修订记录</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/DOWX4uSnoVfbxDuN13ls.png" alt width="548" height="163" referrerpolicy="no-referrer"></p>
<h3>2. 输出环境</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/RBcKzjNKid0ZD29KHgSn.png" alt width="584" height="227" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、产品概述</h2>
<h3>1. 产品介绍</h3>
<p>腾讯会议是深圳市腾讯计算机系统有限公司在2019年年底推出的一款远程云会议写作平台，用户可通过小程序、电脑端、App、电话拨入等形式参与会议。</p>
<h3>2. 产品定位</h3>
<p>腾讯会议是一款高清流畅、便捷易用、安全可靠的云视频会议产品，让用户随时随地高效开会，全方位满足不同场景下用户的沟通和会议需求。</p>
<h3>3. 产品特点</h3>
<p>会议支持一键预约、发起、加入会议、在线文档协作，快速激活讨论、实时屏幕共享，并且拥有强大的会管会控，主持人有序管理会议，另外画质高清、视频可美颜、背景可虚化、智能消除环境声、键盘声，完美还原人声。</p>
<h2 id="toc-3">三、需求分析</h2>
<h3>1. 市场需求分析</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/bfTH7VvFkctSfWVLHP8n.png" alt width="693" height="428" referrerpolicy="no-referrer"></p>
<p>iiMedia Research(艾媒咨询)数据显示，中国智能移动办公市场规模持续稳步增长，2019年中国智能移动办公市场规模达到288亿元，预计2020年将达到449亿元，增长率为55.9%。</p>
<p>艾媒咨询分析师认为，疫情催化在线办公市场爆发，随着在线办公需求增长及用户习惯养成，智能移动办公市场将更快速发展；由此可见，目前云视频平台流量正呈爆发性增长，市场需求较旺盛。</p>
<h3>2. 用户需求分析</h3>
<p>1）用户画像</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/9LUMVoSGomwzd1t1uRAF.png" alt width="1211" height="525" referrerpolicy="no-referrer"></p>
<p>从百度指数中的地域分布图来看，竞品钉钉的用户主要分布在广东、北京、上海等经济较发达地区，用户对移动协作办公的接受能力和接受程度相对较高；由此可知，可推测在经济较发达的地区对线上会议的需求较高。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/cHdqZv8ZIXil561I56Uh.png" alt width="1215" height="403" referrerpolicy="no-referrer"></p>
<p>从百度指数中的人群分布图中可看出，竞品使用人群大部分集中在20-29岁的年轻一族，其中一部分主要是大学生，在疫情期间多数需要在线上上课；另一部分主要是在事业上升期的上班族，在疫情期间，推迟复工的同时也伴随着线上远程工作的出现，即使复工复产也仍然伴随着无接触的远程办公；而腾讯会议的出现会极大满足了大学生线上课程以及上班族远程办公的需求。</p>
<p>从性别方面来看，使用线上会议的男性用户远高于女性，主要原因可能是在互联网工作的男性居多，而互联网公司对线上会议的接受程度较高，使用频率也会较高。</p>
<h3>3. 需求总结</h3>
<p>据上述数据可得知，腾讯会议的目标用户群体主要可以分为较发达地区的年轻用户。</p>
<p>目标用户主要可分为三类：有远程办公需要的企业或者组织、需要进行线上课程的师生、需要多人同时交流的线上活动。</p>
<h3>4. 用户场景需求分析</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/fCn8zQ803nRI6noPcLj8.png" alt width="1318" height="808" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、产品结构</h2>
<h3>1. 产品结构图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/sT5IUwsHGHUYE6rjGtV8.png" alt width="2191" height="3765" referrerpolicy="no-referrer"></p>
<h3>2. 产品功能结构图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/b0CFmPVP6XjpvGyXGRlE.png" alt width="2110" height="4328" referrerpolicy="no-referrer"></p>
<h3>3. 产品信息结构图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/NGuwalfPtOpDKj2ZdwoQ.png" alt width="1400" height="4095" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、全局说明</h2>
<h3>1. 功能权限</h3>
<p>未登录状态：验证手机号可加入会议室，享受免费版的功能。</p>
<p>登录状态：登录用户可使用app内所有功能；疫情期间，普通用户开放了最高可容纳300人和单次会议时长长达9999分钟的会议室；正常版本，个人版可享受限时45分钟的多人群组会议，参会者最高可达25人；专业版不限会议时长，参会者最高可达100人。</p>
<h3> 2. 键盘交互说明</h3>
<p>点击手机号、验证码、会议号、密码输入框，页面底部会弹出数字键盘。</p>
<p>其他输入框，页面底部则弹出拼音键盘。</p>
<h3>3. 页面交互</h3>
<p>1）基本页面交互说明</p>
<ul>
<li>点击个人中心、加入会议、快速会议、预定会议、历史会议等，进入下一页面时均像左滑出。</li>
<li>进入会议时，页面从底端向上滑入，结束会议时，页面向下滑出。</li>
</ul>
<p>2）弹窗说明</p>
<p>悬浮窗：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/aR67ymlSeuqFJ1m9jdxs.png" alt width="610" height="523" referrerpolicy="no-referrer"></p>
<p>对话框：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/Sy5hwXqowISV8Y54GAXO.png" alt width="607" height="523" referrerpolicy="no-referrer"></p>
<p>功能框：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/mVsx2DtGgVeOToogGqd5.png" alt width="608" height="512" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/tMBZNAQsR9Kdtmc61Uye.png" alt width="622" height="517" referrerpolicy="no-referrer"></p>
<p>3）页面异常</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/9eWs7OHZIGhF0mzBGLuU.png" alt width="592" height="424" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/0tiC1TwfLY0pHhmHsDJi.png" alt width="628" height="470" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/MxHLLtBvkPnRU4kc1Xzh.png" alt width="613" height="482" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/k97mDHHTiVxgspasNv3Y.png" alt width="619" height="505" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/seQaDJ1AemhMwO5a8189.png" alt width="584" height="525" referrerpolicy="no-referrer"></p>
<p>4）页面切换</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/BmDnD2ckOu0irdhuYjk9.png" alt width="770" height="394" referrerpolicy="no-referrer"></p>
<p>5）会议情景页面</p>
<p>语音模式：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/zbzbchACMFTjOwK8hlzt.png" alt width="544" height="541" referrerpolicy="no-referrer"></p>
<p>视频模式：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/7ZhxhNwklFu26DOkhArN.png" alt width="516" height="504" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/ECMFODEqViuaDaNNIyNN.png" alt width="280" height="469" referrerpolicy="no-referrer"></p>
<p>共享屏幕模式：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/O9EeiG3YZnecvBaEYWWu.png" alt width="427" height="425" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/ORokgA0i1a5NFeHUeDu2.png" alt width="469" height="443" referrerpolicy="no-referrer"></p>
<p>聊天模式：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/TIEXPVyWfA7xPEE9HTN7.png" alt width="425" height="426" referrerpolicy="no-referrer"></p>
<h2 id="toc-6">六、部分业务流程图</h2>
<h3>1. 登录/注册流程</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/uzWjvcMwHt9mJcyCdLJR.png" alt width="2151" height="1377" referrerpolicy="no-referrer"></p>
<h3>2. 加入会议流程</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/2vePv2Qgwil6HmbuAz4V.png" alt width="1038" height="1316" referrerpolicy="no-referrer"></p>
<h3>3. 预定会议流程</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/nhPDvaicQRYBxXSNHEGm.png" alt width="595" height="857" referrerpolicy="no-referrer"></p>
<h2 id="toc-7">七、页面逻辑图</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/tfAcFhdxYAGHmg5tnyOq.png" alt width="1097" height="599" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/wWdNK6tTa6Y5dO6Ktlt3.png" alt width="909" height="637" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/qo8OKEy3kdwr7nikAj2t.png" alt width="668" height="626" referrerpolicy="no-referrer"></p>
<h2 id="toc-8">八、核心功能说明</h2>
<h3>1. 登录/注册</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/3Z4Lt2pzLLtZwx9l7zjt.png" alt width="3863" height="1977" referrerpolicy="no-referrer"></p>
<p>1）页面名称：登录/注册页面</p>
<p>2）页面入口：打开app时</p>
<p>3）页面逻辑说明：</p>
<ul>
<li>企业微信登录：在登录页点击“企业微信”选项，跳转到企业微信，若你当前所在企业已开通该应用权限则授权登录，否则显示“无添加应用权限”，无法登录。</li>
<li>微信登录：在登录页点击“微信”选项，首次登录需要验证手机号码，输入手机号，继续点击“获取验证码”，系统判断手机号码是否合法，不合法则提示“请输入正确的手机号”，合法则系统会发送验证码至填写的手机号，然后输入验证码，系统判断验证码是否正确，不正确则提示“请重新输入验证码”，正确则进入首页；若非首次登录则会跳转微信页面授权登录。</li>
<li>SSO登录：在登录页点击“SSO登录”选项，输入企业域名，系统判断是否合法，不合法给予提示，满足条件则可登录至首页；点击“我不知道企业域名”选项，输入企业邮箱，系统判断是否合法，不合法则给予提示，满足条件即可登录至首页。</li>
<li>验证码登录：点击“注册/登录”选项，输入手机号，点击“获取验证码”，系统判断手机号码是否合法，不合法则提示“请输入正确的手机号”，合法则系统会发送验证码到你的手机，然后输入验证码，系统判断验证码是否正确，不正确则提示“请重新输入验证码”，正确则进入首页。</li>
<li>帐号密码登录：点击“注册/登录”选项，点击“使用帐号密码登录”选项，输入手机号及密码，点击“登录”，系统将判断手机号码是否合法和注册以及密码是否匹配正确；若满足条件则登录成功进入首页，点击“忘记密码”，系统会自动发送验证码到填写的手机号，验证码匹配成功后可重置密码，密码符合要求则可进入首页。</li>
<li>新用户注册：点击“注册/登录”选项，点击“新用户注册”选项，输入手机号，点击“获取验证码”，系统判断手机号码是否合法，不合法则提示“请输入正确的手机号”，合法则系统会发送验证码至填写的手机号，然后输入验证码，系统判断验证码是否正确，不正确则提示“请重新输入验证码”，验证码匹配正确后可进入首页，点击“登录”选项，系统判断手机号是否合法、是否注册以及密码是否正确。满足条件后，填写会议姓名及密码，完成后可进入首页。</li>
</ul>
<p>4）页面交互说明：点击各个功能选项，右侧滑出进入子页面，同时在各子页面往左侧滑动可返回到上一页面（也可点击返回键）。</p>
<h3>2. 首页及个人信息</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/W0gV5N1xdnZtXVSh6HkD.png" alt width="1528" height="1014" referrerpolicy="no-referrer"></p>
<p>1）页面名称：首页和个人信息页</p>
<p>2）页面入口：登录成功后即可进入首页，个人信息点击首页头像进入</p>
<p>3）页面逻辑说明：</p>
<ul>
<li>个人中心：点击首页头像进入个人中心，个人中心可显示个人会议号、单次会议时长、会议人数上限、云存储录制空间、手机号、微信、版本号等信息；可进行升级空间、更换会议号、绑定邮箱、修改密码、进行一系列设置、吐槽、进入帮助中心、退出登录等操作。</li>
<li>个人资料：在“个人中心”页面点击头像进入个人资料，可更换头像、修改名称和注销账号。</li>
</ul>
<p>4）页面交互说明：点击各个功能选项，右侧滑出进入子页面，同时在各子页面往左侧滑动可返回到上一页面（也可点击返回键）。</p>
<h3>3. 加入会议</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/PEWeGjsBmkQyXgf9TIIl.png" alt width="1689" height="2092" referrerpolicy="no-referrer"></p>
<p>1）页面名称：加入会议页面</p>
<p>2）页面入口：首页直接点击“加入会议”进入或通过微信复制会议号和点击链接进入</p>
<p>3）页面逻辑说明：</p>
<ul>
<li>会议号加入会议：在首页点击“加入会议”选项，进入加入会议界面，输入会议号和与会者姓名，点击“加入会议”按钮，系统判断会议号是否有效，无效则提示“会议号无效”，有效则进入会议室。</li>
<li>邀请链接加入会议：在微信或其他地方点击与会成员发送的会议链接，进入邀请链接界面，点击“加入会议”按钮，则跳转到腾讯会议app进入会议室。</li>
</ul>
<p>4）页面交互说明：点击各个功能选项，右侧滑出进入子页面，同时在各子页面往左侧滑动可返回到上一页面（也可点击返回键），在其他软件点击会议邀请链接可自动唤起并选择跳转到腾讯会议app。</p>
<h3>4. 快速会议</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/qJDrfkSjAUru6ENys8HY.png" alt width="1614" height="1036" referrerpolicy="no-referrer"></p>
<p>1）页面名称：快速会议页面。</p>
<p>2）页面入口：首页点击“快速会议”选项进入。</p>
<p>3）页面逻辑说明：首页直接点击“快速会议”进入快速会议设置页面，可选择是否开启视频和使用个人会议号，点击进入会议即可进入会议室。</p>
<p>4）页面交互说明：点击各个功能选项，右侧滑出进入子页面，同时在各子页面往左侧滑动可返回到上一页面（也可点击返回键）。</p>
<h3>5. 预定会议</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/o2mLuYF7mQzqt9df6gh6.png" alt width="2470" height="2062" referrerpolicy="no-referrer"></p>
<p>1）页面名称：预定会议页面。</p>
<p>2）页面入口：首页点击“预定会议”选项进入。</p>
<p>3）页面逻辑说明：首页直接点击“预定会议”进入预定会议类型设置页面，可选择预定常规会议或者特邀会议；预定常规会议，可选择会议的起止时间，是否定为周期性会议，设置入会密码、上传文档等等；点击完成后可新建日程，预定会议成功后跳转首页显示会议基本信息。预定特邀会议，先填写会议信息，生成会议邀请链接，点击“邀请微信好友”选项可自动跳转至微信并选择发送给好友。</p>
<p>4）页面交互说明：点击各个功能选项，右侧滑出进入子页面，同时在各子页面往左侧滑动可返回到上一页面（也可点击返回键），日期时间选择由底部弹出日期选项页面，点击“邀请微信好友”可自动唤起微信。</p>
<h3>6. 历史会议</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/5oQ0EadRyyH398VCONP8.png" alt width="1972" height="1022" referrerpolicy="no-referrer"></p>
<p>1）页面名称：历史会议页面。</p>
<p>2）页面入口：首页点击“历史会议”选项进入。</p>
<p>3）页面逻辑说明：首页直接点击“历史会议”选项进入近期历史会议，显示其会议名称、会议号以及会议时间和发起人等。点击右上方“管理”选项可选择删除指定历史会议或清除全部会议；点击其中的某个历史会议可进入历史会议详情，显示历史会议的详细信息，创建者还可在此导出参会成员名单，若会议未过期还可重新入会。</p>
<p>4）页面交互说明：点击各个功能选项，右侧滑出进入子页面，同时在各子页面往左侧滑动可返回到上一页面（也可点击返回键）。</p>
<h3>7. 会议中（主持人）</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/Ev7GMKOhLm44rG70Noy2.png" alt width="3251" height="2964" referrerpolicy="no-referrer"></p>
<p>1）页面名称：会议中-主持人页面</p>
<p>2）页面入口：通过“加入会议”选项或邀请链接直接进入</p>
<p>3）页面逻辑说明</p>
<p>管理成员：</p>
<ul>
<li>点击会议室首页的“管理成员”选项，出现“管理人员”弹窗，可选择全体静音、解除全体静音或邀请其他成员进入会议。</li>
<li>点击与会成员，可查看与会成员的姓名、身份和头像。并且可进行解除静音、私聊、改名、设为（撤销）联席主持人、设为（收回）主持人、移至等候室等操作。</li>
<li>当指定某位成员为联席主持人时，联席主持人可进行静音/解除静音、私聊、改名、移至会议室等操作，但是不能指定其他人会联席主持人，也无法将主持人身份移交他人，主持人可随时撤销联席主持人；当指定某位成员为主持人时。若该成员为会议创建者，可随时收回主持人身份。</li>
<li>在会议开始前将某位与会成员移至等候室，成员将在等候室等待。还可将无关人员移出会议室并选择不再让此成员进入会议。</li>
</ul>
<p>聊天：点击会议室首页的“更多”选项，点击“聊天”，弹出聊天界面，可将信息发送给所有人或者指定成员，也可在管理成员页面点击某位与会成员进行私聊，在会议室主界面也可点击表情和聊天直接将信息发送在主界面显示。</p>
<p>屏幕/白板共享：点击会议室首页的“共享屏幕”选项，用户可选择共享自己的屏幕或者共享白板输出内容，不受硬件条件限制。</p>
<p>云录制：点击会议主界面的“更多”选项，选择“云录制”，即可开始录制会议内容，录制会议将在会议结束后通过消息中心发送于录制人员。</p>
<p>会议设置：在会议室首页点击“管理成员”选项，进入管理成员页面，点击左上角的设置，可进行如下操作：</p>
<ul>
<li>是否允许成员自我解除静音；（允许则与会成员可自行解除静音，否则无法解除）</li>
<li>是否允许发送红包。</li>
<li>是否锁定会议（锁定后新成员将无法加入）</li>
<li>是否开启等候室（开启后可在会议开始前将与会成员移至等候室）</li>
<li>是否隐藏会议号和密码</li>
<li>是否仅主持人可共享（开启后其他与会成员将无法共享屏幕）</li>
<li>聊天设置（允许自由聊天、允许公开聊天、允许私聊主持人、全体成员禁言）</li>
<li>录制设置（仅主持人可录制、全体成员可录制、允许部分成员录制）</li>
<li>成员进入时是否播放提示音</li>
<li>成员入会时是否静音（开启、关闭、超过6人后自动开启）</li>
<li>导出参会成员（跳转至新链接可导出参会成员文件）</li>
</ul>
<p>结束会议：在会议室首页点击右上角的“结束”选项。</p>
<ul>
<li>离开会议：离开会议后可重新通过会议号或者邀请链接进入会议。但需要指定新的主持人，否则系统将随机指定一名成员为主持人。</li>
<li>结束会议：所有参会成员将退出会议。</li>
</ul>
<p>4）页面交互说明</p>
<ul>
<li>会议室主界面点击“管理成员”选项，弹窗上滑进入管理成员页面，下滑将返回上一页面。点击与会成员，向下弹出对话框（点击空白处或对话框关闭选项关闭）；</li>
<li>管理成员页面点击“会议设置”选项，右侧滑入会议设置页面（左滑返回上一页面，也可点击返回键）；其他子页面也均由向右滑入，退出均向左往右滑出，或点击返回键。</li>
<li>会议室主界面点击“结束”、“共享屏幕”选项底部弹出Actionbar。其他弹窗也均由底部弹出，退出均点击空白处或者取消。</li>
<li>会议室主界面点击“表情”、“发送信息”、“更多”选项则弹出气泡窗。</li>
</ul>
<h3>8. 会议中（与会成员）</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/OW0KufwE8JwrvAdIlp72.png" alt width="2976" height="2045" referrerpolicy="no-referrer"></p>
<p>1）页面名称：会议中-与会成员页面</p>
<p>2）页面入口：通过“加入会议”选项或邀请链接直接进入</p>
<p>3）页面逻辑说明</p>
<p>成员：</p>
<ul>
<li>在会议室主界面点击“成员”选项，出现与会成员界面，可选择解除静音或邀请其他成员加入会议。</li>
<li>点击与会成员，可查看与会成员的姓名、身份和头像，还可进行私聊、举报等操作。</li>
</ul>
<p>聊天：点击会议室首页的“更多”选项，点击“聊天”，弹出聊天界面，可将信息发送给所有人或者指定成员。也可在成员页面点击某位与会成员进行私聊。在会议室主界面也可点击表情和聊天直接将信息发送在主界面显示。</p>
<p>屏幕/白板共享：点击会议室首页的“共享屏幕”选项，用户可选择共享自己的屏幕或者共享白板输出内容，不受硬件条件限制。</p>
<p>离开会议：在会议室首页点击右上角的“离开”选项。离开会议后将退出，但可重新通过会议号或者邀请链接进入会议。</p>
<p>4）页面交互说明</p>
<ul>
<li>会议室主界面点击“成员”选项，弹窗上滑进入成员页面，下滑将返回上一页面。点击与会成员，向下弹出对话框（点击空白处或对话框关闭选项关闭）；</li>
<li>会议室主界面点击“离开”、“共享屏幕”选项底部弹出Actionbar。其他弹窗也均由底部弹出，退出均点击空白处或者取消。</li>
<li>会议室主界面点击“表情”、“发送信息”、“更多”选项则弹出气泡窗。</li>
</ul>
<h2 id="toc-9">九、总结</h2>
<p>腾讯会议是一款便捷易用、安全可靠的云视频会议产品，满足了用户随时随地高效开会的会议需求，尤其是在会议期间，满足了广大高校以及各大企业的线上会议需求，这也是腾讯会议崛起的重要基础。</p>
<p>随着产品不断更新迭代，腾讯会议的功能也不断得到扩展，其中也有几个功能是该app的亮点：</p>
<ul>
<li>云录制功能：会议过程中，参会人员可能来不及记录重要信息，或者有些参会成员来不及/无法参会，该录制功能可将整场会议录制下来，方便有需要的用户回看会议内容，增强了用户的体验感。</li>
<li>导出参会人员：会议结束后，会议管理员（主持人）在考勤此次参会人员时可直接导出参会人员文档，方便考勤记录。</li>
<li>文档：用户可上传会议文档，方便与会成员浏览。也可在会议中进行新建文档、新建会议纪要对会议主要内容进行记录等操作；各参会成员可以通过文档共享完成信息的收集、更新和分发。</li>
<li>聊天：参会人员在管理员默许的情况下可以自由发送文字弹幕和表情，或者打开聊天弹窗与大家进行交流互动，也支持私聊某位参会人员；在聊天框还支持发送图片、红包，可增强参会者的交流。</li>
</ul>
<p>目前是正在学习产品知识的小白~写的不好的地方还望各位前辈指正，小辈万分感谢~~</p>
<p> </p>
<p>本文由 @吱吱钰 原创发布于人人都是产品经理，未经作者许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4384852" data-author="1203097" data-avatar="https://static.woshipm.com/APP_U_202201_20220104092633_951.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">1人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602183019_3103.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            