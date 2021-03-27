
---
title: 'Tails 4.17 发布，隐私性极高的 Linux 发行版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0327/070545_hZ4l_4937141.png'
author: 开源中国
comments: false
date: Sat, 27 Mar 2021 07:07:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0327/070545_hZ4l_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>Tails 4.17 正式发布，本次更新内容如下：</p> 
<h3>提高自动升级的可靠性</h3> 
<ul> 
 <li> <p>升级时自动修复使用的文件系统；</p> <p>由于文件系统不干净，即使进行手动升级，自动升级有时也会失败。(#17902)</p> </li> 
 <li> <p>下载升级失败时自动恢复。</p> </li> 
</ul> 
<h3>其他更改和更新</h3> 
<ul> 
 <li>更新 Tor Browser 到 10.0.14；</li> 
 <li>更新 Thunderbird 到 78.8.0；</li> 
 <li>更新 Tor 到 0.4.5.7；</li> 
 <li>更新 GRUB 到 2.04-16；</li> 
 <li>更新一些固件包，这应该会改善对一些 Wi-Fi 接口的支持，尤其是 Intel、Broadcom 和 Cypress 接口。</li> 
</ul> 
<h3>修复了一些问题</h3> 
<ul> 
 <li>改进离线时启动不安全浏览器时的错误信息。</li> 
</ul> 
<p>        <img alt height="194" src="https://static.oschina.net/uploads/space/2021/0327/070545_hZ4l_4937141.png" width="551" referrerpolicy="no-referrer"></p> 
<h3>已知问题</h3> 
<ul> 
 <li> <p>Tails 4.14 或更早的版本开始，自动升级已经失效。</p> <p>要从 Tails 4.14 或更早的版本升级，您可以选择以下两种方式：</p> 
  <ol> 
   <li> <p>进行手动升级；</p> </li> 
   <li> <p>从终端修复自动升级。要做到这一点，您可以：</p> 
    <ul> 
     <li> <p>启动 Tails 并设置一个管理密码；</p> </li> 
     <li> <p>在终端上执行以下命令。</p> <pre><code>torsocks curl --silent <https://gitlab.tails.boum.org/tails/tails/-/raw/master/config/chroot_local-includes/usr/share/tails/certs/lets-encrypt-r3.pem> \\
| sudo tee --append /usr/local/etc/ssl/certs/tails.boum.org-CA.pem \\
&& systemctl --user restart tails-upgrade-frontend
</code></pre> <p>注：该命令是一个跨多行的单个命令，一次复制并粘贴整个代码块，并确保它作为单个命令执行。</p> </li> 
    </ul> </li> 
   <li> <p>大约 30 秒后，系统将提示您升级到最新版本的 Tails。</p> </li> 
  </ol> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftails.boum.org%2Fnews%2Fversion_4.17%2F" target="_blank">https://tails.boum.org/news/version_4.17/</a></p>
                                        </div>
                                      
</div>
            