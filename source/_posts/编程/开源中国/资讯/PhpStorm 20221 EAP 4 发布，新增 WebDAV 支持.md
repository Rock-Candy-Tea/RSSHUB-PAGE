
---
title: 'PhpStorm 2022.1 EAP 4 发布，新增 WebDAV 支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-6ce477e7efe59c3056e41043f110ec27b4d.png'
author: 开源中国
comments: false
date: Mon, 07 Mar 2022 07:34:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-6ce477e7efe59c3056e41043f110ec27b4d.png'
---

<div>   
<div class="content">
                                                                                            <p>PhpStorm 2022.1 EAP #4 现已作为第四个尝鲜版<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fphpstorm%2F2022%2F03%2Fphpstorm-2022-1-eap-4%2F" target="_blank">正式发布</a>，该版本的内容包括增强的新建项目向导、对 WebDAV 部署的支持、Rsync 的一些附加功能以及一些新的检查。</p> 
<h3>新的 Composer 项目向导</h3> 
<p>增强 <em><strong>新建项目</strong> </em>向导：当创建一个新的空项目时您可以选择为其自动生成一个<code>composer.json</code>文件，并提供所需的依赖项。</p> 
<p><img alt height="525" src="https://oscimg.oschina.net/oscnet/up-6ce477e7efe59c3056e41043f110ec27b4d.png" width="700" referrerpolicy="no-referrer"></p> 
<p>创建项目后，PhpStorm 会提示你安装它们：</p> 
<p><img alt height="391" src="https://oscimg.oschina.net/oscnet/up-d1527791081f3a12feff9fb636386e05230.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>WebDAV 支持</h2> 
<p style="margin-left:0px">该版本引入了对使用 WebDAV 服务器进行部署的支持。要配置新服务器，请转到<em>首选项 | 构建、执行、部署 | 部署</em>，然后添加一个新的 <em>WebDAV </em>类型的服务器，并提供连接参数：</p> 
<p style="margin-left:0px"><img alt height="544" src="https://oscimg.oschina.net/oscnet/up-cfcacfe5aa7912c57e753a0c9ddacaf2edd.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>覆盖 Rsync 命令行参数</h2> 
<p style="margin-left:0px">PhpStorm 2021.3 为 SFTP 支持引入了 Rsync，以显着加快部署速度。Rsync 工具使用 <code>-zar</code> 命令行选项执行，它将压缩传输的数据 ( <code>z</code>)，保留传输文件和文件夹的权限、所有权和时间戳 ( <code>a</code>)，并递归到子目录 ( <code>r</code>)。</p> 
<p style="margin-left:0px">在此版本中，可以自定义选项集：转到 <em>设置 | 首选项 | 工具 | rsync </em>并提供所需的一组选项：</p> 
<p style="margin-left:0px"><img alt height="544" src="https://oscimg.oschina.net/oscnet/up-1be5f0eabf2876022d6b0a5d8deb52a2f08.png" width="700" referrerpolicy="no-referrer"></p> 
<h2>新的检查</h2> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>添加了一些新的检查，旨在简化正则表达式的使用。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h3>冗余修饰符</h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>以下新检查将报告正则表达式模式中使用，但不影响匹配的修饰符：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>/i</code>（不区分大小写）在不包含字母的模式中</li> 
 <li><code>/D</code>( <em>PCRE_DOLLAR_ENDONLY</em> ) 在不包含美元符号，或包含<code>\m</code>(PCRE_MULTILINE) 修饰符的模式中</li> 
 <li><code>/s</code>（点匹配换行符）在不包含点的模式中</li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>PhpStorm 提供<code>Alt+Enter</code>快速修复，可以快速删除这些修饰符。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt height="445" src="https://oscimg.oschina.net/oscnet/up-c01818c8d0f2d5fb7a469e990d16949568d.png" width="700" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"> </p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>不支持的修饰符</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>该<code>/e</code>修饰符在 PHP 7.0 及更高版本中已弃用。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><img alt height="191" src="https://oscimg.oschina.net/oscnet/up-17cfbb065f7b2f369c8154f789d4b360781.png" width="700" referrerpolicy="no-referrer"></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2>其他显著变化</h2> 
<ul> 
 <li>编辑 javadoc 存根的模板 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-97658" target="_blank">[IDEA-97658]</a></li> 
 <li>支持 yarn/pnpm 的 Corepack 安装 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-52682" target="_blank">[WEB-52682]</a></li> 
 <li>支持 GitHub PR 评论中的建议更改 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-241973" target="_blank">[IDEA-241973]</a></li> 
 <li>允许根据 mime 类型定义特定的外部差异工具 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-69499" target="_blank">[IDEA-69499]</a></li> 
 <li>将鼠标悬停在最大化按钮上时不会出现 Windows 11“对齐布局”。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-276887" target="_blank">[IDEA-276887]</a></li> 
 <li>Webpack 协助不适用于 ESM <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-31023" target="_blank">[WEB-31023]</a></li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"> </p> 
<p style="margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Farticles%2FWI-A-13%2FPhpStorm-2022.1-EAP-4-%28221.4906.9-build%29-Release-Notes" target="_blank">发布说明</a>中提供了该版本的完整更改列表，包括 Bug 修复和其他改进。</p>
                                        </div>
                                      
</div>
            