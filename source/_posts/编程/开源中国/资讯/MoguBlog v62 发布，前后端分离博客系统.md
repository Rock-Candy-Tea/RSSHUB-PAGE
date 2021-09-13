
---
title: 'MoguBlog v6.2 发布，前后端分离博客系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=533'
author: 开源中国
comments: false
date: Mon, 13 Sep 2021 09:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=533'
---

<div>   
<div class="content">
                                                                                            <p>MoguBlog v6.2 已经发布，前后端分离博客系统。</p> 
<p>此版本更新内容包括：</p> 
<ul> 
 <li><strong>fix</strong>: 暂时移除导航栏白名单功能，解决网站出现 <strong>401</strong> 的问题</li> 
 <li><strong>feat:</strong> 增加是否开启注册邮件激活功能，开启后需要通过邮箱验证才能完成注册</li> 
 <li><strong>fix</strong>: 解决博客本地上传时存在图片无法正常显示的问题</li> 
 <li><strong>fix</strong>: 解决导航栏加载出现警告的问题</li> 
 <li><strong>fix</strong>: 优化推荐文章显示</li> 
 <li><strong>fix</strong>: 解决<strong>Markdown</strong>编辑器无法上传图片和数据回显的问题</li> 
 <li><strong>fix</strong>: 修复 <strong>nacos</strong> 连接数据库配置 解决 <strong>admin</strong> 账号权限时的问题</li> 
 <li><strong>fix</strong>：解决点击点赞按钮后，更新的点赞数量会从子组件试图更新父组件，导致显示错误，感谢小伙伴 @<a href="https://gitee.com/allworldg" rel="nofollow noreferrer noopener" target="_blank">allworldg</a> 的 <strong>PR</strong> 。</li> 
 <li><strong>fix</strong>: 修复 <strong>Firefox</strong> 和 <strong>Chrome</strong> 浏览器下搜索框样式显示异常的问题。</li> 
 <li><strong>fix</strong>: 图片选择器变更为懒加载，提升访问速度。</li> 
 <li><strong>feat</strong>: 完善博客备份功能，编辑博客时也支持实时备份</li> 
 <li><strong>feat</strong>: 删除文章时，同步删除该文章下所有的评论</li> 
 <li><strong>fix</strong>: 点赞博客增加文章信息展示</li> 
 <li><strong>fix</strong>: 解决 <strong>Sentinel</strong> 出现的异常，优化 <strong>Markdown</strong> 编辑器下博客备份功能</li> 
 <li><strong>fix</strong>: 修复转载博客版权读取错误，感谢群里小伙伴 @<a href="https://gitee.com/iq120609" rel="nofollow noreferrer noopener" target="_blank">苍山如海丶残阳如血</a> 的 <strong>PR</strong>。</li> 
 <li><strong>feat</strong>: 专题图片增加兜底显示。</li> 
 <li><strong>fix</strong>: 解决后台管理使用手机登录失败的情况。</li> 
 <li><strong>fix</strong>: 修复网盘管理文件夹为空的问题。</li> 
 <li><strong>feat</strong>: 网站新增友链申请模板</li> 
 <li><strong>fix</strong>：采用静态代码块，减少在根据ip地址获取地理信息时的资源消耗，感谢小伙伴 @<a href="https://gitee.com/join20190901" rel="nofollow noreferrer noopener" target="_blank">阿灿</a>的 <strong>PR</strong>。</li> 
 <li><strong>fix</strong>: 采用线程池，完成异步存储日志逻辑实现，感谢小伙伴 @<a href="https://gitee.com/join20190901" rel="nofollow noreferrer noopener" target="_blank">阿灿</a>的 <strong>PR</strong>。</li> 
 <li><strong>feat</strong>：解决执行异步线程收集日志时出现的空指针情况。</li> 
 <li><strong>fix</strong>：退出登录时候，清空Security中的用户信息。整个生命周期可能同时有多个用户在使用。这时候应用需要保存多个 <strong>SecurityContext</strong>（安全上下文），需要利用 <strong>ThreadLocal</strong> 进行保存，每个线程都可以利用<strong>ThreadLocal</strong> 获取其自己的 <strong>SecurityContext</strong>，及安全上下文。用户退出时清除其在<strong>SecurityContextHolder</strong> 中的上下文信息，感谢群里小伙伴 @<a href="https://gitee.com/zjq_6688" rel="nofollow noreferrer noopener" target="_blank">遇见</a> 的PR。</li> 
 <li><strong>fix</strong>: 修复表情弹出框出现的异常。</li> 
 <li><strong>fix</strong>: 修改爬虫模块图片爬取的地址，优化图片截取正则表达式。</li> 
 <li><strong>fix</strong>: 修复后台管理登录失败时的登录限制时长</li> 
 <li><strong>fix</strong>: 解决后台管理搜索时出现的 <strong>BUG</strong></li> 
 <li><strong>fix</strong>：解决 <strong>Banner</strong> 出现边框的问题，解决反馈无法删除的问题</li> 
 <li><strong>feat</strong>: 更新文档，新增一条命令部署蘑菇博客。</li> 
 <li><strong>feat</strong>：优化网站布局样式，评论支持 <strong>Markdown</strong></li> 
 <li><strong>fix</strong>：修复mogu_sms 启动时的问题</li> 
 <li><strong>fix</strong>：修正备案跳转问题</li> 
 <li><strong>feat</strong>：增加搜索模式开关控制；支持一键切换 <strong>SQL</strong> 搜索、<strong>ES</strong>搜索、<strong>Solr</strong>搜索</li> 
</ul> 
<p>详情查看：<a blank="_target" href="https://gitee.com/moxi159753/mogu_blog_v2/releases/v6.2">https://gitee.com/moxi159753/mogu_blog_v2/releases/v6.2</a></p>
                                        </div>
                                      
</div>
            