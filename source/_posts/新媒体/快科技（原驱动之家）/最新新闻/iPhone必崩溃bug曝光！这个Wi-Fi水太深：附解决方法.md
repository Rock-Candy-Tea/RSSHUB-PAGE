
---
title: 'iPhone必崩溃bug曝光！这个Wi-Fi水太深：附解决方法'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210620/00e23e0ebf20470183596fdbb22622aa.gif'
author: 快科技（原驱动之家）
comments: false
date: Sun, 20 Jun 2021 13:12:04 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210620/00e23e0ebf20470183596fdbb22622aa.gif'
---

<div>   
<p>iPhone又出现漏洞了，这个漏洞能让你手机一连WiFi就崩溃。</p>
<p>如果有人把WiFi名称（SSID）设置成一串特殊字符，那么你要小心了，因为你一旦尝试去连接这个WiFi，你的iPhone就会“中招”。</p>
<p>就像下面这样，从此你的iPhone再也连不上WiFi了，即使手动打开也会自动关闭：</p>
<p align="center"><img alt="iPhone必崩溃bug曝光！这个Wi-Fi水太深：附解决方法" h="1080" src="https://img1.mydrivers.com/img/20210620/00e23e0ebf20470183596fdbb22622aa.gif" style="border: black 1px solid;" w="498" referrerpolicy="no-referrer"></p>
<p>而且就算重启iPhone也不管用，必须还原手机的网络设置才能让WiFi功能恢复正常。</p>
<p><strong>仅iPhone受影响</strong></p>
<p>发现这一漏洞的是一位叫做Carl Schou的安全工程师，他把自己家的WiFi设置成了以下名称：%p%s%s%s%s%n</p>
<p style="text-align: center"><img alt="iPhone必崩溃bug曝光！这个Wi-Fi水太深：附解决方法" h="1000" src="https://img1.mydrivers.com/img/20210620/12e1454b-fa59-472a-91e9-b9e8cb3629d6.png" style="border: black 1px solid" w="514" referrerpolicy="no-referrer"></p>
<p>（温馨提示：千万不要自己手贱尝试，也不要去危害其他iPhone用户。）</p>
<p>之后他就发现iPhone的WiFi功能彻底崩溃了。</p>
<p>每次他尝试再次开启WiFi时，系统都会迅速关闭，即便他重新启动设备，或把家里的WiFi改成一个正常的名称也不行。</p>
<p>Carl首先是在他iOS版本14.4.2的iPhone XS上测试发现的，之后他又在最新的14.6系统上进行了同样的测试，漏洞依旧存在。</p>
<p>Carl首先在Twitter上反馈了这一问题，其他多位网友看到他的描述后也复现了该漏洞。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210620/b45fccc4-0c75-471e-b5cb-c554dc0d0d26.png" target="_blank"><img alt="iPhone必崩溃bug曝光！这个Wi-Fi水太深：附解决方法" h="190" src="https://img1.mydrivers.com/img/20210620/Sb45fccc4-0c75-471e-b5cb-c554dc0d0d26.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>而且据这位网友反馈，问题不仅是WiFi不能用，连AirDrop也打不开了。</p>
<p align="center"><img alt="iPhone必崩溃bug曝光！这个Wi-Fi水太深：附解决方法" h="1387" src="https://img1.mydrivers.com/img/20210620/02f970295c674e7494927ee04be5af24.gif" style="border: 1px solid black; height: 1300px; width: 600px;" w="640" referrerpolicy="no-referrer"></p>
<p>当然，这个问题也不是完全不能修复，具体的修复方法我们后面再提。</p>
<p>如果你是Android用户，则完全不必担心，因为有人尝试用Android手机连接同样名称的WiFi，问题没有出现。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210620/dc72fad6-8ee2-4e63-b901-fd5f6c2184b0.png" target="_blank"><img alt="iPhone必崩溃bug曝光！这个Wi-Fi水太深：附解决方法" h="431" src="https://img1.mydrivers.com/img/20210620/Sdc72fad6-8ee2-4e63-b901-fd5f6c2184b0.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>另外，量子位亲测，该WiFi名称对Mac无影响。看来这个漏洞应该是iPhone独有的。</p>
<p>虽然WiFi也不是不能靠重置解决，但一些网友认为，这个“可怕的”漏洞应该引起高度的重视。</p>
<p>因为像这样的漏洞可能会被黑客利用，比如在公共场合设置在流氓WiFi，就可以让附近所有iPhone崩溃。</p>
<p>而且这很可能是一个特权提升漏洞，会导致溢出错误，从而破坏了plist。（plist是苹果用来储存用户设置的文件）。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210620/89dd2311-9c18-4a68-a735-201f6f13430f.png" target="_blank"><img alt="iPhone必崩溃bug曝光！这个Wi-Fi水太深：附解决方法" h="165" src="https://img1.mydrivers.com/img/20210620/S89dd2311-9c18-4a68-a735-201f6f13430f.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>一串字符为何让iPhone崩溃</strong></p>
<p>看到Schou推文的其他安全工程师认为，是iPhone对WiFi名称的解析问题导致了这个错误。</p>
<p>问题就处在名称里的“%”符号上。</p>
<p>如果你学会C、C++语言，那么应该对这个符号有所了解：%叫做“格式化字符串”（format string），用来处理特殊的变量名或命令。</p>
<p>比如“%3d”就是将变量以3位整型数方式输出。</p>
<p>再回到“%p%s%s%s%s%n”这串特殊字符，%p代表输出指针，%s代表输出字符串，%n的含义稍微复杂一些，代表输出%n之前的字符长度。</p>
<p>比如下面这串代码：</p>
<p>printf(“geeks for %ngeeks”, &c);输出结果并不显示%n，只是</p>
<p>geeks for geeks但是这行代码会将%n之前的字符数统计下来，存放在变量c中。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210620/16ca5e9c-eca3-4d5a-a9f2-dc748211077c.png" target="_blank"><img alt="iPhone必崩溃bug曝光！这个Wi-Fi水太深：附解决方法" h="368" src="https://img1.mydrivers.com/img/20210620/S16ca5e9c-eca3-4d5a-a9f2-dc748211077c.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>如果我们再加一句printf(“%d”, c);就会发现输出结果为10。（空格也算一个字符）</p>
<p>iPhone会将未经过滤的Wi-Fi名称（SSID）传递给一些执行格式化字符串的内部库，这会导致任意的内存写入和缓冲区溢出，从而破坏内存数据。而iOS看门狗会终止该进程，导致Wi-Fi禁用。</p>
<p>所以iPhone没有把“%p%s%s%s%s%n”理解成普通文字，而是当成了特殊字符串来处理。iPhone的错误日志也记录下了这一事件。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210620/8edea6ee-35a8-4d13-83c4-93ff983d9d3e.png" target="_blank"><img alt="iPhone必崩溃bug曝光！这个Wi-Fi水太深：附解决方法" h="593" src="https://img1.mydrivers.com/img/20210620/S8edea6ee-35a8-4d13-83c4-93ff983d9d3e.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>至于为何要把WiFi改成这个奇怪的名字，Carl说，他的所有设备都以格式化字符串命名，以此来发现那些有问题的设备。</p>
<p>其实，这也不是iPhone第一次遭遇特殊字符串的攻击。</p>
<p>之前最出名的莫过于2018年的“死亡短信”，只要给iPhone发送一段有特殊泰卢固语字符的短信，用户就再也无法打开短信App，因为只要一点击，iPhone就会自动重启。</p>
<p>iPhone微信也会受到此类攻击的影响。</p>
<p>之后iPhone在iOS 11.3修复了此漏洞，但类似的字符串攻击方式频频出现，几乎每隔一段时间就会出现，防不胜防。</p>
<p><strong>解决方法</strong></p>
<p>这个bug尽管用重启iPhone的方式不能，但也不至于让你的手机彻底坏掉，解决方法并不复杂：</p>
<p>打开iPhone上的“设置”，选择“通用”</p>
<p>进入最下方的“还原”选项</p>
<p>选择“还原网络设置”，输入你的手机密码</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210620/f2a69fd9-53cd-4579-8d4a-a98d6d696f79.png" target="_blank"><img alt="iPhone必崩溃bug曝光！这个Wi-Fi水太深：附解决方法" h="381" src="https://img1.mydrivers.com/img/20210620/Sf2a69fd9-53cd-4579-8d4a-a98d6d696f79.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>等网络还原完成后，你的iPhone就会恢复正常。不用担心手机资料丢失，此操作只会让iPhone“忘记”之前保存的WiFi密码，其他不受影响。</p>
<p>如果你今后看到WiFi名称里有“%”号一定要多加小心了，它可能是恶作剧，也可能是黑客的阴谋。</p>
<p>希望苹果能在下次iOS更新中修复这个漏洞吧。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210620/8e205b1aea12447bb2b9ed3d96520637.jpg" target="_blank"><img alt="iPhone必崩溃bug曝光！这个Wi-Fi水太深：附解决方法" h="399" src="https://img1.mydrivers.com/img/20210620/s_8e205b1aea12447bb2b9ed3d96520637.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/pingguo.htm"><i>#</i>苹果</a><a href="https://news.mydrivers.com/tag/iphoneshouji.htm"><i>#</i>iPhone手机</a><a href="https://news.mydrivers.com/tag/wi-fi.htm"><i>#</i>Wi-Fi</a></p>
<p class="url">
     <span>原文链接：<a href="https://mp.weixin.qq.com/s/VHjdWAdXPQqXA8_OxFZ34w">量子位</a></span>
<span>责任编辑：随心</span>
</p>
        
</div>
            