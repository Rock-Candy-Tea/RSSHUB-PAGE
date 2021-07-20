
---
title: 'code-server 3.11.0 发布，在远程服务器上运行 Visual Studio Code'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4978'
author: 开源中国
comments: false
date: Tue, 20 Jul 2021 06:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4978'
---

<div>   
<div class="content">
                                                                    
                                                        <p>code-server 3.11.0 现已发布，具体更新内容如下： </p> 
<p><strong>VS Code v1.57.1</strong><strong> </strong></p> 
<p>code-server 将所有用户数据保存在 ~/.local/share/code-server 中， 以便在两次安装之间保留这些数据。</p> 
<p><strong>New Features</strong> </p> 
<ul> 
 <li>feat(vscode)：升级到版本 1.57.1 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcdr%2Fcode-server%2Fpull%2F3544" target="_blank">#3544</a></li> 
</ul> 
<p><strong>Bug 修复</strong></p> 
<p>修复反向代理后面的注销</p> 
<ul> 
 <li>修复使用 base path 时的注销问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcdr%2Fcode-server%2Fissues%2F3608" target="_blank">#3608</a> ) <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcdr%2Fcode-server%2Fpull%2F3611" target="_blank">#3611</a></li> 
</ul> 
<p><strong>Documentation</strong></p> 
<p>进行了大量重组以使其更易于参考，以及一些新信息。</p> 
<ul> 
 <li>docs：添加 Pomerium <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcdr%2Fcode-server%2Fpull%2F3424" target="_blank">#3424</a></li> 
 <li>docs：修复拉取请求部分中令人困惑的句子 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcdr%2Fcode-server%2Fpull%2F3460" target="_blank">#3460</a></li> 
 <li>docs：从更新日志中删除 toc</li> 
 <li>docs(MAINTAINING)：添加有关 CHANGELOG 的信息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcdr%2Fcode-server%2Fpull%2F3467" target="_blank">#3467</a></li> 
 <li>docs：将发布过程移至 MAINTAINING.md <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcdr%2Fcode-server%2Fissues%2F3441" target="_blank">#3441</a></li> 
 <li>docs：从 guide.md 格式化“Caddy”</li> 
</ul> 
<p><strong>Development</strong></p> 
<p>移至 Node v14，使用 Argon2 进行 pw 散列和 CI 工作</p> 
<ul> 
 <li>chore：使用 buildx 交叉编译 docker 镜像 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcdr%2Fcode-server%2Fissues%2F3166" target="_blank">#3166</a></li> 
 <li>chore：将 node 更新到 v14 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcdr%2Fcode-server%2Fissues%2F3458" target="_blank">#3458</a></li> 
 <li>chore：更新 .gitignore <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcdr%2Fcode-server%2Fpull%2F3557" target="_blank">#3557</a></li> 
 <li>修复：对 password hash 使用足够的计算量 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcdr%2Fcode-server%2Fpull%2F3422" target="_blank">#3422</a></li> 
 <li>docs(CONTRIBUTING)：添加关于测试的部分 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcdr%2Fcode-server%2Fpull%2F3629" target="_blank">#3629</a></li> 
</ul> 
<p><strong>Development</strong></p> 
<ul> 
 <li>fix(publish)：更新 brew-bump.sh 中的 cdrci fork <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcdr%2Fcode-server%2Fpull%2F3468" target="_blank">#3468</a></li> 
 <li>chore(dev)：从 parcel 中迁移<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcdr%2Fcode-server%2Fpull%2F3578" target="_blank">#3578 </a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcdr%2Fcode-server%2Freleases%2Ftag%2Fv3.11.0" target="_blank">https://github.com/cdr/code-server/releases/tag/v3.11.0</a> </p>
                                        </div>
                                      
</div>
            