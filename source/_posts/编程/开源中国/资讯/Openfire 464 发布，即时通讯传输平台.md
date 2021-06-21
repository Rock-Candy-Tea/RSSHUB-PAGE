
---
title: 'Openfire 4.6.4 发布，即时通讯传输平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4705'
author: 开源中国
comments: false
date: Mon, 21 Jun 2021 07:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4705'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Openfire 是一个功能丰富的即时通讯（IM）和群组聊天服务器，使用 XMPP 协议。Openfire 4.6.4 正式发布，该版本更新内容如下：</p> 
<p><strong>错误</strong></p> 
<ul> 
 <li>LoginLimitManager 的偶尔测试失败；</li> 
 <li>Websocket 无法传递某些错误；</li> 
 <li>管理控制台不显示不在内存中的 MUC rooms；</li> 
 <li>IQVersionHandler 不能处理 bosh/websocket 客户端；</li> 
 <li>Self-presence 状态没有被添加到 kick presence 状态；</li> 
 <li>MUC room 名称的标准化不一致；</li> 
</ul> 
<p><strong>改进：</strong></p> 
<ul> 
 <li>将 common-io 从 2.6 升级至 2.7；</li> 
 <li>不要列出 MUC rooms 的每一页；</li> 
 <li>在管理控制台中重写从内存中清除的 MUC 选项；</li> 
 <li>在管理控制台显示组成员的完整名称；</li> 
 <li>提升大量 MUC rooms 的启动速度；</li> 
 <li>使线程池可以配置；</li> 
 <li>通过 JMX 暴露线程池的状态；</li> 
 <li>在被验证前发送数据时返回 IQ auth 错误；</li> 
 <li>版本检查线程不应该在任务引擎中休眠；</li> 
 <li>不要存储已经存储的离线消息；</li> 
 <li>考虑在 OfflineMessageListener 中使用 OfflineMessage 而不是 Message；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdownload.igniterealtime.org%2Fopenfire%2Fdocs%2Flatest%2Fchangelog.html" target="_blank">https://download.igniterealtime.org/openfire/docs/latest/changelog.html</a></p>
                                        </div>
                                      
</div>
            