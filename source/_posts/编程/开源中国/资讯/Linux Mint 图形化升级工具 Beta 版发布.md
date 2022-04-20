
---
title: 'Linux Mint 图形化升级工具 Beta 版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0420/072106_8aYc_4937141.png'
author: 开源中国
comments: false
date: Wed, 20 Apr 2022 07:21:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0420/072106_8aYc_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>两周前，我们曾报道 Linux Mint 将会推出图形化升级工具的资讯（<a href="https://www.oschina.net/news/190346/linux-mint-upgrade-tool">点此查看</a>），该工具可以让用户更加方便地跨主要版本升级，无需再使用命令行工具，升级过程也会尽可能多地保留用户自定义的库。</p> 
<p>现在这个新的 Upgrade Tool 升级工具的 Beta 版本已经发布，用户可以用该工具将 LMDE（Linux Mint Debian Edition） 4 升级到 LMDE 5，<strong>暂不支持常规的基于 Ubuntu 的 Linux Mint</strong>。</p> 
<h3>步骤：</h3> 
<ul> 
 <li>要安装它，首先需刷新缓存并安装 mintupgrade 软件包；</li> 
</ul> 
<pre><code class="language-bash">apt update
apt install mintupgrade
</code></pre> 
<ul> 
 <li>Upgrade Tool 升级工具具有图形化界面，但需要从命令行启动它：</li> 
</ul> 
<pre><code class="language-bash">sudo mintupgrade
</code></pre> 
<ul> 
 <li>Upgrade Tool 升级工具启动，按照图形化界面上的说明操作即可完成升级；</li> 
</ul> 
<p><img alt height="714" src="https://static.oschina.net/uploads/space/2022/0420/072106_8aYc_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>工具完成且升级成功后，将其卸载并重新启动计算机；</li> 
</ul> 
<pre><code class="language-bash">apt remove mintupgrade
sudo reboot
</code></pre> 
<h3>注意事项：</h3> 
<ul> 
 <li>如果出现任何问题，所有更改都可以使用 Timeshift 恢复；</li> 
 <li>如果因任何原因关闭该工具，无论进行到升级的哪个步骤，都可以再次运行该工具；</li> 
 <li>此工具暂时仅适用于 LMDE，不支持常规的 Linux Mint**（未来会支持）**；</li> 
 <li>该工具尚处于 Beta 版本，因此最好只用于备用电脑或测试该工具；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.linuxmint.com%2F%3Fp%3D4312" target="_blank">https://blog.linuxmint.com/?p=4312</a></p>
                                        </div>
                                      
</div>
            