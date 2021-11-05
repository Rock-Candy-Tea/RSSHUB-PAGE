
---
title: 'Win11上清除TPM之后还能使用吗？实测来了：影响不大'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211105/aa884db0-0122-4589-a8ff-a69c7defbf4f.jpg'
author: 快科技（原驱动之家）
comments: false
date: Fri, 05 Nov 2021 21:39:14 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211105/aa884db0-0122-4589-a8ff-a69c7defbf4f.jpg'
---

<div>   
<p class="MsoNormal">在<span lang="EN-US">Win11</span>系统上，微软在安全性上有个让很多人不理解的要求，那就是必须要有<span lang="EN-US">TPM</span>才能安装——我们现在都知道<span lang="EN-US">TPM</span>可以轻松绕过，有太多工具都可以禁止<span lang="EN-US">TPM</span>要求。现在问题来了，开启<span lang="EN-US">TPM</span>对<span lang="EN-US">Win11</span>的安全登录到底有多大影响？</p>
<p class="MsoNormal">日本同行<span lang="EN-US">PCWatch</span>针对这个问题做了验证，它们在虚拟机上安装了<span lang="EN-US">Win11</span>系统，先是开启<span lang="EN-US">TPM</span>，然后再禁用它，或者是直接清除<span lang="EN-US">TPM</span>，看看会有什么不同。</p>
<p class="MsoNormal">为了这个测试，它们开启了仅允许使用<span lang="EN-US">Windows Hello</span>登录账户的设置，默认不直接使用账号和密码。</p>
<p class="MsoNormal">验证的情况比较多，一点点来说：</p>
<p class="MsoNormal">首先是开启<span lang="EN-US">TPM</span>之后再关闭该功能，<span style="color:#ff0000;"><strong>那么在登录界面会被提示无法识别<span lang="EN-US">PIN</span>码，要求用户重新设置<span lang="EN-US">TPM</span>，不重置的话，可以用账号密码来登录。</strong></span></p>
<p class="MsoNormal">注意一点，如果这时候选择了重置<span lang="EN-US">PIN</span>码，那设置的就是无<span lang="EN-US">TPM</span>时的<span lang="EN-US">PIN</span>码，信息是储存在软件而非<span lang="EN-US">TPM</span>硬件中的，二者不是一回事。</p>
<p class="MsoNormal">第二个验证是开启<span lang="EN-US">TPM</span>，然后关闭，之后再开启<span lang="EN-US">TPM</span>，<strong>那么之前不让<span lang="EN-US">PIN</span>码登录的<span lang="EN-US">Win11</span>账号可以正常使用了，不受影响。</strong></p>
<p class="MsoNormal">第三种情况是<span lang="EN-US">TPM</span>默认开启，不做改变，但是要清除<span lang="EN-US">TPM</span>信息，可以在<span lang="EN-US">BIOS</span>或者软件中操作。</p>
<p class="MsoNormal">在这种情况下，<span lang="EN-US">PIN</span>码是无法使用的，<strong>只能重置，而重置的过程需要验证账户和密码，完成之后就可以继续用新的<span lang="EN-US">PIN</span>码了。</strong></p>
<p class="MsoNormal">看完这个过程，总体感觉来说就是<span lang="EN-US">TPM</span>虽然有点用，但它在<span lang="EN-US">Win11</span>中似乎并不是不可缺少的，关闭或者清除<span lang="EN-US">TPM</span>之后只要重置就好了，黑客如果能拿到系统的账号和密码，<span lang="EN-US">TPM</span>也阻止不了它们登录系统。</p>

<p class="MsoNormal" style="text-align: center;"><img alt="Win11上清除TPM之后还能使用吗？实测来了：影响不大" h="337" src="https://img1.mydrivers.com/img/20211105/aa884db0-0122-4589-a8ff-a69c7defbf4f.jpg" style="text-align: center; border: 1px solid black;" w="600" referrerpolicy="no-referrer"></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/weiruan.htm"><i>#</i>微软</a><a href="https://news.mydrivers.com/tag/windowscaozuoxitong.htm"><i>#</i>Windows操作系统</a><a href="https://news.mydrivers.com/tag/windows_11.htm"><i>#</i>Windows 11</a><a href="https://news.mydrivers.com/tag/tpm.htm"><i>#</i>TPM</a></p>
<p class="url">
     
<span>责任编辑：宪瑞</span>
</p>
        
</div>
            