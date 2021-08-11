
---
title: 'Metabase v0.40.2 发布，公司团队数据分析工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8842'
author: 开源中国
comments: false
date: Wed, 11 Aug 2021 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8842'
---

<div>   
<div class="content">
                                                                                            <p>Metabase 发布了 0.40.2 版本。Metabase 是一个简单的分析工具，通过给公司成员提问，从得到的数据中进行分析、学习。</p> 
<p>此版本更新内容如下：</p> 
<p><strong>Enhancements</strong> </p> 
<ul> 
 <li>0.40.2 的文档改进 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fpull%2F17303" target="_blank">#17303</a> )</li> 
 <li>将 Metabase Cloud 链接添加到托管实例的管理设置 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fpull%2F17134" target="_blank">#17134</a> )</li> 
 <li>修复 dashboard card 悬停按钮拖动行为（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fpull%2F17130" target="_blank">#17130</a>）</li> 
 <li>将过滤器与搜索输入结合使用时，弹出页脚会发生位移 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F16830" target="_blank">#16830</a> )</li> 
 <li>地图设置页面上的按钮需要填充 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F16612" target="_blank">#16612</a> )</li> 
 <li>如果验证失败，LDAP/Email 设置将被清除 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F16226" target="_blank">#16226</a> )</li> 
 <li>修改而不是替换默认的 EB nginx 配置 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F5623" target="_blank">#5623</a> )</li> 
</ul> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li>Snippet 文件夹权限始终应用于 root ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F17268" target="_blank">#17268</a> )</li> 
 <li>由于缺少 Node.js，无法在 VS Code 中开始开发 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F17233" target="_blank">#17233</a> )</li> 
 <li>问题构建器上的搜索小部件挂起 tab，不遵守 API 字段搜索限制 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F17228" target="_blank">#17228</a> )</li> 
 <li>仅显示 50 个组 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F17200" target="_blank">#17200</a> )</li> 
 <li>People search 下拉菜单超出屏幕 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F17186" target="_blank">#17186</a> )</li> 
 <li>电子邮件自动完成和“其他用户的个人收藏”中仅显示 50 个用户 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F17164" target="_blank">#17164</a> )</li> 
 <li>Dashboard - 将“Click Behavior”添加到图像字段可将图像转换为 URL ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F17161" target="_blank">#17161</a> )</li> 
 <li>由于 AWS Inspector 在某些区域不可用，因此无法在 AWS Elastic Beanstalk 上升级到 v0.40.x ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F17143" target="_blank">#17143</a> )</li> 
 <li>Elastic Beanstalk nginx 配置未在最新的 EB docker 镜像上更新 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F17115" target="_blank">#17115</a> )</li> 
 <li>前 50 个用户后无法停用用户 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F17113" target="_blank">#17113</a> )</li> 
 <li>“Audit”部分的 tag 看起来已损坏 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F17102" target="_blank">#17102</a> )</li> 
 <li>......</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Freleases%2Ftag%2Fv0.40.2" target="_blank">https://github.com/metabase/metabase/releases/tag/v0.40.2</a></p>
                                        </div>
                                      
</div>
            