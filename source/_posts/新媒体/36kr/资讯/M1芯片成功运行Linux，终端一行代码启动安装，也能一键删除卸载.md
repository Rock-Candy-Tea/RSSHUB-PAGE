
---
title: 'M1芯片成功运行Linux，终端一行代码启动安装，也能一键删除卸载'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220321/v2_8bc8ee1232994fbe9e578cc7def631e7_img_000'
author: 36kr
comments: false
date: Mon, 21 Mar 2022 09:00:46 GMT
thumbnail: 'https://img.36krcdn.com/20220321/v2_8bc8ee1232994fbe9e578cc7def631e7_img_000'
---

<div>   
<p>终于，<strong>M1系列</strong>的Mac可以启动<strong>Linux-macOS双系统</strong>了！‍‍</p> 
<p class="image-wrapper"><img data-img-size-val="1080,647" src="https://img.36krcdn.com/20220321/v2_8bc8ee1232994fbe9e578cc7def631e7_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">‍</p> 
<p>Asahi Linux在官方推特上宣布：</p> 
<p>首个<strong>原生支持</strong>M1系列Mac的Linux<a class="project-link" data-id="8712" data-name="测试" data-logo="https://img.36krcdn.com/20220318/v2_d188db412f2e4db89c6424314ac39971_img_jpg" data-refer-type="2" href="https://36kr.com/projectDetails/8712" target="_blank">测试</a>版现在已发布，面向所有人开放。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,704" src="https://img.36krcdn.com/20220321/v2_d2aa8a7de8a6493395813be4de8483d9_img_000" referrerpolicy="no-referrer"></p> 
<p>大家只需在终端输入一行代码即可启动安装：</p> 
<blockquote> 
 <p><strong>curl https://alx.sh | sh</strong></p> 
</blockquote> 
<p>有迫不及待的网友已经上手，纷纷晒出自己的成功界面：</p> 
<p class="image-wrapper"><img data-img-size-val="1080,926" src="https://img.36krcdn.com/20220321/v2_70255b0143554631af405ae004842fdd_img_000" referrerpolicy="no-referrer"></p> 
<p class="image-wrapper"><img data-img-size-val="1080,720" src="https://img.36krcdn.com/20220321/v2_0ca38c255e694dd59468919c2d874055_img_000" referrerpolicy="no-referrer"></p> 
<p>这其中还不乏“体验良好”的声音：</p> 
<blockquote> 
 <p><strong>流畅度令人惊讶</strong>！YouTube完全可以正常播放。</p> 
</blockquote> 
<p class="image-wrapper"><img data-img-size-val="1080,991" src="https://img.36krcdn.com/20220321/v2_ae8b1d769a614e0186b547293eb65484_img_000" referrerpolicy="no-referrer"></p> 
<p>代码编辑器Emacs和<a class="project-link" data-id="3968996" data-name="谷歌" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968996" target="_blank">谷歌</a>浏览器也完全没问题！</p> 
<p class="image-wrapper"><img data-img-size-val="1080,675" src="https://img.36krcdn.com/20220321/v2_5e16ded10e144ad3ac452bb339cc4219_img_000" referrerpolicy="no-referrer"></p> 
<p>Asahi Linux曾表示，不仅仅要让Linux在M1上跑起来，最终目标更是将它打磨到可以作为日常操作系统使用的程度。</p> 
<p>它什么来头？</p> 
<h2><strong>历时14个月，专为Apple Sillion打造</strong></h2> 
<p>Asahi Linux其实是一个专门<strong>为Apple Silicon系列</strong>Mac电脑做Linux系统移植的项目，还受到过<strong>“Linux之父”</strong>Linus Torvalds的关注。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,608" src="https://img.36krcdn.com/20220321/v2_e2d7166a26824331a7e14ed095009c2b_img_000" referrerpolicy="no-referrer"></p> 
<p>Asahi Linux由<strong>程序员Hector Martin</strong>（@marcan42）于2020年末众筹发起。</p> 
<p>Hector Martin是一位安全黑客，也是资深的操作系统移植专家，曾为各种设备提供非官方的开源支持来移植Linux系统，包括任天堂Wii、索尼PS系列游戏主机等。</p> 
<p>2021年1月份，Asahi Linux项目众筹完毕，正式启动。</p> 
<p>Asahi这个名字也不是随便起的，正是日语对McIntosh这个苹果品种的称呼。</p> 
<p>当年苹果公司注册商标时候，因为McIntosh已经被一家音响品牌先占用了，所以加了个a变成Macintosh，也就是今天Mac的全称。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,707" src="https://img.36krcdn.com/20220321/v2_675f47a87bc741308f128a0a587c40cf_img_000" referrerpolicy="no-referrer"></p> 
<p>由于Apple Sillion平台并未公开文档，Hector Martin需要对其GPU架构进行<strong>逆向工程</strong>。</p> 
<p>而只要开发者没有从macOS中提取代码建立Linux支持，苹果就允许在不越狱的情况下，在Apple Sillion Mac上启动<strong>无签名或定制内核</strong>。</p> 
<p><strong>历经14个月</strong>，Asahi Linux的第一个公开测试版终于得以成功问世。</p> 
<h2><strong>也可“一键卸载”</strong></h2> 
<p>现在，只要你用的是M1、M1 Pro或M1 Max的苹果电脑（除了Mac Studio），且macOS在12.3及以上，再预留出至少53GB的磁盘空间，即可“一把尝鲜”。</p> 
<p>其中53GB的内存要求指的是安装Asahi Linux Desktop版本，15GB给它，另外38GB预留给macOS进行系统更新。</p> 
<p>Asahi Linux此次一共<strong>提供三个可选版本</strong>：</p> 
<p>Asahi Linux Desktop桌面版，配有完整的Plasma桌面和所有基本软件包。还包括一个图形化的首次启动设置向导，方便用户更改配置或创建第一个账户。</p> 
<p>Asahi Linux Minimal迷你版，一个普通的Arch Linux ARM环境，只有最低限度的支持包。“Arch用户会有宾至如归的感觉！”</p> 
<p>以及仅限UEFI（统一可扩展固件接口）环境的版本，有了它，你就可以通过USB驱动器启动操作系统安装程序，安装任何你想要的东西。</p> 
<p>Asahi Linux支持的具体功能如下：</p> 
<p class="image-wrapper"><img data-img-size-val="984,392" src="https://img.36krcdn.com/20220321/v2_a15459b746be4f4f8686948bfe94fdba_img_000" referrerpolicy="no-referrer"></p> 
<p>其中还包括仅限M1的耳机插孔和仅限Mac Mini的HDMI输出支持。</p> 
<p>现在还<strong>不支持GPU加速</strong>、DisplayPort接口、神经引擎以及Touch Bar等功能。</p> 
<p class="image-wrapper"><img data-img-size-val="546,714" src="https://img.36krcdn.com/20220321/v2_a3905e6434f94c60bda7d17c8119c4fd_img_000" referrerpolicy="no-referrer"></p> 
<p>值得一提的是，这个系统不仅可以一行代码启动安装，也可以“一键删除”：</p> 
<p>安装程序本身没有提供卸载选项，通过<strong>删除系统创建的分区</strong>（比如diskutil命令）<strong>完成卸载</strong>。</p> 
<p>此外，作者还在博客中提醒道：</p> 
<p>1、由于还没开发出直接从该Linux更新系统固件的机制，目前的安装程序还不支持替换macOS，因此双系统的保留很有必要。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,810" src="https://img.36krcdn.com/20220321/v2_6f3c9213c1234c458eab140a24b301eb_img_000" referrerpolicy="no-referrer"></p> 
<p>2、大家可以安装任意数量的macOS和Linux，彼此之间不会互相干扰。</p> 
<p>3、<strong>安装程序也很安全</strong>。所有磁盘管理操作都是在后台使用本机macOS工具（diskutil）执行，不会做任何真正危险的操作。</p> 
<p>不过除非你自己有明显的操作失误（比如wipe disk），还是可能导致数据丢失。</p> 
<p>4、同时欢迎其他有兴趣支持Apple Silicon的Linux发行版作者联系团队，以提供更多版本。</p> 
<p>总体来说，由于Asahi Linux现在还是个很早期的测试版本，主要针对的也是开发者和资深用户，部分功能还略显粗糙。</p> 
<p>但Martin推荐所有人都来试试。</p> 
<p>——安装指导已尽量做到了“不言自明”，基本“傻瓜式”：</p> 
<p class="image-wrapper"><img data-img-size-val="1080,739" src="https://img.36krcdn.com/20220321/v2_95e3e8e32e9a410fbd4081dbe2bce8d2_img_000" referrerpolicy="no-referrer"></p> 
<p>Martin本人亲自示范的视频教程也可以在Nobel Tech的YouTube频道找到：</p> 
<p class="image-wrapper"><img data-img-size-val="1080,511" src="https://img.36krcdn.com/20220321/v2_dd95cfcd55cc4257a160449dc52bca3e_img_000" referrerpolicy="no-referrer"></p> 
<p>有兴趣的读者快去试试吧。</p> 
<p>Asahi Linux官博、官推：</p> 
<p>https://asahilinux.org/2022/03/asahi-linux-alpha-release/</p> 
<p>https://twitter.com/AsahiLinux/status/1504969725771923456</p> 
<p>视频教程：https://www.youtube.com/watch?v=B9uJxvdVFBE</p> 
<p class="editor-note">本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer nofollow" href="https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247616391&idx=2&sn=4e92b7a4cedc3797801d4db3d638c3e7&chksm=e8d1b0f5dfa639e3984337f35c585dbdde03c949a12b242a53cd8f33fba7ae0eed3539264f98#rd">“量子位”（ID:QbitAI）</a>，作者：关注前沿科技，36氪经授权发布。</p>  
</div>
            