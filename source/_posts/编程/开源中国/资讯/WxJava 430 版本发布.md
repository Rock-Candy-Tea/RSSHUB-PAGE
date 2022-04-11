
---
title: 'WxJava 4.3.0 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4389'
author: 开源中国
comments: false
date: Sun, 10 Apr 2022 23:38:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4389'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#24292f; text-align:start">本次正式版本更新，主要是企业微信模块丰富了不少接口，包括会话存档、微信客服等功能接口；小程序模块则完善了不少接口参数的支持和增加一些新的接口支持；公众号模块则主要是修复完善了已有的部分接口；微信支付模块则主要是 增加微信消费者投诉2.0接口；开放平台则主要针对小程序增加了相关接口支持。具体更新日志如下：</p> 
<h2 style="text-align:start">企业微信</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fissues%2F1596" target="_blank">#1596</a><span> </span>新增会话存档相关接口</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fissues%2F2309" target="_blank">#2309</a><span> </span>新增微信客服-接待人员管理、会话分配与消息收发、基础信息获取、帐号管理等部分接口</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2372" target="_blank">#2372</a><span> </span>新增客户群opengid转换和入群欢迎语素材管理相关接口</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2382" target="_blank">#2382</a><span> </span>增加获取商品图册的接口</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2387" target="_blank">#2387</a><span> </span>客户朋友圈接口字段调整</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2391" target="_blank">#2391</a><span> </span>企业群发消息接口结构调整</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2397" target="_blank">#2397</a><span> </span>帐号ID安全性全面升级相关接口改造以及增加代开发应用external_userid转换的接口</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2423" target="_blank">#2423</a><span> </span>新增企业微信 Spring Boot Starter</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2428" target="_blank">#2428</a><span> </span>用户管理接口添加官方新引入的直属领导字段</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2452" target="_blank">#2452</a><span> </span>获取部门列表接口添加返回字段 departmentLeader（部门负责人的UserID）</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2468" target="_blank">#2468</a><span> </span>获取审批申请详情接口返回数据增加关联审批单控件</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2479" target="_blank">#2479</a><span> </span>增加获取企业群发成员执行结果的接口</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2481" target="_blank">#2481</a><span> </span>发送应用消息接口里的文本通知型的模板卡片消息增加引用文本字段</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fissues%2F2518" target="_blank">#2518</a><span> </span>获取审批记录的审批状态增加已退回状态</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fissues%2F2537" target="_blank">#2537</a><span> </span>部门管理增加获取子部门ID列表和获取单个部门详情的接口</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fissues%2F2563" target="_blank">#2563</a><span> </span>优化获取待分配离职成员列表的接口，增加分页查询游标参数</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fissues%2F2579" target="_blank">#2579</a><span> </span>增加企业微信OA自建应用-审批流程引擎相关接口</li> 
 <li>修改解析企业微信推送消息类，添加对企微客户联系变更回调事件的支持</li> 
 <li>增加支持URL的素材文件上传接口</li> 
 <li>增加直播相关接口</li> 
 <li>增加获取企业假期管理配置的接口</li> 
 <li>配置类增加会话存档路径设置</li> 
 <li>重构规范化模板卡片消息部分字段命名，并补充card_image的支持</li> 
</ul> 
<h2 style="text-align:start">公众号</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fissues%2F2411" target="_blank">#2411</a><span> </span>获取草稿列表接口新增两个字段</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2434" target="_blank">#2434</a><span> </span>微信发布能力接口文章信息返回数据增加thumb_url</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2476" target="_blank">#2476</a><span> </span>客服消息增加草稿箱图文消息类型</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2511" target="_blank">#2511</a><span> </span>草稿箱获取图文素材实体类增加图文消息素材的最后更新时间字段</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fissues%2F2516" target="_blank">#2516</a><span> </span>菜单按钮支持新的图文消息类型</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2544" target="_blank">#2544</a><span> </span>修复菜单文章id未序列化问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fissues%2F2553" target="_blank">#2553</a><span> </span>修复草稿相关接口返回值多双引号的问题</li> 
 <li>发布状态轮询接口实体类序列化</li> 
 <li>发布能力获取成功发布列表接口返回增加update_time参数</li> 
</ul> 
<h2 style="text-align:start">小程序</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fissues%2F2198" target="_blank">#2198</a><span> </span>增加根据提交信息数据获取用户安全等级的接口</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fissues%2F2373" target="_blank">#2373</a><span> </span>urllink生成接口增加env_version参数以支持环境隔离</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2375" target="_blank">#2375</a><span> </span>urlscheme生成接口调整请求参数结构</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fissues%2F2386" target="_blank">#2386</a><span> </span>createWxaCodeUnlimit 接口方法支持设置env_string</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2399" target="_blank">#2399</a><span> </span>增加内容安全mediaCheckAsync接口新的实现方法</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2451" target="_blank">#2451</a><span> </span>增加设备订阅消息相关接口</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fissues%2F2455" target="_blank">#2455</a><span> </span>增加新的获取手机号的接口</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2459" target="_blank">#2459</a><span> </span>授权资料变更事件消息增加OpenPID，PluginID，OpenID，RevokeInfo等字段</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2461" target="_blank">#2461</a><span> </span>自定义交易组件上传接口支持图片链接</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2473" target="_blank">#2473</a><span> </span>接入小程序广告实现，实现创建数据源和回传数据两个接口</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2474" target="_blank">#2474</a><span> </span>createWxaCodeUnlimit 接口方法支持设置check_path参数</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2477" target="_blank">#2477</a><span> </span>增加订阅消息通知事件的相关属性支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fissues%2F2491" target="_blank">#2491</a><span> </span>获取小程序scheme码接口请求增加两个过期相关参数</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2506" target="_blank">#2506</a><span> </span>补充完善获取用户encryptKey接口的参数</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2510" target="_blank">#2510</a><span> </span>增加微信小程序即时配送服务的接口</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fissues%2F2534" target="_blank">#2534</a><span> </span>代码提交审核接口新增部分参数</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2567" target="_blank">#2567</a><span> </span>直播间和商品、挂件组件等相关接口完善</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2574" target="_blank">#2574</a><span> </span>物流服务增加即时配送查询相关接口</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2578" target="_blank">#2578</a><span> </span>小程序直播增加挂件组件全局key相关接口</li> 
 <li>WxMaMessage增加小程序撤销授权AppID事件部分字段</li> 
 <li>回调消息解析类WxMaMessage增加allFieldsMap属性，以存储所有xml消息报文</li> 
 <li>获取小程序码的createWxaCode相关接口支持envVersion参数</li> 
</ul> 
<h2 style="text-align:start">微信支付</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2422" target="_blank">#2422</a><span> </span>修复企业付款给员工接口签名错误问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2443" target="_blank">#2443</a><span> </span>增加服务商微工卡相关功能接口以及微信批量转账到零钱的服务商接口实现</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2467" target="_blank">#2467</a><span> </span>微信支付V3接口请求增加代理设置参数的支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fissues%2F2478" target="_blank">#2478</a><span> </span>申请分账和查询分账结果添加detail_id</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2538" target="_blank">#2538</a><span> </span>签约通知结果类修复request_serial字段类型</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2547" target="_blank">#2547</a><span> </span>二级商户进件接口增加owner字段</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fissues%2F2562" target="_blank">#2562</a><span> </span>增加微信消费者投诉2.0接口</li> 
 <li>支付分请求接口代码优化</li> 
</ul> 
<h2 style="text-align:start">开放平台</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2379" target="_blank">#2379</a><span> </span>增加个人小程序快速注册和试用小程序快速注册相关接口</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2385" target="_blank">#2385</a><span> </span>增加为小程序设置用户隐私指引的相关接口</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fpull%2F2550" target="_blank">#2550</a><span> </span>第三方平台新增全局错误码的中文描述</li> 
 <li>优化 Spring Boot Starter 配置逻辑</li> 
 <li>小程序模板管理获取代码模板列表接口返回增加两个小程序相关的字段</li> 
</ul> 
<h2 style="text-align:start">其他公共问题</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fissues%2F2390" target="_blank">#2390</a><span> </span>ApacheHttpClientBuilder增加支持配置重试策略和超时策略的参数</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWechat-Group%2FWxJava%2Fissues%2F2530" target="_blank">#2530</a><span> </span>修复 pull-parser 依赖传递导致spring boot 2.6.3无法启动</li> 
 <li>XmlUtils工具类优化，支持变态微信消息</li> 
</ul>
                                        </div>
                                      
</div>
            