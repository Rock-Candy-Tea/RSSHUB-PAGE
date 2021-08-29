
---
title: '新款 Mac mini 体验：苹果 M1 芯片性能及兼容性完全测试'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3803f533555f4823b0fdae839ec0faff~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 00:13:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3803f533555f4823b0fdae839ec0faff~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>iOS开发者眼中的M1</strong></p>
<p>作为一个常年混迹在数码圈的资深iOS开发者，也用过不少新奇的、有争议的电子产品，就是通常所说的。</p>
<p>第一个吃螃蟹的人，对于M1的发布，也是心痒痒很久了，但毕竟是吃饭的家伙，这次我没有盲目入手，但随着家里的台式越来越磨练我的心志，以及工作的需要。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3803f533555f4823b0fdae839ec0faff~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>狠了狠心，抛弃了陪伴我五年的21.5 iMac（主要因为机械盘慢慢的越来越卡，受不了），掏空我那仅有的积蓄，找熟人拿了台M1的Mac Mini。</p>
<p>距离M1芯片发布刚好半年，观望得也差不多了，没曝出啥大毛病，无非是芯片从x86架构换成了ARM，我就拿来耍一耍，一探究竟。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efb706ca43f54fd684bfcf94f18d8a8b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>到手第一眼觉得还是比想象中要大一圈的，没有在实体店看到过，一直以为真的很Mini，但是想放在我的饭盒里带着走还需要再瘦一点。</p>
<p>基本上不背着包是没法随身携带的，而且上下面菱角分明，虽然好看，但是稍微磕碰一下就肯定有印子，放在桌上我也不敢随意搬动，加个护套还是有必要的。</p>
<h3 data-id="heading-0">性能测试</h3>
<p>硬件配置不进行赘述，M1都一样，除了对性能影响可忽略的固态盘容量和可选的内存大小，一查便知。首次启动，经过一系列网络设置、账号设置、键盘鼠标、个性化设置等等之后，很快进入了桌面。</p>
<p>作为一个优秀的iOS开发者，第一步就是安装Xcode，下载完成后的安装速度并没有觉得很快，也进行了半个小时左右。</p>
<p>然后我打开了系统偏好设置中的软件更新，检查有无新版本，发现可升级到11.4（出厂11.3），于是果断升级，下载接近完成时，突然弹窗提示安装失败（安装所选更新时发生错误），屡试不爽，查原因。</p>
<p>有人说这是由于Mac SIP系统完整性保护机制导致的，解决也比较简单，但是需要重启，我正在安装软件，于是乎暂时搁置。</p>
<p>过了几个小时后屏幕右上角突然弹出安装更新提示，点击安装就直接开始安装了，怀疑是系统已经在后台自动下载更新，手动更新优先级更低导致的。</p>
<p>补充：两个月后更新系统版本11.5.1，下载快要结束的时候，又出现了另一个问题，提示下载失败，好几天都如此，我这暴脾气，直接关了自动更新（后来用家里的网络更新成功，应该是公司的网络限制了）。</p>
<p>然后安装我需要的软件，因为我的资料数据都存在了百度网盘，首先在官网下载并安装完百度网盘，打开的时候弹窗提示需要安装Rosetta插件来将基于Intel芯片的功能适配M1芯片。</p>
<p>点击安装输入开机密码，一会儿就好了，然后再次打开百度网盘，图标在程序坞里弹跳了好几秒，才打开登录界面，退出后再次打开就是正常的启动速度了。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbc724f1ac504de5952acbe61fa251fd~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fb91529de1243d6a1d471e1bc9f388f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">兼容性测试</h3>
<p>这里就是M1最大的一个看点，关于兼容性问题，众所周知，x86是复杂指令集，arm是精简指令集，针对x86开发的app本来是不支持在arm上直接运行的，这就体现了苹果的厉害之处。</p>
<p>苹果通过一个“小插件”，直接把x86转译为支持arm运行的程序，并且，使用是无感的！很多人普遍担心Rosetta2的转译效率，从我的实际体验来看，你压根就不能从启动速度和使用过程判断到底有没有经过转译。</p>
<p>可能有些人听过Rosetta，而M1中使用的Rosetta实际上是Rosetta2，简单理解也就是第二代的意思，那么第一代呢？苹果在06年将Mac从PowerPc架构转为Intel的x86的时候，就是用的Rosetta来转译的！从名字看就知道苹果有着非常优秀的传承思想。</p>
<p>关于 Rosetta，我也去查了一下，苹果官方文档是这么说的：</p>
<p>每当您使用专为配备 Intel 处理器的 Mac 电脑构建的 App 时，Rosetta 2 都会在后台运行。Rosetta 会自动转化 App 以便与 Apple 芯片搭配使用。</p>
<p>在大多数情况下，需要 Rosetta 的 App 的性能不会出现任何差异。</p>
<p>您的哪些 App 需要 Rosetta？</p>
<p>您可以使用“显示简介”来识别需要 Rosetta 或可以使用 Rosetta的 App：</p>
<p>在“访达”中选择相应 App。</p>
<p>从菜单栏的“文件”菜单中，选取“显示简介”。</p>
<p>查看标有“种类”字样的信息：</p>
<p>应用程序 (Intel) 表示 App 仅支持 Intel 处理器，并且需要 Rosetta 才能在任何搭载 Apple 芯片的 Mac 上运行。</p>
<p>应用程序（通用）表示 App 同时支持 Apple 芯片和 Intel 处理器，并且在默认情况下使用 Apple 芯片。</p>
<p>通用 App 的“简介”窗口包含“使用 Rosetta 打开”设置。这项设置可以让电子邮件 App、网页浏览器和其他 App 使用尚未更新以支持 Apple 芯片的附加项。如果某个 App 无法识别插件、扩展或其他附加项，请退出相应 App，选择这项设置，然后再试一次。</p>
<p>我在测试过程中发现，种类为“应用程序（通用）”的App，都有“使用Rosetta打开”的勾选项，除了系统偏好设置.app，我经常使用的App中也只发现了网易有道词典. app和Google Chrome.app种类为“应用程序（通用）”。</p>
<p>其他比如企业微信、Office、XMind、TeamViewer等等，都是“应用程序 (Intel)”，这种类型的app就没有“使用Rosetta打开”的勾选项了，默认会使用Rosetta打开，如下图。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b3e362786f4433ca9dc4a001c3bb729~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0b99914c6d642a6842fd56059f4dc46~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c107dff42b641d18ae6feef3a8bc462~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然，最直观的方式你可以在管理存储空间的窗口来查看，种类一栏中“通用/Intel”一目了然。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa859d1f7818493f8a1ea31daebf9db7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>安装步骤要点</strong></p>
<p>另外，如果系统没有自动提示你安装Rosetta，或者某些App出现闪退，可以终端输入/usr/sbin/softwareupdate --install-rosetta --agree-to-license，完成后在闪退的App简介窗口勾选“使用Rosetta打开”。</p>
<p>然后我需要安装辅助开发工具cocoapods，老套路，我必须来依次安装Homebrew、rvm、ruby、cocoapods，操作过程如下：</p>
<p>1、终端输入</p>
<p>/bin/bash-c"$(curl-fsSL <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fcunkai%2FHomebrewCN%2Fraw%2Fmaster%2FHomebrew.sh)%2522%25E5%259B%259E%25E8%25BD%25A6%25EF%25BC%258C%25E6%258C%2589%25E6%258F%2590%25E7%25A4%25BA%25E7%259A%2584%25E6%2593%258D%25E4%25BD%259C%25E6%25AD%25A5%25E9%25AA%25A4%25E4%25B8%2580%25E6%25AD%25A5%25E6%25AD%25A5%25E6%2589%25A7%25E8%25A1%258C%25EF%25BC%258C%25E5%25AE%2589%25E8%25A3%2585%25E5%25AE%258C%25E6%2588%2590%25E5%2590%258Ebrew" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)%22%E5%9B%9E%E8%BD%A6%EF%BC%8C%E6%8C%89%E6%8F%90%E7%A4%BA%E7%9A%84%E6%93%8D%E4%BD%9C%E6%AD%A5%E9%AA%A4%E4%B8%80%E6%AD%A5%E6%AD%A5%E6%89%A7%E8%A1%8C%EF%BC%8C%E5%AE%89%E8%A3%85%E5%AE%8C%E6%88%90%E5%90%8Ebrew" ref="nofollow noopener noreferrer">gitee.com/cunkai/Home…</a> -v查看是否成功；</p>
<p>2、从github上下载rvm：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frvm%2Frvm%25EF%25BC%258Csudo" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/rvm/rvm%EF%BC%8Csudo" ref="nofollow noopener noreferrer">github.com/rvm/rvm，sud…</a> spctl --master-disable开启允许从任何来源下载应用的选项并选中，然后，双击运行/bin/rvm-installer快捷方式进行离线安装。安装完成后配置到.bash_profile：</p>
<p>export PATH="/Users/zions/.rvm/bin:$PATH"；</p>
<p>3、输入rvm list know查看ruby版本列表，最新的是3.0.1，输入rvm install 3.0.1安装最新的ruby版本，安装完成后rvm list查看是否存在。</p>
<p>没问题，然后输入gem sources -l查看ruby的gem源，国外源就不要用了，浪费宝贵的工作时间，还经常失败，输入gem sources --remove <a href="https://link.juejin.cn/?target=https%3A%2F%2Frubygems.org%2F%25E5%2588%25A0%25E9%2599%25A4%25E5%259B%25BD%25E5%25A4%2596%25E6%25BA%2590%25EF%25BC%258C%25E7%2584%25B6%25E5%2590%258E%25E8%25BE%2593%25E5%2585%25A5gem" target="_blank" rel="nofollow noopener noreferrer" title="https://rubygems.org/%E5%88%A0%E9%99%A4%E5%9B%BD%E5%A4%96%E6%BA%90%EF%BC%8C%E7%84%B6%E5%90%8E%E8%BE%93%E5%85%A5gem" ref="nofollow noopener noreferrer">rubygems.org/删除国外源，然后输入g…</a> sources --add <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgems.ruby-china.com%25E6%25B7%25BB%25E5%258A%25A0%25E5%259B%25BD%25E5%2586%2585%25E6%25BA%2590%25EF%25BC%258C%25E6%258E%25A5%25E7%259D%2580gem" target="_blank" rel="nofollow noopener noreferrer" title="https://gems.ruby-china.com%E6%B7%BB%E5%8A%A0%E5%9B%BD%E5%86%85%E6%BA%90%EF%BC%8C%E6%8E%A5%E7%9D%80gem" ref="nofollow noopener noreferrer">gems.ruby-china.com添加国内源，接着gem</a> sources -l查看是否替换成功。</p>
<p>4、输入sudo gem install cocoapods -n /usr/local/bin进行cocoapods安装，等待10分钟左右完成，pod –version查看是否安装成功，pod repo list查看repos发现没有。</p>
<p>pod repo add master <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FCocoaPods%2FSpecs.git%25E6%25B7%25BB%25E5%258A%25A0repos%25EF%25BC%258Cpod" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/CocoaPods/Specs.git%E6%B7%BB%E5%8A%A0repos%EF%BC%8Cpod" ref="nofollow noopener noreferrer">github.com/CocoaPods/S…</a> search AF自动进行pod setup，提示Setup completed后搜索结果成功出现。</p>
<p>自此，cocoapods成功安装，M1并没有不能使用cocoapods等这些工具，过程也没有多艰难，期间在线安装rvm时遇到问题。</p>
<p>有人说M1芯片不支持rvm，于是我采用了离线安装的方式，并且打开终端.app的简介，勾选了“使用Rosetta打开”，如图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2227af76e6574e66917e4d7add0e5a4e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我在多次使用pod install的时候，发现有些三方框架是会报错的，同样也要先勾选终端的“使用Rosetta打开”，方可正常install，在我的经验来看，这个勾选项基本勾上之后就不要取消了，否则有时候忘记勾选出现一些莫名其妙的问题会卡好久。</p>
<p>包括使用Xcode的时候，从旧Mac上拷贝过来的工程也会有一些关于芯片的问题，会报错无法运行，也建议把Xcode的“使用Rosetta打开”勾选上，当然，一个在M1上从零开始的新项目，就还是不要勾了，毕竟还是会影响性能的。</p>
<p>接下来最炸裂的变化来了，App Store中可下载安装iOS App！感觉不是一般的神奇，当然，能下载的前提是，开发者在上架iOS app的时候，勾选上架Mac App Store。</p>
<p>当然，没有支持Mac App Store的iOS app，也有办法来安装，这里不过多解释了，比如百度网盘和微博的iPad版本可下载、QQ音乐的iPhone版本可下载，</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d44442ad94c14aa2841f51597f7f8bf2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>微信和一些火爆的大型手游就不行，相信以后越来越多的主流app会支持M1的Mac，用起来就跟iPhone或者iPad一模一样，有M1的一定要试一试。</p>
<p>然后扯点其他的，苹果M1系列PC产品的上市，一种新的接口类型随之出现了，就是USB4，Mac Mini配备了两个USB4接口，在接口形态上，USB4统一采用USB Type-C形态，这里可能会有点懵，USB4是一种传输标准、一个协议规范。</p>
<p>它能够达到40Gbps的理论速度，而Type-C是一个硬件层面的形态，目前几乎所有的主流智能手机都使用Type-C形态的接口来进行充电，从USB4开始，往后发展可能全都会使用Type-C这种形态的接口，因为方便好用，插入的时候不分正反。</p>
<p>然后，Mac Mini的这两个USB4接口兼容了苹果之前主推的雷雳接口，也就是说，支持Thunderbolt协议的设备可以直接插这两个USB4接口，不太明白的话就可以把他们看成是一个东西，这里不过多拓展，网上资料更详细。</p>
<p>娱乐及办公</p>
<p>娱乐方面，首先音质的话嘛，只能说聊胜于无吧，就跟十几年前的功能机时代的手机喇叭一样的感觉，真的不能找到任何一个角度来夸一下。</p>
<p>如果是居家用，配一套音响是必不可少的，外接最多支持连接两台显示器，这个用起来还是挺方便的。</p>
<p>我经常两台，一台副屏，没出过什么问题，然后由于官网对于M1的8核图形处理器是否支持高刷没有任何说明，我特意去测验了一下，使用的是冠捷34英寸144Hz高刷曲面带鱼屏。</p>
<p>可以选最高100Hz刷新率，所以M1集成的图形处理器是支持高刷无疑的，达不到144Hz我怀疑是因为我使用的连接线是HDMI，如果用USB4应该就没问题。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60c9b4c215ce4b7d96a9165e00e28b2f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>游戏的话，由于我沉浸于工作也没时间去尝试，我的老Mac由于是机械硬盘，跑星际二会比较卡，特效全关才不影响游戏体验，美服LOL能流畅运行。</p>
<p>另外War Thunder也略卡，画面明显有跳帧，但是也能玩，这个M1的话，我有时间再去试一试，如果只是想玩LOL等腾讯系游戏，START拿走不谢。</p>
<p>腾讯的云游戏平台，不需要安装游戏客户端，不需要每次等很久的版本更新，跟本机硬件好坏没啥关系，绑定WeGame登录即玩。</p>
<p>唯一的缺点就是画面清晰度，就类似于看视频，网速不好的话，画面糊得根本没法放技能。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61514dde9a2a40fc97da9e79b3f0d5d1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>还有一点，有些人买Mac第一件事就是装双系统，Windows可能对绝大部分人来说使用起来更顺手，也可以玩很多游戏，所以M1可能让大家失望了。</p>
<p>M1暂不支持安装Windows，没法使用启动转换 Boot Camp来装双系统（需要微软授权ARM版Windows系统给苹果等等一系列阻碍）。</p>
<p>打开Boot Camp直接提示不能用，但对于实在需要使用Windows的人来说，还可以通过虚拟机来实现，重度Windows使用者就没必要买M1了。</p>
<p>还是支持支持咱的民族企业吧（华为、小米的中高端本本都做的不错），通过虚拟机安装Windows网上很多教程，我暂时也没时间折腾，就没去尝试。</p>
<p>还有一个看点就是M1包含神经网络引擎，这个东西最早是在A11芯片中出现的，由于我暂时涉及不到机器学习，也就没去测验这一块。</p>
<p>需要另外提一句的是，开/关机速度，是真的快，因为需要外接显示器，所以会导致信号有延迟，按下开关后亮屏并没有觉得很快，但是进度条一出现，唰就过去了。</p>
<p>然后输入密码进入桌面，整个过程都是秒级，就跟有点卡顿的安卓机亮屏的感觉一样，虽然说x86的也很快，但是但凡一对比，差距就一目了然。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6a4620e30d6486e88f58a0d8506612e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3eb0ad3a52e145a2bcb7223fe7432151~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>记录：7月26我在写demo的时候发现，M1芯片竟然不能支持关键字IB_DESIGNABLE，无法在StoryBoard上看到效果，并且还报了一个错，却没有具体的错误信息，demo工程在同事的Intel本上一切正常。</p>
<p>于是我将Xcode勾选了“使用Rosetta打开”，重启Xcode，这个时候有了错误信息如下图，想了各种办法都无济于事，虽然不影响编译运行和在模拟器上的效果。</p>
<p>但就是解决不了这个问题，最后放弃了，觉得目前应该无解，也可能是我姿势不对，有知道怎么解决的可以告诉我一下，感激。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/612b530a8146455daa18f0e75bea372a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>8月5我用StoryBoard拉了一个tableView，模拟器运行，滑动的时候失去了Bounce On Scroll效果，松手即停，并且快速滑动的时候，效果也不对，会很快的弹跳一下，同样的，我用scrollView一试，也一样，真机没有问题。</p>
<p>网上也有同学有一样的情况，我猜测是转译导致的，果然，取消勾选“使用Rosetta打开”之后，模拟器运行就没有任何问题，大概率是转译之后没有适配好模拟器导致的，静待苹果修复就好。</p>
<h3 data-id="heading-2">总结</h3>
<p>从iOS开发者的角度来说，买M1作为主力开发是绝对没问题的，速度快的不像话，目前遇到的小issue都不至于影响功能需求开发甚至是项目进度，并且，Xcode作为苹果自家的软件，往后也一定会修复这些问题。</p>
<p>使用体验只会越来越好，而且我觉得在使用过程中遇到这样或那样的情况其实也挺有意思的，当然，前提是你是一个喜欢接受挑战的人，如果你追求稳定，追求一板一眼，那intel可能更适合你。</p></div>  
</div>
            