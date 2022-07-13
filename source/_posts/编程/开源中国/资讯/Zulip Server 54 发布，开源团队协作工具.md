
---
title: 'Zulip Server 5.4 发布，开源团队协作工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2780'
author: 开源中国
comments: false
date: Wed, 13 Jul 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2780'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0"><span style="color:#000000">Zulip Server 5.4 现已发布。Zulip 是一个开源团队协作工具，一款专为实时和异步对话而设计的现代团队聊天应用程序，支持快速搜索、拖放文件上传、图像预览、组私人消息、可听通知、错过电子邮件消息提醒与桌面应用等。</span></p> 
<p style="margin-left:0"><span style="color:#000000">具体更新内容如下：</span></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzulip.com%2Fhelp%2Fexport-your-organization%23export-of-public-data" target="_blank">CVE-2022-31134：</a>从公共数据的导出中排除私人文件上传。</li> 
 <li>升级的 python requirements。</li> 
 <li>改进了负载均衡器的文档以提及 CIDR 地址范围。</li> 
 <li>记录了支持的 CPU 架构的明确列表。</li> 
 <li>切换<code>html2text</code>为作为子进程而不是 Python模块运行，因为它的 GPL 许可证与 Zulip 的不兼容。</li> 
 <li>将<code>markdown-include</code>python 模块替换为重新实现，因为它的 GPL 许可证与 Zulip 的不兼容。</li> 
 <li>由于对<code>python-debian</code>的 GPL依赖于，将用于验证第三方许可证的<code>tools/check-thirdparty</code>开发工具重新授权为 GPL。</li> 
 <li>关闭了 Tornado 服务器中的潜在 race condition，事件到达的时间与请求完全相同，导致服务器错误。</li> 
 <li>添加了一个工具来帮助自动化更多的发布过程。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzulip%2Fzulip%2Freleases%2Ftag%2F5.4" target="_blank">https://github.com/zulip/zulip/releases/tag/5.4</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            