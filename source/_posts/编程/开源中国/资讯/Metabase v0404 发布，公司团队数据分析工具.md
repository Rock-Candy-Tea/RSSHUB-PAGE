
---
title: 'Metabase v0.40.4 发布，公司团队数据分析工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9196'
author: 开源中国
comments: false
date: Sat, 11 Sep 2021 07:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9196'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p>Metabase 发布了 0.40.4 版本。Metabase 是一个简单的分析工具，通过给公司成员提问，从得到的数据中进行分析、学习。</p> 
 <p style="box-sizing: inherit; margin: 0px 0px 20px; line-height: inherit; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">此版本更新内容如下：</p> 
 <p style="box-sizing: inherit; margin: 0px 0px 20px; line-height: inherit; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><strong>Bug 修复</strong></p> 
 <ul> 
  <li>当下拉列表具有<code>null</code>值时，仪表板过滤器自动完成功能不适用于混合搜索/下拉列表( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F17659" rel="nofollow" target="_blank">#17659</a> )</li> 
  <li>除非仪表板在 <span style="color: rgb(36, 41, 47); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI Variable", "Segoe UI", system-ui, ui-sans-serif, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji"; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;">root collection </span>中，否则无法删除仪表板订阅 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F17658" rel="nofollow" target="_blank">#17658</a> )</li> 
  <li>可能不输入订阅的收件人，这将导致黑屏 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F17657" rel="nofollow" target="_blank">#17657</a> )</li> 
  <li>有效的电子邮件设置在保存时消失，但在刷新后重新出现 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F17615" rel="nofollow" target="_blank">#17615</a> )</li> 
  <li>无法在自定义表达式上单击“Learn more” ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F17548" rel="nofollow" target="_blank">#17548</a> )</li> 
  <li>在某些情况下，编辑警报会导致其被删除 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F17547" rel="nofollow" target="_blank">#17547</a> )</li> 
  <li>带有“This is a large database ...”的新数据库仍然使用默认的同步+扫描设置（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F17450" rel="nofollow" target="_blank">#17450</a>）</li> 
  <li>通过搜索将卡片添加到仪表板会导致卡片在浏览器刷新之前显示 spinner  ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15959" rel="nofollow" target="_blank">#15959</a> )</li> 
  <li>自 1.38.3 起无法使用 OpenAM SAML 登录 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F15567" rel="nofollow" target="_blank">#15567</a> )</li> 
  <li>Native 问题 Filter widget type"="None，即使将 filter widget 更改为其他内容后也会隐藏它（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Fissues%2F13825" rel="nofollow" target="_blank">#13825</a>）</li> 
 </ul> 
 <p style="box-sizing:border-box; margin-top:0.25em">更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmetabase%2Fmetabase%2Freleases%2Ftag%2Fv0.40.4" rel="nofollow" target="_blank">https://github.com/metabase/metabase/releases/tag/v0.40.4</a></p> 
</div>
                                        </div>
                                      
</div>
            