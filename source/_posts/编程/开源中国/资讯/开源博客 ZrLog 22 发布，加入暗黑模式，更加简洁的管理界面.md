
---
title: '开源博客 ZrLog 2.2 发布，加入暗黑模式，更加简洁的管理界面'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.zrlog.com/assets/screenprint/article-edit-dark.png'
author: 开源中国
comments: false
date: Mon, 05 Jul 2021 08:33:00 GMT
thumbnail: 'https://www.zrlog.com/assets/screenprint/article-edit-dark.png'
---

<div>   
<div class="content">
                                                                    
                                                        <div> 
 <blockquote> 
  <p>ZrLog是使用 Java 开发的博客/CMS程序，具有简约，易用，组件化，内存占用低等特点。自带 Markdown 编辑器，让更多的精力放在写作上，而不是花费大量时间在学习程序的使用上。</p> 
 </blockquote> 
 <p>ZrLog 从开始使用 bootstrap 作为主要的前端框架都用很多年了，bootstrap 的确是一个特别便于服务端开发人员上手的框架的，但是随着时间的变化，发现 bootstrap 很多地方不太方便的地方，因为仅用默认样式，会出现千篇一律的 UI 样式的。加上之前的使用 JQuery 异步加载网页在浏览器的控制台一直出现警告，所以就将整体的 UI 框架替换为 antd</p> 
 <p>从 2.2 版本开始，ZrLog 管理后台页面从之前的 服务端 freemarker + 客户端 JQuery 渲染 变更为使用 React 客户端渲染，如果需要自己定制修改管理页面需要了解基本的 React 语法</p> 
 <h3>v2.2 变更的内容</h3> 
 <p><strong>v1.5以后版本可通过后台管理提供系统更新直接进行升级，无需下载war手动合并覆盖，重启，Docker 模式运行的程序可以通过 sh upgrade.sh 进行升级</strong></p> 
 <h4>新特</h4> 
 <ul> 
  <li>全新的安装向导和管理页面实现（<code>bootstrap</code> -> <code>antd</code>）UI 更加简洁统一</li> 
  <li>管理界面加入暗黑模式</li> 
  <li>数据库备份插件支持备份到云存储，支持 arm 处理器的备份（树莓派）</li> 
 </ul> 
 <h4>优化</h4> 
 <ul> 
  <li>优化 <code>editormd</code> 的加载逻辑和样式</li> 
  <li>更加简洁的文章撰写界面</li> 
  <li>简化插件管理页面</li> 
  <li>统一管理后台字体类型（font-family）</li> 
  <li>优化存在时的新版本更新的通知样式</li> 
 </ul> 
 <h4>修复</h4> 
 <ul> 
  <li>修复部分情况下的页面静态化的问题</li> 
  <li>文章阅读数统计错误</li> 
  <li><code>editormd</code> 异步加载的导致的样式错乱问题</li> 
 </ul> 
 <h3>其他</h3> 
 <ul> 
  <li>GitHub: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2F94fzb%2Fzrlog" target="_blank">https://github.com/94fzb/zrlog</a></li> 
  <li>码云: <a href="https://gitee.com/94fzb/zrlog">https://gitee.com/94fzb/zrlog</a></li> 
  <li>程序主页: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zrlog.com" target="_blank">https://www.zrlog.com</a></li> 
 </ul> 
 <p>有收获，记得点下 star 收藏下</p> 
 <h3>最后</h3> 
 <p>上一张启用暗黑模式下的文章撰写界面截图</p> 
 <p><img alt src="https://www.zrlog.com/assets/screenprint/article-edit-dark.png" referrerpolicy="no-referrer"></p> 
</div>
                                        </div>
                                      
</div>
            