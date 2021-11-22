
---
title: '继承Win10缺点！教你关闭Win11烦人的网络搜索'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211122/e75cca969e3341fda180c94d810e5b35.gif'
author: 快科技（原驱动之家）
comments: false
date: Mon, 22 Nov 2021 06:32:06 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211122/e75cca969e3341fda180c94d810e5b35.gif'
---

<div>   
<p>从Win10开始，微软就在系统搜索中引入了网络内容搜索。</p>
<p>然而，这个特性却并不很受用户欢迎。当你想在电脑当中搜东西的时候，<span style="color:#ff0000;"><strong>弹出来的可能是来自Bing的无用信息，大大降低了搜索效率。</strong></span></p>
<p>Win11对系统进行了大刀阔斧的修改，但很遗憾的是，<strong>Win10烦人的网络搜索，在Win11中被一并继承了下来。</strong></p>
<p align="center"><img alt="继承Win10缺点！教你关闭Win11烦人的网络搜索" h="541" src="https://img1.mydrivers.com/img/20211122/e75cca969e3341fda180c94d810e5b35.gif" style="border: 1px solid black; width: 600px;" w="700" referrerpolicy="no-referrer"></p>
<p>而与此同时，Win11还强制锁定搜索出来的网络结果使用“microsoft-edge://”协议，而且无法修改，<strong>这意味着即使你设置了其他浏览器为默认，还是会强制使用Edge浏览器打开。</strong></p>
<p>不爽这个设定，怎么办？今天，就来教你要如何关闭Win11的网络搜索。</p>
<p>首先，我们需要打开注册表。在Windows搜索中，<span style="color:#ff0000;"><strong>直接搜索注册表，开启即可。</strong></span></p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211122/4f36d3de-6178-4f7e-b62c-7a96b1ae92a7.png" target="_blank"><img alt="继承Win10缺点！教你关闭Win11烦人的网络搜索" h="428" src="https://img1.mydrivers.com/img/20211122/S4f36d3de-6178-4f7e-b62c-7a96b1ae92a7.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>接着，在注册表中进入到以下路径：</p>
<p>计算机\HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows</p>
<p>用右键点击“Windows”，选择“新建”。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211122/9afaca4a-8fe9-40e3-b232-2b4e0b439af0.jpg" target="_blank"><img alt="继承Win10缺点！教你关闭Win11烦人的网络搜索" h="444" src="https://img1.mydrivers.com/img/20211122/S9afaca4a-8fe9-40e3-b232-2b4e0b439af0.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>新建一个名为“Explorer”的项，按下回车键。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211122/5b46405e-bbdb-4bcf-a194-53af757976e6.png" target="_blank"><img alt="继承Win10缺点！教你关闭Win11烦人的网络搜索" h="444" src="https://img1.mydrivers.com/img/20211122/S5b46405e-bbdb-4bcf-a194-53af757976e6.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>然后，右键点击Explorer的项，新建一个DWORD(32位)值。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211122/449dd659-9406-4734-ae36-eb80a7e1d3bd.jpg" target="_blank"><img alt="继承Win10缺点！教你关闭Win11烦人的网络搜索" h="444" src="https://img1.mydrivers.com/img/20211122/S449dd659-9406-4734-ae36-eb80a7e1d3bd.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>将新建的值命名为“DisableSearchBoxSuggestions”，然后按下回车键。如此一来，就可以控制是否开关网络搜索了。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211122/0d36df7c-7073-4f81-b782-851c85fb652f.png" target="_blank"><img alt="继承Win10缺点！教你关闭Win11烦人的网络搜索" h="444" src="https://img1.mydrivers.com/img/20211122/S0d36df7c-7073-4f81-b782-851c85fb652f.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>到了这里，要关闭Win11的网络搜索就很简单。双击刚才的DisableSearchBoxSuggestions值，然后将其赋值为“1”。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211122/2aa4fa41-6c01-4ae4-8497-c3bc8e3a50cd.png" target="_blank"><img alt="继承Win10缺点！教你关闭Win11烦人的网络搜索" h="444" src="https://img1.mydrivers.com/img/20211122/S2aa4fa41-6c01-4ae4-8497-c3bc8e3a50cd.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>接着保存注册表，重启电脑，再次打开系统搜索，就可以发现已经不会搜出网络结果了！</p>
<p>总的来说，Win10乃至Win11的系统搜索强推Bing引擎，而且没有关闭选项，这困扰了不少用户。如果你也遭遇了这个问题，可以尝试上文的方法。也希望微软能够为用户提供更灵活的选择，带来更好的体验吧。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20211122/b464b65ec0594c6d9da3d9ebffd60f6b.jpg" target="_blank"><img alt="继承Win10缺点！教你关闭Win11烦人的网络搜索" h="337" src="https://img1.mydrivers.com/img/20211122/s_b464b65ec0594c6d9da3d9ebffd60f6b.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/windowscaozuoxitong.htm"><i>#</i>Windows操作系统</a><a href="https://news.mydrivers.com/tag/windows_10.htm"><i>#</i>Windows 10</a></p>
<p class="url">
     <span>原文链接：<a href="https://www.pconline.com.cn/win11/1470/14702690.html#ad=8386">太平洋电脑网</a></span>
<span>责任编辑：振亭</span>
</p>
        
</div>
            