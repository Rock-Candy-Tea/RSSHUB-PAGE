
---
title: '开源密码管理器 Bitwarden 多平台更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4022'
author: 开源中国
comments: false
date: Sat, 19 Mar 2022 07:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4022'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Bitwarden 是一款开源的密码管理服务，使用者可在加密的保管库中储存敏感信息。Bitwarden 平台提供有多种客户端应用程式，包括 Web 版本、桌面应用，浏览器扩展、移动端应用和 CLI 版本等。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">日前 Bitwarden 更新了 Server 1.47.0、Web 2.27.0、Desktop 1.32.0、CLI 1.22.0、Directory Connector 2.9.11 多个版本，对移动应用和浏览器扩展的更新将在后续版本中再更新。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">此次更新内容如下：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>通过 CLI 的 Vault Management API：使用新的<span> </span><code>serve</code><span> </span>CLI 命令，你可以对全套 Vault Management 端点进行 API 调用</li> 
 <li>导出 CLI 命令的变化：<span> </span><code>export</code><span> </span>不再需要一个主密码，但是你现在可以使用<span> </span><code>-password</code><span> </span>参数来为加密导出设置一个自定义的加密/解密密码</li> 
 <li>新的导入器：新版本为 Dashlane 的<span> </span><code>.csv</code><span> </span>文件和 1Password 的<span> </span><code>.1pux</code><span> </span>文件增加了自定义导入器（后者需要 1Password v8.5 以上版本）</li> 
 <li>对 Myki 导入器的改进</li> 
 <li>弃用了 Artifact 绑定：出于安全考虑，SAML SSO 配置的 Artifact 绑定已被删除</li> 
 <li>对 Docker Compose v2 的支持</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbitwarden%2Fdesktop%2Freleases" target="_blank">https://github.com/bitwarden/desktop/releases</a></p>
                                        </div>
                                      
</div>
            