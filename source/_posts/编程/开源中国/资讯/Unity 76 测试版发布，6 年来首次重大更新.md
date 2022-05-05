
---
title: 'Unity 7.6 测试版发布，6 年来首次重大更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0505/072130_16Xw_4937141.png'
author: 开源中国
comments: false
date: Thu, 05 May 2022 07:24:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0505/072130_16Xw_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>Unity 7.6 将是 6 年来 Unity 的第一个重要版本（上一个版本还是在 2016 年 5 月）。官方已经重新启动了 Unity7 的积极开发，并将定期发布具有更多功能的新版本。你可以在 Ubuntu Unity 22.04 上运行以下命令来测试它：</p> 
<pre><code class="language-bash">sudo wget https://repo.unityx.org/unityx.key
sudo apt-key add unityx.key
echo 'deb https://repo.unityx.org/main testing main' | sudo tee /etc/apt/sources.list.d/unity-x.list
sudo apt-get update && sudo apt-get install -y unity
</code></pre> 
<p>下面是 Unity 7.6 中的一些变化：</p> 
<ul> 
 <li>仪表盘（应用启动器）和 HUD 已经被重新设计，使其看起来更现代</li> 
 <li>修复了仪表盘预览中损坏的应用信息和评级。</li> 
 <li>修复了 Dock 中的 "清空垃圾桶" 按钮</li> 
 <li>将完整的 Unity7 shell 源代码迁移到 GitLab，并使其在 22.04 上进行了编译。</li> 
 <li>设计更加扁平化，但保留了全系统范围的模糊效果。</li> 
 <li>dock 的菜单和工具提示被赋予了一个更现代的外观。</li> 
 <li>低图形模式现在工作得更好，仪表盘速度也比以前快。</li> 
 <li>现在 Unity7 的内存占用率略低，而 Ubuntu Unity 22.04 的内存占用率已大幅降低至约 700-800 MB。</li> 
 <li>修复了独立测试的 Unity7 启动器</li> 
 <li>有问题的测试已经被禁用，构建时间大大缩短</li> 
</ul> 
<p><strong>如果您想在 Ubuntu Unity 22.04 上编译 Unity7 并生成 DEB 文件，则需要运行以下命令：</strong></p> 
<pre><code class="language-bash">sudo apt-get install -y build-essential git cmake
git clone https://gitlab.com/ubuntu-unity/unity/unity
cd unity && sudo apt build-dep .
debuild -b --no-sign
nemo .. & disown
</code></pre> 
<p><strong>以下是 Unity 7.6 的一些屏幕截图：</strong></p> 
<p><strong><img alt height="446" src="https://static.oschina.net/uploads/space/2022/0505/072130_16Xw_4937141.png" width="700" referrerpolicy="no-referrer"></strong></p> 
<p><strong><img alt height="353" src="https://static.oschina.net/uploads/space/2022/0505/072141_31A8_4937141.png" width="700" referrerpolicy="no-referrer"></strong></p>
                                        </div>
                                      
</div>
            