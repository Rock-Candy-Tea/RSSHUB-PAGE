
---
title: '在 macOS 下搭建 51 单片机开发环境'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://cdn.sspai.com/2022/03/02/067c70a31982fe82ef780fcbe17dda69.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
author: 少数派 sspai
comments: false
date: Wed, 02 Mar 2022 08:11:25 GMT
thumbnail: 'https://cdn.sspai.com/2022/03/02/067c70a31982fe82ef780fcbe17dda69.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
---

<div>   
<div class="articleWidth-content" data-v-0b37afcb><div class="update-wrap" data-v-0b37afcb></div><div class="content wangEditor-txt minHeight" data-v-0b37afcb><h2> 搭建原因</h2><p><br>本学期的《微机原理与单片机技术》需要进行一些简单的单片机开发实验，原本打算在 Parallels Desktop 的 Windows 虚拟机中进行实验，但实在难以忍受老旧 MacBook 上运行虚拟机的发热和吵闹的风扇声以及割裂的使用体验（我校提供的是“万年前”的盗版 Keil），决定尝试在 macOS 下尝试搭建开发环境。</p><h2>我的设备</h2><ul><li>Macbook Pro ( Intel )</li><li>STC89C52RC 单片机及开发板</li></ul><p><br>本文可能仅适用于 Intel 架构的 macOS 和 STC89C52RC 单片机，使用 ARM 架构 macOS 或其他型号单片机的朋友们可能还需要继续折腾。</p><h2>软件安装</h2><ul><li>CH340/CH341 的 USB 转串口驱动程序</li><li>交叉编译器 sdcc</li><li>程序下载器 stcgal</li><li>一个趁手的代码编辑器</li></ul><h3><br>准备工作</h3><h4><br>Homebrew</h4><p><br>如果没有安装 Homebrew，你可以从 <a href="https://brew.sh/" target="_blank">这里</a> 获取。如果访问较慢，可以尝试更换为 <a href="https://mirrors.tuna.tsinghua.edu.cn/help/homebrew/" target="_blank">清华源</a>。</p><h4><br>Python 和 Pip</h4><p><br>你可以参照我派的 <a href="https://sspai.com/post/69595">这篇教程</a> 来安装 Python 和 Pip。</p><h3><br>驱动程序的安装</h3><p><br>沁恒微电子提供了 CH340/CH341 的 USB 转串口驱动程序，你可以点击 <a href="http://www.wch.cn/download/CH341SER_MAC_ZIP.html" target="_blank">这里</a> 下载。解压后运行 pkg 文件，按照提示即可简单的完成安装。</p><p><br>在完成安装后，将开发板连接至 Mac。在终端中输入：<code>ls /dev/tty.wchusbserial*</code>，<br>若出现了类似的文字（后四位数字可能不同）<code>/dev/tty.wchusbserial1440</code>那么恭喜你，驱动程序的安装已经完成。</p><h3><br>交叉编译工具 sdcc</h3><p><br>在终端中输入：<code>brew install sdcc</code>即可完成安装。</p><h3><br>程序下载器 stcgal</h3><p><br>在终端中输入：<code>pip3 install stcgal</code>即可完成安装。</p><p> </p><h3>初试牛刀——用数码管点亮 SSPAI</h3><h4><br>示例代码</h4><p><br>将下面的代码保存为 main.c。</p><pre class="language-null"><code>#include <8051.h>

unsigned char Table[] = &#123;0x6D,0x73,0x77,0x30&#125;; //对应SPAI四个字母

void Delay(unsigned int x)//@11.0592MHz下延迟1ms
&#123;
unsigned char i, j;
while(x--)
&#123;
i = 2;
j = 199;
do
&#123;
while (--j);
&#125; while (--i);
&#125;

&#125;

void Turn_ON(unsigned int Location ,unsigned int Num1)  //点亮
&#123;
switch(Location) //片选
&#123;
case 1:P2_4=1;P2_3=1;P2_2=1;break;
case 2:P2_4=1;P2_3=1;P2_2=0;break;
case 3:P2_4=1;P2_3=0;P2_2=1;break;
case 4:P2_4=1;P2_3=0;P2_2=0;break;
case 5:P2_4=0;P2_3=1;P2_2=1;break;
case 6:P2_4=0;P2_3=1;P2_2=0;break;
case 7:P2_4=0;P2_3=0;P2_2=1;break;
case 8:P2_4=0;P2_3=0;P2_2=0;break;
&#125;
P0=Table[Num1]; //段选
Delay(1);
P0=0x00;
&#125;

void main() //主函数
&#123;
while(1)
&#123;
Turn_ON(1,0);
Turn_ON(2,0);
Turn_ON(3,1);
Turn_ON(4,2);
Turn_ON(5,3);
&#125;
&#125;</code></pre><h4><br>使用 sdcc 进行编译</h4><p><br>使用终端加载到储存了示例代码的目录下，利用<code>sdcc main.c</code>编译程序后，可以看到 sdcc 已经在同一目录下生成了一系列文件。</p><figure class="ss-imgRows" figcaption="sdcc 编译命令及其生成的文件"><img src="https://cdn.sspai.com/2022/03/02/067c70a31982fe82ef780fcbe17dda69.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt data-original="https://cdn.sspai.com/2022/03/02/067c70a31982fe82ef780fcbe17dda69.png" referrerpolicy="no-referrer"><img src="https://cdn.sspai.com/2022/03/02/7282068ec38d430a1fd6f698de5b3d69.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" alt data-original="https://cdn.sspai.com/2022/03/02/7282068ec38d430a1fd6f698de5b3d69.png" referrerpolicy="no-referrer"></figure><p> </p><h4><br>使用 stcgal 下载到单片机</h4><p><br>可以使用<code>stcgal -P stc89 -p /dev/tty.wchusbserial1440 main.ihx</code>进行下载操作，其中 -P 参数用于说明单片机的类型， -p 参数则用于表明单片机所在的串口位置，main.ihx 则是先前使用 sdcc 编译生成的可执行文件。</p><p><br><i>需要注意的是，在执行 stcgal 命令后，需要给单片机断电后重新上电才能完成写入过程。</i></p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/03/02/cd0bf85ad32996305dd93129ff6d08f2.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/03/02/cd0bf85ad32996305dd93129ff6d08f2.png" referrerpolicy="no-referrer"><figcaption>stcgal 下载 ihx 文件到单片机</figcaption></figure><h3><br>点亮SSPAI了！</h3><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/03/02/2d07fb041a343a3307433d93d0cdf955.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/03/02/2d07fb041a343a3307433d93d0cdf955.jpg" referrerpolicy="no-referrer"><figcaption>利用单片机点亮 SSPAI</figcaption></figure><p><br>此时我们可以看到开发板上的数码管已经亮起了我派。</p><h2><br>偷懒是第一生产力</h2><p><br>作为一个十足的懒人，我甚至不愿意每次修改程序后都要敲上面两行短的不能再短的命令来进行编译和写入，于是我盘算着用「自动操作」偷个懒。</p><h3><br>新建自动操作</h3><p><br>由于自动操作的「快速操作」，在使用时需要在二级菜单里寻找，使用「应用程序」并把它固定到访达的工具栏或许是更为快捷的方式。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/03/02/554def114c8a8450e6975bd7256fde27.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/03/02/554def114c8a8450e6975bd7256fde27.png" referrerpolicy="no-referrer"><figcaption>新建自动操作</figcaption></figure><h3><br>获取文件路径</h3><p><br>使用「实用工具-拷贝至剪贴板」可以帮助我们快速获取文件路径。 但因为我们在下一步中，需要将使用终端命令「cd」到源文件储存的目录中，所以建议将源文件放置在文件夹中，将文件夹作为自动操作的输入，且这样 sdcc 编译生成的文件都会在这一目录中，不会让文件夹变得乱糟糟。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/03/02/9b5a5c37b9acce1ecc0c54177d7b8ceb.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/03/02/9b5a5c37b9acce1ecc0c54177d7b8ceb.png" referrerpolicy="no-referrer"><figcaption>获取文件路径</figcaption></figure><h3><br>使用 shell 脚本编译并下载</h3><p><br>这里首先给出一个示例，但需要根据实际情况修改。</p><pre class="language-shell"><code>export PATH=/usr/local/bin:$PATH
cd $@
sdcc main.c
/Users/0u0/opt/anaconda3/bin/stcgal -P stc89 -p /dev/tty.wchusbserial1440 main.ihx</code></pre><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/03/02/5c70d5741571843140ef99df166a0485.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/03/02/5c70d5741571843140ef99df166a0485.png" referrerpolicy="no-referrer"><figcaption>设置 Shell 脚本和传递输入</figcaption></figure><h4><br>加载到指定目录</h4><p><br>由于我们之前获取了源文件储存的目录作为本步的输入，所以需要将「传递输入」修改为「作为自变量」，并利用<code>cd $@</code>加载到指定目录，自动操作的 shell 中，利用 <code>$@</code>作为自变量。</p><h4><br>编译文件</h4><p><br>如果直接使用 sdcc 命令，会出现 command not found 的报错。这是因为通过自动操作运行的脚本使用默认路径，通常不包括 /usr/local/bin。所以我们需要添加<code>export PATH=/usr/local/bin:$PATH</code>来保证 sdcc 命令可以正确执行。</p><h4><br>下载到单片机</h4><p><br>如果直接执行 stcgal 命令，同样会出现 command not found 的报错，但 stcgal 并不存放在 /usr/local/bin 的路径下。我们可以使用<code>pip3 show stcgal</code>来找到 stcgal 所存放的路径（用 Hapigo 或者其他工具直接搜索 stcgal 也是一个不错的选择），并直接使用该路径来执行 stcgal。</p><p><br><i>请注意修改 -p 之后的参数为</i><code><i>ls /dev/tty.wchusbserial*</i></code><i>获取到的内容。</i></p><h3><br>大功告成</h3><p><br>保存后，将其拖动到应用程序文件夹即可完成安装，然后使用我派「每日一技」提供的技巧，按住 command 键将其拖拽到 Finder 的工具栏即可快速使用。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/03/02/f2fbe8cb0fedc5072efe97a4d3d87845.gif" data-original="https://cdn.sspai.com/2022/03/02/f2fbe8cb0fedc5072efe97a4d3d87845.gif" referrerpolicy="no-referrer"><figcaption>偷懒现场</figcaption></figure><p> </p><p>这就是我在 macOS 下搭建 51 单片机开发环境的过程，希望我的经验能给有需要的朋友一些帮助，也希望派友们如果有更简单（偷懒）的方法可以在评论区告诉我。谢谢会员群里给我鼓励的编辑和会员朋友们！</p></div><div class="update-details-wrap" data-v-0b37afcb></div><!----></div><div style="border:1px solid transparent;" data-v-0b37afcb></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-0b37afcb><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>13</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>12</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-653" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90%E5%9C%A8%20macOS%20%E4%B8%8B%E6%90%AD%E5%BB%BA%2051%20%E5%8D%95%E7%89%87%E6%9C%BA%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83%E3%80%91%E6%90%AD%E5%BB%BA%E5%8E%9F%E5%9B%A0%E6%9C%AC%E5%AD%A6%E6%9C%9F%E7%9A%84%E3%80%8A%E5%BE%AE%E6%9C%BA%E5%8E%9F%E7%90%86%E4%B8%8E%E5%8D%95%E7%89%87%E6%9C%BA%E6%8A%80%E6%9C%AF%E3%80%8B%E9%9C%80%E8%A6%81%E8%BF%9B%E8%A1%8C%E4%B8%80%E4%BA%9B%E7%AE%80%E5%8D%95%E7%9A%84%E5%8D%95%E7%89%87%E6%9C%BA%E5%BC%80%E5%8F%91%E5%AE%9E%E9%AA%8C%EF%BC%8C%E5%8E%9F%E6%9C%AC%E6%89%93%E7%AE%97%E5%9C%A8ParallelsDesktop%E7%9A%84Windows%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%B8%AD%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=https%3A%2F%2Fcdn.sspai.com%2F2022%2F03%2F02%2Fb5040875dd3777542ca50783633adde4.jpg%3FimageMogr2%2Fauto-orient%2Fquality%2F95%2Fthumbnail%2F!1420x708r%2Fgravity%2FCenter%2Fcrop%2F1420x708%2Finterlace%2F1&appkey=3196502474#" target="_blank"><i class="iconfont iconfont-weibo-simple right-16"></i></a><span><div role="tooltip" id="el-popover-4436" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><span class="el-popover__reference-wrapper"><i class="iconfont iconfont-wechat-simple right-16"></i></span></span><a href="https://twitter.com/share?text=%E3%80%90%E5%9C%A8%20macOS%20%E4%B8%8B%E6%90%AD%E5%BB%BA%2051%20%E5%8D%95%E7%89%87%E6%9C%BA%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83%E3%80%91%E6%90%AD%E5%BB%BA%E5%8E%9F%E5%9B%A0%E6%9C%AC%E5%AD%A6%E6%9C%9F%E7%9A%84%E3%80%8A%E5%BE%AE%E6%9C%BA%E5%8E%9F%E7%90%86%E4%B8%8E%E5%8D%95%E7%89%87%E6%9C%BA%E6%8A%80%E6%9C%AF%E3%80%8B%E9%9C%80%E8%A6%81%E8%BF%9B%E8%A1%8C%E4%B8%80%E4%BA%9B%E7%AE%80%E5%8D%95%E7%9A%84%E5%8D%95%E7%89%87%E6%9C%BA%E5%BC%80%E5%8F%91%E5%AE%9E%E9%AA%8C%EF%BC%8C%E5%8E%9F%E6%9C%AC%E6%89%93%E7%AE%97%E5%9C%A8ParallelsDesktop%E7%9A%84Windows%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%B8%AD%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="iconfont iconfont-twitter-simple right-16"></i></a></div></div><span class="el-popover__reference-wrapper"><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            