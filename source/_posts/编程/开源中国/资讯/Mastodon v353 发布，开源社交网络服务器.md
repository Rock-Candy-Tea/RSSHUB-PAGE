
---
title: 'Mastodon v3.5.3 发布，开源社交网络服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=826'
author: 开源中国
comments: false
date: Sat, 28 May 2022 08:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=826'
---

<div>   
<div class="content">
                                                                                            <p>Mastodon v3.5.3 发布<span style="background-color:#ffffff; color:#333333">了。Mastodon 是一个免费的开源社交网络程序，一个商业平台的替代方案，避免了单个公司垄断沟通的风险。无论选择哪个服务器，都可以与其他人进行互动。通过运行自己的 Mastodon 实例，可无缝地参与到社交网络中。</span></p> 
<p>该版本带来如下改动：</p> 
<h3 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>添加</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<ul> 
 <li><strong>添加语言下拉菜单，以在 Web UI 中撰写表单</strong></li> 
 <li><strong>在 Web UI</strong> 中为受限帐户添加警告</li> 
 <li><code>limited</code>在 REST API 中为帐户添加属性</li> 
</ul> 
<h3 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>改变了</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<ul> 
 <li><strong>更改 RSS 提要</strong> 
  <ul> 
   <li>标题现在是发布日期和时间</li> 
   <li>主体现在呈现所有内容，包括民意调查和表情符号</li> 
   <li>所有媒体附件都包含在媒体 RSS 中</li> 
  </ul> </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmastodon%2Fmastodon%2Fpull%2F18515" target="_blank">在隐私政策和 Web UI </a>中将“危险”更改为“敏感”</li> 
 <li>将未经确认的帐户更改为在 REST API中不可见</li> 
 <li>改变<code>tootctl search deploy</code>以提高性能</li> 
 <li>更改搜索索引以使用批处理来最小化资源使用 </li> 
</ul> 
<h3 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<ul> 
 <li>修复追随者和其他计数器能够变为负数</li> 
 <li>修复创建状态时不必要的查询</li> 
 <li>修复警告报告之外的帐户关闭该帐户的所有报告</li> 
 <li>修复重定向到本地帖子的链接时出现的错误</li> 
 <li>修复在 REST API 中返回不可用值的首选发布语言</li> 
 <li>修复外部状态重新记录时的竞争条件错误</li> 
 <li>修复上诉验证错误的缺失字符串</li> 
 <li>修复在 Web UI 中显示关注按钮的阻止/静音列表</li> 
 <li>修复 Redis 配置未由<code>mastodon:setup</code>更改</li> 
 <li>修复未在 Web UI 中使用快速过滤逻辑的流式通知</li> 
 <li>修复浮动操作按钮遮挡 Web UI 中的最后一个元素</li> 
 <li>修复未在审核日志中记录的帐户警告</li> 
 <li>修复直接可见状态的剩余图标</li> 
 <li>修复链接验证需要区分大小写的链接</li> 
 <li>修复嵌入未正确设置其高度</li> 
</ul> 
<h3 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>安全</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<ul> 
 <li>多次修复并发取消关注的递减关注者计数</li> 
 <li>修复能够无限次上诉罢工</li> 
 <li>修复能够报告其他无法访问的状态</li> 
 <li>修复空票任意增加民意调查中的选民人数</li> 
 <li>在批准敏感标记状态的上诉时修复版主身份泄漏 </li> 
 <li>修复暂停的用户能够访问不需要用户的 API </li> 
 <li>修复确认重定向到没有<code>Location</code>标题的应用程序</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmastodon%2Fmastodon%2Freleases%2Ftag%2Fv3.5.3" target="_blank">https://github.com/mastodon/mastodon/releases/tag/v3.5.3</a></p>
                                        </div>
                                      
</div>
            